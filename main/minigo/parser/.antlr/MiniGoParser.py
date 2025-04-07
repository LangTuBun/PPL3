# Generated from c:/Users/RAZER/OneDrive/Documents/HCMUTSUB/PPL/assignment3/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,66,670,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,3,1,162,8,1,1,2,1,2,1,2,1,2,3,2,168,8,2,1,3,1,3,1,3,1,3,
        1,3,3,3,175,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,197,8,6,1,7,1,7,1,7,1,7,3,7,
        203,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,227,8,12,1,13,1,
        13,1,13,1,13,1,13,1,13,3,13,235,8,13,1,14,1,14,1,14,1,14,1,14,3,
        14,242,8,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,
        17,3,17,255,8,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,264,8,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,3,20,282,8,20,1,21,1,21,1,21,3,21,287,8,21,1,22,1,
        22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,298,8,24,1,25,1,25,1,
        25,1,25,3,25,304,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,5,
        26,314,8,26,10,26,12,26,317,9,26,1,27,1,27,1,27,1,27,1,28,1,28,1,
        29,1,29,1,29,1,29,1,30,1,30,1,30,3,30,332,8,30,1,31,1,31,1,32,1,
        32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,348,8,
        33,1,34,1,34,1,34,1,34,1,34,1,34,3,34,356,8,34,1,35,1,35,1,35,1,
        35,1,35,1,35,3,35,364,8,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,381,8,36,1,37,1,37,1,
        37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,3,38,394,8,38,1,39,1,
        39,1,39,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,43,1,
        43,3,43,411,8,43,1,44,1,44,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,
        46,1,46,1,46,1,46,1,46,3,46,427,8,46,1,47,1,47,1,47,1,47,3,47,433,
        8,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,3,48,443,8,48,1,49,
        1,49,1,49,1,49,1,49,1,49,1,49,3,49,452,8,49,1,50,1,50,1,50,1,50,
        1,50,1,50,1,50,1,50,3,50,462,8,50,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,3,51,471,8,51,1,52,1,52,1,52,1,52,1,52,1,52,3,52,479,8,52,1,
        53,1,53,1,53,1,54,1,54,1,54,1,54,3,54,488,8,54,1,55,1,55,3,55,492,
        8,55,1,56,1,56,1,56,1,56,1,56,3,56,499,8,56,1,57,1,57,1,58,1,58,
        3,58,505,8,58,1,58,1,58,1,59,1,59,1,59,1,59,1,59,1,59,3,59,515,8,
        59,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,3,60,525,8,60,1,61,1,
        61,1,61,1,61,1,61,3,61,532,8,61,1,62,1,62,1,63,1,63,3,63,538,8,63,
        1,64,1,64,1,65,1,65,1,65,1,65,1,65,1,65,5,65,548,8,65,10,65,12,65,
        551,9,65,1,66,1,66,1,66,1,66,1,66,1,66,5,66,559,8,66,10,66,12,66,
        562,9,66,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,
        1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,5,67,585,8,67,
        10,67,12,67,588,9,67,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,
        5,68,599,8,68,10,68,12,68,602,9,68,1,69,1,69,1,69,1,69,1,69,1,69,
        1,69,1,69,1,69,1,69,1,69,1,69,5,69,616,8,69,10,69,12,69,619,9,69,
        1,70,1,70,1,70,1,70,1,70,3,70,626,8,70,1,71,1,71,1,71,1,71,1,71,
        1,71,1,71,1,71,1,71,1,71,5,71,638,8,71,10,71,12,71,641,9,71,1,72,
        1,72,1,73,1,73,1,73,1,73,1,73,1,73,3,73,651,8,73,1,74,1,74,1,74,
        1,74,1,74,1,74,3,74,659,8,74,1,75,1,75,1,75,1,75,1,75,3,75,666,8,
        75,1,76,1,76,1,76,0,7,52,130,132,134,136,138,142,77,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,
        132,134,136,138,140,142,144,146,148,150,152,0,4,1,0,42,47,2,0,19,
        22,59,59,1,0,1,4,1,1,49,49,676,0,154,1,0,0,0,2,161,1,0,0,0,4,167,
        1,0,0,0,6,174,1,0,0,0,8,178,1,0,0,0,10,183,1,0,0,0,12,196,1,0,0,
        0,14,198,1,0,0,0,16,204,1,0,0,0,18,209,1,0,0,0,20,215,1,0,0,0,22,
        219,1,0,0,0,24,226,1,0,0,0,26,234,1,0,0,0,28,241,1,0,0,0,30,243,
        1,0,0,0,32,246,1,0,0,0,34,254,1,0,0,0,36,256,1,0,0,0,38,263,1,0,
        0,0,40,281,1,0,0,0,42,286,1,0,0,0,44,288,1,0,0,0,46,290,1,0,0,0,
        48,297,1,0,0,0,50,303,1,0,0,0,52,305,1,0,0,0,54,318,1,0,0,0,56,322,
        1,0,0,0,58,324,1,0,0,0,60,331,1,0,0,0,62,333,1,0,0,0,64,335,1,0,
        0,0,66,347,1,0,0,0,68,355,1,0,0,0,70,363,1,0,0,0,72,380,1,0,0,0,
        74,382,1,0,0,0,76,393,1,0,0,0,78,395,1,0,0,0,80,400,1,0,0,0,82,402,
        1,0,0,0,84,404,1,0,0,0,86,410,1,0,0,0,88,412,1,0,0,0,90,414,1,0,
        0,0,92,426,1,0,0,0,94,432,1,0,0,0,96,442,1,0,0,0,98,451,1,0,0,0,
        100,461,1,0,0,0,102,470,1,0,0,0,104,478,1,0,0,0,106,480,1,0,0,0,
        108,487,1,0,0,0,110,491,1,0,0,0,112,498,1,0,0,0,114,500,1,0,0,0,
        116,504,1,0,0,0,118,514,1,0,0,0,120,524,1,0,0,0,122,531,1,0,0,0,
        124,533,1,0,0,0,126,537,1,0,0,0,128,539,1,0,0,0,130,541,1,0,0,0,
        132,552,1,0,0,0,134,563,1,0,0,0,136,589,1,0,0,0,138,603,1,0,0,0,
        140,625,1,0,0,0,142,627,1,0,0,0,144,642,1,0,0,0,146,650,1,0,0,0,
        148,658,1,0,0,0,150,665,1,0,0,0,152,667,1,0,0,0,154,155,3,2,1,0,
        155,156,5,0,0,1,156,1,1,0,0,0,157,162,1,0,0,0,158,159,3,6,3,0,159,
        160,3,4,2,0,160,162,1,0,0,0,161,157,1,0,0,0,161,158,1,0,0,0,162,
        3,1,0,0,0,163,168,1,0,0,0,164,165,3,6,3,0,165,166,3,4,2,0,166,168,
        1,0,0,0,167,163,1,0,0,0,167,164,1,0,0,0,168,5,1,0,0,0,169,175,3,
        8,4,0,170,175,3,10,5,0,171,175,3,14,7,0,172,175,3,16,8,0,173,175,
        3,18,9,0,174,169,1,0,0,0,174,170,1,0,0,0,174,171,1,0,0,0,174,172,
        1,0,0,0,174,173,1,0,0,0,175,176,1,0,0,0,176,177,3,152,76,0,177,7,
        1,0,0,0,178,179,5,23,0,0,179,180,5,59,0,0,180,181,5,42,0,0,181,182,
        3,128,64,0,182,9,1,0,0,0,183,184,5,24,0,0,184,185,3,12,6,0,185,11,
        1,0,0,0,186,187,5,59,0,0,187,188,3,86,43,0,188,189,5,42,0,0,189,
        190,3,128,64,0,190,197,1,0,0,0,191,192,5,59,0,0,192,197,3,86,43,
        0,193,194,5,59,0,0,194,195,5,42,0,0,195,197,3,128,64,0,196,186,1,
        0,0,0,196,191,1,0,0,0,196,193,1,0,0,0,197,13,1,0,0,0,198,199,5,16,
        0,0,199,202,5,59,0,0,200,203,3,96,48,0,201,203,3,100,50,0,202,200,
        1,0,0,0,202,201,1,0,0,0,203,15,1,0,0,0,204,205,5,15,0,0,205,206,
        5,59,0,0,206,207,3,24,12,0,207,208,3,34,17,0,208,17,1,0,0,0,209,
        210,5,15,0,0,210,211,3,20,10,0,211,212,5,59,0,0,212,213,3,24,12,
        0,213,214,3,34,17,0,214,19,1,0,0,0,215,216,5,51,0,0,216,217,3,22,
        11,0,217,218,5,52,0,0,218,21,1,0,0,0,219,220,5,59,0,0,220,221,3,
        86,43,0,221,23,1,0,0,0,222,227,3,26,13,0,223,224,3,26,13,0,224,225,
        3,32,16,0,225,227,1,0,0,0,226,222,1,0,0,0,226,223,1,0,0,0,227,25,
        1,0,0,0,228,229,5,51,0,0,229,235,5,52,0,0,230,231,5,51,0,0,231,232,
        3,28,14,0,232,233,5,52,0,0,233,235,1,0,0,0,234,228,1,0,0,0,234,230,
        1,0,0,0,235,27,1,0,0,0,236,242,3,30,15,0,237,238,3,30,15,0,238,239,
        5,50,0,0,239,240,3,28,14,0,240,242,1,0,0,0,241,236,1,0,0,0,241,237,
        1,0,0,0,242,29,1,0,0,0,243,244,3,108,54,0,244,245,3,86,43,0,245,
        31,1,0,0,0,246,247,3,86,43,0,247,33,1,0,0,0,248,249,5,53,0,0,249,
        255,5,54,0,0,250,251,5,53,0,0,251,252,3,36,18,0,252,253,5,54,0,0,
        253,255,1,0,0,0,254,248,1,0,0,0,254,250,1,0,0,0,255,35,1,0,0,0,256,
        257,3,40,20,0,257,258,3,38,19,0,258,37,1,0,0,0,259,264,1,0,0,0,260,
        261,3,40,20,0,261,262,3,38,19,0,262,264,1,0,0,0,263,259,1,0,0,0,
        263,260,1,0,0,0,264,39,1,0,0,0,265,282,3,6,3,0,266,267,3,42,21,0,
        267,268,3,152,76,0,268,282,1,0,0,0,269,270,3,60,30,0,270,271,3,152,
        76,0,271,282,1,0,0,0,272,273,3,62,31,0,273,274,3,152,76,0,274,282,
        1,0,0,0,275,276,3,64,32,0,276,277,3,152,76,0,277,282,1,0,0,0,278,
        282,3,34,17,0,279,282,3,66,33,0,280,282,3,72,36,0,281,265,1,0,0,
        0,281,266,1,0,0,0,281,269,1,0,0,0,281,272,1,0,0,0,281,275,1,0,0,
        0,281,278,1,0,0,0,281,279,1,0,0,0,281,280,1,0,0,0,282,41,1,0,0,0,
        283,287,3,54,27,0,284,287,3,58,29,0,285,287,3,44,22,0,286,283,1,
        0,0,0,286,284,1,0,0,0,286,285,1,0,0,0,287,43,1,0,0,0,288,289,3,46,
        23,0,289,45,1,0,0,0,290,291,5,59,0,0,291,292,3,48,24,0,292,47,1,
        0,0,0,293,298,3,50,25,0,294,295,3,50,25,0,295,296,3,48,24,0,296,
        298,1,0,0,0,297,293,1,0,0,0,297,294,1,0,0,0,298,49,1,0,0,0,299,300,
        5,58,0,0,300,304,5,59,0,0,301,304,3,92,46,0,302,304,3,148,74,0,303,
        299,1,0,0,0,303,301,1,0,0,0,303,302,1,0,0,0,304,51,1,0,0,0,305,306,
        6,26,-1,0,306,307,5,59,0,0,307,315,1,0,0,0,308,309,10,2,0,0,309,
        310,5,58,0,0,310,314,5,59,0,0,311,312,10,1,0,0,312,314,3,92,46,0,
        313,308,1,0,0,0,313,311,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,
        315,316,1,0,0,0,316,53,1,0,0,0,317,315,1,0,0,0,318,319,3,52,26,0,
        319,320,3,56,28,0,320,321,3,128,64,0,321,55,1,0,0,0,322,323,7,0,
        0,0,323,57,1,0,0,0,324,325,3,52,26,0,325,326,5,57,0,0,326,327,3,
        128,64,0,327,59,1,0,0,0,328,332,5,11,0,0,329,330,5,11,0,0,330,332,
        3,128,64,0,331,328,1,0,0,0,331,329,1,0,0,0,332,61,1,0,0,0,333,334,
        5,13,0,0,334,63,1,0,0,0,335,336,5,12,0,0,336,65,1,0,0,0,337,338,
        5,8,0,0,338,339,3,70,35,0,339,340,3,34,17,0,340,341,3,152,76,0,341,
        348,1,0,0,0,342,343,5,8,0,0,343,344,3,70,35,0,344,345,3,34,17,0,
        345,346,3,68,34,0,346,348,1,0,0,0,347,337,1,0,0,0,347,342,1,0,0,
        0,348,67,1,0,0,0,349,350,5,9,0,0,350,351,3,34,17,0,351,352,3,152,
        76,0,352,356,1,0,0,0,353,354,5,9,0,0,354,356,3,66,33,0,355,349,1,
        0,0,0,355,353,1,0,0,0,356,69,1,0,0,0,357,358,5,51,0,0,358,364,5,
        52,0,0,359,360,5,51,0,0,360,361,3,128,64,0,361,362,5,52,0,0,362,
        364,1,0,0,0,363,357,1,0,0,0,363,359,1,0,0,0,364,71,1,0,0,0,365,366,
        5,10,0,0,366,367,3,128,64,0,367,368,3,34,17,0,368,369,3,152,76,0,
        369,381,1,0,0,0,370,371,5,10,0,0,371,372,3,74,37,0,372,373,3,34,
        17,0,373,374,3,152,76,0,374,381,1,0,0,0,375,376,5,10,0,0,376,377,
        3,78,39,0,377,378,3,34,17,0,378,379,3,152,76,0,379,381,1,0,0,0,380,
        365,1,0,0,0,380,370,1,0,0,0,380,375,1,0,0,0,381,73,1,0,0,0,382,383,
        3,76,38,0,383,384,5,49,0,0,384,385,3,128,64,0,385,386,5,49,0,0,386,
        387,3,76,38,0,387,75,1,0,0,0,388,394,1,0,0,0,389,394,3,80,40,0,390,
        394,3,82,41,0,391,394,3,84,42,0,392,394,3,10,5,0,393,388,1,0,0,0,
        393,389,1,0,0,0,393,390,1,0,0,0,393,391,1,0,0,0,393,392,1,0,0,0,
        394,77,1,0,0,0,395,396,3,108,54,0,396,397,5,57,0,0,397,398,5,14,
        0,0,398,399,3,128,64,0,399,79,1,0,0,0,400,401,3,128,64,0,401,81,
        1,0,0,0,402,403,3,54,27,0,403,83,1,0,0,0,404,405,3,58,29,0,405,85,
        1,0,0,0,406,411,3,88,44,0,407,411,3,90,45,0,408,411,3,96,48,0,409,
        411,3,100,50,0,410,406,1,0,0,0,410,407,1,0,0,0,410,408,1,0,0,0,410,
        409,1,0,0,0,411,87,1,0,0,0,412,413,7,1,0,0,413,89,1,0,0,0,414,415,
        3,92,46,0,415,416,3,88,44,0,416,91,1,0,0,0,417,418,5,55,0,0,418,
        419,3,94,47,0,419,420,5,56,0,0,420,427,1,0,0,0,421,422,5,55,0,0,
        422,423,3,94,47,0,423,424,5,56,0,0,424,425,3,92,46,0,425,427,1,0,
        0,0,426,417,1,0,0,0,426,421,1,0,0,0,427,93,1,0,0,0,428,433,5,1,0,
        0,429,433,5,59,0,0,430,433,3,44,22,0,431,433,3,128,64,0,432,428,
        1,0,0,0,432,429,1,0,0,0,432,430,1,0,0,0,432,431,1,0,0,0,433,95,1,
        0,0,0,434,435,5,17,0,0,435,436,5,53,0,0,436,443,5,54,0,0,437,438,
        5,17,0,0,438,439,5,53,0,0,439,440,3,98,49,0,440,441,5,54,0,0,441,
        443,1,0,0,0,442,434,1,0,0,0,442,437,1,0,0,0,443,97,1,0,0,0,444,445,
        3,106,53,0,445,446,3,152,76,0,446,452,1,0,0,0,447,448,3,106,53,0,
        448,449,3,152,76,0,449,450,3,98,49,0,450,452,1,0,0,0,451,444,1,0,
        0,0,451,447,1,0,0,0,452,99,1,0,0,0,453,454,5,18,0,0,454,455,5,53,
        0,0,455,462,5,54,0,0,456,457,5,18,0,0,457,458,5,53,0,0,458,459,3,
        102,51,0,459,460,5,54,0,0,460,462,1,0,0,0,461,453,1,0,0,0,461,456,
        1,0,0,0,462,101,1,0,0,0,463,464,3,104,52,0,464,465,3,152,76,0,465,
        471,1,0,0,0,466,467,3,104,52,0,467,468,3,152,76,0,468,469,3,102,
        51,0,469,471,1,0,0,0,470,463,1,0,0,0,470,466,1,0,0,0,471,103,1,0,
        0,0,472,473,5,59,0,0,473,479,3,26,13,0,474,475,5,59,0,0,475,476,
        3,26,13,0,476,477,3,32,16,0,477,479,1,0,0,0,478,472,1,0,0,0,478,
        474,1,0,0,0,479,105,1,0,0,0,480,481,5,59,0,0,481,482,3,86,43,0,482,
        107,1,0,0,0,483,488,5,59,0,0,484,485,5,59,0,0,485,486,5,50,0,0,486,
        488,3,108,54,0,487,483,1,0,0,0,487,484,1,0,0,0,488,109,1,0,0,0,489,
        492,3,112,56,0,490,492,3,116,58,0,491,489,1,0,0,0,491,490,1,0,0,
        0,492,111,1,0,0,0,493,499,5,25,0,0,494,499,5,5,0,0,495,499,5,7,0,
        0,496,499,5,6,0,0,497,499,3,114,57,0,498,493,1,0,0,0,498,494,1,0,
        0,0,498,495,1,0,0,0,498,496,1,0,0,0,498,497,1,0,0,0,499,113,1,0,
        0,0,500,501,7,2,0,0,501,115,1,0,0,0,502,505,5,59,0,0,503,505,3,90,
        45,0,504,502,1,0,0,0,504,503,1,0,0,0,505,506,1,0,0,0,506,507,3,118,
        59,0,507,117,1,0,0,0,508,509,5,53,0,0,509,515,5,54,0,0,510,511,5,
        53,0,0,511,512,3,120,60,0,512,513,5,54,0,0,513,515,1,0,0,0,514,508,
        1,0,0,0,514,510,1,0,0,0,515,119,1,0,0,0,516,525,3,122,61,0,517,518,
        3,122,61,0,518,519,5,50,0,0,519,525,1,0,0,0,520,521,3,122,61,0,521,
        522,5,50,0,0,522,523,3,120,60,0,523,525,1,0,0,0,524,516,1,0,0,0,
        524,517,1,0,0,0,524,520,1,0,0,0,525,121,1,0,0,0,526,532,3,126,63,
        0,527,528,3,124,62,0,528,529,5,48,0,0,529,530,3,126,63,0,530,532,
        1,0,0,0,531,526,1,0,0,0,531,527,1,0,0,0,532,123,1,0,0,0,533,534,
        5,59,0,0,534,125,1,0,0,0,535,538,3,118,59,0,536,538,3,128,64,0,537,
        535,1,0,0,0,537,536,1,0,0,0,538,127,1,0,0,0,539,540,3,130,65,0,540,
        129,1,0,0,0,541,542,6,65,-1,0,542,543,3,132,66,0,543,549,1,0,0,0,
        544,545,10,1,0,0,545,546,5,40,0,0,546,548,3,132,66,0,547,544,1,0,
        0,0,548,551,1,0,0,0,549,547,1,0,0,0,549,550,1,0,0,0,550,131,1,0,
        0,0,551,549,1,0,0,0,552,553,6,66,-1,0,553,554,3,134,67,0,554,560,
        1,0,0,0,555,556,10,1,0,0,556,557,5,39,0,0,557,559,3,134,67,0,558,
        555,1,0,0,0,559,562,1,0,0,0,560,558,1,0,0,0,560,561,1,0,0,0,561,
        133,1,0,0,0,562,560,1,0,0,0,563,564,6,67,-1,0,564,565,3,136,68,0,
        565,586,1,0,0,0,566,567,10,6,0,0,567,568,5,33,0,0,568,585,3,136,
        68,0,569,570,10,5,0,0,570,571,5,34,0,0,571,585,3,136,68,0,572,573,
        10,4,0,0,573,574,5,35,0,0,574,585,3,136,68,0,575,576,10,3,0,0,576,
        577,5,36,0,0,577,585,3,136,68,0,578,579,10,2,0,0,579,580,5,37,0,
        0,580,585,3,136,68,0,581,582,10,1,0,0,582,583,5,38,0,0,583,585,3,
        136,68,0,584,566,1,0,0,0,584,569,1,0,0,0,584,572,1,0,0,0,584,575,
        1,0,0,0,584,578,1,0,0,0,584,581,1,0,0,0,585,588,1,0,0,0,586,584,
        1,0,0,0,586,587,1,0,0,0,587,135,1,0,0,0,588,586,1,0,0,0,589,590,
        6,68,-1,0,590,591,3,138,69,0,591,600,1,0,0,0,592,593,10,2,0,0,593,
        594,5,28,0,0,594,599,3,138,69,0,595,596,10,1,0,0,596,597,5,29,0,
        0,597,599,3,138,69,0,598,592,1,0,0,0,598,595,1,0,0,0,599,602,1,0,
        0,0,600,598,1,0,0,0,600,601,1,0,0,0,601,137,1,0,0,0,602,600,1,0,
        0,0,603,604,6,69,-1,0,604,605,3,140,70,0,605,617,1,0,0,0,606,607,
        10,3,0,0,607,608,5,30,0,0,608,616,3,140,70,0,609,610,10,2,0,0,610,
        611,5,31,0,0,611,616,3,140,70,0,612,613,10,1,0,0,613,614,5,32,0,
        0,614,616,3,140,70,0,615,606,1,0,0,0,615,609,1,0,0,0,615,612,1,0,
        0,0,616,619,1,0,0,0,617,615,1,0,0,0,617,618,1,0,0,0,618,139,1,0,
        0,0,619,617,1,0,0,0,620,626,3,142,71,0,621,622,5,41,0,0,622,626,
        3,140,70,0,623,624,5,29,0,0,624,626,3,140,70,0,625,620,1,0,0,0,625,
        621,1,0,0,0,625,623,1,0,0,0,626,141,1,0,0,0,627,628,6,71,-1,0,628,
        629,3,144,72,0,629,639,1,0,0,0,630,631,10,3,0,0,631,632,5,58,0,0,
        632,638,5,59,0,0,633,634,10,2,0,0,634,638,3,92,46,0,635,636,10,1,
        0,0,636,638,3,148,74,0,637,630,1,0,0,0,637,633,1,0,0,0,637,635,1,
        0,0,0,638,641,1,0,0,0,639,637,1,0,0,0,639,640,1,0,0,0,640,143,1,
        0,0,0,641,639,1,0,0,0,642,643,3,146,73,0,643,145,1,0,0,0,644,651,
        3,110,55,0,645,651,5,59,0,0,646,647,5,51,0,0,647,648,3,128,64,0,
        648,649,5,52,0,0,649,651,1,0,0,0,650,644,1,0,0,0,650,645,1,0,0,0,
        650,646,1,0,0,0,651,147,1,0,0,0,652,653,5,51,0,0,653,659,5,52,0,
        0,654,655,5,51,0,0,655,656,3,150,75,0,656,657,5,52,0,0,657,659,1,
        0,0,0,658,652,1,0,0,0,658,654,1,0,0,0,659,149,1,0,0,0,660,666,3,
        128,64,0,661,662,3,128,64,0,662,663,5,50,0,0,663,664,3,150,75,0,
        664,666,1,0,0,0,665,660,1,0,0,0,665,661,1,0,0,0,666,151,1,0,0,0,
        667,668,7,3,0,0,668,153,1,0,0,0,52,161,167,174,196,202,226,234,241,
        254,263,281,286,297,303,313,315,331,347,355,363,380,393,410,426,
        432,442,451,461,470,478,487,491,498,504,514,524,531,537,549,560,
        584,586,598,600,615,617,625,637,639,650,658,665
    ]

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
                     "'.'", "<INVALID>", "'\\n'" ]

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
        self.checkVersion("4.13.1")
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




    def decl_list(self):

        localctx = MiniGoParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [15, 16, 23, 24]:
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




    def decl_list_tail(self):

        localctx = MiniGoParser.Decl_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_list_tail)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [15, 16, 23, 24]:
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
            if token in [17]:
                self.state = 200
                self.structType()
                pass
            elif token in [18]:
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




    def statementList_tail(self):

        localctx = MiniGoParser.StatementList_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statementList_tail)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [8, 10, 11, 12, 13, 15, 16, 23, 24, 53, 59]:
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




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.declaration()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.basicStatement()
                self.state = 267
                self.endOfSentence()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.returnStatement()
                self.state = 270
                self.endOfSentence()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.breakStatement()
                self.state = 273
                self.endOfSentence()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.continueStatement()
                self.state = 276
                self.endOfSentence()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 6)
                self.state = 278
                self.block()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 279
                self.ifStatement()
                pass
            elif token in [10]:
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




    def chainItem(self):

        localctx = MiniGoParser.ChainItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_chainItem)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(MiniGoParser.DOT)
                self.state = 300
                self.match(MiniGoParser.ID)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.index()
                pass
            elif token in [51]:
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




    def assignOperations(self):

        localctx = MiniGoParser.AssignOperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignOperations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 277076930199552) != 0)):
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




    def type_(self):

        localctx = MiniGoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_type_)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 22, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.typeName()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.arrayType()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.structType()
                pass
            elif token in [18]:
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




    def typeName(self):

        localctx = MiniGoParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752311287808) != 0)):
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




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.basicLiteral()
                pass
            elif token in [55, 59]:
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




    def basicLiteral(self):

        localctx = MiniGoParser.BasicLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_basicLiteral)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(MiniGoParser.NIL)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.match(MiniGoParser.BOOLEAN_LIT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 495
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 496
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [1, 2, 3, 4]:
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




    def integerLiteral(self):

        localctx = MiniGoParser.IntegerLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_integerLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
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




    def compositeLiteral(self):

        localctx = MiniGoParser.CompositeLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_compositeLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.state = 502
                self.match(MiniGoParser.ID)
                pass
            elif token in [55]:
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




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_value)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.compositeLiteralValue()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 25, 29, 41, 51, 55, 59]:
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




    def unary(self):

        localctx = MiniGoParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_unary)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 25, 51, 55, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.postfix(0)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self.match(MiniGoParser.NOT)
                self.state = 622
                self.unary()
                pass
            elif token in [29]:
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




    def endOfSentence(self):

        localctx = MiniGoParser.EndOfSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_endOfSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            _la = self._input.LA(1)
            if not(_la==-1 or _la==49):
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
         




