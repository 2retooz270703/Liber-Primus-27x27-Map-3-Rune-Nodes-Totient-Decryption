# 03 — TURNS

## 1. Locate the key structure

After WEATHER ends at E(14,18), the next cell is A(14,19). The previous stage supplies phase 2 and the distances I = 10 and φ(10) = 4.

For the coordinate selector:

φ²(14) = 2 → μ(2) = −1; φ²(19) = 6 → μ(6) = +1.

V₂(14,19) = (−1, +1) → UP + RIGHT.

Moving 4 cells right from A(14,19) reaches NG(14,23). Two structures meet at this cell:

| Axis | First rune | Center | Last rune | Distance |
|:---|:---:|:---:|:---:|:---:|
| Row 14 | A(14,19) | NG(14,23) | A(14,27) | 4 on each side |
| Column 23 | H(4,23) | NG(14,23) | C(24,23) | 10 on each side |

The vertical sequence H–NG–C forms the key structure. Its outer runes differ, so it is not a matching-rune mirror.

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

## 4. Connections and next movement

The next movement starts again from A(14,19), not from the final ciphertext cell W(10,19).

| Connection | Evidence |
|:---|:---|
| Shared signature | H–NG–C and I–NG–I both give (4, 12, 4): φ(H = 8) = φ(I = 10) = φ(C = 5) = 4, and φ(NG = 21) = 12. Both have Möbius signature (0, 0, 0). |
| Next distance | φ(NG = 21) = 12 |
| Direction | Phase 0: V₀(14,19) = (μ(14), μ(19)) = (+1, −1) → DOWN + LEFT |
| Next key center | A(14,19) → 12 cells down → TH(26,19), center of H–TH–H |
| Next ciphertext | A(14,19) → 12 cells left → G(14,7) |

Continue to [04 — COLD](./04-COLD.md).
