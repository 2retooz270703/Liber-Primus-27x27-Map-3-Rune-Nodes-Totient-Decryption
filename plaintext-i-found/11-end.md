# 11 — END

This example follows **OF THE**. Its last ciphertext cell leads to a pair of intersecting mirrors, while a diagonal `J–B–J` arrangement supplies the next key. The key decrypts three vertically aligned ciphertext runes as **END**.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the connected three-rune nodes

The preceding **THE** ciphertext ends at **`J (19,16)`**. Move **one cell left** to reach `F (19,15)`:

`J (19,16) → left 1 → F (19,15)`

This `F` is the left endpoint of a horizontal mirror. It intersects a vertical mirror at **`X (19,19)`**:

| Row | Column 15 | Column 19 | Column 23 |
|:---:|:---:|:---:|:---:|
| 15 | | **Y** | |
| **19** | **F** | **X** | **F** |
| 23 | | **Y** | |

The two arrangements are:

- **Horizontal:** `F (19,15) → X (19,19) → F (19,23)`.
- **Vertical:** `Y (15,19) → X (19,19) → Y (23,19)`.

Both have the same center, **`X (19,19)`**, and each outer rune is **4 grid cells** from it along its axis.

A separate diagonal arrangement connects back to the preceding ciphertext endpoint:

`J (19,16) → B (23,12) → J (27,8)`

Here **`B (23,12)`** is the center; each outer `J` is **4 diagonal grid steps** away. This **`J–B–J`** node supplies the decryption key, while the **`F–X–F`** mirror identifies the selected ciphertext start.

## 2. Derive and align the decryption key

### Replace the center rune

Keep both outer `J` runes. Replace the center `B` with the rune whose index equals `φ(17)`:

`B = 17 → φ(17) = 16 → T`

The unrotated key is therefore **`J–T–J`**.

### Calculate its rotation

For each rune of the derived key, apply `φ` to its index and then apply `μ` to the result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| J | 11 | φ(11) = 10 | μ(10) = +1 |
| T | 16 | φ(16) = 8 | μ(8) = 0 |
| J | 11 | φ(11) = 10 | μ(10) = +1 |

The **totient signature** is `(10, 8, 10)`, and the **Möbius signature** is `(+1, 0, +1)`.

The Möbius sum determines the number of cyclic left rotations:

`Rotation = (1 + 0 + 1) mod 3 = 2`

Apply **two cyclic left rotations**:

`J–T–J → T–J–J → J–J–T`

**Final key: `J–J–T`.**

## 3. Locate the ciphertext start

The horizontal `F–X–F` mirror found in Section 1 has **radius 4** in grid steps. From the `F (19,15)` reached next to the preceding ciphertext endpoint, move right through the center to its matching outer `F`:

`F (19,15) → right 4 → X (19,19) → right 4 → F (19,23)`

The **recorded ciphertext start** is therefore **`F (19,23)`**. Read **three cells downward** in column 23:

`F (19,23) → L (20,23) → I (21,23)`

The mirror supplies a concrete geometric connection between the old endpoint and the new start. Selecting the far `F`, reading downward, and taking three runes are the choices recorded for this example; the key calculation alone does **not** prove that this is the only possible reading.

## 4. Read and decrypt the ciphertext

Apply the key `J–J–T` to the three ciphertext runes in order. Subtract each **key rune index** from the corresponding **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (19,23) | F = 0 | J = 11 | 0 − 11 ≡ 18 | **E** |
| (20,23) | L = 20 | J = 11 | 20 − 11 ≡ 9 | **N** |
| (21,23) | I = 10 | T = 16 | 10 − 16 ≡ 23 | **D** |

## Result

**Decrypted rune sequence:** `E · N · D`

**Proposed reading: END**

All three modular subtractions reproduce **END** from the stated cells and rotated key.

## 5. A geometric connection at the ciphertext endpoint

The final ciphertext cell, **`I (21,23)`**, is the right endpoint of a horizontal three-rune mirror:

`I (21,21) → R (21,22) → I (21,23)`

| Row | Column 21 | Column 22 | Column 23 |
|:---:|:---:|:---:|:---:|
| **21** | **I** | **R** | **I** |

The key's Möbius signature is **`(+1, 0, +1)`**, classified as **OUTER** in the project's geometric interpretation. The selected ciphertext ends at an **outer** `I` of the `I–R–I` arrangement, matching that classification.

This is an **additional geometric correspondence**, not an arithmetic step required to decrypt **END**. The OUTER interpretation does not independently establish the uniqueness of the selected ciphertext path.
