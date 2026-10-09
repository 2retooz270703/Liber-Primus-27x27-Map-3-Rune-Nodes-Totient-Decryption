# 03 — TURNS

## 1. Locate the node

After WEATHER: E(14,18) → A(14,19).

Phase 2 selects UP + RIGHT: μ(φ²(14)) = μ(2) = −1; μ(φ²(19)) = μ(6) = +1.

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| 4 | | H | |
| 14 | A | NG | A |
| 24 | | C | |

From A, RIGHT 4 (φ(10)) reaches NG(14,23). From NG, UP / DOWN 10 (I = 10) reaches H(4,23) / C(24,23).

A–NG–A is a horizontal mirror. The vertical H–NG–C supplies the key.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H(4,23) – NG(14,23) – C(24,23) | H–NG–C |
| Totient | φ(8) = 4; φ(21) = 12; φ(5) = 4 | (4, 12, 4) |
| Möbius | μ(4) = 0; μ(12) = 0; μ(4) = 0 | (0, 0, 0) |
| Phase | (0 + 0 + 0) mod 3 = 0 | No rotation |

I–NG–I has the same signatures: φ(H) = φ(I) = φ(C) = 4.

## 3. Read and decrypt

Read upward from A(14,19). Subtract the repeating H–NG–C key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,19) | A = 24 | H = 8 | 24 − 8 ≡ 16 | T |
| (13,19) | OE = 22 | NG = 21 | 22 − 21 ≡ 1 | U |
| (12,19) | N = 9 | C = 5 | 9 − 5 ≡ 4 | R |
| (11,19) | B = 17 | H = 8 | 17 − 8 ≡ 9 | N |
| (10,19) | W = 7 | NG = 21 | 7 − 21 ≡ 15 | S |

### TURNS

Next: φ(NG = 21) = 12; phase 0 gives V₀(14,19) = (+1, −1) → DOWN + LEFT.

From A(14,19): DOWN 12 → TH(26,19), center of H–TH–H; LEFT 12 → G(14,7), start of COLD.

Continue to [04 — COLD](./04-COLD.md).
