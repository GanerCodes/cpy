import util

#################### HEADER ####################
from math import *
del factorial, e, pi, tau, sqrt, cbrt, pow
thr1d45cthr, thr1d451thr, thr1d44fthr, thr1d459thr, thr1d461thr, thr1d460thr, ᔐ, thr1d456thr, thr1d453thr = (object, dict, bool, list, tuple, set, str, int, float)
from py_naming_tools import py_escape_var as PEV
from functools import reduce
from itertools import starmap, filterfalse, product, accumulate, zip_longest
LITERAL_OPS_ = {'∧': lambda x, y, *thr1d538thr, **thr1d542thr: x and y, '∨': lambda x, y, *thr1d538thr, **thr1d542thr: x or y, '*': lambda x, y, *thr1d538thr, **thr1d542thr: x * y, '/': lambda x, y, *thr1d538thr, **thr1d542thr: x / y, '<': lambda x, y, *thr1d538thr, **thr1d542thr: x < y, '>': lambda x, y, *thr1d538thr, **thr1d542thr: x > y, '|': lambda x, y, *thr1d538thr, **thr1d542thr: x | y, '&': lambda x, y, *thr1d538thr, **thr1d542thr: x & y, '^': lambda x, y, *thr1d538thr, **thr1d542thr: x ^ y, '%': lambda x, y, *thr1d538thr, **thr1d542thr: x % y, '==': lambda x, y, *thr1d538thr, **thr1d542thr: x == y, '!=': lambda x, y, *thr1d538thr, **thr1d542thr: x != y, '<=': lambda x, y, *thr1d538thr, **thr1d542thr: x <= y, '>=': lambda x, y, *thr1d538thr, **thr1d542thr: x >= y, '//': lambda x, y, *thr1d538thr, **thr1d542thr: x // y, '**': lambda x, y, *thr1d538thr, **thr1d542thr: x ** y, '<<': lambda x, y, *thr1d538thr, **thr1d542thr: x << y, '>>': lambda x, y, *thr1d538thr, **thr1d542thr: x >> y, '+': lambda *thr1d538thr, **thr1d542thr: +thr1d538thr[v] if thr1d538thr[(v := 0)] is thr2400thr or thr1d538thr[(v := 1)] is thr2400thr else thr1d538thr[0] + thr1d538thr[1], '-': lambda *thr1d538thr, **thr1d542thr: -thr1d538thr[v] if thr1d538thr[(v := 0)] is thr2400thr or thr1d538thr[(v := 1)] is thr2400thr else thr1d538thr[0] - thr1d538thr[1], 'not': lambda x, *thr1d538thr, **thr1d542thr: not x, 'is': lambda x, y, *thr1d538thr, **thr1d542thr: x is y, 'is not': lambda x, y, *thr1d538thr, **thr1d542thr: x is not y, 'in': lambda x, y, *thr1d538thr, **thr1d542thr: x in y, 'not in': lambda x, y, *thr1d538thr, **thr1d542thr: x not in y}
thrSTACK = []
GETATTR = lambda x, y, *thr1d538thr, **thr1d542thr: getattr(x, y)
SETATTR = lambda x, y, z, *thr1d538thr, **thr1d542thr: setattr(x, y, z) or z
GETITEM = lambda x, y, *thr1d538thr, **thr1d542thr: x.__getitem__(y)
SETITEM = lambda x, y, z, *thr1d538thr, **thr1d542thr: x.__setitem__(y, z) or z
thrPSH, thrPOP = (lambda x, *thr1d538thr, **thr1d542thr: thrSTACK.append(x) or x, lambda x, *thr1d538thr, **thr1d542thr: thrSTACK.pop(x))
OP_DUPER_ = lambda thrf, *thr1d538thr, **thr1d542thr: lambda x, *thr1d538thr, **thr1d542thr: thrf(x, x, *thr1d538thr, **thr1d542thr)
OP_SWAPA_ = lambda thrf, *thr1d538thr, **thr1d542thr: lambda x, y, *thr1d538thr, **thr1d542thr: thrf(y, x, *thr1d538thr, **thr1d542thr)
OP_LNULL_ = lambda thrf, *thr1d538thr, **thr1d542thr: lambda x, *thr1d538thr, **thr1d542thr: thrf(thr2400thr, x, *thr1d538thr, **thr1d542thr)
OP_RNULL_ = lambda thrf, *thr1d538thr, **thr1d542thr: lambda x, *thr1d538thr, **thr1d542thr: thrf(x, thr2400thr, *thr1d538thr, **thr1d542thr)
OP_BSTAR_ = lambda thrf, *thr1d538thr, **thr1d542thr: lambda x, *thr1d538thr, **thr1d542thr: thrf(*x, *thr1d538thr, **thr1d542thr)
NOOOL = thr2400thr = thr1d45cthr()
thr2713thr, thr2717thr = (True, False)
thr1d49ethrthr2133thr, thr1d4aethrthr2133thr, thr1d5d9thr = (classmethod, staticmethod, callable)
ᗜ = thr25a1thr = None
thrpi = 3.141592653589793
thr2107thr = 2.718281828459045
thrimag = complex(0, 1)
thr2189thr = 0
thr00bdthr, thr2153thr, thr00bcthr, thr2155thr, thr2159thr, thr2150thr, thr215bthr, thr2151thr, thr2152thr = (1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9, 1 / 10)
thr2154thr, thr2156thr = (2 / 3, 2 / 5)
thr00bethr, thr2157thr, thr215cthr = (3 / 4, 3 / 5, 3 / 8)
thr2158thr = 4 / 5
thr215athr, thr215dthr = (5 / 6, 5 / 8)
thr215ethr = 7 / 8
thr221ethr, ᐦ, τ, thrf7e8dthr = (inf, '', 2 * thrpi, thr00bdthr * thrpi)
thrf7c6athr, thrf7c6bthr, thrf7c6cthr, thrf7c6dthr, thrf7c6ethr = (-thrimag, -thr2107thr, -τ, -thrpi, -thrf7e8dthr)
thr1d55dthr, thr1d563thr = (lambda x, *thr1d538thr, **thr1d542thr: [*thr1d538thr] if x is thr2400thr else [x], lambda x, *thr1d538thr, **thr1d542thr: thrf0233thr(x, lambda x, *thr1d538thr, **thr1d542thr: x is thr2400thr))
thr1d5dcthr = is_iter = lambda x, *thr1d538thr, **thr1d542thr: hasattr(x, '__iter__')

class thr1d450thrthr1d451thr(thr1d451thr):

    def __init__(thr1d54athr, thrf, *thr1d538thr, thr1d454thr=thr25a1thr, **thr1d542thr):
        thr1d54athr.thrf, thr1d54athr.thr1d454thr = (thrf, thr1d454thr)
        super().__init__(*thr1d538thr, **thr1d542thr)
    __call__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr1d54athr.thrf(*thr1d538thr, **thr1d542thr)
    __repr__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr1d54athr['__repr__'](thr1d54athr) if '__repr__' in thr1d54athr else super().__repr__()
    __getitem__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: super().__getitem__(x) if x in thr1d54athr else thr1d54athr.thr1d454thr(x)

def BINWRAP_(thrf):

    class ω:

        def __call__(thr1d54athr, x=thr2400thr, y=thr2400thr, **thr1d542thr):
            if x is thr2400thr:
                x, y = (y, x)
            if y is thr2400thr:
                return thrf(x, **thr1d542thr)
            return thrf(x, y, **thr1d542thr)
        __getitem__ = lambda thr1d54athr, s, *thr1d538thr, **thr1d542thr: lambda *thr1d538thr, **thr1d542thr: thr1d54athr(*thr1d538thr, s=s, **thr1d542thr)
    return ω()
thr2b24thr = thr1d45cthr()

def thrf41ethr(thrf):

    def thr1d4bbthr(*thr1d736thr, **thr1d73fthr):

        def thr1d453thr(*thr1d538thr, **thr1d542thr):
            thr1d4d0thr, thr1d538thr = (thr1d459thr(thr1d736thr), thr1d459thr(thr1d538thr))
            thr1d4dathr = thr1d459thr(thr1d73fthr.items())
            a, k = ([], {})
            while thr1d4d0thr:
                x = thr1d4d0thr.pop(0)
                a.append(thr1d538thr.pop(0) if x == thr2b24thr else x)
            while thr1d4dathr:
                x, y = thr1d4dathr.pop(0)
                k[x] = thr1d538thr.pop(0) if y == thr2b24thr else y
            return thrf(*a + thr1d538thr, **k | thr1d542thr)
        return thr1d453thr
    return thr1d4bbthr
thrf005thr = thr1d450thrthr1d451thr((t := (lambda thrf, *thr1d538thr, **thr1d542thr: lambda *thr1d538thr, **thr1d542thr: thrf(*Σ(ᴍ(thr1d538thr, thr1d459thr), []), **thr1d542thr))), thr1d454thr=t)

class ⴳ(thr1d456thr):
    __new__ = lambda thr2102thr, *thr1d538thr, **thr1d542thr: thr1d456thr.__new__(thr2102thr, 1)
    __call__, __repr__ = (lambda *thr1d538thr, **thr1d542thr: ⴳ, lambda thr1d54athr, *thr1d538thr, **thr1d542thr: 'ⴳ')

class ⴴ(thr1d456thr):
    __new__ = lambda thr2102thr, *thr1d538thr, **thr1d542thr: thr1d456thr.__new__(thr2102thr, 0)
    __call__, __repr__ = (lambda *thr1d538thr, **thr1d542thr: ⴴ, lambda thr1d54athr, *thr1d538thr, **thr1d542thr: 'ⴴ')
ⴳ, ⴴ = (ⴳ(), ⴴ())

def ERROR_TRIANGLE(t, thrf=thr2400thr, thr1d454thr=thr2400thr, thr1d447thr=Exception):
    v = thr1d563thr((thrf, thr1d454thr))
    if thr1f0ccthr(v) == 1:
        v = v[0]
        if t == '\uf071':
            raise v

        def r(*thr1d538thr, **thr1d542thr):
            try:
                return v(*thr1d538thr, **thr1d542thr)
            except thr1d447thr as ε:
                if t == '\U000f0536':
                    return thr1d538thr[0] if thr1d538thr else thr25a1thr
                if t == '\uea6c':
                    return ε
    else:

        def r(*thr1d538thr, **thr1d542thr):
            try:
                return thrf(*thr1d538thr, **thr1d542thr)
            except thr1d447thr as ε:
                if t == '\uf071':
                    return thr1d454thr
                if t == '\U000f0536':
                    return thr1d454thr(*thr1d538thr, **thr1d542thr)
                if t == '\uea6c':
                    return thr1d454thr(ε)
    return r
thrf071thr = thr1d450thrthr1d451thr((thrf := thrf41ethr(ERROR_TRIANGLE)('\uf071')), thr1d454thr=lambda x, *thr1d538thr, **thr1d542thr: thrf41ethr(thrf)(thr1d447thr=x))
thrf0536thr = thr1d450thrthr1d451thr((thrf := thrf41ethr(ERROR_TRIANGLE)('\U000f0536')), thr1d454thr=lambda x, *thr1d538thr, **thr1d542thr: thrf41ethr(thrf)(thr1d447thr=x))
threa6cthr = thr1d450thrthr1d451thr((thrf := thrf41ethr(ERROR_TRIANGLE)('\uea6c')), thr1d454thr=lambda x, *thr1d538thr, **thr1d542thr: thrf41ethr(thrf)(thr1d447thr=x))

def _get_depths(x):
    if not thr1d5dcthr(x):
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
    return [_map_pos_d(z, y, i - 1) for z in x] if thr1d5dcthr(x) else y(x)

def _map_d(x, y, n=1):
    if n < 0:
        return _map_neg_d(x, y, -n - 1)
    return _map_pos_d(x, y, 2 ** 24 if n == thr221ethr else n)

def _window(thr1d54fthr, l=1, r=1, m=thr2713thr, s=thr25a1thr, thrdelta=1):
    (c := thr1f0ccthr((thr1d54fthr := thr1d459thr(thr1d54fthr))))
    if s is thr2400thr:
        return ᴍ(thr2b65thr(thr1d54fthr)[l:c - r:thrdelta], lambda x, *thr1d538thr, **thr1d542thr: thr1d54fthr[x - l:x] + thr26f6thr(thr1d54fthr[x]) * thr1d44fthr(m) + thr1d54fthr[x + 1:x + r + 1])
    V = thr26f6thr(s) * l + thr1d54fthr + thr26f6thr(s) * r
    return ᴍ(thr2b65thr(thr1d54fthr)[::thrdelta], lambda x, *thr1d538thr, **thr1d542thr: V[x:x + l] + thr26f6thr(V[x + l]) * thr1d44fthr(m) + V[x + l + 1:x + l + r + 1])

class thr1d44fthrthr1d454thr:
    __getitem__ = lambda thr1d54athr, z, *thr1d538thr, **thr1d542thr: lambda x, y, *thr1d538thr, **thr1d542thr: thr1d54athr.thrf(x, y, z)
    __call__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr1d54athr.thrf(*thr1d538thr)

class thr017fthr(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: reduce(y, x, *(z,) * (z is not thr2400thr)))

class Ϝ(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: thr1d459thr(accumulate(x, y, **{} if z == thr2400thr else {'initial': z})))

class ᙎ(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: _window((h := thr1d563thr(thr22c4thr(x, y)))[0], *(ᐹ(y, thr1d456thr) and thr22c4thr(y, y) or y if thr1f0ccthr(h) == 2 else thr22c4thr(1, 1)), thr2717thr, thr25a1thr if z is thr2400thr else z, 1))

class ᙡ(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: _window((h := thr1d563thr(thr22c4thr(x, y)))[0], *(ᐹ(y, thr1d456thr) and thr22c4thr(y, y) or y if thr1f0ccthr(h) == 2 else thr22c4thr(1, 1)), thr2713thr, thr25a1thr if z is thr2400thr else z, 1))

class ᗢ(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: _window((h := thr1d563thr(thr22c4thr(x, y)))[0], *(ᐹ(y, thr1d456thr) and thr22c4thr(y, y) or y if thr1f0ccthr(h) == 2 else z is thr2400thr and thr22c4thr(1, 1) or thr22c4thr(0, z)), thr2717thr, thr2400thr, z is thr2400thr and 1 or z + 1))

class ᙧ(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: _window((h := thr1d563thr(thr22c4thr(x, y)))[0], *(ᐹ(y, thr1d456thr) and thr22c4thr(y, y) or y if thr1f0ccthr(h) == 2 else z is thr2400thr and thr22c4thr(1, 1) or thr22c4thr(0, z)), thr2713thr, thr2400thr, z is thr2400thr and 1 or z + 1))

class thrf0e35thr(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: ᴍ(thr2b65thr(l), ⴴ if z is thr2400thr else z if thr1d5d9thr(z) else lambda *thr1d538thr, **thr1d542thr: z) + x if (l := (y - thr1f0ccthr(x))) > 0 else x)

class thrf0e37thr(thr1d44fthrthr1d454thr):
    thrf = thr1d4aethrthr2133thr(lambda x, y, z=thr2400thr, *thr1d538thr, **thr1d542thr: x + ᴍ(thr2b65thr(l), ⴴ if z is thr2400thr else z if thr1d5d9thr(z) else lambda *thr1d538thr, **thr1d542thr: z) if (l := (y - thr1f0ccthr(x))) > 0 else x)

class ᴍ:
    thrf = thr1d4aethrthr2133thr(_map_d)

    def __getitem__(thr1d54athr, i):
        S, thrf = (thr1d460thr(i if ᐹ(i, thr1d461thr) else (i,)), thr25a1thr)
        if (s := 'D') in S:
            thrf = lambda f, *thr1d538thr, **thr1d542thr: lambda x, y, *thr1d538thr, **thr1d542thr: type(x)(f(x.items(), y))
        elif (s := 'K') in S:
            thrf = lambda f, *thr1d538thr, **thr1d542thr: lambda x, y, *thr1d538thr, **thr1d542thr: type(x)(ζ(f(x.items(), y), x.values()))
        elif (s := 'V') in S:
            thrf = lambda f, *thr1d538thr, **thr1d542thr: lambda x, y, *thr1d538thr, **thr1d542thr: type(x)(ζ(x.keys(), f(x.items(), y)))
        if thrf:
            S.discard(s)
            return thrf(S and thr1d54athr[S.pop()] or thr1d54athr)
        return lambda x, y, i=i, *thr1d538thr, **thr1d542thr: thr1d54athr.thrf(x, y, i)
    __call__ = lambda thr1d54athr, x, y, *thr1d538thr, **thr1d542thr: thr1d54athr.thrf(x, y, 1)

class ꟿ(ᴍ):
    thrf = thr1d4aethrthr2133thr(lambda x, y, i, *thr1d538thr, **thr1d542thr: _map_d(x, lambda x, *thr1d538thr, **thr1d542thr: y(*(x if thr1d5dcthr(x) else (x,))), i))

class thr221athr:
    __getitem__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: lambda y, *thr1d538thr, **thr1d542thr: y ** (1 / x)
    __call__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: x ** thr00bdthr
thr221athr = thr221athr()
ᴍ, ꟿ, thr017fthr, Ϝ = (ᴍ(), ꟿ(), thr017fthr(), Ϝ())
ᙎ, ᙡ, ᗢ, ᙧ = (ᙎ(), ᙡ(), ᗢ(), ᙧ())
thrf0e35thr, thrf0e37thr = (thrf0e35thr(), thrf0e37thr())

def thr2a33thr(thralpha=thr2400thr, thrbeta=thr2400thr):
    if thralpha is thr2400thr:
        thralpha, thrbeta = (thrbeta, thralpha)
    assert thralpha, 'Assertion failed!' if thrbeta is thr2400thr else thrbeta
    return thralpha

def _wherest(thr1d54fthr, thrf=thr1d44fthr, I=ⴴ):
    thrf = thrf is thr2400thr and thr1d44fthr or thrf
    for i, x in thr21a8thr(thr1d54fthr):
        if thrf(x):
            return i if I else x
    return thr25a1thr
ᣆ = thr1d450thrthr1d451thr((thrf := (lambda x, y, *thr1d538thr, **thr1d542thr: y(x) if (thr1d538thr[0] if thr1f0ccthr(thr1d538thr) else x) else x)), thr1d454thr=lambda a, *thr1d538thr, **thr1d542thr: lambda x, y, *thr1d538thr, **thr1d542thr: thrf(x, y, a))
thrf0445thr = thr1d450thrthr1d451thr(_wherest, I=lambda *thr1d538thr, **thr1d542thr: _wherest(*thr1d538thr, I=thr2713thr))
thrf0441thr = lambda thr1d54fthr, thrf=thr1d44fthr, *thr1d538thr, **thr1d542thr: thr25a1thr if thr25a1thr is (i := thrf0445thr['I'](thr1d54fthr, thrf)) else thr1d54fthr[:i]
thrf0443thr = lambda thr1d54fthr, thrf=thr1d44fthr, *thr1d538thr, **thr1d542thr: thr25a1thr if thr25a1thr is (i := thrf0445thr['I'](thr1d54fthr, thrf)) else thr1d54fthr[i:]
thr2282thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d460thr(x).issubset(thr1d460thr(y))
thr2283thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d460thr(y).issubset(thr1d460thr(x))
thr228athr = lambda x, y, *thr1d538thr, **thr1d542thr: (thralpha := thr1d460thr(x)).issubset((thrbeta := thr1d460thr(y))) and thralpha != thrbeta
thr228bthr = lambda x, y, *thr1d538thr, **thr1d542thr: (thralpha := thr1d460thr(y)).issubset((thrbeta := thr1d460thr(x))) and thralpha != thrbeta
thr2284thr = lambda x, y, *thr1d538thr, **thr1d542thr: not thr2282thr(x, y)
thr2285thr = lambda x, y, *thr1d538thr, **thr1d542thr: not thr2283thr(x, y)
thr220bthr, thr220cthr = (lambda x, y, *thr1d538thr, **thr1d542thr: y in x, lambda x, y, *thr1d538thr, **thr1d542thr: y not in x)
thr2223thr, thr2224thr = (lambda x, y, *thr1d538thr, **thr1d542thr: gcd(x, y) == x, lambda x, y, *thr1d538thr, **thr1d542thr: gcd(x, y) != x)
thr222athr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d460thr(x) | thr1d460thr(y)
thr2229thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d460thr(x) & thr1d460thr(y)
thr2216thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d460thr(x) - thr1d460thr(y)
thr2a09thr = lambda *thr1d538thr, **thr1d542thr: ᴍ(product(*(v[0] if 1 == thr1f0ccthr((v := thr1d563thr(thr1d538thr))) else v)), thr1d459thr)
thr2213thr = lambda *thr1d538thr, **thr1d542thr: [-h[0], +h[0]] if thr1f0ccthr((h := thr1d563thr(thr1d538thr))) == 1 else [h[0] - h[1], h[0] + h[1]]
thr00b1thr = lambda *thr1d538thr, **thr1d542thr: [+h[0], -h[0]] if thr1f0ccthr((h := thr1d563thr(thr1d538thr))) == 1 else [h[0] + h[1], h[0] - h[1]]

def ᐹ(x=thr2400thr, y=thr2400thr):
    if x is thr2400thr:
        return type(y)
    elif y is thr2400thr:
        return type(x)
    return isinstance(x, y if isinstance(y, type) else type(y))
thr1f0ccthr = len
thrf0efethr = thr1d450thrthr1d451thr(lambda x, *thr1d538thr, **thr1d542thr: x, thr1d454thr=lambda x, *thr1d538thr, **thr1d542thr: thr1d450thrthr1d451thr(lambda *thr1d538thr, **thr1d542thr: x, __repr__=lambda *thr1d538thr, **thr1d542thr: f'\U000f0efe[{x}]'), __repr__=lambda *thr1d538thr, **thr1d542thr: '\U000f0efe')
ᴙ = thr1d450thrthr1d451thr(lambda x, *thr1d538thr, **thr1d542thr: (x if ᐹ(x, ᔐ) else thr1d459thr(x))[::-1], L=lambda x, *thr1d538thr, **thr1d542thr: thr1d459thr(x)[::-1])
thr2349thr = lambda x, *thr1d538thr, **thr1d542thr: ζ(*x)
thr236dthr = lambda x, *thr1d538thr, **thr1d542thr: ᴍ(x.split('\u205f'), thr236dthr) if '\u205f' in x else x.split('\u2009')
thr21a8thr = lambda x, *thr1d538thr, **thr1d542thr: thr1d459thr(enumerate(x))
thr2b65thr = lambda x, *thr1d538thr, **thr1d542thr: thr1d459thr(range(x if ᐹ(x, thr1d456thr) else thr1f0ccthr(x)))
thr2908thr, thr2909thr = ᴍ((min, max), lambda thrf, *thr1d538thr, **thr1d542thr: lambda *thr1d538thr, **thr1d542thr: thrf(thr1d538thr[0], key=thr1d538thr[1]) if thr1d538thr[1:] and thr1d5d9thr(thr1d538thr[1]) else thrf(*thr1d563thr(thr1d538thr)))
ⴵ = sign = lambda x, *thr1d538thr, **thr1d542thr: 1 if x > 0 else x and -1 or 0
thr26f6thr = thr1d450thrthr1d451thr(lambda x, *thr1d538thr, **thr1d542thr: [x], S=lambda x, *thr1d538thr, **thr1d542thr: {x}, T=lambda x, *thr1d538thr, **thr1d542thr: (x,))
thr25a2thr = lambda *thr1d538thr, **thr1d542thr: round(*thr1d563thr(thr1d538thr))
thr2026thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d459thr(range(x, y))
thr0021thr = lambda x, *thr1d538thr, **thr1d542thr: thrpi(thrf7e3athr(NOOOL, x), 1)
thr2af0thr, thr2aefthr = (lambda x, *thr1d538thr, **thr1d542thr: +abs(x), lambda x, *thr1d538thr, **thr1d542thr: -abs(x))

def thr2b04thr(x=thr2400thr, y=thr2400thr):
    if x is thr2400thr:
        x, y = (y, x)
    if ᐹ(x, ᔐ) and (y is thr2400thr or ᐹ(y, ᔐ)):
        return x.strip(*thr1d563thr((y,)))
    thr2a33thr(thr2717thr, NOOOL)
thr25c4thr, thr25bathr = (lambda x, y, *thr1d538thr, **thr1d542thr: x, lambda x, y, *thr1d538thr, **thr1d542thr: y)

def thr22c0thr(thr1d44bthr, v=thr2713thr):
    for v in thr1d44bthr:
        if not v:
            return v
    return v

def thr22c1thr(thr1d44bthr, v=thr2717thr):
    for v in thr1d44bthr:
        if v:
            return v
    return v
thr263ethr = lambda *thr1d538thr, flush=thr2713thr, **thr1d542thr: print(*thr1d538thr, flush=flush, **thr1d542thr) or (thr1d538thr and thr1d538thr[0])
ζ = lambda *thr1d538thr, **thr1d542thr: ᴍ(zip(*thr1d563thr(thr1d538thr)), thr1d459thr)
thrpi = lambda x, *thr1d538thr, **thr1d542thr: thr017fthr(x, LITERAL_OPS_['*'], *thr1d563thr(thr1d538thr))
Σ = lambda x, *thr1d538thr, **thr1d542thr: thr017fthr(x, LITERAL_OPS_['+'], *thr1d563thr(thr1d538thr))
thrf04bcthr = lambda x, y, *thr1d538thr, **thr1d542thr: sorted(x, key=thr1d55dthr(y, thr25a1thr)[0])
thrf04bdthr = lambda x, y, *thr1d538thr, **thr1d542thr: sorted(x, key=thr1d55dthr(y, thr25a1thr)[0], reverse=thr2713thr)

def thrf0232thr(x=thr2400thr, y=thr2400thr, s=thr2400thr, neg=thr2717thr):
    if s is LITERAL_OPS_['*']:
        s = y
    if neg:
        y = thr25cbthr(LITERAL_OPS_['not'], y)
    if s is thr2400thr:
        return thr1d459thr(filter(thr25a1thr if y is thr2400thr else y, x))
    if not thr1d5d9thr(s):
        s = thrf0efethr[s]
    if y is thr2400thr:
        return thr1d459thr(filter(thr25a1thr, ᴍ(x, s)))
    return [s(z) if y(z) else z for z in x]
thrf0233thr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: thrf0232thr(*thr1d538thr, **thr1d542thr, neg=thr2713thr))
thrf0232thr = BINWRAP_(thrf0232thr)

def RANGE_(x=thr2400thr, y=thr2400thr, s=thr2400thr, thr1d54fthr=thr2400thr):
    thr2a33thr(not (x is thr2400thr) is y, f'Range missing both values!')
    if (thr1d530thr := (s is thr2400thr)):
        s = 1
    v = y if x is thr2400thr else x if y is thr2400thr else thr2400thr
    if (v is thr2400thr and (x is not thr2400thr and ᐹ(x, thr1d456thr))) and (y is not thr2400thr and ᐹ(y, thr1d456thr)) or (v is not thr2400thr and ᐹ(v, thr1d456thr)):
        if v is not thr2400thr:
            x, y = (0, v)
        if thr1d54fthr == '\U000f7e39':
            return [*range(x, y, s)]
        if thr1d54fthr == '\U000f7e3a':
            return [*range(x + 1, y + 1, s)]
        if thr1d54fthr == '\U000f7e38':
            return [*range(x + 1, y, s)]
        if thr1d54fthr == '\U000f7e3b':
            return [*range(x, y + 1, s)]
    if v is not thr2400thr:
        thr2a33thr(thr1d5dcthr(v), NOOOL)
        v = thr1d459thr(v)
        if thr1d54fthr == '\U000f7e38':
            return (v[0], v[1:-1:s], v[-1])
        if thr1d530thr:
            s = 0
        if thr1d54fthr == '\U000f7e39':
            return v[0 + s]
        if thr1d54fthr == '\U000f7e3a':
            return v[-1 - s]
        if thr1d54fthr == '\U000f7e3b':
            return (v[0 + s], v[-1 - s])
    if thr2218thr(thr1d5dcthr, x) and thr2218thr(thr1d5dcthr, y):
        return [x[h] for h in y[::s]]
    if thr2218thr(thr1d5dcthr, x) and ᐹ(y, thr1d456thr):
        if thr1d54fthr == '\U000f7e39':
            return x[:y:s]
        if thr1d54fthr == '\U000f7e3a':
            return x[0 + 1:y + 1:s]
        if thr1d54fthr == '\U000f7e38':
            return x[0 + 1:y:s]
        if thr1d54fthr == '\U000f7e3b':
            return x[:y + 1:s]
    if ᐹ(x, thr1d456thr) and thr2218thr(thr1d5dcthr, y):
        if thr1d54fthr == '\U000f7e39':
            return y[slice(x, -1, s)]
        if thr1d54fthr == '\U000f7e3a':
            return y[slice(x + 1, thr25a1thr, s)]
        if thr1d54fthr == '\U000f7e38':
            return y[slice(x + 1, -1, s)]
        if thr1d54fthr == '\U000f7e3b':
            return y[slice(x, thr25a1thr, s)]
    thr2a33thr(thr2717thr, f'Invalid arguments! {ᐹ(NOOOL, x)} {ᐹ(NOOOL, y)}')

def JOIN_(x=thr2400thr, y=thr2400thr, s=ᐦ, thr1d54fthr=thr2400thr, LR_def=thr25a1thr, bound_mode=thr2400thr):
    thr2a33thr(not (x is thr2400thr and thr2400thr is y), f'Join missing both values!')
    if x is thr2400thr:
        x, y = (y, x)
    if ᐹ(s, thr1d461thr):
        if ᐹ(s[0], thr1d456thr):
            bound_mode, thr1d54fthr = s
        else:
            thr1d54fthr, bound_mode = s
        thr2a33thr(ᐹ(thr1d54fthr, ᔐ) and ᐹ(bound_mode, thr1d456thr), f'Bad modifiers!')
    elif ᐹ(s, thr1d456thr):
        s, bound_mode = (ᐦ, s)
    if bound_mode is thr2400thr:
        bound_mode = thr1d54fthr == '⟗' and 1 or 0
    if x is thr2400thr:
        x, y = (y, x)
        thr2a33thr(thr1d5dcthr(x), f'Single-arg {t} needs an iterable')
        return ᣆ['L' in s]('\n' * thr1d54fthr in (thrthr := ('⟕⟗' + ᐦ.join(ᴍ(x, ᔐ)) + '⟗⟖')) and thr220bthr(thrthr, thr1d54fthr * '\n'), thr1d459thr)
    Y = y
    if not thr1d5d9thr(y):
        y = thrf0efethr[y]
    R = []
    if thr1f0ccthr(x) == 0 and (thr1d54fthr != '⨝' or bound_mode > 0):
        v = y(LR_def, LR_def)
        if thr1d54fthr in '⟕⟖' or bound_mode == 1:
            R = [v]
        else:
            R = [v, v]
    else:
        if thr1d54fthr in '⟕⟗':
            R.append(y(LR_def, x[0]))
        for i in thrf7e38thr(thr1f0ccthr(x), NOOOL):
            R.extend([x[i - 1], y(x[i - 1], x[i])])
        R.append(x[-1])
        if thr1d54fthr in '⟖⟗':
            R.append(y(x[-1], LR_def))
    return ᐦ.join(ᴍ(R, ᔐ)) if 'L' not in s and ᐹ(Y, ᔐ) else R
thrf7e39thr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: RANGE_(*thr1d538thr, **thr1d542thr, thr1d54fthr='\U000f7e39'))
thrf7e3athr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: RANGE_(*thr1d538thr, **thr1d542thr, thr1d54fthr='\U000f7e3a'))
thrf7e38thr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: RANGE_(*thr1d538thr, **thr1d542thr, thr1d54fthr='\U000f7e38'))
thrf7e3bthr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: RANGE_(*thr1d538thr, **thr1d542thr, thr1d54fthr='\U000f7e3b'))
thr2a1dthr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: JOIN_(*thr1d538thr, **thr1d542thr, thr1d54fthr='⨝'))
thr27d5thr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: JOIN_(*thr1d538thr, **thr1d542thr, thr1d54fthr='⟕'))
thr27d6thr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: JOIN_(*thr1d538thr, **thr1d542thr, thr1d54fthr='⟖'))
thr27d7thr = BINWRAP_(lambda *thr1d538thr, **thr1d542thr: JOIN_(*thr1d538thr, **thr1d542thr, thr1d54fthr='⟗'))
threb86thr = thr1d450thrthr1d451thr(lambda *thr1d538thr, **thr1d542thr: (lambda I, thrf=thr1d44fthr, *thr1d538thr, **thr1d542thr: thr25c4thr((r := {}), ᴍ(I, lambda x, *thr1d538thr, **thr1d542thr: r.setdefault((h := thrf(x)), []).append(x))))(*thr1d563thr(thr1d538thr), **thr1d542thr), S=lambda *thr1d538thr, **thr1d542thr: ᴍ(thrf04bcthr(threba6thr(threb86thr(*thr1d538thr, **thr1d542thr).items), NOOOL), lambda x, *thr1d538thr, **thr1d542thr: x[1]), B=lambda *thr1d538thr, **thr1d542thr: thr25bathr((h := {thr2713thr: [], thr2717thr: [], **threb86thr(*thr1d538thr, **thr1d542thr)}), [h[0], h[1]]))

def threba6thr(thrf, *thr1d538thr, **thr1d542thr):
    if thr1d5d9thr(thrf):
        return thrf(*thr1d538thr, **thr1d542thr)
    if thr1d5dcthr(thrf):
        for x in thrf:
            pass
        return thrf
    thr2a33thr(thr2717thr, f'{thrf} is not iterable or callable.')
thr2218thr = lambda x, y, *thr1d538thr, **thr1d542thr: x(y)
thr25cbthr = lambda x, y, *thr1d538thr, **thr1d542thr: lambda *thr1d538thr, **thr1d542thr: x(y(*thr1d538thr, **thr1d542thr))

class thr1d459thrthr1d459thr(thr1d459thr):
    thr25a1thr
thr22c4thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr25bathr((x if ᐹ(x, thr1d459thrthr1d459thr) else (x := thr1d459thrthr1d459thr((x,)))).append(y), x)
thr2a01thr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d44fthr(x) == thr1d44fthr(y)
thr22bbthr = lambda x, y, *thr1d538thr, **thr1d542thr: thr1d44fthr(x) ^ thr1d44fthr(y) and (x or y)
thr22bcthr = lambda x, y, *thr1d538thr, **thr1d542thr: not (thr1d44fthr(x) and thr1d44fthr(y)) and (x or y)

def thr24e6thr(*thr1d538thr, thr1d400thr=thr25a1thr):
    (thr1d400thr := (thr1d400thr or []))
    *thr1d538thr, thrf = thr1d538thr
    if not thr1d538thr:
        return thrf(*thr1d400thr)
    thr1d552thr, *thr1d538thr = thr1d538thr
    with thr1d552thr as thr1d41athr:
        thr2218thr(thr1d400thr.append, thr1d41athr)
        return thr24e6thr(*thr1d538thr, thrf, thr1d400thr=thr1d400thr)

class thr2135thr(thr1d451thr):
    thr1d436thrthr1d45bthr = 'ℵ'
    __json__ = lambda thr1d54athr, cb, *thr1d4d0thr, **thr1d4dathr: ꟿ['V'](thr1d451thr(thr1d54athr), lambda x, y, *thr1d538thr, **thr1d542thr: cb(y, *thr1d4d0thr, **thr1d4dathr))
    __init__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: super().__init__(*thr1d538thr, **thr1d542thr)
    __setattr__ = thr1d451thr.__setitem__
    __getitem__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: thr1d451thr.__getitem__(thr1d54athr, x) if x in thr1d54athr else thr1d54athr.getdef()
    __getattr__ = __getitem__
    __iter__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: iter(thr1d54athr.items())
    def __repr__(thr1d54athr, *thr1d538thr, **thr1d542thr):
        f1 = (f'[{h[0]}]' if 0 in (h := thr1d54athr.__dict__) else ᐦ)
        f2 = ', '.join(ꟿ(threba6thr(thr1d54athr.items), lambda x, y, *thr1d538thr, **thr1d542thr: f'{x}={y}'))
        return f'{thr1d54athr.__class__.thr1d436thrthr1d45bthr}{f1}({f2})'
    __call__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr25bathr(thr1d451thr.update(thr1d54athr, *thr1d538thr, **thr1d542thr), thr1d54athr)
    __bool__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr1f0ccthr(thr1d54athr) > 0
    __or__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: thr1d54athr.copy()(x)

    def __getstate__(thr1d54athr):
        if thr1d54athr.hasdef():
            return (thr1d451thr(thr1d54athr), thr1d54athr.getdef())
        else:
            return (thr1d451thr(thr1d54athr),)

    def __setstate__(thr1d54athr, s):
        thr1d54athr.__init__(s[0])
        if thr1f0ccthr(s) > 1:
            thr1d54athr.setdef(s[1])

    def __pow__(thr1d54athr, x):
        if x == LITERAL_OPS_['-']:
            return thr2218thr(thr1d459thr, threba6thr(thr1d54athr.keys))
        if x == LITERAL_OPS_['+']:
            return thr2218thr(thr1d459thr, threba6thr(thr1d54athr.values))
        if x == LITERAL_OPS_['*']:
            return thr2218thr(thr1d459thr, threba6thr(thr1d54athr.items))
        thr2a33thr(thr2717thr, NOOOL)
    hasdef = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: 0 in thr1d54athr.__dict__
    getdef = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr1d54athr.__dict__[0]
    setdef = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: thr25bathr(SETITEM(thr1d54athr.__dict__, 0, x), thr1d54athr)

    def copy(thr1d54athr):
        r = type(thr1d54athr)(super().copy())
        if thr1d54athr.hasdef():
            r.setdef(thr1d54athr.getdef())
        return r

class thr2136thr(thr2135thr):
    thr1d436thrthr1d45bthr = 'ℶ'
    __iter__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: iter(thr1d54athr.values())

class _hwrap(thr1d451thr):

    def __init__(thr1d54athr, thr1d450thr):
        thr1d54athr.thr1d450thr, thr1d54athr.thr1d45bthr = (thr1d450thr, thr1d450thr.thr1d436thrthr1d45bthr)
    __getitem__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: thr1d54athr.thr1d450thr().setdef(x)
    __setitem__ = lambda thr1d54athr, x, y, *thr1d538thr, **thr1d542thr: thr25bathr((thr24afthr := thr1d54athr.thr1d450thr()).__setitem__(x, y), thr24afthr)
    __call__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: thr1d54athr.thr1d450thr(*thr1d538thr, **thr1d542thr)
    __or__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: thr1d54athr.thr1d450thr() | x
    __pow__ = lambda thr1d54athr, x, *thr1d538thr, **thr1d542thr: thr1d54athr.thr1d450thr() ** x
    __repr__ = lambda thr1d54athr, *thr1d538thr, **thr1d542thr: f'{thr1d54athr.thr1d45bthr}()'
    __bool__ = lambda *thr1d538thr, **thr1d542thr: thr2717thr
thr2135thr = _hwrap(thr2135thr)
thr2136thr = _hwrap(thr2136thr)

#################### 𝐍 ####################
from util import Z

class thr1d40dthr:

    def __init__(thrf1055thr, t, *c):
        thrf1055thr.t, thrf1055thr.c = (t, c or [])
    __iter__ = lambda thrf1055thr, *thr1d538thr, **thr1d542thr: iter(thrf1055thr.c)
    __getitem__ = lambda thrf1055thr, i, *thr1d538thr, **thr1d542thr: thrf1055thr.c[i]
    __len__ = lambda thrf1055thr, *thr1d538thr, **thr1d542thr: thr1f0ccthr(thrf1055thr.c)
    ft = thr1d4aethrthr2133thr(lambda x, *thr1d538thr, **thr1d542thr: thr1d40dthr(x[0], *(ᴍ(x[1], thr1d40dthr.ft) if ᐹ(x[1], thr1d459thr | thr1d461thr) and thr1f0ccthr(x[1]) == 2 else thr26f6thr(x[1]))))
    tt = lambda thrf1055thr, *thr1d538thr, **thr1d542thr: (thrf1055thr.t, ᴍ(thrf1055thr.c, lambda x, *thr1d538thr, **thr1d542thr: threba6thr(x.tt) if ᐹ(x, thr1d40dthr) else x))
    copy = lambda thrf1055thr, t=thr25a1thr, c=thr25a1thr, *thr1d538thr, **thr1d542thr: ᐹ(NOOOL, thrf1055thr)(thrf1055thr.t if t is thr25a1thr else t, *(thrf1055thr.c if c is thr25a1thr else c))
    rcopy = lambda thrf1055thr, t=thr25a1thr, *thr1d538thr, **thr1d542thr: ᐹ(NOOOL, thrf1055thr)(thrf1055thr.t if t is thr25a1thr else t, *ᴍ(thrf1055thr.c, ᐹ(NOOOL, thrf1055thr).rcopy)) if ᐹ(thrf1055thr, thr1d40dthr) else thrf1055thr

    def frp(thrf1055thr, thrf, r, pre=thr2717thr):
        thr1d4e1thr = lambda x, *thr1d538thr, **thr1d542thr: x.copy(c=ᴍ(x, lambda x, *thr1d538thr, **thr1d542thr: x.frp(thrf, r, pre)))
        thrf1055thr = ᣆ[pre](thrf1055thr, thr1d4e1thr)
        if thr2218thr(thrf, thrf1055thr):
            return r(thrf1055thr)
        return ᣆ[not pre](thrf1055thr, thr1d4e1thr)
    ftrp = lambda thrf1055thr, fs, *thr1d538thr, **thr1d542thr: thrf1055thr.frp(lambda x, *thr1d538thr, **thr1d542thr: x.t in fs, *thr1d538thr, **thr1d542thr)

    def extract(thrf1055thr, thr1d453thr, E=thr25a1thr, thrbeta=thr2713thr, thrdelta=thr2717thr, pre=thr2717thr):
        L = r, E = ([], [] if (γ := (E is thr25a1thr)) else E)
        thr1d740thr = thrf41ethr((thr2102thr := ᐹ(NOOOL, thrf1055thr)).extract)(thr2b24thr, thr1d453thr, E, pre=pre)
        ᴍ(thrf1055thr, lambda x, *thr1d538thr, **thr1d542thr: L[thr1d44fthr(thr1d453thr((x := ᣆ[pre](x, thr1d740thr))))].append(x))
        n = thrf1055thr.copy(c=r if pre else ᴍ(r, thr1d740thr))
        return ((n, E) if thrdelta else E) if thrbeta and γ else n
    filter = lambda thrf1055thr, thrf, *thr1d538thr, **thr1d542thr: thrf1055thr.extract(thr25cbthr(LITERAL_OPS_['not'], f), *thr1d538thr, **thr1d542thr, thrbeta=thr2717thr, thrdelta=thr2717thr)

    def P(thrf1055thr):
        clc = lambda x, c='BL', *thr1d538thr, **thr1d542thr: getattr(Z, c) + x + Z.W
        ML = lambda x, *thr1d538thr, **thr1d542thr: thr1f0ccthr(x) - Σ(ᴍ((Z.W, Z.BL, Z.RE, Z.dBL, Z.GRE, Z.YEL), lambda k, *thr1d538thr, **thr1d542thr: x.count(k) * thr1f0ccthr(k)), 0)

        def box(x):
            (o, c), O, C = ᴍ[2](thr236dthr(f'[]\u2009⎡⎢⎣\u2009⎤⎥⎦'), lambda x, *thr1d538thr, **thr1d542thr: clc(x, 'dBL'))
            x = x.split('\n')
            if thr1f0ccthr(x) == 1:
                return f'{o}{x[0]}{c}'
            ms = thr2909thr(ᴍ(x, ML), NOOOL)
            return '\n'.join(ꟿ(ᙡ(x, NOOOL), lambda x, y, z, *thr1d538thr, **thr1d542thr: O[(n := (1 - (x is thr25a1thr) + (z is thr25a1thr)))] + y + (ms - ML(y)) * ' ' + C[n]))
        if not ᐹ(thrf1055thr, thr1d40dthr):
            return thr2218thr(ᔐ, thrf1055thr)
        thr2205thr = clc('∅', 'RE')

        def format_e(e):
            if not e:
                return ᐦ
            r = []
            for k, v in e:
                if k == 'T':
                    (r := (r + thr26f6thr(clc('T', 'GRE'))))
                else:
                    f0 = clc('→', 'BL')
                    (r := (r + thr26f6thr(f'{k}{f0}{v.t}')))
            f0 = clc('\U000f0141', 'YEL')
            f1 = ','.join(r)
            f2 = clc('\U000f0142', 'YEL')
            return f'{f0}{f1}{f2}'
        nam = (threba6thr(thrf1055thr.t.P) if ᐹ(thrf1055thr.t, thr1d40dthr) else f'{thrf1055thr.t}{format_e(thrf1055thr.e)}' if ᐹ(thrf1055thr, thrNPR) else thr2218thr(ᔐ, thrf1055thr.t)) or thr2205thr
        start = thr2218thr(box, nam)
        (thr2574thr, thr256ethr), m0, m1, m2 = ᴍ[2](thr236dthr(f'─┬\u2009┬─\u2009├╰\u2009│ '), clc)
        if not thr1f0ccthr(thrf1055thr):
            return f'{start}{thr2574thr}{thr2205thr}'
        slns = start.split('\n')
        res, ml = ('\n'.join(slns[:-1]), ML((lne := slns[-1])))
        for i, z in thr21a8thr(thrf1055thr):
            l = (threba6thr(z.P) if ᐹ(z, thr1d40dthr) else thr2218thr(ᔐ, z)).split('\n')
            e = i == thr1f0ccthr(thrf1055thr) - 1
            l[0] = (m1 if i else m0)[e] + l[0]
            l[1:] = ᴍ(l[1:], lambda x, *thr1d538thr, **thr1d542thr: m2[e] + x)
            l = ᴍ(l, lambda x, *thr1d538thr, **thr1d542thr: ml * ' ' + x)
            if not i:
                pre = f'{start}'
                l[0] = pre + ' ' * (ml - ML(pre)) + l[0][ml:]
            (res := (res + ('\n'.join(l) + (not e) * '\n')))
        return res

class thrNPR(thr1d40dthr):
    __slots__ = ('t', 'c', 'e')

    def __init__(thrf1055thr, t, *c, e=thr2400thr):
        thrf1055thr.t, thrf1055thr.c, thrf1055thr.e = (t, not c and [] or thr1d459thr(c), thr2135thr[thr25a1thr] if e is thr2400thr else e)
    __setitem__ = lambda thrf1055thr, x, y, *thr1d538thr, **thr1d542thr: SETITEM(thrf1055thr.c, x, y)

    def __delitem__(thrf1055thr, i):
        del thrf1055thr.c[i]
    cp = copy = lambda thrf1055thr, t=thr25a1thr, c=thr25a1thr, e=thr2400thr, *thr1d538thr, **thr1d542thr: ᐹ(NOOOL, thrf1055thr)(thrf1055thr.t if t is thr25a1thr else t, *(thrf1055thr.c if c is thr25a1thr else c), e=thrf1055thr.e if e is thr2400thr else e)
    cpr = rcopy = lambda thrf1055thr, t=thr25a1thr, *thr1d538thr, **thr1d542thr: ᐹ(NOOOL, thrf1055thr)(thrf1055thr.t if t is thr25a1thr else t, *ᴍ(thrf1055thr.c, ᐹ(NOOOL, thrf1055thr).rcopy), e=thrf1055thr.e.copy()) if ᐹ(thrf1055thr, thr1d40dthr) else thrf1055thr

    def frp(thrf1055thr, thrf, r, pre=thr2717thr):
        thr1d4e1thr = lambda *thr1d538thr, **thr1d542thr: threba6thr((SETITEM(thrf1055thr, x, y.frp(thrf, r, pre)) for x, y in thr21a8thr(thrf1055thr)))
        if pre:
            threba6thr(thr1d4e1thr)
        if thr2218thr(thrf, thrf1055thr):
            return r(thrf1055thr)
        if not pre:
            threba6thr(thr1d4e1thr)
        return thrf1055thr

    def ftrp(thrf1055thr, fs, *thr1d538thr, not_T=thr2713thr, **thr1d542thr):
        if not not_T or not thrf1055thr.e.T:
            thrf = lambda x, *thr1d538thr, **thr1d542thr: (not not_T or not x.e.T) and x.t in thr1d460thr(fs)
            thrf1055thr.frp(thrf, *thr1d538thr, **thr1d542thr)
        return thrf1055thr

    def find(thrf1055thr, thrf, pre=thr2713thr, not_T=thr2713thr, R=thr25a1thr):
        if R is thr25a1thr:
            R = []
        if not_T and thrf1055thr.e.T:
            return R
        if pre:
            threba6thr((c.find(thrf, thr2713thr, not_T, R) for c in thrf1055thr))
        if (do := thrf(thrf1055thr)):
            R.append(thrf1055thr)
        if do and (not pre):
            threba6thr((c.find(thrf, thr2713thr, not_T, R) for c in thrf1055thr))
        return R

    def flat(thrf1055thr, thrf):
        C = []
        for c in thrf1055thr:
            if c.e.T:
                C.append(c)
            elif thrf((c := c.flat(thrf))):
                C.extend(c.c)
            else:
                C.append(c)
        thrf1055thr.c = C
        return thrf1055thr

    def kill_children(thrf1055thr, thrf, not_T=thr2713thr):
        if ᐹ(thrf, ᔐ):
            thrf = lambda n, t=thrf, *thr1d538thr, **thr1d542thr: lambda x, *thr1d538thr, **thr1d542thr: x.t == t
        for i, x in ᴙ(thr21a8thr(thrf1055thr)):
            if not_T and x.e.T:
                continue
            if thrf(x):
                del thrf1055thr[i]
            else:
                thrf1055thr[i].kill_children(thrf, not_T)
        return thrf1055thr

    def as_txt(thrf1055thr):
        l = ''

        def thrf(thrf1055thr):
            nonlocal l
            if thrf1055thr.e.T:
                (l := (l + thrf1055thr.t))
            else:
                threba6thr((thrf(c) for c in thrf1055thr))
        thrf(thrf1055thr)
        return l
    rm = child_killer = kill_children
    filter = lambda thrf1055thr, thrf, *thr1d538thr, **thr1d542thr: thrf1055thr.kill_children(thr25cbthr(LITERAL_OPS_['not'], thrf), *thr1d538thr, **thr1d542thr)
__exports__ = ('𝐍', 'thrNPR')

#################### peggle2 ####################
try:
    import regex as re
except Exception:
    import re
from pickle import loads, dumps
show_cache_table = lambda thr1d445thr, thr212dthr, *thr1d538thr, **thr1d542thr: ꟿ(thr21a8thr(thr212dthr), lambda i, v, *thr1d538thr, **thr1d542thr: ꟿ(thrf04bcthr(thr2135thr(v) ** LITERAL_OPS_['*'], NOOOL), lambda x, y, *thr1d538thr, **thr1d542thr: thr263ethr(f'{i},{x}\t{thr1d445thr[x]}\t{y}')))
from time import time
thr1d4fdthr_ = thr25a1thr

def thr1d4e3thr(s=ᐦ):
    global thr1d4fdthr_
    if thr1d4fdthr_ is thr25a1thr:
        thr263ethr(f'Starting timer')
        thr1d4fdthr_ = threba6thr(time)
        return
    thr263ethr(f'{s} took {threba6thr(time) - thr1d4fdthr_}s')
    thr1d4fdthr_ = thr25a1thr

def gram_convert(thrf1055thr):
    name_remaps = thr2135thr(ζ(thr236dthr('elm_o\u2009elm_a\u2009assign_cln\u2009group_inner\u2009group'), '∨∧←∧∧'))
    thrswa = thr2135thr(T=thr2713thr)
    TT = lambda thrf1055thr, *thr1d538thr, **thr1d542thr: (thrf1055thr.t, *((thrf1055thr[0].t,) if thrf1055thr.t in 'ᔐ~' else (thrf1055thr[0].t, *ᴍ(thrf1055thr[1:], TT)) if thrf1055thr.t == '←' else ᴍ(thrf1055thr, TT)))
    escape = lambda x, t='ݺ', *thr1d538thr, **thr1d542thr: x.replace('␛␛', t).replace('␛', '').replace(t, '␛')
    txt = lambda x, *thr1d538thr, **thr1d542thr: thrNPR(x, e=thrswa)

    def reduce_j(thrf1055thr):
        thralpha, o, thrbeta, *C = thrf1055thr
        if C:
            thr2a33thr(thr2717thr, NOOOL)
        if o.t == '↷':
            return thrNPR('∧', thralpha, thrbeta, thralpha)
        elif o.t == '⯆':
            return thrNPR('∨', thrNPR('∧', thrbeta, thrNPR('+', thrNPR('∧', thralpha, thrbeta))), thrbeta)
        elif o.t == '△':
            return thrNPR('∨', thrNPR('∧', thrNPR('*', thrNPR('∧', thralpha, thrbeta)), thralpha), thralpha)
        elif o.t == '▽':
            return thrNPR('∨', thrNPR('∧', thrNPR('∧', thrbeta, thrNPR('*', thrNPR('∧', thralpha, thrbeta)))), thrNPR('✓'))
        elif o.t == '⯅':
            return thrNPR('∧', thrNPR('+', thrNPR('∧', thralpha, thrbeta)), thralpha)
        thr2a33thr(thr2717thr, NOOOL)

    def bad(thrf1055thr):
        if thrf1055thr.t in thr236dthr('comment\u2009w\u2009W'):
            return thr2713thr
        if ((not thrf1055thr.t and thr1f0ccthr(thrf1055thr) == 1) and thrf1055thr.c[0].e.T) and thrf1055thr.c[0].t in f'()∧∨:=':
            return thr2713thr

    def collapse_ao(thrf1055thr):
        if thrf1055thr.e.T:
            return thrf1055thr
        thrf1055thr.c = Σ(ᴍ(thrf1055thr.c, lambda x, *thr1d538thr, **thr1d542thr: x.c if (x := collapse_ao(x)).t == (thrthr := thrf1055thr.t) and thrthr in '∧∨' else [x]), [])
        return thrf1055thr

    def parse_elm(N):
        thralpha, n, thrbeta = (N[0].as_txt(), N[1], N[2].as_txt())
        l1, l2 = threb86thr['B'](thralpha, f'❗⠶ƨ'.__contains__)
        for o in (*l1, *thrbeta, *l2):
            if o == '~':
                n = thrNPR(o, thrNPR(re.compile(n.as_txt()), e=thrswa))
            else:
                n = thrNPR(o, n)
        return n
    rules = thrf1055thr.rm(bad).ftrp(thr236dthr('prefix\u2009suffix'), lambda x, *thr1d538thr, **thr1d542thr: thrNPR(x.t, txt(x.as_txt()))).ftrp(thr236dthr('str'), lambda x, *thr1d538thr, **thr1d542thr: thrNPR('ᔐ', txt(escape(x.as_txt()[1:-1])))).ftrp(name_remaps ** LITERAL_OPS_['-'], lambda x, *thr1d538thr, **thr1d542thr: thrNPR(name_remaps[x.t], *(y for y in x if not y.e.T)), thr2713thr).flat(lambda x, *thr1d538thr, **thr1d542thr: x.t == '_elm_j').find(lambda x, *thr1d538thr, **thr1d542thr: x.t == 'assign_eql')
    rules = thr2135thr(ᴍ(rules, lambda x, *thr1d538thr, **thr1d542thr: (x[0].as_txt(), x[2])))
    for k, thrf1055thr in rules:
        thrf1055thr = collapse_ao(thrf1055thr.ftrp(thr236dthr('assign_eql'), lambda x, *thr1d538thr, **thr1d542thr: x[0], thr2713thr).flat(lambda x, *thr1d538thr, **thr1d542thr: x.t in thr236dthr('∧\u2009∨\u2009elm_j') and thr1f0ccthr(x) == 1)).ftrp(thr236dthr('elm_j'), reduce_j, thr2713thr).ftrp(thr236dthr('elm'), parse_elm, thr2713thr).ftrp(thr236dthr('←'), lambda x, *thr1d538thr, **thr1d542thr: thrNPR(x.t, txt(x[0][0].t), *x[1:]), thr2713thr).ftrp(thr236dthr('rname'), lambda x, *thr1d538thr, **thr1d542thr: thrNPR('_' * (x[0].t not in '✓✗') + x[0].t, e=thrswa))
        if thrf1055thr.t in '∧∨' and thr1f0ccthr(thrf1055thr) == 1:
            thrf1055thr = thrf1055thr[0]
        rules[k] = TT(thrf1055thr)
    return rules

def parse(thr1d437thr, thr1d445thr, start_rule=thr25a1thr):
    thr212dthr, χ = (ᴍ(thr2b65thr(thr1f0ccthr(thr1d437thr) + 1), lambda x, *thr1d538thr, **thr1d542thr: {}), 0)
    thr1d4e2thr = [(None, thr1f0ccthr(thr1d445thr) - 1 if start_rule is None else start_rule)]
    χ = 0
    while thr1d4e2thr:
        Χ, ι = thr1d4e2thr.pop(-1)
        if Χ is not None:
            χ = Χ
        γ, *thr1d436thr = thr1d445thr[ι]
        thr1d520thr = thr212dthr[χ]
        if γ == 'ᔐ':
            if thr1d436thr[0] == thr1d437thr[χ:(thr1d74cthr := (χ + len(thr1d436thr[0])))]:
                thr1d520thr[ι] = (thr2713thr, thr1d74cthr)
            else:
                thr1d520thr[ι] = (thr2717thr, χ)
        elif γ == '~':
            if (m := thr1d436thr[0].match(thr1d437thr, χ)):
                thr1d520thr[ι] = (thr2713thr, m.span()[1], m)
            else:
                thr1d520thr[ι] = (thr2717thr, χ)
        elif γ == '∧':
            n, thr1d74cthr = thr1d520thr[ι] if ι in thr1d520thr else (0, χ)
            while thr2713thr:
                thr1d73ethr, thr1d450thr = (thr1d436thr[n], thr212dthr[thr1d74cthr])
                if thr1d73ethr not in thr1d450thr:
                    thr1d4e2thr.extend([(χ, ι), (thr1d74cthr, thr1d73ethr)])
                    thr1d520thr[ι] = (n, thr1d74cthr)
                    break
                thr1d454thr, thr1d74cthr = thr212dthr[thr1d74cthr][thr1d73ethr][:2]
                (n := (n + 1))
                if not thr1d454thr:
                    thr1d520thr[ι] = (thr2717thr, χ)
                    break
                if n == len(thr1d436thr):
                    thr1d520thr[ι] = (thr2713thr, thr1d74cthr)
                    break
        elif γ == '∨':
            n = thr1d520thr[ι] if ι in thr1d520thr else 0
            while thr2713thr:
                thr1d73ethr, thr1d450thr = (thr1d436thr[n], thr212dthr[χ])
                if thr1d73ethr not in thr1d450thr:
                    thr1d4e2thr.extend([(χ, ι), (χ, thr1d73ethr)])
                    thr1d520thr[ι] = n
                    break
                thr1d454thr, thr1d74cthr = thr212dthr[χ][thr1d73ethr][:2]
                if thr1d454thr:
                    thr1d520thr[ι] = (thr2713thr, thr1d74cthr, n)
                    break
                (n := (n + 1))
                if n == len(thr1d436thr):
                    thr1d520thr[ι] = (thr2717thr, χ)
                    break
        elif γ == '*' or γ == '+':
            if ι in thr1d520thr:
                c = thr1d520thr[ι]
            else:
                c = thr1d520thr[ι] = [χ]
            thr1d73ethr, thr1d74cthr = (thr1d436thr[0], c[-1])
            while thr2713thr:
                thr1d450thr = thr212dthr[thr1d74cthr]
                if thr1d73ethr not in thr1d450thr:
                    thr1d4e2thr.extend([(χ, ι), (thr1d74cthr, thr1d73ethr)])
                    break
                thr1d454thr, Χ = thr1d450thr[thr1d73ethr][:2]
                if not thr1d454thr:
                    if γ == '*' or len(c) > 1:
                        thr1d520thr[ι] = (thr2713thr, thr1d74cthr, c[:-1])
                    else:
                        thr1d520thr[ι] = (thr2717thr, χ)
                    break
                c.append((thr1d74cthr := Χ))
        elif γ == '✓':
            thr1d520thr[ι] = (thr2713thr, χ)
        elif γ == '✗':
            assert thr2717thr, thr2a33thr(NOOOL, f'Hit an ✗')
        elif γ == '←':
            if thr1d436thr[1] not in thr1d520thr:
                thr1d4e2thr.extend([(χ, ι), (χ, thr1d436thr[1])])
            else:
                thr1d454thr, thr1d74cthr = thr1d520thr[thr1d436thr[1]][:2]
                thr1d520thr[ι] = (thr1d454thr, thr1d74cthr, thr1d436thr[1])
        else:
            if thr1d436thr[0] not in thr1d520thr:
                thr1d4e2thr.extend([(χ, ι), (χ, thr1d436thr[0])])
            else:
                thr1d454thr, thr1d74cthr = thr1d520thr[thr1d436thr[0]][:2]
                if   γ ==  '⮞':
                    thr1d520thr[ι] = (thr1d454thr, χ)
                elif γ ==  '¬':
                    thr1d520thr[ι] = (not thr1d454thr, χ)
                elif γ ==  '❗':
                    assert thr1d454thr
                    thr1d520thr[ι] = (thr1d454thr, thr1d74cthr)
                elif γ ==  '?':
                    thr1d520thr[ι] = (thr2713thr, thr1d74cthr, thr1d454thr)
                else:
                    thr1d520thr[ι] = (thr1d454thr, thr1d74cthr)
    return thr212dthr

def make_rules(r):
    nmp = thr2135thr(ζ(r ** LITERAL_OPS_['-'], thr2b65thr(r)))
    r = ꟿ['K'](r, lambda x, y, *thr1d538thr, **thr1d542thr: '_' + x)
    thr1d402thr = thr2135thr(ζ(r ** LITERAL_OPS_['-'], (thr1d411thr := ᴍ(r ** LITERAL_OPS_['-'], thr26f6thr['T']))))

    def thr1d54athr(r):
        if thr1f0ccthr(r) == 1 and r[0][0] == '_':
            return (r[0],)
        if r in thr1d402thr:
            return thr1d402thr[r]
        if ᐹ(r[0], thr1d456thr):
            r = (thr1d411thr[(thr1d526thr := r[0])][0], *r[1:])
        else:
            thr1d411thr.append((thr1d526thr := thr1f0ccthr(thr1d411thr)))
        if r[0] == '←':
            r = (r[0], r[1], thr1d54athr(r[2]))
        elif r[0] in '✓✗':
            r = (r[0], thr1d526thr)
        elif r[0] not in 'ᔐ~':
            r = (r[0], *ᴍ(r[1:], thr1d54athr))
        return thr25bathr(SETITEM(thr1d411thr, SETITEM(thr1d402thr, r, thr1d526thr), r), thr1d526thr)
    thr1d54athr(('T_root', *ᴍ(ζ(nmp ** LITERAL_OPS_['+'], r ** LITERAL_OPS_['+']), thr1d461thr)))
    thr1d411thr = ᴍ(thr1d411thr, lambda x, *thr1d538thr, **thr1d542thr: (x[0], *ᴍ(x[1:], lambda x, *thr1d538thr, **thr1d542thr: thrf0445thr['I'](r ** LITERAL_OPS_['-'], thrf41ethr(LITERAL_OPS_['=='])(x[0])) if ᐹ(x, thr1d461thr) else x)))
    return thr2135thr[thr1d411thr] | nmp

def parse_to_tree(thr1d445thr, thr212dthr, χ, ι, show_table=thr2717thr, raise_failed=thr2713thr):
    rec = lambda *thr1d538thr, **thr1d542thr: parse_to_tree(thr1d445thr, thr212dthr, *thr1d538thr, raise_failed=raise_failed)
    γ, *C = thr1d445thr[ι]
    if ι not in (thr1d520thr := thr212dthr[χ]):
        return (γ, f'‼∄‼')
    thr1d454thr, thr1d74cthr, *thr1d434thr = thr1d520thr[ι]
    if raise_failed:
        thr2a33thr(thr1d454thr, f'Failed to parse tree!')
    if γ == '∧':
        o = []
        for r in C:
            o.append(rec(χ, r))
            if r not in (thr1d520thr := thr212dthr[χ]):
                break
            χ = thr1d520thr[r][1]
        return (γ, *o)
    if γ == 'ᔐ':
        return (γ, C[0])
    if γ == '?':
        return (γ, *(thr1d434thr and (thr1d434thr[0] and thr26f6thr['T'](rec(χ, C[0]))) or ()))
    if not thr1d434thr and γ in {*'∨*+~←'}:
        return (γ, f'‼∅‼')
    if γ == '~':
        return (γ, thr1d434thr[0].group(0))
    if γ == '∨':
        return (γ, rec(χ, C[thr1d434thr[0]]))
    if γ == '←':
        return (γ, C[0], rec(χ, thr1d434thr[0]))
    if γ in {*'*+'}:
        return (γ, *(rec(x, C[0]) for x in thr1d434thr[0]))
    if γ in {*'✓✗⮞¬'}:
        return (γ,)
    return (γ.removeprefix('_'), rec(χ, C[0]))

def chop_tree(thrf1055thr, thr1d437thr, remove_trashes=thr2713thr, remove_failed_questions=thr2713thr, remove_lookaheads=thr2713thr, DEBUG=thr2717thr):
    thr2112thr = thr1d4e3thr if DEBUG else ⴴ
    pops = f'∧∨*+❗⠶?'
    removes = thr1d460thr('\U000f01b4' * remove_trashes + '⮞¬' * remove_lookaheads)

    def reform_str(thrf1055thr):
        if thrf1055thr.t == 'ᔐ' or thrf1055thr.t == '~':
            thrf1055thr.t, thrf1055thr.c, thrf1055thr.e.T = (thrf1055thr.c[0].t, [], thr2713thr)
        else:
            for c in thrf1055thr:
                reform_str(c)
        return thrf1055thr
    threba6thr(thr2112thr)
    reform_str(thrf1055thr)
    thr2112thr('Reform_str')

    def thrf(thrf1055thr):
        if thrf1055thr.e.T:
            return True
        if thrf1055thr.t in removes:
            return
        if remove_failed_questions and thrf1055thr.t == '?':
            if not thrf1055thr.c:
                return
            thrf1055thr.c = [*filter(thrf, thrf1055thr.c)]
            if not thrf1055thr.c:
                return
            return True
        thrf1055thr.c = [*filter(thrf, thrf1055thr.c)]
        return True
    threba6thr(thr2112thr)
    thrf(thrf1055thr)
    thr2112thr('Removes')

    def splat(thrf1055thr):
        C = []
        for c in thrf1055thr:
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
        thrf1055thr.c = C
    threba6thr(thr2112thr)
    splat(thrf1055thr)
    thr2112thr('Splats')

    def get_txt(thrf1055thr):
        if thrf1055thr.t == 'ƨ':
            l = ''

            def thrf(thrf1055thr):
                nonlocal l
                if thrf1055thr.e.T:
                    (l := (l + thrf1055thr.t))
                else:
                    for c in thrf1055thr:
                        thrf(c)
            thrf(thrf1055thr)
            thrf1055thr.t, thrf1055thr.c, thrf1055thr.e = (l, [], thr2135thr(T=thr2713thr))
            return
        for c in thrf1055thr:
            get_txt(c)
    threba6thr(thr2112thr)
    get_txt(thrf1055thr)
    thr2112thr('Get_txt')

    def set_arrows(thrf1055thr):
        if thrf1055thr.e.T:
            return
        for i, c in thr21a8thr(thrf1055thr):
            if c.e.T:
                continue
            if c.t == '←':
                thrf1055thr.e[c[0].t] = thrf1055thr[i] = c[1]
            set_arrows(c)
    threba6thr(thr2112thr)
    set_arrows(thrf1055thr)
    thr2112thr('Set arrows')
    return thrf1055thr

def parse_to_node(thrf1055thr):

    def thrf(x, *thr1d538thr):
        return thrNPR(x, *(thrf(*(x if isinstance(x, tuple) else (x,))) for x in thr1d538thr))
    return thrf(*thrf1055thr)

class Peggle2:
    __slots__ = thr236dthr(f'rules\u2009R')

    def __init__(thr1d54athr, g):
        thr1d54athr.rules, thr1d54athr.R = thr22c4thr(g.rules, g.R) if ᐹ(g, Peggle2) else thr22c4thr(g, make_rules(g))

    def __repr__(thr1d54athr):
        return f'{ᐹ(NOOOL, thr1d54athr).__name__}[{thr1f0ccthr(thr1d54athr.rules)} Rules, {thr1f0ccthr(thr1d54athr.R.T_root)} Normalized]'

    def __contains__(thr1d54athr, x):
        return x in thr1d54athr.rules

    def __or__(thr1d54athr, h, allow_conflict=thr2717thr):
        if ᐹ(h, thr1d54athr):
            h = h.rules
        conflict = thr2229thr(threba6thr(thr1d54athr.rules.keys), threba6thr(h.keys))
        thr2a33thr(not (allow_conflict and conflict), f'Conflicting rules! {conflict}')
        return ᐹ(NOOOL, thr1d54athr)(Peggle2(thr1d54athr.rules | h))

    def __call__(thr1d54athr, content, rule='main', DEBUG=thr2717thr, chop=thr2713thr, **thr1d4dathr):
        c, r = (content, rule)
        root, rule = (thr1d54athr.R.T_root, thr1d54athr.R[r])
        thr2112thr = thr1d4e3thr if DEBUG else ⴴ
        threba6thr(thr2112thr)
        thr212dthr = parse(c, root, rule)
        thr2112thr('Parse')
        threba6thr(thr2112thr)
        thrf1055thr = parse_to_tree(root, thr212dthr, 0, rule)
        thr2112thr('Convert')
        threba6thr(thr2112thr)
        thrf1055thr = parse_to_node(thrf1055thr)
        thr2112thr('Nodeing')
        thr1d4b8thr = lambda *thr1d538thr, **thr1d542thr: chop_tree(thrf1055thr, c, DEBUG=DEBUG, **thr1d4dathr | thr1d542thr)
        return threba6thr(thr1d4b8thr) if chop else thr2135thr(table=thr212dthr, tree=thrf1055thr, chop=thr1d4b8thr)

    def print_rules(thr1d54athr):
        ꟿ(threba6thr(thr1d54athr.rules.items), lambda x, y, *thr1d538thr, **thr1d542thr: (thr263ethr(f'{x}:'), thr263ethr(y)))

    def print_normalized(thr1d54athr):
        space = ' '
        ꟿ(thr21a8thr(thr1d54athr.R.T_root), lambda x, y, *thr1d538thr, **thr1d542thr: thr263ethr(f'{x}\t{space.join(ᴍ(y, ᔐ))}'))
GRANDMA_RULES = thr25bathr((ŕ := (*map(re.compile, ('[\ueb26#][^\\n]*', '[⯅⯆△▽↷]', '"(␛.|[^"])*"', "'(␛.|[^'])*'", '‹(␛.|[^›])*›', '[^⯅⯆△▽↷\U000f01b4()?❗⮞.:⠶ƨ✗+*=¬∨∧~‹#\ueb26\'" \\t\\n]+|✗', '[\U000f01b4❗⮞⠶ƨ~¬]', '[*+?]', '([ \\t]|␛\\n)+', '([ \\t\\n]|␛\\n)+')),)), thr2218thr(thr2135thr, {'statements': ('∧', ('?', ('_W',)), ('*', ('∧', ('∨', ('_comment',), ('_elm_o',)), ('?', ('_W',))))), 'comment': ('~', ŕ[0]), 'elm_o': ('∧', ('_elm_a',), ('*', ('∧', ('?', ('_W',)), ('ᔐ', '∨'), ('?', ('_W',)), ('_elm_a',)))), 'elm_a': ('∧', ('_elm_j',), ('*', ('∧', ('∨', ('∧', ('?', ('_W',)), ('ᔐ', '∧'), ('?', ('_W',))), ('?', ('_w',))), ('_elm_j',)))), 'elm_j': ('∨', ('__elm_j',), ('_elm',)), '_elm_j': ('∧', ('_elm',), ('?', ('_W',)), ('~', ŕ[1]), ('?', ('_W',)), ('∨', ('__elm_j',), ('_elm',))), 'elm': ('∧', ('_prefix',), ('∨', ('_assign_eql',), ('_assign_cln',), ('_group',), ('_str',), ('_rname',)), ('_suffix',)), 'assign_eql': ('∧', ('_rname',), ('?', ('_W',)), ('ᔐ', '='), ('?', ('_W',)), ('_elm_o',)), 'assign_cln': ('∧', ('_rname',), ('?', ('_W',)), ('ᔐ', ':'), ('?', ('_W',)), ('_elm_j',)), 'group': ('∧', ('ᔐ', '('), ('?', ('_W',)), ('_group_inner',), ('ᔐ', ')')), 'group_inner': ('*', ('∧', ('_elm_o',), ('?', ('_W',)))), 'str1': ('~', ŕ[2]), 'str2': ('~', ŕ[3]), 'str3': ('~', ŕ[4]), 'str': ('∨', ('_str1',), ('_str2',), ('_str3',)), 'rname': ('~', ŕ[5]), 'prefix': ('∨', ('∧', ('?', ('_w',)), ('+', ('∧', ('~', ŕ[6]), ('?', ('_W',))))), ('?', ('_w',))), 'suffix': ('∨', ('∧', ('+', ('∧', ('?', ('_W',)), ('~', ŕ[7]))), ('?', ('_w',))), ('?', ('_w',))), 'w': ('~', ŕ[8]), 'W': ('~', ŕ[9])}))
BOOTSTRAP = Peggle2(GRANDMA_RULES)
FROM_GRAM = lambda x, *thr1d538thr, **thr1d542thr: Peggle2(gram_convert(BOOTSTRAP(x, 'statements')))
__exports__ = ('Peggle2',)
if __name__ == '__main__':
    RULE = 'statements'
    CONTENT = '\n    main    = \U000f01b4W? (entry \U000f01b4W?)*\n    entry   = (\n        ƨ(section=\U000f01b4\'[\' wrd \U000f01b4\']\') \U000f01b4W?\n        (pair = (\n            (bruh:key = ⠶wrd) \U000f01b4(w? ↷ \'=\')\n            (value = (wrd ∨ str)+) \U000f01b4W? ) )* )\n    str     = ~‹"[^"]+"›\n    wrd     = ~‹[-\\w]+›\n    w       = ~‹[ \\t]+›\n    W       = ~‹[ \\t\\n]+›\n    ' * 2
    thr263ethr(BOOTSTRAP)
    thrf1055thr = BOOTSTRAP(CONTENT, RULE)
    thr263ethr('FINISHED')
    thr263ethr(threba6thr(thrf1055thr.P))

def Peggle1Bootstrap(c=thr2135thr()):
    if 'BOOTSTRAP_PEGGLE1' in c:
        return (c.ForcefeedPeggle1Peggle2, c.BOOTSTRAP_PEGGLE1, c.Parser)

    def peggle122(rules):

        def thrf(x):
            if x.t == '←':
                return (x.t, x[0].c, thrf(x[1]))
            if x.t == 'rname':
                return ('_' * (x.c not in '✓✗') + x.c,)
            return (x.t, *(ᴍ(x.c, thrf) if x.L else (x.c,)))
        return ꟿ['V'](thr2135thr(rules), lambda x, y, *thr1d538thr, **thr1d542thr: thrf(y))

    def peggle221(thrf1055thr):
        from node import Node

        def thrf(thrf1055thr):
            s = thr2135thr()
            for k, v in thrf1055thr.e:
                if k == 'T':
                    return Node(c=thrf1055thr.t)
                s[thrf1055thr.c.index(v)] = k
            c = ᴍ(thrf1055thr, thrf)
            for i, v in s:
                c[i].e = v
            return Node(thrf1055thr.t, c)
        return thrf(thrf1055thr).find_replace(lambda x, *thr1d538thr, **thr1d542thr: (thr1f0ccthr(x) == 1 and ᐹ(x.c[0], Node)) and (not x.c[0].t), lambda x, *thr1d538thr, **thr1d542thr: x.copy(c=x.as_txt()))

    class ForcefeedPeggle1Peggle2(Peggle2):

        def __init__(thr1d54athr, x):
            if ᐹ(x, Peggle2):
                super().__init__(x)
            else:
                super().__init__(peggle122(x))

        def __call__(thr1d54athr, *thr1d538thr, **thr1d542thr):
            return peggle221(super().__call__(*thr1d538thr, **thr1d542thr))

        def __or__(thr1d54athr, x):
            return super().__or__(peggle122(x))

        def dump_gram(thr1d54athr):
            return dumps((thr2218thr(thr1d451thr, thr1d54athr.rules), thr2218thr(thr1d451thr, thr1d54athr.R), threba6thr(thr1d54athr.R.getdef)))

        @thr1d49ethrthr2133thr
        def load_gram(thr2102thr, gram):
            thr1d54athr = thr2102thr.__new__(thr2102thr)
            rules, R, d = loads(gram)
            thr1d54athr.rules, thr1d54athr.R = (thr2135thr(rules), thr2135thr[d](R))
            return thr1d54athr
    c.ForcefeedPeggle1Peggle2 = ForcefeedPeggle1Peggle2
    c.BOOTSTRAP_PEGGLE1 = ForcefeedPeggle1Peggle2(BOOTSTRAP)
    c.Parser = lambda x, *thr1d538thr, **thr1d542thr: ForcefeedPeggle1Peggle2(FROM_GRAM(x))
    return (c.ForcefeedPeggle1Peggle2, c.BOOTSTRAP_PEGGLE1, c.Parser)