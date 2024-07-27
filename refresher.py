from util import *
from cpy_transpile import Compiler, CPY_DIR
from time import time, sleep
import subprocess, traceback

CACHE_DIR = GRAM_CACHE_DIR = "/tmp/cpy_cache"

# import peggle ; peggle.test_peggle() ; exit()

def capture_output(𝑓, *𝔸, **𝕂):
    from contextlib import redirect_stdout
    import io
    
    r = ᗜ
    with redirect_stdout(s := io.StringIO()):
        try                  : r = 𝑓(*𝔸, **𝕂)
        except Exception as e: print(traceback.format_exc())
    return r, s.getvalue()

def remember_code_for_tracebacks(path, code, *, funky_monkey={"monkeys": set()}):
    if "monke" not in funky_monkey:
        funky_monkey["monke"] = traceback.linecache.checkcache
        funky_monkey["monkeys"].add(path)
        def monkeymonkeymonkeymonkeymonkey(munkee=None):
            if munkee in funky_monkey["monkeys"]: return
            return funky_monkey["monke"](munkee)
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

def basic_cpy_session(do_cache=ⴳ, ns=ᗜ, hns=ᗜ, fname="cpy-interactive", **𝕂):
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    
    lang_pfx  = os.path.abspath(f"{CPY_DIR}/Languages/☾")
    header_fp = os.path.abspath(f"{lang_pfx}/Code/header.☾")
    lib_fp    = os.path.abspath(f"{lang_pfx}/Libraries")
    if lib_fp not in sys.path: sys.path.insert(0, lib_fp)
    
    hns = {} if hns is ᗜ else hns
    ns  = {} if ns  is ᗜ else ns
    
    hns.setdefault("__builtins__", __builtins__ if ᐹ(__builtins__, ᖱ) else __builtins__.__dict__)
    hns.setdefault("__file__", header_fp)
    run_inj_tb(compiler("☾", R(header_fp), do_cache, **𝕂), hns)
    
    ns["__builtins__"] = { **ns.get("__builtins__", {}), **hns["__builtins__"], **hns }
    ns.setdefault("__name__", "__main__")
    ns.setdefault("__file__", fname)
    return lambda c, **𝕁: compiler("☾", c, do_cache, **𝕂|𝕁), ns

def basic_cpy_interactive_session(print_code=ⴴ, print_output=ⴴ, do_cache=ⴳ,
                                  sanity=ⴳ, interactive_defaults=ᗜ, **𝕂):
    if sanity:
        import ast
        𝕂["code_post_process"] = lambda x: ast.unparse(ast.parse(x))
        𝕂["code_post_process"].ver = "basic_py_reparse"
    compiler, ns = basic_cpy_session(do_cache, **𝕂)
    def interactive(c, return_code=ⴴ, cap_stdout=ⴳ,
                    dynamic_compile=ⴴ, global_verbose_debug=ⴴ,
                    force_exec=ⴴ, **𝕂):
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
        s = min(ⵌ(l)-ⵌ(C) for l in 𝐥 if (C := l.lstrip()))
        c = ᒍ(ń, (l[s:] for l in 𝐥))
        
        (t1 := time(), code := compiler(c, **𝕂), t := time() - t1)
        print_code and print(f"Code ({t=}):\n{prettify_code(code)}")
        
        if return_code: return code
        
        mode = force_exec and "exec" or dynamic_compile and "dynamic" or "eval"
        𝑓 = lambda: run_inj_tb(code, ns, mode=mode)
        r, o = capture_output(𝑓) if cap_stdout else (𝑓(), ᗜ)
        
        print_output and o is not ᗜ and print(o)
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
cpy_timing_test = ρ(cpy_test, level=0, timing_test=ⴳ)
debug_test_exit = ρ(cpy_timing_test, exit=ⴳ)

def run_print_exception(f, *𝔸, **𝕂):
    try:
        return print(𝑓(*𝔸, **𝕂))
    except Exception:
        try:
            print(traceback.format_exc())
        except Exception as e:
            print(f'mfw Exception Exception: {e}')

if __name__ == "__main__":
    from sys import argv
    import readline
    
    # cpy_test("""\nx=⟦\n    A\n    B\n⟧\ny=⟦A\n   B⟧
    # """.strip(), exit=ⴳ)
    # debug_test_exit("""(20.2, .1323, a+.125)""")
    # debug_test_exit("""(20.2, 1323, 0.125)""")
    # debug_test_exit("""-⟥Σb""")
    # debug_test_exit("""☾(‹A⟦B⟧C⟦D⟧E›)""")
    # debug_test_exit("""⥌↦1""")
    # debug_test_exit("""A ᴍᵃ𐞑ᵇ B""")
    
    cpy_kwargs = { "interactive_defaults": { "global_verbose_debug": argv.count("--verbose") } }
    if "--refresher" in argv:
        def refresher(path, 𝑓):
            cur = ᐦ
            while ⴳ:
                if (r := R(path)) != cur:
                    𝑓(r)
                    cur = r
                sleep(1 / 15)
        
        cpy = basic_cpy_interactive_session(
                print_code   = ⴳ,
                print_output = ⴳ,
                do_cache     = ⴴ,
                sanity       = ⴴ,
                **cpy_kwargs)
        refresh = lambda c: run_print_exception(cpy, c)
        refresh_file = "/tmp/cpy_test/test.☾"
        if not os.path.isfile(refresh_file):
            os.makedirs(os.path.dirname(refresh_file), exist_ok=ⴳ)
            W(refresh_file, '☾‹Hello world!›')
        refresher(refresh_file, refresh)
        exit(0)
    
    if len(argv) > 1:
        cpy = basic_cpy_interactive_session(ⴴ, ⴴ, ⴳ,
            ns={ "__file__": (f := os.path.abspath(argv[1])) },
            **cpy_kwargs)
        sys.argv.pop(0)
        cpy(R(f), cap_stdout=ⴴ, force_exec=ⴳ)
        exit(0)
    
    cpy = basic_cpy_interactive_session(
                        print_code = "--debug" in argv,
                      print_output = ⴴ,
                   dynamic_compile = ⴳ,
                   **cpy_kwargs )
    while ⴳ:
        c = input("✝ ")
        print('»', end=ś)
        run_print_exception(cpy, c)