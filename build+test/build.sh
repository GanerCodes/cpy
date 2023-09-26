set -e && cd "${0%/*}"

unset PYTHONHOME PYTHONSTARTUP PYTHONPATH
cd ../cpython-fork
    make -s -j8 distclean && echo C l e a n
    # ./configure -q --with-ensurepip=install --with-pydebug
    ./configure -q --with-ensurepip=install
    make -s -j8 regen-token
    make -s -j8 regen-pegen
    make -s -j8 regen-global-objects
    make -s -j8 regen-all
    make -s -j8
    ./python -m ensurepip --default-pip
cd -

cpy_tool tests.py


# make -s -j8 regen-pegen regen-frozen
# static int symtable_handle_namedexpr(struct symtable *st, expr_ty e) {
#     VISIT(st, expr, e->v.NamedExpr.value);
#     VISIT(st, expr, e->v.NamedExpr.target);
#     return 1;
# }
