# 03 — TURNS

## 1. Locate the key

After WEATHER ends at E(14,18), move one cell right to A(14,19). The previous key supplies phase 2 and the distances 10 and 4.

At A(14,19), φ²(14) = 2 and φ²(19) = 6. Thus V₂ = (μ(2), μ(6)) = (−1, +1): up and right.

Move 4 cells right to NG(14,23). The surrounding runes form a cross:

| Row | Column 19 | Column 23 | Column 27 |
|:---:|:---:|:---:|:---:|
| 4 | | H | |
| 14 | A | NG | A |
| 24 | | C | |

The horizontal A–NG–A has a distance of 4 on each side. Vertically, H and C are 10 cells from NG. The vertical sequence H–NG–C becomes the key structure; it is not a matching-rune mirror.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H(4,23) – NG(14,23) – C(24,23) | H–NG–C |
| Totient signature | φ(H = 8) = 4; φ(NG = 21) = 12; φ(C = 5) = 4 | (4, 12, 4) |
| Möbius signature | μ(4) = 0; μ(12) = 0; μ(4) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |

## 3. Read and decrypt

From A(14,19), read five runes upward. Subtract the repeating key H–NG–C modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,19) | A = 24 | H = 8 | 24 − 8 ≡ 16 | T |
| (13,19) | OE = 22 | NG = 21 | 22 − 21 ≡ 1 | U |
| (12,19) | N = 9 | C = 5 | 9 − 5 ≡ 4 | R |
| (11,19) | B = 17 | H = 8 | 17 − 8 ≡ 9 | N |
| (10,19) | W = 7 | NG = 21 | 7 − 21 ≡ 15 | S |

### TURNS

## 4. Continue to COLD

H–NG–C and I–NG–I share the totient signature (4, 12, 4), since φ(H) = φ(I) = φ(C) = 4. Both give the Möbius signature (0, 0, 0).

Return to A(14,19), not the final W(10,19). The key center NG gives φ(21) = 12, while phase 0 gives V₀(14,19) = (+1, −1): down and left.

| Move from A(14,19) | Destination | Role |
|:---|:---|:---|
| Down 12 | TH(26,19) | Center of H–TH–H |
| Left 12 | G(14,7) | Start of the next ciphertext |

Continue to [04 — COLD](./04-COLD.md).
