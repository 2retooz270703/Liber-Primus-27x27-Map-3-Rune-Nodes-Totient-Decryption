# The Leftmost Cell

Two checks help evaluate a continuation: whether a block’s leftmost cell fits its mode, and whether the next block’s leftmost cell is read first or last.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right. After rotation, cells are numbered row by row from 1 to 729.

| Symbol | Meaning |
| :--- | :--- |
| L | Current leftmost cell: smallest occupied column, bottommost cell in a tie |
| E | Current endpoint: last cell read |
| h | Rune index of the current original key-node center, **before the totient transformation** |
| L′ | Next block’s leftmost cell, selected by the same geometric rule |

L and E may be different cells. The functions `φ` and `μ` are Euler’s totient and Möbius functions, defined in the [decryption method](00-decryption-method.md).

## 2. Check the leftmost cell

For L = `(r,c)`, calculate its absolute index after a **90° clockwise turn**:

$$
n_1(r,c)=27(c-1)+28-r.
$$

Apply `μ` and compare the result with the current block’s mode from [Report 01](01-next-key-signature.md):

| Current mode | Allowed μ(n₁(L)) |
| :--- | :--- |
| Direct | 0 or +1 |
| Reflected | 0 or −1 |

**Zero is allowed in both modes**, so it cannot identify the mode by itself.

## 3. Predict the next reading boundary

Use the **current endpoint E** and the **original center’s rune index h**. The endpoint’s absolute index after a **270° clockwise turn** is:

$$
n_3(r,c)=27(27-c)+r.
$$

Calculate:

$$
\tau_{\mathrm{next}}=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod2.
$$

| Result | Prediction for L′ |
| :---: | :--- |
| 1 | BEGINNING — first cell read |
| 0 | END — last cell read |

This describes the reading order, whether the block is horizontal, vertical, or diagonal.

### Direct implementation

Supply ciphertext cells as nonempty lists of 1-based `(row, column)` coordinates **in reading order**. `original_center_index` is the positive original rune index h at the current center, before its totient transformation. The supplied `mu` and `phi` functions evaluate Möbius and Euler's totient on positive integers.

`reflected` describes the mode of the block being checked: **False = Direct, True = Reflected**. Its +0/+1 phase offset is not used by this check. With the accumulated-state convention of [Report 11](11-seven-thresholds-and-cyclic-phase-modes.md), select that mode from the sum **after the block being checked**. The next block is checked in its own assigned mode.

The boundary forecast returns **1 when the next leftmost cell is read first and 0 when it is read last**. Supply the proposed next ciphertext as a valid straight block of at least two cells, in reading order.

```python
def accepts_leftmost_mode(cipher_cells, reflected, mu):
    """Check a block's leftmost cell: False = Direct, True = Reflected."""
    L = min(cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    r, c = L
    n90 = 27 * (c - 1) + 28 - r
    allowed = (0, -1) if reflected else (0, 1)
    return mu(n90) in allowed


def expected_next_reading_boundary(
    current_cipher_cells, original_center_index, mu, phi
):
    """Predict tau for the next block: 1 = leftmost first, 0 = last."""
    E = current_cipher_cells[-1]
    r, c = E
    n270 = 27 * (27 - c) + r
    return int((mu(n270) + phi(original_center_index)) % 2)


def leftmost_reading_boundary(cipher_cells):
    """Return the next block's actual tau, with its leftmost cell at an end."""
    if len(cipher_cells) < 2:
        raise ValueError("The next block must contain at least two cells.")

    B = cipher_cells[0]
    E = cipher_cells[-1]
    L = min(cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    point = (L[0], L[1])

    if point == (B[0], B[1]):
        return 1
    if point == (E[0], E[1]):
        return 0
    raise ValueError("The leftmost cell must be read first or last.")


def accepts_next_reading_boundary(
    current_cipher_cells, original_center_index, next_cipher_cells, mu, phi
):
    """Check a proposed next block against the predicted reading boundary."""
    predicted = expected_next_reading_boundary(
        current_cipher_cells, original_center_index, mu, phi
    )
    return leftmost_reading_boundary(next_cipher_cells) == predicted


# Check the current block in its own mode:
# accepts_leftmost_mode(current_cipher_cells, current_reflected, mu)
#
# Keep a proposed next reading boundary only if:
# accepts_next_reading_boundary(
#     current_cipher_cells, original_center_index, next_cipher_cells, mu, phi
# )
#
# Also check the proposed next block in its own mode:
# accepts_leftmost_mode(next_cipher_cells, next_reflected, mu)
```
