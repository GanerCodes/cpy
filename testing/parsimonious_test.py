from sys import path as __PATH; __PATH.insert(0, '/home/ganer/Projects/cpy/imports') ; del __PATH ; from CPY_HEADER import * # CPY-a-2023/10/29_17:05:08 
from  parsimonious.grammar import  Grammar
R = <$x$>open(x).read()
print *Grammar(R('gram')).parse(R("code"))