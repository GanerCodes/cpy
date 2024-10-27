try:
    from util import *
except:
    import sys ; sys.path.insert(0, "..") ; from util import *

from PEGGLE2_BOOTSTRAP_AAUGH import Peggle1Bootstrap
Gram, _, Parser = Peggle1Bootstrap()

def test_peggle():
    p = Parser(r"""
        main    = z:✓ (entry 󰆴W?)*
        entry   = (
            (section=󰆴'[' wrd 󰆴']') 󰆴W?
            (pair = (
                (coolPropertyExample:key = ⠶wrd) 󰆴(w? ↷ '=')
                (value = (wrd ∨ str)+) 󰆴W? ) )* )

        str     = ~‹"[^"]+"›
        wrd     = ~‹[-\w]+›
        w       = ~‹[ \t]+›
        W       = ~‹[ \t\n]+›
    """)
    c = r"""[section]
    somekey = somevalue
    someotherkey=someothervalue
    """ * 1
    
    # p = Parser(r"""
    #     main = ((number∨A∨B∨C∨D) 󰆴W?)*
    #     number = ƨ(~‹\.[0-9]+|[0-9]+(\.([0-9]+))?|0[oxbOXB][0-9]+|[0-9]+e[0-9]+›)
    #     A      = ƨ(‹a›)
    #     B      = ƨ(‹b›)+
    #     C      = ƨ(~‹C›)+
    #     D      = ƨ(‹C› ~‹C+›)
    #     W      = ~‹[ \t\n]+›
    # """)
    # c = """20.2 .1323 .125 a a bb C CCC"""
    
    # p = Parser(r"""
    #     main = main = ƨ("A:" 󰆴(~‹a›)) "b" 󰆴"c" ⠶("a" "b") ƨ(a+)
    #     a = "h"
    # """)
    # c = """A:abcabhhhhhhhh"""
    
    # p = Parser(r"""
    #     main = (A*)
    #     A = "h"
    # """)
    # c = """hhhhh"""
    
    # exit()
    
    print("Rules:")
    # BOOTSTRAP.print_rules() ; BOOTSTRAP.print_normalized() ; exit()
    p.print_rules()
    p.print_normalized()
    togprof()
    tr = p(c)
    togprof()
    print("Results:") ; tr.print()

if __name__ == "__main__":
    test_peggle()