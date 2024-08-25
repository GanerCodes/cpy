from util import *
from compiler.lang import Lang
import dynamic_parser
import os

CPY_DIR = Path(__file__).parent.parent
class Compiler:
    def __init__(𝕊, cache_dir, gram_cache_dir):
        os.makedirs(cache_dir, exist_ok=ⴳ)
        os.makedirs(gram_cache_dir, exist_ok=ⴳ)
        𝕊.cache_dir = cache_dir
        𝕊.gram_cache_dir = gram_cache_dir
    
    def __call__(𝕊, lang_name, code, do_cache=ⴳ, code_post_process=ᗜ, **𝕂): # refactor?
        ver, code = 𝕊.extract_version(code)
        to_hash = ver + code
        if code_post_process is not ᗜ:
            assert hasattr(code_post_process, "ver"), "Post processor version missing!"
            to_hash = sha256(to_hash) + ᔐ(code_post_process.ver)
        if do_cache and os.path.isfile(cache := f"{𝕊.cache_dir}/{sha256(to_hash)}"):
            return R(cache)
        code = 𝕊.get_lang(lang_name, ver, do_cache)(code, **𝕂)
        if code_post_process is not ᗜ:
            code = code_post_process(code)
        return do_cache and W(cache, code) or code
    
    def get_lang(𝕊, name, ver=ᐦ, do_cache=ⴳ, **𝕂):
        if not os.path.isdir(folder := CPY_DIR / f"Languages/{name}{'-'*ᖲ(ver)+ver}"):
            raise Exception(f"Unable to find language folder {folder}")
        if not os.path.isfile(file := folder / "lang"):
            raise Exception(f"Unable to find lang file {file}")
        return Lang(R(file), ver, do_cache and 𝕊.gram_cache_dir or ᗜ)
        # I think this is scuffed, if you change the lang file it doesn't detect?

    def extract_version(𝕊, code, ver=ᐦ):
        if (C := code.lstrip()).startswith("❗"):
            ver, code = ⵉ(C, ń, 1)
            ver = ver.lstrip("❗").strip()
        return ver, code

    def test(𝕊, lang, code, debug_level=1, test_timing=ⴴ, **𝕂):
        import time, util, dynamic_parser
        
        qwrap = lambda 𝑊, 𝑓, *𝔸, **𝕂: 𝑊(𝑓, *𝔸, **𝕂) if 𝑊 else (𝑓(*𝔸, **𝕂), 0)
        𝑤 = lambda *𝔸, **𝕂: qwrap(test_timing and time_test, *𝔸, **𝕂)
        
        if debug_level > 0: util.ENABLE_DEBUG()
        if debug_level > 1: dynamic_parser.DEBUG = 1
        
        lang, tΔl = 𝑤(𝕊.get_lang, lang, do_cache=ⴴ)
        if test_timing: togprof()
        resl, tΔc = 𝑤(lang, code, **𝕂)
        if test_timing: togprof()
        
        print(f"CODE:\n{prettify_code(resl)}")
        if test_timing: print(f"\n{tΔl=} + {tΔc=} = {tΔl+tΔc}")