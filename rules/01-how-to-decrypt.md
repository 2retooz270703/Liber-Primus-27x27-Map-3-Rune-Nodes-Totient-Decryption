# 01 — How to Decrypt

The 729 runes from pages 0–2 fill a 27 × 27 matrix, row by row. Each rune has an index from 0 to 28 (not its Gematria Primus prime value). TH, EA, and NG each count as one rune.

## 1. Form the key

Take three runes and change only the center using Euler's totient φ(n). It counts integers from 1 to n that share no factor with n except 1; φ(10) = 4 (1, 3, 7, 9).

| Structure | Center transformation | Key |
|:---:|:---:|:---:|
| X–OE–X | φ(OE = 22) = 10 = I | X–I–X |

A mirror has matching outer runes at equal distances from the center. Non-mirrored triples also occur: H–NG–C, for example, is used directly.

## 2. Choose the rotation

Apply φ to each key rune, then μ. The Möbius function gives 0 when a prime factor repeats; otherwise +1 for an even number of prime factors and −1 for an odd number. Also, μ(1) = +1.

The phase is the sum of the three μ values modulo 3. For key indices k₁, k₂, k₃:

p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3

| Step | Calculation | Result |
|:---|:---|:---:|
| Key | X = 14; I = 10; X = 14 | X–I–X |
| Totient | φ(14) = 6; φ(10) = 4; φ(14) = 6 | (6, 4, 6) |
| Möbius | μ(6) = +1; μ(4) = 0; μ(6) = +1 | (+1, 0, +1) |
| Phase | (1 + 0 + 1) mod 3 = 2 | 2 |
| Rotation | Move the first rune to the end twice | X–X–I |

Phase 0 keeps the original order; phases 1 and 2 shift it left by one or two positions. Keep the full μ signature for later rules.

## 3. Recover the plaintext

For WEATHER, read NG–P–EO–O–E. Repeat the rotated key X–X–I to match all five ciphertext runes: X–X–I–X–X.

Plaintext = (ciphertext − key) mod 29

Subtract the rune indices. Modulo 29 gives a result from 0 to 28: for example, −1 becomes 28.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

This explains how a chosen key decrypts a chosen ciphertext. Finding the next location is covered by the movement rules.
