# 01 — How Runes Become Plaintext

The decryption uses a three-rune key. Euler's totient (`φ`) helps form it, Möbius (`μ`) fixes its order, and subtraction modulo 29 reveals the text.

Three-rune structure → key → phase → repeating key → plaintext

## 1. The rune numbers

The 729 runes from pages 0–2 are arranged into a **27 × 27 matrix**, left to right and row by row. Positions use `(row, column)`, starting at `(1,1)`.

Each rune has a **Gematria Primus index from 0 to 28**. These are not the separate prime-number values. `TH`, `EA`, and `NG`, for example, are each **one rune**, not two letters for calculation purposes.

## 2. How a key is formed

A selected three-rune structure supplies the key. In a *mirror*, the two outer runes match and are equally spaced from the center. Mirrors can run horizontally, vertically, or diagonally.

Usually, only the center changes: replace its index with `φ(center)` and convert that number back into a rune.

| Original structure | Center transformation | Key |
|:---:|:---:|:---:|
| H–TH–H | TH = 2 → φ(2) = 1 = U | H–U–H |

`φ(n)` counts the integers from 1 to *n* that share no factor with *n* other than 1.

Not every selected structure is a mirror. For example, the non-mirrored `H–NG–C` is used directly as a key in [TURNS](../plaintext-i-found/03-TURNS.md).

## 3. How the key's order is chosen

A three-rune key has **three possible starting positions**. Its *phase* chooses one by calculation, rather than by trying different orders.

Apply `φ` to **all three runes of the key**, then `μ` to the three results. **Add the Möbius values modulo 3** to get the phase:

| Operation | Calculation | Result |
|:---|:---|:---|
| Totient signature | φ(8), φ(1), φ(8) | (4, 1, 4) |
| Möbius signature | μ(4), μ(1), μ(4) | (0, +1, 0) |
| Phase | (0 + 1 + 0) mod 3 | 1 |

`μ(n)` is **0** if a squared prime divides *n*; otherwise it is **+1** or **−1** for an even or odd number of distinct prime factors. In particular, `μ(1) = +1`.

The phase rotates the key to the left:

| Phase | Order for H–U–H |
|:---:|:---:|
| 0 | H–U–H |
| 1 | U–H–H |
| 2 | H–H–U |

The example gives **phase 1**, so the active key is `U–H–H`. Keep the full Möbius signature `(0,+1,0)` as well: later rules also use its individual signs.

## 4. How the text is recovered

Repeat the rotated key for as many runes as the selected ciphertext contains. Then subtract rune indices, **ciphertext minus key, modulo 29**.

For the four-rune ciphertext `G–J–EA–A`:

| | 1 | 2 | 3 | 4 |
|:---|:---:|:---:|:---:|:---:|
| Ciphertext | G = 6 | J = 11 | EA = 28 | A = 24 |
| Key | U = 1 | H = 8 | H = 8 | U = 1 |
| Subtract (mod 29) | 5 | 3 | 20 | 23 |
| Plaintext | C | O | L | D |

The result is **COLD**. Modulo 29 keeps the answer between 0 and 28: for example, `13 − 27 = −14 ≡ 15 (mod 29)`.

---

These rules explain **how a chosen key decrypts a chosen ciphertext**. They do not yet determine which structure to use next, where the ciphertext starts, or which direction to read. Those are separate parts of the route reconstruction.
