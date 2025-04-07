# StaticCheck.py

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *  # Use only Undeclared, Redeclared, TypeMismatch
from functools import reduce


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
            print("🥒🥒 sai roiiii")
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


# --- check_assignment_compatibility (More Robust) ---
def check_assignment_compatibility(lhs_type, rhs_type, env):
    """Checks if rhs_type can be assigned to lhs_type (more robust)."""
    lhs_resolved = resolve_type_node(lhs_type) if lhs_type else None
    rhs_resolved = resolve_type_node(rhs_type) if rhs_type else None

    # Cannot assign to/from Void (allow only Void->Void for return/assign?)
    # Let's disallow void assignment completely for simplicity unless returning void
    if isinstance(lhs_resolved, VoidType) or isinstance(rhs_resolved, VoidType):
        return False  # Cannot assign void or assign to void variable

    if lhs_resolved is None or rhs_resolved is None:
        return False

    if types_equivalent(lhs_resolved, rhs_resolved):
        return True
    if isinstance(lhs_resolved, FloatType) and isinstance(rhs_resolved, IntType):
        return True
    if isinstance(lhs_resolved, ArrayType) and isinstance(rhs_resolved, ArrayType):
        if len(lhs_resolved.dimens) == len(rhs_resolved.dimens):
            # TODO: Check dim values
            # Check element compatibility recursively
            return check_assignment_compatibility(
                lhs_resolved.eleType, rhs_resolved.eleType, env
            )
        return False
    if isinstance(lhs_resolved, InterfaceType) and isinstance(rhs_resolved, StructType):
        return check_struct_implements_interface(rhs_resolved, lhs_resolved, env)
    if isinstance(rhs_resolved, NilLiteral):
        if isinstance(lhs_resolved, InterfaceType):
            return True  # Allow nil -> interface
        # TODO: Add other nil rules (pointers?)
        return False
    return False


# Helper to check struct implements interface - uses resolved types
def check_struct_implements_interface(struct_type, interface_type, env):
    if not isinstance(struct_type, StructType) or not isinstance(
        interface_type, InterfaceType
    ):
        return False
    struct_type_name = struct_type.name
    for proto in interface_type.methods:
        method_symbol = lookup_method_global(
            proto.name, struct_type_name, env[0]
        )  # Check global env
        if not method_symbol:
            return False
        method_mtype = method_symbol.mtype
        try:
            proto_ret_res = resolve_type_node(proto.retType)
            method_ret_res = resolve_type_node(method_mtype.rettype)
            if len(proto.params) != len(method_mtype.partype):
                return False
            proto_params_res = [resolve_type_node(pt) for pt in proto.params]
            method_params_res = [resolve_type_node(pm) for pm in method_mtype.partype]
        except Undeclared:
            return False
        if not all(
            types_equivalent(p_proto, p_meth)
            for p_proto, p_meth in zip(proto_params_res, method_params_res)
        ):
            return False
        if not types_equivalent(proto_ret_res, method_ret_res):
            return False
    return True


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
    def __init__(self, ast):
        self.ast = ast
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

    # --- Helper for type resolution using self.type_env ---
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
                # Create a new ArrayType with resolved element type
                # Keep dimensions as they are (expressions)
                resolved_ele = self._resolve_type_node(type_node_or_id.eleType)
                return ArrayType(type_node_or_id.dimens, resolved_ele)
            except Undeclared as e:
                raise e  # Propagate if element type is undeclared
        elif isinstance(type_node_or_id, MType):
            try:
                # Create a new MType with resolved param/return types
                resolved_parts = [
                    self._resolve_type_node(p) for p in type_node_or_id.partype
                ]
                resolved_ret = self._resolve_type_node(type_node_or_id.rettype)
                return MType(resolved_parts, resolved_ret)
            except Undeclared as e:
                raise e
        return type_node_or_id  # Return already resolved types (IntType etc.)

    # --- Helper to check if a type exists ---
    def _check_type_exists(self, type_node_or_id):
        # This just attempts resolution, which raises Undeclared if not found
        self._resolve_type_node(type_node_or_id)
        return True  # No exception means it exists

    # --- checkTypeCompatibility (Use robust version) ---
    def checkTypeCompatibility(self, lhs_type, rhs_type):
        """Checks if rhs_type can be assigned to lhs_type (uses resolved types)."""
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
                # TODO: Check dim values
                # Use instance method checkTypeCompatibility recursively
                return self.checkTypeCompatibility(
                    lhs_resolved.eleType, rhs_resolved.eleType
                )
            return False
        if isinstance(lhs_resolved, InterfaceType) and isinstance(
            rhs_resolved, StructType
        ):
            # Pass self.global_envi for the check
            return check_struct_implements_interface(
                rhs_resolved, lhs_resolved, self.global_envi
            )
        if isinstance(rhs_resolved, NilLiteral):
            if isinstance(lhs_resolved, InterfaceType):
                return True
            return False
        return False

    # --- Visitor Methods ---

    def visitProgram(self, ast: Program, context):
        # Populate self.type_env with declared structs/interfaces first
        # This deviates slightly from pure reduce but handles type forward refs
        declared_types = {}
        for decl in ast.decl:
            if isinstance(decl, (StructType, InterfaceType)):
                type_name = decl.name
                if type_name in self.type_env or type_name in declared_types:
                    raise Redeclared(Type(), type_name)
                # Also check against global symbols added so far in reduce? Complex.
                # Let's assume type names checked against self.type_env is sufficient for now.
                declared_types[type_name] = decl
        self.type_env.update(declared_types)  # Add all found types

        # Check internal consistency of declared types AFTER adding all to env
        for decl in ast.decl:
            if isinstance(decl, (StructType, InterfaceType)):
                self.visit(decl, context)  # Calls visitStructType/InterfaceType

        # Process remaining declarations (Var, Const, Func, Method) using reduce
        reduce(
            lambda ctx, decl: self.visit(decl, ctx)
            if not isinstance(decl, (StructType, InterfaceType))
            else ctx,
            ast.decl,
            context,
        )

        # Check function/method bodies (this requires a second pass or different structure)
        # For simplicity with reduce, we'll rely on checks happening when symbols are used.
        # This won't catch errors in unused functions/methods body.
        # A proper two-pass approach is better for full checking.

        return None

    def visitStructType(self, ast: StructType, context):
        # Internal consistency check (already added to self.type_env in visitProgram)
        field_names = set()
        if hasattr(ast, "elements") and isinstance(ast.elements, list):
            for element in ast.elements:
                if isinstance(element, tuple) and len(element) == 2:
                    field_name, field_type_node = element
                    if field_name in field_names:
                        raise Redeclared(Field(), field_name)
                    field_names.add(field_name)
                    try:  # Check field type validity
                        resolved_type = self._resolve_type_node(field_type_node)
                        if isinstance(resolved_type, VoidType):
                            raise TypeMismatch(ast)
                    except Undeclared as e:
                        raise e
        return context  # Return original context

    def visitInterfaceType(self, ast: InterfaceType, context):
        # Internal consistency check
        prototype_names = set()
        if hasattr(ast, "methods") and isinstance(ast.methods, list):
            for proto in ast.methods:
                if proto.name in prototype_names:
                    raise Redeclared(Prototype(), proto.name)
                prototype_names.add(proto.name)
                self.visit(proto, context)  # Check types within prototype
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
        current_scope = context[0]
        var_name = ast.varName
        if self.lookup(var_name, current_scope, lambda s: s.name):
            raise Redeclared(Variable(), var_name)
        declared_type = ast.varType
        resolved_rhs_type = None
        if ast.varInit:
            rhs_type = self.visit(ast.varInit, context)
            resolved_rhs_type = self._resolve_type_node(rhs_type) if rhs_type else None
            if isinstance(resolved_rhs_type, VoidType):
                raise TypeMismatch(ast.varInit)
        final_var_type = None
        if declared_type:
            resolved_decl_type = self._resolve_type_node(declared_type)
            if resolved_rhs_type:
                if not self.checkTypeCompatibility(
                    resolved_decl_type, resolved_rhs_type
                ):
                    raise TypeMismatch(ast)
            final_var_type = resolved_decl_type
        elif resolved_rhs_type:
            final_var_type = resolved_rhs_type
        else:
            raise StaticError("Variable needs type or initializer: " + var_name)
        if isinstance(final_var_type, VoidType):
            raise TypeMismatch(ast)
        new_symbol = Symbol(var_name, final_var_type, kind=Variable())
        return [[new_symbol] + current_scope] + context[1:]

    def visitConstDecl(self, ast: ConstDecl, context):
        
        current_scope = context[0]
        const_name = ast.conName
        if self.lookup(const_name, current_scope, lambda s: s.name):
            raise Redeclared(Constant(), const_name)
        resolved_rhs_type = None
        if ast.iniExpr:
            rhs_type = self.visit(ast.iniExpr, context)
            resolved_rhs_type = self._resolve_type_node(rhs_type) if rhs_type else None
            if isinstance(resolved_rhs_type, VoidType):
                raise TypeMismatch(ast.iniExpr)
        else:
            raise StaticError("Constant needs initializer: " + const_name)
        declared_type = ast.conType
        final_const_type = None
        if declared_type:
            resolved_decl_type = self._resolve_type_node(declared_type)
            if not self.checkTypeCompatibility(resolved_decl_type, resolved_rhs_type):
                raise TypeMismatch(ast)
            final_const_type = resolved_decl_type
        else:
            final_const_type = resolved_rhs_type
        if isinstance(final_const_type, VoidType):
            raise TypeMismatch(ast)
        new_symbol = Symbol(
            const_name, final_const_type, value=ast.iniExpr, kind=Constant()
        )
        return [[new_symbol] + current_scope] + context[1:]

    def visitFuncDecl(self, ast: FuncDecl, context):
        # ... (Keep implementation using self._resolve_type_node and checking body) ...
        func_name = ast.name
        if self.lookup(
            func_name, context[0], lambda s: s.name and isinstance(s.kind, Function)
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
        if ast.body:
            self.visit(ast.body, fn_ctx)
        self.current_function_ret_type, self.is_in_loop = o_ret, o_loop
        return [updated_global_scope] + outer_context

    # --- visitMethodDecl (using lookup_method_global) ---
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
            receiver_type_name_str = resolved_receiver_type.name
        except Undeclared as e:
            raise e

        # Check Redeclared Method using helper
        if lookup_method_global(method_name, receiver_type_name_str, context[0]):
            raise Redeclared(Method(), method_name)

        # Check signature types exist
        try:
            param_types = [p.parType for p in ast.fun.params]
            [self._check_type_exists(pt) for pt in param_types]
            self._check_type_exists(ast.fun.retType)
        except Undeclared as e:
            raise e

        # Add global symbol
        method_mtype = MType(param_types, ast.fun.retType)
        method_symbol = Symbol(
            method_name, method_mtype, kind=Method(), value=ast
        )  # Store decl in value
        updated_global_scope = [method_symbol] + context[0]
        outer_context = context[1:]
        updated_context = [updated_global_scope] + outer_context

        # Check body
        o_ret, o_loop = self.current_function_ret_type, self.is_in_loop
        try:
            self.current_function_ret_type = self._resolve_type_node(ast.fun.retType)
        except Undeclared as e:
            raise e
        self.is_in_loop = False
        local_scope = []
        method_body_context = [
            local_scope
        ] + context  # Use original outer context stack
        if self.lookup(receiver_name, local_scope, lambda s: s.name):
            raise Redeclared(Variable(), receiver_name)
        receiver_symbol = Symbol(receiver_name, resolved_receiver_type, kind=Variable())
        local_scope.insert(0, receiver_symbol)
        param_names = set([receiver_name])
        try:
            for param in ast.fun.params:
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
        if ast.fun.body:
            self.visit(ast.fun.body, method_body_context)
        self.current_function_ret_type, self.is_in_loop = o_ret, o_loop
        return updated_context  # Return context with global method symbol

    # visitBlock, Id, Assign, If, For*, Break, Continue, Return, Ops, Calls, Access, Literals
    # (Keep implementations)
    def visitBlock(self, ast: Block, context):
        block_scope = []
        block_context = [block_scope] + context
        curr_ctx = block_context
        if ast.member:
            for member in ast.member:
                curr_ctx = self.visit(member, curr_ctx)
        return context

    def visitId(self, ast: Id, context):
        ident_name = ast.name
        symbol = None
        # *** Use self.lookup_symbol for correct scope search ***
        symbol = self.lookup_symbol(ident_name, context)
        if not symbol:
            raise Undeclared(Identifier(), ident_name)
        return symbol.mtype

    def visitAssign(self, ast: Assign, context):
        rhs_visit_type = self.visit(ast.rhs, context)
        resolved_rhs_type = (
            self._resolve_type_node(rhs_visit_type) if rhs_visit_type else None
        )
        if resolved_rhs_type is None or isinstance(resolved_rhs_type, VoidType):
            raise TypeMismatch(ast.rhs)
        resolved_lhs_type, is_lhs_const = None, False
        if isinstance(ast.lhs, Id):
            lhs_symbol = self.lookup_symbol(ast.lhs.name, context)
            if lhs_symbol is None:
                raise Undeclared(Identifier(), ast.lhs.name)
            if not isinstance(lhs_symbol.kind, (Variable, Parameter)):
                raise TypeMismatch(ast.lhs)
            if isinstance(lhs_symbol.kind, Constant):
                is_lhs_const = True
            resolved_lhs_type = self._resolve_type_node(lhs_symbol.mtype)
        elif isinstance(ast.lhs, ArrayCell):
            resolved_lhs_type = self.visit(ast.lhs, context)
        elif isinstance(ast.lhs, FieldAccess):
            resolved_lhs_type = self.visit(ast.lhs, context)
        else:
            raise TypeMismatch(ast.lhs)
        if is_lhs_const:
            raise TypeMismatch(ast.lhs)  # Assign to const
        if resolved_lhs_type is None or isinstance(resolved_lhs_type, VoidType):
            raise TypeMismatch(ast.lhs)
        if not self.checkTypeCompatibility(resolved_lhs_type, resolved_rhs_type):
            raise TypeMismatch(ast)
        return context

    def visitIf(self, ast: If, context):
        expr_visit = self.visit(ast.expr, context)
        expr_res = self._resolve_type_node(expr_visit)

    def visitForBasic(self, ast: ForBasic, context):
        cond_visit = self.visit(ast.cond, context)
        cond_res = self._resolve_type_node(cond_visit)

    def visitForStep(self, ast: ForStep, context):
        loop_scope = []
        loop_ctx = [loop_scope] + context
        ctx_after_init = self.visit(ast.init, loop_ctx) if ast.init else loop_ctx
        cond_visit = self.visit(ast.cond, ctx_after_init) if ast.cond else BOOL_TYPE
        cond_res = self._resolve_type_node(cond_visit)

    def visitForEach(self, ast: ForEach, context):
        arr_visit = self.visit(ast.arr, context)
        arr_type = self._resolve_type_node(arr_visit)

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
                raise TypeMismatch(ast)
            if not self.checkTypeCompatibility(expected, actual):
                raise TypeMismatch(ast)
        elif not isinstance(expected, VoidType):
            raise TypeMismatch(ast)
        return context

    def visitBinaryOp(self, ast: BinaryOp, context):
        op = ast.op
        left_visit = self.visit(ast.left, context)
        right_visit = self.visit(ast.right, context)
        left, right = (
            self._resolve_type_node(left_visit),
            self._resolve_type_node(right_visit),
        )
        if isinstance(left, VoidType) or isinstance(right, VoidType):
            raise TypeMismatch(ast)
        if op in ["+", "-", "*", "/"]:
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
            if isinstance(left, (IntType, FloatType)) and isinstance(
                right, (IntType, FloatType)
            ):
                return BOOL_TYPE
            raise TypeMismatch(ast)
        if op in ["==", "!="]:
            can_compare = False
            if isinstance(left, (IntType, FloatType)) and isinstance(
                right, (IntType, FloatType)
            ):
                can_compare = True
            elif types_equivalent(left, right) and isinstance(
                left, (BoolType, StringType)
            ):
                can_compare = True
            if not can_compare:
                raise TypeMismatch(ast)
            return BOOL_TYPE
        raise StaticError(f"Unhandled: {op}")

    def visitUnaryOp(self, ast: UnaryOp, context):
        op = ast.op
        body_visit = self.visit(ast.body, context)
        expr = self._resolve_type_node(body_visit)
        if isinstance(expr, VoidType):
            raise TypeMismatch(ast.body)
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
        func_name = ast.funName
        # *** Use self.lookup_symbol for multi-scope lookup ***
        symbol = self.lookup_symbol(func_name, context, Function)
        if symbol is None:
            raise Undeclared(Function(), func_name)
        if not isinstance(symbol.mtype, MType):
            raise TypeMismatch(ast)
        func_mtype = symbol.mtype
        if len(ast.args) != len(func_mtype.partype):
            raise TypeMismatch(ast)
        for i in range(len(ast.args)):
            arg_visit = self.visit(ast.args[i], context)
            arg_type = self._resolve_type_node(arg_visit)
            if isinstance(arg_type, VoidType):
                raise TypeMismatch(ast.args[i])
            param_type = self._resolve_type_node(func_mtype.partype[i])
            if not self.checkTypeCompatibility(param_type, arg_type):
                raise TypeMismatch(ast.args[i])
        # Caller checks if Void return is valid in its context
        return func_mtype.rettype

    def visitArrayCell(self, ast: ArrayCell, context):
        arr_visit = self.visit(ast.arr, context)
        arr_type = self._resolve_type_node(arr_visit)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast.arr)
        if len(ast.idx) > len(arr_type.dimens):
            raise TypeMismatch(ast)
        for index_expr in ast.idx:
            idx_visit = self.visit(index_expr, context)
            idx_type = self._resolve_type_node(idx_visit)
            if not isinstance(idx_type, IntType):
                raise TypeMismatch(index_expr)
        if len(ast.idx) == len(arr_type.dimens):
            return arr_type.eleType
        else:
            return ArrayType(arr_type.dimens[len(ast.idx) :], arr_type.eleType)

    def visitFieldAccess(self, ast: FieldAccess, context):
        rcv_visit = self.visit(ast.receiver, context)
        rcv_type = self._resolve_type_node(rcv_visit)
        if not isinstance(rcv_type, StructType):
            print("🥒🥒")
            raise TypeMismatch(ast.receiver)
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

    # --- Implementations for ArrayLiteral, StructLiteral, MethCall ---
    def visitArrayLiteral(self, ast: ArrayLiteral, context):
        # Check if all elements are of the same type
        if not ast.elems:
            raise TypeMismatch(ast)
        first_elem_visit = self.visit(ast.elems[0], context)
        first_elem_type = self._resolve_type_node(first_elem_visit)
        if isinstance(first_elem_type, VoidType):
            raise TypeMismatch(ast.elems[0])
        for elem in ast.elems[1:]:
            elem_visit = self.visit(elem, context)
            elem_type = self._resolve_type_node(elem_visit)
            if isinstance(elem_type, VoidType):
                raise TypeMismatch(elem)
            if not self.checkTypeCompatibility(first_elem_type, elem_type):
                raise TypeMismatch(elem)
        # Check if all elements are of the same type
        
        

    def _check_nested_list(self, data, context):
        raise NotImplementedError(
            "_check_nested_list - Needs refinement based on MiniGo literal rules"
        )

    def visitStructLiteral(self, ast: StructLiteral, context):
        # ... (Keep implementation from previous answers) ...
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
        # TODO: Check if all fields are initialized if needed?
        return struct_type

    def visitMethCall(self, ast: MethCall, context):
        # ... (Keep implementation from previous answers) ...
        method_name = ast.metName
        receiver_visit_type = self.visit(ast.receiver, context)
        resolved_receiver_type = self._resolve_type_node(receiver_visit_type)
        if not isinstance(resolved_receiver_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast.receiver)
        receiver_type_name_str = resolved_receiver_type.name
        method_mtype = None
        if isinstance(resolved_receiver_type, StructType):
            method_symbol = lookup_method_global(
                method_name, receiver_type_name_str, self.global_envi[0]
            )
            if not method_symbol:
                raise Undeclared(Method(), method_name)
            if not isinstance(method_symbol.mtype, MType):
                raise StaticError("Method symbol invalid")
            method_mtype = method_symbol.mtype
        elif isinstance(resolved_receiver_type, InterfaceType):
            found_proto = None
            if hasattr(resolved_receiver_type, "methods") and isinstance(
                resolved_receiver_type.methods, list
            ):
                for proto in resolved_receiver_type.methods:
                    if isinstance(proto, Prototype) and proto.name == method_name:
                        found_proto = proto
                        break
            if not found_proto:
                raise Undeclared(Method(), method_name)
            try:
                resolved_params = [
                    self._resolve_type_node(pt) for pt in found_proto.params
                ]
                resolved_ret = self._resolve_type_node(found_proto.retType)
                method_mtype = MType(resolved_params, resolved_ret)
            except Undeclared as e:
                raise e
        if method_mtype is None:
            raise StaticError(f"Failed to find method signature {method_name}")
        if len(ast.args) != len(method_mtype.partype):
            raise TypeMismatch(ast)
        for i in range(len(ast.args)):
            arg_visit = self.visit(ast.args[i], context)
            arg_type = self._resolve_type_node(arg_visit)
            if isinstance(arg_type, VoidType):
                raise TypeMismatch(ast.args[i])
            param_type = self._resolve_type_node(method_mtype.partype[i])
            if not self.checkTypeCompatibility(param_type, arg_type):
                raise TypeMismatch(ast.args[i])
        # Caller checks void context
        return method_mtype.rettype

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
