from util import *

class AbsoluteWrapper:
    def __init__(𝕊, *a, **k):
        (𝕊.f, *𝕊.a), 𝕊.k = a, k
    def __call__(𝕊, *a, **k):
        if len(a) == 1 and callable(a[0]):
            return 𝕊.f(a[0], *𝕊.a, **𝕊.k)
        return type(𝕊)(𝕊.f, *a, **k)

class DynamicParser:
    def add_reduction(𝕊, f, name, recurse_children=ⴴ):
        f.recurse_children = recurse_children
        𝕊.reductions[name] = f
    
    def add_replacement(𝕊, f, name, recurse_children=ⴴ):
        f.recurse_children = recurse_children
        𝕊.replacements[name] = f
    
    def add_generator(𝕊, f, name):
        𝕊.generators[name] = f
    
    def get_replacement(𝕊, t):
        return 𝕊.replacements.get(t)
    def get_reduction(𝕊, t):
        return 𝕊.reductions.get(t)
    
    def gen(𝕊, n):
        if n.t in 𝕊.generators:
            return 𝕊.generators[n.t](n)
        else:
            if n.S:
                return n.c
            else:
                return ᒍ(ᐦ, ᴍ(𝕊.gen, n.c))
    
    def __init__(𝕊, lang, code):
        𝕊.lang = lang
        𝕊.reductions, 𝕊.replacements, 𝕊.generators = {}, {}, {}
        namespace = {
            "replacement": AbsoluteWrapper(𝕊.add_replacement),
              "reduction": AbsoluteWrapper(𝕊.add_reduction  ),
              "generator": AbsoluteWrapper(𝕊.add_generator  ),
               "parse_as": lang.parse_as,
                    "gen": 𝕊.gen }
        exec(code, namespace)