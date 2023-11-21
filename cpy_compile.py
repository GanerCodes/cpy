import argparse, shlex, os, re
from datetime import datetime
from functools import reduce
from os import path as P

T,F = True, False
ñ,ƨ = '\n '
cpy_bin = P.join(
    cpy_dir := P.split(__file__)[0],
    "bin/cpy_binary")
import_dir = P.join(cpy_dir, "imports")

VERSION = "a"
TIME_SIG = datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
GENERAL_HEADER =  "from sys import path as __PATH; " \
                 f"__PATH.insert(0, '{import_dir.replace('\\', '/')}') ; " \
                  "del __PATH ; " \
                 f"from CPY_HEADER import * # CPY-{VERSION}-{TIME_SIG} \n"

dmp = lambda f, j=T: open(P.join(cpy_dir, f) if j else f).read()
normalize = lambda t: t.strip().replace('␠', ƨ).replace('␤', ñ)
parse_mappings = lambda f,j=T: [list(map(normalize, y.split('␉'))) for x in dmp(f, j).split(ñ) if ((y:=x.strip()) and y[0] not in '#;')]

DEFAULT_MAPPINGS = parse_mappings("MAPPINGS")
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
def compile_code(code, mappings, header="", reparse=F, **_):
    code = ñ+code
    code = escape_code(code)
    for f, *a in mappings:
        code = MAPPING_FUNCS[f](code, *a)
    code = header + unescape_code(code)[1:]
    if reparse:
        code = reparse_code(code)
    return code
def understand_filename(f):
    b, e = P.splitext(f)
    return b + (".py" if (e == ".cpy" or not e) else e)
def proc_file(f, mappings, out_ext=".py", no_header=F, no_write=F, **kwargs):
    b, e = P.splitext(f)
    new_name = b+out_ext
    header = "" if no_header else GENERAL_HEADER
    code = compile_code(dmp(f, F), mappings, header=header, **kwargs)
    if no_write:
        return (new_name, code)
    with open(new_name, 'w') as f:
        f.write(code)
    return new_name

if __name__ == "__main__":
    PA = argparse.ArgumentParser(description="CPY Compiler.")
    PA.add_argument("-d", "--directory", help="Directory of CPY project")
    PA.add_argument("-n", "--no-recurse", action='store_true', help="Recurse into directory")
    PA.add_argument("-c", "--cd-file", help="cd to file location to run instead of directory")
    PA.add_argument("-r", "--reparse", action='store_true', help="try and reparse the files into more normal python")
    PA.add_argument("-s", "--stdout", action='store_true', help="write to stdout rather than files")
    PA.add_argument("--custom-ext", help='override extension; format is "inExt"/"outExt"')
    PA.add_argument("--custom-mappings", help="custom mapping file")
    PA.add_argument("--no-header", action='store_true', help="disable generation/import of header")
    PA.add_argument("--test", action='store_true', help="run the cpy testing utility, ignores most other arguments")
    PA.add_argument("file", nargs='?', help="File to run (if any)")
    PA.add_argument('progargs', nargs=argparse.REMAINDER, help="Arguments to pass, eg. cpy_binary <file> <pyarg1> <pyarg2> … ")
    A = PA.parse_args()
    
    if A.test:
        A.directory = f"{cpy_dir}/build+test"
        A.file = f"{A.directory}/tests.cpy"
        A.no_recurse = T
        A.cd_file = T

    if A.custom_ext:
        in_ext, out_ext = map(".{}".format, A.custom_ext.split('/', 1))
    else:
        in_ext, out_ext = ".cpy", ".py"

    mappings = parse_mappings(A.custom_mappings, F) if A.custom_mappings else DEFAULT_MAPPINGS
    compiler_args = { "mappings": mappings, "out_ext": out_ext,
                      "reparse": A.reparse, "no_header": A.no_header,
                      "no_write": A.stdout }
    
    if not A.no_header:
        with open(P.join(import_dir, "CPY_HEADER.py"), 'w') as f:
            f.write(
                compile_code(
                    f"{dmp("header.cpy")}\n{dmp("combinators.cpy")}\n",
                    **compiler_args))

    if A.stdout:
        r = proc_file(A.file, **compiler_args)
        print(r[1], end='')
        exit()
    
    D = A.directory or os.getcwd()
    
    files = [f for f in (
        (P.join(D, f) for f in os.listdir(D))
            if A.no_recurse else
        (P.join(R, f) for R, _, fs in os.walk(D) for f in fs)
    ) if "/.git/" not in f.replace(*'\\/') and P.splitext(f)[1] == in_ext]
    new_names = [print(f, '→', r:=proc_file(f, **compiler_args)) or r for f in files]
    
    if f := A.file:
        f = understand_filename(f)
        os.chdir(P.split(f)[0] if A.cd_file else D)
        
        args = [cpy_bin, '-u', f, *A.progargs]
        env = os.environ.copy()
        env["PYTHONPATH"] = import_dir
        env.pop("PYTHONHOME", None)
        
        print(f'Running: "{shlex.join(args)}"')
        os.execvpe(cpy_bin, args, env)