#!/bin/bash
"`npm root -g`/vsce/vsce" package
`command -v codium || echo "vscode"` --install-extension "`ls *.vsix | tail -n1`"