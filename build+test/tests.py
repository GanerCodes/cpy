from sys import path as __PATH; __PATH.insert(0, '/home/ganer/Projects/cpy/imports') ; del __PATH ; from CPY_HEADER import * # CPY-a-2023/11/26_02:03:36 
def  x():
    assert (2 if  True )==2
    assert (0 if  False )== None 
    assert [((L:=[0])[0]:='3'), L]=="3"`$["3"]
    assert L[0]=='3'
    assert 25==(( lambda x: x**2)(5))
    assert 25==((x$>x**2)(5))
    assert 25==((h:=<$x$>x**2)(5))
x()

assert [j for _ in (j:="hi")]=="hi"`$"hi"
assert ((lambda x,i=-1: [(i := i+1) for x in range(5)])(1))== magic_list *0**range_binary**5

j=(x=2$>x**2)
assert j()==4
assert j(3)==9

k=<$f=(x$>x**2),y=5$>(f(y*2), ARGS_ , KWARGS_ )[0]
assert (k(y=8))==256
assert ((x$>[x+5, ARGS_ [0] [1], KWARGS_ ])(1, "hello", 3, yay="yay"))==6`$"e"`${'yay':'yay'}





y = 5
assert ((<$y=y$>$>$>y)(6)()())==6
assert  MATH_TAU **2== MATH_TAU **2 
assert (1,"a")[0]==1
assert (2 y)==10
assert (1`$2`$3)[1]==2
assert ("a"`$(1 if  False else 2)`$"b")==["a",2,"b"]
assert ((<$x$>x) map  "a"`$ EMPTY_STRING )==['a','']
assert (1`$2| map (<$x,y$>x+y) **OP_TO_BNARY_ |3`$4)==[4,6]
assert ( map (<$x,y$>x+y,1`$2,3`$4))==[4,6]
assert (1`$<$$> True , 0`$1 if 1 else 2`$3)[0] [1]()== True 
assert ((1`$<$$>2`$3)[1]())==[2,3]
assert (<$x$>x+2)| map | range (3)==2`$3`$4
assert 'ab'|other|"a"=="b"
assert 5**isinstance**int
assert 1**range_binary**4==range(1,4)
assert "a"|(<$x,y$>x+y) **OP_TO_BNARY_ |"b" == 'ab'
assert ( magic_list "abcdefghijkmno"+['12345'])[14] [3] == "4"
assert 'abcdef'[y] == "f"
assert  "a" 2 3 == 6 "a"
assert  1 2 3 4 5 == 120
assert  (3)2 == 6 
assert  (<$x$>x**2) map  2`$5 == 4`$25
assert  magic_list "ab"2  zip     0**range_binary**4   == ("a",0)`$("b",1)`$("a",2)`$("b",3)
assert  magic_list "ab"2 | zip | magic_list  0**range_binary**2 2 == ("a",0)`$("b",1)`$("a",0)`$("b",1) \
== magic_list "ab"2  zip   magic_list *0**range_binary**2*2

swag1 = <$F,n$><$x$>(<$x,y$>(<$x,y$>y **OP_TO_UNARY_ x) FOLD_ |x enlist + REVERSE_ F) FOLD_ |x enlist +0 enlist n
swag2 = <$F,n$><$x$>(<$x,y$>F[-(y+1)% len **F] **OP_TO_UNARY_ x) FOLD_ |x enlist + len F range magic_list n
swag3 = <$F,n$><$x$>(<$x,y$>F[-(y+1)%k] **OP_TO_UNARY_ x) FOLD_ |x enlist +(k:= len F) range magic_list n
A=swag1([<$x$>"A"+x, <$x$>"B"+x], 3)( EMPTY_STRING )
B=swag2([<$x$>"A"+x, <$x$>"B"+x], 3)( EMPTY_STRING )
C=swag2([<$x$>"A"+x, <$x$>"B"+x], 3)( EMPTY_STRING )
assert A==B==C=="ABABAB"
# [&$%]
assert  "swag" == "swag"
assert  "x[0]" == "x[0]"

print *"Passed!"
