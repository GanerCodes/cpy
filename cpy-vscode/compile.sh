set -e && cd "${0%/*}"
export PATH="$PATH:/home/ganer/.local/share/npm/bin"
vsce package
vscodium --install-extension ./cpy-language-0.0.0.vsix