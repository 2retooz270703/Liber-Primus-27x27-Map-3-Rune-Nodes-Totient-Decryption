# 01 — How to Decrypt

*Three runes → Key → Rotation → Plaintext*

The 729 runes from pages 0–2 fill a 27 × 27 matrix, row by row. Each rune has an index from 0 to 28 (not its Gematria Primus prime value). `TH`, `EA`, and `NG` each count as one rune.

## 1. Make the key

Euler's totient φ(n) counts the integers from 1 to n that have no common factor with n except 1. For example, φ(10) = 4: only 1, 3, 7, and 9 qualify.

In a three-rune structure, only the center changes:

**a–b–c → a–φ(b)–c**

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X = 14 | OE = 22 | X = 14 |
| Key | X = 14 | I = 10 | X = 14 |

φ(22) = 10 = I, so **X–OE–X → X–I–X**.

A *mirror* has matching outer runes, equally spaced along a row, column, or diagonal. Non-mirrored triples also occur: `H–NG–C`, for example, is used directly.

## 2. Choose the rotation

Apply φ to all three runes of the new key, then apply the Möbius function μ to each result.

| μ(n) | Meaning | Example |
|:---:|:---|:---|
| 0 | A prime factor is repeated | μ(4) = 0, since 4 = 2² |
| +1 | An even number of distinct prime factors | μ(6) = +1, since 6 = 2 × 3 |
| −1 | An odd number of distinct prime factors | μ(2) = −1 |

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Let `k₁`, `k₂`, and `k₃` be the key indices. Add the three μ values and take the remainder after division by 3:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

Here, p = (1 + 0 + 1) mod 3 = 2. Rotate the key left by two positions:

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

Keep the individual μ values (+1, 0, +1) as well. Later rules use the full signature, not just the phase.

## 3. Reveal the plaintext

For WEATHER, read five ciphertext runes from row 14, columns 14–18: NG–P–EO–O–E. Repeat the rotated key to match: X–X–I–X–X.

**Plaintext index = (ciphertext index − key index) mod 29**

`mod 29` keeps the result between 0 and 28. If a subtraction is negative, add 29. For example, 13 − 14 = −1 → 28 = EA.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

**W–EA–TH–E–R**

These steps decrypt a *selected* ciphertext with a *selected* key. Choosing where to read next is covered by the movement and mirror rules.
