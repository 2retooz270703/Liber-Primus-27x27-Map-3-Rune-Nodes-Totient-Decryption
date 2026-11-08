# Predicting the Next Ciphertext’s Row Parity

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current block |
| E | Last cell read in the current block |
| M | Current original key-node center, before the totient transformation |
| p | Current derived key’s phase: 0, 1, or 2 |
| E′ | Next block’s endpoint: last cell read |
| L′ | Next block’s leftmost cell |

For any cell `X`, `r(X)` is its row and `c(X)` its column. The leftmost cell is in the **smallest column**, with the **bottommost cell** chosen in a tie.

Calculate the current phase `p` modulo 3, as defined in the [decryption method](00-decryption-method.md), before applying these rules.

## 2. Predict the two row parities

All results are reduced modulo 2: **0 = even, 1 = odd**.

For a cell `(r,c)`, its absolute index after a **180° turn** is:

$$
n_2(r,c)=730-\bigl[27(r-1)+c\bigr].
$$

The Möbius value `μ(n)` is **0** if `n` has a repeated prime factor; otherwise it is **+1 or −1**. Either nonzero value toggles parity.

### Endpoint

$$
r(E')\equiv1+p+\mu\bigl(n_2(M)\bigr)\pmod2.
$$

This uses the current phase and the center’s reflected **absolute index**.

### Leftmost cell

First calculate the predicted next-center row bit `b`, using [Report 04](04-predicting-next-key-center-parity.md):

$$
b=\bigl[1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\bigr]\bmod2.
$$

Calculate `b` from the current block before selecting the next node. Then:

$$
r(L')\equiv b+1+p+\mu\bigl(r(M)\bigr)\pmod2.
$$

Here, the Möbius input is the center’s **row number** `r(M)`.

### Direct implementation

Supply the current and proposed next ciphertext cells as nonempty lists of 1-based `(row, column)` coordinates **in reading order**. `current_key_center` is the current original center M. `current_phase` is the current derived key's phase, reduced modulo 3 before use. The supplied `mu` function must evaluate the Möbius function on positive integers.

The prediction returns two bits, labeled `endpoint` and `leftmost`: **0 = even row, 1 = odd row**. The next-center row bit b is calculated internally from the current block. The acceptance function requires both predicted row parities to match the proposed next ciphertext.

```python
def expected_next_row_parities(
    current_cipher_cells, current_key_center, current_phase, mu
):
    """Predict the next endpoint and leftmost row bits: 0 = even, 1 = odd."""
    B = current_cipher_cells[0]
    E = current_cipher_cells[-1]
    M = current_key_center
    p = current_phase % 3

    def n180(cell):
        r, c = cell
        return 730 - (27 * (r - 1) + c)

    b = (1 + B[1] + E[0] + M[0] + mu(n180(B))) % 2
    endpoint = (1 + p + mu(n180(M))) % 2
    leftmost = (b + 1 + p + mu(M[0])) % 2

    return {"endpoint": int(endpoint), "leftmost": int(leftmost)}


def ciphertext_row_parities(cipher_cells):
    """Return the actual endpoint and leftmost row parity bits."""
    E = cipher_cells[-1]
    L = min(cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    return {"endpoint": int(E[0] % 2), "leftmost": int(L[0] % 2)}


def accepts_next_row_parities(
    current_cipher_cells, current_key_center, current_phase,
    next_cipher_cells, mu
):
    """Apply both predicted row parities to a proposed next ciphertext."""
    predicted = expected_next_row_parities(
        current_cipher_cells, current_key_center, current_phase, mu
    )
    return ciphertext_row_parities(next_cipher_cells) == predicted


# Keep a proposed next ciphertext only if:
# accepts_next_row_parities(
#     current_cipher_cells, current_key_center, current_phase,
#     next_cipher_cells, mu
# )
```
