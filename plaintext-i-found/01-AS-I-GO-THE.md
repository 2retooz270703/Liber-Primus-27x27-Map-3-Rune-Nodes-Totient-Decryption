# 01 — AS I GO, THE

The 729 runes are arranged into a 27 × 27 matrix. Coordinates are written as (row, column).

## 1. Find the starting node

| Matrix row | Column 11 | Column 12 | Column 13 |
|:---:|:---:|:---:|:---:|
| 12 | M | H | M |
| 13 | AE | J | EA |
| 14 | EO | AE | OE |

The middle row gives the node AE–J–EA, centered on J(13,12).

## 2. Find the key and starting cell

| Step | Starting values | Calculation | Result |
|---|---|---|---|
| Key | AE–J–EA; J = 11 | φ(11) = 10 = I | AE–I–EA |
| Totient signature | AE = 25; I = 10; EA = 28 | φ(25) = 20; φ(10) = 4; φ(28) = 12 | (20, 4, 12) |
| Möbius signature | (20, 4, 12) | μ(20) = μ(4) = μ(12) = 0 | (0, 0, 0) |
| Key rotation | (0, 0, 0) | (0 + 0 + 0) mod 3 = 0 | No rotation |
| First movement | AE(13,11) | φ(11) + φ(10) = 14; move right | L(13,25) |

## 3. Read and decrypt

From L(13,25), read seven runes in sequence, continuing at the start of row 14. Subtract the repeating key modulo 29.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Cell | (13,25) | (13,26) | (13,27) | (14,1) | (14,2) | (14,3) | (14,4) |
| Ciphertext | L = 20 | AE = 25 | N = 9 | TH = 2 | P = 13 | U = 1 | X = 14 |
| Key | AE = 25 | I = 10 | EA = 28 | AE = 25 | I = 10 | EA = 28 | AE = 25 |
| Subtraction | 20 − 25 ≡ 24 | 25 − 10 = 15 | 9 − 28 ≡ 10 | 2 − 25 ≡ 6 | 13 − 10 = 3 | 1 − 28 ≡ 2 | 14 − 25 ≡ 18 |
| Plaintext | A | S | I | G | O | TH | E |

### AS I GO, THE

The final cell begins a new node: X(14,4)–OE(14,5)–X(14,6). Since φ(22) = 10 = I, its key is X–I–X → [02 — WEATHER](./02-WEATHER.md).
