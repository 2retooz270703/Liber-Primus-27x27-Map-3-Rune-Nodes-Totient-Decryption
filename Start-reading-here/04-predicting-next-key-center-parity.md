# Predicting the Next Key’s Center Parity

Two formulas use the current block’s coordinates to predict whether the next original key-node center lies in an **even or odd** row and column.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current block |
| E | Last cell read in the current block |
| M | Current original key-node center, before the totient transformation |
| (r′, c′) | Next original key-node center |

For any cell `X`, `r(X)` is its row and `c(X)` its column. All inputs are **coordinate numbers**.

Read each formula modulo 2: **0 = even, 1 = odd**.

## 2. Predict the column parity

Add the three current row numbers and 1:

$$
c'\equiv1+r(B)+r(E)+r(M)\pmod2.
$$

## 3. Predict the row parity

First calculate the beginning’s absolute index after a **180° turn**, numbering cells row by row from 1 to 729:

$$
n_2(B)=730-\bigl[27(r(B)-1)+c(B)\bigr].
$$

Then calculate:

$$
r'\equiv1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\pmod2.
$$

The Möbius value `μ(n)` is **0** if `n` has a repeated prime factor; otherwise it is **+1 or −1**. Modulo 2, zero leaves the sum’s parity unchanged, while either nonzero value toggles it.

### Direct implementation

Supply `current_cipher_cells` as a nonempty list of all current ciphertext coordinates **in reading order**. `current_key_center` is the current original center M, and `next_key_center` is a proposed next original center. Both centers are supplied as 1-based `(row, column)` coordinate pairs. The supplied `mu` function must evaluate the Möbius function on positive integers.

The prediction returns two bits labeled `row` and `column`: **0 = even, 1 = odd**. Both are calculated from the current block. The acceptance function requires the proposed next center to match both bits.

```python
def expected_next_key_center_parities(
    current_cipher_cells, current_key_center, mu
):
    """Predict the next original center's row and column parity bits."""
    B = current_cipher_cells[0]
    E = current_cipher_cells[-1]
    M = current_key_center

    n2_B = 730 - (27 * (B[0] - 1) + B[1])
    row = (1 + B[1] + E[0] + M[0] + mu(n2_B)) % 2
    column = (1 + B[0] + E[0] + M[0]) % 2

    return {"row": int(row), "column": int(column)}


def key_center_parities(key_center):
    """Return the actual row and column parity bits of a center coordinate."""
    r, c = key_center
    return {"row": int(r % 2), "column": int(c % 2)}


def accepts_next_key_center_parities(
    current_cipher_cells, current_key_center, next_key_center, mu
):
    """Check that a proposed next original center matches both predictions."""
    predicted = expected_next_key_center_parities(
        current_cipher_cells, current_key_center, mu
    )
    return key_center_parities(next_key_center) == predicted


# Keep a proposed next original center only if:
# accepts_next_key_center_parities(
#     current_cipher_cells, current_key_center, next_key_center, mu
# )
```
