from util import *
from node import *

def p_indent_stack(S, n=0):
    r = []
    while S:
        indent, *exprs = S[0]
        if indent > n:
            r.append(p_indent_stack(S, indent))
        elif indent < n:
            break
        else:
            S.pop(0)
            r.extend(exprs)
    return Node("BLOCK", r)

def whitespace_parser(n):
    calc_indent = lambda n: n.t == 'W' and n.c.split('\n')[-1].count(' ') // 4 or 0
    if n.S: return n
    N = n.copy()
    N.c = ᴍ(whitespace_parser, N.c)
    
    if N.t == "exprs":
        if not N.C: return N
        
        c_pre = N.C[0]
        blocks = [[indent_pre := calc_indent(c_pre)]]
        for c in N.C:
            if c.t == 'W':
                c_pre = c
                continue
            indent = calc_indent(c_pre)
            if indent == indent_pre:
                blocks[-1].append(c)
            else:
                blocks.append([indent, c])
            indent_pre = indent
        N.c = p_indent_stack(blocks, blocks[0][0]).c
    
    elif N.t == "group" and N.C[0].c == '〚':
        raise NotImplementedError
    
    return N

def whitespace_unparser(n, i=0):
    if n.S: return n
    N = n.copy()
    
    if N.t == "BLOCK":
        i += 1
    if N.t in ("BLOCK", "exprs"):
        sep = Node("N", ń+ś*4*i)
        N.c = sum(([sep, n] if n.t != "BLOCK" else [n] for n in N.c), [])
        if N.c and N.t == "exprs":
            N.c.pop(0)
    
    N.c = [whitespace_unparser(c, i) for c in N.c]
    return N

def add_spaces(n):
    def incompat_char(x, y):
        good_chars = "~*/@%&^|-+=:;,.#<>()[]{}' \"\n\t\\"
        return not (x in good_chars or y in good_chars)
    if not n.C: return n
    cc, s = [], peekable([add_spaces(c) for c in n.C])
    while ((α := next(s)) or 1) and s:
        β = s.peek()
        cc.append(α)
        if (a:=α.txt) and (b:=β.txt) and incompat_char(a[-1], b[0]):
            cc.append(Node('w', ś))
    cc.append(α)
    return n.copy(c=cc)