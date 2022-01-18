#!/usr/bin/env python

from rubiks_cube_check import Check
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)7s: %(message)s"
)


Cube = list("OBBOYYWWRWWROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG")
#Cube = list("BBBOYYWWRWWROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG") #0 !=9
#Cube = list("OBBWYYWWRWOROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG") #1 4 <-> 11
#Cube = list("OBBOYYBWRWWWOORGOGRRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG") #2 7 -> 12 -> 19 -> [7]
#Cube = list("OBBOYYWWRWWROORGOGBRYBBGWRYBGORRYBGYWWGBGYOBYRYOGWWROG") #3
Result = Check(Cube)
print(Result)

'''
       O B B                              01 02 03                    
       O Y Y                              04 05 06                    
       W W R                              07 08 09                    
                                                                      
W W R  B R Y  B G O  W W G      10 11 12  19 20 21  28 29 30  37 38 39
O O R  B B G  R R Y  B G Y      13 14 15  22 23 24  31 32 33  40 41 42
G O G  W R Y  B G Y  O B Y      16 17 18  25 26 27  34 35 36  43 44 45
                                                                      
       R Y O                              46 47 48                    
       G W W                              49 50 51                    
       R O G                              52 53 54                    
'''

