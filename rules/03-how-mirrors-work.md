# 03 — How Mirrors Work

*Mirror structures → Shared cells → CENTER / OUTER*

Mirrors connect different parts of the 27 × 27 matrix. The full Möbius signature from Rule 01 can also help us recognize the role of a ciphertext endpoint within these structures.

## 1. Recognize a mirror

A mirror has two matching outer runes, equally spaced from a center. The three cells can lie along a row, column, or diagonal.

For example, **J–D–J** is a diagonal mirror:

| | First outer | Center | Second outer |
|:---|:---:|:---:|:---:|
| Rune | J | D | J |
| Cell | (15,20) | (17,18) | (19,16) |

Each outer J is **2 diagonal steps** from D(17,18). This distance is the mirror's *radius*.

Mirrors can have different radii. Not every three-rune structure is a mirror: `H–NG–C`, for example, has different outer runes.

## 2. Follow shared cells

A cell can belong to several structures. Its role depends on which structure we are examining.

| Shared cell | Structure | Role |
|:---|:---|:---|
| J(19,16) | OE–J–OE | CENTER |
| J(19,16) | J–D–J; J–B–J | OUTER |
| R(21,22) | I–R–I; H–R–H | CENTER |

For example, **END** finishes at I(21,23), an outer rune of I–R–I. Its center, R(21,22), is also the center of H–R–H, which supplies the key for **IS**.

A shared cell provides a connection, but does not automatically tell us which structure to follow next.

## 3. Check the Möbius state

Rule 01 adds three μ values to select the key's phase. Here we keep the **full three-value signature**, because it preserves which positions have 0 or +1.

The J–D–J mirror gives a clear comparison between **NOW THE** and **IDEA**:

| | NOW THE | IDEA |
|:---|:---:|:---:|
| Key | OE–I–OE | A–U–A |
| φ signature | (10, 4, 10) | (8, 1, 8) |
| μ signature | (+1, 0, +1) | (0, +1, 0) |
| Last ciphertext cell | J(15,20) | D(17,18) |
| Role in J–D–J | OUTER | CENTER |

The same correspondence appears in four other recorded stages:

| Stage | μ signature | Final cell | Mirror role |
|:---|:---:|:---:|:---|
| COLD | (0, +1, 0) | A(11,7) | CENTER of EA–A–EA |
| IS | (0, +1, 0) | D(21,10) | CENTER of E–D–E |
| WEATHER | (+1, 0, +1) | E(14,18) | OUTER of E–NG–E |
| END | (+1, 0, +1) | I(21,23) | OUTER of I–R–I |

These observations suggest two useful constraints:

**(0, +1, 0) → CENTER-compatible**  
**(+1, 0, +1) → OUTER-compatible**

The full signature matters because different signatures can produce the same phase. For example, `(0,+1,0)` and `(+1,−1,+1)` both give phase 1, but their individual values are different.

Other states, including `(0,0,0)`, `(+1,−1,+1)`, and `(+1,+1,+1)`, do not yet have a confirmed general CENTER / OUTER rule.

These are repeated matches in the reconstructed route, not a proven method for selecting a unique next mirror. Distances, directions, and geometry still need to agree.
