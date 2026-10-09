# 05 — I MAY

## 1. Locate the node

The COLD key has phase 1. At A(11,7), this gives V₁ = (+1, +1) → DOWN + RIGHT.

| Row | Column 7 | Column 8 | Column 9 |
|:---:|:---:|:---:|:---:|
| 13 | J | NG | L |
| 14 | G | P | F |
| 15 | S/Z | B | EO |
| 16 | AE | C/K | X |
| 17 | D | NG | I |

B(15,8) is the center of the vertical NG–B–NG node.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | B = 17; φ(17) = 16 = T | NG–T–NG |
| Totient signature | φ(NG = 21) = 12; φ(T = 16) = 8; φ(NG = 21) = 12 | (12, 8, 12) |
| Möbius signature | μ(12) = 0; μ(8) = 0; μ(12) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | From the COLD key: φ(H = 8) = 4; φ(U = 1) = 1 | A(11,7) → B(15,8) (down 4, right 1) |

The COLD endpoint A(11,7) is also the center of EA–A–EA. Its totient signature, (φ(28), φ(24), φ(28)) = (12, 8, 12), matches the new key.

## 3. Read and decrypt

From TH(26,19), the center of the H–TH–H node, read four runes leftward. Subtract the repeating NG–T–NG key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (26,19) | TH = 2 | NG = 21 | 2 − 21 ≡ 10 | I |
| (26,18) | G = 6 | T = 16 | 6 − 16 ≡ 19 | M |
| (26,17) | T = 16 | NG = 21 | 16 − 21 ≡ 24 | A |
| (26,16) | E = 18 | NG = 21 | 18 − 21 ≡ 26 | Y |

### I MAY
