# The Red Heading: SEQUENDI RATIO

**Two candidate key constructions · LP2 pages 0–2**

The selected keys produce the literal output **SECUENDI RATIO**. The proposed Latin reading, **SEQUENDI RATIO**, means approximately **“a method of following.”**

## 1. Ciphertext, method, and anchors

The red heading occupies **row 1, columns 1–13** of the 27 × 27 matrix:

**`S H E O G M IA F • S Y E NG C`**

The two words contain **8 and 5 runes**. The separator occupies no cell; `IA` and `NG` each represent one rune.

Use rune indices **0–28** and repeated-key subtraction:

$$
P_i=(C_i-K_i)\bmod29.
$$

Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right. Both constructions use these anchors from the proposed route:

| Anchor | Position or source |
| :--- | :--- |
| Opening J | J(13,12) |
| Original MAP node | EO(15,9) – X(16,9) – I(17,9) |
| MAP node center M | X(16,9) |
| MAP ciphertext endpoint E | AE(17,13) |

**MAP is part of the candidate continuation**, so constructions based on it inherit that uncertainty.

## 2. First word: SECUENDI

### Select the rectangle

Use the MAP center’s rune, **X**. Find pairs of X cells that:

1. Are equally distant from the opening J.
2. Form opposite corners of a rectangle with sides parallel to the grid.
3. Place the entire original MAP node along one side.

The reported search selects one rectangle:

| Clockwise order | Corner | Rune | Coordinate |
| ---: | :--- | :--- | :--- |
| 1 | Upper left | X | (6,3) |
| 2 | Upper right | N | (6,9) |
| 3 | Lower right | X | (24,9) |
| 4 | Lower left | C/K | (24,3) |

The two X corners each have **squared distance 130** from J. The MAP source lies along the right side, at column 9.

This selector was formulated **after the word and key were found**. Its uniqueness applies to these specific conditions.

### Decrypt

Read the corners clockwise from the upper left to obtain the direct, period-four key **X–N–X–C**.

Reverse the first ciphertext word **by rune**, keeping IA intact, then repeat the key:

| Stage | Rune indices |
| :--- | :--- |
| Ciphertext, right to left | 0, 27, 19, 6, 3, 18, 8, 15 |
| Repeated key | 14, 9, 14, 5, 14, 9, 14, 5 |
| Output modulo 29 | 15, 18, 5, 1, 18, 9, 23, 10 |

**Literal result: S–E–C–U–E–N–D–I → SECUENDI.**

## 3. Second word: RATIO

### Extend the MAP displacement

Extend the vector from the MAP center M to its endpoint E by the same amount:

$$
R'=2E-M=2(17,13)-(16,9)=(18,17).
$$

That cell contains **R**. Reflect the opening J through this new center:

$$
Z=2R'-J=2(18,17)-(13,12)=(23,22).
$$

That cell contains **TH**, giving the equally spaced diagonal node:

**`J(13,12) – R(18,17) – TH(23,22)`**

Apply Euler’s totient to the center’s rune index: **φ(4) = 2**, turning R into TH. The derived key is **J–TH–TH = (11,2,2)**.

Its Möbius signature **(+1,+1,+1)** gives phase **0**. Repeat the key in this order.

### Decrypt

Read the second ciphertext word **left to right**:

| Stage | Rune indices |
| :--- | :--- |
| Ciphertext | 15, 26, 18, 21, 5 |
| Repeated key | 11, 2, 2, 11, 2 |
| Output modulo 29 | 4, 24, 16, 10, 3 |

**Result: R–A–T–I–O → RATIO.**

## 4. The Latin interpretation

The first output’s third rune is **C/K, index 5**. The alphabet has no separate Q rune.

Reading that symbol as **Q** gives **SEQUENDI RATIO**. This is a proposed spelling convention; the numerical output remains **SECUENDI RATIO**, with every rune index unchanged.

## 5. What remains unresolved

The two words use different key lengths and reading directions. No established general rule yet predicts both constructions, their starting positions, or the reversal of the first word.

The heading also fails the existing rules for the next ordinary block after MAP. It remains a **separate heading hypothesis**.

The specified keys reproduce all 13 output runes. Whether these choices reflect the intended cipher requires independent evidence.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

