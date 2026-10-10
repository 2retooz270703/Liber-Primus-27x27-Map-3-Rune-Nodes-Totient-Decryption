# 01 — How Runes Become Plaintext

729 runes form a **27 × 27 matrix**, filled row by row from `(1,1)`. Use rune **indices 0–28**, not prime values; names like `TH`, `EA`, and `NG` each represent one rune.

Three runes → Key → Rotation → Plaintext

## 1. Make the key

Keep the outer runes; apply Euler's totient **φ** to the center.

| Structure | Center | Key |
|:---:|:---:|:---:|
| X–OE–X | φ(22) = 10 = I | X–I–X |

`φ(n)` counts the integers from 1 to n that are coprime to n. A mirror has matching outer runes equally spaced around its center, in a row, column, or diagonal.

## 2. Choose the key's rotation

Apply **φ**, then Möbius **μ**, to all three key values.

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

**Phase:** (+1 + 0 + 1) mod 3 = **2**

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

`μ(n)` is 0 if n contains a squared prime factor; otherwise +1 or −1 for an even or odd number of distinct prime factors. `μ(1) = +1`. Keep the full signature `(+1, 0, +1)` for later rules.

## 3. Decrypt

Repeat the rotated key. Subtract **key from ciphertext**, modulo 29.

| Ciphertext | Key | (C − K) mod 29 | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 = 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 = 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 = 4 | R |

### WEATHER

A negative result wraps into 0–28 (for example, −1 ≡ 28 mod 29). Some stages use a direct, non-mirrored key such as `H–NG–C`.

This explains **how to decrypt** once the key and ciphertext are known—not how their locations or reading direction are chosen.
