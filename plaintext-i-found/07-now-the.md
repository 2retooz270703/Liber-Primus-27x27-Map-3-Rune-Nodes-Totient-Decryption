# 07 — NOW THE

This example shows how the **CRY** construction supplies a six-cell movement, how the vertical `OE–J–OE` node produces a new key, and how five ciphertext runes decrypt to `NOW THE`. It also records geometric and numerical connections between this reading and **CRY**.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function. Prime values refer to **Gematria Primus (GP)**, not rune indices.

## 1. Find the three-rune node

In the preceding **CRY** example, the center of the `E–X–E` node is **`X (25,16)`**. Its totient gives the movement distance:

`X = 14 → φ(14) = 6`

Move **6 rows upward** in column 16:

`X (25,16) → up 6 → J (19,16)`

The destination is the center of a vertical three-rune arrangement:

| Row | Column 15 | Column 16 | Column 17 |
|:---:|:---:|:---:|:---:|
| 18 | X | **OE** | R |
| **19** | F | **J** | A |
| 20 | I | **OE** | M |

Read the cells in **column 16**:

- **Top:** `OE (18,16)`.
- **Center:** `J (19,16)` — the rune used to derive the next key's center.
- **Bottom:** `OE (20,16)`.

**Node: `OE–J–OE`.** The same six-cell movement that located the `CRY` ciphertext start now identifies the node used for this key.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer `OE` runes. Replace `J` with the rune whose index equals `φ(11)`:

`J = 11 → φ(11) = 10 → I`

The unrotated key is therefore **`OE–I–OE`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| OE | 22 | φ(22) = 10 | μ(10) = +1 |
| I | 10 | φ(10) = 4 | μ(4) = 0 |
| OE | 22 | φ(22) = 10 | μ(10) = +1 |

The **totient signature** is `(10, 4, 10)`, and the **Möbius signature** is `(+1, 0, +1)`. Their Möbius sum determines the number of cyclic left rotations:

`Rotation = (1 + 0 + 1) mod 3 = 2`

Apply **two cyclic left rotations**:

`OE–I–OE → I–OE–OE → OE–OE–I`

**Final key: `OE–OE–I`.**

## 3. Locate the ciphertext start

The preceding **CRY** ciphertext ends at **`S (17,16)`**. Apply the same distance, **6**, upward from this endpoint:

`S (17,16) → up 6 → TH (11,16)`

The rune at **`(11,16)` is `TH`**. This is the start of the recorded `NOW THE` ciphertext.

The two six-cell movements have different purposes:

- **`X (25,16) → J (19,16)`:** finds the center of the new key node.
- **`S (17,16) → TH (11,16)`:** finds the start of the new ciphertext.

The **distance** is calculated from `φ(X) = 6`. Applying it to the preceding ciphertext endpoint to select the next start is part of the project's recorded route.

## 4. Read and decrypt the ciphertext

From `TH (11,16)`, read **five consecutive cells diagonally down and right**: one row down and one column right at each step.

`(11,16) → (12,17) → (13,18) → (14,19) → (15,20)`

Repeat the final key `OE–OE–I` across these cells. Subtract each **key rune index** from the corresponding **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (11,16) | TH = 2 | OE = 22 | 2 − 22 ≡ 9 | **N** |
| (12,17) | AE = 25 | OE = 22 | 25 − 22 ≡ 3 | **O** |
| (13,18) | B = 17 | I = 10 | 17 − 10 ≡ 7 | **W** |
| (14,19) | A = 24 | OE = 22 | 24 − 22 ≡ 2 | **TH** |
| (15,20) | J = 11 | OE = 22 | 11 − 22 ≡ 18 | **E** |

## Result

**Decrypted rune sequence:** `N · O · W · TH · E`

**Proposed reading: NOW THE**

`TH` is **one rune** in the 29-rune alphabet. The space between `NOW` and `THE` is added when rendering the sequence as English; it is not a separate decrypted symbol.

## 5. Connections in the matrix

These are **additional correspondences**, not operations needed to produce the plaintext by modular subtraction.

### Two mirrors share the same center and distance

The final ciphertext rune of **CRY**, `S (17,16)`, belongs to a horizontal mirror:

`S (17,4) → IA (17,10) → S (17,16)`

The new ciphertext begins at `TH (11,16)`, which belongs to a diagonal mirror with the **same center**:

`TH (11,16) → IA (17,10) → TH (23,4)`

Both arrangements are centered at **`IA (17,10)`**. In the first, each endpoint is **6 horizontal cells** from the center; in the second, each endpoint is **6 diagonal steps** from it.

Applying the totient function twice to the center rune's index also gives six:

`IA = 27 → φ(27) = 18 → φ(18) = 6`

Thus, **`φ²(27) = 6`**, matching the step count in both mirrors and the movement used in Section 3. Here, *distance 6* means six grid steps along the relevant axis or diagonal, not the Euclidean length of a diagonal.

### CRY and NOW THE have the same GP sum

Using **Gematria Primus prime values** for the *decrypted runes*:

| Reading | Rune-by-rune GP values | Sum |
|:---|:---|:---:|
| **CRY** | C = 13, R = 11, Y = 103 | **127** |
| **NOW THE** | N = 29, O = 7, W = 19, TH = 5, E = 67 | **127** |

`13 + 11 + 103 = 29 + 7 + 19 + 5 + 67 = 127`

**127 is the 31st prime.** The transformed center rune of the new key, `I`, also has **GP value 31**. This relates the common plaintext GP sum to the central rune of `OE–I–OE`, but it does not determine the decryption key or the reading direction on its own.

### The OUTER interpretation at the endpoint

The key has Möbius signature **`(+1, 0, +1)`**, classified as **OUTER** in the project's geometric interpretation.

The final ciphertext cell, **`J (15,20)`**, is an outer endpoint of the diagonal arrangement:

`J (15,20) → D (17,18) → J (19,16)`

Each step moves **2 rows down and 2 columns left**. This gives the OUTER classification a corresponding endpoint in the matrix. It is an **interpretive geometric match**, not an additional requirement for decrypting `NOW THE`.
