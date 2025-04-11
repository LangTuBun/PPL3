# StaticCheck.py

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *  # Use only Undeclared, Redeclared, TypeMismatch
from functools import reduce
from collections import defaultdict


# --- MType, Symbol Classes (Keep as before) ---
class MType:
    def __init__(self, partype, rettype):
        self.partype, self.rettype = partype, rettype

    def __str__(self):
        return f"MType([{','.join(map(str, self.partype))}],{self.rettype})"


class Symbol:
    def __init__(self, name, mtype, value=None, kind=None):
        self.name, self.mtype, self.value, self.kind = name, mtype, value, kind

    def __str__(self):
        kind_str = (
            f",{self.kind}"
            if isinstance(self.kind, Kind)
            else (f",{self.kind.__class__.__name__}" if self.kind else "")
        )
        val_str = f",{self.value}" if self.value is not None else ""
        mtype_str = str(self.mtype) if self.mtype else "None"
        return f"Symbol({self.name},{mtype_str}{val_str}{kind_str})"


INT_TYPE, FLOAT_TYPE, BOOL_TYPE, STRING_TYPE, VOID_TYPE, NIL_TYPE = (
    IntType(),
    FloatType(),
    BoolType(),
    StringType(),
    VoidType(),
    NilLiteral(),
)

# Global type environment (cleared on each check)
_global_type_env = {}


# --- Helper Functions ---
def resolve_type_node(type_node_or_id):
    """Resolves Ids to actual Type nodes using _global_type_env."""
    if isinstance(type_node_or_id, Id):
        type_name_str = type_node_or_id.name
        resolved = _global_type_env.get(type_name_str)
        if resolved is None:
            raise Undeclared(Type(), type_name_str)
        return resolved
    return type_node_or_id


def types_equivalent(type1, type2):
    """Checks if two resolved types are equivalent."""
    t1, t2 = (
        resolve_type_node(type1) if type1 else None,
        resolve_type_node(type2) if type2 else None,
    )
    
    if t1 is None or t2 is None:
        return t1 is t2
    if type(t1) is not type(t2):
        return False
    if isinstance(t1, ArrayType):
        
        if t1.dimens != t2.dimens:
            
            return False
        # TODO: Deep dimension value check might be needed if dims are constants
        return types_equivalent(t1.eleType, t2.eleType)
    if isinstance(t1, (StructType, InterfaceType)):
        return t1.name == t2.name  # Compare name string
    if isinstance(t1, MType):
        if len(t1.partype) != len(t2.partype):
            return False
        if not all(types_equivalent(p1, p2) for p1, p2 in zip(t1.partype, t2.partype)):
            return False
        return types_equivalent(t1.rettype, t2.rettype)
    return True  # Basic types, NilLiteral




    # Helper to check struct implements interface - uses resolved types



# Custom lookup for methods - uses global scope
def lookup_method_global(method_name, receiver_type_name_str, global_scope):
    for symbol in global_scope:
        if symbol.name == method_name and isinstance(symbol.kind, Method):
            method_decl_node = symbol.value  # Assumes MethodDecl stored in value
            if method_decl_node and isinstance(method_decl_node, MethodDecl):
                rec_type_node = method_decl_node.recType
                try:
                    resolved_rec_type = resolve_type_node(rec_type_node)
                    if (
                        isinstance(resolved_rec_type, (StructType, InterfaceType))
                        and resolved_rec_type.name == receiver_type_name_str
                    ):
                        return symbol
                except Undeclared:
                    continue
    return None


class StaticChecker(BaseVisitor, Utils):
    def predeclare(self, decl, context):
        if isinstance(decl, StructType) or isinstance(decl, InterfaceType):
            type_name = decl.name
            if type_name in self.type_env or self.lookup(type_name, context[-1], lambda s: s.name):
                raise Redeclared(Type(), type_name)
            self.type_env[type_name] = decl
            context[-1].insert(0, Symbol(type_name, decl, kind=Type()))

        elif isinstance(decl, FuncDecl):
            func_name = decl.name
            if func_name in self.type_env or self.lookup(func_name, context[-1], lambda s: s.name):
                raise Redeclared(Function(), func_name)
            func_type = MType([p.parType for p in decl.params], decl.retType)
            context[-1].insert(0, Symbol(func_name, func_type, kind=Function()))

        elif isinstance(decl, ConstDecl):
            const_name = decl.conName
            if const_name in self.type_env or self.lookup(const_name, context[-1], lambda s: s.name):
                raise Redeclared(Constant(), const_name)
            # Type will be resolved later
            context[-1].insert(0, Symbol(const_name, None, kind=Constant()))

        elif isinstance(decl, VarDecl):
            var_name = decl.varName
            if var_name in self.type_env or self.lookup(var_name, context[-1], lambda s: s.name):
                raise Redeclared(Variable(), var_name)
            context[-1].insert(0, Symbol(var_name, None, kind=Variable()))

    def __init__(self, ast):
        self.ast = ast
        self.duplicate_type_names = set()
        self.method_registry = {}
        global _global_type_env
        _global_type_env = {
            "int": INT_TYPE,
            "float": FLOAT_TYPE,
            "boolean": BOOL_TYPE,
            "string": STRING_TYPE,
        }
        self.global_envi = [
            [
                Symbol("getInt", MType([], INT_TYPE), kind=Function()),
                Symbol("putIntLn", MType([INT_TYPE], VOID_TYPE), kind=Function()),
                Symbol("putInt", MType([INT_TYPE], VOID_TYPE), kind=Function()),
                Symbol("getFloat", MType([], FLOAT_TYPE), kind=Function()),
                Symbol("putFloatLn", MType([FLOAT_TYPE], VOID_TYPE), kind=Function()),
                Symbol("putStringLn", MType([STRING_TYPE], VOID_TYPE), kind=Function()),
                Symbol("putString", MType([STRING_TYPE], VOID_TYPE), kind=Function()),
                Symbol("getString", MType([], STRING_TYPE), kind=Function()),
                Symbol("putBoolLn", MType([BOOL_TYPE], VOID_TYPE), kind=Function()),
                Symbol("getBool", MType([], BOOL_TYPE), kind=Function()),
            ]
        ]
        self.current_function_ret_type = None
        self.is_in_loop = False  # Boolean flag is sufficient

    def check(self):
        # Reset type env for fresh check
        self.type_env = {
            "int": INT_TYPE,
            "float": FLOAT_TYPE,
            "boolean": BOOL_TYPE,
            "string": STRING_TYPE,
        }
        # Populate _global_type_env using self.type_env
        global _global_type_env
        _global_type_env = self.type_env.copy()
        # Start visit
        return self.visit(self.ast, self.global_envi)

    # --- lookup_symbol METHOD needed by visitAssign etc. ---
    def lookup_symbol(self, name, env, kind_filter_class=None):
        """Searches for a symbol name through nested scopes (env list)."""
        for scope in env:  # env is [[inner], [outer], ...]
            found = self.lookup(
                name, scope, lambda s: s.name
            )  # Use Utils.lookup on current scope
            if found:
                if kind_filter_class is None or isinstance(
                    found.kind, kind_filter_class
                ):
                    return found
                else:
                    return None  # Found name but wrong kind
        return None  # Not found in any scope
    def _resolve_type_node(self, type_node_or_id):
        if isinstance(type_node_or_id, Id):
            type_name_str = type_node_or_id.name
            # Use the instance's type_env
            resolved = self.type_env.get(type_name_str)
            if resolved is None:
                raise Undeclared(Type(), type_name_str)
            return resolved
        # Handle resolving internal types if needed (e.g., Array element type)
        elif isinstance(type_node_or_id, ArrayType):
            try:
                resolved_ele = self._resolve_type_node(type_node_or_id.eleType)
                return ArrayType(type_node_or_id.dimens, resolved_ele)
            except Undeclared as e:
                raise e  # Propagate if element type is undeclared
        elif isinstance(type_node_or_id, MType):
            try:
                resolved_parts = [
                    self._resolve_type_node(p) for p in type_node_or_id.partype
                ]
                resolved_ret = self._resolve_type_node(type_node_or_id.rettype)
                return MType(resolved_parts, resolved_ret)
            except Undeclared as e:
                raise e
        return type_node_or_id  

    # --- Helper to check if a type exists ---
    def _check_type_exists(self, type_node_or_id):
        # This just attempts resolution, which raises Undeclared if not found
        self._resolve_type_node(type_node_or_id)
        return True  # No exception means it exists
    def check_struct_implements_interface(self, struct_type, interface_type):
        # 1. Sanity check the types
        if not isinstance(struct_type, StructType) or not isinstance(interface_type, InterfaceType):
            return False

        struct_type_name = struct_type.name

        for proto in interface_type.methods:
            method_found = False
            for scope in self.global_envi:
                for symbol in scope:
                    if (
                        symbol.name == proto.name and
                        isinstance(symbol.kind, Method) and
                        hasattr(symbol.value, "recType")
                    ):
                        try:
                            rec_type = self._resolve_type_node(symbol.value.recType)
                            if isinstance(rec_type, StructType) and rec_type.name == struct_type_name:
                                # Check return type
                                method_type = symbol.mtype
                                proto_ret = self._resolve_type_node(proto.retType)
                                meth_ret = self._resolve_type_node(method_type.rettype)
                                if not self.checkTypeCompatibility(proto_ret, meth_ret):
                                    continue

                                # Check parameter count and types
                                if len(proto.params) != len(method_type.partype):
                                    continue
                                all_match = True
                                for p_proto, p_meth in zip(proto.params, method_type.partype):
                                    resolved_proto = self._resolve_type_node(p_proto)
                                    resolved_meth = self._resolve_type_node(p_meth)
                                    if not self.checkTypeCompatibility(resolved_proto, resolved_meth):
                                        all_match = False
                                        break
                                if all_match:
                                    method_found = True
                                    break
                        except Undeclared:
                            continue
                if method_found:
                    break
            if not method_found:
                return False

        return True

    # --- checkTypeCompatibility (Use robust version) ---
    def checkTypeCompatibility(self, lhs_type, rhs_type):
        lhs_resolved = self._resolve_type_node(lhs_type) if lhs_type else None
        rhs_resolved = self._resolve_type_node(rhs_type) if rhs_type else None

        if isinstance(lhs_resolved, VoidType) or isinstance(rhs_resolved, VoidType):
            return False
        if lhs_resolved is None or rhs_resolved is None:
            return False

        if types_equivalent(lhs_resolved, rhs_resolved):
            return True
        if isinstance(lhs_resolved, FloatType) and isinstance(rhs_resolved, IntType):
            return True
        if isinstance(lhs_resolved, ArrayType) and isinstance(rhs_resolved, ArrayType):
            if lhs_resolved.dimens == rhs_resolved.dimens:
                return self.checkTypeCompatibility(lhs_resolved.eleType, rhs_resolved.eleType)
            return False
        if isinstance(lhs_resolved, InterfaceType) and isinstance(rhs_resolved, StructType):
            return self.check_struct_implements_interface(rhs_resolved, lhs_resolved)
        if isinstance(rhs_resolved, NilLiteral):
            if isinstance(lhs_resolved, InterfaceType):
                return True
            return False
        return False


    # --- Visitor Methods ---

    def visitProgram(self, ast: Program, context):
        seen_type_names = set()
        self.duplicate_type_names = set()

        # First pass — Predeclare all types, constants, variables, and functions
        for decl in ast.decl:
            # --- Type predeclaration (structs + interfaces) ---
            if isinstance(decl, (StructType, InterfaceType)):
                type_name = decl.name
                self.type_env[type_name] = decl
                if type_name in seen_type_names:
                    self.duplicate_type_names.add(type_name)
                else:
                    seen_type_names.add(type_name)

            # --- Constant / Variable predeclaration with conflict check ---
            elif isinstance(decl, (ConstDecl, VarDecl)):
                name = decl.conName if isinstance(decl, ConstDecl) else decl.varName
                kind = Constant() if isinstance(decl, ConstDecl) else Variable()

                # Check for name conflict in global scope
                if self.lookup(name, context[-1], lambda s: s.name):
                    raise Redeclared(kind, name)

                context[-1].insert(0, Symbol(name, None, kind=kind))  # Predeclare with empty type

            # --- Function predeclaration with conflict check ---
            elif isinstance(decl, FuncDecl):
                name = decl.name
                if self.lookup(name, context[-1], lambda s: s.name):
                    raise Redeclared(Function(), name)

                param_types = [param.parType for param in decl.params]
                ret_type = decl.retType
                func_type = MType(param_types, ret_type)
                context[-1].insert(0, Symbol(name, func_type, kind=Function()))

        # Second pass — visit each declaration
        for decl in ast.decl:
            self.visit(decl, context)

        return context




    def visitStructType(self, ast: StructType, context):
        # Raise Redeclared(Type) if the name was seen twice
        if ast.name in self.duplicate_type_names:
            raise Redeclared(Type(), ast.name)

        # Check for name conflict in global scope (with const/var/func)
        if self.lookup(ast.name, context[-1], lambda s: s.name):
            raise Redeclared(Type(), ast.name)

        field_names = set()
        if hasattr(ast, "elements") and isinstance(ast.elements, list):
            for element in ast.elements:
                if isinstance(element, tuple) and len(element) == 2:
                    field_name, field_type_node = element
                    if field_name in field_names:
                        raise Redeclared(Field(), field_name)
                    field_names.add(field_name)
                    try:
                        resolved_type = self._resolve_type_node(field_type_node)
                        if isinstance(resolved_type, VoidType):
                            raise TypeMismatch(ast)
                    except Undeclared as e:
                        raise e

        # Add to global scope (for method/interface lookup)
        context[-1].insert(0, Symbol(ast.name, ast, kind=Type()))
        return context


    def visitInterfaceType(self, ast: InterfaceType, context):
        # Raise Redeclared(Type) if name was duplicated
        if ast.name in self.duplicate_type_names:
            raise Redeclared(Type(), ast.name)

        # Check for name conflict in global scope (with const/var/func)
        if self.lookup(ast.name, context[-1], lambda s: s.name):
            raise Redeclared(Type(), ast.name)

        # Check prototype names (methods)
        prototype_names = set()
        if hasattr(ast, "methods") and isinstance(ast.methods, list):
            for proto in ast.methods:
                if proto.name in prototype_names:
                    raise Redeclared(Prototype(), proto.name)
                prototype_names.add(proto.name)
                self.visit(proto, context)

        # Add to global scope for interface resolution
        context[-1].insert(0, Symbol(ast.name, ast, kind=Type()))
        return context

    def visitPrototype(self, ast: Prototype, context):
        try:
            for p_type_node in ast.params:
                resolved = self._resolve_type_node(p_type_node)
                if isinstance(resolved, VoidType):
                    raise TypeMismatch(ast)
            self._resolve_type_node(ast.retType)
        except Undeclared as e:
            raise e
        return context

    def visitVarDecl(self, ast: VarDecl, context):
        # print("Visiting VarDecl")
        current_scope = context[0]
        var_name = ast.varName

        symbol = self.lookup(var_name, current_scope, lambda s: s.name)

        if symbol:
            if isinstance(symbol.kind, Variable):
                if symbol.mtype is not None:
                    raise Redeclared(Variable(), var_name)
            else:
                raise Redeclared(Variable(), var_name)
        else:
            # New local variable
            symbol = Symbol(var_name, None, kind=Variable())
            current_scope.insert(0, symbol)

        declared_type = ast.varType
        resolved_rhs_type = None

        if ast.varInit:
            rhs_type = self.visit(ast.varInit, context)
            resolved_rhs_type = self._resolve_type_node(rhs_type)
            if isinstance(resolved_rhs_type, VoidType):
                raise TypeMismatch(ast.varInit)

        if declared_type:
            resolved_decl_type = self._resolve_type_node(declared_type)
            if resolved_rhs_type and not self.checkTypeCompatibility(resolved_decl_type, resolved_rhs_type):
                raise TypeMismatch(ast)
            final_var_type = resolved_decl_type
        elif resolved_rhs_type:
            final_var_type = resolved_rhs_type
        else:
            raise StaticError("Variable needs type or initializer: " + var_name)

        if isinstance(final_var_type, VoidType):
            raise TypeMismatch(ast)

        symbol.mtype = final_var_type  # 🧠 Update the symbol in-place
        return context

    def visitConstDecl(self, ast, context): 

        current_scope = context[0]
        const_name = ast.conName
        if const_name in self.type_env:
            raise Redeclared(Constant(), const_name)

        # Look up symbol in current scope only
        symbol = self.lookup(const_name, current_scope, lambda s: s.name)

        if symbol:
            if not isinstance(symbol.kind, Constant):
                raise Redeclared(Constant(), const_name)
            if symbol.mtype is not None:
                raise Redeclared(Constant(), const_name)
        else:
            symbol = Symbol(const_name, None, kind=Constant())
            current_scope.insert(0, symbol)

        if not ast.iniExpr:
            raise StaticError("Constant needs initializer: " + const_name)

        # Evaluate RHS
        rhs_type = self.visit(ast.iniExpr, context)
        resolved_rhs_type = self._resolve_type_node(rhs_type)
        if isinstance(resolved_rhs_type, VoidType):
            raise TypeMismatch(ast.iniExpr)

        # Evaluate declared type if present
        declared_type = ast.conType
        if declared_type:
            resolved_declared_type = self._resolve_type_node(declared_type)
            if not self.checkTypeCompatibility(resolved_declared_type, resolved_rhs_type):
                raise TypeMismatch(ast)
            final_type = resolved_declared_type
        else:
            final_type = resolved_rhs_type

        if isinstance(final_type, VoidType):
            raise TypeMismatch(ast)

        # Update predeclared symbol
        symbol.mtype = final_type
        symbol.value = ast.iniExpr

        return context

    
    
    def visitFuncDecl(self, ast: FuncDecl, context):
        func_name = ast.name
        if self.lookup(
            func_name, context[0], lambda s: s.name 
        ):
            raise Redeclared(Function(), func_name)
        try:
            param_types = [p.parType for p in ast.params]
            [self._check_type_exists(pt) for pt in param_types]
            self._check_type_exists(ast.retType)
        except Undeclared as e:
            raise e
        func_mtype = MType(param_types, ast.retType)
        func_symbol = Symbol(func_name, func_mtype, kind=Function())
        updated_global_scope = [func_symbol] + context[0]
        outer_context = context[1:]
        o_ret, o_loop = self.current_function_ret_type, self.is_in_loop
        try:
            self.current_function_ret_type = self._resolve_type_node(ast.retType)
        except Undeclared as e:
            raise e
        self.is_in_loop = False
        local_scope = []
        fn_ctx = [local_scope] + [updated_global_scope] + outer_context
        param_names = set()
        try:
            for param in ast.params:
                if param.parName in param_names:
                    raise Redeclared(Parameter(), param.parName)
                param_names.add(param.parName)
                res_param_type = self._resolve_type_node(param.parType)
                if isinstance(res_param_type, VoidType):
                    raise TypeMismatch(param)
                param_sym = Symbol(param.parName, res_param_type, kind=Parameter())
                local_scope.insert(0, param_sym)
        except Undeclared as e:
            raise e
            
        # Initialize return error tracking
        self.return_error = None
        
        if ast.body:
            self.visit(ast.body, fn_ctx)
            
        # Check if there was a return type error
        if self.return_error is not None:
            raise TypeMismatch(ast)  # Raise error on the FuncDecl instead of the Return
            
        self.current_function_ret_type, self.is_in_loop = o_ret, o_loop
        return [updated_global_scope] + outer_context

    
        
    def visitFuncDecl(self, ast: FuncDecl, context):
        func_name = ast.name

        # Retrieve the symbol predeclared in the global scope
        symbol = self.lookup(func_name, context[-1], lambda s: s.name)
        if not symbol or not isinstance(symbol.kind, Function):
            raise StaticError("Function not predeclared or wrong kind")

        # Ensure declared types exist
        param_types = [param.parType for param in ast.params]
        for t in param_types:
            self._check_type_exists(t)
        self._check_type_exists(ast.retType)

        # Save return type + loop status
        prev_ret, prev_loop = self.current_function_ret_type, self.is_in_loop
        self.current_function_ret_type = self._resolve_type_node(ast.retType)
        self.is_in_loop = False

        # Set up scopes
        local_scope = []
        param_names = set()

        for param in ast.params:
            if param.parName in param_names:
                raise Redeclared(Parameter(), param.parName)
            param_names.add(param.parName)

            param_type = self._resolve_type_node(param.parType)
            if isinstance(param_type, VoidType):
                raise TypeMismatch(param)
            param_symbol = Symbol(param.parName, param_type, kind=Parameter())
            local_scope.insert(0, param_symbol)

        full_context = [local_scope] + context

        # Init return tracking
        self.return_error = None
        if ast.body:
            self.visit(ast.body, full_context)

        if self.return_error is not None:
            raise TypeMismatch(ast)

        # Restore outer state
        self.current_function_ret_type, self.is_in_loop = prev_ret, prev_loop
        return context


    def visitMethodDecl(self, ast: MethodDecl, context):
        method_name, receiver_type_id, receiver_name = (
            ast.fun.name,
            ast.recType,
            ast.receiver,
        )

        try:
            resolved_receiver_type = self._resolve_type_node(receiver_type_id)

            if not isinstance(resolved_receiver_type, (StructType, InterfaceType)):
                raise TypeMismatch(ast)

            receiver_type_name_str = resolved_receiver_type.name  # Use name string
        except Undeclared as e:
            raise e

        # Check for name collision with struct fields
        if isinstance(resolved_receiver_type, StructType) and hasattr(resolved_receiver_type, "elements"):
            for field_name, _ in resolved_receiver_type.elements:
                if field_name == method_name:
                    raise Redeclared(Method(), method_name)

        # Check method registry with combined key (struct_name, method_name)
        registry_key = (receiver_type_name_str, method_name)
        if registry_key in self.method_registry:
            raise Redeclared(Method(), method_name)
        self.method_registry[registry_key] = ast

        # Resolve and check parameter/return types
        try:
            param_types = [p.parType for p in ast.fun.params]
            [self._check_type_exists(pt) for pt in param_types]
            self._check_type_exists(ast.fun.retType)
        except Undeclared as e:
            raise e

        # Create method symbol and insert into global scope
        method_mtype = MType(param_types, ast.fun.retType)
        method_symbol = Symbol(
            method_name, method_mtype, kind=Method(), value=ast
        )
        context[0].insert(0, method_symbol)  # Insert into current/global scope

        # Set up method context
        o_ret, o_loop = self.current_function_ret_type, self.is_in_loop
        self.current_function_ret_type = self._resolve_type_node(ast.fun.retType)
        self.is_in_loop = False

        local_scope = []

        # Add receiver as a variable to local scope
        if self.lookup(receiver_name, local_scope, lambda s: s.name):
            raise Redeclared(Variable(), receiver_name)
        receiver_symbol = Symbol(receiver_name, resolved_receiver_type, kind=Variable())
        local_scope.insert(0, receiver_symbol)

        # Add parameters to local scope
        param_names = set([receiver_name])
        for param in ast.fun.params:
            if param.parName in param_names:
                raise Redeclared(Parameter(), param.parName)
            param_names.add(param.parName)

            res_param_type = self._resolve_type_node(param.parType)
            if isinstance(res_param_type, VoidType):
                raise TypeMismatch(param)
            param_sym = Symbol(param.parName, res_param_type, kind=Parameter())
            local_scope.insert(0, param_sym)

        # Visit method body
        method_body_context = [local_scope] + context
        if ast.fun.body:
            self.visit(ast.fun.body, method_body_context)

        self.current_function_ret_type, self.is_in_loop = o_ret, o_loop
        return context
    # visitBlock, Id, Assign, If, For*, Break, Continue, Return, Ops, Calls, Access, Literals
    def visitBlock(self, ast: Block, context):
        # Create a new scope for this block
        block_scope = []
        block_context = [block_scope] + context # New context stack

        current_block_internal_context = block_context
        if ast.member:
            for member in ast.member:
                if isinstance(member, (FuncCall, MethCall)):
                    # If the member is a Call used as a statement, check its return type
                    # Pass the block's context down for the call check
                    return_type = self.visit(member, current_block_internal_context)
                    resolved_return_type = self._resolve_type_node(return_type) if return_type else None

                    # *** THE CHECK: Non-void call used as statement is an error ***
                    if not isinstance(resolved_return_type, VoidType):
                        raise TypeMismatch(member)
                
                else:
                    current_block_internal_context = self.visit(member, current_block_internal_context)

        return context


    def visitIf(self, ast: If, context): 
        expr_visit_type = self.visit(ast.expr, context) 

        resolved_expr_type = self._resolve_type_node(expr_visit_type)

        if not isinstance(resolved_expr_type, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, context) # Pass outer context

        if ast.elseStmt:
             self.visit(ast.elseStmt, context) # Pass outer context

        return context
    def visitId(self, ast: Id, context):
        ident_name = ast.name
        symbol = None
        symbol = self.lookup_symbol(ident_name, context)
        if not symbol:
            raise Undeclared(Identifier(), ident_name)
        return symbol.mtype
    def is_valid_lvalue(self, expr):
        return isinstance(expr, (Id, ArrayCell, FieldAccess))


    def visitAssign(self, ast: Assign, context): 
        lhs_node = ast.lhs

        if not self.is_valid_lvalue(lhs_node):
            raise TypeMismatch(ast)

        rhs_type = self.visit(ast.rhs, context)
        resolved_rhs_type = self._resolve_type_node(rhs_type) if rhs_type else None

        if resolved_rhs_type is None or isinstance(resolved_rhs_type, VoidType):
            raise TypeMismatch(ast.rhs)

        if isinstance(lhs_node, Id):
            lhs_name = lhs_node.name
            current_scope = context[0]

            symbol = self.lookup(lhs_name, current_scope, lambda s: s.name)
            if symbol:
                if not isinstance(symbol.kind, (Variable, Parameter)) or isinstance(symbol.kind, Constant):
                    raise TypeMismatch(ast)
                resolved_lhs_type = self._resolve_type_node(symbol.mtype)
                if isinstance(resolved_lhs_type, VoidType):
                    raise TypeMismatch(ast)
                if not self.checkTypeCompatibility(resolved_lhs_type, resolved_rhs_type):
                    raise TypeMismatch(ast)
                return context  # Valid assignment to existing var

            outer_symbol = self.lookup_symbol(lhs_name, context[1:])
            if outer_symbol:
                if not isinstance(outer_symbol.kind, (Variable, Parameter)) or isinstance(outer_symbol.kind, Constant):
                    raise TypeMismatch(ast)
                resolved_lhs_type = self._resolve_type_node(outer_symbol.mtype)
                if isinstance(resolved_lhs_type, VoidType):
                    raise TypeMismatch(ast)
                if not self.checkTypeCompatibility(resolved_lhs_type, resolved_rhs_type):
                    raise TypeMismatch(ast)
                return context  # Valid assignment to outer var

            if isinstance(resolved_rhs_type, VoidType):
                raise TypeMismatch(ast)
            new_symbol = Symbol(lhs_name, resolved_rhs_type, kind=Variable())
            updated_scope = [new_symbol] + current_scope
            return [updated_scope] + context[1:]

        elif isinstance(lhs_node, (ArrayCell, FieldAccess)):
            lhs_type = self.visit(lhs_node, context)
            resolved_lhs_type = self._resolve_type_node(lhs_type) if lhs_type else None
            if resolved_lhs_type is None or isinstance(resolved_lhs_type, VoidType):
                raise TypeMismatch(ast)
            if not self.checkTypeCompatibility(resolved_lhs_type, resolved_rhs_type):
                raise TypeMismatch(ast)
            return context

        raise TypeMismatch(ast)

        
    def visitForBasic(self, ast: ForBasic, context):
        cond_type = self._resolve_type_node(self.visit(ast.cond, context))
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)

        outer_loop_status = self.is_in_loop
        self.is_in_loop = True

        try:
            loop_scope = []
            loop_context = [loop_scope] + context
            self.visit(ast.loop, loop_context)
        finally:
            self.is_in_loop = outer_loop_status

        return context



    def visitForStep(self, ast: ForStep, context): # context = outer context
        loop_scope = []
        loop_context = [loop_scope] + context # [[loop], [outer], ...]

        context_after_init = self.visit(ast.init, loop_context) if ast.init else loop_context

        cond_type = BOOL_TYPE
        if ast.cond:
            cond_visit_type = self.visit(ast.cond, context_after_init)
            cond_type = self._resolve_type_node(cond_visit_type)
            if not isinstance(cond_type, BoolType): raise TypeMismatch(ast)

        if ast.upda:
            self.visit(ast.upda, context_after_init)
        outer_loop_status = self.is_in_loop
        self.is_in_loop = True
        current_loop_body_context = context_after_init 
        if ast.loop and ast.loop.member: 
             for member in ast.loop.member:
                  current_loop_body_context = self.visit(member, current_loop_body_context)
        self.is_in_loop = outer_loop_status

        return context


    def visitForEach(self, ast: ForEach, context):
        # 1. Visit and validate array expression
        arr_visit_type = self.visit(ast.arr, context)
        arr_type = self._resolve_type_node(arr_visit_type)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)

        loop_scope = context[0].copy()
        loop_context = [loop_scope] + context[1:]

        idx_name = ast.idx.name
        if self.lookup(idx_name, loop_scope, lambda s: s.name):
            raise Redeclared(Variable(), idx_name)
        idx_symbol = Symbol(idx_name, INT_TYPE, kind=Variable())
        loop_scope.insert(0, idx_symbol)

        val_name = ast.value.name
        if val_name != "_":
            if self.lookup(val_name, loop_scope, lambda s: s.name):
                raise Redeclared(Variable(), val_name)
            resolved_ele_type = self._resolve_type_node(arr_type.eleType)
            val_symbol = Symbol(val_name, resolved_ele_type, kind=Variable())
            loop_scope.insert(0, val_symbol)

        outer_loop_status = self.is_in_loop
        self.is_in_loop = True
        try:
            if ast.loop and ast.loop.member:
                for member in ast.loop.member:
                    loop_context = self.visit(member, loop_context)
        finally:
            self.is_in_loop = outer_loop_status

        # 6. Return the original outer context
        return context


    def visitBreak(self, ast: Break, context):
        if not self.is_in_loop:
            raise TypeMismatch(ast)
            return context

    def visitContinue(self, ast: Continue, context):
        if not self.is_in_loop:
            raise TypeMismatch(ast)
            return context

    def visitReturn(self, ast: Return, context):
        if self.current_function_ret_type is None:
            raise TypeMismatch(ast)
        expected = self.current_function_ret_type
 
        
        if ast.expr:
            actual_visit = self.visit(ast.expr, context)
            actual = self._resolve_type_node(actual_visit)
            if isinstance(actual, VoidType):
                raise TypeMismatch(ast.expr)
            if isinstance(expected, VoidType):
                # Store error info in a class attribute instead of raising
                self.return_error = ast
                return context
            if not self.checkTypeCompatibility(expected, actual):
                self.return_error = ast
                return context
        elif not isinstance(expected, VoidType):
      
            self.return_error = ast
            return context
        
        return context
    def visitBinaryOp(self, ast: BinaryOp, context):
        op = ast.op
        left_visit = self.visit(ast.left, context)
        right_visit = self.visit(ast.right, context)
        left = self._resolve_type_node(left_visit)
        right = self._resolve_type_node(right_visit)

        if isinstance(left, VoidType) or isinstance(right, VoidType):
            raise TypeMismatch(ast)

        if op == "+":
            if isinstance(left, StringType) and isinstance(right, StringType):
                return STRING_TYPE
            if isinstance(left, FloatType) and isinstance(right, (IntType, FloatType)):
                return FLOAT_TYPE
            if isinstance(left, IntType) and isinstance(right, FloatType):
                return FLOAT_TYPE
            if isinstance(left, IntType) and isinstance(right, IntType):
                return INT_TYPE
            raise TypeMismatch(ast)

        if op in ["-", "*", "/"]:
            if isinstance(left, FloatType) and isinstance(right, (IntType, FloatType)):
                return FLOAT_TYPE
            if isinstance(left, IntType) and isinstance(right, FloatType):
                return FLOAT_TYPE
            if isinstance(left, IntType) and isinstance(right, IntType):
                return INT_TYPE
            raise TypeMismatch(ast)

        if op == "%":
            if isinstance(left, IntType) and isinstance(right, IntType):
                return INT_TYPE
            raise TypeMismatch(ast)

        if op in ["&&", "||"]:
            if isinstance(left, BoolType) and isinstance(right, BoolType):
                return BOOL_TYPE
            raise TypeMismatch(ast)

        if op in ["<", "<=", ">", ">="]:
            if type(left) == type(right) and isinstance(left, (IntType, FloatType)):
                return BOOL_TYPE
            raise TypeMismatch(ast)


        if op in ["==", "!="]:
            can_compare = False
            if isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
                can_compare = True
            elif types_equivalent(left, right) and isinstance(left, (BoolType, StringType)):
                can_compare = True
            if not can_compare:
                raise TypeMismatch(ast)
            return BOOL_TYPE

        raise StaticError(f"Unhandled operator: {op}")


    def visitUnaryOp(self, ast: UnaryOp, context):
        op = ast.op
        body_visit = self.visit(ast.body, context)
        expr = self._resolve_type_node(body_visit)
        if isinstance(expr, VoidType):
            raise TypeMismatch(ast)
        if op == "!":
            if isinstance(expr, BoolType):
                return BOOL_TYPE
            raise TypeMismatch(ast)
        if op == "-":
            if isinstance(expr, (IntType, FloatType)):
                return expr
            raise TypeMismatch(ast)
        raise StaticError(f"Unhandled: {op}")

    def visitFuncCall(self, ast: FuncCall, context):
        # ast.name should be a string
        func_name = ast.funName

        symbol = self.lookup_symbol(func_name, context, Function)
        if not symbol:
            raise Undeclared(Function(), func_name)

        func_type = symbol.mtype
        if not isinstance(func_type, MType):
            raise TypeMismatch(ast)

        if len(ast.args) != len(func_type.partype):
            raise TypeMismatch(ast)

        for i in range(len(ast.args)):
            arg_type = self._resolve_type_node(self.visit(ast.args[i], context))
            param_type = self._resolve_type_node(func_type.partype[i])
            if not self.checkTypeCompatibility(param_type, arg_type):
                raise TypeMismatch(ast)

        return func_type.rettype



    def visitArrayCell(self, ast: ArrayCell, context):
        arr_type = self.visit(ast.arr, context)
        resolved_arr_type = self._resolve_type_node(arr_type)

        if not isinstance(resolved_arr_type, ArrayType):
            raise TypeMismatch(ast)

        if len(ast.idx) != len(resolved_arr_type.dimens):
            raise TypeMismatch(ast)

        for i, idx_expr in enumerate(ast.idx):
            index_type = self.visit(idx_expr, context)
            resolved_index_type = self._resolve_type_node(index_type)
            if not isinstance(resolved_index_type, IntType):
                raise TypeMismatch(ast)  # 👈 raise on whole ArrayCell instead

            # Optional: literal bound check
            index_expr_node = ast.idx[i]
            declared_dim_expr = resolved_arr_type.dimens[i]
            if isinstance(index_expr_node, IntLiteral) and isinstance(declared_dim_expr, IntLiteral):
                if index_expr_node.value >= declared_dim_expr.value:
                    raise TypeMismatch(ast)  # 👈 raise on full ArrayCell

        return resolved_arr_type.eleType

    def visitFieldAccess(self, ast: FieldAccess, context):
        rcv_visit = self.visit(ast.receiver, context)
        rcv_type = self._resolve_type_node(rcv_visit)
        if not isinstance(rcv_type, StructType):
            raise TypeMismatch(ast)
        field_name = ast.field
        found_type_node = None
        if hasattr(rcv_type, "elements"):
            for name, ftype_node in rcv_type.elements:
                if name == field_name:
                    found_type_node = ftype_node
                    break
        if found_type_node is None:
            raise Undeclared(Field(), field_name)
        return found_type_node

    def visitIntLiteral(self, ast, c):
        return INT_TYPE

    def visitFloatLiteral(self, ast, c):
        return FLOAT_TYPE

    def visitBooleanLiteral(self, ast, c):
        return BOOL_TYPE

    def visitStringLiteral(self, ast, c):
        return STRING_TYPE

    def visitNilLiteral(self, ast, c):
        return NIL_TYPE

    # Inside StaticChecker class

    def visitArrayLiteral(self, ast: ArrayLiteral, context): 
        resolved_element_types = []
        final_element_type = None
        struct_dims_values = []

        # --- Use ast.value ---
        literal_content = getattr(ast, 'value', None) # Safely get value attribute

        # 1. Determine Explicit Element Type (if provided)
        explicit_ele_type = None
        if hasattr(ast, 'eleType') and ast.eleType:
            try: explicit_ele_type = self._resolve_type_node(ast.eleType)
            except Undeclared as e: raise TypeMismatch(ast) from e
            if isinstance(explicit_ele_type, VoidType): raise TypeMismatch(ast)

        # 2. Determine Explicit Dimensions (if provided)
        explicit_dims = []
        if hasattr(ast, 'dimensions') and ast.dimensions:
             # ... (validation logic as before) ...
             for i, dim_expr in enumerate(ast.dimensions):
                  dim_visit_type = self.visit(dim_expr, context)
                  resolved_dim_type = self._resolve_type_node(dim_visit_type)
                  if not isinstance(resolved_dim_type, IntType): raise TypeMismatch(dim_expr)
                  explicit_dims.append(dim_expr)
             if not explicit_dims: raise StaticError("Explicit dimension list empty?")

        inferred_ele_type = None
        if literal_content is None: # Handles both missing attribute and explicit None
            if not explicit_ele_type or not explicit_dims: raise TypeMismatch(ast)
        else:
            try:
                inferred_ele_type, inferred_dims_values = self._check_nested_list(
                    literal_content, explicit_ele_type, context # Pass context list
                )
            except (TypeMismatch, StaticError) as e: raise TypeMismatch(ast) from e
            if inferred_ele_type is None: # Inference failed (e.g., only empty lists)
                 if not explicit_ele_type: raise TypeMismatch(ast)
                 else: inferred_ele_type = explicit_ele_type # Use explicit if inference failed
        if explicit_ele_type and inferred_ele_type:
            if not self.checkTypeCompatibility(explicit_ele_type, inferred_ele_type): raise TypeMismatch(ast)
            final_element_type = explicit_ele_type
        elif explicit_ele_type: final_element_type = explicit_ele_type
        elif inferred_ele_type: final_element_type = inferred_ele_type
        else: raise TypeMismatch(ast)

        final_dims = []
        if explicit_dims:
             if inferred_dims_values and len(explicit_dims) == 1 and isinstance(explicit_dims[0], IntLiteral) and len(inferred_dims_values) >= 1:
                  if explicit_dims[0].value != inferred_dims_values[0]: raise TypeMismatch(ast) # Size mismatch
             final_dims = explicit_dims
        elif inferred_dims_values: # Infer from structure
            final_dims = [IntLiteral(d) for d in inferred_dims_values]
        else:
             if not explicit_dims: raise TypeMismatch(ast)
             final_dims = explicit_dims # Use explicit if value was None/empty

        if not final_dims: raise StaticError("Array literal final dimensions undetermined")
        if not final_element_type: raise StaticError("Array literal final element type undetermined")

        return ArrayType(final_dims, final_element_type)


    def _check_nested_list(self, data, explicit_ele_type, context):
        if isinstance(data, Id):
            raise TypeMismatch(data) 

        if not isinstance(data, list):
            if isinstance(data, PrimLit) or isinstance(data, StructLiteral):
                lit_type = self.visit(data, context)
                resolved_lit_type = self._resolve_type_node(lit_type)
                if explicit_ele_type and not self.checkTypeCompatibility(explicit_ele_type, resolved_lit_type):
                    raise TypeMismatch(data)
                return resolved_lit_type, []
            else:
                raise TypeMismatch(data)  

        element_types = []; element_dims = []
        first_elem_type = None; first_elem_dim_values = None

        for item in data:
             next_level_explicit_type = None
             if isinstance(explicit_ele_type, ArrayType): 
                  if len(explicit_ele_type.dimens) > 1: next_level_explicit_type = ArrayType(explicit_ele_type.dimens[1:], explicit_ele_type.eleType)
                  else: next_level_explicit_type = explicit_ele_type.eleType

             item_type, item_dim_values = self._check_nested_list(item, next_level_explicit_type, context) # Pass context list

             if item_type is None: 
                  if explicit_ele_type is None: raise StaticError("Cannot infer type from nested structure containing empty lists")
                  item_type = explicit_ele_type 

             if first_elem_type is None: first_elem_type, first_elem_dim_values = item_type, item_dim_values
             else:
                 resolved_first = self._resolve_type_node(first_elem_type); resolved_item = self._resolve_type_node(item_type)
                 if not types_equivalent(resolved_first, resolved_item):
                      is_f=isinstance(resolved_first,FloatType) or isinstance(resolved_item,FloatType); is_i=isinstance(resolved_first,IntType) or isinstance(resolved_item,IntType)
                      if not (is_f and is_i): raise TypeMismatch(f"Inconsistent types: {resolved_first} vs {resolved_item}")
                      first_elem_type = FloatType() # Promote inferred type
                 if first_elem_dim_values != item_dim_values: raise StaticError(f"Inconsistent dimensions")
             element_types.append(item_type); element_dims.append(item_dim_values)

        inferred_type = first_elem_type
        has_float = any(isinstance(self._resolve_type_node(t), FloatType) for t in element_types if t is not None)
        if has_float and isinstance(self._resolve_type_node(inferred_type), IntType): inferred_type = FloatType()
        inferred_dims_values = [len(data)] + first_elem_dim_values if first_elem_dim_values is not None else [len(data)]

        return inferred_type, inferred_dims_values
    def visitStructLiteral(self, ast: StructLiteral, context):
      
        struct_type = self._resolve_type_node(Id(ast.name))  # Resolve struct type name
        if not isinstance(struct_type, StructType):
            raise TypeMismatch(ast)
        provided_field_names = set()
        defined_fields = {name: ftype for name, ftype in struct_type.elements}
        for field_name, init_expr in ast.elements:
            if field_name in provided_field_names:
                raise TypeMismatch(ast)  # Duplicate field in literal
            provided_field_names.add(field_name)
            if field_name not in defined_fields:
                raise TypeMismatch(ast)  # Field not defined in struct type
            expected_field_type = self._resolve_type_node(defined_fields[field_name])
            actual_init_visit_type = self.visit(init_expr, context)
            resolved_actual_init_type = self._resolve_type_node(actual_init_visit_type)
            if isinstance(resolved_actual_init_type, VoidType):
                raise TypeMismatch(init_expr)
            if not self.checkTypeCompatibility(
                expected_field_type, resolved_actual_init_type
            ):
                raise TypeMismatch(init_expr)
        return struct_type


    def visitMethCall(self, ast: MethCall, context):
        method_name = ast.metName
        receiver_type = self._resolve_type_node(self.visit(ast.receiver, context))

        if isinstance(receiver_type, VoidType):
            raise TypeMismatch(ast)

        if isinstance(receiver_type, StructType):
            registry_key = (receiver_type.name, method_name)
            matched_method = self.method_registry.get(registry_key)
            if not matched_method:
                raise Undeclared(Method(), method_name)

            method_type = MType([p.parType for p in matched_method.fun.params], matched_method.fun.retType)

        elif isinstance(receiver_type, InterfaceType):
            method_type = None
            for proto in receiver_type.methods:
                if proto.name == method_name:
                    method_type = MType(proto.params, proto.retType)
                    break
            if not method_type:
                raise Undeclared(Method(), method_name)

        else:
            raise TypeMismatch(ast)
        if len(ast.args) != len(method_type.partype):
            raise TypeMismatch(ast)

        for arg, param_type in zip(ast.args, method_type.partype):
            arg_type = self._resolve_type_node(self.visit(arg, context))
            if not self.checkTypeCompatibility(self._resolve_type_node(param_type), arg_type):
                raise TypeMismatch(ast)

        return method_type.rettype


    # Type node visits (return context)
    def visitIntType(self, ast, c):
        return c[0]

    def visitFloatType(self, ast, c):
        return c[0]

    def visitBoolType(self, ast, c):
        return c[0]

    def visitStringType(self, ast, c):
        return c[0]

    def visitVoidType(self, ast, c):
        return c[0]

    def visitArrayType(self, ast, c):
        return c[0]