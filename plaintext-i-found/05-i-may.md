# 05 — I MAY

This example shows how the preceding **COLD** key determines a movement from the previous ciphertext endpoint, how a vertical node in the **27 × 27 matrix** supplies the next key, and how four ciphertext runes decrypt to `I MAY`.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the directional anchor and three-rune node

The preceding word, **COLD**, uses the final key `U–H–H`, whose rotation phase is **1**. In the project's directional rule, this phase corresponds to:

`V₁ = (+1, +1) → DOWN + RIGHT`

Start at **`A (11,7)`**, the last ciphertext cell used for `COLD`.

The movement distances come from the preceding key's runes:

- **DOWN:** `H = 8 → φ(8) = 4` rows.
- **RIGHT:** `U = 1 → φ(1) = 1` column.

Apply both movements to the anchor:

`A (11,7) → down 4, right 1 → B (15,8)`

The relevant matrix area is:

| Row | Column 7 | Column 8 | Column 9 |
|:---:|:---:|:---:|:---:|
| 13 | J | **NG** | L |
| 14 | G | P | F |
| **15** | S/Z | **B** | EO |
| 16 | AE | C/K | X |
| 17 | D | **NG** | I |

The destination `B (15,8)` lies midway between two `NG` runes in **column 8**:

- **Top:** `NG (13,8)` — 2 rows above `B`.
- **Center:** `B (15,8)` — the rune used to derive the key's center.
- **Bottom:** `NG (17,8)` — 2 rows below `B`.

**Node: `NG–B–NG`.** The directional movement finds its center; the two outer runes complete the vertical arrangement.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer `NG` runes. Replace the center `B` with the rune whose index equals `φ(17)`:

`B = 17 → φ(17) = 16 → T`

The unrotated key is therefore **`NG–T–NG`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| NG | 21 | φ(21) = 12 | μ(12) = 0 |
| T | 16 | φ(16) = 8 | μ(8) = 0 |
| NG | 21 | φ(21) = 12 | μ(12) = 0 |

The **totient signature** is `(12, 8, 12)`, and the **Möbius signature** is `(0, 0, 0)`. The sum of the Möbius values determines the number of cyclic left rotations:

`Rotation = (0 + 0 + 0) mod 3 = 0`

**Final key: `NG–T–NG`.** No rotation is needed.

## 3. Locate the ciphertext start

For this recorded reading, the ciphertext begins at **`TH (26,19)`**, the center of the earlier `H–TH–H` node used to construct the **COLD** key.

This is **not** the new key-node center, `B (15,8)`. The two centers have different roles:

- **`B (15,8)`:** determines the new decryption key `NG–T–NG`.
- **`TH (26,19)`:** is the starting cell of the four-rune ciphertext read for `I MAY`.

From `TH (26,19)`, read **leftward** across four consecutive cells in row 26:

`(26,19) → (26,18) → (26,17) → (26,16)`

The **DOWN + RIGHT** rule above explains how to locate the new key node. The selection of the previous node center as this ciphertext's starting point is a **separate part of the recorded reading**, not a consequence of those two movement distances alone.

## 4. Read and decrypt the ciphertext

Repeat the key `NG–T–NG` over the four ciphertext runes. For each position, subtract the **key's rune index** from the **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (26,19) | TH = 2 | NG = 21 | 2 − 21 ≡ 10 | **I** |
| (26,18) | G = 6 | T = 16 | 6 − 16 ≡ 19 | **M** |
| (26,17) | T = 16 | NG = 21 | 16 − 21 ≡ 24 | **A** |
| (26,16) | E = 18 | NG = 21 | 18 − 21 ≡ 26 | **Y** |

## Result

**Decrypted rune sequence:** `I · M · A · Y`

**Proposed reading: I MAY**

All four runes decrypt directly to `I`, `M`, `A`, and `Y`. The **space is inserted when interpreting the sequence as English**; it is not an additional decrypted rune.

## 5. A matching signature at the preceding endpoint

The starting anchor **`A (11,7)`** is also the center of the vertical `EA–A–EA` arrangement noted at the end of the **COLD** example:

| Row | Column 7 |
|:---:|:---:|
| 10 | **EA** |
| **11** | **A** |
| 12 | **EA** |

Apply `φ` to the rune indices of this earlier arrangement:

`EA–A–EA → (φ(28), φ(24), φ(28)) = (12, 8, 12)`

This is **identical to the totient signature** of the newly derived `NG–T–NG` key:

`NG–T–NG → (φ(21), φ(16), φ(21)) = (12, 8, 12)`

Thus, the **previous ciphertext endpoint** and the **next key** share the same totient signature even though their rune sequences are different. This is an additional numerical correspondence; it is **not required** for the subtraction that produces `I MAY`.
