# 01 — AS I GO, THE

The 729 runes form a 27 × 27 matrix. Coordinates are given as (row, column).

## 1. Locate the node

| Row | Column 11 | Column 12 | Column 13 |
|:---:|:---:|:---:|:---:|
| 12 | M | H | M |
| 13 | AE | J | EA |
| 14 | EO | AE | OE |

The middle row forms AE–J–EA, with J at (13,12).

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | J = 11; φ(11) = 10 = I | AE–I–EA |
| Totient signature | φ(AE = 25) = 20; φ(I = 10) = 4; φ(EA = 28) = 12 | (20, 4, 12) |
| Möbius signature | μ(20) = 0; μ(4) = 0; μ(12) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | φ(11) + φ(10) = 10 + 4 = 14 | AE(13,11) → 14 cells right → L(13,25) |

## 3. Read and decrypt

Read forward from L(13,25), continuing from the end of row 13 to the start of row 14. Subtract the repeating key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (13,25) | L = 20 | AE = 25 | 20 − 25 ≡ 24 | A |
| (13,26) | AE = 25 | I = 10 | 25 − 10 = 15 | S |
| (13,27) | N = 9 | EA = 28 | 9 − 28 ≡ 10 | I |
| (14,1) | TH = 2 | AE = 25 | 2 − 25 ≡ 6 | G |
| (14,2) | P = 13 | I = 10 | 13 − 10 = 3 | O |
| (14,3) | U = 1 | EA = 28 | 1 − 28 ≡ 2 | TH |
| (14,4) | X = 14 | AE = 25 | 14 − 25 ≡ 18 | E |

### AS I GO, THE

The final X(14,4) also starts the next node: X(14,4) – OE(14,5) – X(14,6). Its center gives φ(OE = 22) = 10 = I, producing the next key X–I–X.

Continue to [02 — WEATHER](./02-WEATHER.md).
