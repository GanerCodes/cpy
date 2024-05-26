from mapping import *
import keyword as py_kw

py_bad_string_chr = lambda s, bad="\\\"'{}": s in bad
py_escape_char    = lambda c, pre='': pre+HX(c) if py_bad_string_chr(c) else c
py_escape_string  = lambda s: ''.join(py_escape_char(c, '\\u') for c in s)
py_escape_var     = lambda s: ''.join(f'_{HX(c)}' if ord(c) > 127 else c for c in s)
py_special_mapper = lambda c, m={'𝗻':'\\n','𝘀':' ','𝘁':'\\t'}: m[c]

PY_ARGS = py_escape_var("𝔸")
PY_KWARGS = py_escape_var("𝕂")
PY_NULL_SPECIAL = "NULL"

class Node_py(Node):
    @classmethod
    def gen_metaop(ℂ, op_, op, l, r, L, R):
        if not isinstance(l, str): l = l.text
        if not isinstance(r, str): r = r.text
        return f"ℜ('{op.t}', {L}, {R}"+(f", l='{l}'" if l else '') + (f", r='{r}'" if r else '')+')'
    
    @classmethod
    def gen_op(ℂ, op_, op, L=ℕ, R=ℕ):
        L = (L:=reach_first(L)) and L.reparse() or ℕ
        R = (R:=reach_first(R)) and R.reparse() or ℕ
        
        if op_.text == op.t and op.t in ℂ.builtin_ops and \
                ℂ.valid_op_args(op, L is not ℕ, R is not ℕ):
            L = '' if L is ℕ else L
            R = '' if R is ℕ else R
            return ℂ(f"{L}{ℂ.builtin_ops[op.t]}{R}", 'ℂ')
        l, r = op_.children[0], op_.children[2]
        L = PY_NULL_SPECIAL if L is ℕ else L
        R = PY_NULL_SPECIAL if R is ℕ else R
        s = ℂ.gen_metaop(op_, op, l, r, L, R)
        return ℂ(s, 'ℂ')
    
    def gen_lambda(𝕊):
        h, b = 𝕊.children
        h = h.children[0]
        if h.expr_name == "lamb_h_preset":
            H = ''.join(x+',' for x in [*"xyzw"[:"𝚲①②③④".index(h.text)]])
            H = f"{H}*{PY_ARGS},**{PY_KWARGS}"
        elif h.expr_name == "lamb_h_implicit":
            H = f"{h.children[0].text},*{PY_ARGS},**{PY_KWARGS}"
        elif h.expr_name == "lamb_h_normal":
            h = h.children[1]
            exprs = 𝕊.partition(h.children, lambda x: x.text == ',', keep_sep=𝔽)
            has_a = has_k = 𝔽
            for e in exprs:
                if not (t := ''.join(k.text for k in e).strip()):
                    continue
                if t[:2] == '**': has_k = 𝕋
                elif t[0] == '*': has_a = 𝕋
            
            if has_a and has_k:
                H = h.reparse()
            elif has_a:
                H = h.reparse()+f',**{PY_KWARGS}'
            elif has_k:
                H = h.reparse()+f',*{PY_ARGS}'
            else:
                H = h.reparse()+f',*{PY_ARGS},**{PY_KWARGS}'
        else:
            assert 𝔽
        return f"(lambda {H}: {b.children[0].reparse()})"
    
    def reparse(𝕊):
        match 𝕊.expr_name:
            case "oper": # for various reasons this is only for Σ´
                return 𝕊.gen_op(𝕊, OP(𝕊.children[1].text)).text
            case "variable":
                return py_escape_var(𝕊.text)
            case "exprs":
                return 𝕊.parse_exprs(𝕊.children).text
            case "lamb":
                return 𝕊.gen_lambda()
            case "str_guts":
                return py_escape_string(𝕊.text)
            case "str_escape":
                return "'" + py_escape_string(𝕊.text[1:]) + "'"
            case "str_sub":
                return "{" + 𝕊.children[1].reparse() + "}"
            case "str_spec_char":
                return "'" + py_special_mapper(𝕊.text) + "'"
            case "special_str":
                r = '"'
                for c in 𝕊.children[1:-1]:
                    match c.expr_name:
                        case "str_escape":
                            r += py_escape_string(c.text[1:])
                        case "str_spec_char":
                            r += py_special_mapper(c.text)
                        case _:
                            r += c.reparse()
                return r + '"'
            case _: # ex. py_str, s, etc.
                if not 𝕊.children:
                    return 𝕊.text
                else:
                    return 𝕊.into_expr(𝕊.children, '').text

class Mapper_py(Mapper):
    SPECIALS = "ℵ𝕋𝔽îπτ□∅∞ᐦ"
    GRAM_FILE = "cpy.gram"
    OPERATOR_FILE = "cpy.ops"
    NODE_CLS = Node_py
    
    builtin_ops = r""". . ∣ , , ∣ : : ∣ % % ∣ @ @ ∣ ⠤ * ∣ * * ∣ ⨯ * ∣ ⋅ * ∣ ⠶ ** ∣ ** ** ∣ / / ∣ ÷ / ∣ + + ∣ - - ∣ ¯ - ∣ ^ ^ ∣ & & ∣ | | ∣ ≔ := ∣ < < ∣ > > ∣ << << ∣ >> >> ∣ ∧ and ∣ ∨ or ∣ ∈ in ∣ ∉ not𝐬in ∣ ¿ if ∣ ⸘ elif ∣ ¡ else"""
    builtin_ops = dict(
        (lambda y:(y[0],y[1].replace('𝐬',' ')))(x.strip().split(' ', 1))
            for x in builtin_ops.replace('\n', '∣').split('∣') )
    
    def __init__(𝕊):
        super().__init__()
        𝕊.NODE_CLS.builtin_ops = 𝕊.builtin_ops
    
    @classmethod
    def generate_gram_regexes(ℂ, op_names):
        rgx_keywords = rgx_or(py_kw.kwlist + py_kw.softkwlist)
        rgx_operator = rgx_or(flat([re.escape(c+'='), re.escape(c)] for c in op_names))
        rgx_specials = rgx_or([*"ℵ𝕋𝔽îπτ□∅∞ᐦ", "\\."*3])
        return {
            "OPERATORS": i_rgx_fmt(rgx_operator),
            "VAR_SPECIAL": i_rgx_fmt(rgx_specials),
            "KEYWORDS": i_rgx_fmt(f"({rgx_keywords})(\\Z|[^_a-zA-Z0-9])") }

from timeit import default_timer as timer

t_A = timer()
tree = Mapper_py()
t_B = timer()
f_0 = t_B - t_A

t_A = timer()
tree = tree("test.txt")
t_B = timer()
f_1 = t_B - t_A

t_A = timer()
tree = tree.reduce()
t_B = timer()
f_2 = t_B - t_A

t_A = timer()
parsed = tree.reparse()
t_B = timer()
f_3 = t_B - t_A


tree.collapse().print()
print('-'*50)
print(parsed)

print('load', f_0)
print('parse', f_1)
print('reduce', f_2)
print('reparse', f_3)

# actual operators
# blocks
# 

# V,pr=0,lambda*a,**k:print(V*'#',*a,**k)
# def A(*a,**k): global V ; V += 1 ; pr(*a,**k)
# def B(*a,**k): global V ; pr(*a,**k) ; V -= 1