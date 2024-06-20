from util import *
from cpy_compile import Compiler, CPY_DIR
from time import time, sleep
import subprocess

CACHE_DIR = GRAM_CACHE_DIR = "/tmp/cpy_cache"

import io
from contextlib import redirect_stdout
def capture_output(𝑓, *𝔸, **𝕂):
    with redirect_stdout(s := io.StringIO()):
        𝑓(*𝔸, **𝕂)
    return s.getvalue()

def refresher(path, 𝑓):
    cur = ""
    while True:
        if (r := R(path)) != cur:
            𝑓(r)
            cur = r
        sleep(1 / 15)

def basic_cpy_session(cache=ⴳ):
    compiler = Compiler(CACHE_DIR, GRAM_CACHE_DIR)
    header = R(f"{CPY_DIR}/languages/☾/code/header.☾")
    exec(compiler("☾", header, cache), ns:={})
    return lambda c: compiler("☾", c, cache), ns
def basic_cpy_interactive_session(print_code=ⴴ, cache=ⴳ):
    compiler, ns = basic_cpy_session(cache)
    def interactive(c, return_mode=ⴴ, return_code=ⴴ):
        # import dynamic_parser ; dynamic_parser.DEBUG = 1
        
        mode = "eval"
        if (C := c.lstrip(ś)) and ((j := C[0]) in ('󰊕', '')):
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
            return print_code and print(r) or r
        else:
            r = capture_output(exec, code, ns)
            return print_code and print(r) or r
    return interactive

if __name__ == "__main__":
    cpy = basic_cpy_interactive_session(ⴳ, ⴴ)
    def refresh(c):
        try:
            cpy(c)
        except Exception as e:
            import traceback
            print(traceback.format_exc())
    refresher("/tmp/cpy_test/test.☾", refresh)