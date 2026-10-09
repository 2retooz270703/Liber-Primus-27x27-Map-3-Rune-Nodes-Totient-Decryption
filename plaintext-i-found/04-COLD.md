# 04 — COLD

## 1. Locate the node

After TURNS, return to A(14,19). The previous key gives φ(NG = 21) = 12. Phase 0 selects DOWN + LEFT: V₀(14,19) = (+1, −1).

| Movement from A(14,19) | Destination | Role |
|:---|:---|:---|
| DOWN 12 | TH(26,19) | Center of H–TH–H |
| LEFT 12 | G(14,7) | Ciphertext start |

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | TH = 2; φ(2) = 1 = U | H–U–H |
| Totient signature | φ(H = 8) = 4; φ(U = 1) = 1; φ(H = 8) = 4 | (4, 1, 4) |
| Möbius signature | μ(4) = 0; μ(1) = +1; μ(4) = 0 | (0, +1, 0) |
| Rotation | (0 + 1 + 0) mod 3 = 1 | U–H–H |

## 3. Read and decrypt

From G(14,7), read four runes upward. Subtract the repeating U–H–H key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (14,7) | G = 6 | U = 1 | 6 − 1 ≡ 5 | C |
| (13,7) | J = 11 | H = 8 | 11 − 8 ≡ 3 | O |
| (12,7) | EA = 28 | H = 8 | 28 − 8 ≡ 20 | L |
| (11,7) | A = 24 | U = 1 | 24 − 1 ≡ 23 | D |

### COLD

This completes the sequence: AS I GO, THE WEATHER TURNS COLD.

## 4. Connections to I MAY

| Connection | Evidence |
|:---|:---|
| CENTER state | The Möbius signature (0, +1, 0) indicates CENTER in the project's interpretation. The final A(11,7) is the center of EA(10,7)–A(11,7)–EA(12,7). |
| Shared signature | EA–A–EA gives (φ(28), φ(24), φ(28)) = (12, 8, 12). The next transformed node, NG–T–NG, has the same signature. |
| Next direction | Phase 1 at A(11,7): μ(φ(11)) = μ(10) = +1; μ(φ(7)) = μ(6) = +1 → DOWN + RIGHT. |

Using the key's values 4 and 1: A(11,7) → DOWN 4 → S(15,7) → RIGHT 1 → B(15,8), center of NG–B–NG.

Continue to [05 — I MAY](./05-I-MAY.md).
