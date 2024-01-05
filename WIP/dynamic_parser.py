from util import *
from node import *
from parsimonious.grammar import Grammar

GRAM_HEADER = ""
CODE_HEADER = """\
from util import *
from node import *
from op import OP\n"""

def join_nodes_flat(t, *N):
    C = []
    for n in N:
        if n.S:
            C.append(n)
        else:
            C.extend(n.C)
    return Node(t, C)

def into_expr(C):
    if ᐹ(C, ᒪ):
        return join_nodes_flat("expr", *ᴍ(into_expr, C))
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
    def _apply_tree_manip(𝕊, m, n, order):
        N = n.copy()
        if m.recurse_children == 'B' and not N.S:
            N.c = ᴍ(ρ(𝕊.lang_tree_manip, order=order), N.c)
        N = m(N)
        if ᐹ(N, ᒪ):
            N = Ń('∅', *N)
            if m.recurse_children == 'A' and not N.S:
                return 𝕊.lang_tree_manip(N, order).c
            return N.c
        else:
            if m.recurse_children == 'A' and not N.S:
                N.c = ᴍ(ρ(𝕊.lang_tree_manip, order=order), N.c)
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
        return Node(N.t, cc)
    
    def add_manip(𝕊, type, f, *names, recurse_children=ⴴ, order=1):
        f.recurse_children = recurse_children
        𝕊.tree_manips[type].setdefault(order, {})
        for name in names:
            𝕊.tree_manips[type][order][name] = f
    def get_manip(𝕊, type, order, t):
        return 𝕊.tree_manips[type].get(order, {}).get(t)

    def general_tree_manip(𝕊, n): # metasyntactical manipulations
        if not n.S:
            n.c = ᴍ(𝕊.general_tree_manip, n.c)
        match n.t:
            case "supscript": n.c = SCRIPT.sup2nrm(n.c)
            case "subscript": n.c = SCRIPT.sub2nrm(n.c)
        return n
    
    def get_orders(𝕊):
        return sorted(set.union(*(set(x.keys()) for x in 𝕊.tree_manips.values())))
    
    def tree_transform(𝕊, n):
        n = 𝕊.general_tree_manip(n)
        print(f"{Z.red}{'-'*100}{Z.wh}")
        n.print()
        print()
        for order in 𝕊.get_orders():
            print(f"{Z.bpu}+{Z.bbla} {Z.pu}{'-'*10}{Z.wh} {order}")
            n = 𝕊.lang_tree_manip(n, order)
            n.print()
            # breakpoint()
            print(f"{Z.bpu}-{Z.bbla} {Z.pu}{'-'*10}{Z.wh} {order}\n")
        print(f"{Z.red}{'-'*100}{Z.wh}")
        return n
    
    def add_generator(𝕊, f, *names):
        for name in names:
            𝕊.generators[name] = f
    def gen(𝕊, n):
        if n.t in 𝕊.generators:
            return 𝕊.generators[n.t](n)
        else:
            return n.c if n.S else ᒍ(ᐦ, ᴍ(𝕊.gen, n.c))
    
    def format_grammar_toks(𝕊, toks):
        return rgx_or(sorted(toks, key=ⵌ, reverse=ⴳ))
    def register_tokset(𝕊, name, toks):
        𝕊.code_namespace[name] = toks
        𝕊.grammar_imports[name.lower()] = 𝕊.format_grammar_toks(toks)
    
    rgx4grammar = SMD(lambda x: f'~"{ᖇ(ᖇ(x, '"', '\\"'), '\\', '\\'*2)}"')
    def parse_gram(𝕊, gram):
        gram = f"{GRAM_HEADER}{
            ᒍ(ń, (f"{i}={𝕊.rgx4grammar(v)}" for \
                  i,v in 𝕊.grammar_imports.items()))
            }\n{gram}"
        return Grammar(gram)
    
    def get_namespace_head(𝕊):
        return {
            "register": 𝕊.register_tokset,
              "op_man": 𝕊.lang.op_man,
               "CONST": {},
                "lang": 𝕊.lang }
    def get_namespace_gen(𝕊):
        return {
            "replacement": AbsoluteWrapper(ρ(𝕊.add_manip, "replacement")),
              "reduction": AbsoluteWrapper(ρ(𝕊.add_manip, "reduction")),
              "generator": AbsoluteWrapper(𝕊.add_generator),
             "parse_expr": 𝕊.lang.op_man.parse_expr,
              "into_expr": into_expr,
               "parse_as": 𝕊.lang.parse_as,
                    "gen": 𝕊.gen } | 𝕊.get_namespace_head()
    
    def __init__(𝕊, lang, code_head, code_gen):
        𝕊.lang, 𝕊.generators, 𝕊.grammar_imports = lang, {}, {}
        𝕊.tree_manips = {"replacement": {}, "reduction": {}}
        𝕊.code_namespace = 𝕊.get_namespace_head()
        𝕊.register_tokset("OPER_LIT", 𝕊.lang.ops.keys())
        exec(CODE_HEADER+code_head, 𝕊.code_namespace)
        𝕊.code_namespace |= 𝕊.get_namespace_gen()
        exec(code_gen, 𝕊.code_namespace)