from util import *
from compiler.lang import Lang
import dynamic_parser
import os

CPY_DIR = os.path.dirname(os.path.abspath(__file__))
class Compiler:
    def __init__(𝕊, cache_dir, gram_cache_dir):
        os.makedirs(cache_dir, exist_ok=ⴳ)
        os.makedirs(gram_cache_dir, exist_ok=ⴳ)
        𝕊.cache_dir = cache_dir
        𝕊.gram_cache_dir = gram_cache_dir
    
    def __call__(𝕊, lang_name, code, use_cache=ⴳ, **K): # refactor?
        ver, code = 𝕊.extract_version(code)
        if use_cache and os.path.isfile(cache := f"{𝕊.cache_dir}/{sha256(ver + code)}"):
            return R(cache)
        code = 𝕊.get_lang(lang_name, ver, use_cache)(code, **K)
        return use_cache and W(cache, code) or code
    
    def get_lang(𝕊, name, ver=ᐦ, use_cache=ⴳ, **K):
        if not os.path.isdir(folder := f"{CPY_DIR}/languages/{name}{'-'*ᖲ(ver)+ver}"):
            raise Exception(f"Unable to find language folder {folder}")
        if not os.path.isfile(file := f"{folder}/lang"):
            raise Exception(f"Unable to find lang file {file}")
        return Lang(R(file), ver, use_cache and 𝕊.gram_cache_dir or ᗜ)
        # I think this is scuffed, if you change the lang file it doesn't detect?

    def extract_version(𝕊, code, ver=ᐦ):
        if (C := code.lstrip()).startswith("❗"):
            ver, code = ⵉ(C, ń, 1)
            ver = ver.lstrip("❗").strip()
        return ver, code

    def test_timing(𝕊, lang, code, debug_level=1, **K):
        import time, util, dynamic_parser
        
        if debug_level > 0: util.ENABLE_DEBUG()
        if debug_level > 1: dynamic_parser.DEBUG = 1
        
        tI = time.time()
        lang = 𝕊.get_lang(lang, use_cache=ⴴ)
        tΔl = time.time() - tI
        
        togprof()
        tI = time.time()
        result = lang(code, **K)
        tΔc = time.time() - tI
        togprof()
        
        print(f"CODE:\n{prettify_code(result)}\n\n{tΔl=} + {tΔc=} = {tΔl+tΔc}")