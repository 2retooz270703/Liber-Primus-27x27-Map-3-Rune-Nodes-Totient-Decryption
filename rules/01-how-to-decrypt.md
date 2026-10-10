# 01 — How to Decrypt

*Three runes → Key → Rotation → Plaintext*

The 729 runes from pages 0–2 are arranged row by row in a 27 × 27 matrix. Each rune has an index from 0 to 28 (not its Gematria Primus prime value). `TH`, `EA`, and `NG` each count as one rune.

## 1. Make the key

Euler's totient, **φ(n)**, counts the numbers from 1 to n that share no factor with n except 1. For example, φ(10) = 4 because only 1, 3, 7, and 9 qualify.

For a three-rune structure, change only the center:

**a–b–c → a–φ(b)–c**

| Stage | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X = 14 | OE = 22 | X = 14 |
| Key | X = 14 | I = 10 | X = 14 |

φ(22) = 10 = I, so `X–OE–X` becomes `X–I–X`.

A *mirror* has matching outer runes. Its three cells can be separated by equal distances along a row, column, or diagonal. Non-mirrored triples also occur; `H–NG–C`, for example, is used directly.

## 2. Choose the key's rotation

Apply φ to all three runes of the new key, then apply the Möbius function **μ**:

| μ(n) | When | Example |
|:---:|:---|:---|
| 0 | Contains a squared prime factor | μ(4) = 0; 4 = 2² |
| +1 | Even number of distinct prime factors | μ(6) = +1; 6 = 2 × 3 |
| −1 | Odd number of distinct prime factors | μ(2) = −1; 2 is prime |

Also, μ(1) = +1.

| Stage | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Let k₁, k₂, k₃ be the three key indices. Add their μ results; the remainder after division by 3 is the **phase**:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

Here: p = (1 + 0 + 1) mod 3 = 2.

Rotate the key left by that many positions:

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

Keep the three individual μ values `(+1, 0, +1)` too: later rules use the full signature, not only its sum.

## 3. Reveal the plaintext

For WEATHER, read `NG–P–EO–O–E` (row 14, columns 14–18). Repeat the rotated key over all five runes: `X–X–I–X–X`.

**Plaintext index = (ciphertext index − key index) mod 29**

`mod 29` means the result must be between 0 and 28. If it is negative, add 29. For example: `13 − 14 = −1 → 28 = EA`.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

**W–EA–TH–E–R**

### WEATHER

These steps decrypt a selected ciphertext with a selected key. Choosing where to read next belongs to the movement and mirror rules.
