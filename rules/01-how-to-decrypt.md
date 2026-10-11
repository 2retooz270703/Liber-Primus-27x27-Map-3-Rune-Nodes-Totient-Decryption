# 01 — How to Decrypt

*Three runes → Key → Rotation → Plaintext*

The 729 runes from pages 0–2 form a 27 × 27 matrix, filled row by row. Each rune has an index from 0 to 28, rather than its Gematria Primus prime value. `TH`, `EA`, and `NG` each count as one rune.

## 1. Make the key

A three-rune structure supplies the key. Usually, the outer runes stay the same while the center changes through Euler's totient function, φ.

φ(n) counts the integers from 1 to n that have no common factor with n except 1. For example, φ(10) = 4, counting 1, 3, 7, and 9.

For **X–OE–X**, only the center changes:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X = 14 | OE = 22 | X = 14 |
| Key | X = 14 | φ(22) = 10 = I | X = 14 |

**X–OE–X → X–I–X**

In general: **a–b–c → a–φ(b)–c**.

A *mirror* has matching outer runes at equal distances from the center. Non-mirrored structures also occur: `H–NG–C`, for example, is used directly without changing its center.

## 2. Choose the rotation

The key has three possible starting positions. Its **phase** (0, 1, or 2) determines which order to use.

First apply φ to each rune of the key, then apply the Möbius function μ to those results. μ depends on prime factors:

| μ(n) | Meaning | Example |
|:---:|:---|:---|
| 0 | A prime factor repeats | μ(4) = 0 (4 = 2 × 2) |
| +1 | An even number of distinct prime factors | μ(6) = +1 (6 = 2 × 3) |
| −1 | An odd number of distinct prime factors | μ(2) = −1 |

Also, μ(1) = +1.

For **X–I–X**, the values are:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Add the three μ values. The remainder after division by 3 gives the phase:

**p = (1 + 0 + 1) mod 3 = 2**

Rotate the key two places to the left:

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

For any key with indices k₁, k₂, k₃, the same rule is:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

Keep the full μ signature **(+1, 0, +1)** as well; later rules use it separately from the phase.

## 3. Reveal the plaintext

For **WEATHER**, the ciphertext is NG–P–EO–O–E (row 14, columns 14–18). Repeat the rotated key X–X–I to match its five runes: X–X–I–X–X.

Subtract each key index from its ciphertext index:

**Plaintext index = (ciphertext index − key index) mod 29**

`mod 29` keeps the result between 0 and 28. If the subtraction is negative, add 29. For example, 13 − 14 = −1 → 28 = EA.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

**W–EA–TH–E–R → WEATHER**

This decrypts an already selected ciphertext with an already selected key. Finding where to read next is covered by the movement and mirror rules.
