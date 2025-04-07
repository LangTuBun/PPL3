grammar MiniGo;

//* ===== HEADER SECTION =====
@lexer::header {
# 2252034
from lexererr import *   
}

@lexer::members {

def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None

    self.prevToken = None
    self.currentToken = None
    self.firstToken = True
    self.braceStack = []

def emit(self):
    tk = self.type

    if tk == self.UNCLOSE_STRING:       
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        print(result)
        raise ErrorToken(result.text)
    else:
        return super().emit()

def nextToken(self):
    from antlr4.Token import CommonToken

    if self.firstToken:
        self.currentToken = super().nextToken()
        while self.currentToken.type == self.NEWLINE:
            self.currentToken = super().nextToken()
        self.firstToken = False
    else:
        self.prevToken = self.currentToken
        self.currentToken = super().nextToken()
        

    

    if self.currentToken.type in [self.L_BRACKET, self.L_PARENT]:
        self.braceStack.append(self.currentToken.type)
    elif self.currentToken.type in [self.R_BRACKET, self.R_PARENT]:
        if self.braceStack:
            self.braceStack.pop()

    if self.currentToken.type == self.NEWLINE:
        if self.braceStack:
            return super().nextToken()

        if self.shouldConvertNewlineToSemiColon():
            
            

            semiToken = CommonToken((self, self._input), self.SEMI_COLON)
            semiToken.text = ";"
            semiToken.line = self.currentToken.line  
            semiToken.column = self.currentToken.column
            semiToken.channel = self.currentToken.channel
            semiToken.start = self.currentToken.start
            semiToken.stop = self.currentToken.stop
            self.prevToken = semiToken
            return semiToken
        else:
            self.prevToken = self.currentToken
            self.currentToken = super().nextToken()
            while self.currentToken.type == self.NEWLINE:
                self.currentToken = super().nextToken()
            return self.currentToken 

    self.prevToken = self.currentToken
    return self.currentToken

def shouldConvertNewlineToSemiColon(self):
    if self.prevToken is None:
        return False  
    
    lastType = self.prevToken.type

    return lastType in [
        self.ID,
        self.DECIMAL_LIT,
        self.FLOAT_LIT,
        self.BOOLEAN_LIT,
        self.STRING_LIT,
        self.OCTAL_LIT,
        self.BINARY_LIT,
        self.HEX_LIT,
        self.RETURN,
        self.CONTINUE,
        self.BREAK,
        self.INT,
        self.FLOAT,
        self.BOOLEAN,
        self.STRING,
        self.R_PARENT,
        self.R_BRACKET,
        self.R_CURLY,
        self.NIL
    ]
}




options{
    language=Python3;
}




//* ===== PARSER RULES =====
program : decl_list EOF;

decl_list :  | declaration decl_list_tail;

decl_list_tail :  | declaration decl_list_tail;



declaration: (constDecl | varDecl | typeDecl | funcDecl | methodDecl) endOfSentence;


constDecl
    : CONST ID ASSIGN expression  
    ;




varDecl
    : VAR varSpec
    ;

// varSpec
//    : ID (type_ (ASSIGN expression)? | ASSIGN expression)  
//    ;   

varSpec
    : ID type_ ASSIGN expression
    | ID type_ 
    | ID ASSIGN expression
    ;



typeDecl
    : TYPE ID (structType | interfaceType)
    ;


funcDecl
    : FUNC ID signature block
    ;


methodDecl
    : FUNC receiver ID signature block
    ;


receiver
    :  L_PARENT receiverComponent R_PARENT
    ;

receiverComponent
    : ID type_
    ;




signature
    : parameters | parameters result;


parameters
    : L_PARENT R_PARENT
    | L_PARENT parameterList R_PARENT
    ;

parameterList
    : parameterComponent 
    | parameterComponent COMMA parameterList
    ;


parameterComponent
    : identifierList type_
    ;

result
    : type_
    ;



block: L_CURLY R_CURLY | L_CURLY statementList R_CURLY ;

statementList : statement  statementList_tail;
statementList_tail: |   statement  statementList_tail;




statement   
    : declaration
    | basicStatement endOfSentence
    | returnStatement endOfSentence
    | breakStatement endOfSentence
    | continueStatement endOfSentence
    | block  
    | ifStatement
    | forStatement
    ;

basicStatement
    : assignmentStatement
    | shortValDeclaration
    | methodOrFunctionCall    
    ;




methodOrFunctionCall
    : methodChain    
    ;
    
methodChain
    : ID chainItems
    ;

chainItems: chainItem | chainItem chainItems;

chainItem
    : DOT ID        
    | index         
    | arguments     
    ;


oneValue
    : ID
    | oneValue DOT ID
    | oneValue index
    ;


assignmentStatement
    : oneValue assignOperations expression
    ;

assignOperations
    : (PLUS_ASSIGN | MINUS_ASSIGN | MULTIPLY_ASSIGN | DIVIDE_ASSIGN | MODULO_ASSIGN | ASSIGN)  
    ;




shortValDeclaration
    : oneValue DECLARE_ASSIGN expression
    ;




returnStatement
    : RETURN | RETURN expression
    ;

breakStatement
    : BREAK
    ;

continueStatement
    : CONTINUE
    ;






ifStatement 
    : IF condition block endOfSentence 
    | IF condition block elseClause
    ;

elseClause 
    : ELSE block endOfSentence
    | ELSE ifStatement
    ;



condition : L_PARENT R_PARENT  | L_PARENT expression R_PARENT;


//
//forStatement
//    : FOR expression block endOfSentence
//   | FOR forInitialization block endOfSentence
//    | FOR forRangeArray block endOfSentence
//    ;


//forInitialization
//    : (basicStatement | declaration)  expression endOfSentence basicStatement
//    ;




forStatement
    : 
    FOR expression block endOfSentence              // for condition {}
    | FOR forClause block endOfSentence               // for init; condition; post {}
    | FOR forRangeArray block endOfSentence           // for range expression {}
    ;

forClause
    : simpleStmt SEMI_COLON expression SEMI_COLON simpleStmt
    ;

simpleStmt
    : /* empty */
    | expressionStmt
    | assignment
    | shortVarDecl
    | varDecl
    ;

forRangeArray
    : identifierList DECLARE_ASSIGN RANGE expression
    ;

expressionStmt : expression;
assignment : assignmentStatement;
shortVarDecl : shortValDeclaration;





type_
    : typeName       //* Primitive or user define types (int, Person, ...)
    | arrayType        //* [5]int. [2][3]float
    | structType     // Structs (e.g., struct { ... })
    | interfaceType    // // Interfaces (e.g., interface { ... })
    ;

typeName
    : INT
    | FLOAT
    | BOOLEAN 
    | STRING
    | ID
    ;


arrayType
    : index typeName
    ;


//* Inside index: A (SINGLE) constant or integer literal
index : L_BRACKET indexExpr R_BRACKET | L_BRACKET indexExpr R_BRACKET index;

indexExpr : DECIMAL_LIT | ID |   methodOrFunctionCall | expression ;

structType 
    : STRUCT L_CURLY R_CURLY
    | STRUCT L_CURLY fieldDeclList R_CURLY
    ;


fieldDeclList 
    : fieldDecl endOfSentence
    | fieldDecl endOfSentence fieldDeclList
    ;
    



interfaceType 
    : INTERFACE L_CURLY R_CURLY
    | INTERFACE L_CURLY methodSpecList R_CURLY
    ;

methodSpecList 
    : methodSpec endOfSentence
    | methodSpec endOfSentence methodSpecList
    ;

methodSpec : ID parameters | ID parameters result;



fieldDecl
    : ID type_
    ;



identifierList : ID | ID COMMA identifierList;




literal
    : basicLiteral
    | compositeLiteral
    ;

basicLiteral
    : NIL
    | BOOLEAN_LIT
    | STRING_LIT
    | FLOAT_LIT
    | integerLiteral
    ;

integerLiteral
    : DECIMAL_LIT
    | BINARY_LIT
    | OCTAL_LIT
    | HEX_LIT
    ;


compositeLiteral : (ID | arrayType) compositeLiteralValue;

compositeLiteralValue 
    : L_CURLY R_CURLY
    | L_CURLY elementList R_CURLY
    ;

elementList 
    : element
    | element COMMA
    | element COMMA elementList
    ;

element
    : value
    | fieldName COLON value
    ;

fieldName : ID;

    
//* recursive, like {{1,2,3}, {4,5,6}}
value
    : compositeLiteralValue | expression
    ;



//* Expressions (ordered by precedence, highest to lowest)
expression
    : logicalOr
    ;

logicalOr
    : logicalAnd
    | logicalOr LOGICAL_OR logicalAnd
    ;

logicalAnd
    : relational
    | logicalAnd LOGICAL_AND relational
    ;


relational
    : additive
    | relational EQUAL additive
    | relational NOT_EQUAL additive
    | relational LESS_THAN additive
    | relational LESS_THAN_OR_EQUAL additive
    | relational GREATER_THAN additive
    | relational GREATER_THAN_OR_EQUAL additive
    ;


additive
    : multiplication_division_modulo
    | additive PLUS multiplication_division_modulo
    | additive MINUS multiplication_division_modulo
    ;


multiplication_division_modulo
    : unary
    | multiplication_division_modulo MULTIPLY unary
    | multiplication_division_modulo DIVIDE unary
    | multiplication_division_modulo MODULO unary
    ;


unary
    : postfix
    | NOT unary
    | MINUS unary
    ;

//* postfix here is just expression, the second one support field access of struct, the third one support array access, and arguments are method access of interface, or function 

postfix 
    : primaryExpr
    | postfix DOT ID    
    | postfix index
    | postfix arguments
    ;

primaryExpr
    : operand
    ;

operand
    : literal 
    | ID
    | L_PARENT expression R_PARENT
    ;



//* Function Calls
arguments 
    : L_PARENT R_PARENT
    | L_PARENT expressionList R_PARENT
    ;

expressionList 
    : expression
    | expression COMMA expressionList
    ;

endOfSentence
    : SEMI_COLON
    | EOF
    ;




//* ===== LEXER RULES - LITERALS =====
//* Number literals
DECIMAL_LIT: '0' | [1-9][0-9]*;
BINARY_LIT: '0' [bB] (BIN_DIGIT)+;
OCTAL_LIT: '0' [oO] (OCTAL_DIGIT)+ ;
HEX_LIT: '0' [xX] (HEX_DIGIT)+;
BOOLEAN_LIT: TRUE | FALSE;

FLOAT_LIT: DECIMAL_LIT '.' ((DEC_DIGIT? EXPONENT? | EXPONENT) |  DEC_DIGIT EXPONENT?)?;
STRING_LIT: '"' CHARACTER* '"'{
    result = str(self.text)
    # result = result[1:-1]
    self.text = result
};

//* ===== LEXER RULES - KEYWORDS =====
//*  Control flow keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';

//*  Function and type keywords
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';

//*  Data type keywords
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';

//*  Variable declaration keywords
CONST: 'const';
VAR: 'var';

//*  Special value keywords
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//*  ===== LEXER RULES - OPERATORS =====
//*  Arithmetic operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';

//*  Comparison operators
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';

//*  Logical operators
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
NOT: '!';

//*  Assignment operators
ASSIGN: '=';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULTIPLY_ASSIGN: '*=';
DIVIDE_ASSIGN: '/=';
MODULO_ASSIGN: '%=';


//* ===== LEXER RULES - SEPARATORS =====
COLON: ':';
SEMI_COLON: ';';
COMMA: ',';
L_PARENT: '(';
R_PARENT: ')';
L_CURLY: '{';
R_CURLY: '}';
L_BRACKET: '[';
R_BRACKET: ']';
DECLARE_ASSIGN: ':=';
DOT:'.';


//* Identifier
ID: [a-zA-Z_] ASCII_CHAR*;

//* ===== LEXER RULES - FRAGMENTS =====
fragment ASCII_CHAR: [a-zA-Z0-9_];
fragment DEC_DIGIT: [0-9]+;
fragment EXPONENT: [eE] [+-]? DECIMAL_LIT;    
fragment BIN_DIGIT: [01];
fragment OCTAL_DIGIT: [0-7];

fragment HEX_DIGIT: [0-9a-fA-F];    

fragment CHARACTER: ESC | ~["\\\r\n] | '/';
fragment ESC: '\\' [tnr"\\];
fragment ESC_ILL: '\\' ~[tnr"\\] | '\\';
fragment COMMENT_CONTENT: ~'*' | ('*' ~'/') | COMMENT_MULTI;



//* ===== LEXER RULES - WHITESPACE AND COMMENTS =====
NEWLINE: '\n';
WHITESPACE: [ \t\r]+ -> skip;
// COMMENT_MULTI: '/*' (COMMENT_CONTENT)* '*/' -> skip;
COMMENT_MULTI: '/*' (COMMENT_CONTENT)* '*/' -> skip;
LINE_COMMENT: '//' ~[\r]*   -> skip;

//* ===== LEXER RULES - ERROR HANDLING =====
// ERROR_CHAR: . {raise ErrorToken(self.text)};

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' CHARACTER*  {
    raise UncloseString(self.text)  
};
ILLEGAL_ESCAPE: '"' CHARACTER* ESC_ILL  {
    raise IllegalEscape(self.text[1:]) 
};