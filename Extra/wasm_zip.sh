set -e && cd "$(dirname `realpath -s $0`)"

FILE="./Extra/wasm_stuff.zip"

rm "$FILE" || :
cd ..
zip -r "$FILE" compiler FontCompose/.SCRIPT_MAP FontCompose/Output/*.json Languages *.py -x "*/__pycache__/*"
cd -
python -m http.server