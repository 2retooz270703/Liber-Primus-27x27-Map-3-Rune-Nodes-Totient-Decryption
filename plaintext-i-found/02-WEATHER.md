# 02 — WEATHER

## 1. Locate the node

| Row | Column 4 | Column 5 | Column 6 |
|:---:|:---:|:---:|:---:|
| 13 | C/K | B | L |
| 14 | X | OE | X |
| 15 | NG | AE | C/K |

The central OE(14,5) forms the node X–OE–X, starting at X(14,4).

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | OE = 22; φ(22) = 10 = I | X–I–X |
| Totient signature | φ(X = 14) = 6; φ(I = 10) = 4; φ(X = 14) = 6 | (6, 4, 6) |
| Möbius signature | μ(6) = +1; μ(4) = 0; μ(6) = +1 | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | X–X–I |
| Movement | φ(22) = 10 | X(14,4) → 10 cells right → NG(14,14) |

NG(14,14) is the center of the 27 × 27 matrix.

## 3. Read and decrypt

From NG(14,14), read five runes rightward. Subtract the repeating X–X–I key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,14) | NG = 21 | X = 14 | 21 − 14 ≡ 7 | W |
| (14,15) | P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| (14,16) | EO = 12 | I = 10 | 12 − 10 ≡ 2 | TH |
| (14,17) | O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| (14,18) | E = 18 | X = 14 | 18 − 14 ≡ 4 | R |

### WEATHER

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Row alignment | W–EA–TH (row 13, columns 14–16) lies above NG–P–EO (row 14). |
| Diagonal mirror | E(6,10) → NG(10,14) → E(14,18), four steps apart; the only E–NG–E mirror found across all axes and distances. |
| OUTER state | (+1, 0, +1) indicates OUTER in the project's interpretation; the final E(14,18) is an outer rune of this mirror. |

These are geometric observations; the decryption is shown above.
