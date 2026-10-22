# 13 — DEATH

This example continues from **IS**. Its last ciphertext rune is the center of a diagonal `E–D–E` mirror. A sequence of connected three-rune nodes leads to a new key and three ciphertext runes that decrypt as **DEATH**.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` denotes Euler's totient function; `μ` denotes the Möbius function. A diagonal distance counts **grid steps** along the diagonal.

## 1. Find the connected three-rune nodes

The preceding **IS** ciphertext ends at **`D (21,10)`**, the center of the diagonal `E–D–E` mirror. From that center, move **2 cells down-right**, perpendicular to the mirror, to reach **`B (23,12)`**:

`D (21,10) → down-right 2 → B (23,12)`

The following nodes connect this position to the next ciphertext start:

| Mirror | First endpoint | Center | Second endpoint | Radius |
|:---|:---:|:---:|:---:|:---:|
| `E–D–E` | E (19,12) | **D (21,10)** | E (23,8) | 2 diagonal steps |
| `J–B–J` | J (19,16) | **B (23,12)** | **J (27,8)** | 4 diagonal steps |
| `J–C–J` | J (25,6) | **C (26,7)** | **J (27,8)** | 1 diagonal step |
| `C–OE–C` | **C (26,3)** | OE (26,5) | **C (26,7)** | 2 horizontal cells |

The route uses the node positions as follows:

1. `E–D–E` supplies the preceding endpoint, `D (21,10)`; the perpendicular move reaches the center `B (23,12)` of `J–B–J`.
2. `J–B–J` and `J–C–J` share **`J (27,8)`**.
3. `J–C–J` and `C–OE–C` share **`C (26,7)`**.

In this proposed reading, **`J–B–J` provides the key**. The remaining connected mirrors lead to the ciphertext start at **`C (26,3)`**.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer `J` runes of `J–B–J`. Replace its center `B` with the rune whose index equals `φ(17)`:

`B = 17 → φ(17) = 16 → T`

The unrotated key is **`J–T–J`**.

### Calculate its rotation

For each rune in the derived key, apply `φ` to its index, then apply `μ` to the resulting totient value:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| J | 11 | φ(11) = 10 | μ(10) = +1 |
| T | 16 | φ(16) = 8 | μ(8) = 0 |
| J | 11 | φ(11) = 10 | μ(10) = +1 |

The **totient signature** is `(10, 8, 10)` and the **Möbius signature** is `(+1, 0, +1)`.

The Möbius sum determines the number of cyclic left rotations:

`Rotation = (1 + 0 + 1) mod 3 = 2`

Apply **two cyclic left rotations**:

`J–T–J → T–J–J → J–J–T`

**Final key: `J–J–T`.** This is the same rotated key previously used for **END**.

## 3. Locate the ciphertext start

Follow the connected nodes from the previous endpoint:

`D (21,10) → B (23,12) → J (27,8) → C (26,7) → C (26,3)`

The individual movements are:

| From | Movement | To | Geometric basis |
|:---|:---|:---|:---|
| D (21,10) | Down-right 2 | B (23,12) | Perpendicular to `E–D–E` |
| B (23,12) | Down-left 4 | J (27,8) | `J–B–J` radius 4 |
| J (27,8) | Up-left 1 | C (26,7) | `J–C–J` radius 1 |
| C (26,7) | Left 4 | C (26,3) | Across `C–OE–C`, through OE (26,5) |

The **recorded ciphertext start** is **`C (26,3)`**. Read **three cells leftward** along row 26:

`C (26,3) → I (26,2) → E (26,1)`

The node arrangement provides a traceable path between the two words. Selecting this route, the leftward reading direction, and the three-rune length are part of the proposed construction; the key calculation alone does **not** establish that this is the only possible path.

## 4. Read and decrypt the ciphertext

Subtract each key rune index from the corresponding ciphertext rune index, **modulo 29**:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (26,3) | C = 5 | J = 11 | 5 − 11 ≡ 23 | **D** |
| (26,2) | I = 10 | J = 11 | 10 − 11 ≡ 28 | **EA** |
| (26,1) | E = 18 | T = 16 | 18 − 16 ≡ 2 | **TH** |

## Result

**Decrypted rune sequence:** `D · EA · TH`

**Proposed reading: DEATH**

`EA` and `TH` are each **one rune**, despite representing two Latin letters. Therefore, **three decrypted runes** spell the five-letter word **DEATH**.

All three modular subtractions reproduce this reading from the stated ciphertext cells and rotated key.

## 5. Numerical connections

### The same key as END

Both **END** and **DEATH** use a key derived from `J–B–J`:

`J–B–J → J–T–J → J–J–T`

The key is reused, but the ciphertext locations and reading directions differ.

### The two passage totals: 233 and 232

Using **rune indices** (not prime-value Gematria Primus totals), add the indices of all decrypted runes in each passage:

| Passage | Sum by word | Total |
|:---|:---|:---:|
| `AS I GO THE WEATHER TURNS COLD` | 39 + 10 + 9 + 20 + 59 + 45 + 51 | **233** |
| `THE IDEA OF THE END IS DEATH` | 20 + 61 + 3 + 20 + 50 + 25 + 53 | **232** |

Since **233 is prime**, Euler's totient function gives:

`φ(233) = 232`

The two rune-index totals therefore form an exact **totient relationship**. This is a numerical observation about the selected plaintext passages, not a step required to decrypt **DEATH**.

### The numbers 17 and 53

The second passage, `THE IDEA OF THE END IS DEATH`, contains **17 runes**. The center of the key-generating node is `B = 17`:

`B = 17 → φ(17) = 16`

The **16th prime** is **53**. Independently, the rune-index sum of **DEATH** is:

`D (23) + EA (28) + TH (2) = 53`

Thus **17 → 16 → 53** connects the key's center, a prime's position, and the decrypted word's rune-index total. This correspondence is exact arithmetically, but it does not independently prove that the selected route or plaintext is unique.
