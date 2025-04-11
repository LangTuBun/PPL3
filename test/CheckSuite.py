import unittest
from TestUtils import TestChecker
from AST import *
import inspect
class CheckSuite(unittest.TestCase):
    def test_redeclared(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))

    def test_type_mismatch(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))


    
    def test_001(self):
        input = """
            var a int;
            func b(){};
            const a int = 1
        """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(
            TestChecker.test(input,expect,inspect.stack()[0].function)
        )
    
    def test_002(self):
        input = """
            var a int = 5;
            var b float = a;
        """
        expect  = ""
        self.assertTrue(
            TestChecker.test(input,expect, inspect.stack()[0].function)
        )
    
    def test_003(self):
        input = """
            var a int = 5;
            var b string = a;
        """
        expect = "Type Mismatch: VarDecl(b,StringType,Id(a))\n"
        self.assertTrue(
            TestChecker.test(input,expect, inspect.stack()[0].function)
        )

    def test_004(self):
        input = """
            func foo(){
                var x int;
                var x float;
            }
        """
        expect = "Redeclared Variable: x\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
  
    def test_005(self):
        """
        LHS is float, so assignment of int is okela
        """
        input = """
            func foo(x int) {
                var y int = x + 1;
                var z float = y + 1.5;  // Valid type conversion
            }
        """
        expect = ""  # No error
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_006(self):

        input = """
        func foo(x int, y float){
            var z int = y;
        }
        """
        expect = "Type Mismatch: VarDecl(z,IntType,Id(y))\n"
        self.assertTrue(
            TestChecker.test(
                input, expect, inspect.stack()[0].function
            )
        )

    def test_007(self):
        input = """
            func foo(){
                var a int = 5;
                if (true){
                    var a float = 3.14;
                }
            }
        """
        expect = ""
        self.assertTrue(
            TestChecker.test(
                input, expect, inspect.stack()[0].function
            )
        )
    
    def test_008(self):
        input = """
            func foo(){
                a := 5;
            }
        """
        expect = ""
        self.assertTrue(
            TestChecker.test(
                input, expect, inspect.stack()[0].function
            )
        )
    def test_for_loop1(self):
        input = """
            func foo(){
                for i := 0; i < 10; i += 1 {
                    var a int = i;
                }
            }
        """
        expect = ""
        self.assertTrue(
            TestChecker.test(
                input, expect, inspect.stack()[0].function
            )
        )
    def test_same_var_inside_and_outside_func(self):
        input = """var a int; func b(){var a int;};"""
        expect = ""  # no error
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_struct_redeclared(self):
        input = """type a struct{}; type a struct{};"""
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_interface_redeclared(self):
        input = """type a interface{}; type a interface {};"""
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

   	

    def test_duplicate_prototype_in_interface(self):
        input = """type a interface{
                    getName(a int) ;
                    getName(a int, b int, c float);
                };"""
        expect = "Redeclared Prototype: getName\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_same_field_in_struct(self):
        input = """type a struct{
                    x int;
                    y int;
                    x int;
                };"""
        expect = "Redeclared Field: x\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_undeclared_method_call(self):
        input = """type Person struct{};
                var p Person;
                //func (p Person) greet() {
                //};
                func main() {
                    p.greet();
                }"""
        expect = "Undeclared Method: greet\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_undeclared_field(self):
        input = """type a struct{
                    y int;
                };
                func b(){
                    var c a;
                    c.x := 5;
                    };"""
        expect = "Undeclared Field: x\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_declared_field(self):
        input = """type A struct{
                    x int;
                    y int;
                };
                func b(){
                    var a A;
                    a.x := 5;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_undeclared_var_access_struct(self):
        input = """type a struct{
                    x int;
                    y int;
                };
                func b(){c.x := 5;};"""
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_wrong_struct_type_access(self):
        input = """type a struct{
                    x int;
                    y int;
                };
                func b(){
                    var c int;
                    c.x := 5;
                };"""
        expect = "Type Mismatch: FieldAccess(Id(c),x)\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))



    def test_assignment_left_side_void(self):
        input = """func a(){};
                func main(){
                    var x int;
                    x := a();
                };"""
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_assignment_float_to_int(self):
        input = """var a int;
                func main(){
                    a := 5.5;
                };"""
        expect = "Type Mismatch: Assign(Id(a),FloatLiteral(5.5))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_same_type(self):
        input = """var a int;
                func main(){
                    a := 5;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_array_to_array_different_size(self):
        input = """var a [1]int;
                var b [10]int;
                func main(){
                    a = b;
                };"""
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_arrayliteral_to_array(self):
        input = """var a [5] int;
                func main(){
                    a := [5] int {1,2,3,4,5};
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_array_different_type(self):
        input = """var a [5] int;
                var b [5] float;
                func main(){
                    a := b;
                };"""
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_struct_to_interface(self):
        input = """type a struct{};
                type b interface{};
                func main(){
                    var x a;
                    var y b;
                    y := x;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_struct_to_interface_missing_method(self):
        input = """type a struct{};
                type b interface{
                    m();
                };
                func main(){
                    var x a;
                    var y b;
                    y := x;
                };"""
        expect = "Type Mismatch: Assign(Id(y),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_undeclared_assignment(self):
        input = """func main(){
                    a := 5;     
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_type_mismatch_constdecl(self):
        input = """const a int = 1.2;"""
        expect = "Type Mismatch: ConstDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
    def test_type_mismatch_vardecl(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


#     # # # TODO: CONDITIONAL: IF & FOR
    def test_if_not_boolean(self):
        input = """func main(){
                    if (5) {
                    }
                };"""
        expect = "Type Mismatch: If(IntLiteral(5),Block([]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_if_not_boolean_2(self):
        input = """func main(){
                    var a boolean = true;
                    if (a) {
                    }
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

#     # # bool chưa khai báo thì sao?
    def test_if_not_boolean_3(self):
        input = """func main(){
                    if (a) {
                    }
                };"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_for_loop(self):
        input = """func main(){
                    for i := "str"; i < 10; i += 1 {
                    };
                };"""
        expect = "Type Mismatch: BinaryOp(Id(i),<,IntLiteral(10))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # # TODO: FUNCTION/METHOD CALL STATEMENT -> VOID;;; FUNCTION/METHOD CALL EXPRESSION -> NOT VOID
    def test_function_call_statement(self):
        input = """func a() int {
        return 1;};
                func main(){
                    a();
                };"""
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_function_call_expression(self):
        input = """func a(){};
                func main(){
                    a := a();
                };"""
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_wrong_function_argument(self):
        input = """func a(b int){};
                func main(){
                    a("string");
                };"""
        expect = 'Type Mismatch: FuncCall(a,[StringLiteral("string")])\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_binary_expression_type_mismatch_2(self):
        input = """func main(){
                    var a string = "string";
                    var b int = -a;
                }"""
        expect = "Type Mismatch: UnaryOp(-,Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_wrong_function_argument_number(self):
        input = """func a(b int, c float){};
                func main(){
                    a(1);
                };"""
        expect = "Type Mismatch: FuncCall(a,[IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_method_call_wrong_object(self):
        input = """
                func main(){
                    var c int;
                    c.b();
                };"""
        expect = "Type Mismatch: MethodCall(Id(c),b,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    
    
    def test_function_call_assignment(self):
        input = """func a()  {
                    return 1;
                };"""
        expect = (
            "Type Mismatch: FuncDecl(a,[],VoidType,Block([Return(IntLiteral(1))]))\n"
        )
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_type_int_return_void(self):
        input = """func a() int {
            return;
        }
        """
        expect = "Type Mismatch: FuncDecl(a,[],IntType,Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        

 

    def test_funtion_type_and_return_type_mismatch(self):
        input = """func a() int {
                    return "string";
                }"""
        expect = "Type Mismatch: FuncDecl(a,[],IntType,Block([Return(StringLiteral(\"string\"))]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))


    def test_return_two_different_type(self):
        input = """func a() {
                    return ;
                    return 5;
                  
                }"""
        expect = "Type Mismatch: FuncDecl(a,[],VoidType,Block([Return(),Return(IntLiteral(5))]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_array_subscript_wrong_type(self):
        input = """
            func main(){
                var a[5] int;
                a["string"] := 5;
            }"""
        expect = 'Type Mismatch: ArrayCell(Id(a),[StringLiteral("string")])\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_array_subscript_wrong_type_2(self):
        input = """
            func main int (){
                var a int = 5;
                a[5] := 5;
            }"""
        expect = "Type Mismatch: ArrayCell(Id(a),[IntLiteral(5)])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_struct_access_wrong_type(self):
        input = """type a struct{
                    x int;
                    y int;
                };
                func main(){
                    var c int;
                    c.x := 5;
                };"""
        expect = "Type Mismatch: FieldAccess(Id(c),x)\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_binary_expression_type_mismatch(self):
        input = """func main(){
                    var a int;
                    var b string;
                    a := a + b;
                }"""
        expect = (
            "Type Mismatch: BinaryOp(Id(a),+,Id(b))\n"
        )
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_multiple_subscript_wrong(self):
        input = """
            var a [5][2] int;
            func main(){
                a[1]["test"] := 5;
            }"""
        expect = 'Type Mismatch: ArrayCell(Id(a),[IntLiteral(1),StringLiteral("test")])\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
        
    def test_0022(self):
        input =   """
                var luukimLKNG int = 1; 
                const luukimLKNG int = 2;
            """
        expect = "Redeclared Constant: luukimLKNG\n"
        print(expect)
        self.assertTrue(TestChecker.test(input,expect , inspect.stack()[0].function))
    def test_0044(self):
        """
            const luukimLKNG = 1; 
            func luukimLKNG () {return;}
        """
        input = Program([ConstDecl("luukimLKNG",None,IntLiteral(1)),FuncDecl("luukimLKNG",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: luukimLKNG\n", inspect.stack()[0].function))

    def test_005(self):
        """ 
            func luukimLKNG () {return;}
            var luukimLKNG = 1;
        """
        input = Program([FuncDecl("luukimLKNG",[],VoidType(),Block([Return(None)])),VarDecl("luukimLKNG", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: luukimLKNG\n", inspect.stack()[0].function))


    def test_007(self):
        """ 
            type  bena struct {
                bena int;
            }
            type LKNG struct {
                bena string;
                LKNG int;
                LKNG float;
            }
        """
        input = Program([StructType("bena",[("bena",IntType())],[]),StructType("LKNG",[("bena",StringType()),("LKNG",IntType()),("LKNG",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: LKNG\n", inspect.stack()[0].function))

    def test_0008(self):
        """ 
func (v LKNG) putIntLn () {return;}
func (v LKNG) getInt () {return;}
func (v LKNG) getInt () {return;
type LKNG struct {
    bena int;
}
        """
        input = Program([MethodDecl("v",Id("LKNG"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("LKNG"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("LKNG"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("LKNG",[("bena",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", inspect.stack()[0].function))

    def test_009(self):
        """ 
type luukimLKNG interface {
    luukimLKNG ();
    luukimLKNG (a int);
}
        """
        input = Program([InterfaceType("luukimLKNG",[Prototype("luukimLKNG",[],VoidType()),Prototype("luukimLKNG",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: luukimLKNG\n", inspect.stack()[0].function))

    def test_010(self):
        """ 
func bena (a, a int) {return;}
        """
        input = Program([FuncDecl("bena",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", inspect.stack()[0].function))

    def test_011(self):
        """ 
func bena (b int) {
    var b = 1;
    var a = 1;
    const a = 1;
}
        """
        input = Program([FuncDecl("bena",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", inspect.stack()[0].function))

    def test_012(self):
        """ 
func bena (b int) {
    for var a = 1; a < 1; a += 1 {
        const a = 2;
    }
}
        """
        input = Program([FuncDecl("bena",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", inspect.stack()[0].function))
    def test_013(self):
        """ 
var a = 1;
var b = a;
var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", inspect.stack()[0].function))
        
    def test_014(self):
        """ 
func bena () int {return 1;}

fun foo () {
    var b = bena();
    foo_votine();
    return;
}
        """
        input = Program([FuncDecl("bena",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("bena",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine\n", inspect.stack()[0].function))

    def test_015(self):
        """ 
type LKNG struct {
    bena int;
}

func (v LKNG) getInt () {
    const c = v.bena;
    var d = v.LKNG;
}
        """
        input = Program([StructType("LKNG",[("bena",IntType())],[]),MethodDecl("v",Id("LKNG"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"bena")),VarDecl("d", None,FieldAccess(Id("v"),"LKNG"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: LKNG\n", inspect.stack()[0].function))
    def test_029(self):
        """
var a [2][3] int;
var b = a[1][2];
var c int = b;
var d [1] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",IntType(),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(d,ArrayType(StringType,[IntLiteral(1)]),Id(b))\n""", inspect.stack()[0].function)) 
    
    def test_030(self):
        """
type S1 struct {v int; x S1;}
var b S1;
var c = b.x.v;
var d = c.x;
        """
        input = Program([StructType("S1",[("v",IntType()),("x",Id("S1"))],[]),VarDecl("b",Id("S1"), None),VarDecl("c", None,FieldAccess(FieldAccess(Id("b"),"x"),"v")),VarDecl("d", None,FieldAccess(Id("c"),"x"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FieldAccess(Id(c),x)\n""", inspect.stack()[0].function)) 
        
    def test_041(self):
        """
            type S1 struct {bena int;}
            func (s S1) bena() int {
            s.bena();
            return 1;
        }
        """
        input = Program([StructType("S1",[("bena",IntType())],[]),MethodDecl("s",Id("S1"),FuncDecl("bena",[],IntType(),Block([MethCall(Id("s"),"bena",[]),Return(IntLiteral(1))])))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: bena\n""", inspect.stack()[0].function)) 
        

    def test_method_call_wrong_object(self):
        input = """
                func main(){
                    var c int;
                    c.b();
                };"""
        expect = "Type Mismatch: MethodCall(Id(c),b,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # # TODO: return voidtype & function type mismatch
    def test_function_call_assignment(self):
        input = """func a(){
                    return 1;
                };"""
        expect = (
            "Type Mismatch: FuncDecl(a,[],VoidType,Block([Return(IntLiteral(1))]))\n"
        )
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_type_int_return_void(self):
        input = """func a() int {
            return;
        }
        """
        expect = "Type Mismatch: FuncDecl(a,[],IntType,Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_funtion_type_and_return_type_mismatch(self):
        input = """func a() int {
                    return "string";
                }"""
        expect = 'Type Mismatch: FuncDecl(a,[],IntType,Block([Return(StringLiteral("string"))]))\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # TODO: 1 FUNCTION CÓ 2 RETURN THÌ SAO
    def test_return_two_different_type(self):
        input = """func a() int {
                    return 5;
                    return "string";
                }"""
        expect = 'Type Mismatch: FuncDecl(a,[],IntType,Block([Return(IntLiteral(5)),Return(StringLiteral("string"))]))\n'

        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # TODO: ARRAY SUBSCRIPTING
    def test_array_subscript_wrong_type(self):
        input = """
                var a [5] int;
            func main(){
                a["string"] := 5;
            }"""
        expect = 'Type Mismatch: ArrayCell(Id(a),[StringLiteral("string")])\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_array_subscript_wrong_type_2(self):
        input = """var a int = 5;
            func main(){
                a[5] := 5;
            }"""
        expect = "Type Mismatch: ArrayCell(Id(a),[IntLiteral(5)])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_for_loop_wtf_2(self):
        input = """
            func main() {
                for i := 0; a < 10; i += 1 {
                    var a int;
                    a := 5;
                }
            }
        """
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_arr_with_for_loop(self):
        input = """
            func main() {
                var a [5] int;
                for i, x := range a {
                    var a int;
                }
            }
        """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_unary_combined(self):
        input = """
            func main() {
                var a int;
                a := -5;
                var b boolean;
                b := !true && false;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_a_lot_of_const(self):
        input = """
            const a int = 1;
            const b int = 2;
            const c int = 3;
            const d int = 4;
            const e int = 5;
            const f int = 6;
            const g int = 7;
            const h int = 8;
            const i int = 9;
            const j int = 10;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_array_literal_69(self):
        input = """
            func main() {
                var a [5] int;
                a := [5]int{1, 2, 3, 4, 5};
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_built_in_function(self):
        input = """
            func main() {
                var a int;
                a := getInt();
                putInt(a);
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_multi_argument_function(self):
        input = """
            func alotOfArguments(a int, b float, c string) {
                var d int;
                d := a + 5;
            }

            func main() {
                var a int;
                alotOfArguments(a, 2.0, "string");
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_multi_argument_function_2(self):
        input = """
            func alotOfArguments(a int, b float, c string) {
                var d int;
                d := a + 5;
            }

            func main() {
                var a int;
                alotOfArguments(2.1, 0, "string");
            }
        """
        expect = 'Type Mismatch: FuncCall(alotOfArguments,[FloatLiteral(2.1),IntLiteral(0),StringLiteral("string")])\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_function_return_array(self):
        input = """
            func returnArray() [5]int {
                return [5]int{1, 2, 3, 4, 5};
            }
            func main() {
                var a [5]int;
                a := returnArray();
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_function_return_struct(self):
        input = """
            type A struct {
                x int;
                y float;
            }

            func returnStruct() A {
                return A{x: 1, y: 2.0};
            }

            func main() {
                var a A;
                a := returnStruct();
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # OKAY
    def test_normal_program(self):
        input = """
            func main() {
                var a int;
                a := 5;
                putInt(a);
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # okay
    def test_array_in_struct(self):
        input = """
            type A struct {
                x [5] int;
            }

            func main() {
                var a A;
                a.x[0] := 5;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # okay
    def test_array_in_struct_2(self):
        input = """
            type A struct {
                x [5] int;
            }

            func main() {
                var a A = A{x: [5]int{1, 2, 3, 4, 5}};
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    ###okay
    def test_const_with_type(self):
        input = """
            const a int = 5;
            const b float = 3.14;
            const c string = "hello";
            const d boolean = true;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_funny_program(self):
        input = """
            func main() {
                var a int;
                a := 5;
                putInt(a);
                putStringLn("Hello, World!");
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_funny_program_2(self):
        input = """
            func main() {
                var a int;
                a := 5;
                putInt(a);
                putString("Hello, World!");
                putString("Hello, World!");
                putString("Hello, World!");
                putString("Hello, World!");
                putString();
            }
        """
        expect = "Type Mismatch: FuncCall(putString,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_everything(self):
        input = """
            func main() {
                var a int;
                a := 5 + 4.0;
                putInt(a);
            }"""
        expect = (
            "Type Mismatch: Assign(Id(a),BinaryOp(IntLiteral(5),+,FloatLiteral(4.0)))\n"
        )
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_string_operations(self):
        input = """
            func main() {
                var a string;
                a := "Hello" + "World";
                putString(a);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_for_loop_an_array_to_calculate_total(self):
        input = """
            func main() {
                var a [5] int;
                var total int;
                for i := 0; i < 5; i+=1 {
                    total := total + a[i];
                }
                putInt(total);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_last_test(self):
        input = """
            func main() {
                var a int;
                a := 5;
                putInt(a);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_assignment_array_to_array(self):
        input = """var a [5] int;
                var b [5] int;
                func main(){
                    a := b;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_array_to_array_different_sizepleee(self):
        input = """var a [5]int;
                var b [10]int;
                func main(){
                    a := b;
                };"""
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_arrayliteral_to_arrayttt(self):
        input = """var a [5] int;
                func main(){
                    a := [5]int {1,2,3,4,5};
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_assignment_array_different_typeeee(self):
        input = """var a [5] int;
                var b [5] float;
                func main(){
                    a := b;
                };"""
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_struct_to_interfaceeeee(self):
        input = """type a struct{};
                type b interface{};
                func main(){
                    var x a;
                    var y b;
                    y := x;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_struct_to_interface_missing_methhhhhod(self):
        input = """type a struct{};
                type b interface{
                    m();
                };
                func main(){
                    var x a;
                    var y b;
                    y := x;
                };"""
        expect = "Type Mismatch: Assign(Id(y),Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_undeclared_assignmmmment(self):
        input = """func main(){
                    a := 5;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # # # TODO: TYPE MISMATCH IN DECLARATION

    def test_type_mismatch_varrrdecl(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_type_mismatch_connnstdecl(self):
        input = """const a int = 1.2;"""
        expect = "Type Mismatch: ConstDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_if_not_booleeeean(self):
        input = """func main(){
                    if (5) {
                    }
                };"""
        expect = "Type Mismatch: If(IntLiteral(5),Block([]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_if_not_boolean_222(self):
        input = """func main(){
                    var a boolean = true;
                    if (a) {
                    }
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_if_not_boolean_333(self):
        input = """func main(){
                    if (a) {
                    }
                };"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_for_looppp(self):
        input = """func main(){
                    for i := "str"; i < 10; i += 1 {
                    }
                };"""
        expect = "Type Mismatch: BinaryOp(Id(i),<,IntLiteral(10))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_function_call_statemennnt(self):
        input = """func a() int {
        return 1;};
                func main(){
                    a();
                };"""
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_function_call_expressionnn(self):
        input = """func a(){};
                func main(){
                    a := a();
                };"""
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_wrong_function_argumennt(self):
        input = """func a(b int){};
                func main(){
                    a("string");
                };"""
        expect = 'Type Mismatch: FuncCall(a,[StringLiteral("string")])\n'
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))





        