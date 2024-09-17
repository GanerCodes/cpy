import sys
from pathlib import Path
_insp = lambda x: x in sys.path or sys.path.insert(0, x)
_insp(cpy_dir := str(Path(__file__).absolute().parent))
_insp(cpy_dir+"/compiler")

from hashlib import sha256 as _sha256 ; sha256 = lambda s: _sha256(s.encode("utf-8")).hexdigest()
from time import time, sleep
from sys import setrecursionlimit
from collections import namedtuple as NT
from functools import reduce, partial as ρ
from itertools import accumulate, pairwise, starmap, \
                      chain, filterfalse, groupby
from more_itertools import *
from pickle import loads, dumps
import textwrap as TW
import os, re, colored
exit_ = exit

setrecursionlimit(1_000_000)

# poorman's cpy
wrg = lambda F: lambda*a,**k:[*F(*a,**k)]
print = lambda *a,__print=print,**k:__print(*a,**k) or a and a[0]
(ń,ś),ᐦ = '\n ', ''
ⴳ, ⴴ, ᗜ = True, False, None
ᖲ, ᖱ, ᒪ = bool, dict, list
ᔐ, ᒍ, ᖇ, ⵉ, ⵐ = str, str.join, str.replace, str.split, str.strip
ᖵ, ᖶ, ζ = wrg(filter), wrg(filterfalse), wrg(zip)
ⵌ, ⵗ = len, range
Т, ᐹ = type, isinstance
ⴷ, ⴸ = all, any
ᴍ, ᴍs, ᴍᴍ = wrg(map), wrg(starmap), lambda n,f,l: ᴍ(f,l) if n<2 else [ᴍᴍ(n-1,f,c) for c in l]
ε = lambda x, y=ᗜ: [x if y is None else y] if x else []
δ = lambda x: [] if x is None else [x]
SMD, CMD, PRP = staticmethod, classmethod, property
FS = frozenset
enum = enumerate
R = lambda p  ,m="r" :(((f:=open(p,m)). read( )   )   , f.close())[0]
W = lambda p,c,m="w+":(((f:=open(p,m)).write(c), c)[1], f.close())[0]
ID = lambda x: x
ZIL = lambda *a,**k: None
HXO = lambda x: hex(ord(x))[2:].zfill(4)
flat = lambda x: reduce(lambda x,y: x+y, l:=ᒪ(x), Т(l[0])() if ⵌ(l) else [])
wrap = lambda x,w=120,q='\t': ᒍ(ń, TW.wrap(x, width=w, subsequent_indent=q))
rgx_or = lambda x: f"({ᒍ(")|(", ᴍ(re.escape, x))})"
spl_H = lambda s,H: ᖱ(windowed(ᴍ(ⵐ,re.split(H,s)[1:]),2,step=2))
reach_first = lambda x: reach_first(x[0]) if ᐹ(x, ᒪ) and ⵌ(x)==1 else x
collapse = lambda x: x if ᐹ(x:=reach_first(x), ᒪ) else [x]
enlist = lambda x: [x]
prettify_code = lambda g: ᒍ(ń, (f"{ᔐ(i+1).zfill(4)}\t{wrap(v, q='\t  ')}" for i,v in enum(ⵉ(g, ń))))
_V,P=0,ρ(PD:=lambda n,*a,**k:exec(f"_V+={n}",globals())or print(ś*(_V-1+(n<0))+'|'+('←→'[n>0]if n else ś),*a,**k),0)

def time_test(𝑓, *𝔸, **𝕂):
    t0 = time()
    return 𝑓(*𝔸, **𝕂), time() - t0

class hashDict(dict):
    __hash__ = lambda 𝕊:hash(frozenset(𝕊.items()))

def part(l, f):
    l, a = l.copy(), []
    while l:
        if f(v := l.pop(0)):
            return a, v, l
        a.append(v)
    assert False

class Holder:
    __slots__ = "A","K"
    def __init__(𝕊,*a,**k):𝕊.A=𝕊.K='∅'
    def s(𝕊,*a,**k):𝕊.A,𝕊.K=a,k;return 𝕊
    __iter__=lambda 𝕊:iter((𝕊.A,𝕊.K))
    __repr__=lambda 𝕊:f"Holder: {𝕊.A=} {𝕊.K=}"

def J́(L, s, l=ⴴ, r=ⴴ, E=ⴳ):
    L = ᒪ(L)
    if ⵌ(L) == 0: return [s]*ᖲ(E and (l or r))
    if ⵌ(L) == 1: return [s]*ᖲ(l)+L+[s]*ᖲ(r)
    R, e = [s] if l else [], (L := L.copy()).pop()
    while L:
        R += [L.pop(0), s]
    R.append(e)
    if r: R.append(s)
    return R

def map_groups(l, F, M, I=ID, O=ID):
    t = []
    for k in l:
        if F(k):
            t.append(I(k))
            continue
        if t:
            yield M(t)
            t = []
        yield O(k)
    if t:
        yield M(t)

class Z:
    s = [colored.Fore.WHITE+colored.Back.BLACK]
    d_b, d_f = colored.Back.__dict__, colored.Fore.__dict__
    def __getattr__(𝕊, a):
        if a == 'p':
            Z.s.pop()
        else:
            if a[0] == 'b': m, a = Z.d_b, a[1:]
            else: m = Z.d_f
            if   a[0] == 'd': a =  "DARK_" + a[1:]
            elif a[0] == 'l': a = "LIGHT_" + a[1:]
            Z.s.append(m[min(ᖵ(lambda x: x.startswith(a), m), key=ⵌ)])
        return Z.s[-1]
Z=Z()

class SCRIPT:
    SCRIPT_FILE_LOC = f"{cpy_dir}/FontCompose/.SCRIPT_MAP"
    SUP, SUB, NRM = {}, {}, {}
    with open(SCRIPT_FILE_LOC) as f:
        CH = CHAR_NRM, CHAR_SUP, CHAR_SUB = \
               f.read().strip().split('\n')
    for n,p,b in zip(*CH):
        SUP[n], SUB[n] = p, b
        NRM[b] = NRM[p] = n
    sup = lambda s, SUP=SUP: str.join(ᐦ, (SUP.get(c, c) for c in s))
    sub = lambda s, SUB=SUB: str.join(ᐦ, (SUB.get(c, c) for c in s))
    nrm = lambda s, NRM=NRM: str.join(ᐦ, (NRM.get(c, c) for c in s))

# class SCRIPT:
#     CHAR_NRM = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZαβγδεζηθϑικλμνξπρςστυφχψω∂ϕΓΔ∇ΘΞΠΣΦΨΩ0123456789:,<>;?!+-/*=(){}[]&$%~𐞑∞"""
#     CHAR_SUP = """ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮ󰀂ᴰᴱ󰀅ᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾ󰀐ᴿ󰀒ᵀᵁⱽᵂ󰀗󰀘󰀙󰁌󰁍󰁎󰁏󰁐󰁑󰁒󰁓◌󰁔󰁕󰁖󰁗󰁘󰁙󰁛󰁜󰁝󰁞󰁟󰁠󰁡󰁢󰁣󰁤◌◌󰀶󰀷◌󰀻󰁁󰁃󰁅󰁈󰁊󰁋⁰¹²³⁴⁵⁶⁷⁸⁹◌󰁱󰂂󰂁󰁲◌ꜝ⁺⁻ᐟ⁼⁽⁾󰁸󰁹󰁺󰁻◌◌◌˜𐞑󰂃"""
#     CHAR_SUB = """ₐₑₕᵢⱼₖₗₘₙ󰂼ₚᵣₛₜᵤᵥₓ󰂓󰂔󰂕󰂖󰂗󰂘󰂙󰂚󰂛󰂜󰂝󰂞󰂟󰂠󰂡󰂢󰂣󰂤󰂥󰂦󰂧󰂨󰂩󰂪󰂫󰂬󰃤󰃥󰃦󰃧󰃨󰃩󰃪󰃫◌󰃬󰃭󰃮󰃯󰃰󰃱󰃳󰃴󰃵󰃶󰃷󰃸󰃹󰃺󰃻󰃼◌◌󰃎󰃏◌󰃓󰃙󰃛󰃝󰃠󰃢󰃣₀₁₂₃₄₅₆₇₈₉﹕󰄎󰄟󰄞󰄏﹖◌₊₋⸝₌₍₎󰄕󰄖󰄗󰄘﹠﹩﹪◌◌"""
#     SUP = ᖱ(ζ(CHAR_SUP, CHAR_NRM))
#     SUB = ᖱ(ζ(CHAR_SUB, CHAR_NRM))
#     NRM = SUP | SUB
#     nrm = lambda x: ᒍ(ᐦ, ᴍ(SCRIPT.NRM.__getitem__, x))

DEBUG_NS = { "mk": lambda x:lambda *𝔸,**𝕂:DEBUG_NS[x](*𝔸,**𝕂),
             "BP": ZIL, "togprof": ZIL }
BP = DEBUG_NS["mk"]("BP")
togprof = DEBUG_NS["mk"]("togprof")
DEBUG = ⴴ
def ENABLE_DEBUG():
    global __proft, lnprof
    import resource, threading, line_profiler, cProfile, pstats, atexit, io
    from inspect import getouterframes, currentframe
    lnprof, __proft = line_profiler.LineProfiler(), ⴴ
    atexit.register(lnprof.print_stats)
    def BP(*a):
        for i, x in enum(a):
            print(f"{Z.r}BP{Z.w} - {Z.g}{i}{Z.w}:\t{wrap(ᔐ(x),q='\t')}")
        print()
        breakpoint()
        if a: return a[0]
    def togprof(bp=ⴴ):
        global __proft
        if __proft:
            __proft.disable()
            s = io.StringIO()
            ps = pstats.Stats(__proft, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
            ps.print_stats()
            print(s.getvalue())
            __proft = ⴴ
            return bp and BP()
        (__proft := cProfile.Profile()).enable()
    DEBUG_NS["BP"], DEBUG_NS["togprof"] = BP, togprof