import argparse, os, re
from functools import reduce
from os import path as P

cpy_dir = P.split(__file__)[0]
dict_replace = lambda d, s: re.compile(
    f"({'|'.join(map(re.escape, d.keys()))})") \
        .sub(lambda m: d[m.string[m.start():m.end()]], s) 

dmp = lambda f, j=True: open(P.join(cpy_dir, f) if j else f).read()
HEADER = f"{dmp("header.cpy")}\n{dmp("combinators.cpy")}\n"

ñ,ƨ = '\n '
MAPPING_FUNCS = {
    "S": str.replace,
    "S_S": lambda t, F, R: t.replace(ñ+F, ñ+R+ƨ).replace(ƨ+F, ƨ+R+ƨ).replace(F, ƨ+R+ƨ),
    "R": lambda t, F, R: re.sub(F, R, t),
    "Y": lambda t, F, R: reduce(lambda x, y: str.replace(x,*y), zip(F, R), t)
}
normalize = lambda t: t.strip().replace('␠', ƨ).replace('␤', ñ)
MAPPINGS = [[*map(normalize, y.split('␉'))] for x in dmp("MAPPINGS").split('\n') if ((y:=x.strip()) and y[0]!='#')]
def compile_code(code):
    code = ñ+code
    for f, *a in MAPPINGS:
        code = MAPPING_FUNCS[f](code, *a)
    return code[1:]

def understand_filename(f):
    b, e = P.splitext(filename)
    return b + (".py" if (e == ".cpy" or not e) else e)

def proc_file(f):
    b, e = P.splitext(f)
    new_name = b+".py"
    print(compile_code(dmp(f, False)))
    print(f,'→',new_name)

PA = argparse.ArgumentParser(description="CPY Compiler.")
PA.add_argument("-d", "--directory", help="Directory of CPY project")
PA.add_argument("-n", "--no-recurse", action='store_true', help="Recurse into directory")
PA.add_argument("-c", "--cd-file", help="cd to file location to run instead of directory")
PA.add_argument("file", nargs='?', help="File to run (if any)")
A = PA.parse_args()

if not (D:=A.directory): D = os.getcwd()

if A.no_recurse:
    files = [P.join(D, f) for f in os.listdir(D)]
else:
    files = [P.join(R, f) for R, _, fs in os.walk(D) for f in fs]
files = [f for f in files if "/.git/" not in f and P.splitext(f)[1] == ".cpy"] # todo fix this

for f in files: proc_file(f)

if (f:=A.file):
    pass