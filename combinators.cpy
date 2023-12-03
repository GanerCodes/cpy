⮌ builtins ⨡ print as print_, map as map_, zip as zip_, \
             isinstance as INST_
⮌ functools ⨡ reduce
⮌ itertools ⨡ product as product_
⮌ copy ⨡ deepcopy as dcp
⮌ types ⨡ UnionType

ₛ E ␉ 𝐎𝐔 ␉ OP_UNARY_
ₛ E ␉ 𝐎𝐁 ␉ OP_BNARY_
ₛ E ␉ 𝕸 ␉ par_or_|par_pow_|par_mul_

Ω OP_:
    __slots__ = ('f', 'd', 'FT', 'kw')
    ⊢ __new__(ℂ,f,d=□,FT=□,⠶𝕂):
        C = type("OP", (ℂ, ), {})
        ⁅setattr(C, m, (⥌𝕊,o,k=k↦𝕊.check(k,o))) ∀m,k∈𝕂.items()⁆
        C.__call__ = staticmethod(f)
        ¿FT:
            C.__getattr__ = ②getattr(FT, y)
            C.__invert__ = 𝕊↦𝕊󰀅ᵀ
        o = super().__new__(C)
        oᶠ, oᵈ, o󰀅ᵀ, oᵏʷ = f, d∨{}, FT, 𝕂
        ↪o
    check = 𝕊,k,v ↦ ⨳(k∉𝕊ᵈ)∧type(𝕊)(𝕊ᶠ, {k:v}|𝕊ᵈ, 𝕊󰀅ᵀ, ⠶𝕊ᵏʷ)
Ω 𝐎𝐔(OP_):
    ⊢ check(𝕊, k, v):
        d = (𝕊 ≔ super().check(k,v))ᵈ
        ↪ 𝕊ᶠ(dᵥ) ¿(v≔l❟)∈d∨(v≔r❟)∈d¡ 𝕊
Ω 𝐎𝐁(OP_):
    ⊢ check(𝕊, k, v):
        d = (𝕊 ≔ super().check(k,v))ᵈ
        ↪ 𝕊ᶠ(d[l❟],d[r❟]) ¿l❟∈d∧r❟∈d¡ 𝕊

⊢ isinstance(x, y):
    ¿INST_(y,type|UnionType): □
    ⸘INST_(y,OP_): y=y󰀅ᵀ
    ⸘INST_(y,list|tuple|set): ↪any(isinstance(x,z)∀z∈y)
    ¡: y=type(y)
    ↪ INST_(x, y)

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
⋀, ⋁ = all𐞁, any𐞁
∪ = (𝚲set.union(⠤map_(set,𝔸)))𐞁
∩ = (𝚲set.intersection(⠤map_(set,𝔸)))𐞁
∖ = (𝚲set.__sub__(⠤map_(set,𝔸)))𐞁
⨉ = (𝚲list(product_(⠤𝔸)))𐞁
⍉ = (𝚲list(ζ(⠤𝔸₀,⠶𝕂)))𐞂
ζ = (𝚲list(map(list,zip_(⠤𝔸,⠶𝕂))))𐞁
ᴙ = 𝐎𝐔(①x﹕﹕₋₁, ⠶par_mul_|par_pow_)
ᴍ = (𝚲(list(map_(⠤𝔸)) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦list(map_(f,⠤𝔸)))𐞂))𐞁
󰈲 = (𝚲(list(filter(𝔸₀,⠤𝔸₁﹕)) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦list(filter(f,⠤𝔸)))𐞂))𐞁
󰈳 = (𝚲(list(filter(⥌x,f=𝔸₀↦¬f(x),⠤𝔸₁﹕)) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦list(filter(①¬f(x),⠤𝔸)))𐞂))𐞁
ſ = (𝚲(reduce(⠤𝔸) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦reduce(f,⠤𝔸))𐞂))𐞁
Σ = (x↦reduce(②x+y,(x≔list(x)),⠤([𝔸₀¿𝔸¡0]¿¬x¡[])))𐞁
Π = (x↦reduce(②x⨯y,(x≔list(x)),⠤([𝔸₀¿𝔸¡0]¿¬x¡[])))𐞁
🃌 = 𝐎𝐔(len, ⠶par_mul_|par_pow_)
⛶ = 𝐎𝐔(①[x], ⠶par_mul_|par_pow_)
☾ = 𝐎𝐔(𝚲print_(⠤𝔸,⠶𝕂)∨(𝔸₀¿𝔸))𐞂
↨ = 𝐎𝐔(enumerate, ⠶par_mul_)
↕ = 𝐎𝐔(range, ⠶par_mul_|par_pow_)
≾ = isinstance𐞁

mk_type = ①𝐎𝐔(x, FT=x, ⠶𝕂)
ƨ  = mk_type(str, ⠶par_mul_)
𝓈  = mk_type(set, ⠶par_mul_)
𝒻𝓈 = mk_type(frozenset, ⠶par_mul_)
𝒾  = mk_type(int, ⠶par_mul_)
𝒻  = mk_type(float, ⠶par_mul_)
𝓁  = mk_type(list, ⠶par_mul_)
𝓉  = mk_type(tuple, ⠶par_mul_)
𝒹  = mk_type(dict, ⠶par_mul_)