from util import *
from dynamic_parser import Gram, DynamicParser, make_op_call, CODE_HEADER
from node import Node
from op import OP, OP_Manager
from time import time

class Lang:
    """ ℭ = {}
    def __new__(ℂ, lang_t, ver=ᐦ, cache_dir=ᗜ):
        h = (sha256(lang_t), ver, cache_dir)
        if h in Lang.ℭ:
            return Lang.ℭ[h]
        return super(Lang, ℂ).__new__(ℂ) """
    
    def __init__(𝕊, lang_t, ver=ᐦ, cache_dir=ᗜ):
        𝕊.ver, 𝕊.ops, 𝕊.op_orders, gram, code_head, code_gen = ver, *𝕊.parse_lang(lang_t)
        𝕊.op_man = OP_Manager(𝕊.ops)
        𝕊.dynamic_parsers = DynamicParser(𝕊, code_head, code_gen)
        𝕊.id = sha256(lang_t + ver)
        ℭ = FileCacher(cache_dir, lambda x, *_: 𝕊.dynamic_parsers.parse_gram(x),
                       Gram.load_gram, Gram.dump_gram)
        𝕊.gram = ℭ(gram, 𝕊.id)
    
    def __call__(𝕊, content, **K):
        if "parser_comment" in 𝕊.gram:
            content = 𝕊.gram(content, "parser_comment", remove_trashes=ⴴ) \
                       .child_killer(lambda n: n.t == "comment").txt
        return 𝕊.parse_content(content, **K)
    
    def __str__(𝕊):
        return f"{Т(𝕊).__name__}[gram={𝕊.gram}][dynamic_parsers={𝕊.dynamic_parsers}][op_man={𝕊.op_man}]"
    
    @staticmethod
    def modchk(tier, mod, R):
        if 'I' in mod:
            mod.discard('I')
            return R | tier
        return R.copy()
    
    def gen_norm_ops(𝕊, op_norm):
        ops = {}
        for tier in op_norm[::-1]:
            food = set(ops.keys())
            for op_t, mod in tier:
                meal = 𝕊.modchk({x[0] for x in tier}, mod, food)
                
                kw = {}
                if mod & set('BS'): kw['L'] = meal.copy()
                if mod & set('BP'): kw['R'] = meal.copy()
                
                op = OP(op_t, mod, **kw)
                op.f = ρ(make_op_call, op)
                ops[op_t] = op
        return ops
    
    def gen_spec_ops(𝕊, op_spec, ops):
        gen_ops = {}
        for L, (op_t, mod), R in op_spec:
            L_c = L and ops[L].L|ops[L].R or {}
            R_c = R and ops[R].L|ops[R].R or {}
            for c in ops:
                if c not in L_c and (O := ops[c]).PB:
                    O.R.add(op_t)
                if c not in R_c and (O := ops[c]).SB:
                    O.L.add(op_t)
            
            kw = {}
            if L: kw['L'] = (ops.keys()-ops[L].L)|{L}
            if R: kw['R'] = 𝕊.modchk(
                {x[1][0] for x in op_spec},
                mod, ops[R].R)
            
            op = OP(op_t, mod, **kw)
            op.f = ρ(make_op_call, op)
            
            gen_ops[op_t] = op
        return gen_ops
    
    def parse_secs(𝕊, secs):
        secs = ᒍ(ń, ᴍ(ⵐ, ⵉ(ᖇ(ᖇ(secs, "␛\n", ś), '␉', ń), ń)))
        op_norm, op_spec, *_ = (ⵉ(x, ń) for x in re.split(r'\n{2,}', secs))
        op_norm = ᴍ(ⵉ, op_norm)
        def parse_oper_dec(x, *, rgx=re.compile(ᖇ("([^𝕩]+)([𝕩]*)", '𝕩', SCRIPT.CHAR_SUP))):
            x, y = rgx.match(x).groups()
            return x, set(SCRIPT.nrm(y))
        
        op_norm = ᴍᴍ(2, parse_oper_dec, op_norm)
        
        tmp = lambda x,y,z: [x, parse_oper_dec(y), z]
        op_spec = [tmp(*ᴍ(ⵐ, ⵉ(i, '｜'))) for i in op_spec]
        
        return op_norm, op_spec
    
    def parse_lang(𝕊, raw):
        sections = spl_H(raw, r"«{3,}([^»]*)»{3,}")
        
        op_norm, op_spec = 𝕊.parse_secs(sections['OPERATORS'])
        op_orders = {i: {h[0] for h in l} for i, l in enum(op_norm)}
        ops = 𝕊.gen_norm_ops(op_norm)
        ops |= 𝕊.gen_spec_ops(op_spec, ops)
        
        return ops, op_orders, sections["GRAMMAR"], sections["HEADERS"], sections["GENERATORS"]
    
    def parse_content(𝕊, content, **K):
        return 𝕊.dynamic_parsers.gen(
                  𝕊.dynamic_parsers.tree_transform(
                      𝕊.gram(content, "parser_main")))