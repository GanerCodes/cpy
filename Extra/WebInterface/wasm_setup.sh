#!/bin/bash
set -e && cd "$(dirname `realpath -s $0`)"

# b/c `zip` sometimes cares
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LC_CTYPE=UTF-8
FILE=`realpath ./wasm_stuff.zip`
TMPF="/tmp/cpy_wasm_cache"

rm -r ./cpy_wasm_cache "$FILE" || :

mkdir -p "$TMPF" || :
☾ --code-cache-dir="$TMPF/code" --gram-cache-dir="$TMPF/gram" "force_caches.☾"

cp -r "$TMPF" `realpath ./cpy_wasm_cache` || :
zip "$FILE" -r ./cpy_wasm_cache
cd ../..
zip "$FILE" -r compiler FontCompose/.SCRIPT_MAP FontCompose/Output/*.json Languages *.py -x "*/__pycache__/*"
cd -
[ $# -ge 1 ] && ☾ gen.☾