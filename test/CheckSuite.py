import unittest
from TestUtils import TestChecker
from AST import *
import inspect
class CheckSuite(unittest.TestCase):
    # def test_redeclared(self):
    #     input = """var a int; var b int; var a int; """
    #     expect = "Redeclared Variable: a\n"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_type_mismatch(self):
    #     input = """var a int = 1.2;"""
    #     expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_undeclared_identifier(self):
    #     input = Program([VarDecl("a",IntType(),Id("b"))])
    #     expect = "Undeclared Identifier: b\n"
    #     self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))


    
    # def test_001(self):
    #     input = """
    #         var a int;
    #         func b(){};
    #         const a int = 1
    #     """
    #     expect = "Redeclared Constant: a\n"
    #     self.assertTrue(
    #         TestChecker.test(input,expect,inspect.stack()[0].function)
    #     )
    
    # def test_002(self):
    #     input = """
    #         var a int = 5;
    #         var b float = a;
    #     """
    #     expect  = ""
    #     self.assertTrue(
    #         TestChecker.test(input,expect, inspect.stack()[0].function)
    #     )
    
    # def test_003(self):
    #     input = """
    #         var a int = 5;
    #         var b string = a;
    #     """
    #     expect = "Type Mismatch: VarDecl(b,StringType,Id(a))\n"
    #     self.assertTrue(
    #         TestChecker.test(input,expect, inspect.stack()[0].function)
    #     )

    # def test_004(self):
    #     input = """
    #         func foo(){
    #             var x int;
    #             var x float;
    #         }
    #     """
    #     expect = "Redeclared Variable: x\n"
    #     self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
  
    # def test_005(self):
    #     """
    #     LHS is float, so assignment of int is okela
    #     """
    #     input = """
    #         func foo(x int) {
    #             var y int = x + 1;
    #             var z float = y + 1.5;  // Valid type conversion
    #         }
    #     """
    #     expect = ""  # No error
    #     self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # def test_006(self):

    #     input = """
    #     func foo(x int, y float){
    #         var z int = y;
    #     }
    #     """
    #     expect = "Type Mismatch: VarDecl(z,IntType,Id(y))\n"
    #     self.assertTrue(
    #         TestChecker.test(
    #             input, expect, inspect.stack()[0].function
    #         )
    #     )

    # def test_007(self):
    #     input = """
    #         func foo(){
    #             var a int = 5;
    #             if (true){
    #                 var a float = 3.14;
    #             }
    #         }
    #     """
    #     expect = ""
    #     self.assertTrue(
    #         TestChecker.test(
    #             input, expect, inspect.stack()[0].function
    #         )
    #     )
    
    # def test_008(self):
    #     input = """
    #         func foo(){
    #             a := 5;
    #         }
    #     """
    #     expect = ""
    #     self.assertTrue(
    #         TestChecker.test(
    #             input, expect, inspect.stack()[0].function
    #         )
    #     )
    #     def test_for_loop(self):
    #         input = """
    #             func foo(){
    #                 for i := 0; i < 10; i += 1 {
    #                     var a int = i;
    #                 }
    #             }
    #         """
    #         expect = ""
    #         self.assertTrue(
    #             TestChecker.test(
    #                 input, expect, inspect.stack()[0].function
    #             )
    #         )
    # def test_same_var_inside_and_outside_func(self):
    #     input = """var a int; func b(){var a int;};"""
    #     expect = ""  # no error
    #     self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # def test_struct_redeclared(self):
    #     input = """type a struct{}; type a struct{};"""
    #     expect = "Redeclared Type: a\n"
    #     self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    # def test_interface_redeclared(self):
    #     input = """type a interface{}; type a interface {};"""
    #     expect = "Redeclared Type: a\n"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

   	

    # def test_duplicate_prototype_in_interface(self):
    #     input = """type a interface{
    #                 getName(a int) ;
    #                 getName(a int, b int, c float);
    #             };"""
    #     expect = "Redeclared Prototype: getName\n"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_same_field_in_struct(self):
    #     input = """type a struct{
    #                 x int;
    #                 y int;
    #                 x int;
    #             };"""
    #     expect = "Redeclared Field: x\n"
    #     self.assertTrue(TestChecker.test(input, expect, 411))


    # def test_undeclared_method_call(self):
    #     input = """type Person struct{};
    #             var p Person;
    #             //func (p Person) greet() {
    #             //};
    #             func main() {
    #                 p.greet();
    #             }"""
    #     expect = "Undeclared Method: greet\n"
    #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test_undeclared_field(self):
    #     input = """type a struct{
    #                 y int;
    #             };
    #             func b(){
    #                 var c a;
    #                 c.x := 5;
    #                 };"""
    #     expect = "Undeclared Field: x\n"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test_declared_field(self):
    #     input = """type A struct{
    #                 x int;
    #                 y int;
    #             };
    #             func b(){
    #                 var a A;
    #                 a.x := 5;
    #             };"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test_undeclared_var_access_struct(self):
    #     input = """type a struct{
    #                 x int;
    #                 y int;
    #             };
    #             func b(){c.x := 5;};"""
    #     expect = "Undeclared Identifier: c\n"
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    def test_wrong_struct_type_access(self):
        input = """type a struct{
                    x int;
                    y int;
                };
                func b(){
                    var c int;
                    c.x := 5;
                };"""
        expect = "Type Mismatch: Id(c)\n"
        self.assertTrue(TestChecker.test(input, expect, 420))



    def test_assignment_left_side_void(self):
        input = """func a(){};
                func main(){
                    var x int;
                    x := a();
                };"""
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 421))


    def test_assignment_float_to_int(self):
        input = """var a int;
                func main(){
                    a = 5.5;
                };"""
        expect = "Type Mismatch: Assign(Id(a),FloatLiteral(5.5))\n"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_assignment_same_type(self):
        input = """var a int;
                func main(){
                    a := 5;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_assignment_array_to_array_different_size(self):
        input = """var a [0]int;
                var b [10]int;
                func main(){
                    a := b;
                };"""
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_assignment_arrayliteral_to_array(self):
        input = """var a [5] int;
                func main(){
                    a := [5] int {1,2,3,4,5};
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_assignment_array_different_type(self):
        input = """var a [5] int;
                var b [5] float;
                func main(){
                    a := b;
                };"""
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_struct_to_interface(self):
        input = """type a struct{};
                type b interface{};
                func main(){
                    var x a;
                    var y b;
                    y := x;
                };"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

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
        self.assertTrue(TestChecker.test(input, expect, 430))

    # def test_undeclared_assignment(self):
    #     input = """func main(){
    #                 a := 5;
    #             };"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # # # TODO: TYPE MISMATCH IN DECLARATION

    def test_type_mismatch_vardecl(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_constdecl(self):
        input = """const a int = 1.2;"""
        expect = "Type Mismatch: ConstDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 433))

    # # # TODO: CONDITIONAL: IF & FOR
    # def test_if_not_boolean(self):
    #     input = """func main(){
    #                 if (5) {
    #                 }
    #             };"""
    #     expect = "Type Mismatch: If(IntLiteral(5),Block([]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test_if_not_boolean_2(self):
    #     input = """func main(){
    #                 var a boolean = true;
    #                 if (a) {
    #                 }
    #             };"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # # bool chưa khai báo thì sao?
    # def test_if_not_boolean_3(self):
    #     input = """func main(){
    #                 if (a) {
    #                 }
    #             };"""
    #     expect = "Undeclared Identifier: a\n"
    #     self.assertTrue(TestChecker.test(input, expect, 451))

    # def test_for_loop(self):
    #     input = """func main(){
    #                 for i := "str"; i < 10; i += 1 {
    #                 }
    #             };"""
    #     expect = "Type Mismatch: BinaryOp(Id(i),<,IntLiteral(10))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # # TODO: FUNCTION/METHOD CALL STATEMENT -> VOID;;; FUNCTION/METHOD CALL EXPRESSION -> NOT VOID
    # def test_function_call_statement(self):
    #     input = """func a() int {
    #     return 1;};
    #             func main(){
    #                 a();
    #             };"""
    #     expect = "Type Mismatch: FuncCall(a,[])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test_function_call_expression(self):
    #     input = """func a(){};
    #             func main(){
    #                 a := a();
    #             };"""
    #     expect = "Type Mismatch: FuncCall(a,[])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test_wrong_function_argument(self):
    #     input = """func a(b int){};
    #             func main(){
    #                 a("string");
    #             };"""
    #     expect = 'Type Mismatch: FuncCall(a,[StringLiteral("string")])\n'
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test_wrong_function_argument_number(self):
    #     input = """func a(b int, c float){};
    #             func main(){
    #                 a(1);
    #             };"""
    #     expect = "Type Mismatch: FuncCall(a,[IntLiteral(1)])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test_method_call_wrong_object(self):
    #     input = """
    #             func main(){
    #                 var c int;
    #                 c.b();
    #             };"""
    #     expect = "Type Mismatch: MethodCall(Id(c),b,[])\n"
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # # TODO: return voidtype & function type mismatch
    # def test_function_call_assignment(self):
    #     input = """func a(){
    #                 return 1;
    #             };"""
    #     expect = (
    #         "Type Mismatch: FuncDecl(a,[],VoidType,Block([Return(IntLiteral(1))]))\n"
    #     )
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # def test_type_int_return_void(self):
    #     input = """func a() int {
    #         return;
    #     }
    #     """
    #     expect = "Type Mismatch: FuncDecl(a,[],IntType,Block([Return()]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test_funtion_type_and_return_type_mismatch(self):
    #     input = """func a() int {
    #                 return "string";
    #             }"""
    #     expect = "Type Mismatch In Statement: Return([StringLiteral(string)])"
    #     self.assertTrue(TestChecker.test(input, expect, 445))

    # def test_return_two_different_type(self):
    #     input = """func a() {
    #                 return;
    #                 return 5;
    #                 // check hết cả 2 return
    #             }"""
    #     expect = "Type Mismatch: FuncDecl(a,[],VoidType,Block([Return(IntLiteral(5))]))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test_array_subscript_wrong_type(self):
    #     input = """
    #             var a [5] int;
    #         func main(){
    #             a["string"] := 5;
    #         }"""
    #     expect = 'Type Mismatch: ArrayCell(Id(a),[StringLiteral("string")])\n'
    #     self.assertTrue(TestChecker.test(input, expect, 446))

    # def test_array_subscript_wrong_type_2(self):
    #     input = """var a int = 5;
    #         int main(){
    #             a[5] := 5;
    #         }"""
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
    #     self.assertTrue(TestChecker.test(input, expect, 447))

    # # TODO: STRUCT ACCESS
    # def test_struct_access_wrong_type(self):
    #     input = """type a struct{
    #                 x int;
    #                 y int;
    #             };
    #             func main(){
    #                 var c int;
    #                 c.x := 5;
    #             };"""
    #     expect = "Type Mismatch: FieldAccess(Id(c),x)\n"
    #     self.assertTrue(TestChecker.test(input, expect, 448))

    # def test_binary_expression_type_mismatch(self):
    #     input = """func main(){
    #                 var a int;
    #                 var b string;
    #                 a := a + b;
    #             }"""
    #     expect = (
    #         "Type Mismatch: BinaryOp(Id(a),+,Id(b))\n"
    #     )
    #     self.assertTrue(TestChecker.test(input, expect, 449))

    # def test_binary_expression_type_mismatch_2(self):
    #     input = """func main(){
    #                 var a string = "string";
    #                 var b int = -a;
    #             }"""
    #     expect = "Type Mismatch: UnaryOp(-,Id(a))\n"
    #     self.assertTrue(TestChecker.test(input, expect, 450))

 
    # def test_multiple_subscript_wrong(self):
    #     input = """
    #         var a [5][2] int;
    #         func main(){
    #             a[1]["test"] := 5;
    #         }"""
    #     expect = 'Type Mismatch: ArrayCell(Id(a),[IntLiteral(1),StringLiteral("test")])\n'
    #     self.assertTrue(TestChecker.test(input, expect, 452))