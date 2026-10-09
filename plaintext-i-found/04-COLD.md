# 04 — COLD

## 1. Locate the node

At A(14,19), the TURNS key's phase 0 gives V₀(14,19) = (+1, −1) → DOWN + LEFT.

| Row | Column 18 | Column 19 | Column 20 |
|:---:|:---:|:---:|:---:|
| 25 | W | H | EA |
| 26 | G | TH | H |
| 27 | EA | H | D |

TH(26,19) is the center of the vertical H–TH–H node.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | TH = 2; φ(2) = 1 = U | H–U–H |
| Totient signature | φ(H = 8) = 4; φ(U = 1) = 1; φ(H = 8) = 4 | (4, 1, 4) |
| Möbius signature | μ(4) = 0; μ(1) = +1; μ(4) = 0 | (0, +1, 0) |
| Rotation | (0 + 1 + 0) mod 3 = 1 | U–H–H |
| Movement | φ(NG = 21) = 12 | A → TH (down 12); A → G (left 12) |

## 3. Read and decrypt

From G(14,7), read four runes upward. Subtract the repeating U–H–H key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,7) | G = 6 | U = 1 | 6 − 1 ≡ 5 | C |
| (13,7) | J = 11 | H = 8 | 11 − 8 ≡ 3 | O |
| (12,7) | EA = 28 | H = 8 | 28 − 8 ≡ 20 | L |
| (11,7) | A = 24 | U = 1 | 24 − 1 ≡ 23 | D |

The final A(11,7) is the center of EA(10,7)–A(11,7)–EA(12,7), matching the key's CENTER state (0, +1, 0).

### COLD
