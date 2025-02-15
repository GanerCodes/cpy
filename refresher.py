from util import *
from cpy_transpile import Compiler, MOON_DIR
import subprocess, traceback

BASE_CACHE_DIR = "/tmp/cpy_cache"
CODE_CACHE_DIR = f"{BASE_CACHE_DIR}/code"
GRAM_CACHE_DIR = f"{BASE_CACHE_DIR}/gram"
HISTORY_FILE   = f"{BASE_CACHE_DIR}/cpy_cli.hist"

def capture_output(𝑓, *𝔸, **𝕂):
    from contextlib import redirect_stdout
    import io
    
    with redirect_stdout(s := io.StringIO()):
        try:
            return (𝑓(*𝔸, **𝕂), ⴳ), s.getvalue()
        except Exception as e:
            return (e, ⴴ), s.getvalue()+ń+traceback.format_exc()

def py_reparse(x):
    import ast
    try:
        return ast.unparse(ast.parse(x))
    except Exception as e:
        raise Exception(f'Failed to reparse code! "{e}"\nCode:\n{prettify_code(x)}')

# stupid monkeypatching garvbarebefshiskodjl
if not hasattr(traceback.linecache, "CPY_CACHE"):
    traceback.linecache.CPY_CACHE = {}
def remember_code_for_tracebacks(path, code, *, funky_monkey={"monkeys": set()}, monkemonEeamnoNEKEEE={}):
    traceback.linecache.CPY_CACHE[path] = code
    monkemonEeamnoNEKEEE[path] = code.split(ń)
    if "monke" not in funky_monkey:
        funky_monkey["monke"] = traceback.linecache.checkcache
        funky_monkey["monkeys"].add(path)
        def monkeymonkeymonkeymonkeymonkey(munkee=None):
            if munkee in funky_monkey["monkeys"]: return
            try:
                return funky_monkey["monke"](munkee)
            except Exception as e:
                print("Monke error:", e)
                return
        gl = traceback.linecache.getlines
        traceback.linecache.checkcache = monkeymonkeymonkeymonkeymonkey
    funky_monkey["monkeys"].add(path)
    traceback.linecache.cache[path] = (ᐦ, ᐦ, code.split(ń), )

def dynamic_compile_py(c, file):
    try               : return compile(c, file, m:="eval"), m
    except SyntaxError: return compile(c, file, m:="exec"), m

def compile_py(code, ns, file=ᗜ, mode="exec"):
    if file is ᗜ: file = ns.get("__file__", "cpy-interactive")
    if mode == "dynamic": return file, *dynamic_compile_py(code, file)
    else                : return file, compile(code, file, mode), mode

def run_inj_tb(code, ns, file=ᗜ, mode="exec"):
    file, compiled, mode = compile_py(code, ns, file, mode)
    remember_code_for_tracebacks(file, code)
    return (exec if mode=="exec" else eval)(compiled, ns)

def basic_cpy_session(do_cache=ⴳ, ns=ᗜ, hns=ᗜ,
                      fname="cpy-interactive", header_carry=ᗜ,
                      code_cache_dir=CODE_CACHE_DIR,
                      gram_cache_dir=GRAM_CACHE_DIR,
                      **𝕂):
    compiler = Compiler(code_cache_dir, gram_cache_dir)
    
    lang_pfx = os.path.abspath(f"{MOON_DIR}/☾")
    code_pfx = os.path.abspath(f"{lang_pfx}/Code")
    libr_pfx = os.path.abspath(f"{lang_pfx}/Libraries")
    header_f = os.path.abspath(f"{code_pfx}/HEADER")
    for f in (code_pfx, libr_pfx):
        f in sys.path or sys.path.insert(0, f)
    
    ns  = {} if ns  is None else ns
    hns = {} if hns is None else hns
    
    if header_carry:
        hns = header_carry | hns
    else:
        hns.setdefault("__builtins__", __builtins__ if ᐹ(__builtins__, ᖱ) else __builtins__.__dict__)
        hns.setdefault("__file__", header_f)
        hns.setdefault("__code_post_process__", 𝕂.get("code_post_process"))
        hns.setdefault("__code_cache_dir__", code_cache_dir)
        hns.setdefault("__gram_cache_dir__", gram_cache_dir)
        hns["__header_namespace__"] = hns
        hcode = '\n'.join(compiler("☾", R(f"{code_pfx}/{x}"), do_cache, **𝕂)
                            for x in R(header_f).split('\n') if x)
        run_inj_tb(hcode, hns)
        
    ns["__builtins__"] = { **ns.get("__builtins__", {}), **hns["__builtins__"], **hns }
    ns.setdefault("__name__", "__main__")
    ns.setdefault("__file__", fname)
    return lambda c, **𝕁: compiler("☾", c, do_cache, **𝕂|𝕁), ns

def basic_cpy_interactive_session(print_code=ⴴ, print_output=ⴴ, do_cache=ⴳ,
                                  sanity=ⴳ, interactive_defaults=ᗜ, **𝕂):
    if sanity and "code_post_process" not in 𝕂:
        𝕂["code_post_process"] = py_reparse
        𝕂["code_post_process"].ver = "basic_py_reparse"
    compiler, ns = basic_cpy_session(do_cache, **𝕂)
    def interactive(c, return_code=ⴴ, cap_stdout=ⴳ, dynamic_compile=ⴴ,
                    global_verbose_debug=ⴴ, force_exec=ⴴ,
                    output_printer=lambda *𝔸,**𝕂:print(*𝔸,**{"end":ᐦ}|𝕂), **𝕂):
        if global_verbose_debug:
            import dynamic_parser
            dynamic_parser.DEBUG = int(global_verbose_debug)
        
        𝐥 = c.split(ń)
        if not force_exec:
            while 𝐥 and not ⵐ(𝐥[0]): del 𝐥[0]
            if 𝐥 and (k := 𝐥[0].lstrip()) and (j := k[0]) == '':
                𝐥[0] = ᖇ(𝐥[0], j, ś, 1)
                force_exec = ⴳ
            while 𝐥 and not ⵐ(𝐥[0]): del 𝐥[0]
        s = min((ⵌ(l)-ⵌ(C) for l in 𝐥 if (C := l.lstrip())), default=0)
        c = ᒍ(ń, (l[s:] for l in 𝐥))
        
        (t1 := time(), code := compiler(c, **𝕂), t := time() - t1)
        print_code and print(f"Code ({t=}):\n{prettify_code(code)}")
        
        if return_code: return code
        
        mode = force_exec and "exec" or dynamic_compile and "dynamic" or "eval"
        𝑓 = lambda: run_inj_tb(code, ns, mode=mode)
        if cap_stdout: (r, ə), o = capture_output(𝑓)
        else         :  r,     o = 𝑓(), ᗜ
        
        if print_output and o is not ᗜ: output_printer(o)
        return r
    
    def run_w_impimp(c, *𝔸, **𝕂): # we love layering hacks
        NS = 𝕂.get("ns", ns)
        if imps := NS["__builtins__"]["get_implict_imports"](c):
            interactive(imps, *𝔸, **𝕂)
        return interactive(c, *𝔸, **𝕂)
    run_w_impimp.ns = ns
    
    if interactive_defaults: return lambda *𝔸,**𝕂:run_w_impimp(*𝔸, **interactive_defaults|𝕂)
    else                   : return run_w_impimp

def cpy_test(c, level=2, timing_test=ⴴ, exit=ⴴ, **𝕂):
    if timing_test: ENABLE_DEBUG()
    compiler = Compiler(CODE_CACHE_DIR, GRAM_CACHE_DIR)
    compiler.test("☾", c, debug_level=level,
                  test_timing=timing_test, **𝕂)
    if exit: exit_()
cpy_timing_test = lambda x, **𝕂: cpy_test(x, level=0, timing_test=ⴳ, **𝕂)
debug_test_exit = lambda x, **𝕂: cpy_test(x, exit=ⴳ, **𝕂)

def cpy_get_custom_func(t, d):
    def 𝑓(ns):
        if k := ns.get(t)             : return k
        if n := ns.get("__builtins__"): return n.get(t, d)
        return d
    return 𝑓

cpy_get_error_printer = cpy_get_custom_func("__error_printer__", print_ex)
cpy_get_highlighter = cpy_get_custom_func("__highlighter__", ID)

def run_custom_errors(𝑓, ns={}, quit=ⴴ):
    try:
        return 𝑓()
    except Exception as ε:
        cpy_get_error_printer(ns)(ε)
        if quit: exit(1)

def run_moon(𝔸, extract_interactive=ⴴ):
    𝔸_copy = 𝔸.copy()
    𝔸, 𝕂 = parse_sysargs(𝔸, c=0, verbose=0, debug=0, no_cache=0, sanity=1,
                         gram_test=0, get_dir=0,
                         code_cache_dir=(ᐦ, CODE_CACHE_DIR),
                         gram_cache_dir=(ᐦ, GRAM_CACHE_DIR))
    if 𝕂.debug    : print(f"{𝔸=}\n{𝕂=}")
    if 𝕂.get_dir  : print(moon_dir) and exit()
    if 𝕂.gram_test: cpy_test(' '.join(𝔸), exit=ⴳ)
    
    cpy_kwargs = {
        "ns": (ns := {}),
        "interactive_defaults": { "global_verbose_debug": 𝕂.verbose },
        "do_cache": not 𝕂.no_cache } | 𝕂
    
    if 𝔸 and not 𝕂.c:
        ns["__file__"] = f = os.path.abspath(𝔸[0])
        cpy = basic_cpy_interactive_session(**ᖱ(
                print_code   = ⴴ,
                print_output = ⴴ,
                do_cache     = ⴳ) | cpy_kwargs)
        
        sys.argv[:] = 𝔸 # jank?
        run_custom_errors(
            lambda: cpy(R(f), cap_stdout=ⴴ, force_exec=ⴳ),
            ns, quit=ⴳ)
        exit()
    
    try:
        import readline
        Path.exists(Path(HISTORY_FILE)) or W(HISTORY_FILE, ᐦ)
        readline.read_history_file(HISTORY_FILE)
    except Exception:
        readline = ⴴ
    fancy, swap_ln = (lambda x: f"\001\x1b[38;2;255;0;135m\002{x}\001\033[0m\002",
                      lambda x: f"\033[1A{x}\033[K") \
                        if readline else \
                     (lambda x: f"\x1b[38;2;255;0;135m{x}\033[0m", ID)
    pmt, ret = fancy('✝')+ś, fancy('⮡')+ś
    
    cpy_kwargs.setdefault("interactive_defaults", {})
    cpy_kwargs["interactive_defaults"] |= { "dynamic_compile": ⴳ }
    
    cpy = basic_cpy_interactive_session(**ᖱ(
          print_code   = 𝕂.debug,
          print_output = ⴳ) | cpy_kwargs)
    cpy.ns = ns;
    
    if 𝕂.c:
        r = cpy(ś.join(𝔸))
        r is not ᗜ and print(r)
        exit()
    
    def 𝑓(c):
        print(swap_ln(pmt + cpy_get_highlighter(ns)(c)))
        if not c:
            print("God is good!")
            return
        if readline:
            readline.append_history_file(1, HISTORY_FILE)
            if c == "☾":
                os.execv(sys.executable, (sys.executable, __file__, *𝔸))
            elif c == "clear":
                os.system("clear")
                return
        run_custom_errors(lambda: print(f"{ret}{cpy(c, cap_stdout=ⴴ)}"), ns)
    if extract_interactive: return 𝑓, cpy
    
    cc_count = 0
    while ⴳ:
        try:
            c = input(pmt)
            cc_count = 0
            𝑓(c)
        except KeyboardInterrupt:
            if not cc_count:
                print("\x1b[2K\rPress ^C again to exit.")
                cc_count += 1
                continue
            print()
            exit()

if __name__ == "__main__":
    run_moon(sys.argv[1:])

# cpy_test("""x¿a∧b¡y""", exit=ⴳ)
# cpy_test("""+𝔸ᵥ ¿𝔸ᵥ􊮝₀≅␀∨𝔸🃌≡1∨𝔸ᵥ􊮝₁≅␀¡ 𝔸₀+𝔸₁""", exit=ⴳ)
# cpy_test("""􊬲ₐaₐ􊬲""", exit=ⴳ)
# cpy_test("""\nx=⟦\n    A\n    B\n⟧\ny=⟦A\n   B⟧""".strip(), exit=ⴳ)
# debug_test_exit("""⥌𝕊,t↦𝕊ᵗ≔t""")
# debug_test_exit("""(20.2, .1323, a+.125)""")
# debug_test_exit("""(20.2, 1323, 0.125)""")
# debug_test_exit("""-⟥Σb""")
# debug_test_exit("""☾(‹A⟦B⟧C⟦D⟧E›)""")
# debug_test_exit("""⥌↦1""")
# debug_test_exit("""A ᴍᵃ𐞑ᵇ B""")
# debug_test_exit("""x""")
# debug_test_exit("""z = x+y""")
# debug_test_exit("""⥌x,z=␀,h=𝑎↦z+x""")