# 03 — TURNS

## 1. Locate the node

After WEATHER, move one cell right: E(14,18) → A(14,19).

The previous key gives two distances: I = 10 and φ(I) = 4. At A(14,19), phase 2 selects UP + RIGHT: μ(φ²(14)) = −1; μ(φ²(19)) = +1.

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| 4 | | H | |
| 14 | A | NG | A |
| 24 | | C | |

From A, move 4 cells right to NG(14,23). From NG, move 10 cells up and down to H(4,23) and C(24,23).

A–NG–A is a horizontal mirror. The vertical H–NG–C forms the key.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H(4,23) – NG(14,23) – C(24,23) | H–NG–C |
| Totient | φ(H = 8) = 4; φ(NG = 21) = 12; φ(C = 5) = 4 | (4, 12, 4) |
| Möbius | μ(4) = 0; μ(12) = 0; μ(4) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |

## 3. Read and decrypt

Read five cells upward from A(14,19). Subtract the repeating H–NG–C key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,19) | A = 24 | H = 8 | 24 − 8 ≡ 16 | T |
| (13,19) | OE = 22 | NG = 21 | 22 − 21 ≡ 1 | U |
| (12,19) | N = 9 | C = 5 | 9 − 5 ≡ 4 | R |
| (11,19) | B = 17 | H = 8 | 17 − 8 ≡ 9 | N |
| (10,19) | W = 7 | NG = 21 | 7 − 21 ≡ 15 | S |

### TURNS

For the next stage, φ(NG = 21) = 12. Phase 0 gives V₀(14,19) = (+1, −1): DOWN + LEFT.

From A(14,19), DOWN 12 reaches TH(26,19), the center of H–TH–H. LEFT 12 reaches G(14,7), where COLD begins.

Continue to [04 — COLD](./04-COLD.md).
