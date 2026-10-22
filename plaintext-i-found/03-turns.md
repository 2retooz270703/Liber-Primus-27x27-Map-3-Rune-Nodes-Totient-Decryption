# 03 — TURNS

This example shows how the preceding **WEATHER** key provides a directional rule, how the geometry of the **27 × 27 matrix** identifies a new three-rune key, and how five ciphertext runes decrypt to `TURNS`.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the directional anchor and key

The preceding word, **WEATHER**, uses the final key `X–X–I`, whose rotation phase is **2**. In the project's directional rule, this phase corresponds to:

`V₂ = (−1, +1) → UP + RIGHT`

Apply this direction at the rune **`A (14,19)`**. The relevant matrix positions are:

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| **4** | — | **H** | — |
| **14** | **A** | **NG** | **A** |
| **24** | — | **C** | — |

There are two intersecting arrangements:

- **Horizontal mirror:** `A (14,19) – NG (14,23) – A (14,27)`. The center is 4 columns from either `A`.
- **Vertical key:** `H (4,23) – NG (14,23) – C (24,23)`. The outer runes are 10 rows above and below `NG`.

The movement distances come from the previous key's rune `I`:

`I = 10 → φ(10) = 4`

Starting at `A (14,19)`, move **4 cells right** to `NG (14,23)`. From that center, move **10 cells up** to `H (4,23)`; the corresponding position **10 cells down** is `C (24,23)`.

Read the vertical sequence **top to bottom** to obtain the new key: **`H–NG–C`**.

## 2. Derive and align the decryption key

### Calculate the rotation

For each rune of `H–NG–C`, apply `φ` to its index, then apply `μ` to the result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| H | 8 | φ(8) = 4 | μ(4) = 0 |
| NG | 21 | φ(21) = 12 | μ(12) = 0 |
| C | 5 | φ(5) = 4 | μ(4) = 0 |

The **totient signature** is `(4, 12, 4)`, and the **Möbius signature** is `(0, 0, 0)`. The Möbius sum determines the number of cyclic left rotations:

`Rotation = (0 + 0 + 0) mod 3 = 0`

**Final key: `H–NG–C`.** No rotation is needed.

## 3. Locate the ciphertext start

The ciphertext starts at the directional anchor **`A (14,19)`**, not at the center of the vertical key, `NG (14,23)`.

Following the **UP** direction, read five consecutive cells in **column 19**, decreasing the row number by 1 each time:

`(14,19) → (13,19) → (12,19) → (11,19) → (10,19)`

The **RIGHT** movement described in Section 1 locates the key geometry. It does **not** change the starting cell of this ciphertext reading.

## 4. Read and decrypt the ciphertext

Repeat the key `H–NG–C` over the five ciphertext runes. For each position, subtract the **key's rune index** from the **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (14,19) | A = 24 | H = 8 | 24 − 8 ≡ 16 | **T** |
| (13,19) | OE = 22 | NG = 21 | 22 − 21 ≡ 1 | **U** |
| (12,19) | N = 9 | C = 5 | 9 − 5 ≡ 4 | **R** |
| (11,19) | B = 17 | H = 8 | 17 − 8 ≡ 9 | **N** |
| (10,19) | W = 7 | NG = 21 | 7 − 21 ≡ 15 | **S** |

## Result

**Decrypted rune sequence:** `T · U · R · N · S`

**Proposed reading: TURNS**

All five decrypted runes correspond directly to the five letters of `TURNS`. No spacing or multi-letter rune expansion is required.
