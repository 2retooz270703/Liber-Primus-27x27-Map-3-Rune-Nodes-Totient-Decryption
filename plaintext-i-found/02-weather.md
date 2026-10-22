# 02 — WEATHER

This example shows how a three-rune node in the **27 × 27 matrix** yields a key, a starting position at the matrix center, and five decrypted runes. It also records three geometric connections associated with the result.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the three-rune node

The relevant section of the matrix is:

| Row | Column 4 | Column 5 | Column 6 |
|:---:|:---:|:---:|:---:|
| 13 | C/K | B | L |
| **14** | **X** | **OE** | **X** |
| 15 | NG | AE | C/K |

Read the three adjacent cells in **row 14**:

- **Left:** `X (14,4)` — the movement anchor.
- **Center:** `OE (14,5)` — the rune used to derive the key's center.
- **Right:** `X (14,6)`.

**Node:** `X–OE–X`.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer runes. Replace the center `OE` with the rune whose index equals `φ(22)`:

`OE = 22 → φ(22) = 10 → I`

The unrotated key is therefore **`X–I–X`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| X | 14 | φ(14) = 6 | μ(6) = +1 |
| I | 10 | φ(10) = 4 | μ(4) = 0 |
| X | 14 | φ(14) = 6 | μ(6) = +1 |

The **Möbius signature** is `(+1, 0, +1)`. Its sum determines the number of cyclic left rotations:

`Rotation = (1 + 0 + 1) mod 3 = 2`

Apply **two cyclic left rotations** to the unrotated key:

`X–I–X → I–X–X → X–X–I`

**Final key: `X–X–I`.**

## 3. Locate the ciphertext start

For this node, the recorded movement uses the original center-rune index (`OE = 22`):

`Distance = φ(22) = 10`

Start from the **leftmost node cell**, `X (14,4)`, and move **10 cells to the right**:

`(14,4) → (14,14)`

The rune at **`(14,14)` is `NG`**. This is the first ciphertext rune.

This position is also the **exact center of the 27 × 27 matrix**: row 14 and column 14 each have 13 cells on either side.

## 4. Read and decrypt the ciphertext

Read five consecutive cells **left to right**, starting at `(14,14)`:

`(14,14) → (14,15) → (14,16) → (14,17) → (14,18)`

Repeat the key `X–X–I` over these five ciphertext runes. For each position, subtract the **key's rune index** from the **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (14,14) | NG = 21 | X = 14 | 21 − 14 ≡ 7 | **W** |
| (14,15) | P = 13 | X = 14 | 13 − 14 ≡ 28 | **EA** |
| (14,16) | EO = 12 | I = 10 | 12 − 10 ≡ 2 | **TH** |
| (14,17) | O = 3 | X = 14 | 3 − 14 ≡ 18 | **E** |
| (14,18) | E = 18 | X = 14 | 18 − 14 ≡ 4 | **R** |

## Result

**Decrypted rune sequence:** `W · EA · TH · E · R`

**Proposed reading: WEATHER**

`EA` and `TH` are each **one rune** in the 29-rune alphabet. Together, the five decrypted runes spell the seven-letter word `WEATHER`.

## 5. Connections in the matrix

The following observations concern the **positions of runes in the matrix**, not additional steps required for the modular subtraction above.

### A matching sequence directly above the ciphertext

The first three decrypted runes, `W–EA–TH`, also occur together in **row 13, columns 14–16**. They sit directly above the first three ciphertext cells, `NG–P–EO`, in **row 14, columns 14–16**.

| Row | Column 14 | Column 15 | Column 16 |
|:---:|:---:|:---:|:---:|
| 13 | **W** | **EA** | **TH** |
| 14 | **NG** | **P** | **EO** |

Thus, the decrypted opening `W–EA–TH` has a spatial counterpart **one row above** its ciphertext positions.

### A diagonal E–NG–E mirror

A separate diagonal passes through these cells:

`E (6,10) → NG (10,14) → E (14,18)`

Each step moves **4 rows down and 4 columns right**, making `NG (10,14)` the midpoint of an `E–NG–E` arrangement.

The last cell, **`E (14,18)`**, is also the **fifth and final ciphertext cell** used to decrypt `WEATHER`. Here `E` is the *ciphertext* rune; it decrypts to `R`.

The project's recorded search identifies this as the **only E–NG–E mirror across the axes and distances examined**. That uniqueness is a reported search result, separate from the arithmetic demonstration.

### The OUTER interpretation

The key's Möbius signature is **`(+1, 0, +1)`**. In the project's geometric interpretation, this is classified as **OUTER**.

The final ciphertext cell, `E (14,18)`, is indeed **one of the two outer endpoints** of the diagonal `E–NG–E` mirror. This connects the project's OUTER label to a specific position in the matrix; it is an interpretive connection rather than an additional decryption operation.
