try:
    from util import *
except:
    import sys ; sys.path.insert(0, "..") ; from util import *

from node import *
import sys

escape = lambda x,t='ݺ':ᖇ(ᖇ(ᖇ(x,"␛␛",t),'␛',ᐦ),t,'␛')

def mk(t, *c):
    if flag := c and c[-1] is None: del c[-1]
    if t == '~': return Node('~', re.compile(c[0].txt))
    c = [mk(*x) if ᐹ(x, tuple) else x for x in c]
    return Node(t, c[0] if flag else c)

def parse_elm(N):
    pre, n, suf = N
    l1, l2 = partition("❗⠶ƨ".__contains__, sorted(pre.txt, key="❗⠶ƨ󰆴¬⮞~".index))
    for k in chain(l1, suf.txt, l2):
        n = mk(k, n)
    return n

def reduce_j(N):
    α, o, β, *C = N
    if C: β = reduce_j(N.copy(c=[β, *C]))
    match o.c:
        case '↷': r = mk('∧', α, β, α)
        case '△': r = mk('∨', ('∧', ('*', ('∧', α, β)), α), α)
        case '▽': r = mk('∨', ('∧', ('∧', β, ('*', ('∧', α, β)))), Ń('✓')) # why so many "∧"
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

CHECK = Node('✓')
QUESTION = Node('?')
LOOKAHEAD_NEG = Node('¬')
class Gram:
    ind = ᐦ
    def __init__(𝕊, rules, DEBUG=ⴴ): 𝕊.rules = rules
    def __contains__(𝕊, c): return c in 𝕊.rules
    def __repr__(𝕊): return f"{Т(𝕊).__name__}[rules={𝕊.rules}]"
    
    def __call__(𝕊, content, rule="main", allow_deletes=ⴳ, DEBUG=ⴴ, **𝕂):
        content = ᒪ(content)
        secs = {((α:=(z:=ᒪ(y))[0][0],β:=z[-1][0]+1)):ᒍ(ᐦ,content[α:β]) for x,y in groupby(enum(content), lambda x: ᐹ(x[1],ᔐ)) if x}
        gseg = ρ(𝕊.get_segment, d=secs, k=tuple(secs.keys()))
        𝑓 = ρ(𝕊.dbg_run if DEBUG else 𝕊.run, m={}, content=content, gseg=gseg, **𝕂)
        𝑓.keywords['f'] = 𝑓
        tree = 𝑓(0, Node("rname", rule))
        if not tree or tree[1] != ⵌ(content):
            if tree:
                try:
                    part = 𝕊.chop(tree[0], allow_deletes=allow_deletes, content=content)
                except Exception:
                    print("Failed to chop tree!")
                    part = tree[0]
                try:
                    print("Incomplete parse tree:")
                    part.print()
                except Exception:
                    print("Failed to pretty print tree!")
                    print(f"Current tree: {tree[0]}")
                print(f"Remainder: {tree[1]}")
                assert ⴴ, f"Peggle failed to complete!"
            else:
                assert ⴴ, f"Peggle failed without generating tree!"
        return 𝕊.chop(tree[0], allow_deletes=allow_deletes, content=content)
    
    @staticmethod
    def get_segment(χ, d, k):
        a, b = 0, ⵌ(k)
        while True:
            n = (a + b) // 2
            α, β = γ = k[n]
            if α <= χ <= β: return d[γ][χ-α:]
            if   α > χ:
                if b == n: return
                a, b = a, n
            elif β < χ:
                if a == n: return
                a, b = n, B
    
    def merge_rules(𝕊, rules): return Gram(𝕊.rules | rules)
    def print_rules(𝕊): [(print(f'Rule "{k}":'), v.print()) for k, v in 𝕊.rules.items()]
    
    def dbg_run(𝕊, χ, r, *, 𝑓, gseg, m, content, z=0, ONLY_NAMED=ⴴ):
        wr = lambda x: Z.G+x+Z.W
        
        LE = lambda x: len(x)-sum(x.count(y)*len(y) for y in (Z.G, Z.W, Z.BL, Z.bYEL, Z.bBLA))
        
        t, c = r.t, r.c
        convs = lambda t,c: f"{Z.BL}{c}{Z.W}" if t == "rname" else f"{t}"
        nam = convs(t,c)
        
        def fmt(A, c, l, B=ᐦ, sf=ⴴ):
            c = ᒍ(ᐦ, [*c[:l], Z.bYEL+[K:=(c[l] if l<ⵌ(c) else (l==ⵌ(c) and ś or ᐦ)),ś][K==ń]+Z.bBLA, [ᐦ,ń][K == ń], *c[l+1:]])
            return ń.join([(Gram.ind[:-2] if (sf and not i) else Gram.ind)+(ś*(LE(A)-sf*2) if i else A)+x for i,x in enumerate(c.split(ń))])+B
        
        if not ONLY_NAMED or t == "rname":
            Gram.ind += "│ " if t == "rname" else "  "
            print(fmt(f"→ {nam}: {wr('󰅁')}", content, χ, wr('󰅂'), sf=ⴳ))
            res = 𝕊.run(χ, r, 𝑓=𝑓, gseg=gseg, m=m, content=content, z=z)
            Gram.ind = Gram.ind[:-2]
            
            if res:
                print(fmt(f"← {nam}: {wr('󰅁')}", content, res[1], wr('󰅂')))
            else:
                print(fmt(f"← {nam}: ", "∅", 99))
            return res
        else:
            return 𝕊.run(χ, r, 𝑓=𝑓, gseg=gseg, m=m, content=content, z=z)
    
    def run(𝕊, χ, r, *, 𝑓, gseg, m, content, z=0):
        t, c, m = r.t, r.c, {} if m is None else m
        if t == '←':
            α, β = c
            j = 𝑓(χ, β, z=z+1)
            if j: return j[0].copy(e=α.c), j[1]
            return # var bind to something that failed, wat do?
        if t == "rname":
            if c == '✗': assert ⴴ # die
            if c == '✓': return CHECK, χ # good
            
            k = χ, c
            if k in m:
                return m[k] or None
            
            j = 𝑓(χ, 𝕊.rules[c], z=z+1)
            if j:
                α, β = j
                m[k] = r = Node(c, [α]), β
            else:
                m[k] = r = None
            return r
        
        if t in "*+∧":
            R = []
            if t in '*+': # as many as possible
                while v := 𝑓(χ, c[0], z=z+1):
                    α, χ = v
                    R.append(α)
                if t == '+' and not R: return # empty plus we leave!!!1
            else: # concatination
                for x in c:
                    if not (v := 𝑓(χ, x, z=z+1)): return
                    α, χ = v
                    R.append(α)
            return Node(t, R), χ
        match t:
            case '?': # its okay you can eat when you want to
                if v := 𝑓(χ, c[0], z=z+1):
                    return Node(t, [v[0]]), v[1]
                return QUESTION, χ
            case '∨': # pick first
                for x in c:
                    if (v := 𝑓(χ, x, z=z+1)): return v
            case '~'|'ᔐ': # regex/str
                if (ƨ := gseg(χ)) is None: return
                if t == '~':
                    if not (ma := c.match(ƨ)): return
                    l = ma.span()[1]
                elif t == 'ᔐ':
                    if not ƨ.startswith(c): return
                    l = ⵌ(c)
                return Node(t, (χ, p := χ+l)), p
            case '❗': # match or die
                if not (v := 𝑓(χ, c[0], z=z+1)): assert ⴴ
                return Node(t, [v[0]]), v[1]
            case '󰆴': # eat & delete
                if not (v := 𝑓(χ, c[0], z=z+1)): return
                return Node(t, [v[0]]), v[1]
            case 'ƨ':
                if not (v := 𝑓(χ, c[0], z=z+1)): return
                return Node(t, [v[0]]), v[1]
            case '⠶': # flatten / atom
                if not (v := 𝑓(χ, c[0], z=z+1)): return
                return Node(t, v[0].c), v[1]
            case '⮞': # positive lookahead
                if not (v := 𝑓(χ, c[0], z=z+1)): return
                return Node(t, [v[0]]), χ
            case '¬': # negative lookahead
                if v := 𝑓(χ, c[0], z=z+1): return
                return LOOKAHEAD_NEG, χ
            case _: # unwillingly die
                assert ⴴ, f"Invalid instruction '{t}'!"
    
    def chop(𝕊, n, allow_deletes=ⴳ, *, content):
        return n \
            .child_killer(lambda n,S=FS("⮞¬"+'󰆴'*allow_deletes): n.t in S and not n.e) \
            .find_replace(
                lambda n, S=FS("ᔐ~"): n.t in S,
                lambda n: Node(c=ᒍ(ᐦ,content[n.c[0]:n.c[1]]))) \
            .find_replace(lambda n: n.t == "ƨ",
                          lambda n: Node(c=ᒍ(ᐦ, [k.txt for k in n.c]))) \
            .flatten_kids(lambda n,S=FS("∧∨~+*?ƨᔐ⮞⠶❗"): n.t in S) \
            .find_replace(lambda n: ⵌ(n)==1 and ᐹ(β:=n.c[0],Node) and not β.t,
                          lambda n: n.copy(c=n.txt))
    
ŕ, ñ = re.compile, Node
Parser = lambda g, *𝔸, B=Gram({'statements': ñ('∨', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('*', [ñ('∧', [ñ('∨', [ñ('rname', 'comment'), ñ('rname', 'elm_o')]), ñ('?', [ñ('rname', 'W')])])])])]), 'comment': ñ('∨', [ñ('~', ŕ('[\ueb26#][^\\n]*'))]), 'elm_o': ñ('∨', [ñ('∧', [ñ('rname', 'elm_a'), ñ('*', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', '∨'), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'elm_a')])])])]), 'elm_a': ñ('∨', [ñ('∧', [ñ('rname', 'elm_j'), ñ('*', [ñ('∧', [ñ('∨', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', '∧'), ñ('?', [ñ('rname', 'W')])]), ñ('?', [ñ('rname', 'w')])]), ñ('rname', 'elm_j')])])])]), 'elm_j': ñ('∨', [ñ('rname', '_elm_j'), ñ('rname', 'elm')]), '_elm_j': ñ('∨', [ñ('∧', [ñ('rname', 'elm'), ñ('?', [ñ('rname', 'W')]), ñ('~', ŕ('[⯅⯆△▽↷]')), ñ('?', [ñ('rname', 'W')]), ñ('∨', [ñ('rname', '_elm_j'), ñ('rname', 'elm')])])]), 'elm': ñ('∨', [ñ('∧', [ñ('rname', 'prefix'), ñ('∨', [ñ('rname', 'assign_eql'), ñ('rname', 'assign_cln'), ñ('rname', 'group'), ñ('rname', 'str'), ñ('rname', 'rname')]), ñ('rname', 'suffix')])]), 'assign_eql': ñ('∨', [ñ('∧', [ñ('rname', 'rname'), ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', '='), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'elm_o')])]), 'assign_cln': ñ('∨', [ñ('∧', [ñ('rname', 'rname'), ñ('?', [ñ('rname', 'W')]), ñ('ᔐ', ':'), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'elm_j')])]), 'group': ñ('∨', [ñ('∧', [ñ('ᔐ', '('), ñ('?', [ñ('rname', 'W')]), ñ('rname', 'group_inner'), ñ('ᔐ', ')')])]), 'group_inner': ñ('∨', [ñ('*', [ñ('∧', [ñ('rname', 'elm_o'), ñ('?', [ñ('rname', 'W')])])])]), 'str1': ñ('∨', [ñ('~', ŕ('"(␛.|[^"])*"'))]), 'str2': ñ('∨', [ñ('~', ŕ("'(␛.|[^'])*'"))]), 'str3': ñ('∨', [ñ('~', ŕ('‹(␛.|[^›])*›'))]), 'str': ñ('∨', [ñ('rname', 'str1'), ñ('rname', 'str2'), ñ('rname', 'str3')]), 'rname': ñ('∨', [ñ('~', ŕ('[^⯅⯆△▽↷󰆴()?❗⮞.:⠶ƨ✗+*=¬∨∧~‹#\'" \\t\\n]+|✗'))]), 'prefix': ñ('∨', [ñ('∧', [ñ('?', [ñ('rname', 'w')]), ñ('+', [ñ('∧', [ñ('~', ŕ('[󰆴❗⮞⠶ƨ~¬]')), ñ('?', [ñ('rname', 'W')])])])]), ñ('?', [ñ('rname', 'w')])]), 'suffix': ñ('∨', [ñ('∧', [ñ('+', [ñ('∧', [ñ('?', [ñ('rname', 'W')]), ñ('~', ŕ('[*+?]'))])]), ñ('?', [ñ('rname', 'w')])]), ñ('?', [ñ('rname', 'w')])]), 'w': ñ('∨', [ñ('~', ŕ('([ \\t]|␛\\n)+'))]), 'W': ñ('∨', [ñ('~', ŕ('([ \\t\\n]|␛\\n)+'))])}), **𝕂: Gram(gram_convert(B(g, "statements")), *𝔸, **𝕂)

def test_peggle():
    p = Parser(r"""
        main    = (entry 󰆴W?)*
        entry   = (
            (section=󰆴'[' wrd 󰆴']') 󰆴W?
            (pair = (
                (coolPropertyExample:key = ⠶wrd) 󰆴(w? ↷ '=')
                (value = (wrd ∨ str)+) 󰆴W? ) )* )

        str     = ~‹"[^"]+"›
        wrd     = ~‹[-\w]+›
        w       = ~‹[ \t]+›
        W       = ~‹[ \t\n]+›
    """)
    c = r"""[section]
    somekey = somevalue
    someotherkey=someothervalue

    [anothersection]
    key123 = "swooce"
    key456="yet another one here"
    """ * 100
    
    # p = Parser(r"""
    #     main = ((number∨A∨B∨C∨D) 󰆴W?)*
    #     number = ƨ(~‹\.[0-9]+|[0-9]+(\.([0-9]+))?|0[oxbOXB][0-9]+|[0-9]+e[0-9]+›)
    #     A      = ƨ(‹a›)
    #     B      = ƨ(‹b›)+
    #     C      = ƨ(~‹C›)+
    #     D      = ƨ(‹C› ~‹C+›)
    #     W      = ~‹[ \t\n]+›
    # """)
    # c = """20.2 .1323 .125 a a bb C CCC"""
    
    # p = Parser(r"""
    #     main = main = ƨ("A:" 󰆴(~‹a›)) "b" 󰆴"c" ⠶("a" "b") ƨ(a+)
    #     a = "h"
    # """)
    # c = """A:abcabhhhhhhhh"""
    
    print("Rules:")
    p.print_rules()
    togprof()
    print("Results:")
    tr = p(c)
    togprof()
    tr.print()

if __name__ == "__main__":
    test_peggle()