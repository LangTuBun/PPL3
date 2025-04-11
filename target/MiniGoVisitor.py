# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_list.
    def visitDecl_list(self, ctx:MiniGoParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_list_tail.
    def visitDecl_list_tail(self, ctx:MiniGoParser.Decl_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDecl.
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varSpec.
    def visitVarSpec(self, ctx:MiniGoParser.VarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeDecl.
    def visitTypeDecl(self, ctx:MiniGoParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiverComponent.
    def visitReceiverComponent(self, ctx:MiniGoParser.ReceiverComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#signature.
    def visitSignature(self, ctx:MiniGoParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameters.
    def visitParameters(self, ctx:MiniGoParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameterList.
    def visitParameterList(self, ctx:MiniGoParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameterComponent.
    def visitParameterComponent(self, ctx:MiniGoParser.ParameterComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#result.
    def visitResult(self, ctx:MiniGoParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementList.
    def visitStatementList(self, ctx:MiniGoParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementList_tail.
    def visitStatementList_tail(self, ctx:MiniGoParser.StatementList_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicStatement.
    def visitBasicStatement(self, ctx:MiniGoParser.BasicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodOrFunctionCall.
    def visitMethodOrFunctionCall(self, ctx:MiniGoParser.MethodOrFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodChain.
    def visitMethodChain(self, ctx:MiniGoParser.MethodChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#chainItems.
    def visitChainItems(self, ctx:MiniGoParser.ChainItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#chainItem.
    def visitChainItem(self, ctx:MiniGoParser.ChainItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#oneValue.
    def visitOneValue(self, ctx:MiniGoParser.OneValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MiniGoParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignOperations.
    def visitAssignOperations(self, ctx:MiniGoParser.AssignOperationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#shortValDeclaration.
    def visitShortValDeclaration(self, ctx:MiniGoParser.ShortValDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseClause.
    def visitElseClause(self, ctx:MiniGoParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forClause.
    def visitForClause(self, ctx:MiniGoParser.ForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#simpleStmt.
    def visitSimpleStmt(self, ctx:MiniGoParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRangeArray.
    def visitForRangeArray(self, ctx:MiniGoParser.ForRangeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionStmt.
    def visitExpressionStmt(self, ctx:MiniGoParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:MiniGoParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_.
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeName.
    def visitTypeName(self, ctx:MiniGoParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#indexExpr.
    def visitIndexExpr(self, ctx:MiniGoParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDeclList.
    def visitFieldDeclList(self, ctx:MiniGoParser.FieldDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodSpecList.
    def visitMethodSpecList(self, ctx:MiniGoParser.MethodSpecListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodSpec.
    def visitMethodSpec(self, ctx:MiniGoParser.MethodSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDecl.
    def visitFieldDecl(self, ctx:MiniGoParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicLiteral.
    def visitBasicLiteral(self, ctx:MiniGoParser.BasicLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:MiniGoParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compositeLiteral.
    def visitCompositeLiteral(self, ctx:MiniGoParser.CompositeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compositeLiteralValue.
    def visitCompositeLiteralValue(self, ctx:MiniGoParser.CompositeLiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elementList.
    def visitElementList(self, ctx:MiniGoParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldName.
    def visitFieldName(self, ctx:MiniGoParser.FieldNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value.
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalOr.
    def visitLogicalOr(self, ctx:MiniGoParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalAnd.
    def visitLogicalAnd(self, ctx:MiniGoParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relational.
    def visitRelational(self, ctx:MiniGoParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additive.
    def visitAdditive(self, ctx:MiniGoParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplication_division_modulo.
    def visitMultiplication_division_modulo(self, ctx:MiniGoParser.Multiplication_division_moduloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary.
    def visitUnary(self, ctx:MiniGoParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#postfix.
    def visitPostfix(self, ctx:MiniGoParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionList.
    def visitExpressionList(self, ctx:MiniGoParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#endOfSentence.
    def visitEndOfSentence(self, ctx:MiniGoParser.EndOfSentenceContext):
        return self.visitChildren(ctx)



del MiniGoParser