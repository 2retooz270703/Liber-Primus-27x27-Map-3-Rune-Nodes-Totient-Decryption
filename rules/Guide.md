# Reading the 27 × 27 Matrix

### A geometric approach to Liber Primus · LP2, pages 0–2

The proposed reading of pages 0–2 begins with a different assumption from an ordinary line-by-line transcription: the runes in the 27 × 27 matrix may be read in selected groups, and the information needed to decipher one group may be encoded in the geometry around it. In this approach, the matrix is not simply a page of ciphertext. It is also a map of possible keys, directions, and connections between passages.

The method brings together three operations. **Three-rune structures** provide the keys used to turn ciphertext into readable text. **Totient and Möbius calculations** determine how those keys are aligned and help describe movement through the matrix. **Geometric mirrors** connect distant or overlapping cells and offer an additional way to check the proposed route.

These operations are easiest to understand in that order. First, we will decode a complete example. Then we will examine how a reading can move from one passage to another. Finally, we will look at why a cell's position inside a mirror matters.

> **Scope.** This is a readable account of the method and the examples recorded on the selected LP2 route. It explains the decryption, movement, and mirror observations together. It does not replace the separate work on predicting the *next* key's complete signature, nor does it establish a unique solution for the entire matrix.

---

## 1. The basic idea: a cipher and a map

Each cell has two kinds of information: **a rune** and **a position**. Both matter, but they serve different purposes. The rune has a numerical index in the 29-symbol cipher alphabet. Its row and column indicate where it sits in the 27 × 27 matrix.

Coordinates in this report are **one-based**: the top-left cell is `(1,1)`, rows increase downward, and columns increase to the right. A label such as `E(14,18)` means that the cell at row 14, column 18 contains the rune `E`.

The arithmetic relies on two number-theoretic functions:

- **Euler's totient, `φ(n)`**, counts the positive integers up to `n` that are relatively prime to `n`. For example, `φ(22) = 10` and `φ(14) = 6`.
- **The Möbius function, `μ(n)`**, returns `+1`, `0`, or `−1`. It gives `0` when `n` has a squared prime factor; otherwise, its sign depends on whether `n` has an even or odd number of distinct prime factors. For example, `μ(6) = +1`, `μ(4) = 0`, and `μ(10) = +1`.

In practice, `φ` produces useful numerical transformations, while `μ` reduces those results to compact three-state signs. The same pair of functions appears in both the key and movement calculations.

### How the pieces fit together

A typical reading follows this sequence:

1. Locate a three-rune structure associated with a ciphertext block.
2. Derive a three-rune key from that structure.
3. Calculate the key's **phase** to choose its cyclic starting position.
4. Repeat the aligned key and subtract its indices from the ciphertext **modulo 29**.
5. Examine the block's endpoint, coordinate-derived directions, and nearby mirror structures to investigate the next passage.

The first four steps explain how the recorded words are decrypted. The fifth explains how their proposed spatial connections are investigated.

---

## 2. From a three-rune structure to a key

A recurring motif in the matrix is a group of three runes. Some are **mirrors**: the two outer runes are identical and are positioned symmetrically around a center. The center can be transformed to derive a key while the two outer values stay unchanged.

Consider the structure:

**`X – OE – X`**

The rune `OE` has index `22`. Applying Euler's totient gives `φ(22) = 10`, which is the index of `I`. Only the center changes:

| Position | Structure | Derived key |
|:--|:--:|:--:|
| Left | `X` | `X` |
| Center | `OE` (`22`) | `I` (`10`) |
| Right | `X` | `X` |

Thus the structure becomes the key **`X – I – X`**.

For a structure whose center is transformed this way, the general rule is:

```text
(a, b, c)  →  (a, φ(b), c)
```

The output of `φ(b)` is read through the same rune-index correspondence used by the cipher.

This transformation is important, but it is **not applied indiscriminately to every three-rune group**. The recorded route also includes non-mirrored keys such as `H – NG – C`, which are used directly. We therefore distinguish the *geometric structure found in the matrix* from the *actual three-rune key used for subtraction*. In some cases they are different; in others they are the same.

## 3. The Möbius signature determines key alignment

Knowing the three key runes is not yet sufficient. A repeating three-rune key can begin at any of its three positions, and different alignments produce different plaintext.

The proposed method resolves that choice using a **phase**, calculated from the key's Möbius signature.

Start with the derived key **`X – I – X`**. Its indices are `(14, 10, 14)`. Apply `φ` to each index, and then apply `μ` to the three results:

| Operation | Left | Center | Right |
|:--|:--:|:--:|:--:|
| Key index | `14` | `10` | `14` |
| Totient `φ` | `6` | `4` | `6` |
| Möbius `μ` | `+1` | `0` | `+1` |

The final row, **`(+1, 0, +1)`**, is the key's Möbius signature. Add its three components and take the result modulo three:

```text
phase = (1 + 0 + 1) mod 3 = 2
```

The phase tells us how many positions to rotate the key **cyclically to the left**:

| Phase | Key alignment |
|:--:|:--|
| `0` | `X – I – X` |
| `1` | `I – X – X` |
| `2` | `X – X – I` |

For this example, phase `2` selects **`X – X – I`**.

Here *rotation* means a cyclic rearrangement of the three key runes. It does **not** mean physically rotating the 27 × 27 matrix.

For a derived key with indices `k1, k2, k3`, the general phase rule is:

```text
p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3
```

The full signature must also be kept. Two keys may share a phase while having different three-component signatures, so the phase and the signature convey different levels of information.

---

## 4. A complete example: decrypting WEATHER

The `WEATHER` example ties the previous steps together and shows what the arithmetic actually produces.

On the selected route, its ciphertext occupies **row 14, columns 14–18**:

```text
NG – P – EO – O – E
```

The derived key is `X – I – X`, whose phase is `2`. We therefore use `X – X – I`, repeating its three runes until the key stream is as long as the five-rune ciphertext:

```text
Ciphertext:  NG   P    EO   O    E
Key stream:  X    X    I    X    X
```

Subtract each key index from the corresponding ciphertext index, taking the result **modulo 29**. A negative difference wraps around into the range of the 29-rune alphabet; for example, `13 − 14 = −1`, which is congruent to `28` modulo 29.

| Cipher | Key | Difference `mod 29` | Output |
|:--:|:--:|:--:|:--:|
| `NG = 21` | `X = 14` | `7` | `W` |
| `P = 13` | `X = 14` | `28` | `EA` |
| `EO = 12` | `I = 10` | `2` | `TH` |
| `O = 3` | `X = 14` | `18` | `E` |
| `E = 18` | `X = 14` | `4` | `R` |

This yields the rune sequence:

```text
W – EA – TH – E – R
```

Read in the alphabet's Latin transliteration, the sequence spells **WEATHER**.

This matters for two reasons. First, the ciphertext runes do not visually resemble the recovered word; the word appears only after the numerical subtraction. Second, the alignment is supplied by a calculation on the *key itself*, rather than by simply trying all three key positions and selecting the most attractive English result.

At this point, however, the calculation has established a reading of **one selected ciphertext block with one selected key**. It has not, by itself, explained how the next block is chosen. That is where the coordinate rules enter.

---

## 5. Moving from one passage to another

The movement observations treat the end of a ciphertext block as a possible starting point for navigating to another key structure. A proposed move has two separate ingredients:

- **Direction** is derived from the current key's phase and the row/column values of a selected cell.
- **Distance** is drawn from totient values associated with the key or a nearby structure.

It is useful to keep these operations separate. The direction rule can be stated compactly; the rule choosing which available totient values become distances is not yet universal across all recorded stages.

### 5.1. Turning a phase into a direction

Let `(r,c)` be a cell's coordinates and `p` the current key's phase. Apply the totient function to **each coordinate exactly `p` times**, then apply the Möbius function:

```text
T_p(r,c) = (φ^p(r), φ^p(c))
V_p(r,c) = (μ(φ^p(r)), μ(φ^p(c)))
```

`T_p` preserves the transformed numerical values, while `V_p` converts them into direction signs. When `p = 0`, the coordinates are used unchanged before applying `μ`.

| Möbius sign | Row movement | Column movement |
|:--:|:--|:--|
| `−1` | Up | Left |
| `+1` | Down | Right |
| `0` | Unspecified | Unspecified |

Rows increase downward and columns increase rightward, so these signs have an unambiguous geometric interpretation. A `0` does **not** automatically mean "stay in place"; rather, that coordinate receives no direction from this sign rule.

One practical subtlety is the **anchor cell**. Some examples use the last ciphertext cell, while another recorded transition uses an immediately adjacent cell. For instance, `WEATHER` ends at `E(14,18)`, but its next coordinate check is made at `A(14,19)`. The choice of anchor must therefore be stated for each example instead of silently assumed.

### 5.2. A worked transition: COLD → I MAY

For `COLD`, the recorded key is **`H – U – H`**, with rune indices `(8, 1, 8)`.

Applying the totient function to its components gives:

```text
φ(8) = 4
φ(1) = 1
φ(8) = 4
```

The resulting values are `(4, 1, 4)`. Their Möbius signature is `(0, +1, 0)`, so the phase is `(0 + 1 + 0) mod 3 = 1`. In this recorded transition, **4** and **1** are used as the two movement distances.

The `COLD` ciphertext ends at `A(11,7)`. Its key has phase `1`, so we apply `φ` once to each coordinate:

```text
Row:     11 → φ(11) = 10 → μ(10) = +1 → DOWN
Column:   7 →  φ(7) =  6 →  μ(6) = +1 → RIGHT
```

With a downward move of four cells and a rightward move of one cell, the route is:

```text
A(11,7)
   ↓ 4 cells
S(15,7)
   → 1 cell
B(15,8)
```

The destination `B(15,8)` is the center of **`NG – B – NG`**, the next recorded three-rune structure.

This example is especially useful because the arithmetic and the geometry meet at a specific location. The phase supplies **down/right**; the key's totient values supply **4/1**; and the resulting destination is a meaningful node rather than just an arbitrary empty coordinate.

The broader records also contain other distance constructions. One uses `φ(OE) = 10`; another uses two successive totients, `φ(J) = 10` and `φ(φ(J)) = 4`, whose sum is `14`. These are concrete observed constructions, but they do not yet amount to a single rule that always selects the correct distance before the destination is known.

### 5.3. What happens when Möbius gives zero?

The `END` example explains why it is important to retain `T_p` alongside the final direction signs.

`END` ends at **`I(21,23)`** and has phase `2`. We therefore apply the totient function twice:

```text
Row:     21 → 12 → 4
Column:  23 → 22 → 10
```

Applying `μ` to these transformed values gives:

```text
T_2(21,23) = (4, 10)
V_2(21,23) = (0, +1)
```

The column points **right**, but the row's `0` leaves its direction unspecified. Nevertheless, the transformed row value **4** has not disappeared: it matches the index of the center rune `R` in the nearby **`I – R – I`** mirror.

Other recorded transitions use a retained totient value in a different geometric role, such as a mirror radius. The important distinction is that **the sign is a directional output, while the number before the sign can still be relevant to the geometry**. Discarding that number would discard part of the observed relationship.

---

## 6. Mirrors: geometry beyond the ciphertext line

A mirror is a three-cell arrangement with two identical outer runes, placed at equal distances on opposite sides of a center. The alignment can be horizontal, vertical, or diagonal.

Consider the diagonal mirror **`J – D – J`**:

| Role | Rune | Cell |
|:--|:--:|:--:|
| First outer | `J` | `(15,20)` |
| Center | `D` | `(17,18)` |
| Second outer | `J` | `(19,16)` |

From the center, one outer cell is two rows above and two columns right; the other is two rows below and two columns left. Their coordinate offsets are equal and opposite:

```text
J(15,20)   (-2,+2) relative to D
D(17,18)    center
J(19,16)   (+2,-2) relative to D
```

The equal-and-opposite offsets, rather than any particular reading direction, identify this arrangement as a mirror.

### 6.1. A cell can participate in several structures

The map is not divided into isolated, non-overlapping triples. The same rune cell can function as the center of one structure and an outer point of another.

For example:

- `J(19,16)` is the **center** of `OE – J – OE`, but an **outer rune** in both `J – D – J` and `J – B – J`.
- `R(21,22)` is the **center** of both `I – R – I` and `H – R – H`.

These shared cells matter because they connect otherwise separate structures through an exact coordinate. When a route reaches a shared cell, the geometry can suggest more than one nearby relationship. The role of the cell—center or outer—is therefore a useful part of evaluating a proposed reading.

### 6.2. Endpoint roles and Möbius signatures

The `J – D – J` mirror also provides a comparison between two recovered passages: **`NOW THE`** and **`IDEA`**. Their ciphertext blocks end at different members of the same structure.

For `NOW THE`, the recorded key is `OE – I – OE`:

```text
φ signature:  (10, 4, 10)
μ signature:  (+1, 0, +1)
Endpoint:     J(15,20) — OUTER in J–D–J
```

For `IDEA`, the recorded key is `A – U – A`:

```text
φ signature:  (8, 1, 8)
μ signature:  (0, +1, 0)
Endpoint:     D(17,18) — CENTER in J–D–J
```

This is a particularly clear connection: the endpoints occupy **different roles inside the same mirror**, and their key signatures differ in a corresponding way. In the first case the outer signature components are nonzero; in the second the center component is nonzero.

The same center/outer correspondence appears in four additional recorded stages:

| Passage | Key's `μ` signature | Endpoint's mirror role |
|:--|:--|:--|
| `COLD` | `(0,+1,0)` | `A(11,7)`: center of `EA–A–EA` |
| `IS` | `(0,+1,0)` | `D(21,10)`: center of `E–D–E` |
| `WEATHER` | `(+1,0,+1)` | `E(14,18)`: outer of `E–NG–E` |
| `END` | `(+1,0,+1)` | `I(21,23)`: outer of `I–R–I` |

Taken together, these examples show a recurring pattern on the recorded route:

**`(0,+1,0)` is associated with center endpoints, while `(+1,0,+1)` is associated with outer endpoints.**

The association gives a second way to inspect a proposed passage. A block can decrypt to recognizable text, but its endpoint may also lie in a mirror whose role agrees with its key's Möbius signature. Such agreement connects the arithmetic of the key with the spatial structure of the matrix. It is a consistency check, not a substitute for finding the ciphertext and its key.

---

## 7. One reading, three complementary layers

The three mechanisms answer different questions about a candidate passage:

| Layer | Main question | What is calculated or checked? |
|:--|:--|:--|
| **Decryption** | *What does this block say?* | Three-rune key, phase, cyclic alignment, subtraction modulo 29 |
| **Movement** | *Where might the reading continue?* | Coordinate signs, totient-derived distances, destination node |
| **Mirrors** | *How does that location connect to the map?* | Equal spacing, shared cells, center/outer endpoint role |

The `WEATHER` block illustrates the first and third layers together. Its selected ciphertext `NG – P – EO – O – E`, decrypted with the phase-aligned key `X – X – I`, produces `W – EA – TH – E – R`. Its last cell, `E(14,18)`, is also an outer member of `E – NG – E`, consistent with the key's `(+1,0,+1)` signature.

The `COLD → I MAY` transition illustrates the second layer. Starting at `A(11,7)`, the phase gives down/right directions and totient values supply distances of four and one, landing on `B(15,8)`, the center of `NG – B – NG`. The destination is meaningful because it belongs to another three-rune structure.

The `NOW THE` and `IDEA` endpoints illustrate the third layer especially well. They do not merely occupy nearby cells: they belong to the *same* `J – D – J` mirror, with different roles that correspond to their different key signatures.

Together, these examples explain why the approach treats plaintext, key arithmetic, and spatial geometry as parts of one investigation rather than as three unrelated collections of numerical coincidences.

## 8. What is specified, and what still needs a rule

The **decryption operation** is fully explicit once the ciphertext coordinates and the derived three-rune key have been selected: calculate the signature and phase, cycle the key, and subtract modulo 29. The examples above make each operation reproducible.

The **navigation procedure** is less complete. The direction signs have a compact formula, but the recorded examples do not yet provide a universal way to choose the movement distance. They also do not always select the anchor cell in the same way: some calculations start at the endpoint, while the `WEATHER` example uses its adjacent `A(14,19)` cell. A zero Möbius sign can leave one movement direction open, even when its underlying totient value supplies a geometric clue.

The **mirror observations** are exact statements about specified cells and their roles in the selected map. Their recurring correspondence with key signatures strengthens the internal coherence of the proposed route. It does not alone select a unique continuation among all possible mirror structures.

This distinction is central to using the method properly: **a successful decryption, a plausible move, and a matching mirror role are three different pieces of evidence**. The strongest candidate passages are those that satisfy all applicable checks without changing the rules from one example to the next.

---

## Reference: formulas at a glance

**Center-totient key derivation (when applicable)**

```text
(a, b, c) → (a, φ(b), c)
```

**Möbius signature and cyclic key phase**

```text
σ(K) = (μ(φ(k1)), μ(φ(k2)), μ(φ(k3)))
p    = [σ1 + σ2 + σ3] mod 3
```

**Rune decryption**

```text
plaintext_index = (ciphertext_index − aligned_key_index) mod 29
```

**Coordinate transforms for movement**

```text
T_p(r,c) = (φ^p(r), φ^p(c))
V_p(r,c) = (μ(φ^p(r)), μ(φ^p(c)))
```

The functions are applied to **rune indices** in the first three formulas and to **cell coordinates** in the last two. Keeping those inputs distinct prevents a common source of confusion.

---

*Research context: [Liber Primus — 27 × 27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). This guide consolidates the original decryption, movement, and mirror notes into a single explanation for the recorded LP2 pages 0–2 route.*
