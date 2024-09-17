if [ ! -d "FontPatcher" ]; then
    git clone -n --depth=1 --filter=tree:0 https://github.com/ryanoasis/nerd-fonts FontPatcher
    cd FontPatcher
        git sparse-checkout set --no-cone src/glyphs font-patcher bin
        git checkout
        sed -i 's/ProggyClean\x27,/ProggyClean\x27,\x27JuliaMono\x27/g' ./bin/scripts/name_parser/FontnameTools.py
    cd -
fi

if [ ! -d "JuliaMono" ]; then
    rm -r JuliaMono || :
    mkdir JuliaMono && cd JuliaMono
        wget https://github.com/cormullion/juliamono/releases/download/v0.056/JuliaMono-ttf.zip
        unzip JuliaMono-ttf.zip && rm JuliaMono-ttf.zip
    cd -
fi