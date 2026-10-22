# 06 — CRY

This example shows how the final ciphertext cell of **I MAY** identifies a new three-rune node, how that node produces the next key, and how three ciphertext runes decrypt to `CRY`. It also records a geometric connection at the new ciphertext endpoint.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the three-rune node

The preceding ciphertext for **I MAY** ends at **`E (26,16)`**. That cell is the lower endpoint of a vertical `E–X–E` arrangement.

The relevant section of the matrix is:

| Row | Column 15 | Column 16 | Column 17 |
|:---:|:---:|:---:|:---:|
| 24 | D | **E** | F |
| **25** | EA | **X** | D |
| **26** | EA | **E** | T |

Read the three cells in **column 16**:

- **Top:** `E (24,16)`.
- **Center:** `X (25,16)` — the rune used to derive the new key's center.
- **Bottom:** `E (26,16)` — the final ciphertext cell of **I MAY**.

**Node: `E–X–E`.** The previous ciphertext ends on one of its outer runes, linking the two readings through a shared matrix position.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer `E` runes. Replace the center `X` with the rune whose index equals `φ(14)`:

`X = 14 → φ(14) = 6 → G`

The unrotated key is therefore **`E–G–E`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| E | 18 | φ(18) = 6 | μ(6) = +1 |
| G | 6 | φ(6) = 2 | μ(2) = −1 |
| E | 18 | φ(18) = 6 | μ(6) = +1 |

The **totient signature** is `(6, 2, 6)`, and the **Möbius signature** is `(+1, −1, +1)`. The sum of the Möbius values determines the number of cyclic left rotations:

`Rotation = (1 − 1 + 1) mod 3 = 1`

Apply **one cyclic left rotation**:

`E–G–E → G–E–E`

**Final key: `G–E–E`.**

## 3. Locate the ciphertext start

The movement distance comes from the **original center rune** of the `E–X–E` node:

`X = 14 → φ(14) = 6`

Start at **`X (25,16)`** and move **6 rows upward**, staying in column 16:

`(25,16) → 6 cells up → (19,16)`

The rune at **`(19,16)` is `J`**. This is the starting cell of the recorded `CRY` ciphertext.

It is also the center of another vertical arrangement, **`OE–J–OE`**:

| Row | Column 16 |
|:---:|:---:|
| 18 | **OE** |
| **19** | **J** |
| 20 | **OE** |

Thus, the **6-cell movement** lands exactly on the center of a second three-rune node. The `E–X–E` node supplies the key; `J (19,16)` supplies the ciphertext start. These are different roles.

## 4. Read and decrypt the ciphertext

From `J (19,16)`, read **three consecutive cells upward** in column 16:

`(19,16) → (18,16) → (17,16)`

Apply the key `G–E–E` in that order. For each cell, subtract the **key's rune index** from the **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (19,16) | J = 11 | G = 6 | 11 − 6 ≡ 5 | **C** |
| (18,16) | OE = 22 | E = 18 | 22 − 18 ≡ 4 | **R** |
| (17,16) | S = 15 | E = 18 | 15 − 18 ≡ 26 | **Y** |

## Result

**Decrypted rune sequence:** `C · R · Y`

**Proposed reading: CRY**

All three ciphertext runes decrypt directly to the letters `C`, `R`, and `Y`. No spacing or multi-letter rune expansion is required.

## 5. A geometric connection at the ciphertext endpoint

The final ciphertext cell, **`S (17,16)`**, is an outer endpoint of a horizontal **`S–IA–S`** arrangement in row 17:

| Row | Column 4 | Column 10 | Column 16 |
|:---:|:---:|:---:|:---:|
| **17** | **S** | **IA** | **S** |

The center is **`IA (17,10)`**. Both outer runes are exactly **6 columns** from it:

`10 − 4 = 6` and `16 − 10 = 6`

The center rune also yields **6** after two applications of Euler's totient function:

`IA = 27 → φ(27) = 18 → φ(18) = 6`

In other words, **`φ²(27) = 6`**, matching both the spacing of the `S–IA–S` mirror and the **6-cell movement** used to locate the ciphertext start in Section 3.

*Matrix-label note:* The interactive map displays these rune names as `S/Z` and `IA/IO`; this document uses the shortened labels `S` and `IA`, consistent with the decryption tables.

This is an **additional geometric and numerical correspondence**, not a step required for the modular subtraction that produces `CRY`.
