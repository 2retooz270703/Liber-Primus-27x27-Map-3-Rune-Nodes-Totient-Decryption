# 14 — YOU

## 1. Locate the node

The SEE key has phase 0. At B(27,14), this gives V₀ = (0, +1) → RIGHT.

Its neutral signature (0, 0, 0) retains the center I = 10. Applying φ twice gives φ²(10) = 2, leading 2 cells right to P(27,16).

| Row | Column 14 | Column 16 | Column 18 |
|:---:|:---:|:---:|:---:|
| 5 | | P | |
| 16 | | R | |
| 27 | B | P | EA |

P(27,16) is the lower outer rune of the vertical P–R–P mirror. Each P is 11 cells from R(16,16).

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | R = 4; φ(4) = 2 = TH | P–TH–P |
| Totient signature | φ(P = 13) = 12; φ(TH = 2) = 1; φ(P = 13) = 12 | (12, 1, 12) |
| Möbius signature | μ(12) = 0; μ(1) = +1; μ(12) = 0 | (0, +1, 0) |
| Rotation | (0 + 1 + 0) mod 3 = 1 | TH–P–P |
| Movement | φ²(I = 10) = 2; φ(R = 4) = 2 | B → P → EA (right 2 each time) |

## 3. Read and decrypt

From EA(27,18), read three runes diagonally up-left. Subtract the TH–P–P key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (27,18) | EA = 28 | TH = 2 | 28 − 2 ≡ 26 | Y |
| (26,17) | T = 16 | P = 13 | 16 − 13 ≡ 3 | O |
| (25,16) | X = 14 | P = 13 | 14 − 13 ≡ 1 | U |

### YOU

The final X(25,16) is the center of E(24,16)–X(25,16)–E(26,16), matching the key's CENTER state (0, +1, 0).
