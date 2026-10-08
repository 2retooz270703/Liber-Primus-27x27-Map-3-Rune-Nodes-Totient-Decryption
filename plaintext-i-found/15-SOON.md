# 15 — SOON

AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH. SEE YOU SOON.

## 1. Start from the end of YOU

The previous chapter, [`14-YOU.md`](./14-YOU.md), ends at **X(25,16)**. Its `P-R-P` mirror generated the key `TH-P-P` with **Möbius phase 1**. We carry this established phase into the coordinate calculation at `X`.

```text
φ(25) = 20 = L   → μ(20) = 0
φ(16) =  8 = H   → μ(8)  = 0

T₁(25,16) = (20,8) = (L,H)
V₁(25,16) = (0,0)
```

The Möbius pair `(0,0)` does not give a direction. However, the project's **hidden-value rule** retains the two values obtained before applying Möbius: **L** and **H**.

In the proposed continuation, **H** helps identify the ciphertext, while **L** points to a family of key-generating mirrors. This division of roles is a route hypothesis, not something determined by `(0,0)` alone.

## 2. H identifies a nearby ciphertext

Look along row 25 from the last cell of `YOU`. Three cells to the right is **H(25,19)** — the rune already present in the retained pair `(L,H)`.

```text
X(25,16) → D(25,17) → W(25,18) → H(25,19)
```

The four consecutive runes form the candidate **ciphertext `X-D-W-H`**. The original full-grid scan reports this exact straight, directed sequence only once.

The surrounding geometry gives another reason to investigate it. The ciphertext sits between two `EA` runes:

```text
EA(25,15) | X-D-W-H | EA(25,20)
```

Those `EA` cells belong to a larger horizontal mirror:

```text
EA(25,10) ── 5 ── EA(25,15) ── 5 ── EA(25,20)
```

This is the grid's **only standard `EA-EA-EA` mirror**. Its three `EA` positions turn out to connect with the other retained value, **L**.

## 3. Three different mirrors generate the same key

Each `EA` in the large mirror is the endpoint of a separate three-rune structure. All three begin with **L**, but have different centers:

| Connected structure | Center transformed by Euler's totient |
|---|---|
| `L(25,4) — C(25,7) — EA(25,10)` | `φ(C=5) = 4 = R` |
| `L(15,15) — I(20,15) — EA(25,15)` | `φ(I=10) = 4 = R` |
| `L(25,8) — EO(25,14) — EA(25,20)` | `φ(EO=12) = 4 = R` |

The respective arm lengths are **3, 5, and 6 cells**. As in the earlier chapters, only the center rune is transformed. Despite their different positions and centers, all three structures produce exactly the same unrotated key:

```text
L-C-EA  → L-R-EA
L-I-EA  → L-R-EA
L-EO-EA → L-R-EA
```

This is the most distinctive part of the primary `SOON` reconstruction. **One large `EA-EA-EA` mirror connects three separate geometric paths to the same key `L-R-EA`.** These are three matching constructions, not three statistically independent proofs.

## 4. Möbius determines the active key

We now have the unrotated key `L-R-EA`. Its Euler totient values give the signature used to calculate the Möbius phase:

```text
φ(L=20)  =  8
φ(R=4)   =  2
φ(EA=28) = 12

Totient signature: (8,2,12)
Möbius signature: (0,-1,0)
Phase:              (0-1+0) mod 3 = 2
```

Phase **2** rotates `L-R-EA` into `EA-L-R`. Repeating the first rune extends the three-rune key over the four ciphertext positions:

```text
L-R-EA → phase 2 → EA-L-R

Active key: EA-L-R-EA
```

The rotation follows from the key's calculated signature; it does not need to be selected by guessing the plaintext.

## 5. Decrypting X-D-W-H

Subtract the active key from the ciphertext, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `X = 14` | `EA = 28` | `14 − 28 ≡ 15` | **S** |
| `D = 23` | `L = 20` | `23 − 20 = 3` | **O** |
| `W = 7` | `R = 4` | `7 − 4 = 3` | **O** |
| `H = 8` | `EA = 28` | `8 − 28 ≡ 9` | **N** |

```text
Ciphertext: X  - D - W - H
Key:        EA - L - R - EA
Plaintext:  S  - O - O - N
```

The result is **SOON**. The primary route ends at **H(25,19)**, and the generated key leaves it with **phase 2**. Both details are important for the next stage.

## 6. Two additional numerical connections

The three key-generating centers are `C`, `I`, and `EO`. Their rune values are **5, 10, and 12**, and all satisfy `φ(n)=4=R`.

There is one more rune value in the same totient class:

```text
φ(n) = 4  →  n ∈ {5,8,10,12}

C = 5    → key-generator center
H = 8    → ciphertext endpoint
I = 10   → key-generator center
EO = 12  → key-generator center
```

Thus **the fourth member of the same totient class is H**, the rune that ends the proposed ciphertext.

A second match appears in the prime-valued Gematria Primus layer. The original hidden pair `(L,H)` has a combined prime weight of **96**, exactly the prime weight of `SOON`:

```text
L + H       = 73 + 23         = 96
S + O + O + N = 53 + 7 + 7 + 29 = 96
```

Both equalities are exact, but they are **additional observations**. Neither is needed for the modular decryption, and neither independently proves that the route was intended.

## 7. A second SOON route starts at the same X

The map also contains a longer path that reaches `SOON` using **different ciphertext and key material**. It begins at the same final `YOU` cell, **X(25,16)**.

That `X` is the center of a vertical `E-X-E` mirror. Its upper rune, **E(24,16)**, also belongs to a diagonal `E-TH-E` mirror:

```text
E(24,16) — X(25,16) — E(26,16)   [vertical E-X-E]
E(22,14) — TH(23,15) — E(24,16)  [diagonal E-TH-E]
```

The shared `E(24,16)` brings the route to **TH(23,15)**. This cell is a useful junction because it is the center of two further mirrors:

```text
X(19,19) — TH(23,15) — X(27,11)
D(22,15) — TH(23,15) — D(24,15)
```

The **X-TH-X branch** can lead to a second ciphertext; the **D-TH-D branch** can lead to its key. These connections are present in the grid, although a general rule compelling the branch choices has not yet been established.

## 8. The hidden branch finds another ciphertext

Follow `X-TH-X` to **X(27,11)**. This `X` is the center of a wide `D-X-D` mirror. Its right `D(27,20)` is, in turn, the center of `P-D-P`:

```text
D(27,2)  — X(27,11) — D(27,20)
P(27,16) — D(27,20) — P(27,24)
```

Notice **P(27,16)**: it is the same `P` used in the preceding `YOU` reconstruction. The opposite outer of the second mirror, **P(27,24)**, begins a straight four-rune sequence on the last row:

```text
P(27,24) → S(27,25) → U(27,26) → W(27,27)
```

This gives the **secondary ciphertext `P-S-U-W`**, another straight, directed sequence reported as unique in the original analysis. Its endpoint is **W(27,27)** — different from the primary `SOON` endpoint `H(25,19)`.

## 9. The other branch generates a second key

Return to the junction **TH(23,15)** and take the `D-TH-D` mirror through **D(22,15)**. Each following cell connects to another mirror:

```text
D(22,15)  — NG(22,17) — D(22,19)
IA(22,16) — D(22,19) — IA(22,22)
IA(16,10) — EA(19,13) — IA(22,16)
```

The chosen outer **IA(22,16)** connects the second and third structures. The last mirror, `IA-EA-IA`, supplies the new key. Transforming its center gives:

```text
EA = 28 → φ(28) = 12 = EO

IA-EA-IA → IA-EO-IA
```

Its phase is calculated in the same way as before:

```text
Totient signature: (18,4,18)
Möbius signature: (0,0,0)
Phase:              0

Active key: IA-EO-IA-IA
```

This key needs no rotation. Extend it to four positions and decrypt `P-S-U-W`:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `P = 13` | `IA = 27` | `13 − 27 ≡ 15` | **S** |
| `S = 15` | `EO = 12` | `15 − 12 = 3` | **O** |
| `U = 1` | `IA = 27` | `1 − 27 ≡ 3` | **O** |
| `W = 7` | `IA = 27` | `7 − 27 ≡ 9` | **N** |

```text
Ciphertext: P  - S  - U  - W
Key:        IA - EO - IA - IA
Plaintext:  S  - O  - O  - N
```

**SOON appears a second time.** The arithmetic works with a different ciphertext, a different mirror network, and a different active key. The longer path does, however, rely on more unproven decisions about which mirror branch to follow.

## 10. Why both SOON endpoints matter

The **primary** reconstruction starts directly from the last cell of `YOU`, derives `(L,H)` using the inherited phase, and produces the key `L-R-EA` through three connected structures. That makes it the more direct proposed continuation.

The **secondary** route is less constrained, but its endpoint **W(27,27)** becomes useful later. In [`16-THEN.md`](./16-THEN.md), the proposed `THEN` route ends at **W(25,27)**. These two endpoints are opposite sides of one vertical mirror:

```text
W(25,27)   ← end of THEN
   |
NG(26,27)  ← center
   |
W(27,27)   ← end of secondary SOON
```

This exact **W-NG-W** connection gives the secondary route a concrete geometric role in the next chapter. It makes that mirror natural to investigate, without establishing that it must be chosen by a universal rule.

The primary endpoint also provides the next chapter's starting coordinate state. Carrying its **phase 2** forward gives:

```text
H(25,19), phase 2

T₂(25,19) = (8,6)
V₂(25,19) = (0,+1) → RIGHT
```

These values are calculated from the primary `SOON` endpoint **before** examining the next ciphertext.

## 11. What remains uncertain

Both proposed decryptions are arithmetically reproducible, and their mirror coordinates can be checked on the grid. The key question is **route selection**.

For the primary route, we still need a general rule explaining why the retained values are assigned as **H → ciphertext endpoint** and **L → key mirrors**. For the secondary route, several mirror transitions remain choices, particularly taking **IA(22,16)** rather than **IA(22,22)** from `IA-D-IA`.

The result is therefore **two structurally different reconstructions of SOON**, not proof that either was the original plaintext intended by Cicada 3301. Their most useful feature is that they leave two well-defined endpoints whose later geometric relationship can be tested.
