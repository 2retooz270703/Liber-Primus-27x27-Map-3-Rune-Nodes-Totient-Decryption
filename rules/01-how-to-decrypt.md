# 01 — How to Decrypt

*Three runes → Key → Rotation → Plaintext*

The 729 runes from pages 0–2 are arranged row by row in a 27 × 27 matrix. Each rune has an index from **0 to 28** (not its Gematria Primus prime value). `TH`, `EA`, and `NG` each count as one rune.

## 1. Make the key

Start with a three-rune structure. Usually, the two outer runes stay the same, while the center changes through **Euler's totient**, φ.

φ(n) counts the numbers from 1 to n that share no factor greater than 1 with n. For example, φ(10) = 4 because only 1, 3, 7, and 9 qualify.

For the structure **X–OE–X**, the center is OE = 22. Since φ(22) = 10 = I:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X = 14 | OE = 22 | X = 14 |
| Key | X = 14 | I = 10 | X = 14 |

**X–OE–X → X–I–X**

In general: **a–b–c → a–φ(b)–c**.

A *mirror* has matching outer runes, equally spaced around the center along a row, column, or diagonal. Not every key comes from a mirror: **H–NG–C**, for example, is used directly without transforming its center.

## 2. Choose the rotation

The three-rune key can start at any of its three positions. The **phase** (0, 1, or 2) tells us which order to use.

First, apply φ to each rune of the new key. Then apply the **Möbius function**, μ, to those three results. μ depends on a number's prime factors:

| μ(n) | Rule | Example |
|:---:|:---|:---|
| 0 | A prime factor repeats | μ(4) = 0, since 4 = 2 × 2 |
| +1 | An even number of distinct prime factors | μ(6) = +1, since 6 = 2 × 3 |
| −1 | An odd number of distinct prime factors | μ(2) = −1 |

Also, μ(1) = +1.

Now apply both functions to **X–I–X**:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Add the three μ values. The remainder after division by 3 is the phase:

**p = (1 + 0 + 1) mod 3 = 2**

Phase 2 means rotating the key **two positions to the left**:

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

For any key with rune indices k₁, k₂, k₃, the same calculation is:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

Keep the full μ pattern **(+1, 0, +1)** too. Later rules use it separately from the phase.

## 3. Reveal the plaintext

For **WEATHER**, the ciphertext is **NG–P–EO–O–E** (row 14, columns 14–18). Repeat the rotated key **X–X–I** until it covers all five runes: **X–X–I–X–X**.

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

These operations decrypt a selected ciphertext with a selected key. Finding which structure and cells to use next is a separate part of the reconstruction.
