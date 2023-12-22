from util import *
from op import OP, OP_MANAGER

class Grammar_parser:
    rgx4grammar = SMD(lambda x: ᖇ(ᖇ(x, '"', '\\"'), '\\', '\\\\'))
    
    def gen_norm_ops(𝕊, op_norm):
        ops = {}
        for tier in op_norm:
            consume = set(ops.keys())
            for op_t, mod in tier:
                food = consume
                if 'I' in mod:
                    mod.discard('I')
                    food = food | { op_t }
                
                kw = {}
                if 'B' in mod:
                    kw['L'] = kw['R'] = food
                else:
                    if 'S' in mod: kw['L'] = food
                    if 'P' in mod: kw['R'] = food
                f = lambda l=ᗜ, r=ᗜ: f"({op})[{l=} {r=}]"
                op = OP(op_t, mod, f=f, **kw)
                ops[op_t] = op
        return ops
    
    def gen_spec_ops(𝕊, op_spec, ops):
        print(op_spec)
        return {}
    
    def parse_secs(𝕊, secs):
        secs = ᒍ(ń, ᴍ(ⵐ, ⵉ(ᖇ(ᖇ(secs, "␛\n", ś), '␉', ń), ń)))
        op_norm, op_spec, var_spec, keywords, *_ = (ⵉ(x, ń) for x in re.split(r'\n{2,}', secs))
        op_norm, var_spec = ᴍ(ⵉ, op_norm), set(ᴍ(ⵐ, var_spec))
        
        def parse_oper_dec(x, *, rgx=re.compile(ᖇ("([^𝕩]+)([𝕩]*)", '𝕩', SCRIPT.CHAR_SUP))):
            x, y = rgx.match(x).groups()
            return x, set(SCRIPT.sup2nrm(y))
        
        op_norm = ᴍᴍ(2, parse_oper_dec, op_norm)
        
        tmp = lambda x,y,z: [x, parse_oper_dec(y), z]
        op_spec = [tmp(*ᴍ(ⵐ, ⵉ(i, '｜'))) for i in op_spec]
        
        return op_norm, op_spec, var_spec, keywords
    
    def parse_parser(𝕊, raw):
        tmp, gram = raw.split("«GRAMMAR»", 1)
        secs, gen = tmp.split("«GENERATORS»", 1)
        
        op_norm, op_spec, var_spec, keywords = 𝕊.parse_secs(secs)
        ops = 𝕊.gen_norm_ops(op_norm)
        ops |= 𝕊.gen_spec_ops(op_spec, ops)
        
        rgxs = { "VAR_SPECIAL": rgx_or(var_spec),
                 "OPERATORS": rgx_or(ops.keys()),
                 "KEYWORDS": rgx_or(keywords) }
        return ops, rgxs, code
    
    def __init__(𝕊, lang_file):
        lang_t = R(lang_file)
        ops, rgxs, code = 𝕊.parse_language(lang_t)
        
        # rgx4grammar

Grammar_parser("cpy.parser", "cpy.gram")

# N: Nullary
# S: Suffix
# P: Prefix
# B: Binary
# I: Include self in right subgrouping (Right assoc.)