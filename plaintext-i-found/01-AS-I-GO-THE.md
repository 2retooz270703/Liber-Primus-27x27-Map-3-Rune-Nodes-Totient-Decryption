# 01 — AS I GO, THE

729 runes are arranged in reading order into a 27 × 27 matrix. Coordinates are given as (row, column).

## 1. Locate the three-rune structure

This 3 × 3 region contains the first node in its middle row:

| Matrix row | Column 11 | Column 12 | Column 13 |
| :---: | :---: | :---: | :---: |
| 12 | M | H | M |
| 13 | AE | J | EA |
| 14 | EO | AE | OE |

The node is AE (13,11) — J (13,12) — EA (13,13). Its center, J, provides both the key and the first movement distance.

## 2. Derive the key and starting position

Transform the center J with Euler's totient function, leaving AE and EA unchanged. The Möbius signature determines whether the resulting key is rotated.

| Step | Starting values | Calculation | Result |
| :--- | :--- | :--- | :--- |
| Create the key | AE — J — EA | φ(J = 11) = 10 = I | AE — I — EA |
| Totient signature | AE = 25, I = 10, EA = 28 | φ(25) = 20; φ(10) = 4; φ(28) = 12 | (20, 4, 12) |
| Möbius signature | (20, 4, 12) | μ(20) = 0; μ(4) = 0; μ(12) = 0 | (0, 0, 0) |
| Key rotation | (0, 0, 0) | (0 + 0 + 0) mod 3 = 0 | Phase 0: no rotation |
| First movement | J = 11 | φ(11) + φ(10) = 10 + 4 = 14 | 14 cells right |

Start at the node's left rune, AE (13,11). Moving 14 cells right lands on L (13,25), the first ciphertext rune.

## 3. Decrypt the seven runes

Read forward from L (13,25), crossing from the end of row 13 to the start of row 14. Repeat the key AE — I — EA and subtract each key value from its ciphertext value modulo 29.

| Position | Matrix cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | (13,25) | L = 20 | AE = 25 | 20 − 25 ≡ 24 | A |
| 2 | (13,26) | AE = 25 | I = 10 | 25 − 10 = 15 | S |
| 3 | (13,27) | N = 9 | EA = 28 | 9 − 28 ≡ 10 | I |
| 4 | (14,1) | TH = 2 | AE = 25 | 2 − 25 ≡ 6 | G |
| 5 | (14,2) | P = 13 | I = 10 | 13 − 10 = 3 | O |
| 6 | (14,3) | U = 1 | EA = 28 | 1 − 28 ≡ 2 | TH |
| 7 | (14,4) | X = 14 | AE = 25 | 14 − 25 ≡ 18 | E |

Plaintext runes: A — S — I — G — O — TH — E

### AS I GO, THE

Spaces and the comma are added for readability.

## 4. Continue to the next key

The last ciphertext rune, X (14,4), also begins the next horizontal three-rune node.

| Stage | Left cell (14,4) | Center cell (14,5) | Right cell (14,6) |
| :--- | :---: | :---: | :---: |
| Original node | X | OE | X |
| Center calculation | X | φ(OE = 22) = 10 = I | X |
| Next key | X | I | X |

The resulting key, X — I — X, leads into [02 — WEATHER](./02-WEATHER.md).
