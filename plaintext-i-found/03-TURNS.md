# 03 — TURNS

## 1. Locate the node

After WEATHER: E(14,18) → A(14,19).

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| 4 | | H | |
| 14 | A | NG | A |
| 24 | | C | |

At A, the WEATHER key's phase 2 gives V₂(14,19) = (−1, +1) → UP + RIGHT.

A–NG–A is a horizontal mirror; the vertical H–NG–C forms the key.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H(4,23) – NG(14,23) – C(24,23) | H–NG–C |
| Totient signature | φ(H = 8) = 4; φ(NG = 21) = 12; φ(C = 5) = 4 | (4, 12, 4) |
| Möbius signature | μ(4) = 0; μ(12) = 0; μ(4) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | φ(I = 10) = 4; I = 10 | A → NG (right 4); NG → H/C (up/down 10) |

## 3. Read and decrypt

From A(14,19), read five runes upward. Subtract the repeating H–NG–C key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,19) | A = 24 | H = 8 | 24 − 8 ≡ 16 | T |
| (13,19) | OE = 22 | NG = 21 | 22 − 21 ≡ 1 | U |
| (12,19) | N = 9 | C = 5 | 9 − 5 ≡ 4 | R |
| (11,19) | B = 17 | H = 8 | 17 − 8 ≡ 9 | N |
| (10,19) | W = 7 | NG = 21 | 7 − 21 ≡ 15 | S |

### TURNS

For COLD, the TURNS key gives phase 0 and φ(NG = 21) = 12. At A(14,19), V₀ = (+1, −1) → DOWN + LEFT.

DOWN 12 reaches TH(26,19), center of H–TH–H; LEFT 12 reaches G(14,7), where COLD begins.

Continue to [04 — COLD](./04-COLD.md).
