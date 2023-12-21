from parsimonious.grammar import Grammar
from collections import namedtuple as NT
from functools import reduce, partial
import regex as re
from sys import setrecursionlimit
setrecursionlimit(10_000_00)

𝕋, 𝔽, ℕ = True, False, None
R = lambda x: open(x).read()
HX = lambda c: hex(ord(c))[2:]
flat = lambda x: reduce(lambda x,y: x+y, l:=list(x), type(l[0])() if len(l) else [])
rgx_or = lambda x: '(' + ')|('.join(x) + ')'
i_rgx_fmt = lambda x: x.replace('"', '\\"').replace('\\', '\\\\')
reach_first = lambda x: reach_first(x[0]) if isinstance(x, list) and len(x)==1 else x
collapse = lambda x: x if isinstance(x:=reach_first(x), list) else [x]

OP = NT("op", [*"tBNPSA"], defaults=['']+[𝔽]*5)

V=0
def PD(n,*a,**k): global V ; V += n ; print(' '*(V-1+(n<0))+'|'+('←→'[n>0] if n else ' '),*a,**k)
P = partial(PD, 0)

class Node:
    def reparse(𝕊): ...
    @classmethod
    def metaop_change_type(ℂ, L, op, R): ...
    @classmethod
    def gen_op(ℂ, op_, op, L=ℕ, R=ℕ): ...
    
    __slots__ = ("text", "expr_name", "children")
    
    def __init__(𝕊, text, expr_name, children=None):
        𝕊.text = text
        𝕊.expr_name = expr_name
        𝕊.children = children or []
    
    def __repr__(𝕊):
        return f'{𝕊.expr_name}⟨"{𝕊.text}"⟩'
    
    def reduce(𝕊):
        if 𝕊.expr_name and 𝕊.expr_name == "var":
            return type(𝕊)(𝕊.text, 𝕊.expr_name, [])
        return type(𝕊)(𝕊.text, 𝕊.expr_name, flat(
                    [C_] if (C_:=c.reduce()).expr_name else
                    (C_.children or [type(𝕊)(C_.text, "s", [])]) 
                for c in 𝕊.children))
    
    def collapse(𝕊):
        n = type(𝕊)(𝕊.text, 𝕊.expr_name, [C_ for c in 𝕊.children if (C_:=c.collapse()).text.strip()])
        if len(n.children) == 1:
            c = n.children[0]
            return type(𝕊)(𝕊.text, 𝕊.expr_name+':'+c.expr_name, c.children)
        return n
    
    def print(𝕊, s='', clean=lambda x: x.replace('\n','ñ')):
        print(f"{s}{𝕊.expr_name} ► {clean(𝕊.text)}")
        if 𝕊.children and all(c.expr_name == 's' for c in 𝕊.children):
            return print(s+'  '+"S-CHAIN: "+'­—'.join(clean(c.text) for c in 𝕊.children))
        [c.print(s+'  ') for c in 𝕊.children]
    
    @classmethod
    def basic_trim_check(ℂ, c):
        return c.text or c.expr_name in ("oper_mod_l", "oper_mod_r")
    
    @classmethod
    def name_filter(ℂ, n):
        return n and not n.startswith('_') and n not in ("expr", )
    
    @classmethod
    def metaop_change_type(ℂ, l, op, r):
        l, r = l.text, r.text
        for u in l:
            match u:
                case '⟥':
                    assert not r and (op.B or op.N)
                    op = OP(op.t, 0, 0, 1, 1)
                case _: assert 𝔽
        for u in r:
            match u:
                case '꜠':
                    assert op.B or op.N
                    op = OP(op.t, 0, 0, 1, 1)
                case 'ᵜ':
                    if any((x:=op.P, y:=op.S)):
                        op = OP(op.t, op.B, op.N, y, x)
                case _: assert 𝔽
        return op
    
    @classmethod
    def from_grammar(ℂ, n):
        return ℂ(n.text,
            n.expr_name if ℂ.name_filter(n.expr_name) else "",
            [C_ for c in n.children if ℂ.basic_trim_check(C_:=ℂ.from_grammar(c))])
    
    @classmethod
    def valid_op_args(ℂ, op, L, R):
        return (op.B or op.N) and L and R or op.P and L and not R or op.S and R and not L or \
            not (op.B or op.N or op.P or op.S or L or R)
    
    @classmethod
    def is_op(ℂ, op_, layer):
        if not (isinstance(op_, ℂ) and op_.expr_name == "oper"):
            return
        L, base, R = op_.children
        if '´' in R.text:
            return
        if base.text in layer:
            return L, base, R
    
    @classmethod
    def get_op(ℂ, op_, layer):
        if not (O := ℂ.is_op(op_, layer)):
            return
        L, base, R = O
        
        op = layer[base.text]
        return op_, ℂ.metaop_change_type(L, op, R)
    
    @classmethod
    def partition(ℂ, l, f, m=lambda x: x, n=lambda x: 𝕋, keep_sep=𝕋):
        r, b = [], []
        for c in filter(n, l):
            if f(c):
                if b:
                    r.append(m(b))
                    b = []
                if keep_sep:
                    r.append(c)
            else:
                b.append(c)
        if b:
            r.append(m(b))
        return r
    
    into_expr = classmethod(lambda ℂ, C_, s=' ', t="expr": ℂ(s.join(c.reparse() for c in C_), t))
    not_whitespace = classmethod(lambda ℂ, x: x.expr_name != "w")
    
    @classmethod
    def parse_layer(ℂ, stack, layer, layers): # intentionally super verbose
        res = []
        while stack:
            c_l = stack.pop(0)
            
            if O := ℂ.get_op(c_l, layer): # Σ
                op_, op = O
                
                if not stack or not op.P: # ¬Σε ∨ ¬Σ󰂢
                    res.append(ℂ.gen_op(*O))
                    continue
                
                c_m = stack.pop(0)
                if ℂ.is_op(c_m, layer): # ΣΓ weird
                    res.append(ℂ.gen_op(*O))
                    stack[0:0] = [ℂ.gen_op(*O, R=c_m)]
                
                stack[0:0] = [ℂ.gen_op(*O, R=c_m)] # Σ𝑥
                continue
            
            if not stack: # 𝑥ε
                res += collapse(c_l)
                continue
            
            c_m = stack.pop(0)
            if not ℂ.is_op(c_m, layer): # 𝑥𝑦
                res += collapse(c_l)
                stack[0:0] = [c_m]
                continue
            
            O = op_, op = ℂ.get_op(c_m, layer)
            if not stack: # 𝑥Σε
                if op.S:
                    stack[0:0] = [ℂ.gen_op(*O, L=c_l)]
                    continue
                
                # weird
                res += collapse(c_l)
                stack[0:0] = [c_m]
                continue
            
            c_r = stack.pop(0)
            if ℂ.is_op(c_r, layer): # 𝑥ΣΓ
                if op.S:
                    stack[0:0] = [ℂ.gen_op(*O, L=c_l), c_r]
                    continue
                
                # weird
                res += collapse(c_l)
                stack[0:0] = [c_m, c_r]
                continue
            
            if op.B: # 𝑥Σ𝑦 (Blocking)
                stack[0:0] = [ℂ.gen_op(*O, c_l, c_r)]
                continue
            if op.N: # 𝑥Σ… (Nonblocking)
                stack[0:0] = [c_r]
                right = ℂ.parse_exprs(collapse(stack), layers)
                stack = [ℂ.gen_op(*O, c_l, right)]
                continue
            
            # weird
            res += collapse(c_l)
            stack[0:0] = [c_m, c_r]
        
        return collapse(res)
    
    @classmethod
    def process_arrow_operators(ℂ, n, layers=ℕ):
        layer, *nlayers = layers or ℂ.arrows
        if nlayers:
            n = ℂ.process_arrow_operators(n, nlayers)
        
        is_arrow = lambda x: isinstance(x, ℂ) and x.expr_name == "oper" and x.text in layer
        into_group = lambda x: ℂ('(' + (ex:=''.join(y.text for y in x)) + ')', "group", [ℂ('(', 's'), ℂ(ex, "expr", x), ℂ(')', 's')])
        
        stack = ℂ.partition(n.copy(), is_arrow, n=ℂ.not_whitespace)
        res = []
        while stack:
            c_l = stack.pop(0)
            print(f"ADSOIJ {c_l=}")
            print(f"ADSOIJ {stack=}")
            print(f"ADSOIJ {res=}")
            if is_arrow(c_l): # left arrows
                A, S = layer[c_l.text]
                assert A.P and stack
                c_r = stack.pop(0)
                print(S)
                val, *vals = ℂ.partition(c_r, partial(ℂ.is_op, layer=S))
                stack[0:0] = [[into_group(val), *vals]]
            else: # obj
                if not stack:
                    res += c_l
                    continue
                
                c_r = stack.pop(0)
                if not is_arrow(c_r):
                    stack[0:0] = [c_l + c_r]
                    continue
                
                A, S = layer[c_r.text]
                if not A.S: # not right arrow
                    res += c_l
                    stack[0:0] = [c_r]
                    continue
                
                *vals, val = ℂ.partition(c_l, partial(ℂ.is_op, layer=S))
                stack[0:0] = [[*vals, into_group(val)]]
                
            # res += c_l
        print(f"RETURN {res=}")
        return res
    
    @classmethod
    def parse_exprs(ℂ, n, layers=ℕ):
        if layers is ℕ:
            n = ℂ.process_arrow_operators(n)
            print(n)
        
        if layers == []:
            return ℂ.into_expr(n)
        
        layer, *nlayers = layers or ℂ.ops
        get_layer_op = partial(ℂ.get_op, layer=layer)
        
        # Skip order if no relevent ops, ~2.5x speedup
        if not any(map(get_layer_op, n)):
            return ℂ.parse_exprs(n, nlayers)
        
        subparse = partial(ℂ.parse_exprs, layers=nlayers)
        stack = ℂ.partition(n.copy(), get_layer_op, subparse, ℂ.not_whitespace)
        
        res = ℂ.parse_layer(stack, layer, layers)
        expr = ℂ.into_expr(res)
        return expr

class Mapper:
    SPECIALS = ...
    GRAM_FILE = ...
    OPERATOR_FILE = ...
    NODE_CLS = ...
    
    @classmethod
    def generate_gram_regexes(𝕊, op_names): ...
    
    def __init__(𝕊):
        𝕊.gram, 𝕊.ops, 𝕊.arrows = 𝕊.parse_gram(type(𝕊).GRAM_FILE, type(𝕊).OPERATOR_FILE)
        𝕊.NODE_CLS.ops, 𝕊.NODE_CLS.arrows = 𝕊.ops, 𝕊.arrows
    
    @classmethod
    def parse_operators_file(ℂ, f, *, r=re.compile(r"(?P<op>[^\sα]+)(?P<mod>[α]*)".replace('α', "ᴮᴺᐟ˜ᴬ󰂢󰂥⸝"))):
        make_op = lambda x: OP(x[0], *([1*bool(set(x[1]) & set(y)) for y in "ᴮ˜ ᴺ 󰂢 󰂥 ᴬ".split(' ')] if x[1] else (1,0,0,0,0)))
        txt = R(f).split('\n')
        return [{a[0]:make_op(a) for a in r.findall(x)} for i in txt if (x:=i.split('')[0].strip())]
    
    @classmethod
    def parse_arrows(ℂ, layers):
        arrows = [{}]
        splitting_ops = set()
        for i, v in reversed(tuple(enumerate(layers))):
            splitting_ops |= set(v)
            for s, op in tuple(v.items()):
                if not op.A: continue
                arrows[-1][s] = (op, splitting_ops.copy())
                del v[s]
                if not v: del layers[i]
            if arrows[-1]:
                arrows += [{}]
        return layers, arrows[:-1]
    
    @classmethod
    def parse_gram(ℂ, gram_f, op_f):
        ops = ℂ.parse_operators_file(op_f)
        ops, arrows = ℂ.parse_arrows(ops)
        op_names = sorted(flat([*l.keys()] for l in (ops+arrows)), key=len, reverse=𝕋)
        grammar_regexes = ℂ.generate_gram_regexes(op_names)
        gram = R(gram_f)
        for f, r in grammar_regexes.items():
            gram = gram.replace('%'+f+'%',r)
        return Grammar(gram), ops, arrows
    
    def clean_comments(𝕊, content):
        parsed = 𝕊.NODE_CLS.from_grammar(𝕊.gram['parser_comment'].parse(content)).reduce()
        return flat(c.text for c in parsed.children if c.expr_name != 'comment')

    def __call__(𝕊, f):
        content = 𝕊.gram.parse(𝕊.clean_comments(R(f)))
        return 𝕊.NODE_CLS.from_grammar(content)
    
    parse_file = __call__