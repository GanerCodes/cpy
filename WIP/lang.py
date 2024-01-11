from util import *
from dynamic_parser import DynamicParser, make_op_call
from node import Node
from op import OP, OP_Manager

class Lang:
    def __init__(𝕊, lang_file):
        lang_t = R(lang_file)
        𝕊.ops, 𝕊.op_orders, gram, code_head, code_gen = 𝕊.parse_lang(lang_t)
        𝕊.op_man = OP_Manager(𝕊.ops)
        𝕊.dynamic_parsers = DynamicParser(𝕊, code_head, code_gen)
        𝕊.gram = 𝕊.dynamic_parsers.parse_gram(gram)
    
    def __call__(𝕊, content_file, **K):
        content = R(content_file)
        if "parser_comment" in 𝕊.gram:
            content = 𝕊.gram(content, "parser_comment", allow_deletes=ⴴ) \
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
            return x, set(SCRIPT.sup2nrm(y))
        
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
        𝕊.dynamic_parsers.code_namespace["CONST"] = K
        return 𝕊.dynamic_parsers.gen(
                  𝕊.dynamic_parsers.tree_transform(
                      𝕊.gram(content, "parser_main")))

def main():
    import dynamic_parser, time, ast
    
    pr = lambda g: print(ᒍ(ń, (f"{ᔐ(i+1).zfill(4)}\t{wrap(v, q='\t  ')}" for i,v in enum(ⵉ(g, ń)))))
    
    tI = time.time()
    l = Lang("cpy.lang")
    tΔl = time.time() - tI
    prs = ρ(l, "test2.txt")
    
    pretty = prs(NOVAR=1)
    
    dynamic_parser.DEBUG = 0
    
    tI = time.time()
    normal = prs()
    tΔc = time.time() - tI
    
    print("NORMAL:")
    pr(normal)
    print("\nNO-CONVERT-VARS:")
    pr(pretty)
    print("\nAST REPARSE:")
    pr(ast.unparse(ast.parse(normal)))
    print(f"\n{tΔl=}, {tΔc=}, {tΔl+tΔc=}\nEXECUTION:")
    exec(normal)

if __name__ == "__main__":
    main()