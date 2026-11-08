# Predicting the Reading Axis

Use the current block’s first cell, last cell, and original key node to predict the next block’s axis and reading order.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Input from the current block |
| :--- | :--- |
| B | First cell read |
| E | Last cell read |
| M | Coordinate of the original key-node center |
| h | Original rune index at that center, before the totient transformation |

**M is a coordinate; h is a rune index.** Fix the original node before calculating: nodes that produce the same derived key can give different predictions.

Use Euler’s totient `φ` and the Möbius function `μ`, defined in the [decryption method](00-decryption-method.md).

After each rotation, number cells row by row from 1 to 729:

| Clockwise turn | Absolute index of cell (r, c) |
| :--- | :--- |
| 0° | n₀ = 27(r−1) + c |
| 90° | n₁ = 27(c−1) + 28−r |
| 180° | n₂ = 730−n₀ |
| 270° | n₃ = 27(27−c) + r |

## 2. Predict the axis

Calculate:

$$
A=n_2(B)+n_0(M),\qquad G=\gcd\bigl(n_1(E),n_2(E)\bigr).
$$

Here, `gcd` means greatest common divisor. Keep `A` as an ordinary integer, even when it exceeds 729.

Then calculate the score:

$$
q=\mu(A)+\mu(G).
$$

| Score | Next axis |
| :--- | :--- |
| q = 0 | Horizontal |
| q > 0 | Vertical |
| q < 0 | Diagonal |

## 3. Determine the reading direction

Apply the [boundary rule](02-leftmost-cell-and-rotations.md):

$$
\tau=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod2.
$$

The next block’s **leftmost cell** is the one in the smallest column; choose the bottommost cell in a tie.

| Axis | τ = 1: leftmost read first | τ = 0: leftmost read last |
| :--- | :--- | :--- |
| Horizontal | Right → | Left ← |
| Vertical | Up ↑ | Down ↓ |
| Diagonal | Up-right ↗ or down-right ↘ | Up-left ↖ or down-left ↙ |

For diagonals, the selected coordinates determine the remaining up/down slope.

### Direct implementation

Supply `current_cipher_cells` as a nonempty list of all current ciphertext coordinates **in reading order**. `current_key_center` is the original center coordinate M. `original_center_index` is the positive original rune index h at that center, before its totient transformation. Coordinates are 1-based `(row, column)` pairs.

The supplied `mu` and `phi` functions evaluate Möbius and Euler's totient on positive integers. In particular, `mu` must accept the unreduced sum A, which can exceed 729.

The prediction returns `axis` and `leftmost_first` (the bit τ): **1 = leftmost read first, 0 = leftmost read last**. Supply the proposed next ciphertext as a valid straight horizontal, vertical, or 45° diagonal block of at least two cells, in reading order. The acceptance function checks both properties; either diagonal slope is allowed when it matches the predicted boundary.

```python
from math import gcd


def expected_next_axis_and_boundary(
    current_cipher_cells, current_key_center, original_center_index, mu, phi
):
    """Predict the next ciphertext's axis and leftmost-first bit tau."""
    B = current_cipher_cells[0]
    E = current_cipher_cells[-1]
    M = current_key_center
    h = original_center_index

    def n0(cell):
        r, c = cell
        return 27 * (r - 1) + c

    def n90(cell):
        r, c = cell
        return 27 * (c - 1) + 28 - r

    def n180(cell):
        return 730 - n0(cell)

    def n270(cell):
        return 730 - n90(cell)

    A = n180(B) + n0(M)
    G = gcd(n90(E), n180(E))
    score = mu(A) + mu(G)

    if score == 0:
        axis = "horizontal"
    elif score > 0:
        axis = "vertical"
    else:
        axis = "diagonal"

    tau = int((mu(n270(E)) + phi(h)) % 2)
    return {"axis": axis, "leftmost_first": tau}


def ciphertext_axis_and_boundary(cipher_cells):
    """Describe a valid straight next block of at least two distinct cells."""
    if len(cipher_cells) < 2:
        raise ValueError("The next block must contain at least two cells.")

    B = cipher_cells[0]
    E = cipher_cells[-1]
    dr, dc = E[0] - B[0], E[1] - B[1]

    if dr == 0 and dc != 0:
        axis = "horizontal"
    elif dc == 0 and dr != 0:
        axis = "vertical"
    elif dr != 0 and abs(dr) == abs(dc):
        axis = "diagonal"
    else:
        raise ValueError("The endpoints must define one of the four axes.")

    L = min(cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    tau = int((B[0], B[1]) == (L[0], L[1]))
    return {"axis": axis, "leftmost_first": tau}


def accepts_next_axis_and_boundary(
    current_cipher_cells, current_key_center, original_center_index,
    next_cipher_cells, mu, phi
):
    """Check both the predicted axis and boundary for a valid next block."""
    predicted = expected_next_axis_and_boundary(
        current_cipher_cells, current_key_center, original_center_index, mu, phi
    )
    return ciphertext_axis_and_boundary(next_cipher_cells) == predicted


# Keep a proposed next ciphertext only if:
# accepts_next_axis_and_boundary(
#     current_cipher_cells, current_key_center, original_center_index,
#     next_cipher_cells, mu, phi
# )
```
