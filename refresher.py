from util import *
from cpy_compile import Compiler, CPY_DIR
from time import time, sleep
import subprocess

CACHE_DIR = GRAM_CACHE_DIR = "/tmp/cpy_cache"

# import peggle ; peggle.test_peggle() ; exit()

import io, traceback
from contextlib import redirect_stdout
def capture_output(𝑓, *𝔸, **𝕂):
    with redirect_stdout(s := io.StringIO()):
        try:
            𝑓(*𝔸, **𝕂)
        except Exception as e:
            print(traceback.format_exc())
    return s.getvalue()

def refresher(path, 𝑓):
    cur = ""
    while True:
        if (r := R(path)) != cur:
            𝑓(r)
            cur = r
        sleep(1 / 15)

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

def exec_with_tb(code, ns, file=ᗜ):
    if file is ᗜ: file = ns.get("__file__", "cpy-interactive")
    compiled = compile(code, file, "exec")
    remember_code_for_tracebacks(file, code)
    return exec(compiled, ns)

def basic_cpy_session(cache=ⴳ, ns=ᗜ, hns=ᗜ, fname="cpy-interactive", **𝕂):
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    
    lang_pfx  = os.path.abspath(f"{CPY_DIR}/Languages/☾")
    header_fp = os.path.abspath(f"{lang_pfx}/Code/header.☾")
    lib_fp    = os.path.abspath(f"{lang_pfx}/Libraries")
    if lib_fp not in sys.path: sys.path.insert(0, lib_fp)
    
    header = R(header_fp)
    hns = {} if hns is ᗜ else hns
    hns.setdefault("__builtins__", __builtins__ if ᐹ(__builtins__, ᖱ) else __builtins__.__dict__)
    hns.setdefault("__file__", header_fp)
    header_py = compiler("☾", header, cache, **𝕂)
    exec_with_tb(header_py, hns)
    ns = {} if ns is ᗜ else ns
    ns["__builtins__"] = ns.get("__builtins__", {}) | hns["__builtins__"] | hns
    ns.setdefault("__name__", "__main__")
    ns.setdefault("__file__", fname)
    return lambda c, **𝕁: compiler("☾", c, cache, **𝕂|𝕁), ns

def basic_cpy_interactive_session(print_code=ⴴ, cache=ⴳ, sanity=ⴳ, interactive_defaults=ᗜ, **𝕂):
    if sanity:
        import ast
        𝕂["code_post_process"] = lambda x: ast.unparse(ast.parse(x))
        𝕂["code_post_process"].ver = "basic_py_reparse"
    compiler, ns = basic_cpy_session(cache, **𝕂)
    def interactive(c, return_mode=ⴴ, return_code=ⴴ, cap_stdout=ⴳ, **𝕂):
        # import dynamic_parser ; dynamic_parser.DEBUG = 1
        
        mode = "eval"
        if (C := c.lstrip(ś)) and ((j := C[0]) in "󰊕"):
            mode, c = "exec", c.replace(j, ś, 1)
        
        lns = c.split(ń)
        s = min(ⵌ(l)-ⵌ(C) for l in lns if (C := l.lstrip(ś)))
        c = ᒍ(ń, (l[s:] for l in lns))
        
        (t1 := time(), code := compiler(c, **𝕂), t := time() - t1)
        print_code and print(f"Code ({t=}):\n{prettify_code(code)}")
        
        if return_code or return_mode:
            if return_code and return_mode:
                return mode, code
            elif return_mode:
                return mode
            elif return_code:
                return code
        
        if mode == "eval":
            r = eval(code, ns)
        else:
            r = capture_output(exec_with_tb, code, ns) if cap_stdout else exec_with_tb(code, ns)
        
        print_code and print(r)
        return r
    interactive.ns = ns
    if interactive_defaults:
        return lambda *𝔸,**𝕂:interactive(*𝔸, **interactive_defaults|𝕂)
    else:
        return interactive

def cpy_timing_test(c, **𝕂):
    ENABLE_DEBUG()
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    compiler.test_timing("☾", c, **𝕂)

def debug_test_exit(code):
    cpy_timing_test(code, debug_level=2) ; exit()

if __name__ == "__main__":
    import traceback
    from sys import argv
    if len(argv) > 1:
        cpy = basic_cpy_interactive_session(ⴴ, ⴳ, ns={ "__file__": (f := os.path.abspath(argv[1])) })
        sys.argv.pop(0)
        cpy(''+R(f), cap_stdout=ⴴ)
        exit(0)
    
    # debug_test_exit("""(20.2, .1323, a+.125)""")
    # debug_test_exit("""(20.2, 1323, 0.125)""")
    # debug_test_exit("""-⟥Σb""")
    # debug_test_exit("""☾(‹A⟦B⟧C⟦D⟧E›)""")
    # debug_test_exit("""⥌↦1""")
    # debug_test_exit("""A ᴍᵃ𐞑ᵇ B""")
    
    cpy = basic_cpy_interactive_session(ⴳ, ⴴ, sanity=ⴴ)
    def refresh(c):
        try:
            cpy(c)
        except Exception:
            try:
                print(traceback.format_exc())
            except Exception as e:
                print(f'mfw Exception Exception: {e}')
    refresh_file = "/tmp/cpy_test/test.☾"
    if not os.path.isfile(refresh_file):
        os.makedirs(os.path.dirname(refresh_file), exist_ok=ⴳ)
        W(refresh_file, ' ☾‹Hello world!›')
    refresher(refresh_file, refresh)