cd "${0%/*}" && set -e

FONT="./JuliaMono/JuliaMono-Regular.ttf"

sh ./cloneRepos.sh

python3.11 ./FontPatcher/font-patcher --careful --mono \
    --complete --has-no-italic --out . --name "JuliaMono" "$FONT"

./merge_fonts.sh JuliaMono-Regular.ttf my_symbols.ttf ./Fonts/99_JuliaMono-Regular.otf
rm 1.ttf 2.ttf JuliaMono-Regular.ttf || :

doas rm /usr/local/share/fonts/Fonts || :
doas ln -s "$(realpath "./Fonts")" /usr/local/share/fonts/Fonts
doas rm /usr/share/fonts/Fonts || :
doas ln -s "$(realpath "./Fonts")" /usr/share/fonts/Fonts

# mv ./JuliaMono-Regular.ttf ./Fonts/JuliaMono-Regular.ttf

sleep 0.1 && fc-cache -fv

# Test chars → 󷹀󷹃󷹂󷹇󷹁󷹛󷹚󷹭󷹮󷹯󷹰