⮌ collections ⨡ deque
⮌ pprint ⨡ PrettyPrinter
⊢ ASSERT_(c,t='\U00002a33'): »c,t; ↪c
pprint = PrettyPrinter(2).pprint
DEGEN_=g↦deque(g,maxlen=0)
EMPTY_STRING, COMPLEX_UNIT = '', 1j
MATH_PI, MATH_TAU = 3.14159265359, 6.28318530718
Ω Namespace:
    __init__ = 𝕊↦𝕂.keys()⨯⚇|🜌(𝕊)|⚇⨯𝕂.values()
    __setitem__ = ⥌𝕊,k,v↦setattr(𝕊,k,v)
    __getitem__ = ⥌𝕊,k↦getattr(𝕊,k)
    __iter__ = 𝕊↦iter(🢖__dict__.items())
    __repr__ = 𝕊↦‹ℕ({(', '.join(‹{k}={v}› ∀k,v∈🢖__dict__.items()))})›
Ω pait:
    ⨡ subprocess as SP
    ⊢ __call__(𝕊,s,⠤𝔸,⠶𝕂):
        proc = 𝕊.SP.Popen(s.split(' '),⠤𝔸,⠶𝕂)
        ↪ (proc.wait()∧𝔽 ¿ "background"∉𝕂) ∨ proc
    _parse = 𝕊,o↦o.read().decode()
    r = 𝕊↦𝕊(⠤𝔸,⠶𝕂).return_code
    S = 𝕊↦𝕊._parse(𝕊(⠤𝔸,stdout=𝕊.SP.PIPE,⠶𝕂).stdout)
    E = 𝕊↦𝕊._parse(𝕊(⠤𝔸,stderr=𝕊.SP.PIPE,⠶𝕂).stderr)
    b = 𝕊↦𝕊(⠤𝔸,background=𝕋,stdout=𝕊.SP.PIPE,stderr=𝕊.SP.PIPE,⠶𝕂)
    ⊢ B(𝕊,⠤𝔸,⠶𝕂):
        o = 𝕊(⠤𝔸,stdout=𝕊.SP.PIPE,stderr=𝕊.SP.PIPE,⠶𝕂)
        ↪ 𝕊._parse(o.stdout), 𝕊._parse(o.stderr)
    ⊢ A(𝕊,⠤𝔸,⠶𝕂):
        o = 𝕊(⠤𝔸,stdout=𝕊.SP.PIPE,stderr=𝕊.SP.PIPE,⠶𝕂)
        ↪ o.return_code, 𝕊._parse(o.stdout), 𝕊._parse(o.stderr)
pait = pait()