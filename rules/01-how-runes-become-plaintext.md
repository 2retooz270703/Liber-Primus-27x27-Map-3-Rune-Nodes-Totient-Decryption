# 01 — How Runes Become Plaintext

The 729 runes from pages 0–2 form a **27 × 27 matrix**, filled row by row. Coordinates start at `(1,1)`. Calculations use **rune indices 0–28**, not prime values; `TH`, `EA`, and `NG` each count as one rune.

| Structure | Generated key | Rotated key | Plaintext |
|:---:|:---:|:---:|:---:|
| X–OE–X | X–I–X | X–X–I | W–EA–TH–E–R |

## 1. Form the key

Keep the outer runes of a mirror. Replace its center with its Euler totient **φ**.

| Left outer | Center | Right outer |
|:---:|:---:|:---:|
| X | OE = 22 | X |
| X | **φ(22) = 10 = I** | X |

**Key: X–I–X**

`φ(n)` counts the integers from 1 to n that are coprime to n. A mirror has equal outer runes at equal distances from its center, horizontally, vertically, or diagonally.

## 2. Set the key's order

Apply **φ**, then Möbius **μ**, to each rune of the generated key.

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

**Phase = (+1 + 0 + 1) mod 3 = 2**

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

The phase rotates the key left by 0, 1, or 2 places. Keep the full Möbius signature **(+1, 0, +1)** for later route calculations.

`μ(n)` is 0 if a prime square divides n; otherwise it is +1 for an even number of distinct prime factors, −1 for an odd number. `μ(1) = +1`.

## 3. Reveal the plaintext

Repeat the rotated key across the selected ciphertext. Subtract **ciphertext − key (mod 29)**, rune by rune.

| Ciphertext | Key | Subtraction mod 29 | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 = 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 = 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 = 4 | R |

### W–EA–TH–E–R → WEATHER

Modulo 29 wraps negative results into 0–28; for example, `−1 ≡ 28`.

---

The route may also use a direct, non-mirrored key such as **H–NG–C**. These steps explain **decryption once the key and ciphertext are known**; selecting their locations and reading direction is a separate problem.
