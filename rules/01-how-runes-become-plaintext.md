# 01 — How Runes Become Plaintext

The 729 runes from pages 0–2 form a 27 × 27 matrix, filled left to right, row by row. Coordinates are written as (row, column), starting at (1,1).

Each rune has a Gematria Primus index from 0 to 28. These indices are used for decryption, not the separate prime-number values. Runes such as TH, EA, and NG each count as one symbol.

These steps explain decryption once the key and ciphertext have been located. Choosing the next node and reading direction is a separate problem.

## 1. Find a three-rune node

| Row | Column 4 | Column 5 | Column 6 |
|:---:|:---:|:---:|:---:|
| 13 | C/K | B | L |
| 14 | X | OE | X |
| 15 | NG | AE | C/K |

The central OE(14,5) forms the mirror X–OE–X. A mirror has matching outer runes, equally spaced around its center. It can be horizontal, vertical, or diagonal.

Some keys also come from non-mirrored triples, such as H–NG–C in [TURNS](../plaintext-i-found/03-TURNS.md), which is used directly.

## 2. Derive and rotate the key

For a mirrored node, keep the outer runes and transform the center using Euler's totient function φ. Then apply φ and the Möbius function μ to the resulting key to determine its phase.

| Step | Calculation | Result |
|:---|:---|:---|
| Key | OE = 22; φ(22) = 10 = I | X–I–X |
| Totient signature | φ(X = 14) = 6; φ(I = 10) = 4; φ(X = 14) = 6 | (6, 4, 6) |
| Möbius signature | μ(6) = +1; μ(4) = 0; μ(6) = +1 | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | X–X–I |

φ(n) counts numbers up to n that have no common factor with n except 1. μ(n) is 0 if n contains a squared prime factor; otherwise it is +1 or −1 according to the number of distinct prime factors (μ(1) = +1).

The Möbius sum modulo 3 gives the phase: 0 keeps the key unchanged, 1 shifts it left once, and 2 shifts it left twice. The full Möbius signature is also retained for structural comparisons.

## 3. Read and decrypt

For WEATHER, read five runes rightward from NG(14,14). Repeat the X–X–I key as X–X–I–X–X, then subtract each key index from its ciphertext index modulo 29. Negative results wrap back into the range 0–28.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,14) | NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| (14,15) | P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| (14,16) | EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| (14,17) | O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| (14,18) | E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

The five plaintext runes W–EA–TH–E–R spell WEATHER.

### WEATHER
