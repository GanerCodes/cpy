import fontforge
import psMat

file = open("compose.txt","r")
compose = file.read()
lines = compose.split("\n")
file.close()
seqs = {}
for line in lines:
    if len(line)<3 or line[0]=="#" or line[-3]!="\"":
        continue
    if not line[-2] in seqs.keys():
        seqs[line[-2]] = []
    seqs[line[-2]].append(line[:-4])
file = open("compose.txt","a")

font = fontforge.open("JuliaMono-Regular.otf")
w = 1200

# ↓↓ change pua_start to add new characters
pua_start = 0x0F1AF1
pua_end = 0x10FFFD

# ↓↓ done in each function because i want to keep characters
# Clear existing PUA glyphs
# for codepoint in range(pua_start, pua_end + 1):
#     try:
#         font.removeGlyph(font[codepoint])
#     except:
#         pass

# ↓↓ self-explanatory
letters = "✝𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫ƇƊҒႺꝈⱮⴽ𝖲ƬѴ𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷𝞋𝝸𝝹𝝺𝝻𝝼𝝽𝝿𝞀𝞁𝞂𝞃𝞄𝞅𝞆𝞇𝞈𝞉𝞍𝝘𝝙𝝯𝝝𝝣𝝥𝝨𝝫𝝭𝝮𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝝑𝜾𝜿𝝀𝝁𝝂𝝃𝝅𝝆𝝇𝝈𝝉𝝊𝝋𝝌𝝍𝝎𝝏𝝓𝜞𝜟𝜵𝜣𝜩𝜫𝜮𝜱𝜳𝜴𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅󰲡󰲣󰲥󰲧󰲩󰲫󰲭󰲯󰲱Ӎ❴❵ℓ℘ℵתℶƒαβγδεζηθϑικλμνξπρςστυφχψω∂ϕΓΔ∇ΘΞΠΣΦΨΩΧ🜂🜄ᐄᐂϲ∀⊲󷹁󷹇󰤱§⨃✣⯈⮞⫢‖÷√¬∅∫∃∄⇕󷹂󷹃∴∵≁≈≔≝≜󷹀≟≅≇≠≡≢∣∤⫰⫯∓±′″‴⁗｜│＊＋／＼＃＞＜⊞ⵌ⌗⨳♯¿⸮␦¡❗ƨƧᖵᖶ∈∉⋸∋∌⟒⫙∧∨⋀⋁⊻⊼≮≤≰≯≥≱∪∩⊃⊂⊅⊋⊇⊉⊄⊊⊆⊈⋃⋂⇍⇏⟨⟩⭥⤡⤢⭡⭣⬆⬇➡↑↓󷹛󷹚⇑⇓⇐⇒↥↧↤↦⊥⊤⊣⊢⋮⋰⋱⌜⌝⌞⌟⌈⌉⌊⌋↕🟑֎󰒼󰒽⮌󰈲󰈳⤉⤈󷹄◄◄►⍭🃌≾⩫ⴵꟿᔐ↺ᒍ⌃∖ᐦ❟󰆴⁅⁆󰅁󰅂⇥⠤󱠨↨⛶🝇ᴍ☾▢↪ᴙ⍉➰⮂⥌⠶🜌𝚲󰋺⨡ᐹ⹏⨝⟕⟗⟖⟦⟧ⴳⴴᗜ⟥⟤꜠ᵜᗯᖲᖱᒪⴷⴸ␡␛⚙✌♺↋↊Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝝤𝝦𝝧𝝩𝝪𝝬𝝾𝞊𝞌𝞎𝞏𝞐𝞑𝞒𝞓𝜵𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞡𝞢𝞣𝞤𝞥𝞦𝞧𝞨𝞩𝞪𝞫𝞬𝞭𝞮𝞯𝞰𝞱𝞲𝞳𝞴𝞵𝞶𝞷𝞸𝞹𝞺𝞻𝞼𝞽𝞾𝞿𝟀𝟁𝟂𝟃𝟄𝟅𝟆𝟇𝟈𝟉𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяΑΒΕΖΗΙΚΛΜΝΟΡΤΥο½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖↉¾⅗⅜⅘⅚⅝⅞[]{}《》｟｠〔〕【】⥏⥑⥜⥠⥝⥡⦋⦌⢨⡅£֍⫾|∥𝜋☃\\/∛∜Ø#⨄⋒⩀⨆∬∭⨌∮∯∰∱⨑∲∳⨕⨖æÆ↮⋉⋊⨲⋈≀⁒╱♭⫚ѵ¶₀⁰₁¹ₙⁿᵢⁱⱼᶨₖᵏ⋎⋏⩄⩅⩑⩒⩓⩔⩕⩖⩙⩚⩛⩜⩝⩞⩟⩠⩢⩣"
letters_no_scale = "⑴⑵⑶⑷⑸⑹⑺⑻⑼⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵🄐🄑🄒🄓🄔🄕🄖🄗🄘🄙🄚🄛🄜🄝🄞🄟🄠🄡🄢🄣🄤🄥🄦🄧🄨🄩⓪①②③④⑤⑥⑦⑧⑨ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩♼⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳·«»↾↿⇂⇃‹›🢔🢖…𝄽⟎⟏⨇⨈✇☮߷♳♴♵♶♷♸♹≃~⋄◌⟐♢↔☺☹♡⛥✡𝌃𝌂*♲✍␤␠␉⟷⭠⭢←→↖↗↙↘🡹🡻🡸🡺🡼🡽🡿🡾⟵⟶⇜⇝⋯⬅⎊⎉⌾⊖⨸⊗⊕⬡⨁⨂⋅•⬤∘⊙⨀○⭗～∗⨯×□⨉－─⟺✓✗∞≖󷹯󷹭󷹮󷹰"
doubles = ["𝓵𝓷","𝓵𝓰","𝘁𝗿","𝗦𝗟","𝗚𝗟","𝗿𝗸","𝘀𝘁","𝗪⁵"] #inline style
triples = ["𝗘𝗻𝗱","𝗔𝘂𝘁","𝗚𝗮𝗹","𝗸𝗲𝗿","𝓵𝓸𝓰","𝘀𝗶𝗻","𝗰𝗼𝘀","𝘁𝗮𝗻","𝘀𝗲𝗰","𝗰𝘀𝗰","𝗰𝗼𝘁","𝗔𝘀𝘀","𝗮𝗿𝗴","𝗺𝗮𝘅","𝗺𝗶𝗻","𝗲𝘅𝗽","𝗱𝗶𝘃","𝗱𝗲𝘁","𝗱𝗲𝗴","𝗲𝗿𝗳","𝗶𝗻𝘁","𝗴𝗰𝗱","𝗹𝗰𝗺","𝗵𝗼𝗺","𝗼𝗯𝗷","𝗹𝗶𝗺","𝗶𝗻𝗳","𝘀𝘂𝗽","𝗺𝗼𝗱","𝗣𝗚𝗟","𝗣𝗦𝗟","𝘀𝗴𝗻","𝘁𝗼𝗿","𝘄𝗿𝘁","𝗪𝗧𝗦","𝗪𝗧𝗙","𝘃𝗮𝗿","𝘀𝘁𝗱","𝗰𝗼𝘃"] # inline style
quads = ["𝗦𝗣𝗘𝗖","𝗦𝗜𝗡𝗛","𝗖𝗢𝗦𝗛","𝗧𝗔𝗡𝗛","𝗦𝗘𝗖𝗛","𝗖𝗦𝗖𝗛","𝗖𝗢𝗧𝗛","𝗖𝗛𝗔𝗥","𝗖𝗨𝗥𝗟","𝗙𝗥𝗢𝗕","𝗚𝗥𝗔𝗗","𝗥𝗔𝗡𝗞","𝗦𝗣𝗔𝗡","𝗪𝗟𝗢𝗚","𝗘𝗥𝗙𝗖","𝗠𝗘𝗠𝗘","𝗡𝗨𝗟𝗟","𝗩𝗢𝗜𝗗","𝗖𝗢𝗥𝗥"] #falling style weeeeeeee

total_used = len(letters)*2+len(letters_no_scale)*2+len(doubles)+len(triples)+len(quads)
print(total_used)

def add_sub_sup_scripts(font, letters, pua_start, scale=True):
    for i, char in enumerate(letters):
        subscript = chr(pua_start + i)
        superscript = chr(pua_start + len(letters) + i)
        sub_glyph = font.createChar(ord(subscript), char + "_sub")
        sup_glyph = font.createChar(ord(superscript), char + "_sup")
        
        # Copy design from the original character
        try:
            sub_glyph.addReference(font[ord(char)].glyphname)
            sup_glyph.addReference(font[ord(char)].glyphname)
        except:
            print("fail at: "+str(ord(char)))
        # Transform to make subscript/superscript smaller and adjust position 
        if scale:
            sub_glyph.transform(psMat.scale(0.6))
            sub_glyph.transform(psMat.translate(w * 0.15, -w * 0.1))
            sup_glyph.transform(psMat.scale(0.65))
            sup_glyph.transform(psMat.translate(w * 0.15, w * 0.65))
        else:
            sub_glyph.transform(psMat.translate(0, -w * 0.35))
            sup_glyph.transform(psMat.translate(0, w * 0.35))

        sub_glyph.width = w
        sup_glyph.width = w

        #add to the xcompose sequences. does another file because im scared of messing up
        # 󰤱 make this work because potential issues
        # codes = {
        #     "<": "less",
        #     ">": "greater"
        # }
        if char in seqs.keys():
            for seq in seqs[char]:
                file.write("<Multi_key><slash>"+seq+":\""+subscript+"\"\n")
                file.write("<Multi_key><backslash>"+seq+":\""+superscript+"\"\n")
        else: #catches characters that have no compose yet and characters that already exist like ~
            file.write("<Multi_key><slash><"+char+">:\""+subscript+"\"\n")
            file.write("<Multi_key><backslash><"+char+">:\""+superscript+"\"\n")
# 󱾄󱽽󱾌 󱾁󱾌 󱽿󱾊󱾇󱾏 𐂷🌲🌳🌴🎄🎋 󱹯󱹡󱹟󱹮󱹡󱹰 󱹩󱹡󱹯󱹯󱹝󱹣󱹡 A𝔸𝓐𝐀𝐴𝔄𝕬🄐Ⓐ🄰🅐А𝗔
# little snowman 󱼩

#lots of trial-error placement here, all of the psMat.function arguments can be changed
def add_doubles(font, doubles, pua_start):
    for i,pair in enumerate(doubles):
        newb = chr(pua_start+i)
        new_glyph = font.createChar(ord(newb),pair+"_combined")
        new_glyph.addReference(font[ord(pair[0])].glyphname)
        new_glyph.transform(psMat.translate(-w * 0.8, 0))
        new_glyph.addReference(font[ord(pair[1])].glyphname)
        new_glyph.transform(psMat.translate(w * 0.9, 0))
        new_glyph.transform(psMat.scale(0.6))
        new_glyph.width = w

def add_triples(font, triples, pua_start):
    for i,pair in enumerate(triples):
        newb = chr(pua_start+i)
        new_glyph = font.createChar(ord(newb),pair+"_combined")
        new_glyph.addReference(font[ord(pair[0])].glyphname)
        new_glyph.transform(psMat.translate(-w * 0.8, 0))
        new_glyph.addReference(font[ord(pair[1])].glyphname)
        new_glyph.transform(psMat.translate(-w * 0.8, 0))
        new_glyph.addReference(font[ord(pair[2])].glyphname)
        new_glyph.transform(psMat.translate(w * 0.4, -w * 0.6))
        new_glyph.transform(psMat.scale(0.5))
        new_glyph.transform(psMat.translate(w * 0.55, w * 0.5))
        new_glyph.width = w

def add_quads(font, quads, pua_start):
    for i,pair in enumerate(quads):
        newb = chr(pua_start+i)
        new_glyph = font.createChar(ord(newb),pair+"_combined")
        new_glyph.addReference(font[ord(pair[0])].glyphname)
        new_glyph.transform(psMat.translate(-w,w * 0.6))
        new_glyph.addReference(font[ord(pair[1])].glyphname)
        new_glyph.transform(psMat.translate(0, w * 1.3))
        new_glyph.addReference(font[ord(pair[2])].glyphname)
        new_glyph.transform(psMat.translate(-w, w * 0.6))
        new_glyph.addReference(font[ord(pair[3])].glyphname)
        new_glyph.transform(psMat.translate(0, -w * 1.9))
        new_glyph.transform(psMat.scale(0.4))
        new_glyph.transform(psMat.translate(w * 0.7, w * 0.6))
        new_glyph.width = w

#i was going to make the functions return the new start location but im too lazy. be careful here
start = pua_start
add_sub_sup_scripts(font, letters, start)
start = start+2*len(letters)
add_sub_sup_scripts(font, letters_no_scale, start, scale=False)
start = start+2*len(letters_no_scale)
add_doubles(font, doubles, start)
start = start+len(doubles)
add_triples(font, triples, start)
start = start+len(triples)
add_quads(font, quads, start)

# ↓↓ done in the functions
# for glyph in font.glyphs():
#     glyph.width = w

# chatgpt is terrible at coding and this garbage doesnt even compile
# font.selection.select(("ranges",None),pua_start,pua_start+2*len(letters)+len(doubles))
# font.selection.CenterInWidth()

font.generate("secondBestMonoFont.ttf")
font.close()

file.close()