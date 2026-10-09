# 03 — TURNS

## 1. Locate the node

From `WEATHER`: E(14,18) → A(14,19).

| Step | Calculation | Result |
|:---|:---|:---|
| Direction (phase 2) | φ²(14) = 2; φ²(19) = 6; μ(2) = −1; μ(6) = +1 | Up + right |
| Right 4 | φ(I = 10) = 4 | NG(14,23) |
| Up / down 10 from NG | I = 10 | H(4,23), C(24,23) |

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| 4 | | H | |
| 14 | A | NG | A |
| 24 | | C | |

A–NG–A is a horizontal mirror (4 cells per side). The vertical H–NG–C (10 per side) supplies the key, though its outer runes differ.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H(4,23) – NG(14,23) – C(24,23) | H–NG–C |
| Totient signature | φ(H = 8) = 4; φ(NG = 21) = 12; φ(C = 5) = 4 | (4, 12, 4) |
| Möbius signature | μ(4) = 0; μ(12) = 0; μ(4) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |

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

## 4. Continue to COLD

H–NG–C and I–NG–I share the signatures (4, 12, 4) and (0, 0, 0), since φ(H) = φ(I) = φ(C) = 4.

| From A(14,19) | Calculation | Result |
|:---|:---|:---|
| Next movement | V₀ = (+1, −1); φ(NG = 21) = 12 | Down + left, 12 cells |
| Down 12 | A(14,19) → TH(26,19) | Center of H–TH–H |
| Left 12 | A(14,19) → G(14,7) | Start of COLD ciphertext |

Continue to [04 — COLD](./04-COLD.md).
