# Predicting the Next Key-Node Axis Group

## 1. What is new?

The earlier reports constrain the next key's signature, phase, center parity, and mirror status, together with several properties of the next ciphertext. In particular, [Report 03](03-predicting-axis-and-reading-direction.md) predicts the **ciphertext's** axis and reading boundary.

The present proposal concerns a different object: the three equally spaced cells of the **original source node from which the next key is derived**. Before applying a center transformation or cyclic key rotation, that node lies on one of four undirected axes:

| Axis number | Original key-node axis | Predicted bit b |
| ---: | --- | :---: |
| 0 | Horizontal, W–E | 0 |
| 1 | Diagonal, NW–SE | 0 |
| 2 | Vertical, N–S | 1 |
| 3 | Diagonal, NE–SW | 1 |

The formula chooses **one of these two groups**, leaving two possible axes. It does not select a complete axis, source position, radius, or plaintext word.

## 2. Coordinates and inputs

Use the project's **27 × 27** matrix with 1-based `(row, column)` coordinates. Rows increase downward; columns increase to the right.

All three inputs belong to the **current** block:

| Symbol | Meaning |
| --- | --- |
| M | Center of the current original three-rune key node |
| Z | Lower outer cell of that node; for a horizontal node, the right outer cell |
| L | Leftmost current ciphertext cell: smallest column, bottommost on ties |

These are geometric definitions. Reversing the recorded order of the same physical source node does not change M or Z. Likewise, L need not be the first ciphertext cell read.

Let the absolute row-major cell indices at 0°, 90°, and 180° clockwise rotation be

$$
n_0(r,c)=27(r-1)+c,
$$

$$
n_1(r,c)=27(c-1)+28-r,
\qquad
n_2(r,c)=730-n_0(r,c).
$$

Here `n₁` and `n₂` are indices of the same original cell after rotating its coordinates. They do not designate additional locations from which runes are read.

## 3. Proposed rule

Calculate

$$
\boxed{X=n_1(M)+n_2(Z),\qquad Y=n_1(L)+n_2(Z).}
$$

Then compare **whether the two Möbius values are negative**:

| Comparison of μ(X) and μ(Y) | Permitted next original key-node axes |
| --- | --- |
| Both negative, or both nonnegative | **Vertical or NE–SW** |
| Exactly one negative | **Horizontal or NW–SE** |

**Zero is nonnegative.** This is a test of `μ < 0`, not merely of squarefreeness or equality of the two Möbius values. For example, `μ(X)=0` and `μ(Y)=+1` belong to the same nonnegative class.

Writing

$$
\chi(n)=\mathbf1[\mu(n)<0],
$$

the predicted bit is

$$
\boxed{b_{i+1}=1\oplus\chi(X)\oplus\chi(Y).}
$$

The symbol `⊕` denotes addition modulo 2. Equivalently, `b = 1` when the two negativity indicators agree, and `b = 0` when they differ.

The inputs are only M, Z, and L from the current block. The formula uses no following plaintext, next-block length, next key values, block number, or accumulated phase S. Its Möbius arguments are positive integers in the range 2…1458.

### Direct implementation

The supplied `mu` function must evaluate the Möbius function on positive integers.

```python
def expected_next_key_axis_group(current_node, current_cipher_cells, mu):
    """0: H or NW-SE; 1: V or NE-SW. Coordinates are 1-based."""
    M = current_node[1]
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

    def n90(cell):
        r, c = cell
        return 27 * (c - 1) + 28 - r

    def n180(cell):
        r, c = cell
        return 730 - (27 * (r - 1) + c)

    X = n90(M) + n180(Z)
    Y = n90(L) + n180(Z)
    return int((mu(X) < 0) == (mu(Y) < 0))


def original_key_axis_group(node):
    """For a valid, nondegenerate three-cell node on one of the four axes."""
    dr = node[-1][0] - node[0][0]
    dc = node[-1][1] - node[0][1]
    return int(dr != 0 and dr * dc <= 0)


# Keep a proposed next source only if:
# original_key_axis_group(next_node) == expected_next_key_axis_group(
#     current_node, current_cipher_cells, mu
# )
```
