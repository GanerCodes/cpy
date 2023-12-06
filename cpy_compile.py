assert __name__ == "__main__", "This file is not meant to be imported!"

import argparse, shlex, os, re
from datetime import datetime
from functools import reduce
from itertools import groupby
from subprocess import Popen
from os import path as P

T,F = True, False
ñ,ƨ = '\n '

jop, psp, pse = P.join, P.split, P.splitext
pdr = lambda f: psp(f)[0]
cpy_dir = psp(__file__)[0]
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

log = lambda *a: QUIET_MODE or print("cpy -", *a)
debug = lambda *a: VERBOSE_MODE and print("cpy-debug -", *a)
error = lambda *a: print("cpy-ERROR -", *a)
dmp = lambda f,j=T: open(cdr(f) if j else f).read()
normalize = lambda t: t.strip().replace('␠', ƨ).replace('␤', ñ)
parse_map_syntax = lambda f,j=T,r=T: [list(map(normalize, y.split('␉'))) for x in (dmp(f,j) if r else f).replace('🝇',ñ).split(ñ) if ((y:=x.strip()) and y[0] not in '#;')]
gby = lambda a,f: {k:list(v) for k,v in groupby(sorted(a,key=f),f)}

DEFAULT_MAPPING = "PY"
MAPPING_FUNCS = {
    "I": None,
    "S": str.replace,
    "E": lambda t, f, r: t.replace(ñ+f, ñ+r+ƨ).replace(ƨ+f, ƨ+r+ƨ).replace(f, ƨ+r+ƨ),
    "R": lambda t, f, r: re.sub(f, r, t),
    "Y": lambda t, f, r: reduce(lambda x, y: str.replace(x, *y), zip(f, r), t) }

def cmd(args, env=None):
    log(f'Running: "{shlex.join(args)}"')
    (proc := Popen(args, env=env)).wait()
    return proc.returncode

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

def search_map_filepath(f, file_dir):
    F = f
    if not P.isabs(f):
        f = P.abspath(jop(file_dir, f))
        debug("Trying mapping file", f)
    if P.isfile(f): return f
    
    f = P.abspath(cdr(jop("mappings/", F)))
    debug("Trying mapping file", f)
    if P.isfile(f): return f
    
    error("Unable to find mapping file", f)
    exit(1)

def parse_implicit_filename(f, in_ext, out_ext):
    b, e = pse(f)
    return b + (out_ext if (e == in_ext or not e) else e)

def parse_macros(mappings, code):
    f = lambda x: (x.startswith("ₛ") and 's') or (x.startswith("ₑ") and 'e') or 'm'
    p = lambda x: parse_map_syntax(ñ.join(c[2:] for c in x), r=F)
    d = {'s':[],'m':[],'e':[]} | gby(code.split(ñ), f)
    debug(f"Macro count: {len(d['s'])}+{len(mappings)}+{len(d['e'])}")
    return p(d['s']) + mappings + p(d['e']), ñ.join(d['m'])

def parse_nesting_mappings(mappings, file_dir):
    new_mappings = []
    for m in mappings:
        𝑓, *a = m
        if 𝑓 != "I":
            new_mappings.append(m)
            continue
        
        f = search_map_filepath(a[0], file_dir)
        
        if '' in (t := open(f).read()):
            maps, _ = parse_macros([], t)
        else:
            maps = parse_map_syntax(t, F, F)
            
        new_mappings += parse_nesting_mappings(maps, pdr(f))
    return new_mappings

def compile_code(code, mappings, header="", reparse=F, file_dir=None, **_):
    mappings, code = parse_macros(mappings, code)
    mappings = parse_nesting_mappings(mappings, file_dir)
    code = escape_code(ñ+code)
    for f, *a in mappings:
        code = MAPPING_FUNCS[f](code, *a)
    code = header + unescape_code(code)[1:]
    if reparse:
        code = reparse_code(code)
    return code
def proc_file(f, mappings, out_ext=".py", no_header=F, no_write=F, **kwargs):
    b, e = pse(f)
    new_name = b+out_ext
    header = "" if no_header else GENERAL_HEADER
    code = compile_code(dmp(f, F), mappings, header=header, file_dir=pdr(f), **kwargs)
    if no_write:
        return (new_name, code)
    with open(new_name, 'w') as o:
        debug(f'"{f}" → "{new_name}"')
        o.write(code)
    return new_name

PA = argparse.ArgumentParser(prog="cpy", description="The cpy Compiler.")
PA.add_argument("-d", "--directory", help="Directory of cpy project")
PA.add_argument("-n", "--no-recurse", action='store_true', help="Recurse into directory")
PA.add_argument("-c", "--cd-file", help="cd to file location to run instead of directory")
PA.add_argument("-p", "--pip", nargs=argparse.REMAINDER, help="Pip tool")
PA.add_argument("-q", "--quiet", action='store_true', help="Suppress non-error messages")
PA.add_argument("-r", "--reparse", action='store_true', help="Try and reparse the files into more normal python")
PA.add_argument("-s", "--stdout", action='store_true', help="Write to stdout rather than files")
PA.add_argument("-v", "--verbose", action='store_true', help="Output debug info")
PA.add_argument("-m", "--custom-mappings", action='append', help="Use custom mapping file")
PA.add_argument("-t", "--steal-macros", action='append', help='Copy macros from another file')
PA.add_argument("--custom-ext", help='Override extension, format is "inExt"/"outExt"')
PA.add_argument("--no-header", action='store_true', help="Disable generation/import of header")
PA.add_argument("--no-cleanup", action='store_true', help="Disable removal of output files after execution")
PA.add_argument("--test", action='store_true', help="Run the cpy testing utility, ignores most other arguments")
PA.add_argument("--build-cpy", action='store_true', help="Build the cpy python binary [requires bash/gcc/etc]")
PA.add_argument("--build-codium", action='store_true', help="Build/install codium highlighting [requires bash/npm/etc]")
PA.add_argument("file", nargs='?', help="File to run (if any)")
PA.add_argument('progargs', nargs=argparse.REMAINDER, help="Arguments to executable, eg. cpy_binary <file> <pyarg1> <pyarg2> … ")
A = PA.parse_args()

if A.test: A.verbose = T
VERBOSE_MODE, QUIET_MODE = A.verbose, A.quiet

debug("Arguments:", A)

if A.build_cpy:
    if (r:=cmd(["bash", cdr("build+test/build.sh")])) != 0:
        error("Failed to build cpy!")
        exit(r)
    log("Built cpy!")

if A.build_codium:
    if (r:=cmd(["bash", cdr("cpy-codium-highlighter/build.sh")])) != 0:
        error("Failed to build Codium syntax highlighter!")
        exit(r)
    log("Built Codium syntax highlighter!")

if (A.build_cpy and A.test) or (A.build_codium and not A.test):
    exit(0)

if A.test:
    A.directory = cdr("build+test")
    A.file = f"{A.directory}/tests.cpy"
    A.no_recurse = A.cd_file = T

if A.pip:
    debug("Using Pip mode")
    args = [cpy_bin, "-m", "pip"]
    if len(A.pip) == 1 and A.pip[0].endswith('.txt'):
        args += ["install", "-r", A.pip[0]]
    else:
        args += A.pip
    exit(cmd(args))

cur_dir = os.getcwd()
D = P.realpath(A.directory or cur_dir)

if A.custom_ext:
    in_ext, out_ext = map(".{}".format, A.custom_ext.split('/', 1))
else:
    in_ext, out_ext = ".cpy", ".py"
debug(f"Got {in_ext=} {out_ext=}")

mappings = []

macro_files = A.steal_macros if A.steal_macros else []
debug("Macro files:", macro_files)
for f in macro_files:
    mappings, _ = parse_macros(mappings, open(f).read())

mapping_files = A.custom_mappings if A.custom_mappings else [DEFAULT_MAPPING]
debug("Mapping files:", mapping_files)
for f in mapping_files:
    mappings += parse_map_syntax(
        search_map_filepath(f, cur_dir), F)

compiler_args = { "mappings": mappings, "out_ext": out_ext,
                  "reparse": A.reparse, "no_header": A.no_header,
                  "no_write": A.stdout }
debug(f"{compiler_args=}")

if not A.no_header:
    debug("Generating header")
    header = compile_code(
        ñ.join(map(dmp, ["header.cpy", "combinators.cpy"])),
        file_dir=D, **compiler_args)
    if A.stdout:
        print(header)
        exit(0)
    else:
        with open(jop(import_dir, "CPY_HEADER.py"), 'w') as f:
            f.write(header)

if A.stdout:
    if not A.file:
        error("Cannot output to stdout with '--no-header' and without <file>.")
        exit(1)
    r = proc_file(A.file, **compiler_args)
    print(r[1], end='')
    exit()

def file_filter(f): # open to future enhancements
    return "/.git/" not in f.replace(*'\\/') and pse(f)[1] == in_ext

files = filter(file_filter, 
    (jop(D, f) for f in os.listdir(D))
        if A.no_recurse else
    (jop(R, f) for R, _, fs in os.walk(D) for f in fs))
new_names = [proc_file(f, **compiler_args) for f in files]
debug(f"Generated files: {new_names}")

log(f"Generated {len(new_names)} files(s)"+(" ◕‿◕ 🩷" if ((h:='rllyawesome') in (env := os.environ.copy())) else env.__setitem__(h,h) or '.'))

if not A.file:
    exit() # No need to execute or cleanup

f = parse_implicit_filename(A.file, in_ext, out_ext)
if not P.isfile(f):
    error(f'Cannot locate file: "{f}"')
    exit(1)

debug(f'File to execute: "{f}"')
os.chdir(pdr(f) if A.cd_file else D)

args = [cpy_bin, '-u', f, *A.progargs]
env["PYTHONPATH"] = import_dir
env.pop("PYTHONHOME", None)
try:
    exit_code = cmd(args, env)
except KeyboardInterrupt:
    exit_code = 1 # jank?

if A.no_cleanup:
    exit(exit_code)

for f in new_names:
    try:
        debug(f"Removing {f}")
        os.remove(f)
    except Exception:
        error(f'Failed to remove "{f}"')

exit(exit_code)

# goodbyenight