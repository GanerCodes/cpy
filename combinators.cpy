⮌ operator ⨡ add as add_
⮌ builtins ⨡ print as print_, map as map_, zip as zip_
⮌ functools ⨡ reduce

# Note: ←→ forces x¹←y²→z¹

Ω OP_:
    ⊢ __new__(ℂ,f,d=□,⠶𝕂):
        C = type("OP", (ℂ, ), {})
        ⁅setattr(C, m, (⥌𝕊,o,k=k↦𝕊.check(k,o))) ∀m,k∈𝕂.items()⁆
        C.__call__ = staticmethod(f)
        o = super().__new__(C)
        o.f, o.d, o.kw = f, d∨{}, 𝕂
        ↪o
    check = 𝕊,k,v ↦ ⨳(k∉𝕊.d)∧type(𝕊)(𝕊.f, {k:v}|𝕊.d, ⠶𝕊.kw)
    __rlshift__ = 𝕊,o ↦ (o≔COAR_OP_(o))∧OP_BNARY_(⥌x,y↦𝕊.f(o.f(x),y), 𝕊.d.copy(), ⠶𝕊.kw)
    __rshift__  = 𝕊,o ↦ (o≔COAR_OP_(o))∧OP_BNARY_(⥌x,y↦𝕊.f(x,o.f(y)), 𝕊.d.copy(), ⠶𝕊.kw)
Ω OP_UNARY_(OP_):
    ⊢ check(𝕊, k, v):
        d = (𝕊 ≔ super().check(k, v)).d
        ↪ 𝕊.f(d[v]) ¿(v≔'l')∈d∨(v≔'r')∈d¡ 𝕊
Ω OP_BNARY_(OP_):
    ⊢ check(𝕊, k, v):
        d = (𝕊 ≔ super().check(k, v)).d
        ↪ 𝕊.f(d['l'],d['r']) ¿'l'∈d∧'r'∈d¡ 𝕊

COAR_OP_ = f↦f ¿isinstance(f, OP_)¡ OP_UNARY_(f, ⠶par_or_)

⊢ SWAP_(o):
    » isinstance(o, OP_BNARY_)
    ↪ OP_BNARY_(
        ⥌x,y↦o.f(y,x),
        d=o.d, ⠶o.kw)
⊢ COMPOSE_(f, g):
    f, g = COAR_OP_(f), COAR_OP_(g)
    » ¬⋀((A≔isinstance(f, OP_BNARY_),B≔isinstance(g, OP_BNARY_))), "Cannot compose two binary operators."
    f, g, K = f.f, g.f, {'d': f.d} | par_or_ #f.kw
    ¿ ¬A∧¬B: ↪OP_UNARY_((x↦f(g(x))), ⠶K)
    ¿ ¬A∧ B: ↪OP_BNARY_((x,y↦f(g(x,y))), ⠶K)
    ¿  A∧¬B: ↪OP_BNARY_((x,y↦f(g(x),g(y))), ⠶K)
⊢ DUP_(f):
    » isinstance(f, OP_BNARY_)
    ↪OP_UNARY_((x↦f.f(x,x)), ⠶{'d': f.d} | f.kw)

par_or_  = dict( __ror__='l',  __or__='r')
par_pow_ = dict(__rpow__='l', __pow__='r')
par_mul_ = dict(__rmul__='l', __mul__='r')
par_add_ = dict(__radd__='l', __add__='r')
OP_TO_UNARY_ = OP_UNARY_(f↦OP_UNARY_(f, ⠶par_or_), __rpow__='l')
OP_TO_BNARY_ = OP_UNARY_(f↦OP_BNARY_(f, ⠶par_or_), __rpow__='l')
OP_SWAP_ = OP_UNARY_(SWAP_, __rmatmul__='l')
OP_DUP_ = OP_UNARY_(DUP_, __rmatmul__='l')
OP_COMPOSE_ = OP_BNARY_(COMPOSE_, ⠶par_add_)
sum = (x↦reduce(add_,(x≔list(x)),⠤([𝔸₀¿𝔸¡0]¿¬x¡[])))²
prod = (x↦reduce(⑵x*y,(x≔list(x)),⠤([𝔸₀¿𝔸¡0]¿¬x¡[])))²
reduce ⌃= OP_TO_BNARY_
isinstance = OP_BNARY_(isinstance, ⠶par_pow_)
range = OP_UNARY_(range, ⠶par_mul_)
range_binary = OP_BNARY_(range, ⠶par_pow_)
enumerate = OP_UNARY_(enumerate, ⠶par_mul_)
print = OP_UNARY_(𝚲print_(⠤𝔸,⠶𝕂)∨(𝔸₀¿𝔸), ⠶par_mul_)
skinniside_z = OP_UNARY_(⑴1¿x>0¡0, ⠶par_mul_)
skinniside_b = OP_UNARY_(⑴(1¿x>0¡¯1)¿x¡0, ⠶par_mul_)
setattrs = f↦(⑵⁅setattr(f,a,b)∀a,b∈zip(x,y)⁆)²
other = (⑵⨳(🃌(l≔⚇⨯x)≡2∧y∈l)∧l[y≡l₀])²
split_string = OP_UNARY_(⑴[split_string(k,' ')¿' '∈k¡k ∀k∈x.split(𝔸₀¿𝔸¡' ')], ⠶par_mul_)

list = OP_UNARY_(list, ⠶par_mul_)
set = OP_UNARY_(set, ⠶par_mul_)
dict = OP_UNARY_(dict, ⠶par_mul_)
len = OP_UNARY_(len, ⠶par_mul_)

# no generators- bad idea?
map = (𝚲(list(map_(⠤𝔸)) ¿🃌(𝔸)>1¡ (⥌⠤𝔸,f=𝔸₀↦list(map_(f,⠤𝔸)))¹))²
zip = (𝚲list(zip_(⠤𝔸,⠶𝕂)))⌃OP_TO_BNARY_