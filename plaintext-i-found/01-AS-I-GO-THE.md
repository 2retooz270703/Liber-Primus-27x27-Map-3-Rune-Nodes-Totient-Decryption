# 01 — AS I GO, THE

Pages 0–2 contain 729 runes. Reading them in order produces a **27 × 27 matrix**.

## 1. Find the key and starting cell

The sequence AE (13,11) — J (13,12) — EA (13,13) provides both the key and the first move.

| Step | Calculation | Result |
|:--|:--|:--|
| Key | φ(J = 11) = 10 = I | **AE–I–EA** |
| Rotation | φ(AE, I, EA) = (20, 4, 12); μ = (0, 0, 0) | Phase 0 — no rotation |
| Move | φ(11) + φ(10) = 10 + 4 = 14 | AE (13,11) → **L (13,25)** |

## 2. Decrypt the seven runes

Starting at L (13,25), read the next seven runes in order, crossing from row 13 into row 14. Repeat the key AE–I–EA and subtract **modulo 29**.

| Cell | Cipher | Key | (Cipher − Key) mod 29 | Plaintext |
|:--|:--:|:--:|:--:|:--:|
| (13,25) | L = 20 | AE = 25 | 24 | A |
| (13,26) | AE = 25 | I = 10 | 15 | S |
| (13,27) | N = 9 | EA = 28 | 10 | I |
| (14,1) | TH = 2 | AE = 25 | 6 | G |
| (14,2) | P = 13 | I = 10 | 3 | O |
| (14,3) | U = 1 | EA = 28 | 2 | TH |
| (14,4) | X = 14 | AE = 25 | 18 | E |

Result: **AS I GO, THE**

## 3. Continue to WEATHER

The last ciphertext cell, X (14,4), begins the next three-rune sequence.

| Sequence | Center transformation | Next key |
|:--|:--|:--|
| X (14,4) — OE (14,5) — X (14,6) | φ(OE = 22) = 10 = I | **X–I–X** |

Next: [02 — WEATHER](./02-WEATHER.md).
