# 17 — THEN

This example continues from **SOON**. The main **SOON** ciphertext ends at **`H (25,19)`**. Its key phase points **rightward**, and two totient-derived distances locate the proposed next ciphertext, **`L–T–W`**. A nearby vertical `IA–IA–IA` mirror supplies the key that decrypts those three runes as **THEN**.

The final ciphertext rune also connects to the **alternative SOON route** through a separate `W–NG–W` mirror.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` denotes Euler's totient function, `μ` denotes the Möbius function, and `φ²(n)` means `φ(φ(n))`. All decryption subtractions are performed **modulo 29**.

## 1. Find the connected three-rune node

The main **SOON** route uses the rotated key `EA–L–R`, whose **rotation phase is 2**. At its endpoint **`H (25,19)`**, the project's direction convention gives:

`V₂ = (0, +1) → RIGHT`

Apply Euler's totient function twice to the endpoint coordinates:

- **Row 25:** `φ(25) = 20`, then `φ²(25) = φ(20) = 8`.
- **Column 19:** `φ(19) = 18`, then `φ²(19) = φ(18) = 6`.

The resulting pair is **`T₂ = (8, 6)`**. Both distances are used along the indicated **rightward** direction:

| From | Direction and distance | Reached cell |
|:---|:---|:---|
| H (25,19) | Right **6** cells | **L (25,25)** |
| H (25,19) | Right **8** cells | **W (25,27)** |

The relevant section of the matrix is:

| Row | Column 19 | Column 22 | Column 25 | Column 26 | Column 27 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 25 | **H** | IA | **L** | **T** | **W** |
| 26 | — | **IA** | — | — | — |
| 27 | — | IA | — | — | — |

The rune **`IA (25,22)`** lies exactly halfway between **`H (25,19)`** and **`L (25,25)`**: each is **3 columns** away. It is also the upper endpoint of a vertical, equally spaced `IA–IA–IA` mirror:

| Mirror | First endpoint | Center | Second endpoint | Radius |
|:---|:---:|:---:|:---:|:---:|
| `IA–IA–IA` | IA (25,22) | **IA (26,22)** | IA (27,22) | **1 vertical cell** |

The **center `IA (26,22)`** generates the next decryption key.

## 2. Derive and align the decryption key

### Replace the center rune

Keep the two outer `IA` runes. Transform the center's rune index with `φ`:

`IA = 27 → φ(27) = 18 → E`

The unrotated key is **`IA–E–IA`**.

### Calculate its rotation

For each rune of the derived key, apply `φ` to its index and then `μ` to the result:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| IA | 27 | φ(27) = 18 | μ(18) = 0 |
| E | 18 | φ(18) = 6 | μ(6) = +1 |
| IA | 27 | φ(27) = 18 | μ(18) = 0 |

The **totient signature** is `(18, 6, 18)`, and the **Möbius signature** is `(0, +1, 0)`.

The sum of Möbius values determines the number of cyclic left rotations:

`Rotation = (0 + 1 + 0) mod 3 = 1`

Apply **one cyclic left rotation**:

`IA–E–IA → E–IA–IA`

**Final repeating key: `E–IA–IA`.**

## 3. Locate the ciphertext start and endpoint

The two distances from **`H (25,19)`** identify the selected three-rune segment:

- **Start:** `L (25,25)`, reached after **6** cells to the right.
- **End:** `W (25,27)`, reached after **8** cells to the right.

Read the cells between these positions **from left to right**:

`L (25,25) → T (25,26) → W (25,27)`

This gives the ciphertext **`L–T–W`**. The direction and both distances are consistent with the stated rules. The choice of this mirror and segment is part of the proposed route; the numerical calculations alone do **not** prove that the continuation is unique.

## 4. Read and decrypt the ciphertext

Subtract each key rune index from the corresponding ciphertext rune index, **modulo 29**:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (25,25) | L = 20 | E = 18 | 20 − 18 ≡ 2 | **TH** |
| (25,26) | T = 16 | IA = 27 | 16 − 27 ≡ 18 | **E** |
| (25,27) | W = 7 | IA = 27 | 7 − 27 ≡ 9 | **N** |

## Result

**Decrypted rune sequence:** `TH · E · N`

**Proposed reading: THEN**

`TH` is **one rune** in this alphabet. Thus, three decrypted runes spell the four-letter English word **THEN**. All three modular subtractions are exact for the selected ciphertext and key.

## 5. Geometric and numerical connections

### The final rune links both SOON routes

The last ciphertext rune of **THEN**, **`W (25,27)`**, and the last rune of the **alternative SOON ciphertext** (`P–S–U–W`), **`W (27,27)`**, are opposite endpoints of the same vertical mirror:

| Mirror | First endpoint | Center | Second endpoint | Radius |
|:---|:---:|:---:|:---:|:---:|
| `W–NG–W` | **W (25,27)** | NG (26,27) | **W (27,27)** | 1 vertical cell |

This is an exact shared geometric feature of the two routes.

### The connecting mirror reproduces phase 2

Transform the center `NG` of the `W–NG–W` mirror:

`NG = 21 → φ(21) = 12 → EO`

The resulting key is **`W–EO–W`**. Its totient and Möbius signatures are:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| W | 7 | φ(7) = 6 | μ(6) = +1 |
| EO | 12 | φ(12) = 4 | μ(4) = 0 |
| W | 7 | φ(7) = 6 | μ(6) = +1 |

**Totient signature:** `(6, 4, 6)`  
**Möbius signature:** `(+1, 0, +1)`

`Rotation phase = (1 + 0 + 1) mod 3 = 2`

This matches the **phase 2** used when moving rightward from the end of the main **SOON** ciphertext.

### The same direction and coordinate signature reappear

At **`W (25,27)`**, the phase-2 coordinate transformation gives:

- `φ²(25) = 8`.
- `φ²(27) = φ(18) = 6`.

Therefore, **`T₂ = (8, 6)`** and **`V₂ = (0, +1) → RIGHT`** under the project's convention.

These are exactly the same coordinate-derived values and direction found at **`H (25,19)`**, the main **SOON** endpoint. This is an additional correspondence between the two locations, not by itself a guarantee of the next reading.

### The preceding plaintext totals match the THEN key

Here the totals use **29-rune indices**, **not Gematria Primus prime values**:

| Plaintext | Rune indices | Total |
|:---|:---|:---:|
| `SEE` | S (15) + E (18) + E (18) | **51** |
| `YOU` | Y (26) + O (3) + U (1) | **30** |
| `SOON` | S (15) + O (3) + O (3) + N (9) | **30** |
| **Combined** | 51 + 30 + 30 | **111** |

Since `111 = 3 × 37`, its totient is:

`φ(111) = (3 − 1)(37 − 1) = 72`

The rotated **THEN** key has the same rune-index sum:

`E–IA–IA = 18 + 27 + 27 = 72`

Thus, **`φ(111) = sum(E–IA–IA) = 72`**. The equality is exact, but it is a **numerical observation**, not an independent proof of the ciphertext route or its uniqueness.
