TRY_SURROUND_SPACE = \
    "𝕋/True 𝔽/False ⤉/max ⤈/min ⋀/all ⋁/any " \
    "Σ/sum Π/prod Ω/class " \
    "☾/print 🃌/len ⨳/ASSERT_ ᴍ/map ⚇/list ζ/zip " \
    "↕/range ↨/enumerate 🜌/setattrs ⍟/DEGEN_ " \
    "⇧/skinniside_z ⇳/skinniside_b ⍭/split_string " \
    "π/MATH_PI τ/MATH_TAU î/COMPLEX_UNIT " \
    "∅/set() □/None ᐦ/EMPTY_STRING ∧/and ∨/or ∈/in ∉/not in " \
    "¬/not λ/lambda ⁅/DEGEN_( ⮌/from ⨡/import " \
    "␡/del ¿/if ¡/else ⸘/elif ∀/for 𝔸/ARGS_ 𝕂/KWARGS_ " \
    "ℂ/SPECIAL_CLASS_ 𝕊/SPECIAL_SELF_ 🢖/SPECIAL_SELF_. ℵ/Namespace"

STANDARD = \
    "⁆/) ≔/:= ≤/<= ≥/>= ≡/== ≠/!= ¯/- ⋄/`$ " \
    "⥌/<$ ↦/$> ⑴/<$x$> ⑵/<$x,y$> ⑶/<$x,y,z$> " \
    "↪/return  ⊢/def  »/assert  ↺/continue  ⇥/break  ≟/case  ⎊/match  " \
    "…/**range_binary** ≾/**isinstance** ⩫/|other| " \
    "ₓ/.x  ᵧ/.y "

import sys, re

dict_replace = lambda d, s: re.compile(
    f"({'|'.join(map(re.escape, d.keys()))})") \
        .sub(lambda m: d[m.string[m.start():m.end()]], s) 

REPS = {}
for t in TRY_SURROUND_SPACE.split(' '):
    f, r = t.split('/', 1)
    REPS['\n'+f] = '\n'+r+' '
    REPS[' '+f] = ' '+r+' '
    REPS[f] = ' '+r+' '
for t in STANDARD.split(' '):
    f, r = t.split('/', 1)
    REPS[f] = r
sys.stdout.write(dict_replace(REPS, '\n'+sys.stdin.read()))