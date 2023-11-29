from sys import path as __PATH; __PATH.insert(0, '/home/ganer/Projects/cpy/imports') ; del __PATH ; from CPY_HEADER import * # CPY-a-2023/11/29_14:02:14 
from  operator import  add as add_
from  builtins import  print as print_, map as map_, zip as zip_, \
             isinstance as INST_
from  functools import  reduce
from  itertools import  product as product_
from  copy import  deepcopy as dcp
from  types import  UnionType


class  OP_:
    __slots__ = ('f', 'd', 'FT', 'kw')
    def  __new__( SPECIAL_CLASS_ ,f,d= None ,FT= None ,** KWARGS_ ):
        C = type("OP", ( SPECIAL_CLASS_ , ), {})
        DEGEN_( setattr(C, m, (<$ SPECIAL_SELF_ ,o,k=k$> SPECIAL_SELF_ .check(k,o))) for m,k in KWARGS_ .items())
        C.__call__ = staticmethod(f)
        if FT:
            C.__getattr__ = <$x,y$>getattr(FT, y)
            C.__invert__ = SPECIAL_SELF_ $> SPECIAL_SELF_ .FT 
        o = super().__new__(C)
        o.f , o.d , o.FT , o.kw  = f, d or {}, FT, KWARGS_ 
        return o
    check = SPECIAL_SELF_ ,k,v $> ASSERT_ (k not in SPECIAL_SELF_ .d ) and type( SPECIAL_SELF_ )( SPECIAL_SELF_ .f , {k:v}| SPECIAL_SELF_ .d , SPECIAL_SELF_ .FT , ** SPECIAL_SELF_ .kw )
class  OP_UNARY_ (OP_):
    def  check( SPECIAL_SELF_ , k, v):
        d = ( SPECIAL_SELF_  := super().check(k,v)).d 
        return  SPECIAL_SELF_ .f (d[v]) if (v:="l") in d or (v:="r") in d else  SPECIAL_SELF_ 
class  OP_BNARY_ (OP_):
    def  check( SPECIAL_SELF_ , k, v):
        d = ( SPECIAL_SELF_  := super().check(k,v)).d 
        return  SPECIAL_SELF_ .f (d["l"],d["r"]) if "l" in d and "r" in d else  SPECIAL_SELF_ 

def  isinstance(x, y):
    if INST_(y,type|UnionType): None 
    elif INST_(y,OP_): y=y.FT 
    elif INST_(y,list|tuple|set): return any(isinstance(x,z) for z in y)
    else : y=type(y)
    return  INST_(x, y)

par_or_  = dict( __ror__="l",  __or__="r")
par_pow_ = dict(__rpow__="l", __pow__="r")
par_mul_ = dict(__rmul__="l", __mul__="r")
par_add_ = dict(__radd__="l", __add__="r")
OP_TO_UNARY_ = OP_UNARY_ (f$> OP_UNARY_ (f, **par_or_, **par_mul_), __rpow__="l")
OP_TO_BNARY_ = OP_UNARY_ (f$> OP_BNARY_ (f, **par_or_, **par_mul_), __rpow__="l")

range_binary = OP_BNARY_ (range, **par_pow_)
skinniside_z = OP_UNARY_ (<$x$>1 if x>0 else 0, **par_mul_)
skinniside_b = OP_UNARY_ (<$x$>(1 if x>0 else -1) if x else 0, **par_mul_)
setattrs = f$>(<$x,y$> DEGEN_( setattr(f,a,b) for a,b in zip(x,y))) **OP_TO_BNARY_ 
other = (<$x,y$> ASSERT_ ( len (l:= magic_list *x)==2 and y in l) and l[y==l[0]]) **OP_TO_BNARY_ 
split_string = OP_UNARY_ (<$x$>[split_string(k," ") if " " in k else k for k in x.split( ARGS_ [0] if ARGS_  else " ")], **par_mul_)

RET_LEFT_ , RET_RGHT_  = OP_BNARY_ (<$x,y$>x, ** par_or_|par_pow_|par_mul_ ), OP_BNARY_ (<$x,y$>y, ** par_or_|par_pow_|par_mul_ )
MAX_ , MIN_  = max **OP_TO_BNARY_ , min **OP_TO_BNARY_ 
CONSTRAIN_  = (<$* ARGS_ ,f=(<$x,y,z$>min(max(z,x),y))$> (<$$>f(* ARGS_ ,a[0])) **OP_TO_BNARY_  if  len (a:= ARGS_ )==1 else  (<$x$>f(*a,x)) **OP_TO_UNARY_  if  len ARGS_ ==2 else  f(* ARGS_ )) **OP_TO_BNARY_ 
all , any  = all **OP_TO_BNARY_ , any **OP_TO_BNARY_ 
UNION_  = (<$$>set.union(*map_(set, ARGS_ ))) **OP_TO_BNARY_ 
INTERSECTION_  = (<$$>set.intersection(*map_(set, ARGS_ ))) **OP_TO_BNARY_ 
SET_MINUS_  = (<$$>set.__sub__(*map_(set, ARGS_ ))) **OP_TO_BNARY_ 
CROSS_  = (<$$>list(product_(* ARGS_ ))) **OP_TO_BNARY_ 
TRANSPOSE_  = (<$$>list( zip (* ARGS_ [0],** KWARGS_ ))) **OP_TO_UNARY_ 
zip  = (<$$>list(map(list,zip_(* ARGS_ ,** KWARGS_ )))) **OP_TO_BNARY_ 
REVERSE_  = OP_UNARY_ (<$x$>x[::-1], **par_mul_|par_pow_)
map  = (<$$>(list(map_(* ARGS_ )) if  len ( ARGS_ )>1 else  (<$* ARGS_ ,f= ARGS_ [0]$>list(map_(f,* ARGS_ ))) **OP_TO_UNARY_ )) **OP_TO_BNARY_ 
FOLD_  = (<$$>(reduce(* ARGS_ ) if  len ( ARGS_ )>1 else  (<$* ARGS_ ,f= ARGS_ [0]$>reduce(f,* ARGS_ )) **OP_TO_UNARY_ )) **OP_TO_BNARY_ 
sum  = (x$>reduce(add_,(x:=list(x)),*([ ARGS_ [0] if ARGS_  else 0] if  not x else []))) **OP_TO_BNARY_ 
PROD_  = (x$>reduce(<$x,y$>x*y,(x:=list(x)),*([ ARGS_ [0] if ARGS_  else 0] if  not x else []))) **OP_TO_BNARY_ 
len  = OP_UNARY_ (len, **par_mul_|par_pow_)
enlist  = OP_UNARY_ (<$x$>[x], **par_mul_|par_pow_)
print  = OP_UNARY_ (<$$>print_(* ARGS_ ,** KWARGS_ ) or ( ARGS_ [0] if ARGS_ )) **OP_TO_UNARY_ 
enumerate  = OP_UNARY_ (enumerate, **par_mul_)
range  = OP_UNARY_ (range, **par_mul_|par_pow_)
isinstance  = isinstance **OP_TO_BNARY_ 

mk_type = <$x$> OP_UNARY_ (x, FT=x, ** KWARGS_ )
magic_str   = mk_type(str, **par_mul_)
magic_set   = mk_type(set, **par_mul_)
magic_frozenset  = mk_type(frozenset, **par_mul_)
magic_int   = mk_type(int, **par_mul_)
magic_float   = mk_type(float, **par_mul_)
magic_list   = mk_type(list, **par_mul_)
magic_tuple   = mk_type(tuple, **par_mul_)
magic_dict   = mk_type(dict, **par_mul_)