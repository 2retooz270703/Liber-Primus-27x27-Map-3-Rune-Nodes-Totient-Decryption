# Filtering the Next Ciphertext’s Beginning

The next beginning is checked against eight rays from the current block’s leftmost cell. A condition at the current endpoint determines whether a **one-cell offset** is allowed.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

In the formulas, `r(X)` and `c(X)` denote a cell’s row and column.

| Symbol | Meaning |
| :--- | :--- |
| L | Current leftmost cell: smallest occupied column, bottommost cell in a tie |
| E | Current endpoint: last cell read |
| B′ | Proposed beginning of the next block: first cell read |

**Measure the displacement from L. Evaluate the Möbius condition at E.** These may be different cells.

## 2. Calculate the allowed offset

For the endpoint `E = (r,c)`, calculate its absolute indices in the original orientation and after a **270° clockwise turn**:

$$
n_0(r,c)=27(r-1)+c,\qquad n_3(r,c)=27(27-c)+r.
$$

The Möbius value `μ(n)` is **0** if `n` has a repeated prime factor; otherwise it is **+1 or −1**.

Set the allowance:

- **q = 1** if both `μ(n₀(E)) = 0` and `μ(n₃(E)) = 0`.
- **q = 0** otherwise.

## 3. Check the next beginning

The eight rays run horizontally, vertically, and diagonally at 45°, with unrestricted length. For a proposed B′, calculate:

$$
\Delta r=r(B')-r(L),\qquad\Delta c=c(B')-c(L),
$$

$$
d_8=\min\left(|\Delta r|,|\Delta c|,\bigl||\Delta r|-|\Delta c|\bigr|\right).
$$

This **grid-offset score** is zero when B′ shares a row, column, or 45° diagonal with L. The anchor L itself also qualifies.

Accept the candidate only if:

$$
d_8\le q.
$$

| Allowance | Required position |
| :--- | :--- |
| q = 0 | Exactly on a ray: d₈ = 0 |
| q = 1 | On a ray or one cell off: d₈ = 0 or 1 |

**An allowance of 1 permits an offset; it does not require one.**

### Direct implementation

Supply `current_cipher_cells` as a nonempty list of all current ciphertext coordinates **in reading order**, using 1-based `(row, column)` pairs. `next_beginning` is the coordinate pair of the first cell read in the proposed next block. The supplied `mu` function must evaluate the Möbius function on positive integers.

The allowance is calculated at the current endpoint E. The acceptance check separately locates L, measures the grid-offset score from L, and applies **`d8 <= q`**. Thus an allowance of 1 accepts both score 0 and score 1.

```python
def next_ray_offset_allowance(current_cipher_cells, mu):
    """Return q: 0 allows only score 0; 1 allows score 0 or 1."""
    E = current_cipher_cells[-1]

    def n0(cell):
        r, c = cell
        return 27 * (r - 1) + c

    def n270(cell):
        r, c = cell
        return 27 * (27 - c) + r

    return int(mu(n0(E)) == 0 and mu(n270(E)) == 0)


def ray_offset(leftmost_cell, next_beginning):
    """Return the report's d8 score relative to the current leftmost cell."""
    dr = abs(next_beginning[0] - leftmost_cell[0])
    dc = abs(next_beginning[1] - leftmost_cell[1])
    return min(dr, dc, abs(dr - dc))


def accepts_next_beginning_with_allowance(
    current_cipher_cells, next_beginning, mu
):
    """Check the next beginning against the endpoint-derived allowance."""
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    q = next_ray_offset_allowance(current_cipher_cells, mu)
    return ray_offset(L, next_beginning) <= q


# Keep a proposed next beginning B_next only if:
# accepts_next_beginning_with_allowance(
#     current_cipher_cells, B_next, mu
# )
```

