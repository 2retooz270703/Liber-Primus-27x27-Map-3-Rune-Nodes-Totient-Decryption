# 13 — SEE

## 1. Locate the nodes

The DEATH key has phase 2. At E(26,1), this gives V₂ = (0, +1) → RIGHT.

Here φ²(26) = φ(12) = 4, matching the radius of EA–J–EA.

| Node | First outer | Center | Second outer |
|:---|:---:|:---:|:---:|
| EA–J–EA | EA(25,2) | J(25,6) | EA(25,10) |
| E–X–E | E(24,16) | X(25,16) | E(26,16) |

EA(25,2) is one cell up-right from E(26,1). Its mirror generates the key.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | J = 11; φ(11) = 10 = I | EA–I–EA |
| Totient signature | φ(EA = 28) = 12; φ(I = 10) = 4; φ(EA = 28) = 12 | (12, 4, 12) |
| Möbius signature | μ(12) = 0; μ(4) = 0; μ(12) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | φ(11) + φ²(11) = 10 + 4 = 14 | EA(25,2) → 14 cells right → X(25,16) |

## 3. Read and decrypt

From X(25,16), read three runes diagonally down-left. Subtract the EA–I–EA key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (25,16) | X = 14 | EA = 28 | 14 − 28 ≡ 15 | S |
| (26,15) | EA = 28 | I = 10 | 28 − 10 ≡ 18 | E |
| (27,14) | B = 17 | EA = 28 | 17 − 28 ≡ 18 | E |

### SEE
