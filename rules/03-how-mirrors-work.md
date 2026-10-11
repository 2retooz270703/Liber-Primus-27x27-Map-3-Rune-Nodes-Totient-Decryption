# 03 — How Mirrors Work

*Mirrors → Shared cells → Möbius states*

A mirror is a three-rune structure with matching outer runes. Mirrors can link different parts of the matrix, while the full Möbius signature can help identify the role of a ciphertext endpoint.

## 1. Recognize a mirror

The outer runes must be equally spaced from the center, along a row, column, or diagonal.

For example, **J–D–J** is a diagonal mirror:

| | First outer | Center | Second outer |
|:---|:---:|:---:|:---:|
| Rune | J | D | J |
| Cell | (15,20) | (17,18) | (19,16) |

Each J is **2 diagonal steps** from D(17,18). This distance is the mirror's *radius*.

Not every three-rune structure is a mirror. For example, `H–NG–C` has different outer runes.

## 2. Follow shared cells

One cell can belong to several structures. Its role depends on which structure we are looking at.

| Cell | Structure | Role |
|:---|:---|:---:|
| J(19,16) | OE–J–OE | CENTER |
| J(19,16) | J–D–J, J–B–J | OUTER |
| R(21,22) | I–R–I, H–R–H | CENTER |

For example, **END** ends at I(21,23), an outer of **I–R–I**. Its center, R(21,22), is also the center of **H–R–H**, which supplies the key for **IS**.

Shared cells connect structures, but do not by themselves determine which one to follow next.

## 3. Check the Möbius state

Rule 01 uses the sum of three μ values to rotate a key. Here we keep all three values, since their positions can also matter.

**NOW THE** and **IDEA** end at different positions in the same **J–D–J** mirror:

| | NOW THE | IDEA |
|:---|:---:|:---:|
| Key | OE–I–OE | A–U–A |
| φ signature | (10, 4, 10) | (8, 1, 8) |
| μ signature | (+1, 0, +1) | (0, +1, 0) |
| Endpoint | J(15,20) | D(17,18) |
| Role in J–D–J | OUTER | CENTER |

The same pattern appears in four other stages:

| Stage | μ signature | Endpoint | Role |
|:---|:---:|:---:|:---|
| COLD | (0, +1, 0) | A(11,7) | CENTER of EA–A–EA |
| IS | (0, +1, 0) | D(21,10) | CENTER of E–D–E |
| WEATHER | (+1, 0, +1) | E(14,18) | OUTER of E–NG–E |
| END | (+1, 0, +1) | I(21,23) | OUTER of I–R–I |

These observations suggest two possible constraints:

**(0, +1, 0) → CENTER-compatible**  
**(+1, 0, +1) → OUTER-compatible**

Different signatures can produce the same phase: (0, +1, 0) and (+1, −1, +1) both give phase 1. Their geometric roles need not be the same.

Other states, including (0, 0, 0) and (+1, +1, +1), do not yet have an established CENTER / OUTER meaning.

These are repeated correspondences, not a rule that uniquely selects the next mirror. Distance, direction, and geometry must still agree.
