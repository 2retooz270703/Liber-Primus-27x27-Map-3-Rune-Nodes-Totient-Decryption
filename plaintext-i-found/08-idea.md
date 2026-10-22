# 08 — IDEA

This example shows how a diagonal three-rune arrangement produces the key for **IDEA**, how the reading continues from the final ciphertext cell of **NOW THE**, and how the new endpoint coincides with the center of another diagonal mirror.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the three-rune node

The previous **NOW THE** ciphertext begins at **`TH (11,16)`** and passes through **`A (14,19)`**. These cells belong to a diagonal arrangement with equal outer runes:

| Row | Column 13 | Column 16 | Column 19 |
|:---:|:---:|:---:|:---:|
| 8 | **A** | | |
| **11** | | **TH** | |
| 14 | | | **A** |

Follow the diagonal **down and right**:

- **Upper endpoint:** `A (8,13)`.
- **Center:** `TH (11,16)` — the rune used to derive the new key's center.
- **Lower endpoint:** `A (14,19)` — also part of the preceding `NOW THE` ciphertext.

The center is **3 diagonal grid steps** from either outer `A`:

`A (8,13) → down-right 3 → TH (11,16) → down-right 3 → A (14,19)`

**Node: `A–TH–A`.** It overlaps the preceding ciphertext at two of its positions.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the outer `A` runes. Replace the center `TH` with the rune whose index equals `φ(2)`:

`TH = 2 → φ(2) = 1 → U`

The unrotated key is therefore **`A–U–A`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| A | 24 | φ(24) = 8 | μ(8) = 0 |
| U | 1 | φ(1) = 1 | μ(1) = +1 |
| A | 24 | φ(24) = 8 | μ(8) = 0 |

The **totient signature** is `(8, 1, 8)`, and the **Möbius signature** is `(0, +1, 0)`. The Möbius sum determines the number of cyclic left rotations:

`Rotation = (0 + 1 + 0) mod 3 = 1`

Apply **one cyclic left rotation**:

`A–U–A → U–A–A`

**Final key: `U–A–A`.**

## 3. Locate the ciphertext start

The lower endpoint of the `A–TH–A` node is **`A (14,19)`**. Moving **one cell down and right** reaches:

`A (14,19) → down-right 1 → J (15,20)`

Importantly, **`J (15,20)` is also the final ciphertext cell of NOW THE**. The new reading therefore begins at the exact position where the previous reading ended.

This one-step connection identifies the **recorded start** of the `IDEA` ciphertext. The node and key calculations above do not, by themselves, establish a general rule that uniquely requires this start or the reading direction below.

## 4. Read and decrypt the ciphertext

From `J (15,20)`, read **three consecutive cells diagonally down and left**: one row down and one column left at each step.

`(15,20) → (16,19) → (17,18)`

Apply the final key `U–A–A` in that order. Subtract each **key rune index** from its **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (15,20) | J = 11 | U = 1 | 11 − 1 ≡ 10 | **I** |
| (16,19) | E = 18 | A = 24 | 18 − 24 ≡ 23 | **D** |
| (17,18) | D = 23 | A = 24 | 23 − 24 ≡ 28 | **EA** |

## Result

**Decrypted rune sequence:** `I · D · EA`

**Proposed reading: IDEA**

`EA` is **one rune** in the 29-rune alphabet, represented by two Latin letters. Thus, three decrypted runes render as the four-letter English word `IDEA`.

## 5. A geometric connection at the ciphertext endpoint

The final ciphertext cell, **`D (17,18)`**, is the center of a diagonal mirror with matching outer runes:

`J (15,20) → D (17,18) → J (19,16)`

| Row | Column 16 | Column 18 | Column 20 |
|:---:|:---:|:---:|:---:|
| 15 | | | **J** |
| **17** | | **D** | |
| 19 | **J** | | |

Each outer `J` is **2 diagonal grid steps** from the center `D`. The first endpoint, **`J (15,20)`**, is also the starting ciphertext cell for `IDEA`.

The derived key's Möbius signature is **`(0, +1, 0)`**, classified as **CENTER** in the project's geometric interpretation. The ciphertext ends at `D (17,18)`, precisely the **center** of the `J–D–J` arrangement.

This is an **additional geometric correspondence**, not a mathematical operation required to decrypt the three ciphertext runes. The CENTER label describes the project's interpretation of the Möbius signature; it does not independently prove the plaintext or reading path.
