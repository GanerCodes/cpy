from util import *
from node import *

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
    return Node('expr', c=C if ᐹ(C, ᔐ) else [C])

def make_thingy(op, l, r, op_):
    ch = lambda n: NULL if n is ᗜ else into_expr(n) if ᐹ(n, ᒪ) else n
    l, r = ch(l), ch(r)
    return Node("op_call", [op_, l, r])

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
            N.c = ᴍ(partial(𝕊.lang_tree_manip, order=order), N.c)
        N = m(N)
        if m.recurse_children == 'A' and not N.S:
            N.c = ᴍ(partial(𝕊.lang_tree_manip, order=order), N.c)
        return N
    
    def lang_tree_manip(𝕊, N, order):
        if m := 𝕊.get_manip("replacement", order, N.t):
            return 𝕊._apply_tree_manip(m, N, order)
        if N.S:
            return N
        
        cc = []
        for n in N.C:
            if m := 𝕊.get_manip("reduction", order, n.t):
                assert m.recurse_children != 'A'
                cc.extend(𝕊._apply_tree_manip(m, n, order))
            else:
                cc.append(𝕊.lang_tree_manip(n, order))
        return Node(N.t, cc)
    
    def add_manip(𝕊, type, f, name, recurse_children=ⴴ, order=1):
        f.recurse_children = recurse_children
        if not 𝕊.tree_manips[type].get(order):
            𝕊.tree_manips[type][order] = {}
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
        for order in 𝕊.get_orders():
            n = 𝕊.lang_tree_manip(n, order)
        return n
    
    def add_generator(𝕊, f, name):
        𝕊.generators[name] = f
    def gen(𝕊, n):
        if n.t in 𝕊.generators:
            return 𝕊.generators[n.t](n)
        else:
            if n.S:
                return n.c
            else:
                return ᒍ(ᐦ, ᴍ(𝕊.gen, n.c))
    
    def __init__(𝕊, lang, code):
        𝕊.lang, 𝕊.generators = lang, {}
        𝕊.tree_manips = {"replacement": {}, "reduction": {}}
        namespace = {
            "replacement": AbsoluteWrapper(partial(𝕊.add_manip, "replacement")),
              "reduction": AbsoluteWrapper(partial(𝕊.add_manip, "reduction")),
              "generator": AbsoluteWrapper(𝕊.add_generator),
             "parse_expr": 𝕊.lang.op_man.parse_expr,
              "into_expr": into_expr,
               "parse_as": 𝕊.lang.parse_as,
                 "op_man": 𝕊.lang.op_man,
                    "gen": 𝕊.gen }
        exec(code, namespace)