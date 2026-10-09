# 03 — TURNS

## 1. Locate the node

After WEATHER: E(14,18) → A(14,19).

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| 4 | | H | |
| 14 | A | NG | A |
| 24 | | C | |

Phase 2 at A selects UP + RIGHT: μ(φ²(14)) = −1; μ(φ²(19)) = +1.

A–NG–A is a horizontal mirror. The vertical H–NG–C forms the key.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H(4,23) – NG(14,23) – C(24,23) | H–NG–C |
| Totient signature | φ(H = 8) = 4; φ(NG = 21) = 12; φ(C = 5) = 4 | (4, 12, 4) |
| Möbius signature | μ(4) = 0; μ(12) = 0; μ(4) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | φ(I = 10) = 4; I = 10 | A(14,19) → RIGHT 4 → NG(14,23); NG → UP/DOWN 10 → H(4,23)/C(24,23) |

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

For COLD, φ(NG = 21) = 12. Phase 0 at A selects DOWN + LEFT: V₀(14,19) = (+1, −1).

From A(14,19), DOWN 12 reaches TH(26,19), center of H–TH–H; LEFT 12 reaches G(14,7), where COLD begins.

Continue to [04 — COLD](./04-COLD.md).
