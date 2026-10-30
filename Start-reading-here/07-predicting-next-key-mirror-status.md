# Predicting the Next Key’s Mirror Status

**Original node geometry · LP2 pages 0–2**

The distance between two cells in the current block predicts whether the next original key node has matching outer runes.

## 1. Define the node type

Use the **original three-rune node** in the matrix, before transforming its center rune or rotating the derived key. Its cells lie on a horizontal, vertical, or 45° diagonal line at equal spacing.

| Node type | Original outer runes |
| :--- | :--- |
| Mirror | Equal |
| Non-mirror | Different |

## 2. Select the two current cells

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Cell to select |
| :--- | :--- |
| Z | Current node’s lower outer cell; for a horizontal node, its right outer cell |
| L | Current ciphertext’s leftmost cell: smallest column, bottommost cell in a tie |

Keep the selected original node fixed throughout the calculation.

In the formulas, `r(X)` and `c(X)` denote a cell’s row and column.

## 3. Calculate the distance and remainder

Use the **Chebyshev distance**: the fewest one-cell moves between Z and L when horizontal, vertical, and diagonal moves are allowed.

$$
d=\max\bigl(|r(Z)-r(L)|,\ |c(Z)-c(L)|\bigr).
$$

A diagonal move counts as **one step**.

Take `d mod 3` and predict the **next** original node’s type:

| Remainder | Next node |
| :---: | :--- |
| 0 or 1 | Mirror — equal outer runes |
| 2 | Non-mirror — different outer runes |

## 4. Example: WEATHER → TURNS

WEATHER’s original node is:

**`X(14,4) – OE(14,5) – X(14,6)`**

Its right outer cell is **Z = (14,6)**. The current ciphertext’s leftmost cell is **L = (14,14)**.

$$
d=\max(|14-14|,|6-14|)=\max(0,8)=8.
$$

$$
8\bmod3=2.
$$

**Prediction: the next node is non-mirror.**

TURNS uses **H–NG–C**. Its outer runes H and C differ, matching the prediction.

## 5. What the result establishes

The rule matches **16/16 transitions** in the selected research reconstruction: **14 mirror** and **2 non-mirror** outcomes. The non-mirror predictions are WEATHER → TURNS and YOU → SOON. Always predicting mirror would already score 14/16.

The rule was found using this route; independent validation is still needed. It predicts the node’s class, while its exact runes, location, and the next plaintext remain undetermined.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

