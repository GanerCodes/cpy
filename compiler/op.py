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
    def __eq__(𝕊, n):
        O = L, base, R = 𝕊.is_op(n)
        return O if base.as_txt() == 𝕊.t else False
    def __call__(𝕊, L, R, op_):
        assert 𝕊.check_args(L, R), "Invalid args for op!"
        return 𝕊.f(L, R, op_)
    def __getattr__(𝕊, a):
        if a == 'M': return 𝕊.P and 𝕊.S
        if ⴷ(ᴍ(_OP_TYPES.__contains__, a)):
            return ⴸ(ᴍ(𝕊._and, [𝕊.v]*ⵌ(_OP_TYPES), a))
        raise AttributeError
    
    copy = lambda 𝕊             : Т(𝕊)(𝕊.t, 𝕊.v, 𝕊.L.copy(), 𝕊.R.copy(), 𝕊.f)
    mod  = lambda 𝕊, v, L=ᗜ, R=ᗜ: Т(𝕊)(𝕊.t, v, 𝕊.L if L is None else 𝕊.L,
                                               𝕊.R if R is None else 𝕊.R, 𝕊.f)
    
    @classmethod
    def TND(ℂ, s, l=ᐦ, r=ᐦ):
        return Ń("oper", ("oper_mod_l", l), ("oper_lit", s), ("oper_mod_r", r))
    
    @classmethod
    def is_op(ℂ, n, ops=ᗜ):
        if not ᐹ(n,Node) or not n.t=="oper": return ⴴ
        
        L, base, R = O = n.C
        base = base.as_txt()
        
        if R.S and '´' in R.as_txt(): return ⴴ
        return L, base, R
    
    def check_args(𝕊, L=ᗜ, R=ᗜ):
        l, r = L is not ᗜ, R is not ᗜ
        if l and r: return 𝕊.B
        if l  or r: return 𝕊.P and R or L and 𝕊.S
        return 𝕊.N
    
    def part(𝕊, nodes, d, op_man):
        assert d in "lr"
        
        i = 0
        if d == 'r': # 󷹇 this code is scary!!1
            stack = [𝕊.R]
            for i, n in enum(nodes):
                O = 𝕊.is_op(n)
                if not O: continue
                l, op_t, r = O
                
                while stack:
                    # print(f"{n=} {op_man[n]=}")
                    pretend_op = op_t
                    if '≺' in l.as_txt():
                        pretend_op = 'ᴍ' # 󷹇 stupid
                    if pretend_op in stack[-1]:
                        stack += [op_man[n].R]
                        break
                    
                    # 󷹇 weird
                    if (𝕊.P or (𝕊.B and not 𝕊.S)) \
                            and op_man[n].t in op_man.table["⨳"].R \
                            and op_man[n].P \
                            and i == 0:
                        stack += [op_man[n].R]
                        break
                        
                    stack.pop()
                else:
                    break
            else:
                i += 1
        elif d == 'l':
            for i, n in [*enum(nodes)][::-1]:
                O = 𝕊.is_op(n)
                if not O: continue
                l, op_t, r = O
                if op_t not in 𝕊.L: break
        return nodes[:i], nodes[i:]
        
    def apply(𝕊, L, R, op_man, op_):
        # print(f"{L=} {op_=} {R=}")
        ll, lr = 𝕊.part(L, 'l', op_man)
        rl, rr = 𝕊.part(R, 'r', op_man)
        # print("ll", ll)
        # print("lr", lr)
        # print(𝕊)
        # print("rl", rl)
        # print("rr", rr)
        
        if rl: rl = op_man.parse_expr(rl)
        
        if 𝕊.B and lr and rl: return ll + [𝕊(lr, rl, op_)], rr # Binary
        if 𝕊.S and lr       : return ll + [𝕊(lr,  ᗜ, op_)], R  # Suffix
        if 𝕊.P        and rl: return L  + [𝕊(ᗜ , rl, op_)], rr # Prefix
        if 𝕊.N              : return L  + [𝕊(ᗜ ,  ᗜ, op_)], R  # Nullary
        
        assert ⴴ, f"Unable to apply operator {𝕊}: {ll=}; {lr=}; {rl=}; {rr=}"

class OP_Manager:
    __slots__ = "table", 

    def __init__(𝕊, table):
        𝕊.table = table
    def __repr__(𝕊):
        return f"{Т(𝕊).__name__}[table={𝕊.table}]"
    def __getitem__(𝕊, n):
        if not (n := OP.is_op(n)):
            return
        L, op_t, R = n
        op = 𝕊.table[op_t]
        return 𝕊.gen_op(L, op, R)
    
    def gen_op(𝕊, l, op, r):
        assert l.t == "oper_mod_l"
        for u in l.as_txt():
            if   u == '⟥':
                assert op.B
                op = op.mod(op.N*'N'+"P")
            elif u == '≺':
                assert op.B
                op = op.mod(op.N*'N'+"S")
            else:
                assert ⴴ
        
        if r.t != "oper_mod_r": return op
        
        for u in r.as_txt():
            if   u == '꜠':
                assert op.B
                op = op.mod(op.N*'N' + "PS")
            elif u == 'ᵜ':
                if op.P or op.S:
                    op = op.mod(op.N*'N' + op.P*'S' + op.S*'P' + op.B*'B', op.R, op.L)
            elif u == '⟤':
                assert op.B
                op = op.mod(op.N*'N' + 'S')
            # 󷹇 postfix modifiers can be dynamic
        return op
    
    def parse_expr(𝕊, n):
        # print("parse_expr:")
        # for x in n: x.print()
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