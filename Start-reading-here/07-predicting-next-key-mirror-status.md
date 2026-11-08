# Predicting the Next Key’s Mirror Status

The distance between two cells in the current block predicts whether the next original key node **has matching outer runes**.

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

### Direct implementation

`current_node` contains the three original current-node coordinates. Supply `current_cipher_cells` as a nonempty list of ciphertext coordinates in reading order. All coordinates are 1-based `(row, column)` pairs.

The prediction returns **1 for a mirror node and 0 for a non-mirror node**. To check a proposed next key, supply its three **original rune indices** in outer–center–outer order as `next_node_runes`, before any center transformation or cyclic key rotation.

```python
def expected_next_key_mirror_bit(current_node, current_cipher_cells):
    """Predict the next original node's type: 1 = mirror, 0 = non-mirror."""
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

    distance = max(abs(Z[0] - L[0]), abs(Z[1] - L[1]))
    return int(distance % 3 != 2)


def original_node_mirror_bit(original_node_runes):
    """Compare the outer rune indices before key transformation or rotation."""
    return int(original_node_runes[0] == original_node_runes[2])


def accepts_next_key_mirror_status(
    current_node, current_cipher_cells, next_node_runes
):
    """Check a proposed next original node against the predicted mirror bit."""
    predicted = expected_next_key_mirror_bit(current_node, current_cipher_cells)
    return original_node_mirror_bit(next_node_runes) == predicted


# Keep a proposed next key only if:
# accepts_next_key_mirror_status(
#     current_node, current_cipher_cells, next_node_runes
# )
```

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
