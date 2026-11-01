
<p align="center">
  <em>
    As I go, the weather turns cold.<br>
    I may cry now.<br>
    The idea of the end is death.<br>
    See you soon, then.<br>
    The key is to go to the east of the map.
  </em>
</p>

---

## The Approach

My hypothesis is that LP2 pages 0–2 should be treated as a single 27 × 27 matrix of runes, rather than as ordinary lines of text. I believe that the words and sentences we seem to recognize when reading these pages are an illusion. The runes may have been arranged to look like readable text, while the actual message is encrypted within the matrix itself.

Instead of reading the runes in their visible order, I study the matrix as a whole, looking for patterns and relationships between individual cells.

## How the proposed decryption works

1. **Choose a three-rune key node** in the matrix. For applicable nodes, replace the center rune's index `b` by `φ(b)`; some recorded non-mirror nodes use their original indices without this replacement.
2. **Calculate its signature.** For the derived key indices `k₁, k₂, k₃`, compute `μ(φ(k₁)), μ(φ(k₂)), μ(φ(k₃))`. Their sum modulo 3 determines the cyclic left-rotation of the key.
3. **Read a selected ciphertext path** from the matrix, using its recorded starting cell, axis, direction, and length.
4. **Repeat the rotated key** and subtract its indices from the ciphertext indices, modulo 29, to obtain plaintext runes.

For example, the original node `X–OE–X` becomes `X–I–X` after the center transformation. Its Möbius phase is `2`, so its aligned key is `X–X–I`. Applying it to five cells beginning at the matrix center `(14,14)` yields **WEATHER**.

The arithmetic is reproducible once the cells and node have been selected. **Selecting the correct cells and node is the unresolved cryptanalytic problem.** See [Report 00](./Start-reading-here/00-decryption-method.md) for a complete worked example.

## The transition rules: the main research result

After reconstructing the initial route, I searched for relationships between each **current** ciphertext/key and the properties of the **next** one. This produced a collection of proposed rules based on simple operations: coordinate rotations by 90°, 180°, or 270°; parity; distances; greatest common divisors; and Möbius values of cell positions.

The rules constrain different aspects of the next block: its key signature and phase, the parity of its key center, the axis and reading boundary, the row and column parity of selected cells, the next starting point's geometric relation to the current block, and whether the next node is mirrored.

An especially recurring input is the **leftmost cell of the current ciphertext**. This makes me suspect that the positions of the blocks may be related by a consistent geometric construction rather than being chosen independently.

These are **constraints, not yet a complete transition algorithm**. The early rules were developed against the recorded route and therefore need independent testing. Their agreement with a continuation is useful for ranking or rejecting candidates, but it is not proof of a unique solution.

### Research notes and formulas

All the notes below are in **[Start-reading-here/](./Start-reading-here/)**. Each one explains its inputs, formula, and worked examples.

| Report | What it covers |
| :-- | :-- |
| [00 — Decryption method](./Start-reading-here/00-decryption-method.md) | Three-rune keys, totient transformation, Möbius phase, and modulo-29 subtraction |
| [01 — Next-key signature](./Start-reading-here/01-next-key-signature.md) | Predicting the next key's phase and Möbius signature |
| [02 — Leftmost cell and rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md) | Rotated cell indices and whether the next leftmost cell is read first or last |
| [03 — Reading axis](./Start-reading-here/03-predicting-axis-and-reading-direction.md) | Predicting horizontal, vertical, or diagonal alignment |
| [04 — Key-center parity](./Start-reading-here/04-predicting-next-key-center-parity.md) | Predicting the next original node center's row and column parity |
| [05 — Ciphertext row parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md) | Predicting the next endpoint and leftmost-cell row parity |
| [06 — Next starting point](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) | Eight-ray geometry, with a conditional one-cell allowance |
| [07 — Mirror status](./Start-reading-here/07-predicting-next-key-mirror-status.md) | Predicting equal or different outer runes in the next node |
| [08 — Minimum block length](./Start-reading-here/08-minimum-ciphertext-block-length.md) | A proposed filter requiring at least two runes per block |
| [09 — Ciphertext column parity](./Start-reading-here/09-predicting-next-ciphertext-column-parity.md) | Predicting the parity of the next leftmost cell's column |

## Why the continuation matters

The original route ends with **SEE YOU SOON, THEN**. Using the proposed transition constraints to search for subsequent key/ciphertext placements produced the meaningful candidate:

> **THE KEY IS TO GO TO THE EAST OF THE MAP.**

It is notable because the words can be decrypted **in sequence** using selected three-rune keys, while the selected placements also match a substantial set of previously formulated geometric and arithmetic constraints. The candidate `MAP` stage additionally has an exact reflection symmetry involving the initial `J(13,12)` cell.

However, the continuation was found by computational search among possible branches. **It remains a candidate, not a confirmed message**, and passing the filters does not mean no other branches can pass them. The next priority is to reduce this remaining ambiguity using rules that are fixed **before** inspecting the resulting English.

See **[plaintext-i-found/](./plaintext-i-found/)** for all **28 numbered block reports**. Files **01–17** document the original reconstruction; files **18–28** document the candidate continuation. Each report provides the selected node, coordinates, arithmetic, and relevant checks.

## Other evidence and hypotheses

**Numerical and geometric correspondences.** The [Strongest Plaintext Evidence](./Start-reading-here/strongest-plaintext-evidence.md) report collects rune-count, rune-index, Gematria Primus, prime-number, and spatial relationships within the selected route, including possible links to LP1. These equalities are reproducible under their stated counting conventions, but their significance is **interpretive**: a numerical coincidence is not an independent proof of decipherment.

**The red heading.** In the separate [red-heading analysis](./Start-reading-here/red-heading-SEQUENDI-RATIO.md), two proposed keys decrypt the heading into the literal rune sequence **SECUENDI RATIO**. Interpreting the `C/K` rune as `Q` suggests the Latin **SEQUENDI RATIO**, approximately *“a method of following.”* This reading is a **hypothesis**, not an established translation of an authenticated heading. If correct, it could describe the procedure needed to navigate the matrix.

**A possible wider application.** My longer-term hypothesis is that pages 0–2 might demonstrate a method also relevant to other pages of *Liber Primus*. This is speculative. The project does not yet show that the remaining pages use the same construction or that apparently textual features elsewhere are decoys.
