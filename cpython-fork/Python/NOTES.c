// symtable.c
static int
symtable_handle_namedexpr(struct symtable *st, expr_ty e)
{
    // λ
    // if (st->st_cur->ste_comp_iter_expr > 0) {
    //     /* Assignment isn't allowed in a comprehension iterable expression */
    //     PyErr_Format(PyExc_SyntaxError, NAMED_EXPR_COMP_ITER_EXPR);
    //     PyErr_RangedSyntaxLocationObject(st->st_filename,
    //                                       e->lineno,
    //                                       e->col_offset + 1,
    //                                       e->end_lineno,
    //                                       e->end_col_offset + 1);
    //     return 0;
    // }
    if (st->st_cur->ste_comprehension) {
        /* Inside a comprehension body, so find the right target scope */
        if (!symtable_extend_namedexpr_scope(st, e->v.NamedExpr.target))
            return 0;
    }
    VISIT(st, expr, e->v.NamedExpr.value);
    VISIT(st, expr, e->v.NamedExpr.target);
    return 1;
}


// python.gram

/* assignment_expression[expr_ty]: # λ
    | a=primary ':=' ~ b=expression {
        CHECK_VERSION(expr_ty, 8, "Assignment expressions are",
        _PyAST_NamedExpr(CHECK(expr_ty, _PyPegen_set_expr_context(p, a, Store)), b, EXTRA)) } */

/* named_expression[expr_ty]: # λ
    | assignment_expression
    | expression !':='
    # | invalid_named_expression */

/* expression[expr_ty] (memo): # λ
    | a=disjunction 'if' b=disjunction 'else' c=expression { _PyAST_IfExp(b, a, c, EXTRA) }
    | a=disjunction 'if' b=disjunction { _PyAST_IfExp(b, a, _PyAST_Constant(Py_None, NULL, EXTRA), EXTRA) }
    | invalid_legacy_expression
    | disjunction
    | lambdef */