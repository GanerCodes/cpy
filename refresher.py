from util import *
from cpy_transpile import Compiler, CPY_DIR
import subprocess, traceback

CACHE_DIR = GRAM_CACHE_DIR = "/tmp/cpy_cache"
HISTORY_FILE = "/tmp/cpy_cli.hist"

def capture_output(𝑓, *𝔸, **𝕂):
    from contextlib import redirect_stdout
    import io
    
    with redirect_stdout(s := io.StringIO()):
        try:
            return (𝑓(*𝔸, **𝕂), ⴳ), s.getvalue()
        except Exception as e:
            return (e, ⴴ), s.getvalue()+ń+traceback.format_exc()

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
        # traceback.linecache.getlines = lambda x, *A: monkemonEeamnoNEKEEE[path] if x in monkemonEeamnoNEKEEE else gl(x, *A)
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
    return (mode == "exec" and exec or eval)(compiled, ns)

def basic_cpy_session(do_cache=ⴳ, ns=ᗜ, hns=ᗜ, fname="cpy-interactive", header_carry=ᗜ, **𝕂):
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    
    lang_pfx = os.path.abspath(f"{CPY_DIR}/Languages/☾")
    code_pfx = os.path.abspath(f"{lang_pfx}/Code")
    libr_pfx = os.path.abspath(f"{lang_pfx}/Libraries")
    header_f = os.path.abspath(f"{code_pfx}/header.☾")
    for f in (code_pfx, libr_pfx):
        f in sys.path or sys.path.insert(0, f)
    
    ns  = {} if ns  is ᗜ else ns
    hns = {} if hns is ᗜ else hns
    
    if header_carry:
        hns = header_carry | hns
    else:
        hns.setdefault("__builtins__", __builtins__ if ᐹ(__builtins__, ᖱ) else __builtins__.__dict__)
        hns.setdefault("__file__", header_f)
        run_inj_tb(compiler("☾", R(header_f), do_cache, **𝕂), hns)
        hns["__header_namespace__"] = hns
    
    ns["__builtins__"] = { **ns.get("__builtins__", {}), **hns["__builtins__"], **hns }
    ns.setdefault("__name__", "__main__")
    ns.setdefault("__file__", fname)
    return lambda c, **𝕁: compiler("☾", c, do_cache, **𝕂|𝕁), ns

def py_reparse(x):
    import ast
    try:
        return ast.unparse(ast.parse(x))
    except Exception as e:
        raise Exception(f'Failed to reparse code! "{e}"\nCode:\n{x}')

def basic_cpy_interactive_session(print_code=ⴴ, print_output=ⴴ, do_cache=ⴳ,
                                  sanity=ⴳ, interactive_defaults=ᗜ, **𝕂):
    if sanity:
        𝕂["code_post_process"] = py_reparse
        𝕂["code_post_process"].ver = "basic_py_reparse"
    compiler, ns = basic_cpy_session(do_cache, **𝕂)
    def interactive(c, return_code=ⴴ, cap_stdout=ⴳ,
                    dynamic_compile=ⴴ, global_verbose_debug=ⴴ,
                    force_exec=ⴴ, output_printer=print, **𝕂):
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
        if cap_stdout:
            (r, ə), o = capture_output(𝑓)
        else:
            r, o = 𝑓(), ᗜ
        
        if print_output and o is not ᗜ: output_printer(o)
        return r
    interactive.ns = ns
    if interactive_defaults:
        return lambda *𝔸,**𝕂:interactive(*𝔸, **interactive_defaults|𝕂)
    else:
        return interactive

def cpy_test(c, level=2, timing_test=ⴴ, exit=ⴴ, **𝕂):
    if timing_test: ENABLE_DEBUG()
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    compiler.test("☾", c, debug_level=level,
                  test_timing=timing_test, **𝕂)
    if exit: exit_()
cpy_timing_test = lambda x, **𝕂: cpy_test(x, level=0, timing_test=ⴳ, **𝕂)
debug_test_exit = lambda x, **𝕂: cpy_test(x, exit=ⴳ, **𝕂)

def run_print_exception(𝑓, *𝔸, **𝕂):
    try:
        return print(𝑓(*𝔸, **𝕂))
    except Exception:
        try:
            print(traceback.format_exc())
        except Exception as e:
            print(f'mfw Exception Exception: {e}')

def cpy_get_custom_func(t, d):
    def 𝑓(ns):
        if t in ns["__builtins__"]:
            return ns["__builtins__"][t]
        return d
    return 𝑓

cpy_get_error_printer = cpy_get_custom_func("__error_printer__", RAISE)
cpy_get_highlighter = cpy_get_custom_func("__highlighter__", ID)

def run_custom_errors(𝑓, ns={}, quit=ⴴ):
    try:
        return 𝑓()
    except Exception as ε:
        cpy_get_error_printer(ns)(ε)
        quit and exit(1)

def run_moon(args, extract_interactive=ⴴ):
    # cpy_test("""󰆴 factorial, e, pi, tau, sqrt, cbrt""", exit=ⴳ)
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
    
    try:
        import readline
        Path.exists(Path(HISTORY_FILE)) or W(HISTORY_FILE, ᐦ)
        readline.read_history_file(HISTORY_FILE)
    except Exception:
        readline = ⴴ
    
    agets = lambda x: (args.count(x := "--"+x), y:=[t for t in args if t != x], args.clear(), args.extend(y))[0]
    
    cpy_kwargs = { "interactive_defaults": { "global_verbose_debug": agets("verbose") } }
    if agets("no-cache"): cpy_kwargs["do_cache"] = ⴴ
    
    if agets("refresher"):
        def refresher(path, 𝑓):
            cur = ᐦ
            while ⴳ:
                if (r := R(path)) != cur:
                    𝑓(r)
                    cur = r
                sleep(1 / 15)
        
        cpy = basic_cpy_interactive_session(**ᖱ(
                print_code   = ⴳ,
                print_output = ⴳ,
                do_cache     = ⴴ,
                sanity       = ⴴ) | cpy_kwargs)
        refresh = lambda c: run_print_exception(cpy, c)
        refresh_file = "/tmp/cpy_test/test.☾"
        if not os.path.isfile(refresh_file):
            os.makedirs(os.path.dirname(refresh_file), exist_ok=ⴳ)
            W(refresh_file, '☾‹Hello world!›')
        refresher(refresh_file, refresh)
        exit(0)
    
    arg_debug = agets("debug")
    ns = {}
    
    if len(args):
        ns = { "__file__": (f := os.path.abspath(args[0])) }
        cpy = basic_cpy_interactive_session(**ᖱ(
                print_code   = ⴴ,
                print_output = ⴴ,
                do_cache     = ⴳ,
                ns           = ns) | cpy_kwargs)
        
        sys.argv[:] = args # jank?
        run_custom_errors(
            lambda: cpy(R(f), cap_stdout=ⴴ, force_exec=ⴳ),
            ns, quit=ⴳ)
        exit(0)
    
    cpy_kwargs.setdefault("interactive_defaults", {})
    cpy_kwargs["interactive_defaults"] |= { "dynamic_compile": ⴳ }
    cpy = basic_cpy_interactive_session(**ᖱ(
          print_code   = arg_debug,
          print_output = ⴳ,
          ns           = ns) | cpy_kwargs)
    if readline:
        s,e = "\001\002"
        swap_ln = lambda x: f"\033[1A{x}\033[K"
    else:
        s = e = ᐦ
        swap_ln = lambda x: x
    fancy = lambda x: f"{s}\x1b[38;2;255;0;135m{e}{x}{s}\033[0m{e}"
    prompt = fancy('✝') + ś
    cc_count = 0
    
    def 𝑓(c):
        print(swap_ln(prompt + cpy_get_highlighter(ns)(c)))
        if not c:
            print("God is good!")
            return
        if readline:
            readline.append_history_file(1, HISTORY_FILE)
            if c == "☾":
                os.execv(sys.executable, (sys.executable, __file__))
        run_custom_errors(lambda: print(f"{fancy('⮡')} {cpy(c, cap_stdout=ⴴ)}"), ns)
    if extract_interactive:
        return 𝑓
    
    while ⴳ:
        try:
            c = input(prompt)
            cc_count = 0
            𝑓(c)
        except KeyboardInterrupt:
            if not cc_count:
                print("\x1b[2K\rPress ^C again to exit.")
                cc_count += 1
                continue
            print()
            exit(0)

if __name__ == "__main__":
    run_moon(sys.argv[1:])