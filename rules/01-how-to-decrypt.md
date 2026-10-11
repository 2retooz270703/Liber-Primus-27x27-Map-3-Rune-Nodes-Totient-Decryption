# 01 — How to Decrypt

## 1. Make the key

A three-rune structure supplies the key. Usually, the outer runes stay the same while the center changes through Euler's totient function, φ.

For X–OE–X:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X | OE | X |
| Key | X | φ(22) = 10 = I | X |

X–OE–X → X–I–X

In general: **a–b–c → a–φ(b)–c**.

Non-mirrored structures also occur: H–NG–C, for example, is used directly without changing its center.

## 2. Choose the rotation

The key has three possible starting positions. Its **phase** (0, 1, or 2) determines which order to use.

First apply φ to each rune of the key, then apply the Möbius function μ to those results.

For X–I–X:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Add the three μ values. The remainder after division by 3 gives the phase:

p = (1 + 0 + 1) mod 3 = 2

Rotate the key two places to the left:

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

For any key with indices k₁, k₂, k₃, the same rule is:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

Keep the full μ signature (+1, 0, +1) as well; later rules use it separately from the phase.

## 3. Reveal the plaintext

For WEATHER, the ciphertext is NG–P–EO–O–E (row 14, columns 14–18). Repeat the rotated key X–X–I to match its five runes: X–X–I–X–X.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 ≡ 4 | R |
