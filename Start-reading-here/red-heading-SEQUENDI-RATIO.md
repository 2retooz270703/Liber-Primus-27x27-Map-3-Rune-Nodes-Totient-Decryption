# Reading the Red Heading

**Candidate title: SEQUENDI RATIO — “a method of following”**

The two keys below produce **SECUENDI RATIO**. Reading its C/K rune as Q gives the proposed Latin spelling **SEQUENDI RATIO**. The alphabet has no separate Q rune; this interpretation leaves the rune’s value, 5, unchanged.

## 1. What is being decrypted?

The red heading contains these two groups, occupying the first 13 cells of the matrix’s top row:

**`S H E O G M IA F • S Y E NG C`**

The first group has eight runes; the second has five. Labels such as IA and NG each represent one rune.

| Group | Reading direction | Repeating key |
| :--- | :--- | :--- |
| First eight runes | Right to left | X–N–X–C |
| Last five runes | Left to right | J–TH–TH |

Each word starts with the first rune of its own key.

## 2. How the subtraction works

Each rune has a number from **0 to 28**. Subtract the key rune’s number from the encrypted rune’s number. If the answer is negative, add **29**. Convert the result back to a rune.

For example, the first word begins with F when read backwards:

**F(0) − X(14) = −14; add 29 to get 15, which is S.**

Repeat the key until the word ends.

## 3. First word: a key from four corners

### Find the key in the matrix

Coordinates use **(row, column)**, counted from 1. Rows increase downward; columns increase to the right.

Four matrix cells form this rectangle:

| Row | Column 3 | Column 9 |
| :--- | :--- | :--- |
| 6 | X | N |
| 24 | C/K | X |

Start at the upper-left corner and read clockwise: **X → N → X → C**. These four runes form the repeating key.

The rectangle connects to earlier parts of the proposed plaintext route:

- The two opposite X corners are equally distant from the opening **J(13,12)**.
- The original MAP key source, **EO(15,9)–X(16,9)–I(17,9)**, lies along the rectangle’s right side. Its center rune X supplies the symbol used for the opposite corners.

The reported search finds one rectangle satisfying these conditions.

### Read backwards and subtract

Reverse the order of the eight heading runes. Keep IA together as one symbol.

| Step | Rune sequence |
| :--- | :--- |
| Read the encrypted word backwards | F · IA · M · G · O · E · H · S |
| Repeat the key | X · N · X · C · X · N · X · C |
| After subtraction | S · E · C · U · E · N · D · I |

The literal result is **SECUENDI**.

## 4. Second word: a key built from MAP

### Find the three key cells

Use the proposed MAP stage:

1. Its original key center is **X(16,9)**.
2. Its ciphertext ends at **AE(17,13)**: one row down and four columns right.
3. Repeat that move from AE. It reaches **R(18,17)**.
4. The opening **J(13,12)** is five rows above and five columns left of R. Continue five rows down and five columns right from R to reach **TH(23,22)**.

These three cells form an equally spaced diagonal:

**`J(13,12) – R(18,17) – TH(23,22)`**

Apply the project’s center-rune transformation: **R has index 4, and φ(4) = 2**, the index of TH. The key becomes **J–TH–TH**.

The project’s phase calculation gives **0**, so this key stays in that order.

### Read forwards and subtract

| Step | Rune sequence |
| :--- | :--- |
| Read the encrypted word forwards | S · Y · E · NG · C |
| Repeat the key | J · TH · TH · J · TH |
| Subtract rune numbers | R · A · T · I · O |

The result is **RATIO**.

## 5. What remains uncertain

These remain candidate constructions. Both depend on the proposed MAP reading, and the rectangle conditions were formulated after finding the first word and key.

A general rule has yet to explain the different key shapes, reading directions, and starting positions. The heading also does not fit the existing rules for the next ordinary block after MAP, so it remains a separate heading hypothesis.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
