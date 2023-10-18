import argparse, shlex, os, re
from datetime import datetime
from functools import reduce
from os import path as P

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

dmp = lambda f, j=True: open(P.join(cpy_dir, f) if j else f).read()
normalize = lambda t: t.strip().replace('␠', ƨ).replace('␤', ñ)
MAPPING_FUNCS = {
    "S": str.replace,
    "E": lambda t, F, R: t.replace(ñ+F, ñ+R+ƨ).replace(ƨ+F, ƨ+R+ƨ).replace(F, ƨ+R+ƨ),
    "R": lambda t, F, R: re.sub(F, R, t),
    "Y": lambda t, F, R: reduce(lambda x, y: str.replace(x, *y), zip(F, R), t) }
MAPPINGS = [list(map(normalize, y.split('␉'))) for x in dmp("MAPPINGS").split(ñ) if ((y:=x.strip()) and y[0]!='#')]

def escape_code(code):
    t, r = iter(code), ''
    while True:
        try: c = next(t)
        except Exception: break
        
        if c == '␛':
            c += str(ord(next(t))).zfill(7)
        r += c
    return r
def unescape_code(code):
    t, r = iter(code), ''
    while True:
        try: c = next(t)
        except Exception: break
        
        if c == '␛':
            c = chr(int(''.join(next(t) for i in range(7))))
        r += c
    return r
def compile_code(code, header=""):
    code = ñ+code
    code = escape_code(code)
    for f, *a in MAPPINGS:
        code = MAPPING_FUNCS[f](code, *a)
    code = unescape_code(code)
    return header+code[1:]

def understand_filename(f):
    b, e = P.splitext(f)
    return b + (".py" if (e == ".cpy" or not e) else e)
def proc_file(f):
    b, e = P.splitext(f)
    new_name = b+".py"
    code = compile_code(dmp(f, False), GENERAL_HEADER)
    with open(new_name, 'w') as F:
        F.write(code)
    return new_name

with open(P.join(import_dir, "CPY_HEADER.py"), 'w') as f:
    f.write(
        compile_code(
            f"{dmp("header.cpy")}\n{dmp("combinators.cpy")}\n"))

if __name__ == "__main__":
    PA = argparse.ArgumentParser(description="CPY Compiler.")
    PA.add_argument("-d", "--directory", help="Directory of CPY project")
    PA.add_argument("-n", "--no-recurse", action='store_true', help="Recurse into directory")
    PA.add_argument("-c", "--cd-file", help="cd to file location to run instead of directory")
    PA.add_argument("--test", action='store_true', help="run the cpy testing utility, ignores most other arguments")
    PA.add_argument("file", nargs='?', help="File to run (if any)")
    PA.add_argument('pyargs', nargs=argparse.REMAINDER, help="Arguments to pass to cpy_binary, eg. cpy_binary <pyarg1> <pyarg2> … <file>")
    A = PA.parse_args()
    
    if A.test:
        A.directory = f"{cpy_dir}/build+test"
        A.file = f"{A.directory}/tests.cpy"
        A.no_recurse = True
        A.cd_file = True

    D = A.directory or os.getcwd()

    files = [f for f in (
            (P.join(D, f) for f in os.listdir(D))
                if A.no_recurse else
            (P.join(R, f) for R, _, fs in os.walk(D) for f in fs)
        ) if "/.git/" not in f.replace(*'\\/') and P.splitext(f)[1] == ".cpy"]

    new_names = [print(f, '→', r:=proc_file(f)) or r for f in files]
    
    if f := A.file:
        f = understand_filename(f)
        os.chdir(P.split(f)[0] if A.cd_file else D)
        
        args = [cpy_bin, *A.pyargs, f]
        env = os.environ.copy()
        env["PYTHONPATH"] = import_dir
        env.pop("PYTHONHOME", None)
        
        print(f'Running: "{shlex.join(args)}"')
        os.execvpe(cpy_bin, args, env)