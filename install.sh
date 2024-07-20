#!/bin/sh
set -e && cd "${0%/*}"

DEST=~/.local/bin/☾

python3.12 -m pip install -r requirements.txt

echo '#/bin/sh' > ./bin/☾
echo 'python3.12 -u' \""$(realpath ./refresher.py)"\" '"$@"' >> ./bin/☾

rm "$DEST" || :
ln -s "$(realpath ./bin/☾)" "$DEST"