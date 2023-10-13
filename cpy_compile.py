import argparse, shlex, os, re
from functools import reduce
from os import path as P

cpy_bin = P.join(
    cpy_dir := P.split(__file__)[0],
    "bin/cpy_binary")

dict_replace = lambda d, s: re.compile(
    f"({'|'.join(map(re.escape, d.keys()))})") \
        .sub(lambda m: d[m.string[m.start():m.end()]], s) 

dmp = lambda f, j=True: open(P.join(cpy_dir, f) if j else f).read()

ñ,ƨ = '\n '
MAPPING_FUNCS = {
    "S": str.replace,
    "E": lambda t, F, R: t.replace(ñ+F, ñ+R+ƨ).replace(ƨ+F, ƨ+R+ƨ).replace(F, ƨ+R+ƨ),
    "R": lambda t, F, R: re.sub(F, R, t),
    "Y": lambda t, F, R: reduce(lambda x, y: str.replace(x, *y), zip(F, R), t) }
normalize = lambda t: t.strip().replace('␠', ƨ).replace('␤', ñ)
MAPPINGS = [[*map(normalize, y.split('␉'))] for x in dmp("MAPPINGS").split(ñ) if ((y:=x.strip()) and y[0]!='#')]
def compile_code(code, header=""):
    code = ñ+code
    for f, *a in MAPPINGS:
        code = MAPPING_FUNCS[f](code, *a)
    return header+code[1:]

def understand_filename(f):
    b, e = P.splitext(f)
    return b + (".py" if (e == ".cpy" or not e) else e)

HEADER = compile_code(f"{dmp("header.cpy")}\n{dmp("combinators.cpy")}\n")
def proc_file(f):
    b, e = P.splitext(f)
    new_name = b+".py"
    code = compile_code(dmp(f, False), HEADER)
    with open(new_name, 'w') as F:
        F.write(code)
    return new_name

PA = argparse.ArgumentParser(description="CPY Compiler.")
PA.add_argument("-d", "--directory", help="Directory of CPY project")
PA.add_argument("-n", "--no-recurse", action='store_true', help="Recurse into directory")
PA.add_argument("-c", "--cd-file", help="cd to file location to run instead of directory")
PA.add_argument("file", nargs='?', help="File to run (if any)")
PA.add_argument('pyargs', nargs=argparse.REMAINDER, help="Arguments to pass to cpy_binary, eg. cpy_binary <pyarg1> <pyarg2> … <file>")
A = PA.parse_args()

D = A.directory or os.getcwd()

files = [f for f in (
        (P.join(D, f) for f in os.listdir(D))
            if A.no_recurse else
        (P.join(R, f) for R, _, fs in os.walk(D) for f in fs)
    ) if "/.git/" not in f.replace(*'\\/') and P.splitext(f)[1] == ".cpy"]

new_names = [print(f, '→', r:=proc_file(f)) or r for f in files]

if (f:=A.file):
    f = understand_filename(f)
    os.chdir(P.split(f)[0] if A.cd_file else D)
    
    args = [cpy_bin, *A.pyargs, f]
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    
    print(f'Running: "{shlex.join(args)}"')
    os.execvpe(cpy_bin, args, env)