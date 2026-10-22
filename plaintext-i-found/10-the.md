# 10 — THE

## 1. Locate the nodes

| Row | Column 15 | Column 16 | Column 17 |
|:---:|:---:|:---:|:---:|
| 18 | X | OE | R |
| 19 | F | J | A |
| 20 | I | OE | M |

J(19,16) connects two nodes: the vertical OE–J–OE and the diagonal J(15,20)–D(17,18)–J(19,16).

## 2. Derive the key and starting point

The vertical OE–J–OE provides the key.

| Step | Calculation | Result |
|:---|:---|:---|
| Key | J = 11; φ(11) = 10 = I | OE–I–OE |
| Totient signature | φ(OE = 22) = 10; φ(I = 10) = 4; φ(OE = 22) = 10 | (10, 4, 10) |
| Möbius signature | μ(10) = +1; μ(4) = 0; μ(10) = +1 | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | OE–OE–I; use OE–OE |
| Movement | One cell right of J(19,16) | A(19,17) |

## 3. Read and decrypt

From A(19,17), read two runes leftward. Subtract the OE–OE key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (19,17) | A = 24 | OE = 22 | 24 − 22 ≡ 2 | TH |
| (19,16) | J = 11 | OE = 22 | 11 − 22 ≡ 18 | E |

**Plaintext: THE**
