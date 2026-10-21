# 08 — IDEA

## 1. Locate the node

| Row | Column 13 | Column 16 | Column 19 |
|:---:|:---:|:---:|:---:|
| 8 | A | | |
| 11 | | TH | |
| 14 | | | A |

The diagonal A–TH–A has TH(11,16) at its center. Each outer A is three cells away.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | TH = 2; φ(2) = 1 = U | A–U–A |
| Totient signature | φ(A = 24) = 8; φ(U = 1) = 1; φ(A = 24) = 8 | (8, 1, 8) |
| Möbius signature | μ(8) = 0; μ(1) = +1; μ(8) = 0 | (0, +1, 0) |
| Rotation | (0 + 1 + 0) mod 3 = 1 | U–A–A |
| Movement | From A(14,19), one cell down-right | J(15,20) |

## 3. Read and decrypt

From J(15,20), read three runes diagonally down-left. Subtract the U–A–A key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (15,20) | J = 11 | U = 1 | 11 − 1 ≡ 10 | I |
| (16,19) | E = 18 | A = 24 | 18 − 24 ≡ 23 | D |
| (17,18) | D = 23 | A = 24 | 23 − 24 ≡ 28 | EA |

### IDEA

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Diagonal mirror | J(15,20)–D(17,18)–J(19,16), with D(17,18) at the center. |
| CENTER state | The key's Möbius signature (0, +1, 0) indicates CENTER in the project's interpretation, matching the final D. |
