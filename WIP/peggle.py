# maybe?
from util import *
from node import *
from grammar import P2N
# from parsimonious.grammar import Grammar

from line_profiler import LineProfiler
from time import time
import cProfile
prof = LineProfiler()

def mk(t, *c):
    flag = ⴴ
    if c and c[-1] is ᗜ:
        flag = ⴳ
        c.pop()
    c = [mk(*x) if ᐹ(x, tuple) else x for x in c]
    if t == '~':
        assert ⵌ(t) == 1
        return Node('~', re.compile(c[0].txt))
    return Node(t, c[0] if flag else ᒪ(c))

def parse_elm(N):
    pre, n, suf = N
    pre = sorted(pre.txt, key="❗⠶󰆴¬⮞~".index)
    for k in chain(
          ᖶ('❗⠶'.__contains__, pre),
          suf.txt,
          ᖵ('❗⠶'.__contains__, pre)):
        n = mk(k, n)
    return n

def reduce_j(N):
    α, o, β, *C = N
    if C: β = reduce_j(N.copy(c=[β, *C]))
    match o.c:
        case '↷': r = mk('∧', α, β, α)
        case '△': r = mk('∨', ('∧', ('*', ('∧', α, β)), α), α)
        case '▽': r = mk('∨', ('∧', ('∧', β, ('*', ('∧', α, β)))), Ń('✓'))
        case '⯅': r = mk('∧', ('+', ('∧', α, β)), α)
        case '⯆': r = mk('∨', ('∧', β, ('+', ('∧', α, β))), β)
        case  _ : assert ⴴ
    return r

def gram_convert(t):
    name_remaps = { "elm_o": '∨', "elm_a": '∧', "assign_cln": "←" }
    _, rules = t \
         .child_killer(lambda n: n.t == "comment") \
         .      filter(lambda n: not (n.t and n.t in "wW")) \
         .      filter(lambda n: not (not n.t and n.c and n.c in "()∧∨:")) \
         .find_replace(lambda n: n.t in ("prefix", "suffix"), lambda n: n.copy(c=n.txt)) \
         .find_replace(lambda n: n.t == "str", lambda n: n.copy(c=n.txt[1:-1])) \
         .find_replace(lambda n: n.t in name_remaps, lambda n: n.copy(name_remaps[n.t])) \
         .flatten_kids(lambda n: n.t == "_elm_j") \
         .find_replace(lambda n: n.t == "assign_eql", lambda n: n.C[0], collect=ⴳ)
    rules = { r.C[0].c:r.C[2] for r in rules }
    for k, v in rules.items():
        rules[k] = v \
            .find_replace(lambda n: n.t == "elm", parse_elm) \
            .flatten_kids(lambda n: ⵌ(n) == 1 and n.t in (*"∨∧", "elm_j", "group_inner")) \
            .find_replace(lambda n: n.t == "elm_j", reduce_j) \
            .flatten_kids(lambda n: ⵌ(n) == 1 and n.t == "group") \
            .find_replace(lambda n: n.t == "group", lambda n: n.copy('∧')) \
            .find_replace(lambda n: n.t == "str", lambda n: n.copy('ᔐ', n.txt))
        
    return rules

class Gram:
    def __init__(𝕊, rules):
        𝕊.rules = rules
    
    def run(𝕊, s, r):
        if r.t == "rname":
            if r.c == '✗': # die
                assert ⴴ
            if j := 𝕊.run(s, 𝕊.rules[r.c]):
                return Node(r.c, [j[0]]), j[1]
            return
        t, c = r.t, r.c
        
        if t in "*+∧":
            R = []
            if t in '*+': # as many as possible
                while v := 𝕊.run(s, c[0]):
                    α, s = v
                    R.append(α)
                if t == '+' and not R: return # empty plus we leave!!!1
            else: # concatination
                for x in c:
                    if not (v := 𝕊.run(s, x)): return
                    α, s = v
                    R.append(α)
            return Node(t, R), s
        match t:
            case '?': # its okay you can eat when you want to
                if v := 𝕊.run(s, c[0]):
                    return Node(t, v[0]), v[1]
                return Node(t), s
            case '∨': # pick first
                for x in c:
                    if (v := 𝕊.run(s, x)): return v
            case '~'|'ᔐ': # regex/str
                L = s[0].t[1] if s else 10**12
                st = 𝕊.ST[L:]
                if t == '~':
                    if not (m := c.match(st)): return
                    R = m.span()[1]
                elif t == 'ᔐ':
                    if not st.startswith(c): return
                    R = ⵌ(c)
                return Node(t, s[:R]), s[R:]
            case '❗': # match or die
                if not (v := 𝕊.run(s, c[0])): assert ⴴ
                return Node(t, v[0]), v[1]
            case '󰆴': # eat & delete
                if not (v := 𝕊.run(s, c[0])): return
                return Node(t, v[0]), v[1]
            case '⮞': # positive lookahead
                if not (v := 𝕊.run(s, c[0])): return
                return Node(t, v[0]), s
            case '¬': # negative lookahead
                if v := 𝕊.run(s, c[0]): return
                return Node(t, v[0]), s
            case '⠶': # flatten
                return Node(t), s
            case '✓': # good
                return Node(t), s
            case _: # unwillingly die
                assert ⴴ, f"Invalid instruction '{t}'!"
    
    def chop(𝕊, n):
        return n \
            .flatten_kids(lambda n: n.t in tuple("∧∨~+*?ᔐ⠶⮞❗")) \
            .child_killer(lambda n: n.t[0] in ('✓','¬','󰆴')) \
            .find_replace(
                lambda n: n.L,
                lambda n: n.copy(c=ᒪ(map_groups(n.C,
                    lambda n: ᐹ(n.t,tuple) and n.t[0]=='□',
                    lambda l: Ń(ᐦ, ᒍ(ᐦ, l)),
                    lambda n: n.txt)))) \
            .find_replace(lambda n: n.L and ⵌ(n) == 1 and n.C[0].t in "~ᔐ",
                          lambda n: n.copy(c=n.txt)) \
    
    def __call__(𝕊, content, rule="main"):
        𝕊.ST = content
        tree = 𝕊.run([Node(('□', i), c) for i, c in enum(content)], 𝕊.rules[rule])
        
        if not tree or tree[1]:
            if tree:
                print("BUILT TREE:")
                tree[0].print()
                print("REMAINDER:", tree[1])
                assert ⴴ, f"Didn't finish :<"
            else:
                assert ⴴ, f"Didn't finish, failed!"
        return 𝕊.chop(tree[0])
rules_bootstrap = {'statements': Node('∨', [Node('∧', [Node('?', [Node('rname', 'W')]), Node('*', [Node('∧', [Node('∨', [Node('rname', 'comment'), Node('rname', 'elm_o')]), Node('?', [Node('rname', 'W')])])])])]), 'comment': Node('∨', [Node('~', regex.Regex('[\ueb26#][^\\n]*', flags=regex.V0))]), 'elm_o': Node('∨', [Node('∧', [Node('rname', 'elm_a'), Node('*', [Node('∧', [Node('?', [Node('rname', 'W')]), Node('ᔐ', '∨'), Node('?', [Node('rname', 'W')]), Node('rname', 'elm_a')])])])]), 'elm_a': Node('∨', [Node('∧', [Node('rname', 'elm_j'), Node('*', [Node('∧', [Node('∨', [Node('∧', [Node('?', [Node('rname', 'W')]), Node('ᔐ', '∧'), Node('?', [Node('rname', 'W')])]), Node('?', [Node('rname', 'w')])]), Node('rname', 'elm_j')])])])]), 'elm_j': Node('∨', [Node('rname', '_elm_j'), Node('rname', 'elm')]), '_elm_j': Node('∨', [Node('∧', [Node('rname', 'elm'), Node('?', [Node('rname', 'W')]), Node('~', regex.Regex('[⯅⯆△▽↷]', flags=regex.V0)), Node('?', [Node('rname', 'W')]), Node('∨', [Node('rname', '_elm_j'), Node('rname', 'elm')])])]), 'elm': Node('∨', [Node('∧', [Node('rname', 'prefix'), Node('∨', [Node('rname', 'assign_eql'), Node('rname', 'assign_cln'), Node('rname', 'group'), Node('rname', 'str'), Node('rname', 'rname')]), Node('rname', 'suffix')])]), 'assign_eql': Node('∨', [Node('∧', [Node('rname', 'rname'), Node('?', [Node('rname', 'W')]), Node('ᔐ', '='), Node('?', [Node('rname', 'W')]), Node('rname', 'elm_o')])]), 'assign_cln': Node('∨', [Node('∧', [Node('rname', 'rname'), Node('?', [Node('rname', 'W')]), Node('ᔐ', ':'), Node('?', [Node('rname', 'W')]), Node('rname', 'elm_j')])]), 'group': Node('∨', [Node('∧', [Node('ᔐ', '('), Node('?', [Node('rname', 'W')]), Node('rname', 'group_inner'), Node('ᔐ', ')')])]), 'group_inner': Node('∨', [Node('*', [Node('∧', [Node('rname', 'elm_o'), Node('?', [Node('rname', 'W')])])])]), 'str1': Node('∨', [Node('~', regex.Regex('"(␛␛.|[^"])*"', flags=regex.V0))]), 'str2': Node('∨', [Node('~', regex.Regex("'(␛␛.|[^'])*'", flags=regex.V0))]), 'str3': Node('∨', [Node('~', regex.Regex('‹(␛␛.|[^›])*›', flags=regex.V0))]), 'str': Node('∨', [Node('rname', 'str1'), Node('rname', 'str2'), Node('rname', 'str3')]), 'rname': Node('∨', [Node('~', regex.Regex('[^⯅⯆△▽↷\U000f01b4()?❗⮞.:⠶✗+*=¬∨∧~‹#\'" \\t\\n]+|✗', flags=regex.V0))]), 'prefix': Node('∨', [Node('∧', [Node('?', [Node('rname', 'w')]), Node('+', [Node('∧', [Node('~', regex.Regex('[\U000f01b4❗⮞⠶~¬]', flags=regex.V0)), Node('?', [Node('rname', 'W')])])])]), Node('?', [Node('rname', 'w')])]), 'suffix': Node('∨', [Node('∧', [Node('+', [Node('∧', [Node('?', [Node('rname', 'W')]), Node('~', regex.Regex('[*+?]', flags=regex.V0))])]), Node('?', [Node('rname', 'w')])]), Node('?', [Node('rname', 'w')])]), 'w': Node('∨', [Node('~', regex.Regex('([ \\t]|␛␛\\n)+', flags=regex.V0))]), 'W': Node('∨', [Node('~', regex.Regex('([ \\t\\n]|␛␛\\n)+', flags=regex.V0))])}
Parser = lambda g, B=Gram(rules_bootstrap): Gram(gram_convert(B(g, "statements")))

coolio = r"""
main = 󰆴a?⯅b  ❗a⯅b
a="a"
b="b"
w = ~"([ \t]|␛␛\n)+"
W = ~"([ \t\n]|␛␛\n)+"
"""

k = Parser(coolio)
print(*k.rules.items(),sep=ń)
k(("abababa")).print()