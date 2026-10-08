# 03 — TURNS

AS I GO, THE WEATHER TURNS

## 1. Continue from WEATHER

The previous chapter, [`02-WEATHER.md`](./02-WEATHER.md), ends at **E(14,18)**. The cell immediately to its right is **A(14,19)**, which becomes the crossroads for the next stage.

The `WEATHER` key was built from `X-I-X`, with **Möbius phase 2**. It also left us with two related values:

```text
I = 10
φ(I) = 4
```

We use **10** and **4** again to locate the next key. The phase-2 coordinate selector at `A(14,19)` gives the directions:

```text
φ²(14) = 2 → μ(2) = -1
φ²(19) = 6 → μ(6) = +1

V₂(14,19) = (-1,+1) → UP + RIGHT
```

The selector points **up and right**. The inherited numbers supply the distances, while the nearby rune structure shows where they can be applied.

## 2. Find the key through NG

Start at `A(14,19)` and move **RIGHT 4**:

```text
A(14,19) → RIGHT 4 → NG(14,23)
```

This `NG` lies at the center of a horizontal, equally spaced `A-NG-A` structure:

```text
A(14,19) ── 4 ── NG(14,23) ── 4 ── A(14,27)
```

Now apply the other inherited number, **10**, vertically from `NG(14,23)`:

```text
NG(14,23) → UP 10   → H(4,23)
NG(14,23) → DOWN 10 → C(24,23)
```

The resulting vertical structure is:

```text
 H(4,23)
    |
   10
    |
NG(14,23)
    |
   10
    |
 C(24,23)
```

Its outer runes are different, **H** and **C**, so this is not a matching-rune mirror. We use the three runes in their existing order as the key structure: **`H-NG-C`**.

The geometry is the important connection: **RIGHT 4** reaches the central `NG`, and **UP/DOWN 10** identifies the two outer runes. Both distances come from the preceding stage.

## 3. Determine the key's Möbius phase

Calculate the Euler totient of each rune in `H-NG-C`:

```text
φ(H=8)   = 4
φ(NG=21) = 12
φ(C=5)   = 4

Totient signature: (4,12,4)
```

The same signature appears in the related `I-NG-I` structure, giving both rune sequences the numerical pattern **(4,12,4)**.

Next, apply the Möbius function to determine the rotation:

```text
μ(4)  = 0
μ(12) = 0
μ(4)  = 0

Möbius signature: (0,0,0)
Phase:              (0+0+0) mod 3 = 0
```

**Phase 0** leaves `H-NG-C` unchanged. Because the ciphertext contains five runes, repeat the three-rune key from the beginning:

```text
H-NG-C → phase 0 → H-NG-C

Active key: H-NG-C-H-NG
```

## 4. Read the ciphertext and decrypt TURNS

Return to the crossroads **A(14,19)**. Reading straight upward gives five consecutive runes:

```text
A(14,19) → OE(13,19) → N(12,19) → B(11,19) → W(10,19)
```

This gives **ciphertext `A-OE-N-B-W`**. Subtract the active key `H-NG-C-H-NG`, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `A = 24` | `H = 8` | `24 − 8 = 16` | **T** |
| `OE = 22` | `NG = 21` | `22 − 21 = 1` | **U** |
| `N = 9` | `C = 5` | `9 − 5 = 4` | **R** |
| `B = 17` | `H = 8` | `17 − 8 = 9` | **N** |
| `W = 7` | `NG = 21` | `7 − 21 ≡ 15` | **S** |

```text
Ciphertext: A - OE - N - B - W
Key:        H - NG - C - H - NG
Plaintext:  T - U  - R - N - S
```

The result is **TURNS**. The key is built around `NG(14,23)`, while the ciphertext begins at the original crossroads `A(14,19)`. Both are connected by the inherited distance **4**.

## 5. A numerical link to I-NG-I

There is a useful relationship between the newly constructed key and a mirror of the form `I-NG-I`:

```text
H-NG-C → φ → (4,12,4)
I-NG-I → φ → (4,12,4)
```

The outer runes differ, but their totient values are equal:

```text
φ(H=8)  = 4
φ(I=10) = 4
φ(C=5)  = 4
```

This explains why **H-NG-C** and **I-NG-I** produce the same signature. The equality also accounts for their common neutral Möbius pattern `(0,0,0)`.

## 6. NG supplies the next movement to COLD

The route now returns to the **A(14,19)** crossroads rather than starting from the last ciphertext rune `W(10,19)`. The center of the `TURNS` key structure is **NG = 21**. Applying Euler's totient gives a new value:

```text
NG = 21
φ(21) = 12
```

The current **phase 0** gives a different directional selector at the crossroads:

```text
V₀(14,19) = (+1,-1) → DOWN + LEFT
```

Using **12** in these two directions reaches the structures used for the next word:

```text
A(14,19) → DOWN 12 → TH(26,19)
A(14,19) → LEFT 12 → G(14,7)
```

**TH(26,19)** is the center of the next key-generating `H-TH-H` mirror, while **G(14,7)** begins the next ciphertext. Thus, the same `NG` that sits at the center of the `TURNS` key also supplies the distance that connects this stage to **COLD**, explained in [`04-COLD.md`](./04-COLD.md).
