from sys import path as __PATH; __PATH.insert(0, '/home/ganer/Projects/cpy/imports') ; del __PATH ; from CPY_HEADER import * # CPY-a-2023/11/24_13:45:31 
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
assert (1`$2| map (<$x,y$>x+y)**OP_TO_BNARY_|3`$4)==[4,6]
assert ( map (<$x,y$>x+y,1`$2,3`$4))==[4,6]
assert (1`$<$$> True , 0`$1 if 1 else 2`$3)[0] [1]()== True 
assert ((1`$<$$>2`$3)[1]())==[2,3]
assert (<$x$>x+2)| map | range (3)==2`$3`$4
assert 'ab'|other|"a"=="b"
assert 5**isinstance**int
assert 1**range_binary**4==range(1,4)
assert "a"|(<$x,y$>x+y)**OP_TO_BNARY_|"b" == 'ab'
assert ( magic_list "abcdefghijkmno"+['12345'])[14] [3] == "4"
assert 'abcdef'[y] == "f"
assert  "a" 2 3 == 6 "a"
assert  1 2 3 4 5 == 120
assert  (3)2 == 6 
assert  magic_list "ab"2  zip     0**range_binary**4   == ("a",0)`$("b",1)`$("a",2)`$("b",3)
assert  magic_list "ab"2 | zip | magic_list  0**range_binary**2 2 == ("a",0)`$("b",1)`$("a",0)`$("b",1) \
== magic_list "ab"2  zip   magic_list *0**range_binary**2*2

assert  "swag" == "swag"
assert  "x[0]" == "x[0]"

print *"Passed!"