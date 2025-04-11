# Generated from c:/Users/RAZER/OneDrive/Documents/HCMUTSUB/PPL/assignment3/initial/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declList.
    def enterDeclList(self, ctx:MiniGoParser.DeclListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declList.
    def exitDeclList(self, ctx:MiniGoParser.DeclListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declList_tail.
    def enterDeclList_tail(self, ctx:MiniGoParser.DeclList_tailContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declList_tail.
    def exitDeclList_tail(self, ctx:MiniGoParser.DeclList_tailContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declaration.
    def enterDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declaration.
    def exitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#eos.
    def enterEos(self, ctx:MiniGoParser.EosContext):
        pass

    # Exit a parse tree produced by MiniGoParser#eos.
    def exitEos(self, ctx:MiniGoParser.EosContext):
        pass


    # Enter a parse tree produced by MiniGoParser#constDecl.
    def enterConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#constDecl.
    def exitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#varDecl.
    def enterVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#varDecl.
    def exitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#varSpec.
    def enterVarSpec(self, ctx:MiniGoParser.VarSpecContext):
        pass

    # Exit a parse tree produced by MiniGoParser#varSpec.
    def exitVarSpec(self, ctx:MiniGoParser.VarSpecContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typeDecl.
    def enterTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typeDecl.
    def exitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structType.
    def enterStructType(self, ctx:MiniGoParser.StructTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structType.
    def exitStructType(self, ctx:MiniGoParser.StructTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#fieldDeclList.
    def enterFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#fieldDeclList.
    def exitFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#fieldDecl.
    def enterFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#fieldDecl.
    def exitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interfaceType.
    def enterInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interfaceType.
    def exitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcDecl.
    def enterFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcDecl.
    def exitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#methodDecl.
    def enterMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methodDecl.
    def exitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#returnType.
    def enterReturnType(self, ctx:MiniGoParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#returnType.
    def exitReturnType(self, ctx:MiniGoParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block.
    def enterBlock(self, ctx:MiniGoParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block.
    def exitBlock(self, ctx:MiniGoParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmtDeclList.
    def enterStmtDeclList(self, ctx:MiniGoParser.StmtDeclListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmtDeclList.
    def exitStmtDeclList(self, ctx:MiniGoParser.StmtDeclListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statementList.
    def enterStatementList(self, ctx:MiniGoParser.StatementListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statementList.
    def exitStatementList(self, ctx:MiniGoParser.StatementListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statement.
    def enterStatement(self, ctx:MiniGoParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statement.
    def exitStatement(self, ctx:MiniGoParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#simpleStatement.
    def enterSimpleStatement(self, ctx:MiniGoParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#simpleStatement.
    def exitSimpleStatement(self, ctx:MiniGoParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#receiver.
    def enterReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass

    # Exit a parse tree produced by MiniGoParser#receiver.
    def exitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass


    # Enter a parse tree produced by MiniGoParser#returnStatement.
    def enterReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#returnStatement.
    def exitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#breakStatement.
    def enterBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#breakStatement.
    def exitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continueStatement.
    def enterContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continueStatement.
    def exitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ifStatement.
    def enterIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ifStatement.
    def exitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forStatement.
    def enterForStatement(self, ctx:MiniGoParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forStatement.
    def exitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forCondition.
    def enterForCondition(self, ctx:MiniGoParser.ForConditionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forCondition.
    def exitForCondition(self, ctx:MiniGoParser.ForConditionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forClause.
    def enterForClause(self, ctx:MiniGoParser.ForClauseContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forClause.
    def exitForClause(self, ctx:MiniGoParser.ForClauseContext):
        pass


    # Enter a parse tree produced by MiniGoParser#rangeClause.
    def enterRangeClause(self, ctx:MiniGoParser.RangeClauseContext):
        pass

    # Exit a parse tree produced by MiniGoParser#rangeClause.
    def exitRangeClause(self, ctx:MiniGoParser.RangeClauseContext):
        pass


    # Enter a parse tree produced by MiniGoParser#paramList.
    def enterParamList(self, ctx:MiniGoParser.ParamListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#paramList.
    def exitParamList(self, ctx:MiniGoParser.ParamListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#paramDecl.
    def enterParamDecl(self, ctx:MiniGoParser.ParamDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#paramDecl.
    def exitParamDecl(self, ctx:MiniGoParser.ParamDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#identifierList.
    def enterIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#identifierList.
    def exitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typeAnnotation.
    def enterTypeAnnotation(self, ctx:MiniGoParser.TypeAnnotationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typeAnnotation.
    def exitTypeAnnotation(self, ctx:MiniGoParser.TypeAnnotationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression.
    def enterExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expression.
    def exitExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logicalOr.
    def enterLogicalOr(self, ctx:MiniGoParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logicalOr.
    def exitLogicalOr(self, ctx:MiniGoParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logicalAnd.
    def enterLogicalAnd(self, ctx:MiniGoParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logicalAnd.
    def exitLogicalAnd(self, ctx:MiniGoParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by MiniGoParser#equalityAndRelational.
    def enterEqualityAndRelational(self, ctx:MiniGoParser.EqualityAndRelationalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#equalityAndRelational.
    def exitEqualityAndRelational(self, ctx:MiniGoParser.EqualityAndRelationalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#additive.
    def enterAdditive(self, ctx:MiniGoParser.AdditiveContext):
        pass

    # Exit a parse tree produced by MiniGoParser#additive.
    def exitAdditive(self, ctx:MiniGoParser.AdditiveContext):
        pass


    # Enter a parse tree produced by MiniGoParser#multiplicative.
    def enterMultiplicative(self, ctx:MiniGoParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#multiplicative.
    def exitMultiplicative(self, ctx:MiniGoParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#unaryExpr.
    def enterUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#unaryExpr.
    def exitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#postFixOps.
    def enterPostFixOps(self, ctx:MiniGoParser.PostFixOpsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#postFixOps.
    def exitPostFixOps(self, ctx:MiniGoParser.PostFixOpsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#postfixExpr.
    def enterPostfixExpr(self, ctx:MiniGoParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#postfixExpr.
    def exitPostfixExpr(self, ctx:MiniGoParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#postfixOp.
    def enterPostfixOp(self, ctx:MiniGoParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#postfixOp.
    def exitPostfixOp(self, ctx:MiniGoParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#functionCall.
    def enterFunctionCall(self, ctx:MiniGoParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MiniGoParser#functionCall.
    def exitFunctionCall(self, ctx:MiniGoParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MiniGoParser#methodCall.
    def enterMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methodCall.
    def exitMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        pass


    # Enter a parse tree produced by MiniGoParser#indexAccess.
    def enterIndexAccess(self, ctx:MiniGoParser.IndexAccessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#indexAccess.
    def exitIndexAccess(self, ctx:MiniGoParser.IndexAccessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#compositeLiteral.
    def enterCompositeLiteral(self, ctx:MiniGoParser.CompositeLiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#compositeLiteral.
    def exitCompositeLiteral(self, ctx:MiniGoParser.CompositeLiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignStatement.
    def enterAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignStatement.
    def exitAssignStatement(self, ctx:MiniGoParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#operand.
    def enterOperand(self, ctx:MiniGoParser.OperandContext):
        pass

    # Exit a parse tree produced by MiniGoParser#operand.
    def exitOperand(self, ctx:MiniGoParser.OperandContext):
        pass


    # Enter a parse tree produced by MiniGoParser#selector.
    def enterSelector(self, ctx:MiniGoParser.SelectorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#selector.
    def exitSelector(self, ctx:MiniGoParser.SelectorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#selectorExpr.
    def enterSelectorExpr(self, ctx:MiniGoParser.SelectorExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#selectorExpr.
    def exitSelectorExpr(self, ctx:MiniGoParser.SelectorExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arguments.
    def enterArguments(self, ctx:MiniGoParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arguments.
    def exitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#fieldLiteralList.
    def enterFieldLiteralList(self, ctx:MiniGoParser.FieldLiteralListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#fieldLiteralList.
    def exitFieldLiteralList(self, ctx:MiniGoParser.FieldLiteralListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#fieldLiteral.
    def enterFieldLiteral(self, ctx:MiniGoParser.FieldLiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#fieldLiteral.
    def exitFieldLiteral(self, ctx:MiniGoParser.FieldLiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MiniGoParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MiniGoParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#incDecStatement.
    def enterIncDecStatement(self, ctx:MiniGoParser.IncDecStatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#incDecStatement.
    def exitIncDecStatement(self, ctx:MiniGoParser.IncDecStatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:MiniGoParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:MiniGoParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#elementList.
    def enterElementList(self, ctx:MiniGoParser.ElementListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#elementList.
    def exitElementList(self, ctx:MiniGoParser.ElementListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arrayType.
    def enterArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arrayType.
    def exitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal.
    def enterLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal.
    def exitLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#operator.
    def enterOperator(self, ctx:MiniGoParser.OperatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#operator.
    def exitOperator(self, ctx:MiniGoParser.OperatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literalType.
    def enterLiteralType(self, ctx:MiniGoParser.LiteralTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literalType.
    def exitLiteralType(self, ctx:MiniGoParser.LiteralTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#allType.
    def enterAllType(self, ctx:MiniGoParser.AllTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#allType.
    def exitAllType(self, ctx:MiniGoParser.AllTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structLiteral.
    def enterStructLiteral(self, ctx:MiniGoParser.StructLiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structLiteral.
    def exitStructLiteral(self, ctx:MiniGoParser.StructLiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#methodSpecList.
    def enterMethodSpecList(self, ctx:MiniGoParser.MethodSpecListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methodSpecList.
    def exitMethodSpecList(self, ctx:MiniGoParser.MethodSpecListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#methodSpec.
    def enterMethodSpec(self, ctx:MiniGoParser.MethodSpecContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methodSpec.
    def exitMethodSpec(self, ctx:MiniGoParser.MethodSpecContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expressionList.
    def enterExpressionList(self, ctx:MiniGoParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expressionList.
    def exitExpressionList(self, ctx:MiniGoParser.ExpressionListContext):
        pass



del MiniGoParser