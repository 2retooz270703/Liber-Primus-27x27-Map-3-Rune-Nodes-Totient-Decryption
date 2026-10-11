# 01 — How to Decrypt

The 729 runes from pages 0–2 form a 27 × 27 matrix. Calculations use rune indices 0–28, not Gematria Primus prime values. TH, EA, and NG each count as one rune.

## 1. Form the key

Start with three runes. Keep the outer runes and replace the center using Euler's totient function, φ.

φ(n) counts the numbers from 1 to n that share no factor with n except 1. For example, φ(10) = 4 because only 1, 3, 7, and 9 qualify.

| Structure | Center transformation | Key |
|:---:|:---:|:---:|
| X–OE–X | OE = 22 → φ(22) = 10 = I | X–I–X |

A mirror has matching outer runes at equal distances from its center. Non-mirrored structures can also supply keys; H–NG–C is used directly.

## 2. Choose the rotation

Apply φ to each key rune, then apply the Möbius function, μ, to each result.

μ(n) is 0 if a prime factor repeats; otherwise it is +1 for an even number of prime factors and −1 for an odd number. Also, μ(1) = +1.

| | First rune | Second rune | Third rune |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Here, μ(6) = +1 because 6 = 2 × 3, while μ(4) = 0 because 4 = 2 × 2.

Add the three μ values modulo 3 to find the phase. For key indices k₁, k₂, k₃:

p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3

For X–I–X, p = (1 + 0 + 1) mod 3 = 2. The phase determines how far the key rotates left:

| Phase | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| Key order | X–I–X | I–X–X | X–X–I |

The active key is X–X–I. Keep the full μ pattern (+1, 0, +1) for later rules.

## 3. Recover the plaintext

For WEATHER, the ciphertext is NG–P–EO–O–E. Repeat the active key X–X–I across all five runes.

Plaintext = (Ciphertext − Key) mod 29

Subtract rune indices. Modulo 29 keeps the result from 0 to 28; for example, 13 − 14 = −1 becomes 28.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

This explains decryption once the key and ciphertext are known. Choosing their locations is a separate part of the reconstruction.
