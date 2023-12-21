from mapping import *

_OP_TYPES = "NPSB"
class OP:
    __slots__ = tuple("tvLRf")
    _and = staticmethod(lambda x, y: x & 1 << _OP_TYPES.index(y))
    _or  = staticmethod(lambda x, y: x | 1 << _OP_TYPES.index(y))
    
    @classmethod
    def is_op(ℂ, n, ops=ℕ):
        if not isinstance(n, Node) or not n.expr_name == "oper":
            return 𝔽
        
        L, base, R = O = n.children
        base = base.text
        
        if '´' in R.text:
            return 𝔽
        return L, base, R
    
    def __init__(𝕊, t, v="", L=ℕ, R=ℕ, f=ℕ):
        𝕊.t, 𝕊.v, 𝕊.L, 𝕊.R, 𝕊.f = t, reduce(𝕊._or, v, 0), L or [], R or [], f or print
    
    def __repr__(𝕊):
        return f"⟨{𝕊.t},{bin(𝕊.v)[2:].zfill(len(_OP_TYPES))[::-1]}⟩"
    
    def __getattr__(𝕊, a):
        if a == 'M': # unary works as prefix AND suffix
            return 𝕊.P and 𝕊.S
            
        if all(map(_OP_TYPES.__contains__, a)):
            return any(map(𝕊._and, [𝕊.v]*len(_OP_TYPES), a))
        raise AttributeError
    
    def __eq__(𝕊, n):
        O = L, base, R = 𝕊.is_op(n)
        if base.text != 𝕊.t:
            return 𝔽
        return O
    
    def __call__(𝕊, L=ℕ, R=ℕ):
        assert 𝕊.check_args(L, R), "Invalid args for op!"
        return 𝕊.f(L, R)
    
    def check_args(𝕊, L=ℕ, R=ℕ):
        l, r = L is not ℕ, R is not ℕ
        if l and r:
            return 𝕊.B
        if l or r:
            return 𝕊.P and R or L and 𝕊.S
        return 𝕊.N
    
    def part(𝕊, nodes, d):
        assert d in "lr"
        
        i = 0
        if d == 'r': # this code brings me fear
            stack = [𝕊.R]
            for i, n in enumerate(nodes):
                if O := 𝕊.is_op(n):
                    while stack:
                        if O[1] in stack[-1]:
                            stack += [GRAB_OP_FROM_NODE(O).R]
                            break
                        stack.pop()
                    if not stack:
                        break
            else:
                i += 1
        elif d == 'l':
            for i, n in [*enumerate(nodes)][::-1]:
                if O := 𝕊.is_op(n):
                    if O[1] not in 𝕊.L:
                        break
        return nodes[:i], nodes[i:]

def apply_op(op, L, R):
    ll, lr = op.part(L, 'l')
    rl, rr = op.part(R, 'r')
    
    P(1, f"{L} │{op}│ {R}")
    P(2, f"{ll} ⟨{lr} │ {op} │ {rl}⟩ {rr}")
    
    if op.B and lr and rl: # Binary
        return ll + [op(lr, parse(rl))], rr
    if op.S and lr: # Suffix
        return ll + [op(lr, ℕ)], rr
    if op.P and rl: # Prefix
        return ll + [op(ℕ, parse(rl))], rr
    if op.N: # Nullary
        return ll + [op(ℕ, ℕ)], rr
    assert 𝔽

def parse(n):
    PD(1, "PARSE", n)
    L, R = [], n.copy()
    while R:
        c = R.pop(0)
        P(f"STACKS: {L=} │{c}│ {R=}")
        if O := OP.is_op(c):
            op = GRAB_OP_FROM_NODE(O)
            L, R = apply_op(op, L, R)
        else:
            L += [c]
    PD(-1, L+R)
    return L + R

def o(t):
    return Node(ℕ, "oper", [
        Node(expr_name='oper_mod_l'),
        Node(t, 'oper_literal'),
        Node(expr_name='oper_mod_r')])
def v(t):
    return Node(t, 'v')
def GRAB_OP_FROM_NODE(n):
    k=lambda x: ''.join(map(str,x))if isinstance(x,list)else b
    match n[1]:
        case '≔': return OP('≔', "B", R='+⋅≔',
                f=lambda a, b: f"⟨{k(a)}≔({k(b)})⟩")
        case '+': return OP('+', "B", L='⋅', R='⋅≔',
                f=lambda a, b: f"({k(a)}+{k(b)})")
        case '⋅': return OP('⋅', "B", R='≔',
                f=lambda a, b: f"({k(a)}⋅{k(b)})")

p = "2⋅a≔2+c≔3⋅2+5"
p = [o(i) if i in "⋅+≔" else v(i) for i in "2⋅a≔2+c≔3⋅2+5"]
p = parse(p)
print(*p)