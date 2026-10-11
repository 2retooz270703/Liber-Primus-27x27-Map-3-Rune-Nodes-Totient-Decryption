# 01 — How to Decrypt

A three-rune structure gives a key. Two calculations determine its rotation; subtracting that key reveals the plaintext.

The 729 runes from pages 0–2 are arranged row by row in a 27 × 27 matrix. Calculations use rune indices 0–28, not Gematria Primus prime values. TH, EA, and NG each count as one rune.

## 1. Make the key

Take three runes from the matrix. Usually, the outer runes stay unchanged and the center is replaced using Euler's totient, φ.

φ(n) counts the integers from 1 to n that have no common factor with n other than 1. For example, φ(10) = 4, counting 1, 3, 7, and 9.

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Original | X | OE = 22 | X |
| After φ | X | φ(22) = 10 = I | X |

The resulting key is **X–I–X**.

A *mirror* has matching outer runes at equal distances from its center. Not every key comes from a mirror: H–NG–C, for example, is used directly without changing its center.

## 2. Choose the rotation

Now use the **new key**, X–I–X. Apply φ to each of its three rune indices, then apply the Möbius function μ to each result.

μ(n) examines prime factors: a repeated factor gives 0; otherwise an odd number of factors gives −1, and an even number gives +1. For example, μ(2) = −1 and μ(1) = +1.

| | Left: X = 14 | Center: I = 10 | Right: X = 14 |
|:---|:---:|:---:|:---:|
| φ | 6 | 4 | 6 |
| Prime factors | 2 × 3 | 2² | 2 × 3 |
| μ | +1 | 0 | +1 |

Add the three μ values to get the *phase*. Mod 3 means taking the remainder after dividing by 3, so the phase is always 0, 1, or 2:

p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3

Here, k₁, k₂, and k₃ are the indices of the **generated key**, from left to right.

For X–I–X: p = (1 + 0 + 1) mod 3 = **2**.

| Phase | Key order |
|:---:|:---:|
| 0 | X–I–X |
| 1 | I–X–X |
| 2 | X–X–I |

Each phase is a left rotation of the same key: phase 0 keeps the order, phase 1 shifts it once, and phase 2 shifts it twice. Here the active key is **X–X–I**. The full μ signature (+1, 0, +1) is also kept for movement rules.

## 3. Read the plaintext

Repeat the active key until it is as long as the ciphertext. For WEATHER, NG–P–EO–O–E is paired with X–X–I–X–X.

Subtract the key index from the ciphertext index at each position. Mod 29 keeps the result between 0 and 28; for example, 13 − 14 = −1 becomes 28 = EA.

Plaintext = (ciphertext − key) mod 29

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

These rules decrypt a selected ciphertext with a selected key. Choosing where to read next is a separate part of the reconstruction.
