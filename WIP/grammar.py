from util import *
from dynamic_parser import DynamicParser
from node import Node
from op import OP, OP_MANAGER
from parsimonious.grammar import Grammar

DYNAMIC_PARSER_HEADER = """\
from util import *
from node import *"""

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
    rgx4grammar = SMD(lambda x: ᖇ(ᖇ(x, '"', '\\"'), '\\', '\\\\'))
    
    @staticmethod
    def modchk(tier, mod, R):
        if 'I' in mod:
            mod.discard('I')
            R = R | tier
        return R
    
    def gen_norm_ops(𝕊, op_norm):
        ops = {}
        for tier in op_norm:
            consume = set(ops.keys())
            for op_t, mod in tier:
                food = 𝕊.modchk({x[0] for x in tier}, mod, consume)
                
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
        gen_ops = {}
        for L, (op_t, mod), R in op_spec:
            for c in ops:
                if not L or c in ops[L].L|ops[L].R:
                    if (O := ops[c]).PB:
                        O.R.add(op_t)
                if not R or c in ops[R].L|ops[R].R:
                    if (O := ops[c]).SB:
                        O.L.add(op_t)
            
            kw = {}
            if L: kw['L'] = (ops.keys()-ops[L].L)|{L}
            if R: kw['R'] = 𝕊.modchk(
                {x[1][0] for x in op_spec},
                mod, (ops.keys()-ops[R].R)|{R})
            
            f = lambda l=ᗜ, r=ᗜ: f"({op})[{l=} {r=}]"
            op = OP(op_t, mod, f=f, **kw)
            
            gen_ops[op_t] = op
        return gen_ops
    
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
    
    def parse_gram(𝕊, gram, rgxs):
        for f, r in rgxs.items():
            gram = ᖇ(gram, f"%{f}%", 𝕊.rgx4grammar(r))
        return Grammar(gram)
    
    def parse_lang(𝕊, raw):
        temp, gram = raw.split("«GRAMMAR»", 1)
        secs, code = temp.split("«GENERATORS»", 1)
        
        op_norm, op_spec, var_spec, keywords = 𝕊.parse_secs(secs)
        ops = 𝕊.gen_norm_ops(op_norm)
        ops |= 𝕊.gen_spec_ops(op_spec, ops)
        
        gen_rgx = lambda x: rgx_or(sorted(x, key=ⵌ, reverse=ⴳ))
        rgxs = { "VAR_SPECIAL": gen_rgx(var_spec),
                   "OPERATORS": gen_rgx(ops.keys()),
                    "KEYWORDS": gen_rgx(keywords) }
        gram = 𝕊.parse_gram(gram, rgxs)
        
        dynamic_parsers = DynamicParser(𝕊, DYNAMIC_PARSER_HEADER + '\n' + code)
        
        return ops, gram, dynamic_parsers
    
    def __init__(𝕊, lang_file):
        lang_t = R(lang_file)
        𝕊.ops, 𝕊.gram, 𝕊.dynamic_parsers = 𝕊.parse_lang(lang_t)
    
    def general_one_time_manip(𝕊, n):
        # responsible for metasyntactical manipulations,
        # ex. making subscripts/superscripts easier to work with
        if not n.S:
            n.c = ᴍ(𝕊.general_one_time_manip, n.c)
        match n.t:
            case "supscript": n.c = SCRIPT.sup2nrm(n.c)
            case "subscript": n.c = SCRIPT.sub2nrm(n.c)
        return n
    
    def _apply_tree_manip(𝕊, m, n):
        N = n.copy()
        if m.recurse_children == 'B' and not N.S:
            N.c = ᴍ(𝕊.lang_tree_manip, N.c)
        N = m(n)
        if m.recurse_children == 'A' and not N.S:
            N.c = ᴍ(𝕊.lang_tree_manip, N.c)
        return N
    
    def lang_tree_manip(𝕊, N):
        if m := 𝕊.dynamic_parsers.get_replacement(N.t):
            return 𝕊._apply_tree_manip(m, N)
        if N.S:
            return N
        
        cc = []
        for n in N.C:
            if m := 𝕊.dynamic_parsers.get_reduction(N.t):
                assert m.recurse_children != 'A'
                cc.extend(𝕊._apply_tree_manip(m, n))
            else:
                cc.append(𝕊.lang_tree_manip(n))
        return Node(N.t, cc)
        
    def gen_as(𝕊, n, t=ᗜ):
        if t is ᗜ:
            t = n.t
        
        # print(f"Generating {n} as '{t}'")
        return "asd"
    
    def parse_as(𝕊, p, content, **kw):
        gram = 𝕊.gram[p]
        p = P2N(gram.parse(content), **kw)
        return p
    
    def clean_comments(𝕊, content):
        return 𝕊.parse_as("parser_comment", content, F=lambda n: n.t != "comment").txt
    
    def parse_content(𝕊, content):
        n = 𝕊.parse_as("parser_main", content)
        n.print()
        n = 𝕊.general_one_time_manip(n)
        n = 𝕊.lang_tree_manip(n)
        n.print()
        return 𝕊.gen_as(n)
    
    def __call__(𝕊, content_file):
        content = R(content_file)
        if "parser_comment" in 𝕊.gram:
            content = 𝕊.clean_comments(content)
        content = 𝕊.parse_content(content)
        return content

l = Lang("cpy.lang")
l("test.txt")

# N: Nullary
# S: Suffix
# P: Prefix
# B: Binary
# I: Include self in right subgrouping (Right assoc.)