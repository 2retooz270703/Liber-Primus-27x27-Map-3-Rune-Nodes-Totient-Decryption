# 01 — AS I GO, THE

This example shows how a three-rune node in the **27 × 27 matrix** yields a key, a starting position, and seven decrypted runes.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the three-rune node

The relevant section of the matrix is:

| Row | Column 11 | Column 12 | Column 13 |
|:---:|:---:|:---:|:---:|
| 12 | M | H | M |
| **13** | **AE** | **J** | **EA** |
| 14 | EO | AE | OE |

Read the three adjacent cells in **row 13**:

- **Left:** `AE (13,11)` — the movement anchor.
- **Center:** `J (13,12)` — the rune used to derive the key's center.
- **Right:** `EA (13,13)`.

**Node:** `AE–J–EA`.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer runes. Replace the center `J` with the rune whose index equals `φ(11)`:

`J = 11 → φ(11) = 10 → I`

The unrotated key is therefore **`AE–I–EA`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| AE | 25 | φ(25) = 20 | μ(20) = 0 |
| I | 10 | φ(10) = 4 | μ(4) = 0 |
| EA | 28 | φ(28) = 12 | μ(12) = 0 |

The **Möbius signature** is `(0, 0, 0)`. Its sum determines the number of cyclic left rotations:

`Rotation = (0 + 0 + 0) mod 3 = 0`

**Final key: `AE–I–EA`.** No rotation is needed.

## 3. Locate the ciphertext start

For this node, the recorded movement uses the original center-rune index (`J = 11`) and the derived center-rune index (`I = 10`):

`Distance = φ(11) + φ(10) = 10 + 4 = 14`

Start from the **leftmost node cell**, `AE (13,11)`, and move **14 cells to the right**:

`(13,11) → (13,25)`

The rune at **`(13,25)` is `L`**. This is the first ciphertext rune.

## 4. Read and decrypt the ciphertext

Read from `(13,25)` **left to right**. After column 27, continue at **column 1 of the next row**:

`(13,25) → (13,26) → (13,27) → (14,1) → (14,2) → (14,3) → (14,4)`

Repeat the key `AE–I–EA` over these seven ciphertext runes. For each position, subtract the **key's rune index** from the **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (13,25) | L = 20 | AE = 25 | 20 − 25 ≡ 24 | **A** |
| (13,26) | AE = 25 | I = 10 | 25 − 10 ≡ 15 | **S** |
| (13,27) | N = 9 | EA = 28 | 9 − 28 ≡ 10 | **I** |
| (14,1) | TH = 2 | AE = 25 | 2 − 25 ≡ 6 | **G** |
| (14,2) | P = 13 | I = 10 | 13 − 10 ≡ 3 | **O** |
| (14,3) | U = 1 | EA = 28 | 1 − 28 ≡ 2 | **TH** |
| (14,4) | X = 14 | AE = 25 | 14 − 25 ≡ 18 | **E** |

## Result

**Decrypted rune sequence:** `A · S · I · G · O · TH · E`

**Proposed reading: AS I GO, THE**

`TH` is **one rune** in the 29-rune alphabet. The spaces and comma are added for readability; they are not produced by the subtraction itself.
