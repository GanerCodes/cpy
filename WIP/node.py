from util import *

class Node:
    __slots__ = ('t', 'c')
    
    n = CMD(lambda 𝕋,t,*C: 𝕋(t, [ᐹ(c,ᗜ|𝕋) and c or ᐹ(c,ᔐ) and 𝕋(c=c) or 𝕋.n(*c) for c in C]))
    def __init__(𝕊, t=ᐦ, c=ᗜ):
        assert ᐹ(t, ᔐ) and ᐹ(c, ᗜ|ᔐ|ᒪ)
        𝕊.t, 𝕊.c = t, c or []
    
    def __eq__(𝕊, n):
        if ᐹ(n, ᔐ):
            return 𝕊.t == n
        assert ᐹ(n, Node)
        return 𝕊.t == n.t and 𝕊.c == n.c
    
    def __repr__(𝕊):
        r = 𝕊.t
        if 𝕊.S:
            r += f'["{𝕊.c}"]'
        else:
            r += f"[{ᒍ(',', ᴍ(ᔐ, 𝕊.C))}]"
        return r
   
    def copy(𝕊, t=ᗜ, c=ᗜ, deep=0):
        T = 𝕊.t if t is ᗜ else t
        C = 𝕊.c if c is ᗜ else c
        if ᐹ(C, ᔐ) or not deep:
            return Node(T, C)
        if deep == 1:
            return Node(T, C.copy(deep=deep))
        if deep  > 1:
            return Node(T, ᴍ(partial(type(𝕊).copy, deep=deep), C))
        assert ⴴ
    
    C = PRP(lambda 𝕊: 𝕊.c if ᐹ(𝕊.c, ᒪ) else [])
    S = PRP(lambda 𝕊: ᐹ(𝕊.c, ᔐ))
    text = lambda 𝕊: 𝕊.c if ᐹ(𝕊.c, ᔐ) else ᒍ(ᐦ, ᴍ(Node.text, 𝕊.c))
    txt = PRP(text)
    print = lambda 𝕊,d=100,p=0,m=64,w=64,s=3,N=Z.lR+'∅'+Z.W,F=lambda x,s=Z.P+'_'+Z.W:ᖇ(x,ń,s),D=lambda x,a=Z.G,b=Z.W:a+x+b,X=lambda x,a=Z.bdB,b=Z.bBLA:a+x+b:𝕊.t=="oper" and ((Y:=lambda v:ⵉ(𝕊.C[v].print(d,1)[0][1],ś,1)[-1]) and [(p,D('╴')+f"oper {Y(0)}|{Y(1)}|{Y(2)}")]) or d and (p and [(p,f"{D("╴╮╷"[ᖲ(𝕊.C)*(1+(p<2))])}{𝕊.t or N} {X(F(𝕊.txt[:m]) or N)}{((l:=ⵌ(𝕊.txt))>m) and f"……+{l-w}" or ᐦ}"),*((C:=[c.print(d-1,p+1) for c in 𝕊.C]) and sum([[(a,D("├│╰ "[(i+2>ⵌ(C))*2+ᖲ(o)]+"─ "[o>0]*(s-1))+d) for o,(a,d) in enum(v)] for i,v in enum(C)],[]))] or print(*(x[1] for x in 𝕊.print(d,1)),sep=ń)) or [(p,𝕊.t+'.'*3)]

NULL = Node("NULL")
Ń = Node.n