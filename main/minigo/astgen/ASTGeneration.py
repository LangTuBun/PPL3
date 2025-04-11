from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

from antlr4.tree.Tree import ParseTreeListener, ParseTree, TerminalNodeImpl, ErrorNodeImpl, TerminalNode, \
    INVALID_INTERVAL




class ASTGeneration(MiniGoVisitor):
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))


    def visitDecl_list(self, ctx:MiniGoParser.Decl_listContext):
        if not ctx.getChildCount():
            return []
    
        first_decl = self.visit(ctx.declaration())
        rest_decls = self.visit(ctx.decl_list_tail())

        return [first_decl] + rest_decls    

        

    def visitDecl_list_tail(self, ctx:MiniGoParser.Decl_list_tailContext):
        if not ctx.getChildCount():
            return []

        first_decl = self.visit(ctx.declaration())
        rest_decls = self.visit(ctx.decl_list_tail())
        return [first_decl] + rest_decls


    	
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        if ctx.constDecl():
            return self.visit(ctx.constDecl())
        elif ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.typeDecl():
            return self.visit(ctx.typeDecl())
        elif ctx.funcDecl():
            return self.visit(ctx.funcDecl())
        else:  # Must be methodDecl
            return self.visit(ctx.methodDecl())
    
    def visitConstDecl(self, ctx: MiniGoParser.ConstDeclContext):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        const_type = None # Default to None
        if ctx.typeName(): # Check if the optional type_ rule exists in the context
            const_type = self.visit(ctx.typeName())

      
        return ConstDecl(conName=name, conType=const_type, iniExpr=expr)


    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visit(ctx.varSpec())

    def visitVarSpec(self, ctx:MiniGoParser.VarSpecContext):
        name = ctx.ID().getText()

        if ctx.type_() and ctx.ASSIGN() and ctx.expression():
            var_type = self.visit(ctx.type_())
            expr = self.visit(ctx.expression())
            return VarDecl(name, var_type, expr)
        elif ctx.type_():
            var_type = self.visit(ctx.type_())
            return VarDecl(name, var_type, None)
        else:
            expr = self.visit(ctx.expression())
            return VarDecl(name, None, expr)
    
    def visitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        name = ctx.ID().getText()

   
        if ctx.structType():
            eles =  self.visit(ctx.structType())
            return StructType(name, eles, [])
        else:
            methods =  self.visit(ctx.interfaceType())
            return InterfaceType(name ,methods)
        
    
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        """
        Visit a function declaration node and return a FuncDecl AST node.
        
        Expected structure:
        func <ID> <signature> <block>
        
        Where <signature> may include parameters and an optional return type.
        """
        name = ctx.ID().getText()

        params = []
        param_list_ctx = ctx.signature().parameters().parameterList()
        if param_list_ctx:
            params = self.visit(param_list_ctx)

        
    
        ret_type = self.visit(ctx.signature().result()) if ctx.signature().result() else VoidType()
        
        body = self.visit(ctx.block())
        
        return FuncDecl(name, params, ret_type, body)

    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        """
        Visit a method declaration node and return a MethodDecl AST node.
        
        For example:
            func (c Calculator) Add(x int) int {
                c.value += x;
                return c.value;
            }
            
        This extracts the receiver's name and type, along with the method signature and body.
        """
        receiver_component = ctx.receiver().receiverComponent()
        receiver_name = receiver_component.ID().getText()
        receiver_type = self.visit(receiver_component.type_())

        method_name = ctx.ID().getText()
        params = []
        param_list_ctx = ctx.signature().parameters().parameterList()
        if param_list_ctx:
            params = self.visit(param_list_ctx)

        
    
        ret_type = self.visit(ctx.signature().result()) if ctx.signature().result() else VoidType()

        body = self.visit(ctx.block())

        func_decl = FuncDecl(method_name, params, ret_type, body)
        return MethodDecl(receiver_name, receiver_type, func_decl)


    def visitParameters(self, ctx:MiniGoParser.ParametersContext):
        if not ctx.parameterList():
            return []

        return self.visit(ctx.parameterList())
    
    def visitParameterList(self, ctx:MiniGoParser.ParameterListContext):

        if not ctx.parameterList(): 
            return self.visit(ctx.parameterComponent())
    
        first_params = self.visit(ctx.parameterComponent())
        rest_params = self.visit(ctx.parameterList())

        return first_params + rest_params

    def visitParameterComponent(self, ctx: MiniGoParser.ParameterComponentContext):
        param_type = self.visit(ctx.type_())

        ids = self.visit(ctx.identifierList())

        return [ParamDecl(id_name, param_type) for id_name in ids]

    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        if not ctx.identifierList():
            return [ctx.ID().getText()]
        
        first_id = ctx.ID().getText()
        rest_ids = self.visit(ctx.identifierList())

        return [first_id] + rest_ids

    def visitResult(self, ctx:MiniGoParser.ResultContext):
        return self.visit(ctx.type_())

    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        if not ctx.statementList():
            return Block([])
        
        stmts = self.visit( ctx.statementList())
        return Block(stmts)

    def visitStatementList(self, ctx:MiniGoParser.StatementListContext):
        first_stmt = self.visit(ctx.statement())

        if ctx.statementList_tail():
            rest_stmts = self.visit(ctx.statementList_tail())
            return [first_stmt] + rest_stmts    
        else:
            return [first_stmt]
    
    def visitStatementList_tail(self, ctx:MiniGoParser.StatementList_tailContext):
        if not ctx.getChildCount(): 
            return []

        first_stmts = self.visit(ctx.statement())
        rest_stmts = self.visit(ctx.statementList_tail())

        return [first_stmts] + rest_stmts

    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.declaration():
            return self.visit(ctx.declaration())
        elif ctx.basicStatement():
            return self.visit(ctx.basicStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.block():
            return self.visit(ctx.block())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        else:  
            return self.visit(ctx.forStatement())
    
    def visitBasicStatement(self, ctx:MiniGoParser.BasicStatementContext):
        if ctx.assignmentStatement():
            
            return self.visit(ctx.assignmentStatement())
        elif ctx.shortValDeclaration():
            return self.visit(ctx.shortValDeclaration())
        else:
            return self.visit(ctx.methodOrFunctionCall())

    def visitAssignmentStatement(self, ctx:MiniGoParser.AssignmentStatementContext):
        lhs = self.visit(ctx.oneValue())
        op = ctx.assignOperations().getText()
        rhs = self.visit(ctx.expression())


        if op != '=':
            binary_op = op[0]
            new_rhs = BinaryOp(binary_op, lhs, rhs)
            return Assign(lhs, new_rhs)

        return Assign(lhs, rhs)

    def visitShortValDeclaration(self, ctx:MiniGoParser.ShortValDeclarationContext):
        lhs = self.visit(ctx.oneValue())
        expr = self.visit(ctx.expression())

        

        return Assign(lhs,  expr)
            

    def visitMethodOrFunctionCall(self, ctx:MiniGoParser.MethodOrFunctionCallContext):
        return self.visit(ctx.methodChain())

    def visitMethodChain(self, ctx:MiniGoParser.MethodChainContext):
        self.current_chain_expr = Id(ctx.ID().getText())
        self.current_method_name = None

        self.visit(ctx.chainItems())
        return self.current_chain_expr

    def visitChainItems(self, ctx:MiniGoParser.ChainItemsContext):

        self.visit(ctx.chainItem())
        if ctx.chainItems():
            self.visit(ctx.chainItems())
            

    def visitChainItem(self, ctx:MiniGoParser.ChainItemContext):
        if ctx.DOT():
            field_name = ctx.ID().getText()

            self.current_chain_expr = FieldAccess(self.current_chain_expr, field_name)
            self.current_method_name = field_name

        elif ctx.index():
            indices = self.visit(ctx.index())

            self.current_chain_expr = ArrayCell(self.current_chain_expr, indices)
            self.current_method_name = None
        elif ctx.arguments():
            args = []
            if ctx.arguments().expressionList():
                args = self.visit(ctx.arguments().expressionList())

            if self.current_method_name:
                obj = self.current_chain_expr.receiver
                self.current_chain_expr = MethCall(
                    obj, self.current_method_name, args
                )
                self.current_method_name = None


            elif isinstance(self.current_chain_expr, Id):
                
                self.current_chain_expr = FuncCall(self.current_chain_expr.name, args)

      
    
    def visitOneValue(self, ctx:MiniGoParser.OneValueContext):
    
        if len(ctx.children) == 1:
            return Id(ctx.ID().getText())
        
        if ctx.DOT():
            return FieldAccess(
                self.visit(ctx.oneValue()),  
                ctx.ID().getText()           
            )
        
        base = self.visit(ctx.oneValue())
        indices = []
        while isinstance(base, ArrayCell):
            indices.extend([j for j in base.idx ])
            base = base.arr
        
        indices.extend(self.visit(ctx.index()))
        return ArrayCell(base, indices)

    
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))

        return Return(None)
    
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return Break()
    
    def visitContinueStatement(self, ctx: MiniGoParser.ContinueStatementContext):
        return Continue()
    
    
    
    def visitIfStatement(self, ctx: MiniGoParser.IfStatementContext):
        cond = None
        if ctx.condition():
            cond = self.visit(ctx.condition().expression())
        else:
            raise ValueError("If statement must have conditions!")

        then_block = self.visit(ctx.block())
        else_block = None

        if ctx.elseClause():
            else_block = self.visit(ctx.elseClause())
        
        return If(cond, then_block, else_block)

    def visitElseClause(self, ctx: MiniGoParser.ElseClauseContext):
        if ctx.block():
            return self.visit(ctx.block())
        else:
            return self.visit(ctx.ifStatement())
        
    
    def visitExpressionStmt(self, ctx:MiniGoParser.ExpressionStmtContext):
        return self.visit(ctx.expression())

    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visit(ctx.assignmentStatement())

    def visitShortVarDecl(self, ctx:MiniGoParser.ShortVarDeclContext): 
        return self.visit(ctx.shortValDeclaration())


    def visitSimpleStmt(self, ctx:MiniGoParser.SimpleStmtContext):
        if ctx.expressionStmt():
            return self.visit(ctx.expressionStmt())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.shortVarDecl():
            return self.visit(ctx.shortVarDecl())
        elif ctx.varDecl():
            return self.visit(ctx.varDecl())
        else:
            return None

    def  visitForClause(self, ctx: MiniGoParser.ForClauseContext):
        init_stmt = self.visit(ctx.simpleStmt(0))
        epxr = self.visit(ctx.expression())
        simpleStmt = self.visit(ctx.simpleStmt(1))
        return (init_stmt, epxr, simpleStmt)
    

    def visitForStatement(self, ctx: MiniGoParser.ForStatementContext):
        loop_body = self.visit(ctx.block())
        
        if ctx.expression():
            cond = self.visit(ctx.expression())
            return ForBasic(cond, loop_body)
        elif ctx.forClause():
            init, cond, update = self.visit(ctx.forClause())
            return ForStep(init, cond, update, loop_body)
        
        else:
            # range
            range_ctx = ctx.forRangeArray()
            ids = self.visit(range_ctx.identifierList())
            arr = self.visit(range_ctx.expression())

            idx = Id(ids[0])
            val = Id(ids[1] if len(ids) > 1 else '_')

            return ForEach (idx, val, arr, loop_body)
        

    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visit(ctx.logicalOr())

    def visitLogicalOr(self, ctx:MiniGoParser.LogicalOrContext):
        if not ctx.LOGICAL_OR():
            return self.visit(ctx.logicalAnd())
    
        left = self.visit(ctx.logicalOr())
        right = self.visit(ctx.logicalAnd())
        return BinaryOp("||", left, right)
    
    def visitLogicalAnd(self, ctx:MiniGoParser.LogicalAndContext):
        if not ctx.LOGICAL_AND():
            return self.visit(ctx.relational())

        left = self.visit(ctx.logicalAnd())
        right = self.visit(ctx.relational())
        return BinaryOp("&&", left, right)

    def visitRelational(self, ctx:MiniGoParser.RelationalContext):
        if ctx.getChildCount() == 1 and not any([ctx.EQUAL(), ctx.NOT_EQUAL(),
                                              ctx.LESS_THAN(), ctx.LESS_THAN_OR_EQUAL(),
                                              ctx.GREATER_THAN(), ctx.GREATER_THAN_OR_EQUAL()]):
            return self.visit(ctx.additive())
        
        left = self.visit(ctx.relational())
        right = self.visit(ctx.additive())

        if ctx.EQUAL():
            op = "=="
        elif ctx.NOT_EQUAL():
            op = "!="
        elif ctx.LESS_THAN():
            op = "<"
        elif ctx.LESS_THAN_OR_EQUAL():
            op = "<="
        elif ctx.GREATER_THAN():
            op = ">"
        else:
            op = ">="
        
        return BinaryOp(op, left, right)

    def visitAdditive(self, ctx:MiniGoParser.AdditiveContext):
        if not ctx.PLUS() and not ctx.MINUS():
            return self.visit(ctx.multiplication_division_modulo())
        
        left = self.visit(ctx.additive())
        right = self.visit(ctx.multiplication_division_modulo())

        op = "+" if ctx.PLUS() else "-"

        return BinaryOp(op, left, right)
    
    def visitMultiplication_division_modulo(self, ctx:MiniGoParser.Multiplication_division_moduloContext):
        if not ctx.MULTIPLY() and not ctx.DIVIDE() and not ctx.MODULO():
            return self.visit(ctx.unary())
        
        left = self.visit(ctx.multiplication_division_modulo())
        right = self.visit(ctx.unary())

        if ctx.MULTIPLY():
            op = "*"
        elif ctx.DIVIDE():
            op = "/"
        else:
            op = "%"

        return BinaryOp(op, left, right)
    
    def visitUnary(self, ctx:MiniGoParser.UnaryContext):
        if ctx.postfix():
            return self.visit(ctx.postfix())
        
        op = "!" if ctx.NOT() else "-"
        expr = self.visit(ctx.unary())
        return UnaryOp(op, expr)

    def visitPostfix(self, ctx:MiniGoParser.PostfixContext):
        
        if ctx.primaryExpr():
            return self.visit(ctx.primaryExpr())
        
        base = self.visit(ctx.postfix())

        if ctx.DOT():
            return FieldAccess(base, ctx.ID().getText())
        elif ctx.index():
            indices = self.visit(ctx.index())
            if isinstance(base, ArrayCell):
                base.idx.extend(indices)
                return base
            else:
                return ArrayCell(base, indices)
        else:
            args = []
            if ctx.arguments().expressionList():
                args = self.visit(ctx.arguments().expressionList())

            if isinstance(base, FieldAccess):
                return MethCall(base.receiver, base.field, args)
            elif isinstance(base, Id):

       
                return FuncCall(base.name, args)
            else:
                raise ValueError("Base must be fieldacces or Id")
        
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visit(ctx.operand())
    
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.expression())
    
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.basicLiteral():
            return self.visit(ctx.basicLiteral())
        return self.visit(ctx.compositeLiteral())

    def visitBasicLiteral(self, ctx:MiniGoParser.BasicLiteralContext):
        if ctx.NIL():
            return NilLiteral()
        
        elif ctx.BOOLEAN_LIT():
            val = ctx.BOOLEAN_LIT().getText()
            return BooleanLiteral(val == 'true')

        elif ctx.STRING_LIT():
          
            return StringLiteral(ctx.STRING_LIT().getText())

        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        
        else:
            return self.visit(ctx.integerLiteral())
    
    def visitIntegerLiteral(self, ctx:MiniGoParser.IntegerLiteralContext):
        if ctx.DECIMAL_LIT():
            return IntLiteral(int(ctx.DECIMAL_LIT().getText()))
        
        elif ctx.BINARY_LIT():
            val = ctx.BINARY_LIT().getText()[2:]  # Remove '0b' prefix
            return IntLiteral(int(val, 2))
        elif ctx.OCTAL_LIT():
            val = ctx.OCTAL_LIT().getText()[2:]  # Remove '0o' prefix
            return IntLiteral(int(val, 8))
        else:  # HEX_LIT
            val = ctx.HEX_LIT().getText()[2:]  # Remove '0x' prefix
            return IntLiteral(int(val, 16))
        
    def visitCompositeLiteral(self, ctx:MiniGoParser.CompositeLiteralContext):
        if ctx.ID():
            name = ctx.ID().getText()
            elements = []
            if ctx.compositeLiteralValue().elementList():
                elements = self.visit(ctx.compositeLiteralValue().elementList())
            return StructLiteral(name, elements)

        else:
            arr_type = self.visit(ctx.arrayType())
            dimensions = arr_type.dimens
            ele_type = arr_type.eleType
            values = []
        
            if ctx.compositeLiteralValue().elementList():
                values = self.visit(ctx.compositeLiteralValue().elementList())
            

            return ArrayLiteral(dimensions, ele_type, values)

    def visitElementList(self, ctx:MiniGoParser.ElementListContext):
        elements = []
        element = self.visit(ctx.element())
        
        elements.append(element)

        if ctx.elementList():
            elements.extend(self.visit(ctx.elementList()))


        
        return elements

    def visitElement(self, ctx:MiniGoParser.ElementContext):
        if ctx.fieldName():
            key = ctx.fieldName().ID().getText()
            value = self.visit(ctx.value())
            return (key, value)
        return self.visit(ctx.value())
    

    def visitValue(self, ctx:MiniGoParser.ValueContext):
        if ctx.compositeLiteralValue():
            return self.visit(ctx.compositeLiteralValue())
        return self.visit(ctx.expression())
    
    def visitCompositeLiteralValue(self, ctx:MiniGoParser.CompositeLiteralValueContext):
        if not ctx.elementList():
            return []
        return self.visit(ctx.elementList())
    
    def visitExpressionList(self, ctx:MiniGoParser.ExpressionListContext):

        if not ctx.expressionList():
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expressionList())

    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        if not ctx.expressionList():
            return []

        return self.visit(ctx.expressionList())
    
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        index_expr = self.visit(ctx.indexExpr())
    
        if ctx.index():
            rest_indices = self.visit(ctx.index())
            return [index_expr] + rest_indices
        return [index_expr]
    
    def visitIndexExpr(self, ctx:MiniGoParser.IndexExprContext):
        if ctx.DECIMAL_LIT():
            return IntLiteral(int(ctx.DECIMAL_LIT().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.methodOrFunctionCall():
            return self.visit(ctx.methodOrFunctionCall())
        
    
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        if ctx.typeName():
            return self.visit(ctx.typeName())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.structType():
            return self.visit(ctx.structType())
        return self.visit(ctx.interfaceType())
    
    def visitTypeName(self, ctx:MiniGoParser.TypeNameContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        return Id(ctx.ID().getText())

    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        ele_type = self.visit(ctx.typeName())
        dims = self.visit(ctx.index())

        return ArrayType(dims, ele_type)
    
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        elements = []
        
        if ctx.fieldDeclList():
            elements = self.visit(ctx.fieldDeclList())
        
        return elements
    
    def visitFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        elements = []
        field_decl = self.visit(ctx.fieldDecl())
        elements.append(field_decl)

        if ctx.fieldDeclList():
            elements.extend(self.visit(ctx.fieldDeclList()))
        return elements

     
    def visitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        name = ctx.ID().getText()
        field_type = self.visit(ctx.type_())
        return (name, field_type)
    
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        methods = []
        if ctx.methodSpecList():
            methods = self.visit(ctx.methodSpecList())
        
        return methods
    

    def visitMethodSpecList(self, ctx:MiniGoParser.MethodSpecListContext):
        methods = []

        # Get the first  specification
        method_spec = self.visit(ctx.methodSpec())
        methods.append(method_spec)

        if ctx.methodSpecList():
            methods.extend(self.visit(ctx.methodSpecList()))

        return methods

    def visitMethodSpec(self, ctx:MiniGoParser.MethodSpecContext):
        name = ctx.ID().getText()

        params = []

        if ctx.parameters():
            params = self.visit(ctx.parameters())
        
        params_type = [i.parType for i in params]
        ret_type = VoidType()
        if ctx.result():
            ret_type = self.visit(ctx.result())

        return Prototype(name, params_type, ret_type)
        






    

