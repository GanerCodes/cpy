from util import *
from compiler.lang import Lang
import dynamic_parser
import os

CPY_DIR = Path(__file__).parent.parent
class Compiler:
    def __init__(𝕊, code_cache_dir, gram_cache_dir):
        𝕊.code_cache_dir = code_cache_dir
        𝕊.gram_cache_dir = gram_cache_dir
    
    def __call__(𝕊, lang_name, code, do_cache=ⴳ, code_post_process=ᗜ, **𝕂):
        ver1, code, ver2 = *𝕊.extract_version(code), ᐦ
        if code_post_process is not ᗜ:
            assert hasattr(code_post_process, "ver"), "Post processor version missing!"
            ver2 = ᔐ(code_post_process.ver)
        lang = 𝕊.get_lang(lang_name, ver1, do_cache)
        def load_lang(*𝔸):
            c = lang(code, **𝕂)
            return c if code_post_process is ᗜ else code_post_process(c)
        ℭ = FileCacher(do_cache and 𝕊.code_cache_dir, load_lang)
        return ℭ(code, lang_name, ver1, lang.id)
    
    def get_lang(𝕊, name, ver=ᐦ, do_cache=ⴳ, **𝕂):
        file = CPY_DIR / f"Languages/{name}{'-'*ᖲ(ver)+ver}" / "lang"
        assert file.exists(), f"Unable to find lang: {file}"
        return Lang(R(file), ver, do_cache and 𝕊.gram_cache_dir)

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