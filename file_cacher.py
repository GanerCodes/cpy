from util import *
class FileCacher:
    __slots__ = *"fHLS",
    def __init__(𝕤, p, 𝑓, 𝓛=loads, 𝓢=dumps, 
                 𝓗=lambda *𝔸, **𝕂: sha256(f"{𝔸}{𝕂}")):
        if p: os.makedirs(p := Path(p), exist_ok=1)
        𝕤.𝑓, 𝕤.𝓛, 𝕤.𝓢 = 𝑓, 𝓛, 𝓢
        𝕤.𝓗 = p and (lambda *𝔸, **𝕂: p / str(𝓗(*𝔸, **𝕂)))
    def __call__(𝕤, *𝔸, **𝕂):
        if not 𝕤.𝓗: return 𝕤.𝑓(*𝔸, **𝕂)
        if os.path.exists(p := 𝕤.𝓗(*𝔸, **𝕂)):
            with open(p, "rb") as f:
                R = f.read()
            try:
                return 𝕤.𝓛(R)
            except Exception as ε:
                ε = ["Failed to load cached file!", ε]
                try:
                    p.unlink()
                except Exception as ε2:
                    ε += ["Failed to remove corrupted cache file!", ε2]
                raise ε
        W = 𝕤.𝓢(v := 𝕤.𝑓(*𝔸, **𝕂))
        with open(p, "wb") as f:
            f.write(W)
        return v