# 04 — COLD

## 1. Locate the node

After TURNS, return to A(14,19).

| Row | Column 18 | Column 19 | Column 20 |
|:---:|:---:|:---:|:---:|
| 25 | W | H | EA |
| 26 | G | TH | H |
| 27 | EA | H | D |

At A, the TURNS key's phase 0 gives V₀(14,19) = (+1, −1) → DOWN + LEFT.

The vertical H–TH–H forms the next key; G(14,7) begins the ciphertext.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | TH = 2; φ(2) = 1 = U | H–U–H |
| Totient signature | φ(H = 8) = 4; φ(U = 1) = 1; φ(H = 8) = 4 | (4, 1, 4) |
| Möbius signature | μ(4) = 0; μ(1) = +1; μ(4) = 0 | (0, +1, 0) |
| Rotation | (0 + 1 + 0) mod 3 = 1 | U–H–H |
| Movement | φ(NG = 21) = 12 | A → TH (down 12); A → G (left 12) |

## 3. Read and decrypt

From G(14,7), read four runes upward. Subtract the repeating U–H–H key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,7) | G = 6 | U = 1 | 6 − 1 ≡ 5 | C |
| (13,7) | J = 11 | H = 8 | 11 − 8 ≡ 3 | O |
| (12,7) | EA = 28 | H = 8 | 28 − 8 ≡ 20 | L |
| (11,7) | A = 24 | U = 1 | 24 − 1 ≡ 23 | D |

### COLD

## 4. Connections to I MAY

| Connection | Evidence |
|:---|:---|
| CENTER state | (0, +1, 0) indicates CENTER in the project's interpretation; the final A(11,7) is the center of EA(10,7)–A(11,7)–EA(12,7). |
| Shared signature | EA–A–EA and NG–T–NG both give (12, 8, 12). The latter comes from NG–B–NG through φ(B = 17) = 16 = T. |

For I MAY, the COLD key's phase 1 gives V₁(11,7) = (μ(φ(11)), μ(φ(7))) = (μ(10), μ(6)) = (+1, +1) → DOWN + RIGHT.

Using distances 4 and 1: A(11,7) → S(15,7) (down 4) → B(15,8) (right 1), center of NG–B–NG

Continue to [05 — I MAY](./05-I-MAY.md).
