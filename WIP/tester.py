from parsimonious.grammar import Grammar
from collections import namedtuple as NT
from functools import reduce
import keyword as py_kw
import regex as re

T, F = True, False
R = lambda x: open(x).read()
HX = lambda c: hex(ord(c))[2:]
flat = lambda x: reduce(lambda x,y: x+y, l:=list(x), type(l[0])() if len(l) else [])
rgx_or  = lambda x: '(' + ')|('.join(x) + ')'
i_rgx_fmt = lambda x: x.replace('"', '\\"').replace('\\', '\\\\')

py_bad_string_chr = lambda s, bad="\\\"'{}": s in bad
py_escape_char    = lambda c, pre='': pre+HX(c) if py_bad_string_chr(c) else c

py_escape_string  = lambda s: ''.join(py_escape_char(c, '\\u') for c in s)
py_escape_var     = lambda s: ''.join('_'+py_escape_char(c) for c in s)

py_special_mapper = lambda c, m=dict(zip("𝗻𝘀𝘁","nst")): '\\'+m[c]

def partition(l, f):
    r, b = [], []
    for c in l:
        if f(c):
            r, b = r+[b, c], []
        else:
            b += [c]
    return r + ([b] if b else [])

class Node:
    def name_filter(n):
        return n and not n.startswith('_') \
               and n not in ("expr", )
    from_grammar = lambda n: Node(n.text,
            n.expr_name if Node.name_filter(n.expr_name) else "",
            [C for c in n.children if (C:=Node.from_grammar(c)).text])
    def __init__(𝕊, text, expr_name, children):
        𝕊.text = text
        𝕊.expr_name = expr_name
        𝕊.children = children
    def __repr__(𝕊):
        return f'{𝕊.expr_name}: "{𝕊.text}"'
    def reduce(𝕊):
        if 𝕊.expr_name and 𝕊.expr_name == "var":
            return Node(𝕊.text, 𝕊.expr_name, [])
        return Node(𝕊.text, 𝕊.expr_name, flat(
                    [C] if (C:=c.reduce()).expr_name else
                    (C.children or [Node(C.text, "s", [])]) 
                for c in 𝕊.children))
    def collapse(𝕊):
        n = Node(𝕊.text, 𝕊.expr_name, [C for c in 𝕊.children if (C:=c.collapse()).text.strip()])
        if len(n.children) == 1:
            c = n.children[0]
            return Node(𝕊.text, 𝕊.expr_name+':'+c.expr_name, c.children)
        return n
    def print(𝕊, s='', clean=lambda x: x.replace('\n','ñ')):
        print(f"{s}{𝕊.expr_name} ► {clean(𝕊.text)}")
        if 𝕊.children and all(c.expr_name == 's' for c in 𝕊.children):
            return print(s+'  '+"S-CHAIN: "+'­—'.join(clean(c.text) for c in 𝕊.children))
        [c.print(s+'  ') for c in 𝕊.children]
    
    def reparse(𝕊):
        match 𝕊.expr_name:
            case "exprs":
                return parse_exprs(𝕊.children)
            case "str_guts":
                return py_escape_string(𝕊.text)
            case "str_escape":
                return "'" + py_escape_string(𝕊.text[1:]) + "'"
            case "str_sub":
                return "{" + 𝕊.children[1].reparse() + "}"
            case "special_char":
                return "'" + py_special_mapper(𝕊.text) + "'"
            case "special_str":
                r = '"'
                for c in 𝕊.children[1:-1]:
                    match c.expr_name:
                        case "str_escape":
                            r += py_escape_string(c.text[1:])
                        case "special_char":
                            r += py_special_mapper(c.text)
                        case _:
                            r += c.reparse()
                return r + '"'
            case _: # ex. py_str, s, etc.
                if not 𝕊.children:
                    return 𝕊.text
                else:
                    return ''.join(c.reparse() for c in 𝕊.children)

op = NT("op", [*"tBNPS"], defaults=['']+[F]*4)
def parse_operators_file(f, *, r=re.compile(r"(?P<op>[^\sα]+)(?P<mod>[α]*)".replace('α', "ᴮᴺᐟ˜󰂢󰂥⸝"))):
    make_op = lambda x: op(x[0], *([1*bool(set(x[1]) & set(y)) for y in "ᴮ˜ ᴺ˜ 󰂢 󰂥".split(' ')] if x[1] else (1,0,0,0)))
    txt = open(f).read().split('\n')
    return [[make_op(a) for a in r.findall(x)] for i in txt if (x:=i.split('')[0].strip())]

def parse_gram(gram_f, op_f):
    ops = parse_operators_file(op_f)
    op_names = sorted(flat([o.t for o in i] for i in ops), key=len, reverse=T)
    
    rgx_keywords = rgx_or(py_kw.kwlist + py_kw.softkwlist)
    rgx_operator = rgx_or(flat([re.escape(c+'='), re.escape(c)] for c in op_names))
    rgx_specials = rgx_or("ℵ𝕋𝔽îπτ□∅∞ᐦ")
    
    gram = R(gram_f)
    gram = gram.replace(  "%OPERATORS%", i_rgx_fmt(rgx_operator)) \
               .replace("%VAR_SPECIAL%", i_rgx_fmt(rgx_specials)) \
               .replace("%PY_KEYWORDS%", i_rgx_fmt(f"({rgx_keywords})(\\Z|[^_a-zA-Z0-9])"))
    
    return Grammar(gram), ops

def clean_comments(content):
    parsed = Node.from_grammar(gram['parser_comment'].parse(content)).reduce()
    return flat(c.text for c in parsed.children if c.expr_name != 'comment')

def parse_file(gram, f):
    content = gram.parse(clean_comments(R(f)))
    return Node.from_grammar(content)

gram, ops = parse_gram("cpy.gram", "operators")
tree = parse_file(gram, "test.txt").reduce()
tree.collapse().print()

V=0
def A():
    global V
    V += 1
def B():
    global V
    V -= 1
pr=lambda*a,**k:print(V*'#',*a,**k)

def parse_exprs(n, layers=ops):
    A()
    pr("1", n)
    layer, *nlayers = layers
    L = {o.t:o for o in layer}
    
    stack = partition(n.copy(), lambda x: isinstance(x, Node) and x.expr_name=="oper" and x.text in L)
    if nlayers:
        stack = [parse_exprs(c, nlayers) if isinstance(c, list) else c for c in stack]
    pr("2", stack)
    
    res = []
    while stack:
        pr("STACK", stack)
        c = stack[0]
        if not isinstance(c, Node):
            item_l = stack.pop(0)
            if not stack:
                res += [item_l]
                break
            
            op = L[stack.pop(0).text]
            if op.S:
                stack = [f"⟨{item_l}│{op.t}⟩"] + stack
                continue
            if op.B:
                item_r = stack.pop(0)
                stack = [f"⟨{item_l}│{op.t}│{item_r}⟩"] + stack
                continue
            if op.N:
                item_r = parse_exprs(stack, layers)
                stack = [f"⟨{item_l}│{op.t}│{item_r}⟩"]
                continue
            assert F
        
        op = L[stack.pop(0).text]
        assert op.P
        item_r = stack.pop(0)
        stack = [f"⟨{op.t}│{item_r}⟩"] + stack
    
    if len(res) == 1:
        res = res[0]
    
    pr("RES", '→', res)
    B()
    return res
    # pr("TODO")
    # return ''.join(x.text for x in n)

print('-'*50)
print(tree.reparse())