set -e && cd "${0%/*}"
export PATH="$PATH:~/.local/share/npm/bin"
vsce package
vscodium --install-extension ./cpy-language-0.0.0.vsix

# { "name": "general_keyword", "match": "(?<![a-zA-Z0-9_])(cls|False|await|else|import|pass|break|except|in|raise|True|class|finally|is|return|and|continue|for|lambda|try|as|def|from|nonlocal|while|assert|del|global|not|with|async|elif|if|or|yield)(?![0-9a-zA-Z_])" },

# { "name": "comment.line.number-sign",
#   "match": "(#[^֎🟑]*)(?=[֎🟑]|$)",
#   "captures": { "0": { "name": "punctuation.definition.comment" } }},

# { "name": "string", "begin": "\"", "end": "\"" }