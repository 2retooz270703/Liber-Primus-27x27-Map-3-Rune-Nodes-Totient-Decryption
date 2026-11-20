# 06 — The opening key and the final Gematria Primus sum

**The 118 plaintext runes from the opening block through `DIE` have a total Gematria Primus value of 5,360. The opening key gives exactly the same number when the map position of its first cell is multiplied by the rune index at its reflection across the main diagonal.**

## The two factors on the map

The opening key starts at row 13, column 11. On the 27 × 27 map, cells are numbered from 1, left to right and top to bottom. Twelve complete rows precede this cell, so its position is **12 × 27 + 11 = 335**.

Reflection across the main diagonal exchanges row and column. The opening cell **(13, 11)** therefore reflects to **(11, 13)**, which contains the rune **T**. Its zero-based index in the project's 29-rune alphabet is **16**. This reflected cell also serves as the first key cell of `I ASK`, the block immediately before `DIE`.

The product uses two distinct quantities: the **map position** of the opening cell and the **alphabet index** of the rune in the reflected cell. Their product is **335 × 16 = 5,360**.

## The final block supplies the exact remainder

For the plaintext total, each rune contributes its Gematria Primus prime value. The first 34 blocks, ending with `YOU`, contribute 4,709. The next four blocks, `GO | DO | AS | I ASK`, contribute 464. This brings the subtotal through `I ASK` to **5,173** across 115 runes.

| Plaintext rune in block 39 | GP value | Running plaintext total |
|---|---:|---:|
| D | 89 | 5,262 |
| I | 31 | 5,293 |
| E | 67 | **5,360** |

The difference between the opening-key product and the subtotal through `I ASK` is **5,360 − 5,173 = 187**. The three runes of `DIE` contribute precisely **89 + 31 + 67 = 187**.

The other terminal branch reads `WINGING` from indices `(7,21,21)`, or W·ING·ING. The corresponding primes are 19, 79 and 79, so the branch contributes 177 GP to the shared 5,173 prefix and totals **5,350**. Both final blocks contain three runes. [Terminal-route replay](../Start-reading-here/27-key-alignment-from-node-geometry.md)

## What the equality establishes

**GP(plaintext through DIE) = 4,709 + 464 + 187 = 5,360 = 335 × 16.**

For the recorded route through `I ASK`, this gives a concrete test of any proposed final block. To reach the opening-key product, its runes must contribute exactly 187 GP. Addition is insensitive to rune order, so the route's key and ciphertext supply the reading order.
