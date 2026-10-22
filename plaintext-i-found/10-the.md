# 10 — THE

This example follows **OF** by switching from the diagonal `J–D–J` mirror to the vertical `OE–J–OE` mirror. Both nodes meet at **`J (19,16)`**. The vertical node supplies a key that decrypts two adjacent ciphertext runes as **THE**.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` is Euler's totient function; `μ` is the Möbius function.

## 1. Find the connected three-rune nodes

The previous **OF** example uses the diagonal mirror:

`J (15,20) → D (17,18) → J (19,16)`

Its lower `J (19,16)` is also the center of a vertical mirror:

`OE (18,16) → J (19,16) → OE (20,16)`

| Row | Column 15 | Column 16 | Column 17 |
|:---:|:---:|:---:|:---:|
| 18 | X | **OE** | R |
| **19** | F | **J** | **A** |
| 20 | I | **OE** | M |

The two mirrors share **`J (19,16)`**, but they play different roles in the consecutive examples:

- **OF:** the diagonal `J–D–J` supplies the key.
- **THE:** the vertical `OE–J–OE` supplies the key.

**Key-generating node: `OE–J–OE`.** Its center is `J (19,16)`, with the two `OE` runes immediately above and below it.

## 2. Derive and align the decryption key

### Replace the center rune

Keep both outer `OE` runes. Replace the center `J` with the rune whose index equals `φ(11)`:

`J = 11 → φ(11) = 10 → I`

The unrotated key is therefore **`OE–I–OE`**.

### Calculate its rotation

For each rune in the derived key, first apply `φ` to its index, then apply `μ` to the result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| OE | 22 | φ(22) = 10 | μ(10) = +1 |
| I | 10 | φ(10) = 4 | μ(4) = 0 |
| OE | 22 | φ(22) = 10 | μ(10) = +1 |

The **totient signature** is `(10, 4, 10)`, and the **Möbius signature** is `(+1, 0, +1)`.

The Möbius sum determines the number of cyclic left rotations:

`Rotation = (1 + 0 + 1) mod 3 = 2`

Apply two left rotations:

`OE–I–OE → I–OE–OE → OE–OE–I`

**Final repeating key: `OE–OE–I`.** Because the selected ciphertext contains only **two runes**, the decryption uses the first two key positions: **`OE–OE`**. The final `I` is not used.

## 3. Locate the ciphertext start

From the shared center **`J (19,16)`**, move **one cell right**:

`J (19,16) → right 1 → A (19,17)`

The recorded ciphertext begins at **`A (19,17)`** and is read **one cell left**, returning to the shared center:

`A (19,17) → J (19,16)`

This connects the new reading directly to the same `J` used in the geometry of **OF**. However, the one-cell movement, leftward direction, and two-rune length are the choices documented in this example; the key calculation alone does **not** establish them as unique.

## 4. Read and decrypt the ciphertext

Apply the first two positions of the rotated key `OE–OE–I`, subtracting each **key rune index** from its **ciphertext rune index**, modulo 29:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (19,17) | A = 24 | OE = 22 | 24 − 22 ≡ 2 | **TH** |
| (19,16) | J = 11 | OE = 22 | 11 − 22 ≡ 18 | **E** |

Here, **`TH` is a single rune** in the 29-rune alphabet, so two decrypted runes yield the three-letter word **THE**.

## Result

**Decrypted rune sequence:** `TH · E`

**Proposed reading: THE**

The arithmetic reproduces **THE** from the stated ciphertext cells and rotated key. The shared `J (19,16)` provides a concrete geometric link to **OF**, but that link does not by itself prove this reading is uniquely intended.
