# 01 — How Runes Become Plaintext

This chapter explains how a selected three-rune structure becomes a decryption key, how its reading phase is calculated, and how that key reveals plaintext. Finding the next structure and ciphertext location is a separate part of the reconstruction.

## 1. The 27×27 matrix

Pages 0–2 of *Liber Primus* contain 729 rune positions. They are arranged row by row into a **27 × 27 matrix** (729 = 27 × 27), starting at (1,1) and continuing left to right. Coordinates are written as **(row, column)**.

Each rune has a **Gematria Primus index from 0 to 28**. These indices—not the separate prime-number gematria values—are used for keys and subtraction.

| Rune | Index |
|:---|---:|
| U | 1 |
| TH | 2 |
| I | 10 |
| J | 11 |
| X | 14 |
| NG | 21 |
| OE | 22 |
| EA | 28 |

A rune is one symbol, not necessarily one Latin letter: `TH`, `EA`, `OE`, and `NG` each count as **one rune**.

## 2. Generate the key

Keys come from three-rune structures in the matrix. In a **mirror**, the two outer runes match, with a center exactly between them. The structure can be horizontal, vertical, or diagonal, and its radius can be greater than one cell.

For a mirror-based key, keep the outer runes and apply **Euler's totient** `φ` to the center. `φ(n)` counts the positive integers up to `n` that are coprime to it.

| Row | Column 4 | Column 5 | Column 6 |
|:---:|:---:|:---:|:---:|
| 14 | X | OE | X |

The center is OE(14,5). Since **OE = 22** and **φ(22) = 10 = I**:

`X–OE–X → X–I–X`

Not every recovered key is a mirror or requires this center transformation. For example, [`TURNS`](../plaintext-i-found/03-TURNS.md) uses the non-mirrored key `H–NG–C` directly.

## 3. Determine the reading phase

Once the key is known, apply `φ` to **all three key runes** to obtain its totient signature. Then apply the **Möbius function** `μ` to each value. `μ(n)` is `0` when a squared prime divides `n`; otherwise it is `+1` or `−1` according to whether `n` has an even or odd number of distinct prime factors, with `μ(1) = +1`.

The three Möbius values determine the key's **left rotation**:

`phase = (μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))) mod 3`

| Step | Calculation | Result |
|:---|:---|:---|
| Key | φ(OE = 22) = 10 = I | X–I–X |
| Totient signature | φ(14), φ(10), φ(14) | (6, 4, 6) |
| Möbius signature | μ(6), μ(4), μ(6) | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | X–X–I |

The phase selects one of three cyclic orders:

| Phase | Reading order | Example |
|:---:|:---|:---|
| 0 | k₁–k₂–k₃ | AE–I–EA → AE–I–EA |
| 1 | k₂–k₃–k₁ | H–U–H → U–H–H |
| 2 | k₃–k₁–k₂ | X–I–X → X–X–I |

The **full Möbius signature** is kept as well as its phase: different signatures can produce the same rotation but may carry different structural information.

## 4. Read and decrypt

Once the ciphertext cells have been identified, repeat the rotated key to match their number. For **WEATHER**, the five ciphertext runes are read rightward from NG(14,14), using `X–X–I–X–X`.

Subtract the key index from each ciphertext index **modulo 29**:

`Plaintext = (Ciphertext − Key) mod 29`

Negative results wrap into the range 0–28; for example, `13 − 14 ≡ 28 (mod 29)`.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,14) | NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| (14,15) | P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| (14,16) | EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| (14,17) | O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| (14,18) | E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

Five plaintext runes spell **WEATHER** because `EA` and `TH` each represent a single rune. The full matrix path appears in [`02-WEATHER.md`](../plaintext-i-found/02-WEATHER.md).

## 5. What this explains

These calculations determine **how a given key decrypts a given ciphertext**. They do not, by themselves, identify which structure to use, where to begin reading, or how long the ciphertext is. Those choices belong to the movement and structural rules, and the reconstruction does not yet establish a universal rule that resolves every such choice.
