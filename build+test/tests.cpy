# kitchen sink tests
⊢ x():
    »(2¿𝕋)≡2
    »(0¿𝔽)≡□
    »[((L≔[0])₀≔'3'), L]≡3❟⋄[3❟]
    »L₀≡'3'
    »25≡((λx: x**2)(5))
    »25≡((x↦x**2)(5))
    »25≡((h≔⥌x↦x⌃2)(5))
x()

»[j∀_∈(j≔"hi")]≡"hi"⋄"hi"
»((lambda x,i=-1: [(i := i+1) for x in range(5)])(1))≡⚇⨯0…5
j=(x=2↦x**2)
»j()≡4
»j(3)≡9
k=⥌f=(x↦x**2),y=5↦(f(y*2), 𝔸, 𝕂)₀
»(k(y=8))≡256
»((x↦[x+5,𝔸₀ ₁,𝕂])(1, "hello", 3, yay="yay"))≡6⋄e❟⋄{'yay':'yay'}

y = 5
»((⥌y=y↦↦↦y)(6)()())≡6
»τ⌃2≡֎inline comment epic֎τ**2 
»(1,a❟)₀≡1
»(2 y)≡10
»(1⋄2⋄3)₁≡2
»(a❟⋄(1¿𝔽¡2)⋄b❟)≡[a❟,2,b❟]
»((⑴x) ᴍ a❟⋄ᐦ)≡['a','']
»(1⋄2|ᴍ(⑵x+y)𐞁|3⋄4)≡[4,6]
»(ᴍ(⑵x+y,1⋄2,3⋄4))≡[4,6]
»(1⋄𝚲𝕋, 0⋄1¿1¡2⋄3)₀ ₁()≡𝕋
»((1⋄𝚲2⋄3)₁())≡[2,3]
»(⑴x+2)|ᴍ|↕(3)≡2⋄3⋄4
»'ab'⩫a❟≡b❟
»5≾int ∧ ᐦ≾ƨ ∧ 'h'≾ᐦ ∧ 0≾𝒾 ∧ 0≾0 \
       ∧ 1 𝒾.__add__𐞁 2≡3 ∧ 5⨯≾𝒾⋄ƨ \
       ∧ 5⨯≾⨯(int|float)
»1…4≡range(1,4)
»a❟|(②x+y)𐞁|b❟ ≡ 'ab'
»(𝓁"abcdefghijkmno"+['12345'])₁₄ ₃ ≡ 4❟
»'abcdef' ≡ f❟
»(①x⌃2) ᴍ 2⋄5 ≡ 4⋄25
»5<∞

# Comments
»1≡1  among sw🟑🟑🟑🟑🟑🟑🟑🟑🟑ag֎֎֎֎֎
 diahjs֎diohu;
֎
                asduha8sy0ouduiahsd
adwkai
22=@+=q]apdd
֎֎dadasdasdadw23da2dwada֎
🟑 odjaao2hda=8092hdijonkl 🟑
 🟑

# implicit multiplication
» "a" 2 3 ≡ 6 a❟
» 1 2 3 4 5 ≡ 120
» (3)2 ≡ 6

# transpose
»(𝑎≔[1⋄2,3⋄4])⍉⍉≡𝑎≠𝑎⍉

# zip
» 𝓁"ab"2  ζ    0…4   ≡ (a❟⋄0)⋄(b❟⋄1)⋄(a❟⋄2)⋄(b❟⋄3)
» 𝓁"ab"2 |ζ| 𝓁 0…2 2 ≡ (a❟⋄0)⋄(b❟⋄1)⋄(a❟⋄0)⋄(b❟⋄1) \
≡ 𝓁"ab"2  ζ  𝓁*0…2*2

# filter
» (①x>2)󰈲↕⨯10 ≡ 3…10𝓁
» (①x>2)󰈳↕⨯10 ≡ 0…3𝓁

# fold/enlist/reverse/general test
swag1 = ⥌F,n↦①(②(②y𐞂x)ſ|x⛶+ᴙF)ſ|x⛶+0⛶n
swag2 = ⥌F,n↦①(②F[-(y+1)%🃌⌃F]𐞂x)ſ|x⛶+🃌F↕𝓁n
swag3 = ⥌F,n↦①(②F₋₍₊₁₎﹪ₖ𐞂x)ſ|x⛶+(k≔🃌F)↕𝓁n
A=swag1([①A❟+x, ①B❟+x], 3)(ᐦ)
B=swag2([①A❟+x, ①B❟+x], 3)(ᐦ)
C=swag2([①A❟+x, ①B❟+x], 3)(ᐦ)
»A≡B≡C≡"ABABAB"

# set stuff
»{1,2}∪{3,2}∖{1}∩{2}≡{2}
# right/left operators [subject to change?]
»1◄2≡2►1≡1
»(①x)𐞂5⌃◄⌃2≡5

# min/max
»1⤉2 ≡ 2⤈4 ≡ ⤉(¯1,2) ≡ ⤈(5,2) ≡ 2
# constrain
»󷹄(-1,1, 22)≡1 ∧ 󷹄(-1,1,¯22)≡-1
»󷹄(¯1,1)|¯2 ≡ ¯1󷹄(¯2)1 ≡ 󷹄(¯1,1)(¯2) ≡ 󷹄(¯2)(¯1,1) ≡ ¯1
»󷹄(¯1,1)|22 ≡ ¯1󷹄(2)1 ≡ 󷹄(¯1,1)(5) ≡ 󷹄(3)(¯1,1) ≡ 1

# macros/escaping
ₛ R ␉ 𝐢 ␉ swag
ₑ R ␉ ₀ ␉ cool
ₑ I ␉ ./mapping_test
» "𝐢𝐡𝑚␛𝐡" ≡ "swageggH\N{MATHEMATICAL BOLD SMALL H}"
» "x₀" ≡ "x[0]"

☾ "CPY Tests passed!"