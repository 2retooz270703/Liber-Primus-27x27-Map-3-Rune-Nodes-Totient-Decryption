# 15 — SOON

> **Recovered plaintext candidate:** `SOON`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON`  
> **Status:** strongest current continuation after `YOU`. The primary route produces the same key from three different mirror structures. A longer, separate route also decrypts to `SOON`. The calculations are exact; some route choices remain hypotheses.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. Start from the end of YOU

The previous chapter, [`14-YOU.md`](./14-YOU.md), ends at:

```text
X(25,16)
```

Its key comes from `P-R-P → P-TH-P`, with Möbius phase **1**. We carry that phase into the next coordinate calculation:

```text
φ(25) = 20 = L     μ(20) = 0
φ(16) =  8 = H     μ(8)  = 0

T₁(25,16) = (20,8) = (L,H)
V₁(25,16) = (0,0)
```

Möbius gives no direction, but the existing **hidden-value rule** retains `L` and `H`.

The proposed roles are simple:

```text
H → end of the ciphertext
L → start of the key-generating structures
```

---

## 2. H marks a ciphertext beside X

On the same row, `H` appears three cells to the right of the final `YOU` node:

```text
X(25,16) → D(25,17) → W(25,18) → H(25,19)

CIPHERTEXT = X-D-W-H
```

The directed sequence `X-D-W-H` occurs **only once** among the grid's straight, consecutive four-rune paths.

The crucial point is that **H=8 was already present in the coordinate state**. Its role as the next ciphertext endpoint is a proposed selection rule, not something the Möbius signs alone determine.

---

## 3. One EA mirror connects three key generators

The ciphertext is contained inside the right arm of a horizontal mirror:

```text
EA(25,10) ── 5 ── EA(25,15) ── 5 ── EA(25,20)

EA(25,15) | X-D-W-H | EA(25,20)
```

This is the grid's **only standard EA-EA-EA mirror**.

Now look at its three `EA` nodes. Each can be reached by a different equal-step structure starting with the other hidden rune, **L**:

| Generator | Exact mirror | Center transformation |
|---|---|---|
| A | `L(25,4) — C(25,7) — EA(25,10)` | `φ(C=5)=4=R` |
| B | `L(15,15) — I(20,15) — EA(25,15)` | `φ(I=10)=4=R` |
| C | `L(25,8) — EO(25,14) — EA(25,20)` | `φ(EO=12)=4=R` |

Their arm lengths are **3, 5, and 6** respectively. All three centers independently produce the same unrotated key:

```text
L-C-EA  ─┐
L-I-EA  ─┼─→ L-R-EA
L-EO-EA ─┘
```

**This is the main strength of the primary route:** three different geometric structures, attached to the three nodes of one larger mirror, converge on **L-R-EA**. They are distinct constructions, though not three statistically independent proofs.

---

## 4. Two numerical cross-checks

The first connection comes from the complete set of positive rune indices satisfying `φ(n)=4`:

```text
{5,8,10,12} = {C,H,I,EO}
```

Three of these are exactly the key-mirror centers:

```text
C, I, EO → φ = 4 = R
```

The fourth is **H**, the ciphertext endpoint. Thus one totient class appears on both sides of the construction.

There is also a prime-weight match. The hidden pair after `YOU` is `L,H`:

```text
prime(L) + prime(H) = 73 + 23 = 96

prime(SOON) = S + O + O + N
            = 53 + 7 + 7 + 29 = 96
```

So:

```text
prime(L) + prime(H) = prime(SOON) = 96
```

These are exact numerical relationships. They **support checking the proposed route**, but neither one determines the route or proves the word was intentionally encoded.

---

## 5. Möbius fixes the key — and decrypts SOON

All three generators give the unrotated key `L-R-EA`.

```text
KEY = L-R-EA

Totient signature:
φ(20), φ(4), φ(28) = (8,2,12)

Möbius signature:
μ(8), μ(2), μ(12) = (0,-1,0)

phase = (0-1+0) mod 3 = 2
```

Rotate by the calculated phase and repeat the first rune for the fourth ciphertext position:

```text
L-R-EA → phase 2 → EA-L-R

ACTIVE KEY = EA-L-R-EA
```

Apply `P = (C − K) mod 29`:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `X = 14` | `EA = 28` | `14 − 28 ≡ 15` | **S** |
| `D = 23` | `L = 20` | `23 − 20 = 3` | **O** |
| `W = 7` | `R = 4` | `7 − 4 = 3` | **O** |
| `H = 8` | `EA = 28` | `8 − 28 ≡ 9` | **N** |

```text
CIPHERTEXT: X   D   W   H
KEY:        EA  L   R   EA
            --------------
PLAINTEXT:  S   O   O   N
```

# **SOON**

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON**

---

## 6. A hidden second route begins at the same X

There is also a **different geometric route** to `SOON`, using another ciphertext and another key.

Start again at `X(25,16)`. It is the center of:

```text
E(24,16)
X(25,16)
E(26,16)

E-X-E
```

The upper `E(24,16)` connects to:

```text
E(22,14) — TH(23,15) — E(24,16)
```

The center **TH(23,15)** is a mirror hub. Two further mirrors pass through it:

```text
X(19,19) — TH(23,15) — X(27,11)   (radius 4)
D(22,15) — TH(23,15) — D(24,15)   (radius 1)
```

The `X-TH-X` branch leads to the **second ciphertext**; the `D-TH-D` branch leads to its **key**. These are real mirror connections, although choosing each branch is not yet dictated by a universal rule.

---

## 7. The secondary ciphertext: P-S-U-W

Follow the `X-TH-X` branch to `X(27,11)`, then through the connected mirrors:

```text
X(19,19) — TH(23,15) — X(27,11)
                            |
D(27,2) ───────── X(27,11) ───────── D(27,20)
                                       |
P(27,16) ─────── D(27,20) ─────── P(27,24)
```

The last `P` begins a consecutive four-rune segment:

```text
P(27,24) → S(27,25) → U(27,26) → W(27,27)

CIPHERTEXT₂ = P-S-U-W
```

This directed `P-S-U-W` also occurs **only once** in the grid.

There is a direct link to the earlier research: **P(27,16)** was already used in [`14-YOU.md`](./14-YOU.md). The hidden second route therefore intersects a previously known node before reaching a new endpoint, **W(27,27)**.

---

## 8. The secondary key and a second SOON

Return to the same hub, `TH(23,15)`, and follow the other branch:

```text
D(22,15) — TH(23,15) — D(24,15)
D(22,15) — NG(22,17) — D(22,19)
IA(22,16) — D(22,19) — IA(22,22)
IA(16,10) — EA(19,13) — IA(22,16)
```

The last mirror generates the key:

```text
IA-EA-IA

φ(EA=28) = 12 = EO

IA-EA-IA → IA-EO-IA
```

Möbius fixes its phase without changing the order:

```text
Totient signature = (18,4,18)
Möbius signature  = (0,0,0)
phase = 0

ACTIVE KEY₂ = IA-EO-IA-IA
```

Now decrypt the second ciphertext:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `P = 13` | `IA = 27` | `13 − 27 ≡ 15` | **S** |
| `S = 15` | `EO = 12` | `15 − 12 = 3` | **O** |
| `U = 1` | `IA = 27` | `1 − 27 ≡ 3` | **O** |
| `W = 7` | `IA = 27` | `7 − 27 ≡ 9` | **N** |

```text
CIPHERTEXT₂: P   S   U   W
KEY₂:        IA  EO  IA  IA
             --------------
PLAINTEXT:   S   O   O   N
```

# **SOON — AGAIN**

The second route uses **different ciphertext, a different mirror key, and phase 0**, yet gives the same plaintext. It is a supporting reconstruction, not a proven independent message from Cicada.

---

## 9. Why the two SOON routes matter

The constructions can be compared directly:

| | Primary SOON | Hidden secondary SOON |
|---|---|---|
| Ciphertext | `X-D-W-H` | `P-S-U-W` |
| Active key | `EA-L-R-EA` | `IA-EO-IA-IA` |
| Key phase | **2** | **0** |
| Final cell | **H(25,19)** | **W(27,27)** |
| Main structure | Unique `EA-EA-EA` with three key generators | Two branches from the `TH(23,15)` mirror hub |

The primary route is the better direct continuation of `YOU` because it starts at the final `X` of `YOU`, applies the inherited phase 1 to its coordinates, finds `H` on the same row, and produces its key through three converging structures.

The longer secondary route is valuable because it reaches **the same word without reusing the primary ciphertext or key**. It has more unresolved branch choices, so it should remain a cross-check rather than replace the direct route.

### A connection that becomes important in chapter 16

The primary `SOON` endpoint is **H(25,19)** with phase **2**:

```text
φ²(25) = 8     μ(8) = 0
φ²(19) = 6     μ(6) = +1

T₂(25,19) = (8,6)
V₂(25,19) = (0,+1) → RIGHT
```

Those **pre-existing values (8,6)** are the starting state for [`16-THEN.md`](./16-THEN.md).

The *secondary* `SOON` endpoint **W(27,27)** also matters later: the proposed `THEN` ciphertext ends at **W(25,27)**, and the two endpoints belong to one exact vertical mirror:

```text
W(25,27)    ← end of THEN
   |
NG(26,27)   ← center
   |
W(27,27)    ← end of secondary SOON
```

So the second `SOON` route is not just a duplicated decryption: **its endpoint becomes part of a concrete geometric connection in the next chapter**. That connection makes `W-NG-W` a natural mirror to examine, but does not by itself prove a mandatory phase choice.

---

## 10. What remains open

The primary route has a strong internal structure, but it still assumes the hidden pair `(L,H)` is used as:

```text
L → key-generating mirrors
H → ciphertext endpoint
```

This role assignment needs to be predicted by a reusable rule rather than justified only after finding `SOON`.

The hidden secondary route has additional fork choices, especially the choice of **IA(22,16)** rather than **IA(22,22)** in the `IA-D-IA` mirror.

**What is established:** both ciphertexts, both keys, the phase calculations, the mirror coordinates, and the two modular decryptions can be checked directly on the map.

**What remains a hypothesis:** that either route—especially the longer hidden route—was intentionally designed to produce the plaintext `SOON`.

The most useful next step is already documented in [`16-THEN.md`](./16-THEN.md): the fixed primary endpoint **H(25,19)** and phase **2** produce `(8,6)`, which can be tested against the next ciphertext's geometry.
