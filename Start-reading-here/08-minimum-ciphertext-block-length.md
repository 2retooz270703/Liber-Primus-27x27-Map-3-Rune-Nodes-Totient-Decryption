# Minimum Ciphertext Block Length

**Two-rune search filter · LP2 pages 0–2**

## 1. Proposed rule

Require **at least two runes per independently decrypted ciphertext block** when searching for continuations.

Let `N` be the number of ciphertext cells read continuously with one assigned key stream. Each cell produces one decrypted rune. Keep blocks where:

$$
N\ge2.
$$

A block may contain several English words. Count runes using the project’s **29-rune alphabet**: `TH` and `EA` each count as one rune.

## 2. Examples

| Independent block | Decrypted runes | Rune count | Filter result |
| :--- | :--- | ---: | :--- |
| THE | TH · E | 2 | Keep |
| I MAY | I · M · A · Y | 4 | Keep |
| I | I | 1 | Reject |

The word **I** in **I MAY** belongs to the four-rune block and receives no separate key assignment.

A three-rune key node can still decrypt a two-rune ciphertext block.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

