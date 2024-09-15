# Prob should be in the ☾ language folder but im lazy ⎺⟍_⟨ᐛ⟩_⟋⎺

from util import *
from string import digits
from unicodedata import is_normalized, name
py_special_mapper  = lambda c, m={'𝗻':'\\n','𝘀':' ','𝘁':'\\t'}: m[c]
py_bad_string_chr  = lambda s, bad="\n\t\\\"'{}": s in bad
py_escape_char     = lambda c, u='\\u': u+HXO(c) if py_bad_string_chr(c) else c
py_escape_string   = lambda s: ᐦ.join(py_escape_char(c) for c in s)
py_ok_identifier   = lambda x: x in digits or is_normalized("NFKC", x) and x.isidentifier()
py_reformat_char   = lambda c: f"ᐧ{(name(c, HXO(c)).replace(ś, '_').replace('-', '_'))}ᐧ" # HXO(c)+'ᐧ' better but needs sed-stuff for debuggin
py_escape_var      = lambda s, check=1: ᒍ(ᐦ, (c if ord(c)<127 and c!='!' or py_ok_identifier(c) else py_reformat_char(c) for c in s)) \
                                    if check and s != '!=' else s