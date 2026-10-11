# 01 — How to Decrypt

*Three runes → Key → Rotation → Plaintext*

The 729 runes from pages 0–2 fill a 27 × 27 matrix, row by row. Rune indices run from 0 to 28, not the Gematria Primus prime values.

`TH`, `EA`, and `NG` each count as one rune.

## 1. Form the key

Start with three runes. Usually, only the center changes through Euler's totient function, φ.

φ(n) counts the numbers from 1 to n that have no common factor with n except 1. For example, φ(10) = 4: the numbers 1, 3, 7, 9.

| Original structure | Center calculation | Key |
|:---:|:---:|:---:|
| X–OE–X | φ(22) = 10 = I | X–I–X |

A *mirror* has matching outer runes at equal distances from its center. Not every key comes from a mirror: `H–NG–C`, for example, is used without changing its center.

## 2. Rotate the key

Apply φ to all three key values, then apply the Möbius function μ to each result.

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

| μ(n) | Rule | Example |
|:---:|:---|:---|
| +1 | Even number of distinct prime factors | μ(6) = +1 |
| −1 | Odd number of distinct prime factors | μ(2) = −1 |
| 0 | A prime factor repeats | μ(4) = 0 |

Also, μ(1) = +1.

Add the three μ values to find the phase. Here, k₁, k₂ and k₃ are the three key indices.

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

Here: `p = (1 + 0 + 1) mod 3 = 2`.

| Phase | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| Key order | X–I–X | I–X–X | X–X–I |

The active key is X–X–I. The full μ pattern (+1, 0, +1) is also kept for later rules.

## 3. Decrypt the runes

For WEATHER, the ciphertext is NG–P–EO–O–E. Repeat X–X–I to cover all five runes.

Subtract the key values from the ciphertext values:

**Plaintext = (ciphertext − key) mod 29**

`mod 29` keeps the result between 0 and 28. For example, 13 − 14 = −1, so add 29 to get 28 = EA.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

This rule decrypts a selected ciphertext with a selected key. How the next location is chosen is covered separately.
