from collections import namedtuple as NT
from functools import reduce, partial
from itertools import accumulate
from enum import Enum
import regex as re

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

SMD, CMD, PRP = staticmethod, classmethod, property

def R(*a,**kw):
    with open(*a,**kw) as f:
        return f.read()
enum = enumerate
HXO = lambda x: hex(ord(x))[2:]
flat = lambda x: reduce(lambda x,y: x+y, l:=ᒪ(x), type(l[0])() if ⵌ(l) else [])
rgx_or = lambda x: f"({ᒍ(')|(', x)})"
reach_first = lambda x: reach_first(x[0]) if ᐹ(x, ᒪ) and ⵌ(x)==1 else x
collapse = lambda x: x if ᐹ(x:=reach_first(x), ᒪ) else [x]
enlist = lambda x: [x]
_V,P=0,partial(PD:=lambda n,*a,**k:exec(f"_V+={n}",globals())or print(' '*(_V-1+(n<0))+'|'+('←→'[n>0]if n else' '),*a,**k),0)

class SCRIPT:
    CHAR_NRM = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZαβγδεζηθϑικλμνξπρςστυφχψω∂ϕΓΔ∇ΘΞΠΣΦΨΩ0123456789:,<>;?!+-/*=()&$%~"""
    CHAR_SUP = """ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮ󰀂ᴰᴱ󰀅ᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾ󰀐ᴿ󰀒ᵀᵁⱽᵂ󰀗󰀘󰀙󰁌󰁍󰁎󰁏󰁐󰁑󰁒󰁓◌󰁔󰁕󰁖󰁗󰁘󰁙󰁛󰁜󰁝󰁞󰁟󰁠󰁡󰁢󰁣󰁤◌◌󰀶󰀷◌󰀻󰁁󰁃󰁅󰁈󰁊󰁋⁰¹²³⁴⁵⁶⁷⁸⁹◌󰁱󰂂󰂁󰁲◌ꜝ⁺⁻ᐟ⁼⁽⁾◌◌◌˜"""
    CHAR_SUB = """ₐₑₕᵢⱼₖₗₘₙ󰂼ₚᵣₛₜᵤᵥₓ󰂓󰂔󰂕󰂖󰂗󰂘󰂙󰂚󰂛󰂜󰂝󰂞󰂟󰂠󰂡󰂢󰂣󰂤󰂥󰂦󰂧󰂨󰂩󰂪󰂫󰂬󰃤󰃥󰃦󰃧󰃨󰃩󰃪󰃫◌󰃬󰃭󰃮󰃯󰃰󰃱󰃳󰃴󰃵󰃶󰃷󰃸󰃹󰃺󰃻󰃼◌◌󰃎󰃏◌󰃓󰃙󰃛󰃝󰃠󰃢󰃣₀₁₂₃₄₅₆₇₈₉﹕󰄎󰄟󰄞󰄏﹖◌₊₋⸝₌₍₎﹠﹩﹪◌"""
    SUP = ᖱ(ζ(CHAR_SUP, CHAR_NRM))
    SUB = ᖱ(ζ(CHAR_SUB, CHAR_NRM))
    sup2nrm = lambda x: ᒍ(ᐦ, ᴍ(SCRIPT.SUP.__getitem__, x))
    sub2nrm = lambda x: ᒍ(ᐦ, ᴍ(SCRIPT.SUB.__getitem__, x))

class Node:
    def __init__(𝕊, t=ᐦ, c=ᗜ):
        𝕊.t, 𝕊.c = t, c or []
    def __repr__(𝕊):
        return 𝕊.t+(f"[{ᒍ(',', ᴍ(ᔐ,𝕊.C))}]" if 𝕊.C else f'"{𝕊.c}"')
    C = PRP(lambda 𝕊: 𝕊.c if ᐹ(𝕊.c, ᒪ) else [])
    txt = PRP(lambda 𝕊: 𝕊.c if ᐹ(𝕊.c, ᔐ) else ᒍ(ᐦ, ᴍ(Node.txt, 𝕊.c)))