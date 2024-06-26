from util import *
from cpy_compile import Compiler, CPY_DIR
from time import time, sleep
import subprocess

CACHE_DIR = GRAM_CACHE_DIR = "/tmp/cpy_cache"

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

def cpy_timing_test(c, **𝕂):
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    compiler.test_timing("☾", c, **𝕂)

def basic_cpy_session(cache=ⴳ, ns=ᗜ, hns=ᗜ):
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    
    lang_pfx = f"{CPY_DIR}/languages/☾"
    header_fp = f"{lang_pfx}/code/header.☾"
    lib_fp = f"{lang_pfx}/libraries"
    
    header = R(header_fp)
    hns = {} if hns is ᗜ else hns
    hns.setdefault("__builtins__", __builtins__ if ᐹ(__builtins__, ᖱ) else __builtins__.__dict__)
    hns.setdefault("__file__", header_fp)
    
    lib_fp in sys.path or sys.path.insert(0, lib_fp)
    
    exec(compiler("☾", header, cache), hns)
    ns = {} if ns is ᗜ else ns
    ns["__builtins__"] = ns.get("__builtins__", {}) | hns["__builtins__"] | hns
    ns.setdefault("__name__", "__main__")
    ns.setdefault("__file__", ᗜ)
    return lambda c: compiler("☾", c, cache), ns

def basic_cpy_interactive_session(print_code=ⴴ, cache=ⴳ, **𝕂):
    compiler, ns = basic_cpy_session(cache, **𝕂)
    def interactive(c, return_mode=ⴴ, return_code=ⴴ, cap_stdout=ⴳ):
        # import dynamic_parser ; dynamic_parser.DEBUG = 1
        
        mode = "eval"
        if (C := c.lstrip(ś)) and ((j := C[0]) in "󰊕"):
            mode, c = "exec", c.replace(j, ś, 1)
        
        lns = c.split(ń)
        s = min(ⵌ(l)-ⵌ(C) for l in lns if (C := l.lstrip(ś)))
        c = ᒍ(ń, (l[s:] for l in lns))
        
        (t1 := time(), code := compiler(c), t := time() - t1)
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
            r = capture_output(exec, code, ns) if cap_stdout else exec(code, ns)
        
        print_code and print(r)
        return r
    interactive.ns = ns
    return interactive

# cpy_timing_test('☾(‹A⟦B⟧C⟦D⟧E›)', debug_level=2) ; exit()

if __name__ == "__main__":
    import traceback
    from sys import argv
    if len(argv) > 1:
        cpy = basic_cpy_interactive_session(ⴴ, ⴳ, ns={ "__file__": (f := argv[1]) })
        cpy(''+R(f), cap_stdout=ⴴ)
        exit(0)
    
    cpy = basic_cpy_interactive_session(ⴳ, ⴴ)
    def refresh(c):
        try:
            cpy(c)
        except Exception:
            try:
                print(traceback.format_exc())
            except Exception as e:
                print(f'mfw Exception Exception: {e}')
    refresher("/tmp/cpy_test/test.☾", refresh)