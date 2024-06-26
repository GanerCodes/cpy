from util import *
from node import *

_OP_TYPES = "NPSB"
class OP:
    __slots__ = tuple("tvFLRf")
    _and = SMD(lambda x, y: x & 1 << _OP_TYPES.index(y))
    _or  = SMD(lambda x, y: x | 1 << _OP_TYPES.index(y))
    
    def __init__(𝕊, t, v=ᐦ, L=ᗜ, R=ᗜ, f=print):
        v, F = set(ᖵ(lambda x: x in _OP_TYPES, v)), \
               set(ᖵ(lambda x: x not in _OP_TYPES, v))
        𝕊.t, 𝕊.v, 𝕊.F = t, reduce(𝕊._or, v, 0), F
        𝕊.L, 𝕊.R, 𝕊.f = L or set(), R or set(), f
    def __contains__(𝕊, v): return v in 𝕊.F
    def __repr__(𝕊): return f"⟨{𝕊.t}│{bin(𝕊.v)[2:].zfill(ⵌ(_OP_TYPES))[::-1]}{f"│{𝕊.F}⟩" if 𝕊.F else '⟩'}"
    def __getattr__(𝕊, a):
        if a == 'M': # unary works as prefix AND suffix
            return 𝕊.P and 𝕊.S
            
        if ⴷ(ᴍ(_OP_TYPES.__contains__, a)):
            return ⴸ(ᴍ(𝕊._and, [𝕊.v]*ⵌ(_OP_TYPES), a))
        raise AttributeError
    
    def __eq__(𝕊, n):
        O = L, base, R = 𝕊.is_op(n)
        if base.txt != 𝕊.t:
            return ⴴ
        return O
    
    def __call__(𝕊, L, R, op_):
        assert 𝕊.check_args(L, R), "Invalid args for op!"
        return 𝕊.f(L, R, op_)
    
    def copy(𝕊): return Т(𝕊)(𝕊.t, 𝕊.v, 𝕊.L.copy(), 𝕊.R.copy(), 𝕊.f)
    def mod(𝕊, v): return Т(𝕊)(𝕊.t, v, 𝕊.L, 𝕊.R, 𝕊.f)
    
    @classmethod
    def TND(ℂ, s, l=ᐦ, r=ᐦ):
        return Ń("oper", 
            ("oper_mod_l", l or Node(ᐦ)),
            ("oper_lit"  , s),
            ("oper_mod_r", r or Node(ᐦ)))
    
    @classmethod
    def is_op(ℂ, n, ops=ᗜ):
        if not ᐹ(n, Node) or not n.t == "oper":
            return ⴴ
        
        L, base, R = O = n.C
        base = base.txt
        
        if '´' in R.txt:
            return ⴴ
        return L, base, R
    
    def check_args(𝕊, L=ᗜ, R=ᗜ):
        l, r = L is not ᗜ, R is not ᗜ
        if l and r:
            return 𝕊.B
        if l or r:
            return 𝕊.P and R or L and 𝕊.S
        return 𝕊.N
    
    def part(𝕊, nodes, d, op_man):
        assert d in "lr"
        
        i = 0
        if d == 'r': # this code is scary!!1
            stack = [𝕊.R]
            for i, n in enum(nodes):
                O = 𝕊.is_op(n)
                if not O: continue
                _, op_t, _ = O
                
                while stack:
                    if op_t in stack[-1]:
                        stack += [op_man[n].R]
                        break
                    stack.pop()
                if not stack: break
            else:
                i += 1
        elif d == 'l':
            for i, n in [*enum(nodes)][::-1]:
                O = 𝕊.is_op(n)
                if not O: continue
                _, op_t, _ = O
                
                if op_t not in 𝕊.L: break
        return nodes[:i], nodes[i:]
        
    def apply(𝕊, L, R, op_man, op_):
        ll, lr = 𝕊.part(L, 'l', op_man)
        rl, rr = 𝕊.part(R, 'r', op_man)
        
        if rl: rl = op_man.parse_expr(rl)
        
        if 𝕊.B and lr and rl: return ll + [𝕊(lr, rl, op_)], rr # Binary
        if 𝕊.S and lr       : return ll + [𝕊(lr,  ᗜ, op_)], R  # Suffix
        if 𝕊.P and rl       : return L  + [𝕊(ᗜ , rl, op_)], rr # Prefix
        if 𝕊.N              : return L  + [𝕊(ᗜ ,  ᗜ, op_)], R  # Nullary
        
        assert ⴴ, f"Unable to apply operator {𝕊}: {ll=}; {lr=}; {rl=}; {rr=}"

class OP_Manager:
    def __init__(𝕊, table):
        𝕊.table = table
    
    def __getitem__(𝕊, n):
        L, op_t, R = OP.is_op(n)
        op = 𝕊.table[op_t]
        return 𝕊.gen_op(L, op, R)
    
    def __repr__(𝕊):
        return f"{Т(𝕊).__name__}[table={𝕊.table}]"
    
    def gen_op(𝕊, l, op, r):
        l, r = l.txt, r.txt
        for u in l:
            match u:
                case '⟥':
                    assert op.B and not r
                    op = op.mod(op.N*'N'+"S")
                case _:
                    assert ⴴ
        for u in r:
            match u:
                case '꜠':
                    assert op.B
                    op = op.mod(op.N*'N'+"PS")
                case 'ᵜ':
                    if ⴸ((x:=op.P, y:=op.S)):
                        op = op.mod(op.N*'N'+y*'S'+x*'P'+op.B*'B')
                # we now have custom mods
                # case _:
                    # assert ⴴ
        return op
    
    def parse_expr(𝕊, n):
        # PD(1, "PARSE", n)
        L, R = [], n.copy()
        while R:
            c = R.pop(0)
            # PD(0, f"STACKS: {L=} │{c}│ {R=}")
            if O := OP.is_op(c):
                L, R = 𝕊[c].apply(L, R, 𝕊, c)
            else:
                L += [c]
        # PD(-1, L+R)
        return L + R