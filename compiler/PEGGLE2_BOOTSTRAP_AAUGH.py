import util

### HEADER
exec('from math import *')
del factorial, e, pi, tau, sqrt, cbrt
ᐧ1d45cᐧ, ᐧ1d451ᐧ, ᐧ1d44fᐧ, ᐧ1d459ᐧ, ᐧ1d461ᐧ, ᐧ1d460ᐧ, ᔐ, ᐧ1d456ᐧ, ᐧ1d453ᐧ = (object, dict, bool, list, tuple, set, str, int, float)
from py_naming_tools import py_escape_var as PEV
from functools import reduce
from itertools import starmap, filterfalse, product, accumulate, zip_longest
LITERAL_OPS_ = {'∧': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x and y, '∨': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x or y, '*': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x * y, '/': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x / y, '<': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x < y, '>': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x > y, '|': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x | y, '&': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x & y, '^': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x ^ y, '%': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x % y, '==': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x == y, '!=': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x != y, '<=': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x <= y, '>=': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x >= y, '//': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x // y, '**': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x ** y, '<<': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x << y, '>>': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x >> y, '+': lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: +v[0] if 1 == ᐧ1f0ccᐧ((v := ᐧ1d563ᐧ(ᐧ1d538ᐧ))) else v[0] + v[1], '-': lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: -v[0] if 1 == ᐧ1f0ccᐧ((v := ᐧ1d563ᐧ(ᐧ1d538ᐧ))) else v[0] - v[1], 'not': lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: not ᐧ1d563ᐧ(ᐧ1d538ᐧ)[0], 'is': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x is y, 'is not': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x is not y, 'in': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x in y, 'not in': lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x not in y}
getitem, setitem = (lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x[y], lambda x, y, z, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.__setitem__(y, z))
setattr_ret_ = lambda x, y, z, w, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: setattr(y, z, w) or w
setitem_ret_ = lambda x, y, z, w, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: setitem(y, z, w) or w
OP_DUPER_ = lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(x, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
OP_SWAPA_ = lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(y, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
OP_LNULL_ = lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(ᐧ2400ᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
OP_RNULL_ = lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(x, ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
OP_BSTAR_ = lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(*x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
ᐧ2400ᐧ = NULL = ᐧ1d45cᐧ()
ᐧ2713ᐧ, ᐧ2717ᐧ = (True, False)
ᐧ1d49eᐧᐧ2133ᐧ, ᐧ1d4aeᐧᐧ2133ᐧ, ᐧ1d5d9ᐧ = (classmethod, staticmethod, callable)
ᗜ = ᐧ25a1ᐧ = None
π = 3.141592653589793
ᐧ212fᐧ = 2.718281828459045
î = complex(0, 1)
ᐧ221eᐧ, ᐦ, τ = (inf, '', 2 * π)
ᐧ2189ᐧ = 0
ᐧ00bdᐧ, ᐧ2153ᐧ, ᐧ00bcᐧ, ᐧ2155ᐧ, ᐧ2159ᐧ, ᐧ2150ᐧ, ᐧ215bᐧ, ᐧ2151ᐧ, ᐧ2152ᐧ = (1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10)
ᐧ2154ᐧ, ᐧ2156ᐧ = (2 / 3, 2 / 5)
ᐧ00beᐧ, ᐧ2157ᐧ, ᐧ215cᐧ = (3 / 4, 3 / 5, 3 / 8)
ᐧ2158ᐧ = 4 / 5
ᐧ215aᐧ, ᐧ215dᐧ = (5 / 6, 5 / 8)
ᐧ215eᐧ = 7 / 8
ᐧ1d55dᐧ, ᐧ1d563ᐧ = (lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: [*ᐧ1d538ᐧ] if x is ᐧ2400ᐧ else [x], lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧf0233ᐧ(x, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x is ᐧ2400ᐧ))
is_iter = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: hasattr(x, '__iter__')

class ᐧ1d450ᐧᐧ1d451ᐧ(ᐧ1d451ᐧ):

    def __init__(ᐧ1d54aᐧ, ƒ, *ᐧ1d538ᐧ, ᐧ1d454ᐧ=ᐧ25a1ᐧ, **ᐧ1d542ᐧ):
        ᐧ1d54aᐧ.ƒ, ᐧ1d54aᐧ.ᐧ1d454ᐧ = (ƒ, ᐧ1d454ᐧ)
        super().__init__(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
    __call__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ƒ(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
    __repr__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ['__repr__'](ᐧ1d54aᐧ) if '__repr__' in ᐧ1d54aᐧ else super().__repr__()
    __getitem__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: super().__getitem__(x) if x in ᐧ1d54aᐧ else ᐧ1d54aᐧ.ᐧ1d454ᐧ(x)
ᐧ2b24ᐧ = ᐧ1d45cᐧ()

def ᐧf41eᐧ(ƒ):

    def ᐧ1d4bbᐧ(*ᐧ1d736ᐧ, **ᐧ1d73fᐧ):

        def ᐧ1d453ᐧ(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ):
            ᐧ1d4d0ᐧ, ᐧ1d538ᐧ = (ᐧ1d459ᐧ(ᐧ1d736ᐧ), ᐧ1d459ᐧ(ᐧ1d538ᐧ))
            ᐧ1d4daᐧ = ᐧ1d459ᐧ(ᐧ1d73fᐧ.items())
            a, k = ([], {})
            while ᐧ1d4d0ᐧ:
                x = ᐧ1d4d0ᐧ.pop(0)
                a.append(ᐧ1d538ᐧ.pop(0) if x == ᐧ2b24ᐧ else x)
            while ᐧ1d4daᐧ:
                x, y = ᐧ1d4daᐧ.pop(0)
                k[x] = ᐧ1d538ᐧ.pop(0) if y == ᐧ2b24ᐧ else y
            return ƒ(*a + ᐧ1d538ᐧ, **k | ᐧ1d542ᐧ)
        return ᐧ1d453ᐧ
    return ᐧ1d4bbᐧ
ᐧf005ᐧ = ᐧ1d450ᐧᐧ1d451ᐧ((t := (lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(*Σ(ᐧ1d538ᐧ, []), **ᐧ1d542ᐧ))), ᐧ1d454ᐧ=t)

class ⴳ(ᐧ1d456ᐧ):
    __new__ = lambda ᐧ2102ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d456ᐧ.__new__(ᐧ2102ᐧ, 1)
    __call__, __repr__ = (lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ⴳ, lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: 'ⴳ')

class ⴴ(ᐧ1d456ᐧ):
    __new__ = lambda ᐧ2102ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d456ᐧ.__new__(ᐧ2102ᐧ, 0)
    __call__, __repr__ = (lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ⴴ, lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: 'ⴴ')
ⴳ, ⴴ = (ⴳ(), ⴴ())

def _get_depths(x):
    if not is_iter(x):
        return {0}
    if ᐹ(x, ᔐ):
        return {1}
    return {w + 1 for z in x for w in _get_depths(z)}

def _map_neg_d(x, y, n):
    if ᐹ(x, ᔐ):
        return [y(z) for z in x] if not n else y(x) if n == 1 else x
    if 0 in (d := _get_depths(x)):
        return x if n else y(x)
    x = [_map_neg_d(z, y, n) for z in x]
    return y(x) if n in d else x

def _map_pos_d(x, y, i):
    if not i:
        return y(x)
    if ᐹ(x, ᔐ):
        return [y(z) for z in x]
    return [_map_pos_d(z, y, i - 1) for z in x] if is_iter(x) else y(x)

def _map_d(x, y, n=1):
    if n < 0:
        return _map_neg_d(x, y, -n - 1)
    return _map_pos_d(x, y, 2 ** 24 if n == ᐧ221eᐧ else n)

class ᐧ221aᐧ:
    __getitem__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: y ** (1 / x)
    __call__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x ** ᐧ00bdᐧ

def _window(ᐧ1d54fᐧ, l=1, r=1, m=ᐧ2713ᐧ, s=ᐧ25a1ᐧ, Δ=1):
    (c := ᐧ1f0ccᐧ((ᐧ1d54fᐧ := ᐧ1d459ᐧ(ᐧ1d54fᐧ))))
    if s is ᐧ2400ᐧ:
        return ᴍ(ᐧ2b65ᐧ(ᐧ1d54fᐧ)[l:c - r:Δ], lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54fᐧ[x - l:x] + ᐧ26f6ᐧ(ᐧ1d54fᐧ[x]) * ᐧ1d44fᐧ(m) + ᐧ1d54fᐧ[x + 1:x + r + 1])
    V = ᐧ26f6ᐧ(s) * l + ᐧ1d54fᐧ + ᐧ26f6ᐧ(s) * r
    return ᴍ(ᐧ2b65ᐧ(ᐧ1d54fᐧ)[::Δ], lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: V[x:x + l] + ᐧ26f6ᐧ(V[x + l]) * ᐧ1d44fᐧ(m) + V[x + l + 1:x + l + r + 1])

class ᐧ1d44fᐧᐧ1d454ᐧ:
    __getitem__ = lambda ᐧ1d54aᐧ, z, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ƒ(x, y, z)
    __call__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ƒ(*ᐧ1d538ᐧ)

class ᐧ017fᐧ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: reduce(y, x, *(z,) * (z is not ᐧ2400ᐧ)))

class Ϝ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(accumulate(x, y, **{} if z == ᐧ2400ᐧ else {'initial': z})))

class ᙎ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: _window((h := ᐧ1d563ᐧ(ᐧ22c4ᐧ(x, y)))[0], *(ᐹ(y, ᐧ1d456ᐧ) and ᐧ22c4ᐧ(y, y) or y if ᐧ1f0ccᐧ(h) == 2 else ᐧ22c4ᐧ(1, 1)), ᐧ2717ᐧ, ᐧ25a1ᐧ if z is ᐧ2400ᐧ else z, 1))

class ᙡ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: _window((h := ᐧ1d563ᐧ(ᐧ22c4ᐧ(x, y)))[0], *(ᐹ(y, ᐧ1d456ᐧ) and ᐧ22c4ᐧ(y, y) or y if ᐧ1f0ccᐧ(h) == 2 else ᐧ22c4ᐧ(1, 1)), ᐧ2713ᐧ, ᐧ25a1ᐧ if z is ᐧ2400ᐧ else z, 1))

class ᗢ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: _window((h := ᐧ1d563ᐧ(ᐧ22c4ᐧ(x, y)))[0], *(ᐹ(y, ᐧ1d456ᐧ) and ᐧ22c4ᐧ(y, y) or y if ᐧ1f0ccᐧ(h) == 2 else z is ᐧ2400ᐧ and ᐧ22c4ᐧ(1, 1) or ᐧ22c4ᐧ(0, z)), ᐧ2717ᐧ, ᐧ2400ᐧ, z is ᐧ2400ᐧ and 1 or z + 1))

class ᙧ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: _window((h := ᐧ1d563ᐧ(ᐧ22c4ᐧ(x, y)))[0], *(ᐹ(y, ᐧ1d456ᐧ) and ᐧ22c4ᐧ(y, y) or y if ᐧ1f0ccᐧ(h) == 2 else z is ᐧ2400ᐧ and ᐧ22c4ᐧ(1, 1) or ᐧ22c4ᐧ(0, z)), ᐧ2713ᐧ, ᐧ2400ᐧ, z is ᐧ2400ᐧ and 1 or z + 1))

class ᐧf0e35ᐧ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᴍ(ᐧ2b65ᐧ(l), ⴴ if z is ᐧ2400ᐧ else z if ᐧ1d5d9ᐧ(z) else lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: z) + x if (l := (y - ᐧ1f0ccᐧ(x))) > 0 else x)

class ᐧf0e37ᐧ(ᐧ1d44fᐧᐧ1d454ᐧ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, z=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x + ᴍ(ᐧ2b65ᐧ(l), ⴴ if z is ᐧ2400ᐧ else z if ᐧ1d5d9ᐧ(z) else lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: z) if (l := (y - ᐧ1f0ccᐧ(x))) > 0 else x)

class ᴍ:
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(_map_d)

    def __getitem__(ᐧ1d54aᐧ, i):
        S, ƒ = (ᐧ1d460ᐧ(i if ᐹ(i, ᐧ1d461ᐧ) else (i,)), ᐧ25a1ᐧ)
        if (s := 'D') in S:
            ƒ = lambda f, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: type(x)(f(x.items(), y))
        elif (s := 'K') in S:
            ƒ = lambda f, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: type(x)(ζ(f(x.items(), y), x.values()))
        elif (s := 'V') in S:
            ƒ = lambda f, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: type(x)(ζ(x.keys(), f(x.items(), y)))
        if ƒ:
            S.discard(s)
            return ƒ(S and ᐧ1d54aᐧ[S.pop()] or ᐧ1d54aᐧ)
        return lambda x, y, i=i, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ƒ(x, y, i)
    __call__ = lambda ᐧ1d54aᐧ, x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ƒ(x, y, 1)

class ꟿ(ᴍ):
    ƒ = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, y, i, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: _map_d(x, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: y(*(x if is_iter(x) else (x,))), i))
ᐧf0efeᐧ = ᐧ1d450ᐧᐧ1d451ᐧ(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x, ᐧ1d454ᐧ=lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d450ᐧᐧ1d451ᐧ(lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x, __repr__=lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: f'\U000f0efe[{x}]'), __repr__=lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: '\U000f0efe')
ᐧ221aᐧ = ᐧ221aᐧ()
ᴍ, ꟿ, ᐧ017fᐧ, Ϝ = (ᴍ(), ꟿ(), ᐧ017fᐧ(), Ϝ())
ᙎ, ᙡ, ᗢ, ᙧ = (ᙎ(), ᙡ(), ᗢ(), ᙧ())
ᐧf0e35ᐧ, ᐧf0e37ᐧ = (ᐧf0e35ᐧ(), ᐧf0e37ᐧ())

def ᐧ2a33ᐧ(α, β):
    if α is ᐧ2400ᐧ:
        α, β = (β, α)
    assert α, β is ᐧ2400ᐧ and ᐦ or β
    return α

def _wherest(ᐧ1d54fᐧ, ƒ=ᐧ1d44fᐧ, I=ⴴ):
    ƒ = ƒ is ᐧ2400ᐧ and ᐧ1d44fᐧ or ƒ
    for i, x in ᐧ21a8ᐧ(ᐧ1d54fᐧ):
        if ƒ(x):
            return i if I else x
    return ᐧ25a1ᐧ
ᣆ = ᐧ1d450ᐧᐧ1d451ᐧ((ƒ := (lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: y(x) if (ᐧ1d538ᐧ[0] if ᐧ1f0ccᐧ(ᐧ1d538ᐧ) else x) else x)), ᐧ1d454ᐧ=lambda a, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(x, y, a))
ᐧf0445ᐧ = ᐧ1d450ᐧᐧ1d451ᐧ(_wherest, I=lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: _wherest(*ᐧ1d538ᐧ, I=ᐧ2713ᐧ))
ᐧf0441ᐧ = lambda ᐧ1d54fᐧ, ƒ=ᐧ1d44fᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25a1ᐧ if ᐧ25a1ᐧ is (i := ᐧf0445ᐧ['I'](ᐧ1d54fᐧ, ƒ)) else ᐧ1d54fᐧ[:i]
ᐧf0443ᐧ = lambda ᐧ1d54fᐧ, ƒ=ᐧ1d44fᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25a1ᐧ if ᐧ25a1ᐧ is (i := ᐧf0445ᐧ['I'](ᐧ1d54fᐧ, ƒ)) else ᐧ1d54fᐧ[i:]
ᐧ2282ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d460ᐧ(x).issubset(ᐧ1d460ᐧ(y))
ᐧ2283ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d460ᐧ(y).issubset(ᐧ1d460ᐧ(x))
ᐧ228aᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (α := ᐧ1d460ᐧ(x)).issubset((β := ᐧ1d460ᐧ(y))) and α != β
ᐧ228bᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (α := ᐧ1d460ᐧ(y)).issubset((β := ᐧ1d460ᐧ(x))) and α != β
ᐧ2284ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: not ᐧ2282ᐧ(x, y)
ᐧ2285ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: not ᐧ2283ᐧ(x, y)
ᐧ222aᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d460ᐧ(x) | ᐧ1d460ᐧ(y)
ᐧ2229ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d460ᐧ(x) & ᐧ1d460ᐧ(y)
ᐧ2216ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d460ᐧ(x) - ᐧ1d460ᐧ(y)
ᐧ2a09ᐧ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᴍ(product(*(v[0] if 1 == ᐧ1f0ccᐧ((v := ᐧ1d563ᐧ(ᐧ1d538ᐧ))) else v)), ᐧ1d459ᐧ)
ᐧ220bᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: y in x
ᐧ220cᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: y not in x
ᐧ2213ᐧ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: [-h[0], +h[0]] if ᐧ1f0ccᐧ((h := ᐧ1d563ᐧ(ᐧ1d538ᐧ))) == 1 else [h[0] - h[1], h[0] + h[1]]
ᐧ00b1ᐧ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: [+h[0], -h[0]] if ᐧ1f0ccᐧ((h := ᐧ1d563ᐧ(ᐧ1d538ᐧ))) == 1 else [h[0] + h[1], h[0] - h[1]]

def ᐹ(x=ᐧ2400ᐧ, y=ᐧ2400ᐧ):
    if x is ᐧ2400ᐧ:
        return type(y)
    elif y is ᐧ2400ᐧ:
        return type(x)
    return isinstance(x, y if isinstance(y, type) else type(y))
ᐧ1f0ccᐧ = len
ᴙ = ᐧ1d450ᐧᐧ1d451ᐧ(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (x if ᐹ(x, ᔐ) else ᐧ1d459ᐧ(x))[::-1], L=lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(x)[::-1])
ᐧ2349ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ζ(*x)
ᐧ236dᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᴍ(x.split('\u205f'), ᐧ236dᐧ) if '\u205f' in x else x.split('\u2009')
ᐧ21a8ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(enumerate(x))
ᐧ2b65ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(range(x if ᐹ(x, ᐧ1d456ᐧ) else ᐧ1f0ccᐧ(x)))
ᐧ2908ᐧ, ᐧ2909ᐧ = ᴍ((min, max), lambda ƒ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(ᐧ1d538ᐧ[0], key=ᐧ1d538ᐧ[1]) if ᐧ1d538ᐧ[1:] and ᐧ1d5d9ᐧ(ᐧ1d538ᐧ[1]) else ƒ(*ᐧ1d563ᐧ(ᐧ1d538ᐧ)))
ⴵ = sign = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: 1 if x > 0 else x and -1 or 0
ᐧ26f6ᐧ = ᐧ1d450ᐧᐧ1d451ᐧ(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: [x], S=lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: {x}, T=lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (x,))
ᐧ25a2ᐧ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: round(*ᐧ1d563ᐧ(ᐧ1d538ᐧ))
ᐧ2026ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(range(x, y))
ᐧ0021ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: Π(ᐧ2026ᐧ(1, x + 1), 1)
ᐧ2af0ᐧ, ᐧ2aefᐧ = (lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: +abs(x), lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: -abs(x))

def ᐧ2b04ᐧ(x=ᐧ2400ᐧ, y=ᐧ2400ᐧ):
    if x is ᐧ2400ᐧ:
        x, y = (y, x)
    if ᐹ(x, ᔐ) and (y is ᐧ2400ᐧ or ᐹ(y, ᔐ)):
        return x.strip(*ᐧ1d563ᐧ((y,)))
    ᐧ2a33ᐧ(ᐧ2717ᐧ, NULL)
ᐧ25c4ᐧ, ᐧ25baᐧ = (lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x, lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: y)

def ᐧ22c0ᐧ(ᐧ1d44bᐧ, v=ᐧ2713ᐧ):
    for v in ᐧ1d44bᐧ:
        if not v:
            return v
    return v

def ᐧ22c1ᐧ(ᐧ1d44bᐧ, v=ᐧ2717ᐧ):
    for v in ᐧ1d44bᐧ:
        if v:
            return v
    return v
ᐧ263eᐧ = lambda *ᐧ1d538ᐧ, flush=ᐧ2713ᐧ, **ᐧ1d542ᐧ: print(*ᐧ1d538ᐧ, flush=flush, **ᐧ1d542ᐧ) or (ᐧ1d538ᐧ and ᐧ1d538ᐧ[0])
ζ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᴍ(zip(*ᐧ1d563ᐧ(ᐧ1d538ᐧ)), ᐧ1d459ᐧ)
ᐧf0232ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(filter(*ᐧ1d55dᐧ(*ᐧ1d538ᐧ, ᐧ25a1ᐧ), x))
ᐧf0233ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d459ᐧ(filterfalse(*ᐧ1d55dᐧ(*ᐧ1d538ᐧ, ᐧ25a1ᐧ), x))
Π = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ017fᐧ(x, LITERAL_OPS_['*'], *ᐧ1d563ᐧ(ᐧ1d538ᐧ))
Σ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ017fᐧ(x, LITERAL_OPS_['+'], *ᐧ1d563ᐧ(ᐧ1d538ᐧ))
ᐧf04bcᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: sorted(x, key=ᐧ1d55dᐧ(y, ᐧ25a1ᐧ)[0])
ᐧf04bdᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: sorted(x, key=ᐧ1d55dᐧ(y, ᐧ25a1ᐧ)[0], reverse=ᐧ2713ᐧ)
ᐧeb86ᐧ = ᐧ1d450ᐧᐧ1d451ᐧ(lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (lambda I, ƒ=ᐧ1d44fᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25c4ᐧ((r := {}), ᴍ(I, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: r.setdefault((h := ƒ(x)), []).append(x))))(*ᐧ1d563ᐧ(ᐧ1d538ᐧ), **ᐧ1d542ᐧ), S=lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᴍ(ᐧf04bcᐧ(ᐧeba6ᐧ(ᐧeb86ᐧ(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ).items), NULL), lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x[1]), B=lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25baᐧ((h := {ᐧ2713ᐧ: [], ᐧ2717ᐧ: [], **ᐧeb86ᐧ(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ)}), [h[0], h[1]]))
ᐧeba6ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
ᐧ2218ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x(y)
ᐧ25cbᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x(y(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ))

class ᐧ1d459ᐧᐧ1d459ᐧ(ᐧ1d459ᐧ):
    ᐧ25a1ᐧ
ᐧ22c4ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25baᐧ((x if ᐹ(x, ᐧ1d459ᐧᐧ1d459ᐧ) else (x := ᐧ1d459ᐧᐧ1d459ᐧ((x,)))).append(y), x)
ᐧ2a01ᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d44fᐧ(x) == ᐧ1d44fᐧ(y)
ᐧ22bbᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d44fᐧ(x) ^ ᐧ1d44fᐧ(y) and (x or y)
ᐧ22bcᐧ = lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: not (ᐧ1d44fᐧ(x) and ᐧ1d44fᐧ(y)) and (x or y)

def ᐧ24e6ᐧ(*ᐧ1d538ᐧ, ᐧ1d400ᐧ=ᐧ25a1ᐧ):
    (ᐧ1d400ᐧ := (ᐧ1d400ᐧ or []))
    *ᐧ1d538ᐧ, ƒ = ᐧ1d538ᐧ
    if not ᐧ1d538ᐧ:
        return ƒ(*ᐧ1d400ᐧ)
    ᐧ1d552ᐧ, *ᐧ1d538ᐧ = ᐧ1d538ᐧ
    with ᐧ1d552ᐧ as ᐧ1d41aᐧ:
        ᐧ2218ᐧ(ᐧ1d400ᐧ.append, ᐧ1d41aᐧ)
        return ᐧ24e6ᐧ(*ᐧ1d538ᐧ, ƒ, ᐧ1d400ᐧ=ᐧ1d400ᐧ)

class ᐧ2135ᐧ(ᐧ1d451ᐧ):
    ᐧ1d436ᐧᐧ1d45bᐧ = 'ℵ'
    __init__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: super().__init__(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
    __setattr__ = ᐧ1d451ᐧ.__setitem__
    __getitem__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d451ᐧ.__getitem__(ᐧ1d54aᐧ, x) if x in ᐧ1d54aᐧ else ᐧ1d54aᐧ.getdef()
    __getattr__ = __getitem__
    __iter__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: iter(ᐧ1d54aᐧ.items())
    __repr__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: f'{ᐧ1d54aᐧ.__class__.ᐧ1d436ᐧᐧ1d45bᐧ}{(f'[{h[0]}]' if 0 in (h := ᐧ1d54aᐧ.__dict__) else ᐦ)}({', '.join(ꟿ(ᐧeba6ᐧ(ᐧ1d54aᐧ.items), lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: f'{x}={y}'))})'
    __call__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25baᐧ(ᐧ1d451ᐧ.update(ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ), ᐧ1d54aᐧ)
    __bool__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1f0ccᐧ(ᐧ1d54aᐧ) > 0
    __or__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.copy()(x)

    def __getstate__(ᐧ1d54aᐧ):
        if ᐧ1d54aᐧ.hasdef():
            return (ᐧ1d451ᐧ(ᐧ1d54aᐧ), ᐧ1d54aᐧ.getdef())
        else:
            return (ᐧ1d451ᐧ(ᐧ1d54aᐧ),)

    def __setstate__(ᐧ1d54aᐧ, s):
        ᐧ1d54aᐧ.__init__(s[0])
        if ᐧ1f0ccᐧ(s) > 1:
            ᐧ1d54aᐧ.setdef(s[1])

    def __pow__(ᐧ1d54aᐧ, x):
        if x == LITERAL_OPS_['-']:
            return ᐧ2218ᐧ(ᐧ1d459ᐧ, ᐧeba6ᐧ(ᐧ1d54aᐧ.keys))
        if x == LITERAL_OPS_['+']:
            return ᐧ2218ᐧ(ᐧ1d459ᐧ, ᐧeba6ᐧ(ᐧ1d54aᐧ.values))
        if x == LITERAL_OPS_['*']:
            return ᐧ2218ᐧ(ᐧ1d459ᐧ, ᐧeba6ᐧ(ᐧ1d54aᐧ.items))
        ᐧ2a33ᐧ(ᐧ2717ᐧ, NULL)
    hasdef = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: 0 in ᐧ1d54aᐧ.__dict__
    getdef = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.__dict__[0]
    setdef = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25baᐧ(setitem_ret_((þ0 := x), (þ1 := ᐧ1d54aᐧ.__dict__), (þ2 := 0), þ0), ᐧ1d54aᐧ)

    def copy(ᐧ1d54aᐧ):
        r = type(ᐧ1d54aᐧ)(super().copy())
        if ᐧ1d54aᐧ.hasdef():
            r.setdef(ᐧ1d54aᐧ.getdef())
        return r

class ᐧ2136ᐧ(ᐧ2135ᐧ):
    ᐧ1d436ᐧᐧ1d45bᐧ = 'ℶ'
    __iter__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: iter(ᐧ1d54aᐧ.values())

class _hwrap(ᐧ1d451ᐧ):

    def __init__(ᐧ1d54aᐧ, ᐧ1d450ᐧ):
        ᐧ1d54aᐧ.ᐧ1d450ᐧ, ᐧ1d54aᐧ.ᐧ1d45bᐧ = (ᐧ1d450ᐧ, ᐧ1d450ᐧ.ᐧ1d436ᐧᐧ1d45bᐧ)
    __getitem__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ᐧ1d450ᐧ().setdef(x)
    __setitem__ = lambda ᐧ1d54aᐧ, x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ25baᐧ((ᐧ24afᐧ := ᐧ1d54aᐧ.ᐧ1d450ᐧ()).__setitem__(x, y), ᐧ24afᐧ)
    __call__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ᐧ1d450ᐧ(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ)
    __or__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ᐧ1d450ᐧ() | x
    __pow__ = lambda ᐧ1d54aᐧ, x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.ᐧ1d450ᐧ() ** x
    __repr__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: f'{ᐧ1d54aᐧ.ᐧ1d45bᐧ}()'
    __bool__ = ⴴ
ᐧ2135ᐧ = _hwrap(ᐧ2135ᐧ)
ᐧ2136ᐧ = _hwrap(ᐧ2136ᐧ)

### 𝐍
from util import Z

class ᐧ1d40dᐧ:

    def __init__(ᐧ1d54aᐧ, t, *c):
        ᐧ1d54aᐧ.t, ᐧ1d54aᐧ.c = (t, c or [])
    __iter__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: iter(ᐧ1d54aᐧ.c)
    __repr__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: f'𝐍⟨{ᐧ1d54aᐧ.t or '∅'}⟩⟨{', '.join(ᴍ(ᐧ1d54aᐧ, ᔐ))}⟩'
    __getitem__ = lambda ᐧ1d54aᐧ, i, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.c[i]
    __len__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1f0ccᐧ(ᐧ1d54aᐧ.c)
    ft = ᐧ1d4aeᐧᐧ2133ᐧ(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d40dᐧ(x[0], *(ᴍ(x[1], ᐧ1d40dᐧ.ft) if ᐹ(x[1], ᐧ1d459ᐧ | ᐧ1d461ᐧ) and ᐧ1f0ccᐧ(x[1]) == 2 else ᐧ26f6ᐧ(x[1]))))
    tt = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (ᐧ1d54aᐧ.t, ᴍ(ᐧ1d54aᐧ.c, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧeba6ᐧ(x.tt) if ᐹ(x, ᐧ1d40dᐧ) else x))
    copy = lambda ᐧ1d54aᐧ, t=ᐧ25a1ᐧ, c=ᐧ25a1ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐹ(NULL, ᐧ1d54aᐧ)(ᐧ1d54aᐧ.t if t is ᐧ25a1ᐧ else t, *(ᐧ1d54aᐧ.c if c is ᐧ25a1ᐧ else c))
    rcopy = lambda ᐧ1d54aᐧ, t=ᐧ25a1ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐹ(NULL, ᐧ1d54aᐧ)(ᐧ1d54aᐧ.t if t is ᐧ25a1ᐧ else t, *ᴍ(ᐧ1d54aᐧ.c, ᐹ(NULL, ᐧ1d54aᐧ).rcopy)) if ᐹ(ᐧ1d54aᐧ, ᐧ1d40dᐧ) else ᐧ1d54aᐧ

    def frp(ᐧ1d54aᐧ, f, r, pre=ᐧ2717ᐧ):
        ᐧ1d4e1ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.copy(c=ᴍ(x, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.frp(f, r, pre)))
        ᐧ1d54aᐧ = ᣆ[pre](ᐧ1d54aᐧ, ᐧ1d4e1ᐧ)
        if ᐧ2218ᐧ(f, ᐧ1d54aᐧ):
            return r(ᐧ1d54aᐧ)
        return ᣆ[not pre](ᐧ1d54aᐧ, ᐧ1d4e1ᐧ)
    ftrp = lambda ᐧ1d54aᐧ, fs, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.frp(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.t in fs, *ᐧ1d538ᐧ)

    def extract(ᐧ1d54aᐧ, f, E=ᐧ25a1ᐧ, β=ᐧ2713ᐧ, Δ=ᐧ2717ᐧ, pre=ᐧ2717ᐧ):
        L = r, E = ([], [] if E is ᐧ25a1ᐧ else E)
        ᐧ2102ᐧ = ᐹ(NULL, ᐧ1d54aᐧ)
        ᐧ1d740ᐧ = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ2102ᐧ.extract(x, f, E, pre=pre)
        ᴍ(ᐧ1d54aᐧ, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: L[ᐧ1d44fᐧ(f((x := ᣆ[pre](x, ᐧ1d740ᐧ))))].append(x))
        n = ᐧ1d54aᐧ.copy(c=r if pre else ᴍ(r, ᐧ1d740ᐧ))
        return ((n, E) if Δ else E) if β and E is ᐧ25a1ᐧ else n
    filter = lambda ᐧ1d54aᐧ, f, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.extract(ᐧ25cbᐧ(LITERAL_OPS_['not'], f), *ᐧ1d538ᐧ, **ᐧ1d542ᐧ, β=ᐧ2717ᐧ, Δ=ᐧ2717ᐧ)

    def P(ᐧ1d54aᐧ):
        clc = lambda x, c='BL', *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: getattr(Z, c) + x + Z.W
        ML = lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ1f0ccᐧ(x) - Σ(ᴍ((Z.W, Z.BL, Z.RE, Z.dBL, Z.GRE, Z.YEL), lambda k, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.count(k) * ᐧ1f0ccᐧ(k)), 0)

        def box(x):
            (o, c), O, C = ᴍ[2](ᐧ236dᐧ(f'[]\u2009⎡⎢⎣\u2009⎤⎥⎦'), lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: clc(x, 'dBL'))
            x = x.split('\n')
            if ᐧ1f0ccᐧ(x) == 1:
                return f'{o}{x[0]}{c}'
            ms = ᐧ2909ᐧ(ᴍ(x, ML), NULL)
            return '\n'.join(ꟿ(ᙡ(x, NULL), lambda x, y, z, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: O[(n := (1 - (x is ᐧ25a1ᐧ) + (z is ᐧ25a1ᐧ)))] + y + (ms - ML(y)) * ' ' + C[n]))
        if not ᐹ(ᐧ1d54aᐧ, ᐧ1d40dᐧ):
            return ᐧ2218ᐧ(ᔐ, ᐧ1d54aᐧ)
        ᐧ2205ᐧ = clc('∅', 'RE')

        def format_e(e):
            if not e:
                return ᐦ
            r = []
            for k, v in e:
                if k == 'T':
                    (r := (r + ᐧ26f6ᐧ(clc('T', 'GRE'))))
                else:
                    (r := (r + ᐧ26f6ᐧ(f'{k}{clc('→', 'BL')}{v.t}')))
            return f'{clc('\U000f0141', 'YEL')}{','.join(r)}{clc('\U000f0142', 'YEL')}'
        nam = (ᐧeba6ᐧ(ᐧ1d54aᐧ.t.P) if ᐹ(ᐧ1d54aᐧ.t, ᐧ1d40dᐧ) else f'{ᐧ1d54aᐧ.t}{format_e(ᐧ1d54aᐧ.e)}' if ᐹ(ᐧ1d54aᐧ, Ń) else ᐧ2218ᐧ(ᔐ, ᐧ1d54aᐧ.t)) or ᐧ2205ᐧ
        start = ᐧ2218ᐧ(box, nam)
        (ᐧ2574ᐧ, ᐧ256eᐧ), m0, m1, m2 = ᴍ[2](ᐧ236dᐧ(f'─┬\u2009┬─\u2009├╰\u2009│ '), clc)
        if not ᐧ1f0ccᐧ(ᐧ1d54aᐧ):
            return f'{start}{ᐧ2574ᐧ}{ᐧ2205ᐧ}'
        slns = start.split('\n')
        res, ml = ('\n'.join(slns[:-1]), ML((lne := slns[-1])))
        for i, z in ᐧ21a8ᐧ(ᐧ1d54aᐧ):
            l = (ᐧeba6ᐧ(z.P) if ᐹ(z, ᐧ1d40dᐧ) else ᐧ2218ᐧ(ᔐ, z)).split('\n')
            e = i == ᐧ1f0ccᐧ(ᐧ1d54aᐧ) - 1
            l[0] = (m1 if i else m0)[e] + l[0]
            l[1:] = ᴍ(l[1:], lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: m2[e] + x)
            l = ᴍ(l, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ml * ' ' + x)
            if not i:
                pre = f'{start}'
                l[0] = pre + ' ' * (ml - ML(pre)) + l[0][ml:]
            (res := (res + ('\n'.join(l) + (not e) * '\n')))
        return res

class Ń(ᐧ1d40dᐧ):

    def __init__(ᐧ1d54aᐧ, t, *c, e=ᐧ2400ᐧ):
        ᐧ1d54aᐧ.t, ᐧ1d54aᐧ.c, ᐧ1d54aᐧ.e = (t, not c and [] or ᐧ1d459ᐧ(c), ᐧ2135ᐧ[ᐧ25a1ᐧ] if e is ᐧ2400ᐧ else e)
    __repr__ = lambda ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: f'Ń⟨{ᐧ1d54aᐧ.t or '∅'}⟩⟨{ᐧ1d54aᐧ.e}⟩⟨{', '.join(ᴍ(ᐧ1d54aᐧ, ᔐ))}⟩'
    __setitem__ = lambda ᐧ1d54aᐧ, x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: setitem_ret_((þ0 := y), (þ1 := ᐧ1d54aᐧ.c), (þ2 := x), þ0)
    copy = lambda ᐧ1d54aᐧ, t=ᐧ25a1ᐧ, c=ᐧ25a1ᐧ, e=ᐧ2400ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐹ(NULL, ᐧ1d54aᐧ)(ᐧ1d54aᐧ.t if t is ᐧ25a1ᐧ else t, *(ᐧ1d54aᐧ.c if c is ᐧ25a1ᐧ else c), e=ᐧ1d54aᐧ.e if e is ᐧ2400ᐧ else e)
    rcopy = lambda ᐧ1d54aᐧ, t=ᐧ25a1ᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐹ(NULL, ᐧ1d54aᐧ)(ᐧ1d54aᐧ.t if t is ᐧ25a1ᐧ else t, *ᴍ(ᐧ1d54aᐧ.c, ᐹ(NULL, ᐧ1d54aᐧ).rcopy), e=ᐧ1d54aᐧ.e.copy()) if ᐹ(ᐧ1d54aᐧ, ᐧ1d40dᐧ) else ᐧ1d54aᐧ

    def frp(ᐧ1d54aᐧ, f, r, pre=ᐧ2717ᐧ):
        ᐧ1d4e1ᐧ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ꟿ(ᐧ21a8ᐧ(ᐧ1d54aᐧ), lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: setitem_ret_((þ0 := y.frp(f, r, pre)), (þ1 := ᐧ1d54aᐧ), (þ2 := x), þ0))
        if pre:
            ᐧeba6ᐧ(ᐧ1d4e1ᐧ)
        if ᐧ2218ᐧ(f, ᐧ1d54aᐧ):
            return r(ᐧ1d54aᐧ)
        if not pre:
            ᐧeba6ᐧ(ᐧ1d4e1ᐧ)
        return ᐧ1d54aᐧ
    ftrp = lambda ᐧ1d54aᐧ, fs, *ᐧ1d538ᐧ, not_T=ᐧ2713ᐧ, **ᐧ1d542ᐧ: ᐧ1d54aᐧ.frp(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.t in ᐧ1d460ᐧ(fs) and (not (not_T and ᐧ1d54aᐧ.e.T)), *ᐧ1d538ᐧ)
__exports__ = ('𝐍', 'Ń')

### peggle2
# ᐧf02faᐧ('𝐍', LITERAL_OPS_['*'])
import regex as re
from pickle import loads, dumps
show_cache_table = lambda ᐧ1d445ᐧ, ᐧ212dᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ꟿ(ᐧ21a8ᐧ(ᐧ212dᐧ), lambda i, v, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ꟿ(ᐧf04bcᐧ(ᐧ2135ᐧ(v) ** LITERAL_OPS_['*'], NULL), lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ263eᐧ(f'{i},{x}\t{ᐧ1d445ᐧ[x]}\t{y}')))
from time import time
ᐧ1d4fdᐧ_ = ᐧ25a1ᐧ

def ᐧ1d4e3ᐧ(s=ᐦ):
    return
    global ᐧ1d4fdᐧ_
    if ᐧ1d4fdᐧ_ is ᐧ25a1ᐧ:
        ᐧ263eᐧ(f'Starting timer')
        ᐧ1d4fdᐧ_ = ᐧeba6ᐧ(time)
        return
    ᐧ263eᐧ(f'{s} took {ᐧeba6ᐧ(time) - ᐧ1d4fdᐧ_}s')
    ᐧ1d4fdᐧ_ = ᐧ25a1ᐧ

def parse(ᐧ1d437ᐧ, ᐧ1d445ᐧ, start_rule=ᐧ25a1ᐧ):
    ᐧ212dᐧ, χ = (ᴍ(ᐧ2b65ᐧ(ᐧ1f0ccᐧ(ᐧ1d437ᐧ) + 1), lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: {}), 0)
    ᐧ1d4e2ᐧ = [(None, ᐧ1f0ccᐧ(ᐧ1d445ᐧ) - 1 if start_rule is None else start_rule)]
    χ = 0
    while ᐧ1d4e2ᐧ:
        Χ, ι = ᐧ1d4e2ᐧ.pop(-1)
        if Χ is not None:
            χ = Χ
        γ, *ᐧ1d436ᐧ = ᐧ1d445ᐧ[ι]
        ᐧ1d520ᐧ = ᐧ212dᐧ[χ]
        match γ:
            case 'ᔐ':
                if ᐧ1d436ᐧ[0] == ᐧ1d437ᐧ[χ:(ᐧ1d74cᐧ := (χ + len(ᐧ1d436ᐧ[0])))]:
                    ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, ᐧ1d74cᐧ)
                else:
                    ᐧ1d520ᐧ[ι] = (ᐧ2717ᐧ, χ)
            case '~':
                if (m := ᐧ1d436ᐧ[0].match(ᐧ1d437ᐧ, χ)):
                    ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, m.span()[1], m)
                else:
                    ᐧ1d520ᐧ[ι] = (ᐧ2717ᐧ, χ)
            case '∧':
                n, ᐧ1d74cᐧ = ᐧ1d520ᐧ[ι] if ι in ᐧ1d520ᐧ else (0, χ)
                while ᐧ2713ᐧ:
                    ᐧ1d73eᐧ, ᐧ1d450ᐧ = (ᐧ1d436ᐧ[n], ᐧ212dᐧ[ᐧ1d74cᐧ])
                    if ᐧ1d73eᐧ not in ᐧ1d450ᐧ:
                        ᐧ1d4e2ᐧ.extend([(χ, ι), (ᐧ1d74cᐧ, ᐧ1d73eᐧ)])
                        ᐧ1d520ᐧ[ι] = (n, ᐧ1d74cᐧ)
                        break
                    ᐧ1d454ᐧ, ᐧ1d74cᐧ = ᐧ212dᐧ[ᐧ1d74cᐧ][ᐧ1d73eᐧ][:2]
                    (n := (n + 1))
                    if not ᐧ1d454ᐧ:
                        ᐧ1d520ᐧ[ι] = (ᐧ2717ᐧ, χ)
                        break
                    if n == len(ᐧ1d436ᐧ):
                        ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, ᐧ1d74cᐧ)
                        break
            case '∨':
                n = ᐧ1d520ᐧ[ι] if ι in ᐧ1d520ᐧ else 0
                while ᐧ2713ᐧ:
                    ᐧ1d73eᐧ, ᐧ1d450ᐧ = (ᐧ1d436ᐧ[n], ᐧ212dᐧ[χ])
                    if ᐧ1d73eᐧ not in ᐧ1d450ᐧ:
                        ᐧ1d4e2ᐧ.extend([(χ, ι), (χ, ᐧ1d73eᐧ)])
                        ᐧ1d520ᐧ[ι] = n
                        break
                    ᐧ1d454ᐧ, ᐧ1d74cᐧ = ᐧ212dᐧ[χ][ᐧ1d73eᐧ][:2]
                    if ᐧ1d454ᐧ:
                        ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, ᐧ1d74cᐧ, n)
                        break
                    (n := (n + 1))
                    if n == len(ᐧ1d436ᐧ):
                        ᐧ1d520ᐧ[ι] = (ᐧ2717ᐧ, χ)
                        break
            case '*' | '+':
                if ι in ᐧ1d520ᐧ:
                    c = ᐧ1d520ᐧ[ι]
                else:
                    c = ᐧ1d520ᐧ[ι] = [χ]
                ᐧ1d73eᐧ, ᐧ1d74cᐧ = (ᐧ1d436ᐧ[0], c[-1])
                while ᐧ2713ᐧ:
                    ᐧ1d450ᐧ = ᐧ212dᐧ[ᐧ1d74cᐧ]
                    if ᐧ1d73eᐧ not in ᐧ1d450ᐧ:
                        ᐧ1d4e2ᐧ.extend([(χ, ι), (ᐧ1d74cᐧ, ᐧ1d73eᐧ)])
                        break
                    ᐧ1d454ᐧ, Χ = ᐧ1d450ᐧ[ᐧ1d73eᐧ][:2]
                    if not ᐧ1d454ᐧ:
                        if γ == '*' or len(c) > 1:
                            ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, ᐧ1d74cᐧ, c[:-1])
                        else:
                            ᐧ1d520ᐧ[ι] = (ᐧ2717ᐧ, χ)
                        break
                    c.append((ᐧ1d74cᐧ := Χ))
            case '✓':
                ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, χ)
            case '✗':
                assert ᐧ2717ᐧ, ᐧ2a33ᐧ(NULL, f'Hit an ✗')
            case '←':
                if ᐧ1d436ᐧ[1] not in ᐧ1d520ᐧ:
                    ᐧ1d4e2ᐧ.extend([(χ, ι), (χ, ᐧ1d436ᐧ[1])])
                else:
                    ᐧ1d454ᐧ, ᐧ1d74cᐧ = ᐧ1d520ᐧ[ᐧ1d436ᐧ[1]][:2]
                    ᐧ1d520ᐧ[ι] = (ᐧ1d454ᐧ, ᐧ1d74cᐧ, ᐧ1d436ᐧ[1])
            case _:
                if ᐧ1d436ᐧ[0] not in ᐧ1d520ᐧ:
                    ᐧ1d4e2ᐧ.extend([(χ, ι), (χ, ᐧ1d436ᐧ[0])])
                else:
                    ᐧ1d454ᐧ, ᐧ1d74cᐧ = ᐧ1d520ᐧ[ᐧ1d436ᐧ[0]][:2]
                    match γ:
                        case '⮞':
                            ᐧ1d520ᐧ[ι] = (ᐧ1d454ᐧ, χ)
                        case '¬':
                            ᐧ1d520ᐧ[ι] = (not ᐧ1d454ᐧ, χ)
                        case '❗':
                            assert ᐧ1d454ᐧ
                            ᐧ1d520ᐧ[ι] = (ᐧ1d454ᐧ, ᐧ1d74cᐧ)
                        case '?':
                            ᐧ1d520ᐧ[ι] = (ᐧ2713ᐧ, ᐧ1d74cᐧ, ᐧ1d454ᐧ)
                        case _:
                            ᐧ1d520ᐧ[ι] = (ᐧ1d454ᐧ, ᐧ1d74cᐧ)
    return ᐧ212dᐧ

def make_rules(r):
    nmp = ᐧ2135ᐧ(ζ(r ** LITERAL_OPS_['-'], ᐧ2b65ᐧ(r)))
    r = ꟿ['K'](r, lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: '_' + x)
    ᐧ1d402ᐧ = ᐧ2135ᐧ(ζ(r ** LITERAL_OPS_['-'], (ᐧ1d411ᐧ := ᴍ(r ** LITERAL_OPS_['-'], ᐧ26f6ᐧ['T']))))

    def ᐧ1d54aᐧ(r):
        if ᐧ1f0ccᐧ(r) == 1 and r[0][0] == '_':
            return (r[0],)
        if r in ᐧ1d402ᐧ:
            return ᐧ1d402ᐧ[r]
        if ᐹ(r[0], ᐧ1d456ᐧ):
            r = (ᐧ1d411ᐧ[(ᐧ1d526ᐧ := r[0])][0], *r[1:])
        else:
            ᐧ1d411ᐧ.append((ᐧ1d526ᐧ := ᐧ1f0ccᐧ(ᐧ1d411ᐧ)))
        if r[0] == '←':
            r = (r[0], r[1], ᐧ1d54aᐧ(r[2]))
        elif r[0] in '✓✗':
            r = (r[0], ᐧ1d526ᐧ)
        elif r[0] not in 'ᔐ~':
            r = (r[0], *ᴍ(r[1:], ᐧ1d54aᐧ))
        ᐧ1d411ᐧ[setitem_ret_((þ0 := ᐧ1d526ᐧ), (þ1 := ᐧ1d402ᐧ), (þ2 := r), þ0)] = r
        return ᐧ1d526ᐧ
    ᐧ1d54aᐧ(('T_root', *ᴍ(ζ(nmp ** LITERAL_OPS_['+'], r ** LITERAL_OPS_['+']), ᐧ1d461ᐧ)))
    ᐧ1d411ᐧ = ᴍ(ᐧ1d411ᐧ, lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (x[0], *ᴍ(x[1:], lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧf0445ᐧ['I'](r ** LITERAL_OPS_['-'], ᐧf41eᐧ(LITERAL_OPS_['=='])(x[0])) if ᐹ(x, ᐧ1d461ᐧ) else x)))
    return ᐧ2135ᐧ[ᐧ1d411ᐧ] | nmp

def parse_to_tree(ᐧ1d445ᐧ, ᐧ212dᐧ, χ, ι, show_table=ᐧ2717ᐧ, raise_failed=ᐧ2713ᐧ):
    rec = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: parse_to_tree(ᐧ1d445ᐧ, ᐧ212dᐧ, *ᐧ1d538ᐧ, raise_failed=raise_failed)
    γ, *C = ᐧ1d445ᐧ[ι]
    if ι not in (ᐧ1d520ᐧ := ᐧ212dᐧ[χ]):
        return (γ, f'‼∄‼')
    ᐧ1d454ᐧ, ᐧ1d74cᐧ, *ᐧ1d434ᐧ = ᐧ1d520ᐧ[ι]
    if raise_failed:
        ᐧ2a33ᐧ(ᐧ1d454ᐧ, f'Failed to parse tree!')
    if γ == '∧':
        o = []
        for r in C:
            o.append(rec(χ, r))
            if r not in (ᐧ1d520ᐧ := ᐧ212dᐧ[χ]):
                break
            χ = ᐧ1d520ᐧ[r][1]
        return (γ, *o)
    if γ == 'ᔐ':
        return (γ, C[0])
    if γ == '?':
        return (γ, *(ᐧ1d434ᐧ and (ᐧ1d434ᐧ[0] and ᐧ26f6ᐧ['T'](rec(χ, C[0]))) or ()))
    if not ᐧ1d434ᐧ and γ in {*'∨*+~←'}:
        return (γ, f'‼∅‼')
    if γ == '~':
        return (γ, ᐧ1d434ᐧ[0].group(0))
    if γ == '∨':
        return (γ, rec(χ, C[ᐧ1d434ᐧ[0]]))
    if γ == '←':
        return (γ, C[0], rec(χ, ᐧ1d434ᐧ[0]))
    if γ in {*'*+'}:
        return (γ, *(rec(x, C[0]) for x in ᐧ1d434ᐧ[0]))
    if γ in {*'✓✗⮞¬'}:
        return (γ,)
    return (γ.removeprefix('_'), rec(χ, C[0]))

def chop_tree(ᐧf1055ᐧ, ᐧ1d437ᐧ, remove_trashes=ᐧ2713ᐧ, remove_failed_questions=ᐧ2713ᐧ, remove_lookaheads=ᐧ2713ᐧ):
    pops = f'∧∨*+❗⠶?'
    removes = ᐧ1d460ᐧ('\U000f01b4' * remove_trashes + '⮞¬' * remove_lookaheads)

    def reform_str(ᐧf1055ᐧ):
        if ᐧf1055ᐧ.t == 'ᔐ' or ᐧf1055ᐧ.t == '~':
            ᐧf1055ᐧ.t, ᐧf1055ᐧ.c, ᐧf1055ᐧ.e.T = (ᐧf1055ᐧ.c[0].t, [], ᐧ2713ᐧ)
        else:
            for c in ᐧf1055ᐧ:
                reform_str(c)
        return ᐧf1055ᐧ
    ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
    reform_str(ᐧf1055ᐧ)
    ᐧ1d4e3ᐧ('Reform_str')

    def ƒ(ᐧf1055ᐧ):
        if ᐧf1055ᐧ.e.T:
            return True
        if ᐧf1055ᐧ.t in removes:
            return
        if remove_failed_questions and ᐧf1055ᐧ.t == '?':
            if not ᐧf1055ᐧ.c:
                return
            ᐧf1055ᐧ.c = list(filter(ƒ, ᐧf1055ᐧ.c))
            if not ᐧf1055ᐧ.c:
                return
            return True
        ᐧf1055ᐧ.c = list(filter(ƒ, ᐧf1055ᐧ.c))
        return True
    ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
    ƒ(ᐧf1055ᐧ)
    ᐧ1d4e3ᐧ('Removes')

    def splat(ᐧf1055ᐧ):
        C = []
        for c in ᐧf1055ᐧ:
            if c.e.T:
                C.append(c)
                continue
            v = splat(c)
            if isinstance(v, list):
                C.extend(v)
            elif c.t in pops:
                if c.t == '⠶':
                    for l in c:
                        C.extend(l.c)
                else:
                    C.extend(c.c)
            else:
                C.append(c)
        ᐧf1055ᐧ.c = C
    ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
    splat(ᐧf1055ᐧ)
    ᐧ1d4e3ᐧ('Splats')

    def get_txt(ᐧf1055ᐧ):
        if ᐧf1055ᐧ.t == 'ƨ':
            l = ''

            def ƒ(ᐧf1055ᐧ):
                nonlocal l
                if ᐧf1055ᐧ.e.T:
                    (l := (l + ᐧf1055ᐧ.t))
                else:
                    for c in ᐧf1055ᐧ:
                        ƒ(c)
            ƒ(ᐧf1055ᐧ)
            ᐧf1055ᐧ.t, ᐧf1055ᐧ.c, ᐧf1055ᐧ.e = (l, [], ᐧ2135ᐧ(T=ᐧ2713ᐧ))
            return
        for c in ᐧf1055ᐧ:
            get_txt(c)
    ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
    get_txt(ᐧf1055ᐧ)
    ᐧ1d4e3ᐧ('Get_txt')

    def set_arrows(ᐧf1055ᐧ):
        if ᐧf1055ᐧ.e.T:
            return
        for i, c in ᐧ21a8ᐧ(ᐧf1055ᐧ):
            if c.e.T:
                continue
            if c.t == '←':
                ᐧf1055ᐧ.e[c[0].t] = ᐧf1055ᐧ[i] = c[1]
            set_arrows(c)
    ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
    set_arrows(ᐧf1055ᐧ)
    ᐧ1d4e3ᐧ('Set arrows')
    return ᐧf1055ᐧ

def parse_to_node(ᐧf1055ᐧ):

    def ƒ(x, *ᐧ1d538ᐧ):
        return Ń(x, *(ƒ(*(x if isinstance(x, tuple) else (x,))) for x in ᐧ1d538ᐧ))
    return ƒ(*ᐧf1055ᐧ)

class Peggle2:
    __slots__ = ᐧ236dᐧ(f'rules\u2009R')

    def __init__(ᐧ1d54aᐧ, g):
        ᐧ1d54aᐧ.rules, ᐧ1d54aᐧ.R = ᐧ22c4ᐧ(g.rules, g.R) if ᐹ(g, Peggle2) else ᐧ22c4ᐧ(g, make_rules(g))

    def __repr__(ᐧ1d54aᐧ):
        return f'{ᐹ(NULL, ᐧ1d54aᐧ).__name__}[{ᐧ1f0ccᐧ(ᐧ1d54aᐧ.rules)} Rules, {ᐧ1f0ccᐧ(ᐧ1d54aᐧ.R.T_root)} Normalized]'

    def __contains__(ᐧ1d54aᐧ, x):
        return x in ᐧ1d54aᐧ.rules

    def __or__(ᐧ1d54aᐧ, h, allow_conflict=ᐧ2717ᐧ):
        if ᐹ(h, ᐧ1d54aᐧ):
            h = h.rules
        conflict = ᐧ2229ᐧ(ᐧeba6ᐧ(ᐧ1d54aᐧ.rules.keys), ᐧeba6ᐧ(h.keys))
        ᐧ2a33ᐧ(not (allow_conflict and conflict), f'Conflicting rules! {conflict}')
        return ᐹ(NULL, ᐧ1d54aᐧ)(Peggle2(ᐧ1d54aᐧ.rules | h))

    def __call__(ᐧ1d54aᐧ, content, rule='main', DEBUG=ᐧ2717ᐧ, chop=ᐧ2713ᐧ, **ᐧ1d4daᐧ):
        ᐧ2a33ᐧ(not DEBUG, 'Not implemented.')
        c, r = (content, rule)
        root, rule = (ᐧ1d54aᐧ.R.T_root, ᐧ1d54aᐧ.R[r])
        ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
        ᐧ212dᐧ = parse(c, root, rule)
        ᐧ1d4e3ᐧ('Parse')
        ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
        ᐧf1055ᐧ = parse_to_tree(root, ᐧ212dᐧ, 0, rule)
        ᐧ1d4e3ᐧ('Convert')
        ᐧeba6ᐧ(ᐧ1d4e3ᐧ)
        ᐧf1055ᐧ = parse_to_node(ᐧf1055ᐧ)
        ᐧ1d4e3ᐧ('Nodeing')
        ᐧ1d4b8ᐧ = lambda *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: chop_tree(ᐧf1055ᐧ, c, **ᐧ1d4daᐧ | ᐧ1d542ᐧ)
        return ᐧeba6ᐧ(ᐧ1d4b8ᐧ) if chop else ᐧ2135ᐧ(table=ᐧ212dᐧ, tree=ᐧf1055ᐧ, chop=ᐧ1d4b8ᐧ)

    def print_rules(ᐧ1d54aᐧ):
        ꟿ(ᐧeba6ᐧ(ᐧ1d54aᐧ.rules.items), lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (ᐧ263eᐧ(f'{x}:'), ᐧ263eᐧ(y)))

    def print_normalized(ᐧ1d54aᐧ):
        ꟿ(ᐧ21a8ᐧ(ᐧ1d54aᐧ.R.T_root), lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ᐧ263eᐧ(f'{x}\t{' '.join(ᴍ(y, ᔐ))}'))
GRANDMA_RULES = ᐧ25baᐧ((ŕ := (*map(re.compile, ('[\ueb26#][^\\n]*', '[⯅⯆△▽↷]', '"(␛.|[^"])*"', "'(␛.|[^'])*'", '‹(␛.|[^›])*›', '[^⯅⯆△▽↷\U000f01b4()?❗⮞.:⠶ƨ✗+*=¬∨∧~‹#\ueb26\'" \\t\\n]+|✗', '[\U000f01b4❗⮞⠶ƨ~¬]', '[*+?]', '([ \\t]|␛\\n)+', '([ \\t\\n]|␛\\n)+')),)), ᐧ2218ᐧ(ᐧ2135ᐧ, {'statements': ('∨', ('∧', ('?', ('_W',)), ('*', ('∧', ('∨', ('_comment',), ('_elm_o',)), ('?', ('_W',)))))), 'comment': ('∨', ('~', ŕ[0])), 'elm_o': ('∨', ('∧', ('_elm_a',), ('*', ('∧', ('?', ('_W',)), ('ᔐ', '∨'), ('?', ('_W',)), ('_elm_a',))))), 'elm_a': ('∨', ('∧', ('_elm_j',), ('*', ('∧', ('∨', ('∧', ('?', ('_W',)), ('ᔐ', '∧'), ('?', ('_W',))), ('?', ('_w',))), ('_elm_j',))))), 'elm_j': ('∨', ('__elm_j',), ('_elm',)), '_elm_j': ('∨', ('∧', ('_elm',), ('?', ('_W',)), ('~', ŕ[1]), ('?', ('_W',)), ('∨', ('__elm_j',), ('_elm',)))), 'elm': ('∨', ('∧', ('_prefix',), ('∨', ('_assign_eql',), ('_assign_cln',), ('_group',), ('_str',), ('_rname',)), ('_suffix',))), 'assign_eql': ('∨', ('∧', ('_rname',), ('?', ('_W',)), ('ᔐ', '='), ('?', ('_W',)), ('_elm_o',))), 'assign_cln': ('∨', ('∧', ('_rname',), ('?', ('_W',)), ('ᔐ', ':'), ('?', ('_W',)), ('_elm_j',))), 'group': ('∨', ('∧', ('ᔐ', '('), ('?', ('_W',)), ('_group_inner',), ('ᔐ', ')'))), 'group_inner': ('∨', ('*', ('∧', ('_elm_o',), ('?', ('_W',))))), 'str1': ('∨', ('~', ŕ[2])), 'str2': ('∨', ('~', ŕ[3])), 'str3': ('∨', ('~', ŕ[4])), 'str': ('∨', ('_str1',), ('_str2',), ('_str3',)), 'rname': ('∨', ('~', ŕ[5])), 'prefix': ('∨', ('∧', ('?', ('_w',)), ('+', ('∧', ('~', ŕ[6]), ('?', ('_W',))))), ('?', ('_w',))), 'suffix': ('∨', ('∧', ('+', ('∧', ('?', ('_W',)), ('~', ŕ[7]))), ('?', ('_w',))), ('?', ('_w',))), 'w': ('∨', ('~', ŕ[8])), 'W': ('∨', ('~', ŕ[9]))}))
BOOTSTRAP = Peggle2(GRANDMA_RULES)
__exports__ = ('Peggle2',)
if __name__ == '__main__':
    RULE = 'statements'
    CONTENT = '\n    main    = \U000f01b4W? (entry \U000f01b4W?)*\n    entry   = (\n        ƨ(section=\U000f01b4\'[\' wrd \U000f01b4\']\') \U000f01b4W?\n        (pair = (\n            (bruh:key = ⠶wrd) \U000f01b4(w? ↷ \'=\')\n            (value = (wrd ∨ str)+) \U000f01b4W? ) )* )\n    str     = ~‹"[^"]+"›\n    wrd     = ~‹[-\\w]+›\n    w       = ~‹[ \\t]+›\n    W       = ~‹[ \\t\\n]+›\n    ' * 2
    ᐧ263eᐧ(BOOTSTRAP)
    ᐧf1055ᐧ = BOOTSTRAP(CONTENT, RULE)
    ᐧ263eᐧ('FINISHED')
    ᐧ263eᐧ(ᐧeba6ᐧ(ᐧf1055ᐧ.P))

def Peggle1Bootstrap(c=ᐧ2135ᐧ()):
    if 'BOOTSTRAP_PEGGLE1' in c:
        return (c.ForcefeedPeggle1Peggle2, c.BOOTSTRAP_PEGGLE1)

    def peggle122(rules):

        def ƒ(x):
            if x.t == '←':
                return (x.t, x[0].c, ƒ(x[1]))
            if x.t == 'rname':
                return ('_' * (x.c not in '✓✗') + x.c,)
            return (x.t, *(ᴍ(x.c, ƒ) if x.L else (x.c,)))
        return ꟿ['V'](ᐧ2135ᐧ(rules), lambda x, y, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: ƒ(y))

    def peggle221(ᐧf1055ᐧ):
        from node import Node

        def ƒ(ᐧf1055ᐧ):
            s = ᐧ2135ᐧ()
            for k, v in ᐧf1055ᐧ.e:
                if k == 'T':
                    return Node(c=ᐧf1055ᐧ.t)
                s[ᐧf1055ᐧ.c.index(v)] = k
            c = ᴍ(ᐧf1055ᐧ, ƒ)
            for i, v in s:
                c[i].e = v
            return Node(ᐧf1055ᐧ.t, c)
        return ƒ(ᐧf1055ᐧ).find_replace(lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: (ᐧ1f0ccᐧ(x) == 1 and ᐹ(x.c[0], Node)) and (not x.c[0].t), lambda x, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ: x.copy(c=x.txt))

    class ForcefeedPeggle1Peggle2(Peggle2):

        def __init__(ᐧ1d54aᐧ, x):
            if ᐹ(x, Peggle2):
                super().__init__(x)
            else:
                super().__init__(peggle122(x))

        def __call__(ᐧ1d54aᐧ, *ᐧ1d538ᐧ, **ᐧ1d542ᐧ):
            return peggle221(super().__call__(*ᐧ1d538ᐧ, **ᐧ1d542ᐧ))

        def __or__(ᐧ1d54aᐧ, x):
            return super().__or__(peggle122(x))

        def dump_gram(ᐧ1d54aᐧ):
            return dumps((ᐧ2218ᐧ(ᐧ1d451ᐧ, ᐧ1d54aᐧ.rules), ᐧ2218ᐧ(ᐧ1d451ᐧ, ᐧ1d54aᐧ.R), ᐧeba6ᐧ(ᐧ1d54aᐧ.R.getdef)))

        @ᐧ1d49eᐧᐧ2133ᐧ
        def load_gram(ᐧ2102ᐧ, gram):
            ᐧ1d54aᐧ = ᐧ2102ᐧ.__new__(ᐧ2102ᐧ)
            rules, R, d = loads(gram)
            ᐧ1d54aᐧ.rules, ᐧ1d54aᐧ.R = (ᐧ2135ᐧ(rules), ᐧ2135ᐧ[d](R))
            return ᐧ1d54aᐧ
    c.ForcefeedPeggle1Peggle2 = ForcefeedPeggle1Peggle2
    c.BOOTSTRAP_PEGGLE1 = ForcefeedPeggle1Peggle2(BOOTSTRAP)
    return (c.ForcefeedPeggle1Peggle2, c.BOOTSTRAP_PEGGLE1)