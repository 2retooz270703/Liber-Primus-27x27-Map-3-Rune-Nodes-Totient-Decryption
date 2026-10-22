# 04 — COLD

This example shows how the preceding **TURNS** key supplies a direction and movement distance, how a three-rune node in the **27 × 27 matrix** produces the next key, and how four ciphertext runes decrypt to `COLD`.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the directional anchor and three-rune node

The preceding word, **TURNS**, uses the final key `H–NG–C`, whose rotation phase is **0**. In the project's directional rule, this phase corresponds to:

`V₀ = (+1, −1) → DOWN + LEFT`

Apply this direction at the rune **`A (14,19)`**, the starting cell used for `TURNS`.

The movement distance comes from the preceding key's center rune, `NG`:

`NG = 21 → φ(21) = 12`

Move **12 rows down** from `A (14,19)` to `TH (26,19)`. The relevant matrix area is:

| Row | Column 18 | Column 19 | Column 20 |
|:---:|:---:|:---:|:---:|
| 25 | W | **H** | EA |
| **26** | G | **TH** | H |
| 27 | EA | **H** | D |

Read the three cells in **column 19**:

- **Top:** `H (25,19)`.
- **Center:** `TH (26,19)` — the rune used to derive the key's center.
- **Bottom:** `H (27,19)`.

**Node: `H–TH–H`.** Its center is exactly 12 rows below the directional anchor.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer `H` runes. Replace `TH` with the rune whose index equals `φ(2)`:

`TH = 2 → φ(2) = 1 → U`

The unrotated key is therefore **`H–U–H`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to that result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| H | 8 | φ(8) = 4 | μ(4) = 0 |
| U | 1 | φ(1) = 1 | μ(1) = +1 |
| H | 8 | φ(8) = 4 | μ(4) = 0 |

The **totient signature** is `(4, 1, 4)`, and the **Möbius signature** is `(0, +1, 0)`. The sum of the Möbius values determines the number of cyclic left rotations:

`Rotation = (0 + 1 + 0) mod 3 = 1`

Apply **one cyclic left rotation**:

`H–U–H → U–H–H`

**Final key: `U–H–H`.**

## 3. Locate the ciphertext start

The same distance, **12**, is used in the **LEFT** direction from the anchor `A (14,19)`:

`(14,19) → 12 cells left → (14,7)`

The rune at **`(14,7)` is `G`**. This is the first ciphertext rune.

The two movements have different purposes:

- **DOWN 12:** locates the center `TH (26,19)` of the `H–TH–H` key node.
- **LEFT 12:** locates the ciphertext start `G (14,7)`.

From `G (14,7)`, the recorded ciphertext reading goes **upward** through four consecutive cells in column 7:

`(14,7) → (13,7) → (12,7) → (11,7)`

The **DOWN + LEFT** rule locates the node and start; it should not be confused with the **UP** direction used to read the ciphertext.

## 4. Read and decrypt the ciphertext

Repeat the key `U–H–H` over the four ciphertext runes. For each position, subtract the **key's rune index** from the **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (14,7) | G = 6 | U = 1 | 6 − 1 ≡ 5 | **C** |
| (13,7) | J = 11 | H = 8 | 11 − 8 ≡ 3 | **O** |
| (12,7) | EA = 28 | H = 8 | 28 − 8 ≡ 20 | **L** |
| (11,7) | A = 24 | U = 1 | 24 − 1 ≡ 23 | **D** |

## Result

**Decrypted rune sequence:** `C · O · L · D`

**Proposed reading: COLD**

All four decrypted runes correspond directly to the four letters of `COLD`. No multi-letter rune expansion is required.

## 5. A connection at the ciphertext endpoint

The final ciphertext cell, **`A (11,7)`**, is the center of a second vertical three-rune arrangement:

| Row | Column 7 |
|:---:|:---:|
| 10 | **EA** |
| **11** | **A** |
| 12 | **EA** |

This produces **`EA–A–EA`**, centered on the last cell read during the `COLD` decryption.

The key `U–H–H` has the Möbius signature **`(0, +1, 0)`**, which the project interprets as a **CENTER** state. The endpoint falling at the center of `EA–A–EA` is therefore an additional geometric correspondence.

This observation is **not needed for the modular subtraction** that yields `COLD`; it is a separate positional connection worth tracking across the sequence.
