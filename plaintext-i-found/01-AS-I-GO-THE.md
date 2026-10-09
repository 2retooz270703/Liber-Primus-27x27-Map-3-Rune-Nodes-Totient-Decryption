# 01 — AS I GO, THE

## 1. Find the key and starting point

Pages 0–2 of *Liber Primus* contain **729 runes**, arranged row by row into a **27×27 matrix**.

In row 13, we find:

`AE(13,11) — J(13,12) — EA(13,13)`

The center rune **J = 11** gives:

- **Key:** φ(11) = 10 = I → **AE-I-EA**
- **Rotation:** φ(AE, I, EA) = (20, 4, 12); μ(20, 4, 12) = (0, 0, 0) → phase 0, so the key stays unchanged.
- **Movement:** φ(11) + φ(10) = 10 + 4 = **14**

Starting from **AE(13,11)**, move **14 cells right** to **L(13,25)**.

## 2. Decrypt the seven runes

Starting at **L(13,25)**, read seven consecutive runes. The sequence crosses from the end of row 13 into row 14.

```text
Cipher: L  AE N  TH P  U  X
Key:    AE I  EA AE I  EA AE
Plain:  A  S  I  G  O  TH E
```

Subtract the repeating key from the ciphertext **modulo 29**.

For example: `L(20) − AE(25) ≡ 24 = A (mod 29)`.

The seven runes produce **AS I GO, THE**.

## 3. Find the next key

The final ciphertext rune **X(14,4)** also begins another three-rune structure:

`X(14,4) — OE(14,5) — X(14,6)`

Its center gives **φ(OE = 22) = 10 = I**.

Thus **X-OE-X → X-I-X**, forming the next key structure.

The continuation to **WEATHER** is covered in [`02-WEATHER.md`](./02-WEATHER.md).
