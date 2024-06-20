from sys import path as __PATH; __PATH.insert(0, '/home/ganer/Projects/cpy/imports') ; del __PATH ; from CPY_HEADER import * # CPY-a-2024/06/20_13:12:59 
from  collections import  deque
from  pprint import  PrettyPrinter
pprint = PrettyPrinter(2).pprint

DEGEN_  = g$>deque(g,maxlen=0)
def  ASSERT_ (c,t='\U00002a33'): assert c,t; return c
EMPTY_STRING , MATH_COMPLEX_UNIT  = '', 1j
MATH_TAU  = 2*( MATH_PI  := 3.14159265359)
MATH_INFINITY  = float("inf")

class  Namespace(dict):
    __init__ = SPECIAL_SELF_ $>super().__init__(** KWARGS_ )
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
    __iter__ = SPECIAL_SELF_ $>iter( SPECIAL_SELF_ .items())
    __repr__ = SPECIAL_SELF_ $> f"""\U00002135({(', '.join( f"""{k}={v}"""  for k,v in SPECIAL_SELF_ ))})""" 
    copy = SPECIAL_SELF_ $> Namespace (**super().copy())
class  pait:
    import  subprocess as ρ
    def  __call__( SPECIAL_SELF_ ,s,* ARGS_ ,** KWARGS_ ):
        b = KWARGS_ .pop("background", False )
        proc = SPECIAL_SELF_ .ρ .Popen(s.split(' '),* ARGS_ ,** KWARGS_ )
        return  (proc.wait() and  False  if  not b) or  proc
    _parse = SPECIAL_SELF_ ,o$>o.read().decode()
    r = SPECIAL_SELF_ $> SPECIAL_SELF_ (* ARGS_ ,** KWARGS_ ).return_code
    S = SPECIAL_SELF_ $> SPECIAL_SELF_ ._parse( SPECIAL_SELF_ (* ARGS_ ,stdout= SPECIAL_SELF_ .ρ .PIPE,** KWARGS_ ).stdout)
    E = SPECIAL_SELF_ $> SPECIAL_SELF_ ._parse( SPECIAL_SELF_ (* ARGS_ ,stderr= SPECIAL_SELF_ .ρ .PIPE,** KWARGS_ ).stderr)
    b = SPECIAL_SELF_ $> SPECIAL_SELF_ (* ARGS_ ,background= True ,stdout= SPECIAL_SELF_ .ρ .PIPE,stderr= SPECIAL_SELF_ .ρ .PIPE,** KWARGS_ )
    def  B( SPECIAL_SELF_ ,* ARGS_ ,** KWARGS_ ):
        o = SPECIAL_SELF_ (* ARGS_ ,stdout= SPECIAL_SELF_ .ρ .PIPE,stderr= SPECIAL_SELF_ .ρ .PIPE,** KWARGS_ )
        return  SPECIAL_SELF_ ._parse(o.stdout), SPECIAL_SELF_ ._parse(o.stderr)
    def  A( SPECIAL_SELF_ ,* ARGS_ ,** KWARGS_ ):
        o = SPECIAL_SELF_ (* ARGS_ ,stdout= SPECIAL_SELF_ .ρ .PIPE,stderr= SPECIAL_SELF_ .ρ .PIPE,** KWARGS_ )
        return  o.return_code, SPECIAL_SELF_ ._parse(o.stdout), SPECIAL_SELF_ ._parse(o.stderr)
pait = pait()