# 06 — CRY

## 1. Locate the node

The I MAY ciphertext ends at E(26,16), the lower rune of E–X–E.

| Row | Column 15 | Column 16 | Column 17 |
|:---:|:---:|:---:|:---:|
| 24 | D | E | F |
| 25 | EA | X | D |
| 26 | EA | E | T |

X(25,16) is the center of the vertical E–X–E node.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | X = 14; φ(14) = 6 = G | E–G–E |
| Totient signature | φ(E = 18) = 6; φ(G = 6) = 2; φ(E = 18) = 6 | (6, 2, 6) |
| Möbius signature | μ(6) = +1; μ(2) = −1; μ(6) = +1 | (+1, −1, +1) |
| Rotation | (1 − 1 + 1) mod 3 = 1 | G–E–E |
| Movement | φ(X = 14) = 6 | X(25,16) → 6 cells up → J(19,16) |

J(19,16) is the center of the vertical OE–J–OE node.

## 3. Read and decrypt

From J(19,16), read three runes upward. Subtract the G–E–E key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (19,16) | J = 11 | G = 6 | 11 − 6 ≡ 5 | C |
| (18,16) | OE = 22 | E = 18 | 22 − 18 ≡ 4 | R |
| (17,16) | S = 15 | E = 18 | 15 − 18 ≡ 26 | Y |

The final S(17,16) is an outer rune of S–IA–S, spaced 6 cells apart. The center IA(17,10) also gives φ²(IA = 27) = 6.

### CRY
