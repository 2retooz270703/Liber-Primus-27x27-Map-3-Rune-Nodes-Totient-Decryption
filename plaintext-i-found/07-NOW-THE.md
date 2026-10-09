# 07 — NOW THE

## 1. Locate the node

The CRY key gives the distance 6. It leads to J(19,16), the center of OE–J–OE, and TH(11,16), where the ciphertext begins.

| Row | Column 15 | Column 16 | Column 17 |
|:---:|:---:|:---:|:---:|
| 18 | X | OE | R |
| 19 | F | J | A |
| 20 | I | OE | M |

The central J(19,16) forms the vertical OE–J–OE node.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | J = 11; φ(11) = 10 = I | OE–I–OE |
| Totient signature | φ(OE = 22) = 10; φ(I = 10) = 4; φ(OE = 22) = 10 | (10, 4, 10) |
| Möbius signature | μ(10) = +1; μ(4) = 0; μ(10) = +1 | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | OE–OE–I |
| Movement | From the CRY key: φ(X = 14) = 6 | X(25,16) → J(19,16) (up 6); S(17,16) → TH(11,16) (up 6) |

## 3. Read and decrypt

From TH(11,16), read five runes diagonally down-right. Subtract the repeating OE–OE–I key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (11,16) | TH = 2 | OE = 22 | 2 − 22 ≡ 9 | N |
| (12,17) | AE = 25 | OE = 22 | 25 − 22 ≡ 3 | O |
| (13,18) | B = 17 | I = 10 | 17 − 10 ≡ 7 | W |
| (14,19) | A = 24 | OE = 22 | 24 − 22 ≡ 2 | TH |
| (15,20) | J = 11 | OE = 22 | 11 − 22 ≡ 18 | E |

### NOW THE

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Shared distance | S(17,4)–IA(17,10)–S(17,16) and TH(11,16)–IA(17,10)–TH(23,4) both have radius 6. Also, φ²(IA = 27) = 6. |
| Equal prime sums | CRY: 13 + 11 + 103 = 127; NOW THE: 29 + 7 + 19 + 5 + 67 = 127. |
| Prime index | 127 is the 31st prime; the transformed center I has prime value 31. |
| OUTER state | (+1, 0, +1) indicates OUTER in the project's interpretation. The final J(15,20) is an outer rune of J(15,20)–D(17,18)–J(19,16). |

These are additional geometric and numerical observations; the decryption is shown above.
