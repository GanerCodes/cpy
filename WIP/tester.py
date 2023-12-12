from parsimonious.grammar import Grammar
from functools import reduce
from keyword import kwlist, softkwlist
from regex import escape as re_escape

R = lambda x: open(x).read()
HX = lambda c: hex(ord(c))[2:]

flat = lambda x: reduce(lambda x,y: x+y, l:=list(x), type(l[0])() if len(l) else [])

py_bad_string_chr = lambda s, bad="\\\"'{}": s in bad
py_escape_char    = lambda c, pre='': pre+HX(c) if py_bad_string_chr(c) else c

py_escape_string  = lambda s: ''.join(py_escape_char(c, '\\u') for c in s)
py_escape_var     = lambda s: ''.join('_'+py_escape_char(c) for c in s)

py_special_mapper = lambda c, m=dict(zip("𝗻𝘀𝘁","nst")): '\\'+m[c]

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
    
    def split_children(𝕊, f):
        r, b = [], []
        for c in 𝕊.children:
            if f(c):
                r, b = r+[b, c], []
            else:
                b += [c]
        return r + [b]
    def split_and_group(𝕊, f):
        k = split_children(𝕊, f)
        # for 
    
    def reparse(𝕊):
        match 𝕊.expr_name:
            case "exprs":
                print(𝕊.split_children(
                    lambda c: c.expr_name == "oper" and c.text in ops[-1]))
                return 𝕊.text
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

parse_operations = lambda t: [x.strip().split(' ') for x in t.replace('\n', '∣').split('∣')]
parse_op_mapping = lambda t: [[y.replace('𝐬', ' ') for y in x.strip().split(' ')] for x in t.replace('\n', '∣').split('∣')]
parse_op_customs = lambda t: [x.split(' ') for x in t.split('\n')]

rgx_fmt = lambda x: x.replace('"', '\\"').replace('\\', '\\\\')
rgx_or  = lambda x: '(' + ')|('.join(x) + ')'

ops, opm, opc = R("ops").split('\n\n')
ops, opm, opc = parse_operations(ops), parse_op_mapping(opm), parse_op_customs(opc)

py_keywords = kwlist + softkwlist

rgx_keywords = rgx_or(py_keywords)
rgx_operator = rgx_or(flat([[re_escape(c+'='), re_escape(c)] for c in flat(ops)]))
rgx_specials = rgx_or([re_escape(c) for c in flat(flat(opc))])

gram = R("test.gram")
gram = gram.replace(  "%OPERATORS%", rgx_fmt(rgx_operator))
gram = gram.replace("%VAR_SPECIAL%", rgx_fmt(rgx_specials))
gram = gram.replace("%PY_KEYWORDS%", rgx_fmt(f"({rgx_keywords})(\\Z|[^_a-zA-Z0-9])"))
gram = Grammar(gram)

def clean_comments(content):
    parsed = Node.from_grammar(gram['parser_comment'].parse(content)).reduce()
    return flat(c.text for c in parsed.children if c.expr_name != 'comment')
    
content = R("test.txt")
content = clean_comments(content)

tree = Node.from_grammar(gram.parse(content))
tree = tree.reduce()
tree.collapse().print()
print('-'*50)
print(tree.reparse())