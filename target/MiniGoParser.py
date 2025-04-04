# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u02a0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a4\n\3\3\4")
        buf.write("\3\4\3\4\3\4\5\4\u00aa\n\4\3\5\3\5\3\5\3\5\3\5\5\5\u00b1")
        buf.write("\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00c7\n\b\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00cd\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00e5\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u00ed\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00f4")
        buf.write("\n\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0101\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u010a\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u011c")
        buf.write("\n\26\3\27\3\27\3\27\5\27\u0121\n\27\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\5\32\u012c\n\32\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0132\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u013c\n\34\f\34\16\34\u013f\13\34\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \5 \u014e\n \3!\3!\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\5#\u015e\n#\3$\3$\3$\3$\3$\3$\5$\u0166\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\5%\u016e\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u017f\n&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\5(\u018c\n(\3)\3)\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\3-\5-\u019d\n-\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01ad\n\60\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u01b3\n\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u01bd\n\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\5\63\u01c6\n\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01d0\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u01d9\n\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\5\66\u01e1\n\66\3\67\3\67\3\67\38\38\38\38")
        buf.write("\58\u01ea\n8\39\39\59\u01ee\n9\3:\3:\3:\3:\3:\5:\u01f5")
        buf.write("\n:\3;\3;\3<\3<\5<\u01fb\n<\3<\3<\3=\3=\3=\3=\3=\3=\5")
        buf.write("=\u0205\n=\3>\3>\3>\3>\3>\3>\3>\3>\5>\u020f\n>\3?\3?\3")
        buf.write("?\3?\3?\5?\u0216\n?\3@\3@\3A\3A\5A\u021c\nA\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3C\7C\u0226\nC\fC\16C\u0229\13C\3D\3D\3D\3")
        buf.write("D\3D\3D\7D\u0231\nD\fD\16D\u0234\13D\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\7E\u024b")
        buf.write("\nE\fE\16E\u024e\13E\3F\3F\3F\3F\3F\3F\3F\3F\3F\7F\u0259")
        buf.write("\nF\fF\16F\u025c\13F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G")
        buf.write("\3G\7G\u026a\nG\fG\16G\u026d\13G\3H\3H\3H\3H\3H\5H\u0274")
        buf.write("\nH\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\7I\u0280\nI\fI\16I\u0283")
        buf.write("\13I\3J\3J\3K\3K\3K\3K\3K\3K\5K\u028d\nK\3L\3L\3L\3L\3")
        buf.write("L\3L\5L\u0295\nL\3M\3M\3M\3M\3M\5M\u029c\nM\3N\3N\3N\2")
        buf.write("\t\66\u0084\u0086\u0088\u008a\u008c\u0090O\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\2\6\3\2,\61\4\2\25\30==\3\2\3\6\3\3\63\63\2\u02a6")
        buf.write("\2\u009c\3\2\2\2\4\u00a3\3\2\2\2\6\u00a9\3\2\2\2\b\u00b0")
        buf.write("\3\2\2\2\n\u00b4\3\2\2\2\f\u00b9\3\2\2\2\16\u00c6\3\2")
        buf.write("\2\2\20\u00c8\3\2\2\2\22\u00ce\3\2\2\2\24\u00d3\3\2\2")
        buf.write("\2\26\u00d9\3\2\2\2\30\u00dd\3\2\2\2\32\u00e4\3\2\2\2")
        buf.write("\34\u00ec\3\2\2\2\36\u00f3\3\2\2\2 \u00f5\3\2\2\2\"\u00f8")
        buf.write("\3\2\2\2$\u0100\3\2\2\2&\u0102\3\2\2\2(\u0109\3\2\2\2")
        buf.write("*\u011b\3\2\2\2,\u0120\3\2\2\2.\u0122\3\2\2\2\60\u0124")
        buf.write("\3\2\2\2\62\u012b\3\2\2\2\64\u0131\3\2\2\2\66\u0133\3")
        buf.write("\2\2\28\u0140\3\2\2\2:\u0144\3\2\2\2<\u0146\3\2\2\2>\u014d")
        buf.write("\3\2\2\2@\u014f\3\2\2\2B\u0151\3\2\2\2D\u015d\3\2\2\2")
        buf.write("F\u0165\3\2\2\2H\u016d\3\2\2\2J\u017e\3\2\2\2L\u0180\3")
        buf.write("\2\2\2N\u018b\3\2\2\2P\u018d\3\2\2\2R\u0192\3\2\2\2T\u0194")
        buf.write("\3\2\2\2V\u0196\3\2\2\2X\u019c\3\2\2\2Z\u019e\3\2\2\2")
        buf.write("\\\u01a0\3\2\2\2^\u01ac\3\2\2\2`\u01b2\3\2\2\2b\u01bc")
        buf.write("\3\2\2\2d\u01c5\3\2\2\2f\u01cf\3\2\2\2h\u01d8\3\2\2\2")
        buf.write("j\u01e0\3\2\2\2l\u01e2\3\2\2\2n\u01e9\3\2\2\2p\u01ed\3")
        buf.write("\2\2\2r\u01f4\3\2\2\2t\u01f6\3\2\2\2v\u01fa\3\2\2\2x\u0204")
        buf.write("\3\2\2\2z\u020e\3\2\2\2|\u0215\3\2\2\2~\u0217\3\2\2\2")
        buf.write("\u0080\u021b\3\2\2\2\u0082\u021d\3\2\2\2\u0084\u021f\3")
        buf.write("\2\2\2\u0086\u022a\3\2\2\2\u0088\u0235\3\2\2\2\u008a\u024f")
        buf.write("\3\2\2\2\u008c\u025d\3\2\2\2\u008e\u0273\3\2\2\2\u0090")
        buf.write("\u0275\3\2\2\2\u0092\u0284\3\2\2\2\u0094\u028c\3\2\2\2")
        buf.write("\u0096\u0294\3\2\2\2\u0098\u029b\3\2\2\2\u009a\u029d\3")
        buf.write("\2\2\2\u009c\u009d\5\4\3\2\u009d\u009e\7\2\2\3\u009e\3")
        buf.write("\3\2\2\2\u009f\u00a4\3\2\2\2\u00a0\u00a1\5\b\5\2\u00a1")
        buf.write("\u00a2\5\6\4\2\u00a2\u00a4\3\2\2\2\u00a3\u009f\3\2\2\2")
        buf.write("\u00a3\u00a0\3\2\2\2\u00a4\5\3\2\2\2\u00a5\u00aa\3\2\2")
        buf.write("\2\u00a6\u00a7\5\b\5\2\u00a7\u00a8\5\6\4\2\u00a8\u00aa")
        buf.write("\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00aa")
        buf.write("\7\3\2\2\2\u00ab\u00b1\5\n\6\2\u00ac\u00b1\5\f\7\2\u00ad")
        buf.write("\u00b1\5\20\t\2\u00ae\u00b1\5\22\n\2\u00af\u00b1\5\24")
        buf.write("\13\2\u00b0\u00ab\3\2\2\2\u00b0\u00ac\3\2\2\2\u00b0\u00ad")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b3\5\u009aN\2\u00b3\t\3\2\2\2")
        buf.write("\u00b4\u00b5\7\31\2\2\u00b5\u00b6\7=\2\2\u00b6\u00b7\7")
        buf.write(",\2\2\u00b7\u00b8\5\u0082B\2\u00b8\13\3\2\2\2\u00b9\u00ba")
        buf.write("\7\32\2\2\u00ba\u00bb\5\16\b\2\u00bb\r\3\2\2\2\u00bc\u00bd")
        buf.write("\7=\2\2\u00bd\u00be\5X-\2\u00be\u00bf\7,\2\2\u00bf\u00c0")
        buf.write("\5\u0082B\2\u00c0\u00c7\3\2\2\2\u00c1\u00c2\7=\2\2\u00c2")
        buf.write("\u00c7\5X-\2\u00c3\u00c4\7=\2\2\u00c4\u00c5\7,\2\2\u00c5")
        buf.write("\u00c7\5\u0082B\2\u00c6\u00bc\3\2\2\2\u00c6\u00c1\3\2")
        buf.write("\2\2\u00c6\u00c3\3\2\2\2\u00c7\17\3\2\2\2\u00c8\u00c9")
        buf.write("\7\22\2\2\u00c9\u00cc\7=\2\2\u00ca\u00cd\5b\62\2\u00cb")
        buf.write("\u00cd\5f\64\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2")
        buf.write("\u00cd\21\3\2\2\2\u00ce\u00cf\7\21\2\2\u00cf\u00d0\7=")
        buf.write("\2\2\u00d0\u00d1\5\32\16\2\u00d1\u00d2\5$\23\2\u00d2\23")
        buf.write("\3\2\2\2\u00d3\u00d4\7\21\2\2\u00d4\u00d5\5\26\f\2\u00d5")
        buf.write("\u00d6\7=\2\2\u00d6\u00d7\5\32\16\2\u00d7\u00d8\5$\23")
        buf.write("\2\u00d8\25\3\2\2\2\u00d9\u00da\7\65\2\2\u00da\u00db\5")
        buf.write("\30\r\2\u00db\u00dc\7\66\2\2\u00dc\27\3\2\2\2\u00dd\u00de")
        buf.write("\7=\2\2\u00de\u00df\5X-\2\u00df\31\3\2\2\2\u00e0\u00e5")
        buf.write("\5\34\17\2\u00e1\u00e2\5\34\17\2\u00e2\u00e3\5\"\22\2")
        buf.write("\u00e3\u00e5\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e4\u00e1\3")
        buf.write("\2\2\2\u00e5\33\3\2\2\2\u00e6\u00e7\7\65\2\2\u00e7\u00ed")
        buf.write("\7\66\2\2\u00e8\u00e9\7\65\2\2\u00e9\u00ea\5\36\20\2\u00ea")
        buf.write("\u00eb\7\66\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00e6\3\2\2")
        buf.write("\2\u00ec\u00e8\3\2\2\2\u00ed\35\3\2\2\2\u00ee\u00f4\5")
        buf.write(" \21\2\u00ef\u00f0\5 \21\2\u00f0\u00f1\7\64\2\2\u00f1")
        buf.write("\u00f2\5\36\20\2\u00f2\u00f4\3\2\2\2\u00f3\u00ee\3\2\2")
        buf.write("\2\u00f3\u00ef\3\2\2\2\u00f4\37\3\2\2\2\u00f5\u00f6\5")
        buf.write("n8\2\u00f6\u00f7\5X-\2\u00f7!\3\2\2\2\u00f8\u00f9\5X-")
        buf.write("\2\u00f9#\3\2\2\2\u00fa\u00fb\7\67\2\2\u00fb\u0101\78")
        buf.write("\2\2\u00fc\u00fd\7\67\2\2\u00fd\u00fe\5&\24\2\u00fe\u00ff")
        buf.write("\78\2\2\u00ff\u0101\3\2\2\2\u0100\u00fa\3\2\2\2\u0100")
        buf.write("\u00fc\3\2\2\2\u0101%\3\2\2\2\u0102\u0103\5*\26\2\u0103")
        buf.write("\u0104\5(\25\2\u0104\'\3\2\2\2\u0105\u010a\3\2\2\2\u0106")
        buf.write("\u0107\5*\26\2\u0107\u0108\5(\25\2\u0108\u010a\3\2\2\2")
        buf.write("\u0109\u0105\3\2\2\2\u0109\u0106\3\2\2\2\u010a)\3\2\2")
        buf.write("\2\u010b\u011c\5\b\5\2\u010c\u010d\5,\27\2\u010d\u010e")
        buf.write("\5\u009aN\2\u010e\u011c\3\2\2\2\u010f\u0110\5> \2\u0110")
        buf.write("\u0111\5\u009aN\2\u0111\u011c\3\2\2\2\u0112\u0113\5@!")
        buf.write("\2\u0113\u0114\5\u009aN\2\u0114\u011c\3\2\2\2\u0115\u0116")
        buf.write("\5B\"\2\u0116\u0117\5\u009aN\2\u0117\u011c\3\2\2\2\u0118")
        buf.write("\u011c\5$\23\2\u0119\u011c\5D#\2\u011a\u011c\5J&\2\u011b")
        buf.write("\u010b\3\2\2\2\u011b\u010c\3\2\2\2\u011b\u010f\3\2\2\2")
        buf.write("\u011b\u0112\3\2\2\2\u011b\u0115\3\2\2\2\u011b\u0118\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c+")
        buf.write("\3\2\2\2\u011d\u0121\58\35\2\u011e\u0121\5<\37\2\u011f")
        buf.write("\u0121\5.\30\2\u0120\u011d\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u011f\3\2\2\2\u0121-\3\2\2\2\u0122\u0123\5\60\31")
        buf.write("\2\u0123/\3\2\2\2\u0124\u0125\7=\2\2\u0125\u0126\5\62")
        buf.write("\32\2\u0126\61\3\2\2\2\u0127\u012c\5\64\33\2\u0128\u0129")
        buf.write("\5\64\33\2\u0129\u012a\5\62\32\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u0127\3\2\2\2\u012b\u0128\3\2\2\2\u012c\63\3\2\2\2\u012d")
        buf.write("\u012e\7<\2\2\u012e\u0132\7=\2\2\u012f\u0132\5^\60\2\u0130")
        buf.write("\u0132\5\u0096L\2\u0131\u012d\3\2\2\2\u0131\u012f\3\2")
        buf.write("\2\2\u0131\u0130\3\2\2\2\u0132\65\3\2\2\2\u0133\u0134")
        buf.write("\b\34\1\2\u0134\u0135\7=\2\2\u0135\u013d\3\2\2\2\u0136")
        buf.write("\u0137\f\4\2\2\u0137\u0138\7<\2\2\u0138\u013c\7=\2\2\u0139")
        buf.write("\u013a\f\3\2\2\u013a\u013c\5^\60\2\u013b\u0136\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013d\u013e\3\2\2\2\u013e\67\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0141\5\66\34\2\u0141\u0142\5:\36\2\u0142")
        buf.write("\u0143\5\u0082B\2\u01439\3\2\2\2\u0144\u0145\t\2\2\2\u0145")
        buf.write(";\3\2\2\2\u0146\u0147\5\66\34\2\u0147\u0148\7;\2\2\u0148")
        buf.write("\u0149\5\u0082B\2\u0149=\3\2\2\2\u014a\u014e\7\r\2\2\u014b")
        buf.write("\u014c\7\r\2\2\u014c\u014e\5\u0082B\2\u014d\u014a\3\2")
        buf.write("\2\2\u014d\u014b\3\2\2\2\u014e?\3\2\2\2\u014f\u0150\7")
        buf.write("\17\2\2\u0150A\3\2\2\2\u0151\u0152\7\16\2\2\u0152C\3\2")
        buf.write("\2\2\u0153\u0154\7\n\2\2\u0154\u0155\5H%\2\u0155\u0156")
        buf.write("\5$\23\2\u0156\u0157\5\u009aN\2\u0157\u015e\3\2\2\2\u0158")
        buf.write("\u0159\7\n\2\2\u0159\u015a\5H%\2\u015a\u015b\5$\23\2\u015b")
        buf.write("\u015c\5F$\2\u015c\u015e\3\2\2\2\u015d\u0153\3\2\2\2\u015d")
        buf.write("\u0158\3\2\2\2\u015eE\3\2\2\2\u015f\u0160\7\13\2\2\u0160")
        buf.write("\u0161\5$\23\2\u0161\u0162\5\u009aN\2\u0162\u0166\3\2")
        buf.write("\2\2\u0163\u0164\7\13\2\2\u0164\u0166\5D#\2\u0165\u015f")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0166G\3\2\2\2\u0167\u0168")
        buf.write("\7\65\2\2\u0168\u016e\7\66\2\2\u0169\u016a\7\65\2\2\u016a")
        buf.write("\u016b\5\u0082B\2\u016b\u016c\7\66\2\2\u016c\u016e\3\2")
        buf.write("\2\2\u016d\u0167\3\2\2\2\u016d\u0169\3\2\2\2\u016eI\3")
        buf.write("\2\2\2\u016f\u0170\7\f\2\2\u0170\u0171\5\u0082B\2\u0171")
        buf.write("\u0172\5$\23\2\u0172\u0173\5\u009aN\2\u0173\u017f\3\2")
        buf.write("\2\2\u0174\u0175\7\f\2\2\u0175\u0176\5L\'\2\u0176\u0177")
        buf.write("\5$\23\2\u0177\u0178\5\u009aN\2\u0178\u017f\3\2\2\2\u0179")
        buf.write("\u017a\7\f\2\2\u017a\u017b\5P)\2\u017b\u017c\5$\23\2\u017c")
        buf.write("\u017d\5\u009aN\2\u017d\u017f\3\2\2\2\u017e\u016f\3\2")
        buf.write("\2\2\u017e\u0174\3\2\2\2\u017e\u0179\3\2\2\2\u017fK\3")
        buf.write("\2\2\2\u0180\u0181\5N(\2\u0181\u0182\7\63\2\2\u0182\u0183")
        buf.write("\5\u0082B\2\u0183\u0184\7\63\2\2\u0184\u0185\5N(\2\u0185")
        buf.write("M\3\2\2\2\u0186\u018c\3\2\2\2\u0187\u018c\5R*\2\u0188")
        buf.write("\u018c\5T+\2\u0189\u018c\5V,\2\u018a\u018c\5\f\7\2\u018b")
        buf.write("\u0186\3\2\2\2\u018b\u0187\3\2\2\2\u018b\u0188\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018cO\3\2\2")
        buf.write("\2\u018d\u018e\5n8\2\u018e\u018f\7;\2\2\u018f\u0190\7")
        buf.write("\20\2\2\u0190\u0191\5\u0082B\2\u0191Q\3\2\2\2\u0192\u0193")
        buf.write("\5\u0082B\2\u0193S\3\2\2\2\u0194\u0195\58\35\2\u0195U")
        buf.write("\3\2\2\2\u0196\u0197\5<\37\2\u0197W\3\2\2\2\u0198\u019d")
        buf.write("\5Z.\2\u0199\u019d\5\\/\2\u019a\u019d\5b\62\2\u019b\u019d")
        buf.write("\5f\64\2\u019c\u0198\3\2\2\2\u019c\u0199\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019dY\3\2\2\2\u019e")
        buf.write("\u019f\t\3\2\2\u019f[\3\2\2\2\u01a0\u01a1\5^\60\2\u01a1")
        buf.write("\u01a2\5Z.\2\u01a2]\3\2\2\2\u01a3\u01a4\79\2\2\u01a4\u01a5")
        buf.write("\5`\61\2\u01a5\u01a6\7:\2\2\u01a6\u01ad\3\2\2\2\u01a7")
        buf.write("\u01a8\79\2\2\u01a8\u01a9\5`\61\2\u01a9\u01aa\7:\2\2\u01aa")
        buf.write("\u01ab\5^\60\2\u01ab\u01ad\3\2\2\2\u01ac\u01a3\3\2\2\2")
        buf.write("\u01ac\u01a7\3\2\2\2\u01ad_\3\2\2\2\u01ae\u01b3\7\3\2")
        buf.write("\2\u01af\u01b3\7=\2\2\u01b0\u01b3\5.\30\2\u01b1\u01b3")
        buf.write("\5\u0082B\2\u01b2\u01ae\3\2\2\2\u01b2\u01af\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3a\3\2\2\2\u01b4")
        buf.write("\u01b5\7\23\2\2\u01b5\u01b6\7\67\2\2\u01b6\u01bd\78\2")
        buf.write("\2\u01b7\u01b8\7\23\2\2\u01b8\u01b9\7\67\2\2\u01b9\u01ba")
        buf.write("\5d\63\2\u01ba\u01bb\78\2\2\u01bb\u01bd\3\2\2\2\u01bc")
        buf.write("\u01b4\3\2\2\2\u01bc\u01b7\3\2\2\2\u01bdc\3\2\2\2\u01be")
        buf.write("\u01bf\5l\67\2\u01bf\u01c0\5\u009aN\2\u01c0\u01c6\3\2")
        buf.write("\2\2\u01c1\u01c2\5l\67\2\u01c2\u01c3\5\u009aN\2\u01c3")
        buf.write("\u01c4\5d\63\2\u01c4\u01c6\3\2\2\2\u01c5\u01be\3\2\2\2")
        buf.write("\u01c5\u01c1\3\2\2\2\u01c6e\3\2\2\2\u01c7\u01c8\7\24\2")
        buf.write("\2\u01c8\u01c9\7\67\2\2\u01c9\u01d0\78\2\2\u01ca\u01cb")
        buf.write("\7\24\2\2\u01cb\u01cc\7\67\2\2\u01cc\u01cd\5h\65\2\u01cd")
        buf.write("\u01ce\78\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01c7\3\2\2\2")
        buf.write("\u01cf\u01ca\3\2\2\2\u01d0g\3\2\2\2\u01d1\u01d2\5j\66")
        buf.write("\2\u01d2\u01d3\5\u009aN\2\u01d3\u01d9\3\2\2\2\u01d4\u01d5")
        buf.write("\5j\66\2\u01d5\u01d6\5\u009aN\2\u01d6\u01d7\5h\65\2\u01d7")
        buf.write("\u01d9\3\2\2\2\u01d8\u01d1\3\2\2\2\u01d8\u01d4\3\2\2\2")
        buf.write("\u01d9i\3\2\2\2\u01da\u01db\7=\2\2\u01db\u01e1\5\34\17")
        buf.write("\2\u01dc\u01dd\7=\2\2\u01dd\u01de\5\34\17\2\u01de\u01df")
        buf.write("\5\"\22\2\u01df\u01e1\3\2\2\2\u01e0\u01da\3\2\2\2\u01e0")
        buf.write("\u01dc\3\2\2\2\u01e1k\3\2\2\2\u01e2\u01e3\7=\2\2\u01e3")
        buf.write("\u01e4\5X-\2\u01e4m\3\2\2\2\u01e5\u01ea\7=\2\2\u01e6\u01e7")
        buf.write("\7=\2\2\u01e7\u01e8\7\64\2\2\u01e8\u01ea\5n8\2\u01e9\u01e5")
        buf.write("\3\2\2\2\u01e9\u01e6\3\2\2\2\u01eao\3\2\2\2\u01eb\u01ee")
        buf.write("\5r:\2\u01ec\u01ee\5v<\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec")
        buf.write("\3\2\2\2\u01eeq\3\2\2\2\u01ef\u01f5\7\33\2\2\u01f0\u01f5")
        buf.write("\7\7\2\2\u01f1\u01f5\7\t\2\2\u01f2\u01f5\7\b\2\2\u01f3")
        buf.write("\u01f5\5t;\2\u01f4\u01ef\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4")
        buf.write("\u01f1\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2")
        buf.write("\u01f5s\3\2\2\2\u01f6\u01f7\t\4\2\2\u01f7u\3\2\2\2\u01f8")
        buf.write("\u01fb\7=\2\2\u01f9\u01fb\5\\/\2\u01fa\u01f8\3\2\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\5x=\2\u01fd")
        buf.write("w\3\2\2\2\u01fe\u01ff\7\67\2\2\u01ff\u0205\78\2\2\u0200")
        buf.write("\u0201\7\67\2\2\u0201\u0202\5z>\2\u0202\u0203\78\2\2\u0203")
        buf.write("\u0205\3\2\2\2\u0204\u01fe\3\2\2\2\u0204\u0200\3\2\2\2")
        buf.write("\u0205y\3\2\2\2\u0206\u020f\5|?\2\u0207\u0208\5|?\2\u0208")
        buf.write("\u0209\7\64\2\2\u0209\u020f\3\2\2\2\u020a\u020b\5|?\2")
        buf.write("\u020b\u020c\7\64\2\2\u020c\u020d\5z>\2\u020d\u020f\3")
        buf.write("\2\2\2\u020e\u0206\3\2\2\2\u020e\u0207\3\2\2\2\u020e\u020a")
        buf.write("\3\2\2\2\u020f{\3\2\2\2\u0210\u0216\5\u0080A\2\u0211\u0212")
        buf.write("\5~@\2\u0212\u0213\7\62\2\2\u0213\u0214\5\u0080A\2\u0214")
        buf.write("\u0216\3\2\2\2\u0215\u0210\3\2\2\2\u0215\u0211\3\2\2\2")
        buf.write("\u0216}\3\2\2\2\u0217\u0218\7=\2\2\u0218\177\3\2\2\2\u0219")
        buf.write("\u021c\5x=\2\u021a\u021c\5\u0082B\2\u021b\u0219\3\2\2")
        buf.write("\2\u021b\u021a\3\2\2\2\u021c\u0081\3\2\2\2\u021d\u021e")
        buf.write("\5\u0084C\2\u021e\u0083\3\2\2\2\u021f\u0220\bC\1\2\u0220")
        buf.write("\u0221\5\u0086D\2\u0221\u0227\3\2\2\2\u0222\u0223\f\3")
        buf.write("\2\2\u0223\u0224\7*\2\2\u0224\u0226\5\u0086D\2\u0225\u0222")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u0085\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022b\bD\1\2\u022b\u022c\5\u0088E\2\u022c\u0232")
        buf.write("\3\2\2\2\u022d\u022e\f\3\2\2\u022e\u022f\7)\2\2\u022f")
        buf.write("\u0231\5\u0088E\2\u0230\u022d\3\2\2\2\u0231\u0234\3\2")
        buf.write("\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0087")
        buf.write("\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0236\bE\1\2\u0236")
        buf.write("\u0237\5\u008aF\2\u0237\u024c\3\2\2\2\u0238\u0239\f\b")
        buf.write("\2\2\u0239\u023a\7#\2\2\u023a\u024b\5\u008aF\2\u023b\u023c")
        buf.write("\f\7\2\2\u023c\u023d\7$\2\2\u023d\u024b\5\u008aF\2\u023e")
        buf.write("\u023f\f\6\2\2\u023f\u0240\7%\2\2\u0240\u024b\5\u008a")
        buf.write("F\2\u0241\u0242\f\5\2\2\u0242\u0243\7&\2\2\u0243\u024b")
        buf.write("\5\u008aF\2\u0244\u0245\f\4\2\2\u0245\u0246\7\'\2\2\u0246")
        buf.write("\u024b\5\u008aF\2\u0247\u0248\f\3\2\2\u0248\u0249\7(\2")
        buf.write("\2\u0249\u024b\5\u008aF\2\u024a\u0238\3\2\2\2\u024a\u023b")
        buf.write("\3\2\2\2\u024a\u023e\3\2\2\2\u024a\u0241\3\2\2\2\u024a")
        buf.write("\u0244\3\2\2\2\u024a\u0247\3\2\2\2\u024b\u024e\3\2\2\2")
        buf.write("\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u0089\3")
        buf.write("\2\2\2\u024e\u024c\3\2\2\2\u024f\u0250\bF\1\2\u0250\u0251")
        buf.write("\5\u008cG\2\u0251\u025a\3\2\2\2\u0252\u0253\f\4\2\2\u0253")
        buf.write("\u0254\7\36\2\2\u0254\u0259\5\u008cG\2\u0255\u0256\f\3")
        buf.write("\2\2\u0256\u0257\7\37\2\2\u0257\u0259\5\u008cG\2\u0258")
        buf.write("\u0252\3\2\2\2\u0258\u0255\3\2\2\2\u0259\u025c\3\2\2\2")
        buf.write("\u025a\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u008b\3")
        buf.write("\2\2\2\u025c\u025a\3\2\2\2\u025d\u025e\bG\1\2\u025e\u025f")
        buf.write("\5\u008eH\2\u025f\u026b\3\2\2\2\u0260\u0261\f\5\2\2\u0261")
        buf.write("\u0262\7 \2\2\u0262\u026a\5\u008eH\2\u0263\u0264\f\4\2")
        buf.write("\2\u0264\u0265\7!\2\2\u0265\u026a\5\u008eH\2\u0266\u0267")
        buf.write("\f\3\2\2\u0267\u0268\7\"\2\2\u0268\u026a\5\u008eH\2\u0269")
        buf.write("\u0260\3\2\2\2\u0269\u0263\3\2\2\2\u0269\u0266\3\2\2\2")
        buf.write("\u026a\u026d\3\2\2\2\u026b\u0269\3\2\2\2\u026b\u026c\3")
        buf.write("\2\2\2\u026c\u008d\3\2\2\2\u026d\u026b\3\2\2\2\u026e\u0274")
        buf.write("\5\u0090I\2\u026f\u0270\7+\2\2\u0270\u0274\5\u008eH\2")
        buf.write("\u0271\u0272\7\37\2\2\u0272\u0274\5\u008eH\2\u0273\u026e")
        buf.write("\3\2\2\2\u0273\u026f\3\2\2\2\u0273\u0271\3\2\2\2\u0274")
        buf.write("\u008f\3\2\2\2\u0275\u0276\bI\1\2\u0276\u0277\5\u0092")
        buf.write("J\2\u0277\u0281\3\2\2\2\u0278\u0279\f\5\2\2\u0279\u027a")
        buf.write("\7<\2\2\u027a\u0280\7=\2\2\u027b\u027c\f\4\2\2\u027c\u0280")
        buf.write("\5^\60\2\u027d\u027e\f\3\2\2\u027e\u0280\5\u0096L\2\u027f")
        buf.write("\u0278\3\2\2\2\u027f\u027b\3\2\2\2\u027f\u027d\3\2\2\2")
        buf.write("\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0281\u0282\3")
        buf.write("\2\2\2\u0282\u0091\3\2\2\2\u0283\u0281\3\2\2\2\u0284\u0285")
        buf.write("\5\u0094K\2\u0285\u0093\3\2\2\2\u0286\u028d\5p9\2\u0287")
        buf.write("\u028d\7=\2\2\u0288\u0289\7\65\2\2\u0289\u028a\5\u0082")
        buf.write("B\2\u028a\u028b\7\66\2\2\u028b\u028d\3\2\2\2\u028c\u0286")
        buf.write("\3\2\2\2\u028c\u0287\3\2\2\2\u028c\u0288\3\2\2\2\u028d")
        buf.write("\u0095\3\2\2\2\u028e\u028f\7\65\2\2\u028f\u0295\7\66\2")
        buf.write("\2\u0290\u0291\7\65\2\2\u0291\u0292\5\u0098M\2\u0292\u0293")
        buf.write("\7\66\2\2\u0293\u0295\3\2\2\2\u0294\u028e\3\2\2\2\u0294")
        buf.write("\u0290\3\2\2\2\u0295\u0097\3\2\2\2\u0296\u029c\5\u0082")
        buf.write("B\2\u0297\u0298\5\u0082B\2\u0298\u0299\7\64\2\2\u0299")
        buf.write("\u029a\5\u0098M\2\u029a\u029c\3\2\2\2\u029b\u0296\3\2")
        buf.write("\2\2\u029b\u0297\3\2\2\2\u029c\u0099\3\2\2\2\u029d\u029e")
        buf.write("\t\5\2\2\u029e\u009b\3\2\2\2\66\u00a3\u00a9\u00b0\u00c6")
        buf.write("\u00cc\u00e4\u00ec\u00f3\u0100\u0109\u011b\u0120\u012b")
        buf.write("\u0131\u013b\u013d\u014d\u015d\u0165\u016d\u017e\u018b")
        buf.write("\u019c\u01ac\u01b2\u01bc\u01c5\u01cf\u01d8\u01e0\u01e9")
        buf.write("\u01ed\u01f4\u01fa\u0204\u020e\u0215\u021b\u0227\u0232")
        buf.write("\u024a\u024c\u0258\u025a\u0269\u026b\u0273\u027f\u0281")
        buf.write("\u028c\u0294\u029b")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'if'", "'else'", "'for'", "'return'", "'continue'", 
                     "'break'", "'range'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'nil'", "'true'", "'false'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "':'", "';'", 
                     "','", "'('", "')'", "'{'", "'}'", "'['", "']'", "':='", 
                     "'.'", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", 
                      "HEX_LIT", "BOOLEAN_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "IF", "ELSE", "FOR", "RETURN", "CONTINUE", "BREAK", 
                      "RANGE", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                      "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "NIL", 
                      "TRUE", "FALSE", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LOGICAL_AND", 
                      "LOGICAL_OR", "NOT", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                      "MULTIPLY_ASSIGN", "DIVIDE_ASSIGN", "MODULO_ASSIGN", 
                      "COLON", "SEMI_COLON", "COMMA", "L_PARENT", "R_PARENT", 
                      "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "DECLARE_ASSIGN", 
                      "DOT", "ID", "NEWLINE", "WHITESPACE", "COMMENT_MULTI", 
                      "LINE_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl_list_tail = 2
    RULE_declaration = 3
    RULE_constDecl = 4
    RULE_varDecl = 5
    RULE_varSpec = 6
    RULE_typeDecl = 7
    RULE_funcDecl = 8
    RULE_methodDecl = 9
    RULE_receiver = 10
    RULE_receiverComponent = 11
    RULE_signature = 12
    RULE_parameters = 13
    RULE_parameterList = 14
    RULE_parameterComponent = 15
    RULE_result = 16
    RULE_block = 17
    RULE_statementList = 18
    RULE_statementList_tail = 19
    RULE_statement = 20
    RULE_basicStatement = 21
    RULE_methodOrFunctionCall = 22
    RULE_methodChain = 23
    RULE_chainItems = 24
    RULE_chainItem = 25
    RULE_oneValue = 26
    RULE_assignmentStatement = 27
    RULE_assignOperations = 28
    RULE_shortValDeclaration = 29
    RULE_returnStatement = 30
    RULE_breakStatement = 31
    RULE_continueStatement = 32
    RULE_ifStatement = 33
    RULE_elseClause = 34
    RULE_condition = 35
    RULE_forStatement = 36
    RULE_forClause = 37
    RULE_simpleStmt = 38
    RULE_forRangeArray = 39
    RULE_expressionStmt = 40
    RULE_assignment = 41
    RULE_shortVarDecl = 42
    RULE_type_ = 43
    RULE_typeName = 44
    RULE_arrayType = 45
    RULE_index = 46
    RULE_indexExpr = 47
    RULE_structType = 48
    RULE_fieldDeclList = 49
    RULE_interfaceType = 50
    RULE_methodSpecList = 51
    RULE_methodSpec = 52
    RULE_fieldDecl = 53
    RULE_identifierList = 54
    RULE_literal = 55
    RULE_basicLiteral = 56
    RULE_integerLiteral = 57
    RULE_compositeLiteral = 58
    RULE_compositeLiteralValue = 59
    RULE_elementList = 60
    RULE_element = 61
    RULE_fieldName = 62
    RULE_value = 63
    RULE_expression = 64
    RULE_logicalOr = 65
    RULE_logicalAnd = 66
    RULE_relational = 67
    RULE_additive = 68
    RULE_multiplication_division_modulo = 69
    RULE_unary = 70
    RULE_postfix = 71
    RULE_primaryExpr = 72
    RULE_operand = 73
    RULE_arguments = 74
    RULE_expressionList = 75
    RULE_endOfSentence = 76

    ruleNames =  [ "program", "decl_list", "decl_list_tail", "declaration", 
                   "constDecl", "varDecl", "varSpec", "typeDecl", "funcDecl", 
                   "methodDecl", "receiver", "receiverComponent", "signature", 
                   "parameters", "parameterList", "parameterComponent", 
                   "result", "block", "statementList", "statementList_tail", 
                   "statement", "basicStatement", "methodOrFunctionCall", 
                   "methodChain", "chainItems", "chainItem", "oneValue", 
                   "assignmentStatement", "assignOperations", "shortValDeclaration", 
                   "returnStatement", "breakStatement", "continueStatement", 
                   "ifStatement", "elseClause", "condition", "forStatement", 
                   "forClause", "simpleStmt", "forRangeArray", "expressionStmt", 
                   "assignment", "shortVarDecl", "type_", "typeName", "arrayType", 
                   "index", "indexExpr", "structType", "fieldDeclList", 
                   "interfaceType", "methodSpecList", "methodSpec", "fieldDecl", 
                   "identifierList", "literal", "basicLiteral", "integerLiteral", 
                   "compositeLiteral", "compositeLiteralValue", "elementList", 
                   "element", "fieldName", "value", "expression", "logicalOr", 
                   "logicalAnd", "relational", "additive", "multiplication_division_modulo", 
                   "unary", "postfix", "primaryExpr", "operand", "arguments", 
                   "expressionList", "endOfSentence" ]

    EOF = Token.EOF
    DECIMAL_LIT=1
    BINARY_LIT=2
    OCTAL_LIT=3
    HEX_LIT=4
    BOOLEAN_LIT=5
    FLOAT_LIT=6
    STRING_LIT=7
    IF=8
    ELSE=9
    FOR=10
    RETURN=11
    CONTINUE=12
    BREAK=13
    RANGE=14
    FUNC=15
    TYPE=16
    STRUCT=17
    INTERFACE=18
    STRING=19
    INT=20
    FLOAT=21
    BOOLEAN=22
    CONST=23
    VAR=24
    NIL=25
    TRUE=26
    FALSE=27
    PLUS=28
    MINUS=29
    MULTIPLY=30
    DIVIDE=31
    MODULO=32
    EQUAL=33
    NOT_EQUAL=34
    LESS_THAN=35
    LESS_THAN_OR_EQUAL=36
    GREATER_THAN=37
    GREATER_THAN_OR_EQUAL=38
    LOGICAL_AND=39
    LOGICAL_OR=40
    NOT=41
    ASSIGN=42
    PLUS_ASSIGN=43
    MINUS_ASSIGN=44
    MULTIPLY_ASSIGN=45
    DIVIDE_ASSIGN=46
    MODULO_ASSIGN=47
    COLON=48
    SEMI_COLON=49
    COMMA=50
    L_PARENT=51
    R_PARENT=52
    L_CURLY=53
    R_CURLY=54
    L_BRACKET=55
    R_BRACKET=56
    DECLARE_ASSIGN=57
    DOT=58
    ID=59
    NEWLINE=60
    WHITESPACE=61
    COMMENT_MULTI=62
    LINE_COMMENT=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.decl_list()
            self.state = 155
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def decl_list_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_list_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = MiniGoParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.declaration()
                self.state = 159
                self.decl_list_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def decl_list_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_list_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list_tail" ):
                return visitor.visitDecl_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def decl_list_tail(self):

        localctx = MiniGoParser.Decl_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_list_tail)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.declaration()
                self.state = 165
                self.decl_list_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 169
                self.constDecl()
                pass

            elif la_ == 2:
                self.state = 170
                self.varDecl()
                pass

            elif la_ == 3:
                self.state = 171
                self.typeDecl()
                pass

            elif la_ == 4:
                self.state = 172
                self.funcDecl()
                pass

            elif la_ == 5:
                self.state = 173
                self.methodDecl()
                pass


            self.state = 176
            self.endOfSentence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.CONST)
            self.state = 179
            self.match(MiniGoParser.ID)
            self.state = 180
            self.match(MiniGoParser.ASSIGN)
            self.state = 181
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def varSpec(self):
            return self.getTypedRuleContext(MiniGoParser.VarSpecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.VAR)
            self.state = 184
            self.varSpec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarSpec" ):
                return visitor.visitVarSpec(self)
            else:
                return visitor.visitChildren(self)




    def varSpec(self):

        localctx = MiniGoParser.VarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varSpec)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(MiniGoParser.ID)
                self.state = 187
                self.type_()
                self.state = 188
                self.match(MiniGoParser.ASSIGN)
                self.state = 189
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(MiniGoParser.ID)
                self.state = 192
                self.type_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(MiniGoParser.ID)
                self.state = 194
                self.match(MiniGoParser.ASSIGN)
                self.state = 195
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MiniGoParser.TYPE)
            self.state = 199
            self.match(MiniGoParser.ID)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 200
                self.structType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 201
                self.interfaceType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.FUNC)
            self.state = 205
            self.match(MiniGoParser.ID)
            self.state = 206
            self.signature()
            self.state = 207
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def signature(self):
            return self.getTypedRuleContext(MiniGoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.FUNC)
            self.state = 210
            self.receiver()
            self.state = 211
            self.match(MiniGoParser.ID)
            self.state = 212
            self.signature()
            self.state = 213
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PARENT(self):
            return self.getToken(MiniGoParser.L_PARENT, 0)

        def receiverComponent(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverComponentContext,0)


        def R_PARENT(self):
            return self.getToken(MiniGoParser.R_PARENT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.L_PARENT)
            self.state = 216
            self.receiverComponent()
            self.state = 217
            self.match(MiniGoParser.R_PARENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_receiverComponent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiverComponent" ):
                return visitor.visitReceiverComponent(self)
            else:
                return visitor.visitChildren(self)




    def receiverComponent(self):

        localctx = MiniGoParser.ReceiverComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_receiverComponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MiniGoParser.ID)
            self.state = 220
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(MiniGoParser.ResultContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignature" ):
                return visitor.visitSignature(self)
            else:
                return visitor.visitChildren(self)




    def signature(self):

        localctx = MiniGoParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_signature)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.parameters()
                self.state = 224
                self.result()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PARENT(self):
            return self.getToken(MiniGoParser.L_PARENT, 0)

        def R_PARENT(self):
            return self.getToken(MiniGoParser.R_PARENT, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MiniGoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameters)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(MiniGoParser.L_PARENT)
                self.state = 229
                self.match(MiniGoParser.R_PARENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(MiniGoParser.L_PARENT)
                self.state = 231
                self.parameterList()
                self.state = 232
                self.match(MiniGoParser.R_PARENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterComponent(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterComponentContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = MiniGoParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameterList)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.parameterComponent()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.parameterComponent()
                self.state = 238
                self.match(MiniGoParser.COMMA)
                self.state = 239
                self.parameterList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameterComponent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterComponent" ):
                return visitor.visitParameterComponent(self)
            else:
                return visitor.visitChildren(self)




    def parameterComponent(self):

        localctx = MiniGoParser.ParameterComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameterComponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.identifierList()
            self.state = 244
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_result

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult" ):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = MiniGoParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(MiniGoParser.L_CURLY)
                self.state = 249
                self.match(MiniGoParser.R_CURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MiniGoParser.L_CURLY)
                self.state = 251
                self.statementList()
                self.state = 252
                self.match(MiniGoParser.R_CURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementList_tail(self):
            return self.getTypedRuleContext(MiniGoParser.StatementList_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.statement()
            self.state = 257
            self.statementList_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementList_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementList_tail(self):
            return self.getTypedRuleContext(MiniGoParser.StatementList_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList_tail" ):
                return visitor.visitStatementList_tail(self)
            else:
                return visitor.visitChildren(self)




    def statementList_tail(self):

        localctx = MiniGoParser.StatementList_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statementList_tail)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.R_CURLY]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.L_CURLY, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.statement()
                self.state = 261
                self.statementList_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def basicStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BasicStatementContext,0)


        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.declaration()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.basicStatement()
                self.state = 267
                self.endOfSentence()
                pass
            elif token in [MiniGoParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.returnStatement()
                self.state = 270
                self.endOfSentence()
                pass
            elif token in [MiniGoParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.breakStatement()
                self.state = 273
                self.endOfSentence()
                pass
            elif token in [MiniGoParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.continueStatement()
                self.state = 276
                self.endOfSentence()
                pass
            elif token in [MiniGoParser.L_CURLY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 278
                self.block()
                pass
            elif token in [MiniGoParser.IF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 279
                self.ifStatement()
                pass
            elif token in [MiniGoParser.FOR]:
                self.enterOuterAlt(localctx, 8)
                self.state = 280
                self.forStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentStatementContext,0)


        def shortValDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.ShortValDeclarationContext,0)


        def methodOrFunctionCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodOrFunctionCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basicStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicStatement" ):
                return visitor.visitBasicStatement(self)
            else:
                return visitor.visitChildren(self)




    def basicStatement(self):

        localctx = MiniGoParser.BasicStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_basicStatement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.shortValDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.methodOrFunctionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodOrFunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodChain(self):
            return self.getTypedRuleContext(MiniGoParser.MethodChainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodOrFunctionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodOrFunctionCall" ):
                return visitor.visitMethodOrFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def methodOrFunctionCall(self):

        localctx = MiniGoParser.MethodOrFunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_methodOrFunctionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.methodChain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodChainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def chainItems(self):
            return self.getTypedRuleContext(MiniGoParser.ChainItemsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodChain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodChain" ):
                return visitor.visitMethodChain(self)
            else:
                return visitor.visitChildren(self)




    def methodChain(self):

        localctx = MiniGoParser.MethodChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_methodChain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.ID)
            self.state = 291
            self.chainItems()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChainItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chainItem(self):
            return self.getTypedRuleContext(MiniGoParser.ChainItemContext,0)


        def chainItems(self):
            return self.getTypedRuleContext(MiniGoParser.ChainItemsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_chainItems

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChainItems" ):
                return visitor.visitChainItems(self)
            else:
                return visitor.visitChildren(self)




    def chainItems(self):

        localctx = MiniGoParser.ChainItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_chainItems)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.chainItem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.chainItem()
                self.state = 295
                self.chainItems()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChainItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_chainItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChainItem" ):
                return visitor.visitChainItem(self)
            else:
                return visitor.visitChildren(self)




    def chainItem(self):

        localctx = MiniGoParser.ChainItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_chainItem)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(MiniGoParser.DOT)
                self.state = 300
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.index()
                pass
            elif token in [MiniGoParser.L_PARENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.arguments()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OneValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def oneValue(self):
            return self.getTypedRuleContext(MiniGoParser.OneValueContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_oneValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneValue" ):
                return visitor.visitOneValue(self)
            else:
                return visitor.visitChildren(self)



    def oneValue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.OneValueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_oneValue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 313
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.OneValueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oneValue)
                        self.state = 308
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 309
                        self.match(MiniGoParser.DOT)
                        self.state = 310
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.OneValueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oneValue)
                        self.state = 311
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 312
                        self.index()
                        pass

             
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oneValue(self):
            return self.getTypedRuleContext(MiniGoParser.OneValueContext,0)


        def assignOperations(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOperationsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MiniGoParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.oneValue(0)
            self.state = 319
            self.assignOperations()
            self.state = 320
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOperationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MULTIPLY_ASSIGN(self):
            return self.getToken(MiniGoParser.MULTIPLY_ASSIGN, 0)

        def DIVIDE_ASSIGN(self):
            return self.getToken(MiniGoParser.DIVIDE_ASSIGN, 0)

        def MODULO_ASSIGN(self):
            return self.getToken(MiniGoParser.MODULO_ASSIGN, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignOperations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOperations" ):
                return visitor.visitAssignOperations(self)
            else:
                return visitor.visitChildren(self)




    def assignOperations(self):

        localctx = MiniGoParser.AssignOperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignOperations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULTIPLY_ASSIGN) | (1 << MiniGoParser.DIVIDE_ASSIGN) | (1 << MiniGoParser.MODULO_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortValDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oneValue(self):
            return self.getTypedRuleContext(MiniGoParser.OneValueContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_shortValDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortValDeclaration" ):
                return visitor.visitShortValDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def shortValDeclaration(self):

        localctx = MiniGoParser.ShortValDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_shortValDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.oneValue(0)
            self.state = 325
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 326
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnStatement)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(MiniGoParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.match(MiniGoParser.RETURN)
                self.state = 330
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def elseClause(self):
            return self.getTypedRuleContext(MiniGoParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifStatement)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(MiniGoParser.IF)
                self.state = 338
                self.condition()
                self.state = 339
                self.block()
                self.state = 340
                self.endOfSentence()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(MiniGoParser.IF)
                self.state = 343
                self.condition()
                self.state = 344
                self.block()
                self.state = 345
                self.elseClause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = MiniGoParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseClause)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(MiniGoParser.ELSE)
                self.state = 350
                self.block()
                self.state = 351
                self.endOfSentence()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(MiniGoParser.ELSE)
                self.state = 354
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PARENT(self):
            return self.getToken(MiniGoParser.L_PARENT, 0)

        def R_PARENT(self):
            return self.getToken(MiniGoParser.R_PARENT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_condition)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(MiniGoParser.L_PARENT)
                self.state = 358
                self.match(MiniGoParser.R_PARENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(MiniGoParser.L_PARENT)
                self.state = 360
                self.expression()
                self.state = 361
                self.match(MiniGoParser.R_PARENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def forClause(self):
            return self.getTypedRuleContext(MiniGoParser.ForClauseContext,0)


        def forRangeArray(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeArrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forStatement)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(MiniGoParser.FOR)
                self.state = 366
                self.expression()
                self.state = 367
                self.block()
                self.state = 368
                self.endOfSentence()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(MiniGoParser.FOR)
                self.state = 371
                self.forClause()
                self.state = 372
                self.block()
                self.state = 373
                self.endOfSentence()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.match(MiniGoParser.FOR)
                self.state = 376
                self.forRangeArray()
                self.state = 377
                self.block()
                self.state = 378
                self.endOfSentence()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SimpleStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SimpleStmtContext,i)


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI_COLON)
            else:
                return self.getToken(MiniGoParser.SEMI_COLON, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForClause" ):
                return visitor.visitForClause(self)
            else:
                return visitor.visitChildren(self)




    def forClause(self):

        localctx = MiniGoParser.ForClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_forClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.simpleStmt()
            self.state = 383
            self.match(MiniGoParser.SEMI_COLON)
            self.state = 384
            self.expression()
            self.state = 385
            self.match(MiniGoParser.SEMI_COLON)
            self.state = 386
            self.simpleStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def shortVarDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ShortVarDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_simpleStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStmt" ):
                return visitor.visitSimpleStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleStmt(self):

        localctx = MiniGoParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_simpleStmt)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.expressionStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
                self.shortVarDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 392
                self.varDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forRangeArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRangeArray" ):
                return visitor.visitForRangeArray(self)
            else:
                return visitor.visitChildren(self)




    def forRangeArray(self):

        localctx = MiniGoParser.ForRangeArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_forRangeArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.identifierList()
            self.state = 396
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 397
            self.match(MiniGoParser.RANGE)
            self.state = 398
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStmt" ):
                return visitor.visitExpressionStmt(self)
            else:
                return visitor.visitChildren(self)




    def expressionStmt(self):

        localctx = MiniGoParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.assignmentStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shortValDeclaration(self):
            return self.getTypedRuleContext(MiniGoParser.ShortValDeclarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_shortVarDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortVarDecl" ):
                return visitor.visitShortVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def shortVarDecl(self):

        localctx = MiniGoParser.ShortVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_shortVarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.shortValDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(MiniGoParser.TypeNameContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_type_)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.typeName()
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.arrayType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.structType()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
                self.interfaceType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typeName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = MiniGoParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def typeName(self):
            return self.getTypedRuleContext(MiniGoParser.TypeNameContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.index()
            self.state = 415
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def indexExpr(self):
            return self.getTypedRuleContext(MiniGoParser.IndexExprContext,0)


        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(MiniGoParser.L_BRACKET)
                self.state = 418
                self.indexExpr()
                self.state = 419
                self.match(MiniGoParser.R_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(MiniGoParser.L_BRACKET)
                self.state = 422
                self.indexExpr()
                self.state = 423
                self.match(MiniGoParser.R_BRACKET)
                self.state = 424
                self.index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def methodOrFunctionCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodOrFunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_indexExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)




    def indexExpr(self):

        localctx = MiniGoParser.IndexExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_indexExpr)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(MiniGoParser.DECIMAL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
                self.methodOrFunctionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 431
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_structType)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(MiniGoParser.STRUCT)
                self.state = 435
                self.match(MiniGoParser.L_CURLY)
                self.state = 436
                self.match(MiniGoParser.R_CURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(MiniGoParser.STRUCT)
                self.state = 438
                self.match(MiniGoParser.L_CURLY)
                self.state = 439
                self.fieldDeclList()
                self.state = 440
                self.match(MiniGoParser.R_CURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclContext,0)


        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def fieldDeclList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldDeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclList" ):
                return visitor.visitFieldDeclList(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclList(self):

        localctx = MiniGoParser.FieldDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_fieldDeclList)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.fieldDecl()
                self.state = 445
                self.endOfSentence()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.fieldDecl()
                self.state = 448
                self.endOfSentence()
                self.state = 449
                self.fieldDeclList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def methodSpecList(self):
            return self.getTypedRuleContext(MiniGoParser.MethodSpecListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_interfaceType)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(MiniGoParser.INTERFACE)
                self.state = 454
                self.match(MiniGoParser.L_CURLY)
                self.state = 455
                self.match(MiniGoParser.R_CURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(MiniGoParser.INTERFACE)
                self.state = 457
                self.match(MiniGoParser.L_CURLY)
                self.state = 458
                self.methodSpecList()
                self.state = 459
                self.match(MiniGoParser.R_CURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSpecListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodSpec(self):
            return self.getTypedRuleContext(MiniGoParser.MethodSpecContext,0)


        def endOfSentence(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfSentenceContext,0)


        def methodSpecList(self):
            return self.getTypedRuleContext(MiniGoParser.MethodSpecListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodSpecList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSpecList" ):
                return visitor.visitMethodSpecList(self)
            else:
                return visitor.visitChildren(self)




    def methodSpecList(self):

        localctx = MiniGoParser.MethodSpecListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_methodSpecList)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.methodSpec()
                self.state = 464
                self.endOfSentence()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.methodSpec()
                self.state = 467
                self.endOfSentence()
                self.state = 468
                self.methodSpecList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def parameters(self):
            return self.getTypedRuleContext(MiniGoParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(MiniGoParser.ResultContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSpec" ):
                return visitor.visitMethodSpec(self)
            else:
                return visitor.visitChildren(self)




    def methodSpec(self):

        localctx = MiniGoParser.MethodSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_methodSpec)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(MiniGoParser.ID)
                self.state = 473
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.match(MiniGoParser.ID)
                self.state = 475
                self.parameters()
                self.state = 476
                self.result()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = MiniGoParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MiniGoParser.ID)
            self.state = 481
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = MiniGoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_identifierList)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.match(MiniGoParser.ID)
                self.state = 485
                self.match(MiniGoParser.COMMA)
                self.state = 486
                self.identifierList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.BasicLiteralContext,0)


        def compositeLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.BOOLEAN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.basicLiteral()
                pass
            elif token in [MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.compositeLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MiniGoParser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def integerLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.IntegerLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basicLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicLiteral" ):
                return visitor.visitBasicLiteral(self)
            else:
                return visitor.visitChildren(self)




    def basicLiteral(self):

        localctx = MiniGoParser.BasicLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_basicLiteral)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.match(MiniGoParser.BOOLEAN_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 495
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 496
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 497
                self.integerLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def BINARY_LIT(self):
            return self.getToken(MiniGoParser.BINARY_LIT, 0)

        def OCTAL_LIT(self):
            return self.getToken(MiniGoParser.OCTAL_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_integerLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLiteral" ):
                return visitor.visitIntegerLiteral(self)
            else:
                return visitor.visitChildren(self)




    def integerLiteral(self):

        localctx = MiniGoParser.IntegerLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_integerLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECIMAL_LIT) | (1 << MiniGoParser.BINARY_LIT) | (1 << MiniGoParser.OCTAL_LIT) | (1 << MiniGoParser.HEX_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compositeLiteralValue(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeLiteralValueContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_compositeLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeLiteral" ):
                return visitor.visitCompositeLiteral(self)
            else:
                return visitor.visitChildren(self)




    def compositeLiteral(self):

        localctx = MiniGoParser.CompositeLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_compositeLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 502
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.L_BRACKET]:
                self.state = 503
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 506
            self.compositeLiteralValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeLiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_compositeLiteralValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeLiteralValue" ):
                return visitor.visitCompositeLiteralValue(self)
            else:
                return visitor.visitChildren(self)




    def compositeLiteralValue(self):

        localctx = MiniGoParser.CompositeLiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_compositeLiteralValue)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(MiniGoParser.L_CURLY)
                self.state = 509
                self.match(MiniGoParser.R_CURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.match(MiniGoParser.L_CURLY)
                self.state = 511
                self.elementList()
                self.state = 512
                self.match(MiniGoParser.R_CURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementList" ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = MiniGoParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_elementList)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.element()
                self.state = 518
                self.match(MiniGoParser.COMMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 520
                self.element()
                self.state = 521
                self.match(MiniGoParser.COMMA)
                self.state = 522
                self.elementList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def fieldName(self):
            return self.getTypedRuleContext(MiniGoParser.FieldNameContext,0)


        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_element)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.fieldName()
                self.state = 528
                self.match(MiniGoParser.COLON)
                self.state = 529
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldName" ):
                return visitor.visitFieldName(self)
            else:
                return visitor.visitChildren(self)




    def fieldName(self):

        localctx = MiniGoParser.FieldNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_fieldName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compositeLiteralValue(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeLiteralValueContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_value)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.L_CURLY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.compositeLiteralValue()
                pass
            elif token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.BOOLEAN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.L_PARENT, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalOrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.logicalOr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalAndContext,0)


        def logicalOr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalOrContext,0)


        def LOGICAL_OR(self):
            return self.getToken(MiniGoParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicalOr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)



    def logicalOr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicalOrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_logicalOr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.logicalAnd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicalOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOr)
                    self.state = 544
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 545
                    self.match(MiniGoParser.LOGICAL_OR)
                    self.state = 546
                    self.logicalAnd(0) 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalContext,0)


        def logicalAnd(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalAndContext,0)


        def LOGICAL_AND(self):
            return self.getToken(MiniGoParser.LOGICAL_AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicalAnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)



    def logicalAnd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicalAndContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_logicalAnd, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.relational(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicalAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAnd)
                    self.state = 555
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 556
                    self.match(MiniGoParser.LOGICAL_AND)
                    self.state = 557
                    self.relational(0) 
                self.state = 562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveContext,0)


        def relational(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(MiniGoParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(MiniGoParser.GREATER_THAN, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)



    def relational(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.RelationalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_relational, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.additive(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 586
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 584
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 566
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 567
                        self.match(MiniGoParser.EQUAL)
                        self.state = 568
                        self.additive(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 569
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 570
                        self.match(MiniGoParser.NOT_EQUAL)
                        self.state = 571
                        self.additive(0)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 572
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 573
                        self.match(MiniGoParser.LESS_THAN)
                        self.state = 574
                        self.additive(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 575
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 576
                        self.match(MiniGoParser.LESS_THAN_OR_EQUAL)
                        self.state = 577
                        self.additive(0)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 578
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 579
                        self.match(MiniGoParser.GREATER_THAN)
                        self.state = 580
                        self.additive(0)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 581
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 582
                        self.match(MiniGoParser.GREATER_THAN_OR_EQUAL)
                        self.state = 583
                        self.additive(0)
                        pass

             
                self.state = 588
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplication_division_modulo(self):
            return self.getTypedRuleContext(MiniGoParser.Multiplication_division_moduloContext,0)


        def additive(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)



    def additive(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_additive, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.multiplication_division_modulo(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 600
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 598
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.AdditiveContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                        self.state = 592
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 593
                        self.match(MiniGoParser.PLUS)
                        self.state = 594
                        self.multiplication_division_modulo(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.AdditiveContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                        self.state = 595
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 596
                        self.match(MiniGoParser.MINUS)
                        self.state = 597
                        self.multiplication_division_modulo(0)
                        pass

             
                self.state = 602
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplication_division_moduloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryContext,0)


        def multiplication_division_modulo(self):
            return self.getTypedRuleContext(MiniGoParser.Multiplication_division_moduloContext,0)


        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplication_division_modulo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication_division_modulo" ):
                return visitor.visitMultiplication_division_modulo(self)
            else:
                return visitor.visitChildren(self)



    def multiplication_division_modulo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Multiplication_division_moduloContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_multiplication_division_modulo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 617
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 615
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Multiplication_division_moduloContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplication_division_modulo)
                        self.state = 606
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 607
                        self.match(MiniGoParser.MULTIPLY)
                        self.state = 608
                        self.unary()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Multiplication_division_moduloContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplication_division_modulo)
                        self.state = 609
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 610
                        self.match(MiniGoParser.DIVIDE)
                        self.state = 611
                        self.unary()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Multiplication_division_moduloContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplication_division_modulo)
                        self.state = 612
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 613
                        self.match(MiniGoParser.MODULO)
                        self.state = 614
                        self.unary()
                        pass

             
                self.state = 619
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def unary(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryContext,0)


        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MiniGoParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_unary)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT, MiniGoParser.BINARY_LIT, MiniGoParser.OCTAL_LIT, MiniGoParser.HEX_LIT, MiniGoParser.BOOLEAN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.NIL, MiniGoParser.L_PARENT, MiniGoParser.L_BRACKET, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.postfix(0)
                pass
            elif token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self.match(MiniGoParser.NOT)
                self.state = 622
                self.unary()
                pass
            elif token in [MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
                self.match(MiniGoParser.MINUS)
                self.state = 624
                self.unary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def postfix(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postfix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix" ):
                return visitor.visitPostfix(self)
            else:
                return visitor.visitChildren(self)



    def postfix(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PostfixContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_postfix, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.primaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 637
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PostfixContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix)
                        self.state = 630
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 631
                        self.match(MiniGoParser.DOT)
                        self.state = 632
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PostfixContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix)
                        self.state = 633
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 634
                        self.index()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PostfixContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix)
                        self.state = 635
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 636
                        self.arguments()
                        pass

             
                self.state = 641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PARENT(self):
            return self.getToken(MiniGoParser.L_PARENT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def R_PARENT(self):
            return self.getToken(MiniGoParser.R_PARENT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_operand)
        try:
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 646
                self.match(MiniGoParser.L_PARENT)
                self.state = 647
                self.expression()
                self.state = 648
                self.match(MiniGoParser.R_PARENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PARENT(self):
            return self.getToken(MiniGoParser.L_PARENT, 0)

        def R_PARENT(self):
            return self.getToken(MiniGoParser.R_PARENT, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_arguments)
        try:
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.match(MiniGoParser.L_PARENT)
                self.state = 653
                self.match(MiniGoParser.R_PARENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 654
                self.match(MiniGoParser.L_PARENT)
                self.state = 655
                self.expressionList()
                self.state = 656
                self.match(MiniGoParser.R_PARENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = MiniGoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_expressionList)
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
                self.expression()
                self.state = 662
                self.match(MiniGoParser.COMMA)
                self.state = 663
                self.expressionList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndOfSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endOfSentence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndOfSentence" ):
                return visitor.visitEndOfSentence(self)
            else:
                return visitor.visitChildren(self)




    def endOfSentence(self):

        localctx = MiniGoParser.EndOfSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_endOfSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.EOF or _la==MiniGoParser.SEMI_COLON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.oneValue_sempred
        self._predicates[65] = self.logicalOr_sempred
        self._predicates[66] = self.logicalAnd_sempred
        self._predicates[67] = self.relational_sempred
        self._predicates[68] = self.additive_sempred
        self._predicates[69] = self.multiplication_division_modulo_sempred
        self._predicates[71] = self.postfix_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def oneValue_sempred(self, localctx:OneValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def logicalOr_sempred(self, localctx:LogicalOrContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def logicalAnd_sempred(self, localctx:LogicalAndContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def relational_sempred(self, localctx:RelationalContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def additive_sempred(self, localctx:AdditiveContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def multiplication_division_modulo_sempred(self, localctx:Multiplication_division_moduloContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def postfix_sempred(self, localctx:PostfixContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         




