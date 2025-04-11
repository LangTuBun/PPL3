# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# 2252034
from lexererr import *   



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\2\7\2\u009f\n\2\f\2\16\2\u00a2\13\2")
        buf.write("\5\2\u00a4\n\2\3\3\3\3\3\3\6\3\u00a9\n\3\r\3\16\3\u00aa")
        buf.write("\3\4\3\4\3\4\6\4\u00b0\n\4\r\4\16\4\u00b1\3\5\3\5\3\5")
        buf.write("\6\5\u00b7\n\5\r\5\16\5\u00b8\3\6\3\6\5\6\u00bd\n\6\3")
        buf.write("\7\3\7\3\7\5\7\u00c2\n\7\3\7\5\7\u00c5\n\7\3\7\5\7\u00c8")
        buf.write("\n\7\3\7\3\7\5\7\u00cc\n\7\5\7\u00ce\n\7\3\b\3\b\7\b\u00d2")
        buf.write("\n\b\f\b\16\b\u00d5\13\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3")
        buf.write("<\3<\7<\u019b\n<\f<\16<\u019e\13<\3=\3=\3>\6>\u01a3\n")
        buf.write(">\r>\16>\u01a4\3?\3?\5?\u01a9\n?\3?\3?\3@\3@\3A\3A\3B")
        buf.write("\3B\3C\3C\3C\5C\u01b6\nC\3D\3D\3D\3E\3E\3E\5E\u01be\n")
        buf.write("E\3F\3F\3F\3F\5F\u01c4\nF\3G\3G\3H\6H\u01c9\nH\rH\16H")
        buf.write("\u01ca\3H\3H\3I\3I\3I\3I\7I\u01d3\nI\fI\16I\u01d6\13I")
        buf.write("\3I\3I\3I\3I\3I\3J\3J\3J\3J\7J\u01e1\nJ\fJ\16J\u01e4\13")
        buf.write("J\3J\3J\3K\3K\3K\3L\3L\7L\u01ed\nL\fL\16L\u01f0\13L\3")
        buf.write("L\3L\3M\3M\7M\u01f6\nM\fM\16M\u01f9\13M\3M\3M\3M\2\2N")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d>\u008f?\u0091@\u0093A\u0095B\u0097C\u0099")
        buf.write("D\3\2\24\3\2\63;\3\2\62;\4\2DDdd\4\2QQqq\4\2ZZzz\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\4\2GGgg\4\2--//\3\2\62\63\3\2\62")
        buf.write("9\5\2\62;CHch\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\3\2,,\3")
        buf.write("\2\61\61\5\2\13\13\17\17\"\"\3\2\17\17\2\u020c\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u00a3\3\2\2\2\5\u00a5")
        buf.write("\3\2\2\2\7\u00ac\3\2\2\2\t\u00b3\3\2\2\2\13\u00bc\3\2")
        buf.write("\2\2\r\u00be\3\2\2\2\17\u00cf\3\2\2\2\21\u00d9\3\2\2\2")
        buf.write("\23\u00dc\3\2\2\2\25\u00e1\3\2\2\2\27\u00e5\3\2\2\2\31")
        buf.write("\u00ec\3\2\2\2\33\u00f5\3\2\2\2\35\u00fb\3\2\2\2\37\u0101")
        buf.write("\3\2\2\2!\u0106\3\2\2\2#\u010b\3\2\2\2%\u0112\3\2\2\2")
        buf.write("\'\u011c\3\2\2\2)\u0123\3\2\2\2+\u0127\3\2\2\2-\u012d")
        buf.write("\3\2\2\2/\u0135\3\2\2\2\61\u013b\3\2\2\2\63\u013f\3\2")
        buf.write("\2\2\65\u0143\3\2\2\2\67\u0148\3\2\2\29\u014e\3\2\2\2")
        buf.write(";\u0150\3\2\2\2=\u0152\3\2\2\2?\u0154\3\2\2\2A\u0156\3")
        buf.write("\2\2\2C\u0158\3\2\2\2E\u015b\3\2\2\2G\u015e\3\2\2\2I\u0160")
        buf.write("\3\2\2\2K\u0163\3\2\2\2M\u0165\3\2\2\2O\u0168\3\2\2\2")
        buf.write("Q\u016b\3\2\2\2S\u016e\3\2\2\2U\u0170\3\2\2\2W\u0172\3")
        buf.write("\2\2\2Y\u0175\3\2\2\2[\u0178\3\2\2\2]\u017b\3\2\2\2_\u017e")
        buf.write("\3\2\2\2a\u0181\3\2\2\2c\u0183\3\2\2\2e\u0185\3\2\2\2")
        buf.write("g\u0187\3\2\2\2i\u0189\3\2\2\2k\u018b\3\2\2\2m\u018d\3")
        buf.write("\2\2\2o\u018f\3\2\2\2q\u0191\3\2\2\2s\u0193\3\2\2\2u\u0196")
        buf.write("\3\2\2\2w\u0198\3\2\2\2y\u019f\3\2\2\2{\u01a2\3\2\2\2")
        buf.write("}\u01a6\3\2\2\2\177\u01ac\3\2\2\2\u0081\u01ae\3\2\2\2")
        buf.write("\u0083\u01b0\3\2\2\2\u0085\u01b5\3\2\2\2\u0087\u01b7\3")
        buf.write("\2\2\2\u0089\u01bd\3\2\2\2\u008b\u01c3\3\2\2\2\u008d\u01c5")
        buf.write("\3\2\2\2\u008f\u01c8\3\2\2\2\u0091\u01ce\3\2\2\2\u0093")
        buf.write("\u01dc\3\2\2\2\u0095\u01e7\3\2\2\2\u0097\u01ea\3\2\2\2")
        buf.write("\u0099\u01f3\3\2\2\2\u009b\u00a4\7\62\2\2\u009c\u00a0")
        buf.write("\t\2\2\2\u009d\u009f\t\3\2\2\u009e\u009d\3\2\2\2\u009f")
        buf.write("\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u009b\3")
        buf.write("\2\2\2\u00a3\u009c\3\2\2\2\u00a4\4\3\2\2\2\u00a5\u00a6")
        buf.write("\7\62\2\2\u00a6\u00a8\t\4\2\2\u00a7\u00a9\5\177@\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\6\3\2\2\2\u00ac\u00ad\7\62")
        buf.write("\2\2\u00ad\u00af\t\5\2\2\u00ae\u00b0\5\u0081A\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\b\3\2\2\2\u00b3\u00b4\7\62")
        buf.write("\2\2\u00b4\u00b6\t\6\2\2\u00b5\u00b7\5\u0083B\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\n\3\2\2\2\u00ba\u00bd\5\65")
        buf.write("\33\2\u00bb\u00bd\5\67\34\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bd\f\3\2\2\2\u00be\u00bf\5\3\2\2\u00bf")
        buf.write("\u00cd\7\60\2\2\u00c0\u00c2\5{>\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c5\5")
        buf.write("}?\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c8")
        buf.write("\3\2\2\2\u00c6\u00c8\5}?\2\u00c7\u00c1\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00ce\3\2\2\2\u00c9\u00cb\5{>\2\u00ca\u00cc")
        buf.write("\5}?\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce")
        buf.write("\3\2\2\2\u00cd\u00c7\3\2\2\2\u00cd\u00c9\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\16\3\2\2\2\u00cf\u00d3\7$\2\2\u00d0")
        buf.write("\u00d2\5\u0085C\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2")
        buf.write("\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\7$\2\2\u00d7")
        buf.write("\u00d8\b\b\2\2\u00d8\20\3\2\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7h\2\2\u00db\22\3\2\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7g\2\2\u00e0")
        buf.write("\24\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3\7q\2\2\u00e3")
        buf.write("\u00e4\7t\2\2\u00e4\26\3\2\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7w\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\u00eb\7p\2\2\u00eb\30\3\2\2\2\u00ec")
        buf.write("\u00ed\7e\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\u00f0\7v\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2")
        buf.write("\u00f3\7w\2\2\u00f3\u00f4\7g\2\2\u00f4\32\3\2\2\2\u00f5")
        buf.write("\u00f6\7d\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7g\2\2\u00f8")
        buf.write("\u00f9\7c\2\2\u00f9\u00fa\7m\2\2\u00fa\34\3\2\2\2\u00fb")
        buf.write("\u00fc\7t\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7p\2\2\u00fe")
        buf.write("\u00ff\7i\2\2\u00ff\u0100\7g\2\2\u0100\36\3\2\2\2\u0101")
        buf.write("\u0102\7h\2\2\u0102\u0103\7w\2\2\u0103\u0104\7p\2\2\u0104")
        buf.write("\u0105\7e\2\2\u0105 \3\2\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("\u0108\7{\2\2\u0108\u0109\7r\2\2\u0109\u010a\7g\2\2\u010a")
        buf.write("\"\3\2\2\2\u010b\u010c\7u\2\2\u010c\u010d\7v\2\2\u010d")
        buf.write("\u010e\7t\2\2\u010e\u010f\7w\2\2\u010f\u0110\7e\2\2\u0110")
        buf.write("\u0111\7v\2\2\u0111$\3\2\2\2\u0112\u0113\7k\2\2\u0113")
        buf.write("\u0114\7p\2\2\u0114\u0115\7v\2\2\u0115\u0116\7g\2\2\u0116")
        buf.write("\u0117\7t\2\2\u0117\u0118\7h\2\2\u0118\u0119\7c\2\2\u0119")
        buf.write("\u011a\7e\2\2\u011a\u011b\7g\2\2\u011b&\3\2\2\2\u011c")
        buf.write("\u011d\7u\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f")
        buf.write("\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7i\2\2\u0122")
        buf.write("(\3\2\2\2\u0123\u0124\7k\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write("\u0126\7v\2\2\u0126*\3\2\2\2\u0127\u0128\7h\2\2\u0128")
        buf.write("\u0129\7n\2\2\u0129\u012a\7q\2\2\u012a\u012b\7c\2\2\u012b")
        buf.write("\u012c\7v\2\2\u012c,\3\2\2\2\u012d\u012e\7d\2\2\u012e")
        buf.write("\u012f\7q\2\2\u012f\u0130\7q\2\2\u0130\u0131\7n\2\2\u0131")
        buf.write("\u0132\7g\2\2\u0132\u0133\7c\2\2\u0133\u0134\7p\2\2\u0134")
        buf.write(".\3\2\2\2\u0135\u0136\7e\2\2\u0136\u0137\7q\2\2\u0137")
        buf.write("\u0138\7p\2\2\u0138\u0139\7u\2\2\u0139\u013a\7v\2\2\u013a")
        buf.write("\60\3\2\2\2\u013b\u013c\7x\2\2\u013c\u013d\7c\2\2\u013d")
        buf.write("\u013e\7t\2\2\u013e\62\3\2\2\2\u013f\u0140\7p\2\2\u0140")
        buf.write("\u0141\7k\2\2\u0141\u0142\7n\2\2\u0142\64\3\2\2\2\u0143")
        buf.write("\u0144\7v\2\2\u0144\u0145\7t\2\2\u0145\u0146\7w\2\2\u0146")
        buf.write("\u0147\7g\2\2\u0147\66\3\2\2\2\u0148\u0149\7h\2\2\u0149")
        buf.write("\u014a\7c\2\2\u014a\u014b\7n\2\2\u014b\u014c\7u\2\2\u014c")
        buf.write("\u014d\7g\2\2\u014d8\3\2\2\2\u014e\u014f\7-\2\2\u014f")
        buf.write(":\3\2\2\2\u0150\u0151\7/\2\2\u0151<\3\2\2\2\u0152\u0153")
        buf.write("\7,\2\2\u0153>\3\2\2\2\u0154\u0155\7\61\2\2\u0155@\3\2")
        buf.write("\2\2\u0156\u0157\7\'\2\2\u0157B\3\2\2\2\u0158\u0159\7")
        buf.write("?\2\2\u0159\u015a\7?\2\2\u015aD\3\2\2\2\u015b\u015c\7")
        buf.write("#\2\2\u015c\u015d\7?\2\2\u015dF\3\2\2\2\u015e\u015f\7")
        buf.write(">\2\2\u015fH\3\2\2\2\u0160\u0161\7>\2\2\u0161\u0162\7")
        buf.write("?\2\2\u0162J\3\2\2\2\u0163\u0164\7@\2\2\u0164L\3\2\2\2")
        buf.write("\u0165\u0166\7@\2\2\u0166\u0167\7?\2\2\u0167N\3\2\2\2")
        buf.write("\u0168\u0169\7(\2\2\u0169\u016a\7(\2\2\u016aP\3\2\2\2")
        buf.write("\u016b\u016c\7~\2\2\u016c\u016d\7~\2\2\u016dR\3\2\2\2")
        buf.write("\u016e\u016f\7#\2\2\u016fT\3\2\2\2\u0170\u0171\7?\2\2")
        buf.write("\u0171V\3\2\2\2\u0172\u0173\7-\2\2\u0173\u0174\7?\2\2")
        buf.write("\u0174X\3\2\2\2\u0175\u0176\7/\2\2\u0176\u0177\7?\2\2")
        buf.write("\u0177Z\3\2\2\2\u0178\u0179\7,\2\2\u0179\u017a\7?\2\2")
        buf.write("\u017a\\\3\2\2\2\u017b\u017c\7\61\2\2\u017c\u017d\7?\2")
        buf.write("\2\u017d^\3\2\2\2\u017e\u017f\7\'\2\2\u017f\u0180\7?\2")
        buf.write("\2\u0180`\3\2\2\2\u0181\u0182\7<\2\2\u0182b\3\2\2\2\u0183")
        buf.write("\u0184\7=\2\2\u0184d\3\2\2\2\u0185\u0186\7.\2\2\u0186")
        buf.write("f\3\2\2\2\u0187\u0188\7*\2\2\u0188h\3\2\2\2\u0189\u018a")
        buf.write("\7+\2\2\u018aj\3\2\2\2\u018b\u018c\7}\2\2\u018cl\3\2\2")
        buf.write("\2\u018d\u018e\7\177\2\2\u018en\3\2\2\2\u018f\u0190\7")
        buf.write("]\2\2\u0190p\3\2\2\2\u0191\u0192\7_\2\2\u0192r\3\2\2\2")
        buf.write("\u0193\u0194\7<\2\2\u0194\u0195\7?\2\2\u0195t\3\2\2\2")
        buf.write("\u0196\u0197\7\60\2\2\u0197v\3\2\2\2\u0198\u019c\t\7\2")
        buf.write("\2\u0199\u019b\5y=\2\u019a\u0199\3\2\2\2\u019b\u019e\3")
        buf.write("\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019dx")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\t\b\2\2\u01a0")
        buf.write("z\3\2\2\2\u01a1\u01a3\t\3\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5|\3\2\2\2\u01a6\u01a8\t\t\2\2\u01a7\u01a9\t\n\2")
        buf.write("\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ab\5\3\2\2\u01ab~\3\2\2\2\u01ac\u01ad")
        buf.write("\t\13\2\2\u01ad\u0080\3\2\2\2\u01ae\u01af\t\f\2\2\u01af")
        buf.write("\u0082\3\2\2\2\u01b0\u01b1\t\r\2\2\u01b1\u0084\3\2\2\2")
        buf.write("\u01b2\u01b6\5\u0087D\2\u01b3\u01b6\n\16\2\2\u01b4\u01b6")
        buf.write("\7\61\2\2\u01b5\u01b2\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u0086\3\2\2\2\u01b7\u01b8\7^\2\2")
        buf.write("\u01b8\u01b9\t\17\2\2\u01b9\u0088\3\2\2\2\u01ba\u01bb")
        buf.write("\7^\2\2\u01bb\u01be\n\17\2\2\u01bc\u01be\7^\2\2\u01bd")
        buf.write("\u01ba\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u008a\3\2\2\2")
        buf.write("\u01bf\u01c4\n\20\2\2\u01c0\u01c1\7,\2\2\u01c1\u01c4\n")
        buf.write("\21\2\2\u01c2\u01c4\5\u0091I\2\u01c3\u01bf\3\2\2\2\u01c3")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4\u008c\3\2\2\2")
        buf.write("\u01c5\u01c6\7\f\2\2\u01c6\u008e\3\2\2\2\u01c7\u01c9\t")
        buf.write("\22\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01cd\bH\3\2\u01cd\u0090\3\2\2\2\u01ce\u01cf\7")
        buf.write("\61\2\2\u01cf\u01d0\7,\2\2\u01d0\u01d4\3\2\2\2\u01d1\u01d3")
        buf.write("\5\u008bF\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d7\u01d8\7,\2\2\u01d8\u01d9\7")
        buf.write("\61\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\bI\3\2\u01db\u0092")
        buf.write("\3\2\2\2\u01dc\u01dd\7\61\2\2\u01dd\u01de\7\61\2\2\u01de")
        buf.write("\u01e2\3\2\2\2\u01df\u01e1\n\23\2\2\u01e0\u01df\3\2\2")
        buf.write("\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5")
        buf.write("\u01e6\bJ\3\2\u01e6\u0094\3\2\2\2\u01e7\u01e8\13\2\2\2")
        buf.write("\u01e8\u01e9\bK\4\2\u01e9\u0096\3\2\2\2\u01ea\u01ee\7")
        buf.write("$\2\2\u01eb\u01ed\5\u0085C\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2")
        buf.write("\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\b")
        buf.write("L\5\2\u01f2\u0098\3\2\2\2\u01f3\u01f7\7$\2\2\u01f4\u01f6")
        buf.write("\5\u0085C\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2")
        buf.write("\u01f9\u01f7\3\2\2\2\u01fa\u01fb\5\u0089E\2\u01fb\u01fc")
        buf.write("\bM\6\2\u01fc\u009a\3\2\2\2\32\2\u00a0\u00a3\u00aa\u00b1")
        buf.write("\u00b8\u00bc\u00c1\u00c4\u00c7\u00cb\u00cd\u00d3\u019c")
        buf.write("\u01a4\u01a8\u01b5\u01bd\u01c3\u01ca\u01d4\u01e2\u01ee")
        buf.write("\u01f7\7\3\b\2\b\2\2\3K\3\3L\4\3M\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DECIMAL_LIT = 1
    BINARY_LIT = 2
    OCTAL_LIT = 3
    HEX_LIT = 4
    BOOLEAN_LIT = 5
    FLOAT_LIT = 6
    STRING_LIT = 7
    IF = 8
    ELSE = 9
    FOR = 10
    RETURN = 11
    CONTINUE = 12
    BREAK = 13
    RANGE = 14
    FUNC = 15
    TYPE = 16
    STRUCT = 17
    INTERFACE = 18
    STRING = 19
    INT = 20
    FLOAT = 21
    BOOLEAN = 22
    CONST = 23
    VAR = 24
    NIL = 25
    TRUE = 26
    FALSE = 27
    PLUS = 28
    MINUS = 29
    MULTIPLY = 30
    DIVIDE = 31
    MODULO = 32
    EQUAL = 33
    NOT_EQUAL = 34
    LESS_THAN = 35
    LESS_THAN_OR_EQUAL = 36
    GREATER_THAN = 37
    GREATER_THAN_OR_EQUAL = 38
    LOGICAL_AND = 39
    LOGICAL_OR = 40
    NOT = 41
    ASSIGN = 42
    PLUS_ASSIGN = 43
    MINUS_ASSIGN = 44
    MULTIPLY_ASSIGN = 45
    DIVIDE_ASSIGN = 46
    MODULO_ASSIGN = 47
    COLON = 48
    SEMI_COLON = 49
    COMMA = 50
    L_PARENT = 51
    R_PARENT = 52
    L_CURLY = 53
    R_CURLY = 54
    L_BRACKET = 55
    R_BRACKET = 56
    DECLARE_ASSIGN = 57
    DOT = 58
    ID = 59
    NEWLINE = 60
    WHITESPACE = 61
    COMMENT_MULTI = 62
    LINE_COMMENT = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'continue'", "'break'", 
            "'range'", "'func'", "'type'", "'struct'", "'interface'", "'string'", 
            "'int'", "'float'", "'boolean'", "'const'", "'var'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "':'", "';'", 
            "','", "'('", "')'", "'{'", "'}'", "'['", "']'", "':='", "'.'", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", "HEX_LIT", "BOOLEAN_LIT", 
            "FLOAT_LIT", "STRING_LIT", "IF", "ELSE", "FOR", "RETURN", "CONTINUE", 
            "BREAK", "RANGE", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
            "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "NIL", "TRUE", "FALSE", 
            "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", 
            "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
            "LOGICAL_AND", "LOGICAL_OR", "NOT", "ASSIGN", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MULTIPLY_ASSIGN", "DIVIDE_ASSIGN", "MODULO_ASSIGN", 
            "COLON", "SEMI_COLON", "COMMA", "L_PARENT", "R_PARENT", "L_CURLY", 
            "R_CURLY", "L_BRACKET", "R_BRACKET", "DECLARE_ASSIGN", "DOT", 
            "ID", "NEWLINE", "WHITESPACE", "COMMENT_MULTI", "LINE_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", "HEX_LIT", "BOOLEAN_LIT", 
                  "FLOAT_LIT", "STRING_LIT", "IF", "ELSE", "FOR", "RETURN", 
                  "CONTINUE", "BREAK", "RANGE", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MULTIPLY", 
                  "DIVIDE", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                  "LOGICAL_AND", "LOGICAL_OR", "NOT", "ASSIGN", "PLUS_ASSIGN", 
                  "MINUS_ASSIGN", "MULTIPLY_ASSIGN", "DIVIDE_ASSIGN", "MODULO_ASSIGN", 
                  "COLON", "SEMI_COLON", "COMMA", "L_PARENT", "R_PARENT", 
                  "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "DECLARE_ASSIGN", 
                  "DOT", "ID", "ASCII_CHAR", "DEC_DIGIT", "EXPONENT", "BIN_DIGIT", 
                  "OCTAL_DIGIT", "HEX_DIGIT", "CHARACTER", "ESC", "ESC_ILL", 
                  "COMMENT_CONTENT", "NEWLINE", "WHITESPACE", "COMMENT_MULTI", 
                  "LINE_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.STRING_LIT_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                result = str(self.text)
                # result = result[1:-1]
                self.text = result

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(self.text)  

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:]) 

     


