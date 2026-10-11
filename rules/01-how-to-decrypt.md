# 01 — How to Decrypt

The 729 runes from pages 0–2 form a 27 × 27 matrix. Each rune has an index from 0 to 28 (not its Gematria Primus prime value). TH, EA, and NG each count as one rune.

## 1. Form the key

Take three runes and replace the center with its Euler totient value. The outer runes stay unchanged.

| Original structure | Center transformation | Generated key |
|:---:|:---:|:---:|
| X–OE–X | φ(22) = 10 = I | X–I–X |

**φ(n)** counts the numbers from 1 to n that share no factor with n except 1. For example, φ(10) = 4 because 1, 3, 7, and 9 qualify.

A *mirror* has matching outer runes at equal distances. Non-mirrored triples can also supply keys: H–NG–C, for example, is used without changing its center.

## 2. Find the phase

Apply φ to each rune of the new key. Then apply the Möbius function μ to those three results.

**μ(n)** is 0 if a prime factor repeats. Otherwise, it is +1 for an even number of distinct prime factors and −1 for an odd number. For example: μ(4) = 0, μ(6) = +1, μ(2) = −1, and μ(1) = +1.

For the three key indices k₁, k₂, k₃, the phase is:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

| Step | Calculation | Result |
|:---|:---|:---:|
| Totient | φ(14), φ(10), φ(14) | (6, 4, 6) |
| Möbius | μ(6), μ(4), μ(6) | (+1, 0, +1) |
| Phase | (1 + 0 + 1) mod 3 | 2 |
| Rotation | X–I–X → I–X–X → X–X–I | X–X–I |

Mod 3 means the remainder after division by 3. The result gives the number of left rotations: 0, 1, or 2. Keep the full Möbius signature (+1, 0, +1) for the movement rules.

## 3. Reveal the plaintext

Repeat the rotated key to match the ciphertext length. For WEATHER, read NG–P–EO–O–E and use X–X–I–X–X.

**Plaintext = (ciphertext − key) mod 29**

Subtract the rune indices position by position. *Mod 29* keeps each answer between 0 and 28: for example, −1 becomes 28.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

These steps decrypt a chosen ciphertext with a chosen key. Finding where to read next is a separate part of the reconstruction.
