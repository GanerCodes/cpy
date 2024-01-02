from traceback_with_variables import activate_by_import

from collections import namedtuple as NT
from functools import reduce, partial
from itertools import accumulate, pairwise
from more_itertools import windowed, split_at, mark_ends, peekable
import colored
import regex as re
from enum import Enum

# poorman's cpy
print = lambda *a,__print=print,**k: __print(*a,**k) or a and a[0]
(ń,ś),ᐦ = '\n ', ''
ⴳ, ⴴ, ᗜ = True, False, None
ᖲ, ᖱ, ᒪ = bool, dict, list
ᔐ, ᒍ, ᖇ, ⵉ, ⵐ = str, str.join, str.replace, str.split, str.strip
ⵌ, ⵗ = len, range
ᴍ, ζ = lambda*a,**k:[*map(*a,**k)], lambda*a,**k:[*zip(*a,**k)]
ᖵ    = lambda*a,**k:[*filter(*a,**k)]
Т, ᐹ = type, isinstance
ⴷ, ⴸ = all, any
ᴍᴍ = lambda n,f,l: ᴍ(f,l) if n<=1 else [ᴍᴍ(n-1,f,c) for c in l]
ε = lambda x: [x] if x else []
SMD, CMD, PRP = staticmethod, classmethod, property

def J́(L, s, l=ⴴ, r=ⴴ):
    if ⵌ(L) == 0: return [s]*ᖲ(l or r)
    if ⵌ(L) == 1: return [s]*ᖲ(l)+L+[s]*ᖲ(r)
    r, e = [s] if l else [], (L := L.copy()).pop()
    while L:
        r += [L.pop(0), s]
    r.append(e)
    if r:
        r.append(s)
    return r

enum = enumerate
R = lambda *a,**k:open(*a,**k).read()
HXO = lambda x: hex(ord(x))[2:].zfill(4)
flat = lambda x: reduce(lambda x,y: x+y, l:=ᒪ(x), type(l[0])() if ⵌ(l) else [])
rgx_or = lambda x: f"({ᒍ(')|(', ᴍ(re.escape, x))})"
spl_H = lambda s,H: ᖱ(windowed(ᴍ(ⵐ,re.split(H,s)[1:]),2,step=2))
reach_first = lambda x: reach_first(x[0]) if ᐹ(x, ᒪ) and ⵌ(x)==1 else x
collapse = lambda x: x if ᐹ(x:=reach_first(x), ᒪ) else [x]
enlist = lambda x: [x]
_V,P=0,partial(PD:=lambda n,*a,**k:exec(f"_V+={n}",globals())or print(' '*(_V-1+(n<0))+'|'+('←→'[n>0]if n else' '),*a,**k),0)

class Z:
    s=[colored.Fore.WHITE+colored.Back.BLACK]
    def __getattr__(𝕊, a):
        if a == 'p':
            Z.s.pop()
        else:
            if a[0] == 'b': m, a = colored.Back, a[1:]
            else: m = colored.Fore
            if   a[0] == 'd': a =  "DARK_" + a[1:]
            elif a[0] == 'l': a = "LIGHT_" + a[1:]
            Z.s += [getattr(m,
                min(filter(lambda x: x.startswith(a), dir(m)), key=ⵌ))]
        return Z.s[-1]
Z=Z()

class SCRIPT:
    CHAR_NRM = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZαβγδεζηθϑικλμνξπρςστυφχψω∂ϕΓΔ∇ΘΞΠΣΦΨΩ0123456789:,<>;?!+-/*=()&$%~"""
    CHAR_SUP = """ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮ󰀂ᴰᴱ󰀅ᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾ󰀐ᴿ󰀒ᵀᵁⱽᵂ󰀗󰀘󰀙󰁌󰁍󰁎󰁏󰁐󰁑󰁒󰁓◌󰁔󰁕󰁖󰁗󰁘󰁙󰁛󰁜󰁝󰁞󰁟󰁠󰁡󰁢󰁣󰁤◌◌󰀶󰀷◌󰀻󰁁󰁃󰁅󰁈󰁊󰁋⁰¹²³⁴⁵⁶⁷⁸⁹◌󰁱󰂂󰂁󰁲◌ꜝ⁺⁻ᐟ⁼⁽⁾◌◌◌˜"""
    CHAR_SUB = """ₐₑₕᵢⱼₖₗₘₙ󰂼ₚᵣₛₜᵤᵥₓ󰂓󰂔󰂕󰂖󰂗󰂘󰂙󰂚󰂛󰂜󰂝󰂞󰂟󰂠󰂡󰂢󰂣󰂤󰂥󰂦󰂧󰂨󰂩󰂪󰂫󰂬󰃤󰃥󰃦󰃧󰃨󰃩󰃪󰃫◌󰃬󰃭󰃮󰃯󰃰󰃱󰃳󰃴󰃵󰃶󰃷󰃸󰃹󰃺󰃻󰃼◌◌󰃎󰃏◌󰃓󰃙󰃛󰃝󰃠󰃢󰃣₀₁₂₃₄₅₆₇₈₉﹕󰄎󰄟󰄞󰄏﹖◌₊₋⸝₌₍₎﹠﹩﹪◌"""
    SUP = ᖱ(ζ(CHAR_SUP, CHAR_NRM))
    SUB = ᖱ(ζ(CHAR_SUB, CHAR_NRM))
    sup2nrm = lambda x: ᒍ(ᐦ, ᴍ(SCRIPT.SUP.__getitem__, x))
    sub2nrm = lambda x: ᒍ(ᐦ, ᴍ(SCRIPT.SUB.__getitem__, x))