cp ./Output/99_JuliaMono-Regular.ttf /Configs/Fonts/99_JuliaMono-Regular.ttf
cp ./Output/.XCompose /Configs/X11_Configs/.XCompose

doas rm /usr/local/share/fonts/Fonts || :
doas ln -s "$(realpath "/Configs/Fonts")" /usr/local/share/fonts/Fonts
doas rm /usr/share/fonts/Fonts || :
doas ln -s "$(realpath "/Configs/Fonts")" /usr/share/fonts/Fonts

sleep 0.1 && fc-cache -fv

# Test chars → 󷹀󷹃󷹂󷹇󷹁󷹛󷹚󷹭󷹮󷹯󷹰
