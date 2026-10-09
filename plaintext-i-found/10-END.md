# 10 — END

## 1. Locate the nodes

The OF THE ciphertext ends at J(19,16). One cell left is F(19,15), part of the horizontal F–X–F mirror.

| Row | Column 15 | Column 19 | Column 23 |
|:---:|:---:|:---:|:---:|
| 15 | | Y | |
| 19 | F | X | F |
| 23 | | Y | |

F–X–F and Y–X–Y share the center X(19,19), with a radius of 4. The diagonal J(19,16)–B(23,12)–J(27,8) provides the key.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | B = 17; φ(17) = 16 = T | J–T–J |
| Totient signature | φ(J = 11) = 10; φ(T = 16) = 8; φ(J = 11) = 10 | (10, 8, 10) |
| Möbius signature | μ(10) = +1; μ(8) = 0; μ(10) = +1 | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | J–J–T |
| Movement | F–X–F, radius 4 | F(19,15) → X(19,19) → F(19,23), right 4 each |

## 3. Read and decrypt

From F(19,23), read three runes downward. Subtract the J–J–T key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (19,23) | F = 0 | J = 11 | 0 − 11 ≡ 18 | E |
| (20,23) | L = 20 | J = 11 | 20 − 11 ≡ 9 | N |
| (21,23) | I = 10 | T = 16 | 10 − 16 ≡ 23 | D |

The final I(21,23) is an outer rune of I(21,21)–R(21,22)–I(21,23), matching the key's OUTER state (+1, 0, +1).

### END
