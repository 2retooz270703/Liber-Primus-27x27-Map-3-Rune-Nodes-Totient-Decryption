# 01 — How Runes Become Plaintext

729 runes → 27 × 27 grid. Each rune has an index **0–28**, not a prime value. `TH`, `EA`, and `NG` each count as one rune.

## 1. Change the center

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X | OE = 22 | X |
| Key | X | I = 10 | X |

**φ(22) = 10 = I.** Only the center changes; the outer runes stay in place.

## 2. Rotate the key

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

**Phase = (1 + 0 + 1) mod 3 = 2.** Rotate the key left by two positions.

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

Keep the full Möbius pattern `(+1, 0, +1)` for the route rules.

## 3. Subtract to reveal the text

Repeat the rotated key. Subtract its rune indices from the ciphertext **modulo 29**.

| | 1 | 2 | 3 | 4 | 5 |
|:---|:---:|:---:|:---:|:---:|:---:|
| Ciphertext | NG = 21 | P = 13 | EO = 12 | O = 3 | E = 18 |
| − Key | X = 14 | X = 14 | I = 10 | X = 14 | X = 14 |
| = Plaintext | W = 7 | EA = 28 | TH = 2 | E = 18 | R = 4 |

**W–EA–TH–E–R → WEATHER**

<details>
<summary>Definitions and exceptions</summary>

- **φ(n)** (Euler's totient) counts integers from 1 to `n` that are coprime to `n`.
- **μ(n)** (Möbius function) is `0` if `n` has a squared prime factor; otherwise it is `+1` or `−1` for an even or odd number of distinct prime factors. `μ(1) = +1`.
- **Modulo 29** wraps results into `0–28`: `13 − 14 = −1 ≡ 28`, which is `EA`.
- **Structures:** Mirrors have matching outer runes at equal distances from their center. A non-mirrored triple, such as `H–NG–C`, can also supply a key without the same center transformation.

</details>

The calculations explain **how** a key decrypts ciphertext. Selecting the key's location, the ciphertext, and its reading direction remains a separate problem.
