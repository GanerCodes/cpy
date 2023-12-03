set -e && cd "${0%/*}"
export PATH="$PATH:~/.local/share/npm/bin"
vsce package
vscodium --install-extension ./cpy-language-0.0.0.vsix