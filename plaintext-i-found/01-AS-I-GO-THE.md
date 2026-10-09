# 01 — AS I GO, THE

The 729 runes are arranged in reading order into a 27 × 27 matrix.

## 1. Find the key and starting cell

The key comes from the middle row of this 3 × 3 area:

| Row | Column 11 | Column 12 | Column 13 |
| :--- | :---: | :---: | :---: |
| 12 | M | H | M |
| 13 | AE | J | EA |
| 14 | EO | AE | OE |

The center J (13,12) determines both the key and the movement.

| Step | Starting values | Calculation | Result |
| :--- | :--- | :--- | :--- |
| Key | AE — J — EA | φ(J = 11) = 10 = I | AE — I — EA |
| Rotation | AE = 25, I = 10, EA = 28 | φ → (20, 4, 12); μ → (0, 0, 0) | Phase 0: keep the order |
| Movement | J = 11 | φ(11) + φ(10) = 10 + 4 | 14 cells right |

Start at AE (13,11). Moving 14 cells right leads to L (13,25).

## 2. Decrypt the seven runes

Read from L (13,25), continuing from the end of row 13 to the beginning of row 14. Repeat the key AE — I — EA and subtract modulo 29.

| Cell | Ciphertext | Key | Calculation (mod 29) | Plaintext |
| :--- | :---: | :---: | :---: | :---: |
| (13,25) | L · 20 | AE · 25 | 20 − 25 ≡ 24 | A |
| (13,26) | AE · 25 | I · 10 | 25 − 10 = 15 | S |
| (13,27) | N · 9 | EA · 28 | 9 − 28 ≡ 10 | I |
| (14,1) | TH · 2 | AE · 25 | 2 − 25 ≡ 6 | G |
| (14,2) | P · 13 | I · 10 | 13 − 10 = 3 | O |
| (14,3) | U · 1 | EA · 28 | 1 − 28 ≡ 2 | TH |
| (14,4) | X · 14 | AE · 25 | 14 − 25 ≡ 18 | E |

Plaintext: AS I GO, THE

## 3. Continue to the next key

The last ciphertext rune, X (14,4), is also the first rune of the next structure.

| Cell | Rune | Position in structure | Operation |
| :--- | :---: | :--- | :--- |
| (14,4) | X | Left | Unchanged |
| (14,5) | OE | Center | φ(OE = 22) = 10 = I |
| (14,6) | X | Right | Unchanged |

Next key: X — I — X

Continue in [02 — WEATHER](./02-WEATHER.md).
