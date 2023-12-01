assert __name__ == "__main__", "This file is not meant to be imported!"

import argparse, shlex, os, re
from datetime import datetime
from functools import reduce
from itertools import groupby
from subprocess import Popen
from os import path as P

T,F = True, False
ñ,ƨ = '\n '

jop, spp, spx = P.join, P.split, P.splitext
cpy_dir = spp(__file__)[0]
cdr = lambda f: jop(cpy_dir, f)

cpy_bin = cdr("bin/cpy_binary")
import_dir = cdr("imports")

VERSION = "a"
TIME_SIG = datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
GENERAL_HEADER =  "from sys import path as __PATH; " \
                 f"__PATH.insert(0, '{import_dir.replace('\\', '/')}') ; " \
                  "del __PATH ; " \
                 f"from CPY_HEADER import * # CPY-{VERSION}-{TIME_SIG} \n"
QUIET_MODE = F
VERBOSE_MODE = F # enabled globally if relevent flag is present

log = lambda *a: QUIET_MODE or print("CPY -", *a)
debug = lambda *a: VERBOSE_MODE and print("Debug:", *a) 
dmp = lambda f,j=T: open(cdr(f) if j else f).read()
normalize = lambda t: t.strip().replace('␠', ƨ).replace('␤', ñ)
parse_mappings = lambda f,j=T,r=T: [list(map(normalize, y.split('␉'))) for x in (dmp(f,j) if r else f).replace('🝇',ñ).split(ñ) if ((y:=x.strip()) and y[0] not in '#;')]
gby = lambda a,f: {k:list(v) for k,v in groupby(sorted(a,key=f),f)}

DEFAULT_MAPPING_FILE = cdr("mappings/MAPPINGS_PY")
MAPPING_FUNCS = {
    "S": str.replace,
    "E": lambda t, f, r: t.replace(ñ+f, ñ+r+ƨ).replace(ƨ+f, ƨ+r+ƨ).replace(f, ƨ+r+ƨ),
    "R": lambda t, f, r: re.sub(f, r, t),
    "Y": lambda t, f, r: reduce(lambda x, y: str.replace(x, *y), zip(f, r), t) }

def reparse_code(code):
    import ast
    return ast.unparse(ast.parse(code))
def escape_code(code):
    t, r = iter(code), ''
    while T:
        try: c = next(t)
        except Exception: break
        
        if c == '␛':
            c += str(ord(next(t))).zfill(7)
        r += c
    return r
def unescape_code(code):
    t, r = iter(code), ''
    while T:
        try: c = next(t)
        except Exception: break
        
        if c == '␛':
            c = chr(int(''.join(next(t) for i in range(7))))
        r += c
    return r
def parse_macros(mappings, code):
    f = lambda x: (x.startswith("ₛ") and 's') or (x.startswith("ₑ") and 'e') or 'm'
    p = lambda x: parse_mappings(ñ.join(c[2:] for c in x), r=F)
    d = {'s':[],'m':[],'e':[]} | gby(code.split(ñ), f)
    debug(f"Macro count: {len(d['s'])}+{len(mappings)}+{len(d['e'])}")
    return p(d['s']) + mappings + p(d['e']), ñ.join(d['m'])
def compile_code(code, mappings, header="", reparse=F, **_):
    mappings, code = parse_macros(mappings, code)
    
    code = escape_code(ñ+code)
    for f, *a in mappings:
        code = MAPPING_FUNCS[f](code, *a)
    code = header + unescape_code(code)[1:]
    if reparse:
        code = reparse_code(code)
    return code
def understand_filename(f):
    b, e = spx(f)
    return b + (".py" if (e == ".cpy" or not e) else e)
def proc_file(f, mappings, out_ext=".py", no_header=F, no_write=F, **kwargs):
    b, e = spx(f)
    new_name = b+out_ext
    header = "" if no_header else GENERAL_HEADER
    code = compile_code(dmp(f, F), mappings, header=header, **kwargs)
    if no_write:
        return (new_name, code)
    with open(new_name, 'w') as o:
        debug(f'"{f}" → "{new_name}"')
        o.write(code)
    return new_name

PA = argparse.ArgumentParser(description="CPY Compiler.")
PA.add_argument("-d", "--directory", help="Directory of CPY project")
PA.add_argument("-n", "--no-recurse", action='store_true', help="Recurse into directory")
PA.add_argument("-c", "--cd-file", help="cd to file location to run instead of directory")
PA.add_argument("-r", "--reparse", action='store_true', help="Try and reparse the files into more normal python")
PA.add_argument("-s", "--stdout", action='store_true', help="Write to stdout rather than files")
PA.add_argument("-v", "--verbose", action='store_true', help="Output debug info")
PA.add_argument("-q", "--quiet", action='store_true', help="Suppress non-error messages")
PA.add_argument("--custom-ext", help='Override extension, format is "inExt"/"outExt"')
PA.add_argument("--custom-mappings", help="Use custom mapping file")
PA.add_argument("--no-header", action='store_true', help="Disable generation/import of header")
PA.add_argument("--no-cleanup", action='store_true', help="Disable removal of output files after execution")
PA.add_argument("--test", action='store_true', help="Run the cpy testing utility, ignores most other arguments")
PA.add_argument("file", nargs='?', help="File to run (if any)")
PA.add_argument('progargs', nargs=argparse.REMAINDER, help="Arguments to executable, eg. cpy_binary <file> <pyarg1> <pyarg2> … ")
A = PA.parse_args()

VERBOSE_MODE, QUIET_MODE = A.verbose, A.quiet

debug("Arguments:", A)

if A.test:
    A.directory = cdr("build+test")
    A.file = f"{A.directory}/tests.cpy"
    A.no_recurse = A.cd_file = T

if A.custom_ext:
    in_ext, out_ext = map(".{}".format, A.custom_ext.split('/', 1))
else:
    in_ext, out_ext = ".cpy", ".py"
debug(f"Got {in_ext=} {out_ext=}")

mappings = parse_mappings(A.custom_mappings or DEFAULT_MAPPING_FILE, F)
compiler_args = { "mappings": mappings, "out_ext": out_ext,
                  "reparse": A.reparse, "no_header": A.no_header,
                  "no_write": A.stdout }
debug(f"{compiler_args=}")

if not A.no_header:
    debug("Generating header")
    with open(jop(import_dir, "CPY_HEADER.py"), 'w') as f:
        f.write(
            compile_code(
                f"{dmp("header.cpy")}\n{dmp("combinators.cpy")}\n",
                **compiler_args))

if A.stdout:
    if not A.file:
        print("Cannot output to stdout without <file> argument.")
        exit(1)
    r = proc_file(A.file, **compiler_args)
    print(r[1], end='')
    exit()

D = P.realpath(A.directory or os.getcwd())

def file_filter(f): # open to future enhancements
    return "/.git/" not in f.replace(*'\\/') and spx(f)[1] == in_ext

files = filter(file_filter, 
    (jop(D, f) for f in os.listdir(D))
        if A.no_recurse else
    (jop(R, f) for R, _, fs in os.walk(D) for f in fs))
new_names = [proc_file(f, **compiler_args) for f in files]
debug(f"Generated files: {new_names}")

log(f"Generated {len(new_names)} files.")

if not A.file:
    exit() # No need to execute or cleanup

f = understand_filename(A.file)
if not P.isfile(f):
    print(f'Cannot locate file: "{f}"')
    exit(1)

debug(f'File to execute: "{f}"')
os.chdir(P.split(f)[0] if A.cd_file else D)

args = [cpy_bin, '-u', f, *A.progargs]
env = os.environ.copy()
env["PYTHONPATH"] = import_dir
env.pop("PYTHONHOME", None)

log(f'Running: "{shlex.join(args)}"')
Popen(args, env=env).wait()

if A.no_cleanup:
    exit()

for f in new_names:
    try:
        debug(f"Removing {f}")
        os.remove(f)
    except Exception:
        print(f'Failed to remove "{f}"')