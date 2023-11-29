⮌ operator ⨡ add as add_
⮌ builtins ⨡ print as print_, map as map_, zip as zip_
⮌ functools ⨡ reduce
⮌ itertools ⨡ product as product_
⮌ copy ⨡ deepcopy as dcp

ₛ E ␉ 𝐎𝐔 ␉ OP_UNARY_
ₛ E ␉ 𝐎𝐁 ␉ OP_BNARY_
ₛ E ␉ 𝕸 ␉ par_or_|par_pow_|par_mul_

Ω OP_:
    ⊢ __new__(ℂ,f,d=□,⠶𝕂):
        C = type("OP", (ℂ, ), {})
        ⁅setattr(C, m, (⥌𝕊,o,k=k↦𝕊.check(k,o))) ∀m,k∈𝕂.items()⁆
        C.__call__ = staticmethod(f)
        o = super().__new__(C)
        oᶠ, oᵈ, oᵏʷ = f, d∨{}, 𝕂
        ↪o
    check = 𝕊,k,v ↦ ⨳(k∉𝕊ᵈ)∧type(𝕊)(𝕊ᶠ, {k:v}|𝕊ᵈ, ⠶𝕊ᵏʷ)
Ω 𝐎𝐔(OP_):
    ⊢ check(𝕊, k, v):
        d = (𝕊 ≔ super().check(k,v))ᵈ
        ↪ 𝕊ᶠ(d[v]) ¿(v≔l❟)∈d∨(v≔r❟)∈d¡ 𝕊
Ω 𝐎𝐁(OP_):
    ⊢ check(𝕊, k, v):
        d = (𝕊 ≔ super().check(k,v))ᵈ
        ↪ 𝕊ᶠ(d[l❟],d[r❟]) ¿l❟∈d∧r❟∈d¡ 𝕊

par_or_  = dict( __ror__=l❟,  __or__=r❟)
par_pow_ = dict(__rpow__=l❟, __pow__=r❟)
par_mul_ = dict(__rmul__=l❟, __mul__=r❟)
par_add_ = dict(__radd__=l❟, __add__=r❟)
OP_TO_UNARY_ = 𝐎𝐔(f↦𝐎𝐔(f, ⠶par_or_, ⠶par_mul_), __rpow__=l❟)
OP_TO_BNARY_ = 𝐎𝐔(f↦𝐎𝐁(f, ⠶par_or_, ⠶par_mul_), __rpow__=l❟)
range_binary = 𝐎𝐁(range, ⠶par_pow_)
skinniside_z = 𝐎𝐔(①1¿x>0¡0, ⠶par_mul_)
skinniside_b = 𝐎𝐔(①(1¿x>0¡¯1)¿x¡0, ⠶par_mul_)
setattrs = f↦(②⁅setattr(f,a,b)∀a,b∈zip(x,y)⁆)𐞁
other = (②⨳(🃌(l≔⚇⨯x)≡2∧y∈l)∧l[y≡l₀])𐞁
split_string = 𝐎𝐔(①[split_string(k, ❟)¿ ❟∈k¡k ∀k∈x.split(𝔸₀¿𝔸¡ ❟)], ⠶par_mul_)


◄, ► = 𝐎𝐁(②x, ⠶𝕸), 𝐎𝐁(②y, ⠶𝕸)
⤉, ⤈ = max𐞁, min𐞁
󷹄 = (⥌*𝔸,f=(③min(max(z,x),y))↦ (𝚲f(⠤𝔸,a₀))𐞁 ¿🃌(a≔𝔸)≡1¡ (①f(⠤a,x))𐞂 ¿🃌𝔸≡2¡ f(⠤𝔸))𐞁
⋀ = all𐞁
⋁ = any𐞁
∪ = (𝚲set.union(⠤map_(set,𝔸)))𐞁
∩ = (𝚲set.intersection(⠤map_(set,𝔸)))𐞁
∖ = (𝚲set.__sub__(⠤map_(set,𝔸)))𐞁
⨉ = (𝚲list(product_(⠤𝔸)))𐞁
⍉ = (𝚲list(ζ(⠤𝔸₀,⠶𝕂)))𐞂
ζ = (𝚲list(map(list,zip_(⠤𝔸,⠶𝕂))))𐞁
ᴙ = 𝐎𝐔(①x﹕﹕₋₁, ⠶par_mul_|par_pow_)
ᴍ = (𝚲(list(map_(⠤𝔸)) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦list(map_(f,⠤𝔸)))𐞂))𐞁
ſ = (𝚲(reduce(⠤𝔸) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦reduce(f,⠤𝔸))𐞂))𐞁
Σ = (x↦reduce(add_,(x≔list(x)),⠤([𝔸₀¿𝔸¡0]¿¬x¡[])))𐞁
Π = (x↦reduce(②x⨯y,(x≔list(x)),⠤([𝔸₀¿𝔸¡0]¿¬x¡[])))𐞁
🃌 = 𝐎𝐔(len, ⠶par_mul_|par_pow_)
⛶ = 𝐎𝐔(①[x], ⠶par_mul_|par_pow_)
☾ = 𝐎𝐔(𝚲print_(⠤𝔸,⠶𝕂)∨(𝔸₀¿𝔸))𐞂
↨ = 𝐎𝐔(enumerate, ⠶par_mul_)
↕ = 𝐎𝐔(range, ⠶par_mul_|par_pow_)
isinstance = 𝐎𝐁(isinstance, ⠶par_pow_)

ƨ  = 𝐎𝐔(str, ⠶par_mul_)
𝓈  = 𝐎𝐔(set, ⠶par_mul_)
𝒻𝓈 = 𝐎𝐔(frozenset, ⠶par_mul_)
𝒾  = 𝐎𝐔(int, ⠶par_mul_)
𝒻  = 𝐎𝐔(float, ⠶par_mul_)
𝓁  = 𝐎𝐔(list, ⠶par_mul_)
𝓉  = 𝐎𝐔(tuple, ⠶par_mul_)
𝒹  = 𝐎𝐔(dict, ⠶par_mul_)