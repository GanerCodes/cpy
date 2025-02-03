import sys
from pathlib import Path
_insp = lambda x: x in sys.path or sys.path.insert(0, x)
_insp(str(moon_dir := Path(__file__).absolute().parent))
_insp(str(moon_dir / "compiler"))
from hashlib import sha256 as _sha256 ; sha256 = lambda s: _sha256(s.encode("utf-8")).hexdigest()
from unicodedata import is_normalized, name
from time import time, sleep
from sys import setrecursionlimit
from collections import namedtuple as NT
from functools import reduce, partial as ρ
from itertools import accumulate, pairwise, starmap, chain, filterfalse, groupby
from string import ascii_lowercase, ascii_uppercase, digits
from uuid import uuid4
from pickle import loads, dumps
import textwrap as TW
import os, traceback
try             : import regex as re
except Exception: import re
exit_ = exit

setrecursionlimit(1_000_000)

# poorman's ☾
wrg = lambda F:lambda*a,**k:[*F(*a,**k)]
print = lambda *a,__print=print,**k:__print(*a,**k) or a and a[0]
print_ex = lambda e: print(''.join(traceback.format_exception(type(e), e, e.__traceback__)), end='')
ⴳ, ⴴ, ᗜ, ᐦ, (ń,ś) = True, False, None, '', '\n '
ᖲ, ᖱ, ᒪ = bool, dict, list
ᔐ, ᒍ, ᖇ, ⵉ, ⵐ = str, str.join, str.replace, str.split, str.strip
Т, ᐹ, ⵌ, ⴷ, ⴸ = type, isinstance, len, all, any
ᴍ, ꟿ, ᴍᴍ = wrg(map), wrg(starmap), lambda n,f,l: ᴍ(f,l) if n<2 else [ᴍᴍ(n-1,f,c) for c in l]
ᖵ, ζ = wrg(filter), wrg(zip)
SMD, CMD, PRP = staticmethod, classmethod, property
enum = enumerate
R = lambda p  ,m="r" :(((f:=open(p,m)). read( )   )   , f.close())[0]
W = lambda p,c,m="w+":(((f:=open(p,m)).write(c), c)[1], f.close())[0]
ID = lambda x: x
ZIL = lambda *a,**k: None
HXO = lambda x: hex(ord(x))[2:].zfill(4)
wrap = lambda x,w=120,q='\t': ᒍ(ń, TW.wrap(x, width=w, subsequent_indent=q))
rgx_or = lambda x: f"({ᒍ(")|(", ᴍ(re.escape, x))})"
prettify_code = lambda g: ᒍ(ń, (f"{ᔐ(i+1).zfill(4)}\t{wrap(v, q='\t  ')}" for i,v in enum(ⵉ(g, ń))))
_V,P=0,ρ(PD:=lambda n,*a,**k:exec(f"_V+={n}",globals())or print(ś*(_V-1+(n<0))+'|'+('←→'[n>0]if n else ś),*a,**k),0)
def RAISE(ε): raise ε

class peekable(ᒪ):
    __init__ = lambda 𝕊,*𝔸,**𝕂: super().__init__(*𝔸,**𝕂)
    __next__ = lambda 𝕊: 𝕊.pop(0)
    peek = lambda 𝕊: 𝕊[0]

def split_at(𝚇, 𝑓, 𝚔=ⴴ):
    r,v = [],0
    for i,x in enum(𝚇):
        if not 𝑓(x): continue
        r.append(𝚇[v:i])
        v = i+1
        if 𝚔:
            r.append([x])
    r.append(𝚇[v:])
    return r

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

class hashDict(ᖱ): __hash__ = lambda 𝕊:hash(frozenset(𝕊.items()))
class Bunch(ᖱ): __getattr__ = lambda 𝕊, x: 𝕊[x]

def J́(L, s, l=ⴴ, r=ⴴ, E=ⴳ):
    L = [*L]
    if ⵌ(L) == 0: return [s]*ᖲ(E and (l or r))
    if ⵌ(L) == 1: return [s]*ᖲ(l)+L+[s]*ᖲ(r)
    R, e = [s] if l else [], (L := L.copy()).pop()
    while L: R += [L.pop(0), s]
    R.append(e)
    if r: R.append(s)
    return R

TERM_RESET = '\x1b[0m'
def termclr(t, fg=ᗜ, bg=ᗜ, rst=ⴳ): # 🌈.☾
    R = ᐦ
    for c, n in zip((fg, bg), (38, 48)):
        if c is ᗜ: continue
        r, g, b = c
        R += f'\x1b[{n};2;{r};{g};{b}m'
    return R + str(t) + TERM_RESET * bool(rst)

class Z:
    __slots__ = ()
    s = [termclr(ᐦ, (255,)*3, (0,)*3)]
    clrs = { k:tuple(v.to_bytes(3)) for k,v in {
                "w"  : 0xFFFFFF, "wh" : 0xFFFFFF,
                "b"  : 0x0000FF, "bl" : 0x0000FF,
                "bla": 0x000000, "gre": 0x00FF00,
                "g"  : 0xAAAAAA, "r"  : 0xFF0000,
                "red": 0xFF0000, "yel": 0xFFFF00,
                "pu" : 0xFF00FF, "p"  : 0xFF8888  }.items() }
    def __getattr__(𝕊, a):
        if a == 'p':
            Z.s.pop()
        else:
            if   a[0] == 'b': m, a = 'B', a[1:]
            else            : m = 'F'
            
            if   a[0] == 'd': t, a = 0.5, a[1:]
            elif a[0] == 'l': t, a = 2.0, a[1:]
            else            : t = 1
            c = tuple(min(int(x*t),255) for x in Z.clrs[a.lower()])
            Z.s.append(termclr(ᐦ, c, ᗜ, rst=ⴴ) if m=='F' else termclr(ᐦ, ᗜ, c, rst=ⴴ))
        return Z.s[-1]
Z=Z()

# 󰤱 make these work under sub/sup

FRAC_CONV = ᖱ(zip("12 13 14 15 16 17 18 19 110 23 25 27 29 34 35 37 38 310 45 47 49 56 57 58 59 67 78 79 710 89 910 03 1100".split(' '),"½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖󷶲󷶷¾⅗󷶳⅜󷷆⅘󷶴󷷂⅚󷶵⅝󷶹󷶶⅞󷶺󷷇󷶻󷷈↉󷷉"))
def TOFRAC(x): # 󰤱 allow seperation by /÷ w/ whitespaces? and finding in middle?
    return FRAC_CONV.get(x, x)
class UPSIDEDOWNSYNDROME:
    NRM = "0123456789abcdefoxABCDEFOXîĵ󷺈ℇτπ󷺍󷺏∞"
    USD = "󷰽󷰾󷰿󷱀󷱁󷱂󷱃󷱄󷱅󷱆󷱇󷱈󷱉󷱊󷱋󷱌󷱍󷱎󷱏󷱐󷱑󷱒󷱓󷱔󷱕󷱖󷱪󷱽󷱾󷱫󷱬󷱭󷱮󷱰󷱩"
    MAP = dict(zip(NRM, USD)) | dict(zip(USD, NRM))
    flip = lambda s, MAP=MAP: str.join(ᐦ, (MAP.get(c, c) for c in s))
class SCRIPT:
    SCRIPT_FILE_LOC = moon_dir / "FontCompose/.SCRIPT_MAP"
    with open(SCRIPT_FILE_LOC) as f:
        CHAR_NRM,CHAR_SUP,CHAR_SUB = f.read().strip().split(ń)
    SUP = ᔐ.maketrans(CHAR_NRM, CHAR_SUP)
    SUB = ᔐ.maketrans(CHAR_NRM, CHAR_SUB)
    NRM = ᔐ.maketrans(CHAR_SUP+CHAR_SUB, CHAR_NRM*2)
    sup,sub,nrm = (lambda s, T=T: s.translate(T) for T in (SUP,SUB,NRM))

def parse_sysargs(𝐴, **𝕂):
    𝐴, alias = 𝐴.copy(), {}
    𝕂 = ᖱ([ᖇ(y,*"-_") if ᐹ(y,ᔐ) else y for y in x] for x in 𝕂.items())
    for k, v in [*𝕂.items()]:
        if ᐹ(v, ᔐ) and v:
            del 𝕂[k]
            alias[k] =v
    while 𝐴:
        if not (T := 𝐴[0]).startswith("-"):
            if T == "/": 𝐴.pop(0)
            break
        t, *E = ⵉ(T[1:], '=', 1)
        if not t.startswith("-"):
            𝐴[0:1] = [f"--{x}{E and '='+E[0] or ᐦ}" for x in t]
            continue
        t = ᖇ(alias.get(*(ᖇ(t[1:],*"-_"),)*2),*"-_")
        e = E and ⵉ(E[0], ',')
        assert t in 𝕂, f'Unknown argument, "{t}"'
        if ᐹ(v := 𝕂[t], tuple): v, _ = v
        
        if   ᐹ(v, ᒪ):
            assert e, f'Need at least one value for "{t}"'
            𝕂[t] = [*v, *e]
        elif ᐹ(v, ᔐ):
            assert ⵌ(e)==1, f'Exactly 1 value accepted for "{t}"'
            assert not v, f'Duplicate entry for "{t}"'
            𝕂[t] = e[0]
        elif ᐹ(v, int):
            assert ⵌ(e) <= 1, f'0 or 1 values accepted for "{t}"'
            𝕂[t] = v + int(e[0] if e else 1)
        else:
            assert ⴴ
        𝐴.pop(0)
    return 𝐴, Bunch({k: v[1] if ᐹ(v, tuple) else v for k,v in 𝕂.items()})

def time_test(𝑓, *𝔸, **𝕂):
    t0 = time()
    return 𝑓(*𝔸, **𝕂), time() - t0
DEBUG_NS = { "mk": lambda x:lambda *𝔸,**𝕂:DEBUG_NS[x](*𝔸,**𝕂),
             "BP": ZIL, "togprof": ZIL }
BP = DEBUG_NS["mk"]("BP")
togprof = DEBUG_NS["mk"]("togprof")
DEBUG = ⴴ
def ENABLE_DEBUG():
    global __proft, lnprof
    import resource, threading, cProfile, pstats, atexit, io
    from inspect import getouterframes, currentframe
    __proft = ⴴ
    try:
        import line_profiler
        lnprof  = line_profiler.LineProfiler()
        atexit.register(lnprof.print_stats)
    except Exception:
        print("Unable to load line_profiler.")
    
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

from file_cacher import FileCacher