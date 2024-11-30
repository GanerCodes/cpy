from util import *

# this should prob be the composition of some normal cacher and a filecacher ⎺⟍_⟨.~.⟩_⟋⎺
class FileCacher:
    __slots__ = *"pfHLSC", "has_local"
    def __init__(𝕤, p, 𝑓, 𝓛=loads, 𝓢=dumps, 
                 𝓗=lambda *𝔸, **𝕂: sha256(f"{𝔸}{𝕂}"),
                 has_local=ⴳ):
        if p: os.makedirs(p := Path(p), exist_ok=1)
        𝕤.p, 𝕤.𝑓, 𝕤.𝓛, 𝕤.𝓢, 𝕤.𝓗 = p, 𝑓, 𝓛, 𝓢, 𝓗
        if has_local:
            𝕤.has_local, 𝕤.ℭ = ⴳ, {}
    def __call__(𝕤, *𝔸, **𝕂):
        h = 𝕤.𝓗(*𝔸, **𝕂)
        if 𝕤.has_local:
            if h in 𝕤.ℭ:
                return 𝕤.ℭ[h]
        if 𝕤.p and os.path.exists(p := 𝕤.p / h):
            with open(p, "rb") as f:
                R = f.read()
            try:
                v = 𝕤.𝓛(R)
                if 𝕤.has_local:
                    𝕤.ℭ[h] = v
                return v
            except Exception as ε:
                ε = ["Failed to load cached file!", ε]
                try:
                    p.unlink()
                except Exception as ε2:
                    ε += ["Failed to remove corrupted cache file!", ε2]
                    raise ε
        v = 𝕤.𝑓(*𝔸, **𝕂)
        if 𝕤.has_local:
            𝕤.ℭ[h] = v
        if 𝕤.p:
            W = 𝕤.𝓢(v)
            with open(h, "wb") as f:
                f.write(W)
        return v