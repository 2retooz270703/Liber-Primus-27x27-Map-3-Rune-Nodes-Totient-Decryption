# Minimum Ciphertext Block Length

**A Proposed Constraint on Single-Rune Decryptions**

*LP2 pages 0–2 · 29-rune alphabet · Block-based plaintext*

---

## Observation

In the selected reconstruction, **no ciphertext is decrypted as an isolated single-rune block**. Single-letter words such as **I** appear within longer plaintext blocks rather than being assigned their own ciphertext and key:

| Recorded block | Decrypted runes | Rune count |
|---|---|---:|
| [AS I GO, THE](../plaintext-i-found/01-as-i-go-the.md) | `A · S · I · G · O · TH · E` | 7 |
| [I MAY](../plaintext-i-found/05-i-may.md) | `I · M · A · Y` | 4 |
| [OF](../plaintext-i-found/09-of.md) | `O · F` | 2 |
| [THE](../plaintext-i-found/10-the.md) | `TH · E` | 2 |

**Rune count is not the same as English letter count:** `TH` is one rune.

## Proposed Search Constraint

**Require at least two runes per independently decrypted ciphertext block.** Single-letter words may still occur *inside* a longer block, but standalone one-rune candidates should be excluded from continuation searches. One-rune decryptions are especially flexible and can generate many false-positive branches.

**Status:** This is an observed property of the **selected reconstruction**, not yet proof that the original encryption algorithm cannot produce a one-rune block. Treat the minimum length as a proposed filter to test against future evidence.
