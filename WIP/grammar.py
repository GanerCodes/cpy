from util import *
from dynamic_parser import DynamicParser, make_thingy
from node import Node
from op import OP, OP_MANAGER

content_filter = lambda n: n.t or n.c
content_reducer = lambda n: not n.t
def P2N(p, F=content_filter, R=content_reducer):
    args = F, R
    if p.expr_name.startswith('__'):
        return Node('__')
    if p.expr_name.endswith('_'):
        return Node(p.expr_name, 
            p.children and
                ᒍ(ᐦ, (P2N(x, *args).txt for x in p.children)) 
            or 
                p.text)
    
    C = []
    for n in p.children:
        n = P2N(n, *args)
        if n.t.startswith('__') or F and not F(n):
            continue
        if not n.S and (n.t.startswith('_') or R and R(n)):
            C.extend(n.c)
            continue
        C.append(n)
    return Node(p.expr_name, C if p.children else p.text)

class Lang:
    def __init__(𝕊, lang_file):
        lang_t = R(lang_file)
        𝕊.ops, gram, code_head, code_gen = 𝕊.parse_lang(lang_t)
        𝕊.op_man = OP_MANAGER(𝕊.ops)
        𝕊.dynamic_parsers = DynamicParser(𝕊, code_head, code_gen)
        𝕊.gram = 𝕊.dynamic_parsers.parse_gram(gram)
    
    def __call__(𝕊, content_file):
        content = R(content_file)
        if "parser_comment" in 𝕊.gram:
            content = 𝕊.clean_comments(content)
        content = 𝕊.parse_content(content)
        return content
    
    @staticmethod
    def modchk(tier, mod, R):
        if 'I' in mod:
            mod.discard('I')
            R = R | tier
        else:
            R = R.copy()
        return R
    
    def gen_norm_ops(𝕊, op_norm):
        # all_ops = { i[0] for o in op_norm for i in o }
        ops = {}
        for tier in op_norm[::-1]:
            consume = set(ops.keys())
            for op_t, mod in tier:
                food = 𝕊.modchk({x[0] for x in tier}, mod, consume)
                
                kw = {}
                if mod & set('BS'): kw['L'] = food.copy()
                if mod & set('BP'): kw['R'] = food.copy()
                op = OP(op_t, mod, **kw)
                op.f = partial(make_thingy, op)
                ops[op_t] = op
        return ops
    
    def gen_spec_ops(𝕊, op_spec, ops): # beaned atm
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
            op.f = partial(make_thingy, op)
            
            gen_ops[op_t] = op
        return gen_ops
    
    def parse_secs(𝕊, secs):
        secs = ᒍ(ń, ᴍ(ⵐ, ⵉ(ᖇ(ᖇ(secs, "␛\n", ś), '␉', ń), ń)))
        op_norm, op_spec, *_ = (ⵉ(x, ń) for x in re.split(r'\n{2,}', secs))
        op_norm = ᴍ(ⵉ, op_norm)
        def parse_oper_dec(x, *, rgx=re.compile(ᖇ("([^𝕩]+)([𝕩]*)", '𝕩', SCRIPT.CHAR_SUP))):
            x, y = rgx.match(x).groups()
            return x, set(SCRIPT.sup2nrm(y))
        
        op_norm = ᴍᴍ(2, parse_oper_dec, op_norm)
        
        tmp = lambda x,y,z: [x, parse_oper_dec(y), z]
        op_spec = [tmp(*ᴍ(ⵐ, ⵉ(i, '｜'))) for i in op_spec]
        
        return op_norm, op_spec
    
    def parse_lang(𝕊, raw):
        sections = spl_H(raw, r"«{3,}([^»]*)»{3,}")
        
        op_norm, op_spec = 𝕊.parse_secs(sections['OPERATORS'])
        ops = 𝕊.gen_norm_ops(op_norm)
        ops |= 𝕊.gen_spec_ops(op_spec, ops)
        
        return ops, sections["GRAMMAR"], sections["HEADERS"], sections["GENERATORS"]
    
    def parse_as(𝕊, p, content, **kw):
        gram = 𝕊.gram[p]
        p = P2N(gram.parse(content), **kw)
        return p
    
    def clean_comments(𝕊, content):
        return 𝕊.parse_as("parser_comment", content, F=lambda n: n.t != "comment").txt
    
    def parse_content(𝕊, content):
        n = 𝕊.parse_as("parser_main", content)
        # n.print()
        n = 𝕊.dynamic_parsers.tree_transform(n)
        # n.print()
        return 𝕊.dynamic_parsers.gen(n)
    
l = Lang("cpy.lang")
print('-'*50)
print(l("test.txt"))

# N: Nullary
# S: Suffix
# P: Prefix
# B: Binary
# I: Include self in right subgrouping (Right assoc.)