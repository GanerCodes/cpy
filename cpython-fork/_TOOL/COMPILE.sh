set -e
unset PYTHONHOME PYTHONSTARTUP PYTHONPATH
cd ..
make -s -j8 distclean && echo C l e a n
./configure -q --with-ensurepip=install --with-pydebug
# exit 0
make -s -j8 regen-token
make -s -j8 regen-pegen
make -s -j8 regen-global-objects
make -s -j8 regen-all
make -s -j8
./python -m ensurepip --default-pip

bin_location="$(realpath ../bin)/cpy_binary"
rm "${bin_location}"
ln -s "$(realpath "./python")" "${bin_location}"
cd TOOL
cpy_tool TESTING.py

# make -s -j8 regen-pegen regen-frozen

# static int symtable_handle_namedexpr(struct symtable *st, expr_ty e) {
#     VISIT(st, expr, e->v.NamedExpr.value);
#     VISIT(st, expr, e->v.NamedExpr.target);
#     return 1;
# }