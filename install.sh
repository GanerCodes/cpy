#!/bin/sh
set -e && cd "$(dirname `realpath -s $0`)"

DEST=~/.local/bin/☾

python3.12 -m pip install -r requirements.txt

mkdir ./bin || :
echo '#/bin/sh' > ./bin/☾
echo 'exec python3.12 -u' \""$(realpath refresher.py)"\" '"$@"' >> ./bin/☾
chmod +x ./bin/☾

rm "$DEST" || :
ln -s "$(realpath ./bin/☾)" "$DEST"