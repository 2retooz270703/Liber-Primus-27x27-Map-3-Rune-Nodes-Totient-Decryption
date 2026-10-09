# 01 — AS I GO, THE

The 729 runes form a 27 × 27 matrix, filled in reading order. All coordinates below use (row, column).

## 1. The starting pattern

A 3 × 3 area of the matrix contains the first three-rune node:

| Row | Column 11 | Column 12 | Column 13 |
|:---:|:---:|:---:|:---:|
| 12 | M | H | M |
| 13 | AE | J | EA |
| 14 | EO | AE | OE |

The middle row, AE(13,11) — J(13,12) — EA(13,13), is the starting node. Its center, J, determines both the key and the first movement.

## 2. The key and starting position

| Step | Calculation | Result |
|---|---|---|
| Form the key | J = 11 → φ(11) = 10 = I | AE–I–EA |
| Totient signature | φ(25) = 20; φ(10) = 4; φ(28) = 12 | (20, 4, 12) |
| Möbius signature | μ(20) = μ(4) = μ(12) = 0 | (0, 0, 0) |
| Key rotation | (0 + 0 + 0) mod 3 = 0 | No rotation |
| Movement | φ(11) + φ(10) = 10 + 4 | 14 cells right |

Starting at AE(13,11), move 14 cells right to L(13,25). This is where the ciphertext begins.

## 3. The decryption

Read seven runes from L(13,25), continuing into the next row after column 27. Repeat the key AE–I–EA and subtract it from the ciphertext modulo 29.

| Matrix cell | Cipher rune | Key rune | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (13,25) | L = 20 | AE = 25 | 20 − 25 ≡ 24 | A |
| (13,26) | AE = 25 | I = 10 | 25 − 10 = 15 | S |
| (13,27) | N = 9 | EA = 28 | 9 − 28 ≡ 10 | I |
| (14,1) | TH = 2 | AE = 25 | 2 − 25 ≡ 6 | G |
| (14,2) | P = 13 | I = 10 | 13 − 10 = 3 | O |
| (14,3) | U = 1 | EA = 28 | 1 − 28 ≡ 2 | TH |
| (14,4) | X = 14 | AE = 25 | 14 − 25 ≡ 18 | E |

### AS I GO, THE

The seven plaintext runes are A–S–I–G–O–TH–E. Word spacing and punctuation are added for readability.

## 4. The next connection

The last ciphertext rune, X(14,4), is also the first rune of another three-rune node:

X(14,4) — OE(14,5) — X(14,6)

Its center gives φ(OE = 22) = 10 = I, changing X–OE–X into X–I–X. This is the key structure for the continuation in [02 — WEATHER](./02-WEATHER.md).
