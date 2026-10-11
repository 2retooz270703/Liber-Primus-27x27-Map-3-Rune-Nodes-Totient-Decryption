# 01 — How to Decrypt

The 729 runes from pages 0–2 form a 27 × 27 matrix. Each rune has an index from 0 to 28 (not its Gematria Primus prime value). Labels such as TH, EA, and NG each count as one rune.

## 1. Generate the key

Start with three runes. A *mirror* has matching outer runes, equally spaced around a center. Usually, only the center changes; the two outer runes stay the same.

The change uses **Euler's totient**, φ(n): the number of integers from 1 to n that share no factor with n except 1. For example, φ(10) = 4, counting 1, 3, 7, and 9.

| Original structure | Center transformation | Generated key |
|:---:|:---:|:---:|
| X–OE–X | OE = 22 → φ(22) = 10 = I | X–I–X |

Some keys are used without this transformation. For example, H–NG–C is a non-mirrored triple used directly.

## 2. Find the phase

The generated key can be rotated into three different orders. Its *phase* tells us which order to use.

First apply φ to **all three key runes**. Then apply the **Möbius function**, μ, to the three results:

- μ(n) = **0** when a prime factor repeats, as in 4 = 2 × 2.
- Otherwise, μ(n) = **+1** for an even number of prime factors (6 = 2 × 3), or **−1** for an odd number (2). Also μ(1) = +1.

Add the three μ results and take the remainder after dividing by 3. For key indices k₁, k₂, k₃, the formula is:

p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3

Here is the full calculation for X–I–X:

| Step | Calculation | Result |
|:---|:---|:---:|
| Rune indices | X = 14; I = 10; X = 14 | (14, 10, 14) |
| Totient φ | φ(14) = 6; φ(10) = 4; φ(14) = 6 | (6, 4, 6) |
| Möbius μ | μ(6) = +1; μ(4) = 0; μ(6) = +1 | (+1, 0, +1) |
| Phase | (1 + 0 + 1) mod 3 | 2 |
| Rotate | Shift X–I–X left twice | X–X–I |

Phase 0 leaves the order unchanged; phase 1 rotates left once; phase 2 rotates left twice. The active key here is X–X–I. The complete μ signature (+1, 0, +1) is retained for later rules.

## 3. Decrypt the runes

Repeat the active key to match the ciphertext length. For WEATHER, the five ciphertext runes NG–P–EO–O–E are paired with X–X–I–X–X.

Subtract the key index from the ciphertext index, then take the result modulo 29:

Plaintext = (ciphertext − key) mod 29

This keeps the result between 0 and 28. For example, 13 − 14 = −1 becomes 28 = EA after adding 29.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

These steps decrypt a selected ciphertext with a selected key. How to find the next location is covered in [02 — How to Move](./02-how-to-move.md).
