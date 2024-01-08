from util import *
from node import *

escape = lambda x,t='ݺ':ᖇ(ᖇ(ᖇ(x,"␛␛",t),'␛',ᐦ),t,'␛')

def mk(t, *c):
    if flag := c and c[-1] is None: del c[-1]
    if t == '~': return Node('~', re.compile(c[0].txt))
    c = [mk(*x) if ᐹ(x, tuple) else x for x in c]
    return Node(t, c[0] if flag else c)

def parse_elm(N):
    pre, n, suf = N
    l1, l2 = partition("❗⠶".__contains__, sorted(pre.txt, key="❗⠶󰆴¬⮞~".index))
    for k in chain(l1, suf.txt, l2):
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
    name_remaps = { "elm_o": '∨', "elm_a": '∧', "assign_cln": '←', "group_inner": '∧' }
    rules = t \
         .child_killer(lambda n: n.t == "comment") \
         .      filter(lambda n: not (n.t and n.t in "wW")) \
         .      filter(lambda n: not (not n.t and n.c and n.c in "()∧∨:=")) \
         .find_replace(lambda n: n.t in ("prefix", "suffix"), lambda n: n.copy(c=n.txt)) \
         .find_replace(lambda n: n.t == "str", lambda n: n.copy(c=escape(n.txt[1:-1]))) \
         .find_replace(lambda n: n.t in name_remaps, lambda n: n.copy(name_remaps[n.t])) \
         .flatten_kids(lambda n: n.t == "_elm_j") \
         .collect_kids(lambda n: n.t == "assign_eql")
    rules = { r.C[0].c:r.C[1] for r in rules }
    for k, v in rules.items():
        rules[k] = v \
            .find_replace(lambda n: n.t == "assign_eql", lambda n: n.C[0]) \
            .find_replace(lambda n: n.t == "elm", parse_elm) \
            .flatten_kids(lambda n: ⵌ(n) == 1 and n.t in (*"∨∧", "elm_j")) \
            .find_replace(lambda n: n.t == "elm_j", reduce_j) \
            .flatten_kids(lambda n: ⵌ(n) == 1 and n.t == "group") \
            .find_replace(lambda n: n.t == "group", lambda n: n.copy('∧')) \
            .find_replace(lambda n: n.t == "str", lambda n: n.copy('ᔐ', n.txt))
        
    return rules

class Gram:
    def __init__(𝕊, rules):
        𝕊.rules = rules
    
    def __call__(𝕊, content, rule="main", allow_deletes=ⴳ):
        𝕊.ST = content
        tree = 𝕊.run([Node(('□', i), c) for i, c in enum(content)], Node("rname", rule))
        
        if not tree or tree[1]:
            if tree:
                assert ⴴ, f"Didn't finish:\n\tCurrent tree: {tree[0]}\n\tRemainder: {tree[1]}"
            else:
                assert ⴴ, f"Didn't finish, failed!"
        return 𝕊.chop(tree[0], allow_deletes=allow_deletes)
    
    def __contains__(𝕊, c):
        return c in 𝕊.rules
    
    def __repr__(𝕊):
        return f"{Т(𝕊).__name__}[rules={𝕊.rules}]"
    
    def print_rules(𝕊):
        for k, v in 𝕊.rules.items():
            print(f'Rule "{k}":')
            v.print()
    
    def merge_rules(𝕊, rules):
        return Gram(𝕊.rules | rules)
    
    def run(𝕊, s, r, *, m=ᗜ):
        t, c, m = r.t, r.c, {} if m is None else m
        if t == '←':
            α, β = c
            j = 𝕊.run(s, β, m=m)
            if j:
                return j[0].copy(e=α.c), j[1]
            else:
                ...
                return
        if t == "rname":
            if c == '✗': # die
                assert ⴴ
            if c == '✓': # good
                return Node('✓'), s
            
            loc = s[0].t[1] if s else -1
            k = loc, c
            if k in m:
                if not (j := m[k]):
                    return
                return j[0], s[j[1]:]
            
            j = 𝕊.run(s, 𝕊.rules[c], m=m)
            if j:
                α, σ = j
                r = Node(c, [α]), σ
                m[k] = r[0], ⵌ(s)-ⵌ(σ)
            else:
                m[k] = r = None
            return r
        
        if t in "*+∧":
            R = []
            if t in '*+': # as many as possible
                while v := 𝕊.run(s, c[0], m=m):
                    α, s = v
                    R.append(α)
                if t == '+' and not R: return # empty plus we leave!!!1
            else: # concatination
                for x in c:
                    if not (v := 𝕊.run(s, x, m=m)): return
                    α, s = v
                    R.append(α)
            return Node(t, R), s
        match t:
            case '?': # its okay you can eat when you want to
                if v := 𝕊.run(s, c[0], m=m):
                    return Node(t, [v[0]]), v[1]
                return Node(t), s
            case '∨': # pick first
                for x in c:
                    if (v := 𝕊.run(s, x, m=m)): return v
            case '~'|'ᔐ': # regex/str
                L = s[0].t[1] if s else 10**12
                st = 𝕊.ST[L:]
                if t == '~':
                    if not (ma := c.match(st)): return
                    R = ma.span()[1]
                elif t == 'ᔐ':
                    if not st.startswith(c): return
                    R = ⵌ(c)
                return Node(t, s[:R]), s[R:]
            case '❗': # match or die
                if not (v := 𝕊.run(s, c[0], m=m)): assert ⴴ
                return Node(t, [v[0]]), v[1]
            case '󰆴': # eat & delete
                if not (v := 𝕊.run(s, c[0], m=m)): return
                return Node(t, [v[0]]), v[1]
            case '⠶': # flatten
                if v := 𝕊.run(s, c[0], m=m): return Node(t, v[0].c), v[1]
            case '⮞': # positive lookahead
                if not (v := 𝕊.run(s, c[0], m=m)): return
                return Node(t, [v[0]]), s
            case '¬': # negative lookahead
                if v := 𝕊.run(s, c[0], m=m): return
                return Node(t), s
            case _: # unwillingly die
                assert ⴴ, f"Invalid instruction '{t}'!"
    
    def chop(𝕊, n, allow_deletes=ⴳ):
            # .print() \
        return n \
            .child_killer(lambda n,S=FS("⮞¬"+'󰆴'*allow_deletes): n.t in S or (n.t == '✓' and not n.e)) \
            .flatten_kids(lambda n,S=FS("∧∨~+*?ᔐ⠶⮞❗"): n.t in S) \
            .find_replace(
                lambda n: n.L,
                lambda n: n.copy(c=ᒪ(map_groups(n.C,
                    lambda n: ᐹ(n.t,tuple) and n.t[0]=='□',
                    lambda l: Ń(ᐦ, ᒍ(ᐦ, l)),
                    lambda n: n.txt)))) \
            .find_replace(lambda n: n.L and ⵌ(n) == 1 and n.C[0].t in "~ᔐ",
                          lambda n: n.copy(c=n.txt)) \
            .flatten_kids(lambda n: n.t == '⠶')
    
ŕ, ñ = ρ(re.compile, flags=regex.V0), Node
Parser = lambda g, B=Gram({'statements': ñ('∨', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('*', [ñ('∧', [ñ('∨', [ñ('rname', 'comment'), ñ('rname', 'elm_o')]), ñ('?', [ñ('rname', 'W')])])])])]), 'comment': ñ('∨', [ñ('~', ŕ('[\ueb26#][^\\n]*'))]), 'elm_o': ñ('∨', [ñ('∧', [ñ('rname', 'elm_a'), ñ('*', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', '∨'), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'elm_a')])])])]), 'elm_a': ñ('∨', [ñ('∧', [ñ('rname', 'elm_j'), ñ('*', [ñ('∧', [ñ('∨', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', '∧'), ñ('?', [ñ('rname', 'W')])]), ñ('?', [ñ('rname', 'w')])]), ñ('rname', 'elm_j')])])])]), 'elm_j': ñ('∨', [ñ('rname', '_elm_j'), ñ('rname', 'elm')]), '_elm_j': ñ('∨', [ñ('∧', [ñ('rname', 'elm'), ñ('?', [ñ('rname', 'W')]), ñ('~', ŕ('[⯅⯆△▽↷]')), ñ('?', [ñ('rname', 'W')]), ñ('∨', [ñ('rname', '_elm_j'), ñ('rname', 'elm')])])]), 'elm': ñ('∨', [ñ('∧', [ñ('rname', 'prefix'), ñ('∨', [ñ('rname', 'assign_eql'), ñ('rname', 'assign_cln'), ñ('rname', 'group'), ñ('rname', 'str'), ñ('rname', 'rname')]), ñ('rname', 'suffix')])]), 'assign_eql': ñ('∨', [ñ('∧', [ñ('rname', 'rname'), ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', '='), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'elm_o')])]), 'assign_cln': ñ('∨', [ñ('∧', [ñ('rname', 'rname'), ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', ':'), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'elm_j')])]), 'group': ñ('∨', [ñ('∧', [ñ('ᔐ', '('), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'group_inner'), ñ('ᔐ', ')')])]), 'group_inner': ñ('∨', [ñ('*', [ñ('∧', [ñ('rname', 'elm_o'), ñ('?', [ñ('rname', 'W')])])])]), 'str1': ñ('∨', [ñ('~', ŕ('"(␛.|[^"])*"'))]), 'str2': ñ('∨', [ñ('~', ŕ("'(␛.|[^'])*'"))]), 'str3': ñ('∨', [ñ('~', ŕ('‹(␛.|[^›])*›'))]), 'str': ñ('∨', [ñ('rname', 'str1'), ñ('rname', 'str2'), ñ('rname', 'str3')]), 'rname': ñ('∨', [ñ('~', ŕ('[^⯅⯆△▽↷󰆴()?❗⮞.:⠶✗+*=¬∨∧~‹#\'" \\t\\n]+|✗'))]), 'prefix': ñ('∨', [ñ('∧', [ñ('?', [ñ('rname', 'w')]), ñ('+', [ñ('∧', [ñ('~', ŕ('[󰆴❗⮞⠶~¬]')), ñ('?', [ñ('rname', 'W')])])])]), ñ('?', [ñ('rname', 'w')])]), 'suffix': ñ('∨', [ñ('∧', [ñ('+', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('~', ŕ('[*+?]'))])]), ñ('?', [ñ('rname', 'w')])]), ñ('?', [ñ('rname', 'w')])]), 'w': ñ('∨', [ñ('~', ŕ('([ \\t]|␛\\n)+'))]), 'W': ñ('∨', [ñ('~', ŕ('([ \\t\\n]|␛\\n)+'))])}): Gram(gram_convert(B(g, "statements")))

if __name__ == "__main__":
    # togprof()
    p = Parser(r"""
        main    = (entry 󰆴W?)*
        entry   = (
            (section=󰆴'[' wrd 󰆴']') 󰆴W?
            (pair = (
                (sand:key   = ⠶wrd) 󰆴(w? ↷ '=') egg:✓
                (value = (wrd ∨ str)+) 󰆴W? ) )* )

        str     = ~‹"[^"]+"›
        wrd     = ~‹[-\w]+›
        w       = ~‹[ \t]+›
        W       = ~‹[ \t\n]+›
    """)
    # togprof()
    
    p.print_rules()
    
    c = r"""[section]
    somekey = somevalue
    someotherkey=someothervalue

    [anothersection]
    key123 = "swooce"
    key456="yet another one here"
    """ * 1
    
    # togprof()
    tr = p(c)
    
    print(tr['sand'])
    
    # togprof()
    tr.print()