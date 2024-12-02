from util import *
from node import *
from PEGGLE2_BOOTSTRAP_AAUGH import Peggle1Bootstrap
Gram, _, Parser = Peggle1Bootstrap()

GRAM_HEADER = ""
CODE_HEADER = """\
from util import *
from node import *
from op import OP\n"""

def join_nodes_flat(t, *N):
    C = []
    for n in N:
        if n.S: C.append(n)
        else  : C.extend(n.C)
    return Node(t, C)

def into_expr(C):
    if ᐹ(C, ᒪ): return join_nodes_flat("expr", *ᴍ(into_expr, C))
    return Node('expr', C if ᐹ(C, ᔐ) else [C])

def make_op_call(op, l, r, op_):
    ch = lambda n: NULL if n is ᗜ else into_expr(n) if ᐹ(n, ᒪ) else n
    return Node("op_call", [ch(l), op_, ch(r)])

class AbsoluteWrapper:
    def __init__(𝕊, *a, **k):
        (𝕊.f, *𝕊.a), 𝕊.k = a, k
    def __call__(𝕊, *a, **k):
        if len(a) == 1 and callable(a[0]):
            return 𝕊.f(a[0], *𝕊.a, **𝕊.k)
        return type(𝕊)(𝕊.f, *a, **k)

class DynamicParser:
    def __init__(𝕊, lang, code_head, code_gen):
        𝕊.lang, 𝕊.generators, 𝕊.grammar_imports = lang, {}, {}
        𝕊.tree_manips = {"replacement": {}, "reduction": {}}
        𝕊.code_namespace = 𝕊.get_namespace_head()
        exec(CODE_HEADER+code_head, 𝕊.code_namespace)
        𝕊.register_tokset("oper_lit", 𝕊.lang.ops.keys())
        𝕊.register_tokset("SUPSCRIPT", SCRIPT.CHAR_SUP, ⴳ)
        𝕊.register_tokset("SUBSCRIPT", SCRIPT.CHAR_SUB, ⴳ)
        𝕊.code_namespace |= 𝕊.get_namespace_gen()
        exec(code_gen, 𝕊.code_namespace)
        for k,v in 𝕊.code_namespace.items():
            if not k.startswith("σ_"):
                continue
            𝕊.parse_manip_layer(k, v)
    
    def __repr__(𝕊):
        return f"{Т(𝕊).__name__}[orders={𝕊.get_orders()}]"
    
    def _apply_tree_manip(𝕊, m, n, order):
        N = n.copy()
        if m.rec and 'B' in m.rec and not N.S:
            N.c = 𝕊.lang_tree_manip(Node('∅', N.c), order).c
        N = m(N)
        if ᐹ(N, ᒪ):
            N = Node('∅', N)
            if m.rec and 'A' in m.rec and not N.S:
                return 𝕊.lang_tree_manip(N, order).c
            return N.c
        else:
            if m.rec and 'A' in m.rec and not N.S:
                N.c = 𝕊.lang_tree_manip(N.copy('∅'), order).c
            return N
    
    def lang_tree_manip(𝕊, N, order):
        if m := 𝕊.get_manip("replacement", order, N.t):
            return 𝕊._apply_tree_manip(m, N, order)
        if N.S:
            return N
        
        cc = []
        for n in N.C:
            if m := 𝕊.get_manip("reduction", order, n.t):
                h = 𝕊._apply_tree_manip(m, n, order)
                cc.extend(h)
            else:
                cc.append(𝕊.lang_tree_manip(n, order))
        return N.copy(c=cc)
    
    def parse_manip_layer(𝕊, f_n, f):
        o_num, manips = int(f_n.split('_', 1)[1]), []
        it = iter(f())
        
        if ᐹ(α := next(it), ᔐ):
            α, pfx = next(it), f"{α}: "
        else:
            pfx = ᐦ
        
        while it:
            h = Holder()
            try:
                β = it.send(h.s)
            except StopIteration:
                break
            finally:
                manips.append((h.A[0], α))
            α = β
        
        order = (o_num, pfx+ᒍ(" | ", (m[1].K.pop(*"n□") for m in manips)))
        for f, (a, k) in manips:
            𝕊.add_manip(k.pop("type"), f, *a, order=order, **k)
    def add_manip(𝕊, type, f, *names, rec=ⴴ, order=1):
        f.rec = rec
        𝕊.tree_manips[type].setdefault(order, {})
        for name in names:
            𝕊.tree_manips[type][order][name] = f
    def get_manip(𝕊, T, order, t):
        if s := 𝕊.tree_manips[T].get(order):
            return s.get(t)

    def general_tree_manip(𝕊, n): # metasyntactical manipulations
        n = n.copy()
        if not n.S: n.c = ᴍ(𝕊.general_tree_manip, n.c)
        return n
    
    def get_orders(𝕊):
        return sorted(set.union(*(set(x.keys()) for x in 𝕊.tree_manips.values())))
    
    def tree_transform(𝕊, n, max_order=99999):
        n = 𝕊.general_tree_manip(n)
        if DEBUG: (print(f"{Z.red}{'-'*100}{Z.wh}"), n.print())
        for order in 𝕊.get_orders():
            if order[0] >= max_order:
                if DEBUG: print(f"{Z.pu} {order[0]} >= {max_order}, stopping.")
                break
            if DEBUG: print(f"{Z.bpu}+{Z.bbla} {Z.pu}{'-'*10}{Z.wh} {order}")
            n = 𝕊.lang_tree_manip(n, order)
            if DEBUG: n.print()
        if DEBUG: print(f"{Z.red}{'-'*100}{Z.wh}")
        return n
    
    def add_generator(𝕊, f, *names):
        for name in names:
            𝕊.generators[name] = f
    def gen(𝕊, n):
        if n.t in 𝕊.generators:
            return 𝕊.generators[n.t](n)
        return n.c if n.S else ᒍ(ᐦ, ᴍ(𝕊.gen, n.c))
    
    def format_grammar_toks(𝕊, toks):
        return rgx_or(sorted(toks, key=ⵌ, reverse=ⴳ))
    def register_tokset(𝕊, name, toks, conseq=ⴴ):
        𝕊.code_namespace[name] = toks
        if all(len(t) == 1 for t in toks):
            res = f"[{ᒍ(ᐦ, ((t in ']\\-')*'\\'+t for t in toks))}]{ᖲ(conseq)*'+'}"
        else:
            res = 𝕊.format_grammar_toks(toks)
        𝕊.grammar_imports[name] = res
    
    def parse_gram(𝕊, gram):
        new_rules = { i:Node('~', re.compile(v)) for i,v in 𝕊.grammar_imports.items() }
        return Parser(gram) | new_rules
    
    def get_namespace_head(𝕊):
        return {
            "register": 𝕊.register_tokset,
              "op_man": 𝕊.lang.op_man,
                "lang": 𝕊.lang }
    def get_namespace_gen(𝕊):
        return {
            "replacement": lambda *a,**k:Holder().s(*a,type="replacement",**k),
              "reduction": lambda *a,**k:Holder().s(*a,type="reduction"  ,**k),
              "generator": AbsoluteWrapper(𝕊.add_generator),
             "parse_expr": 𝕊.lang.op_man.parse_expr,
              "into_expr": into_expr,
                   "gram": lambda *a,**k: 𝕊.lang.gram(*a,**k),
         "tree_transform": 𝕊.tree_transform,
                    "gen": 𝕊.gen } | 𝕊.get_namespace_head()