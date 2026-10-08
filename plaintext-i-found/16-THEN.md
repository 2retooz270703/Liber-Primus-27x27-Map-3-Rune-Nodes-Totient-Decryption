# 16 — THEN

AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH. SEE YOU SOON, THEN.

## 1. Start from the end of SOON

The primary `SOON` route ends at **H(25,19)**. Its key already established **Möbius phase 2** in the previous chapter. We carry that phase forward rather than choosing a new one for `THEN`.

Apply phase 2 to the endpoint coordinates:

```text
φ²(25) = 8   → μ(8) = 0
φ²(19) = 6   → μ(6) = +1

T₂(25,19) = (8,6)
V₂(25,19) = (0,+1) → RIGHT
```

We now have a **RIGHT-compatible direction** and two retained values: **8 and 6**. The direction comes from the existing selector; their use as distances is the route hypothesis tested below.

## 2. The numbers point to both ends of the ciphertext

Starting at `H(25,19)`, both distances land on row 25:

- **RIGHT 6** reaches `L(25,25)`.
- **RIGHT 8** reaches `W(25,27)`.

The three consecutive runes between those two positions are:

```text
L(25,25) → T(25,26) → W(25,27)
```

That gives the candidate **ciphertext `L-T-W`**. In the full grid, this exact directed straight three-rune sequence occurs only once.

The striking detail is that **both values from the previous phase fit the same short segment**: `6` reaches its beginning, and `8` reaches its end. This is an exact geometric match, though a universal rule requiring these two particular distances is not yet proven.

## 3. A mirror exactly halfway to the ciphertext

The distance from `H(25,19)` to `L(25,25)` is six cells. Its midpoint is therefore `IA(25,22)`, three cells from either end:

```text
H(25,19) ── 3 ── IA(25,22) ── 3 ── L(25,25)
                       |
                   IA(26,22)  ← center
                       |
                   IA(27,22)
```

Those three vertical runes form **IA-IA-IA** — the only standard mirror of this exact type in the matrix. Its position gives a concrete reason to investigate it as the key source.

Transform the center with Euler's totient:

```text
IA = 27
φ(27) = 18 = E

IA-IA-IA → IA-E-IA
```

Now calculate the key's Möbius phase:

```text
Totient signature: (18,6,18)
Möbius signature: (0,+1,0)
Phase:              1

IA-E-IA → E-IA-IA
```

The resulting **active key is `E-IA-IA`**. Phase **2** located the ciphertext; phase **1** is calculated separately to rotate this new key.

## 4. Decrypting L-T-W

Subtract the generated key from the ciphertext, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `L = 20` | `E = 18` | `20 − 18 = 2` | **TH** |
| `T = 16` | `IA = 27` | `16 − 27 ≡ 18` | **E** |
| `W = 7` | `IA = 27` | `7 − 27 ≡ 9` | **N** |

```text
Ciphertext: L  - T  - W
Key:        E  - IA - IA
Plaintext:  TH - E  - N
```

The result is **THEN**. It is written with four Latin letters but consists of **three runes**, because `TH` is a single rune.

## 5. THEN connects to the hidden SOON route

The last ciphertext rune of `THEN` is **W(25,27)**. In [`15-SOON.md`](./15-SOON.md), the **secondary, hidden reconstruction of SOON** ends at **W(27,27)**.

These endpoints sit on opposite sides of `NG(26,27)`:

```text
W(25,27)   ← end of THEN
   |
NG(26,27)  ← center
   |
W(27,27)   ← end of secondary SOON
```

Together they form the mirror **W-NG-W**. This makes it a natural mirror to examine next: it directly joins the new endpoint to an endpoint already found through a different `SOON` route. The connection is exact, even though the pattern `W-NG-W` itself is not globally unique.

Its center produces another phase:

```text
NG = 21 → φ(21) = 12 = EO
W-NG-W → W-EO-W

Totient signature: (6,4,6)
Möbius signature: (+1,0,+1)
Phase:              2
```

**If this connecting mirror is used for the next phase**, the end of `THEN` gives:

```text
T₂(25,27) = (8,6)
V₂(25,27) = (0,+1) → RIGHT
```

That is **the same state** obtained at the end of primary `SOON`: phase **2**, totient pair **(8,6)**, and Möbius pair **(0,+1)**. The two endpoints are also exactly **8 columns apart**.

This return is **conditional**, not automatic. The final `W(25,27)` also belongs to a `W-W-W` mirror that produces phase **1**; simply retaining the active phase of `THEN` also gives a different coordinate state. What makes `W-NG-W` worth examining is its direct connection to the previously documented secondary `SOON` route — not a proven rule that it must always be selected.

## 6. One more numerical connection

The rune-index totals of the three preceding words add up to:

```text
SEE + YOU + SOON = 51 + 30 + 30 = 111
φ(111) = 72
```

The generated key for `THEN` has exactly the same sum:

```text
E + IA + IA = 18 + 27 + 27 = 72
```

This is an exact numerical relationship, but it was noticed **after** finding `THEN`. It is an additional observation, not an independent prediction.

## 7. Conclusion

The proposed continuation links several concrete observations: the phase inherited from `SOON`, two distances matching one ciphertext, a midpoint mirror that generates the decryption key, and a final mirror joining `THEN` to the hidden secondary `SOON` route.

The coordinates and decryption are reproducible. What remains open is whether a **single, predetermined selection rule** would force these same distances and mirrors without knowing the word in advance. For now, **THEN is a well-supported research candidate, not verified original Cicada 3301 plaintext**.
