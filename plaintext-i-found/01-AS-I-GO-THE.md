# 01 — AS I GO, THE

*Liber Primus · Pages 0–2*

The 729 runes are arranged in reading order into a 27 × 27 matrix.

## 1. Find the key

The starting structure is in row 13:

AE (13,11) — J (13,12) — EA (13,13)

| Step | Calculation | Result |
| :--- | :--- | :--- |
| Key | φ(J = 11) = 10 = I | AE–I–EA |
| Rotation | φ(AE, I, EA) = (20, 4, 12) → μ = (0, 0, 0) | Phase 0 · unchanged |
| Movement | φ(11) + φ(10) = 10 + 4 | 14 cells right |

From AE (13,11), moving 14 cells right reaches L (13,25).

## 2. Read and decrypt

Starting at L (13,25), read seven consecutive runes. After the end of row 13, continue at the beginning of row 14.

Repeat the key AE–I–EA and subtract its values modulo 29.

| Cell | Cipher − key (mod 29) | Plaintext |
| :--- | :--- | :---: |
| (13,25) | L (20) − AE (25) ≡ 24 | A |
| (13,26) | AE (25) − I (10) ≡ 15 | S |
| (13,27) | N (9) − EA (28) ≡ 10 | I |
| (14,1) | TH (2) − AE (25) ≡ 6 | G |
| (14,2) | P (13) − I (10) ≡ 3 | O |
| (14,3) | U (1) − EA (28) ≡ 2 | TH |
| (14,4) | X (14) − AE (25) ≡ 18 | E |

Plaintext — *AS I GO, THE*

## 3. Continue from X

The final ciphertext rune, X (14,4), also begins the next three-rune structure.

| Structure | Center | Next key |
| :--- | :--- | :--- |
| X (14,4) — OE (14,5) — X (14,6) | φ(OE = 22) = 10 = I | X–I–X |

Next: [02 — WEATHER](./02-WEATHER.md)
