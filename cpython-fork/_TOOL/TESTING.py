
from  collections import  deque
from  pprint import  PrettyPrinter
def  ASSERT_(c,t='\U00002a33'): assert c,t; return c
pprint = PrettyPrinter(2).pprint
DEGEN_=g$>deque(g,maxlen=0)
EMPTY_STRING=''
COMPLEX_UNIT=1j
MATH_PI = 3.14159265359
MATH_TAU = 6.28318530718
class  pait:
    import  subprocess as SP
    def  __call__( SPECIAL_SELF_ ,s,* ARGS_ ,** KWARGS_ ):
        proc = SPECIAL_SELF_ .SP.Popen(s.split(' '),* ARGS_ ,** KWARGS_ )
        return  (proc.wait() and  False  if  "background" not in  KWARGS_ ) or  proc
    _parse = SPECIAL_SELF_ ,o$>o.read().decode()
    r = SPECIAL_SELF_ $> SPECIAL_SELF_ (* ARGS_ ,** KWARGS_ ).return_code
    S = SPECIAL_SELF_ $> SPECIAL_SELF_ ._parse( SPECIAL_SELF_ (* ARGS_ ,stdout= SPECIAL_SELF_ .SP.PIPE,** KWARGS_ ).stdout)
    E = SPECIAL_SELF_ $> SPECIAL_SELF_ ._parse( SPECIAL_SELF_ (* ARGS_ ,stderr= SPECIAL_SELF_ .SP.PIPE,** KWARGS_ ).stderr)
    b = SPECIAL_SELF_ $> SPECIAL_SELF_ (* ARGS_ ,background= True ,stdout= SPECIAL_SELF_ .SP.PIPE,stderr= SPECIAL_SELF_ .SP.PIPE,** KWARGS_ )
    def  B( SPECIAL_SELF_ ,* ARGS_ ,** KWARGS_ ):
        o = SPECIAL_SELF_ (* ARGS_ ,stdout= SPECIAL_SELF_ .SP.PIPE,stderr= SPECIAL_SELF_ .SP.PIPE,** KWARGS_ )
        return  SPECIAL_SELF_ ._parse(o.stdout), SPECIAL_SELF_ ._parse(o.stderr)
    def  A( SPECIAL_SELF_ ,* ARGS_ ,** KWARGS_ ):
        o = SPECIAL_SELF_ (* ARGS_ ,stdout= SPECIAL_SELF_ .SP.PIPE,stderr= SPECIAL_SELF_ .SP.PIPE,** KWARGS_ )
        return  o.return_code, SPECIAL_SELF_ ._parse(o.stdout), SPECIAL_SELF_ ._parse(o.stderr)
pait = pait()
from  operator import  add as add_
from  builtins import  print as print_, map as map_, zip as zip_
from  functools import  reduce

# Note: <<>> forces x**OP_TO_UNARY_<<y**OP_TO_BNARY_>>z**OP_TO_UNARY_

class  OP_:
    def  __new__( SPECIAL_CLASS_ ,f,d= None ,** KWARGS_ ):
        C = type("OP", ( SPECIAL_CLASS_ , ), {})
        DEGEN_( setattr(C, m, (<$ SPECIAL_SELF_ ,o,k=k$> SPECIAL_SELF_ .check(k,o))) for m,k in  KWARGS_ .items())
        C.__call__ = staticmethod(f)
        o = super().__new__(C)
        o.f, o.d, o.kw = f, d or {}, KWARGS_ 
        return o
    check = SPECIAL_SELF_ ,k,v $> ASSERT_ (k not in  SPECIAL_SELF_ .d) and type( SPECIAL_SELF_ )( SPECIAL_SELF_ .f, {k:v}| SPECIAL_SELF_ .d, ** SPECIAL_SELF_ .kw)
    __rlshift__ = SPECIAL_SELF_ ,o $> (o:=COAR_OP_(o)) and OP_BNARY_(<$x,y$> SPECIAL_SELF_ .f(o.f(x),y), SPECIAL_SELF_ .d.copy(), ** SPECIAL_SELF_ .kw)
    __rshift__  = SPECIAL_SELF_ ,o $> (o:=COAR_OP_(o)) and OP_BNARY_(<$x,y$> SPECIAL_SELF_ .f(x,o.f(y)), SPECIAL_SELF_ .d.copy(), ** SPECIAL_SELF_ .kw)
class  OP_UNARY_(OP_):
    def  check( SPECIAL_SELF_ , k, v):
        d = ( SPECIAL_SELF_  := super().check(k, v)).d
        return  SPECIAL_SELF_ .f(d[v]) if (v:='l') in d or (v:='r') in d else  SPECIAL_SELF_ 
class  OP_BNARY_(OP_):
    def  check( SPECIAL_SELF_ , k, v):
        d = ( SPECIAL_SELF_  := super().check(k, v)).d
        return  SPECIAL_SELF_ .f(d['l'],d['r']) if 'l' in d and 'r' in d else  SPECIAL_SELF_ 

COAR_OP_ = f$>f if isinstance(f, OP_) else  OP_UNARY_(f, **par_or_)

def  SWAP_(o):
    assert  isinstance(o, OP_BNARY_)
    return  OP_BNARY_(
        <$x,y$>o.f(y,x),
        d=o.d, **o.kw)
def  COMPOSE_(f, g):
    f, g = COAR_OP_(f), COAR_OP_(g)
    assert  not  all ((A:=isinstance(f, OP_BNARY_),B:=isinstance(g, OP_BNARY_))), "Cannot compose two binary operators."
    f, g, K = f.f, g.f, {'d': f.d} | par_or_ #f.kw
    if  not A and  not B: return OP_UNARY_((x$>f(g(x))), **K)
    if  not A and  B: return OP_BNARY_((x,y$>f(g(x,y))), **K)
    if   A and  not B: return OP_BNARY_((x,y$>f(g(x),g(y))), **K)
def  DUP_(f):
    assert  isinstance(f, OP_BNARY_)
    return OP_UNARY_((x$>f.f(x,x)), **{'d': f.d} | f.kw)

par_or_  = dict( __ror__='l',  __or__='r')
par_pow_ = dict(__rpow__='l', __pow__='r')
par_mul_ = dict(__rmul__='l', __mul__='r')
par_add_ = dict(__radd__='l', __add__='r')
OP_TO_UNARY_ = OP_UNARY_(f$>OP_UNARY_(f, **par_or_), __rpow__='l')
OP_TO_BNARY_ = OP_UNARY_(f$>OP_BNARY_(f, **par_or_), __rpow__='l')
OP_SWAP_ = OP_UNARY_(SWAP_, __rmatmul__='l')
OP_DUP_ = OP_UNARY_(DUP_, __rmatmul__='l')
OP_COMPOSE_ = OP_BNARY_(COMPOSE_, **par_add_)
sum = (x$>reduce(add_,(x:=list(x)),*([ ARGS_ [0] if  ARGS_  else 0] if  not x else [])))**OP_TO_BNARY_
prod = (x$>reduce(<$x,y$>x*y,(x:=list(x)),*([ ARGS_ [0] if  ARGS_  else 0] if  not x else [])))**OP_TO_BNARY_
reduce **= OP_TO_BNARY_
isinstance = OP_BNARY_(isinstance, **par_pow_)
range = OP_UNARY_(range, **par_mul_)
range_binary = OP_BNARY_(range, **par_pow_)
enumerate = OP_UNARY_(enumerate, **par_mul_)
list = OP_UNARY_(list, **par_mul_)
print = OP_UNARY_(<$$>print_(* ARGS_ ,** KWARGS_ ) or ( ARGS_ [0] if  ARGS_ ), **par_mul_)
skinniside_z = OP_UNARY_(<$x$>1 if x>0 else 0, **par_mul_)
skinniside_b = OP_UNARY_(<$x$>(1 if x>0 else -1) if x else 0, **par_mul_)
setattrs = f$>(<$x,y$> DEGEN_( setattr(f,a,b) for a,b in zip(x,y)))**OP_TO_BNARY_
other = (<$x,y$> ASSERT_ ( len (l:= list *x)==2 and y in l) and l[y==l[0]])**OP_TO_BNARY_
split_string = OP_UNARY_(<$x$>[split_string(k,' ') if ' ' in k else k for k in x.split( ARGS_ [0] if  ARGS_  else ' ')], **par_mul_)

# no generators- bad idea?
map = (<$$>(list(map_(* ARGS_ )) if  len ( ARGS_ )>1 else  (<$* ARGS_ ,f= ARGS_ [0]$>list(map_(f,* ARGS_ )))**OP_TO_UNARY_))**OP_TO_BNARY_
zip = (<$$>list(zip_(* ARGS_ ,** KWARGS_ )))**OP_TO_BNARY_
def  x():
    print (1)
    print (2) if  True 
    print (0) if  False 
    L = [0]
    print ((L[0] := '3'), L)
    assert 25== print (( lambda x: x**2)(5))
    assert 25== print ((x $> x**2)(5))
    h = <$x$>x**2
    assert 25== print (h(5))
print (x())

j=(x=2$>x**2)
print (j(2))

k=<$f=(x$>x**2),y=5$> print (f(y*2), ARGS_ , KWARGS_ )
print (k(y=8))

print ((x$>[x+5, ARGS_ [0] [1], KWARGS_ ])(1, "hello", 3, yay="yay"))

m=<$x$>(<$$>list(map(x, ARGS_ [0])))
f=<$$> ARGS_ [0]**2
print (*𝕞(f)([1,2,3]))
print (*[f(x) for x in [1,2,3]])

h=x,y$>x**2+y
print (h(5,1))

y = 5
print ((<$y=y$>$>$>y)(6)()())

print (2 y)
print (1`$2`$3)
print ("a"`$(1 if  False  else 2)`$"b")
print ()
print  map "a"`$ EMPTY_STRING 
print (1`$2| map (<$x,y$>x+y)**OP_TO_BNARY_|3`$4)
print ( list * map (<$x,y$>x+y,1`$2,3`$4))
print (1`$2|( map ((<$x,y$>x+y)**OP_TO_BNARY_>><$x$>x**2)**OP_TO_BNARY_)|3`$4)
print (1`$<$$> True , 0`$1 if 1 else 2`$3)
print ((1`$<$$>2`$3)[1]())

for i in range(10):
    print(i)

for i in  range (10): print (i)

print | map | range (10)