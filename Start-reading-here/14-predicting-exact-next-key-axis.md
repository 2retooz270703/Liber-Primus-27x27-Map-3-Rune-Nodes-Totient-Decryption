# Predicting the Exact Next Key-Node Axis

## 1. What is new?

Report 13 predicts a group containing two possible axes of the next **original three-rune key node**. The present candidate adds a bit that distinguishes a diagonal from a horizontal or vertical source. Together, the two bits select one exact undirected axis:

| Report 13 group bit b | New diagonal bit d | Axis number 2b+d | Next original key-node axis |
| :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | Horizontal, W–E |
| 0 | 1 | 1 | Diagonal, NW–SE |
| 1 | 0 | 2 | Vertical, N–S |
| 1 | 1 | 3 | Diagonal, NE–SW |

This predicts the source node's axis **before any center transformation or cyclic key alignment**. It leaves the source's radius, center position and reading order unresolved. The next ciphertext's axis is a separate property, addressed by [Report 03](03-predicting-axis-and-reading-direction.md).

## 2. Coordinates and inputs

Use the project's **27 × 27** matrix with 1-based `(row, column)` coordinates. Rows increase downward; columns increase to the right. All inputs belong to the **current** block.

| Symbol | Meaning |
| :--- | :--- |
| M | Center of the current original key node |
| Z | Its lower outer cell; for a horizontal node, its right outer cell |
| L | Current ciphertext's leftmost cell: smallest column, bottommost on ties |
| u, h, z | The three original source-rune indices, before applying φ or rotating the key |
| GP(k) | The prime weight of rune index k |

The source is a valid, equally spaced three-cell node on one of the four axes. Keep its center in the middle of the supplied coordinate triple. Reversing the whole triple preserves M, Z and the GP sum. L is selected geometrically and need not be the first ciphertext cell read.

GP assigns the first 29 primes in rune-index order: **F=2, U=3, TH=5, O=7, R=11, …, EA=109**. Use the original source values, including the **original center h**. The GP sum of a transformed key is a different quantity.

The rotated absolute cell indices are:

$$
n_0(r,c)=27(r-1)+c,\qquad n_1(r,c)=27(c-1)+28-r,
$$

$$
n_2(r,c)=730-n_0(r,c),\qquad n_3(r,c)=730-n_1(r,c).
$$

These number the same original cell after 0°, 90°, 180° and 270° clockwise rotations. They do not select additional cells from which runes are read. Keep sums of indices as ordinary integers, including values greater than 729.

## 3. Proposed exact-axis rule

### A. Retain the group bit from Report 13

Calculate:

$$
X=n_1(M)+n_2(Z),\qquad Y=n_1(L)+n_2(Z).
$$

Then:

$$
b=1\oplus\mathbf1[\mu(X)<0]\oplus\mathbf1[\mu(Y)<0].
$$

Thus **b=1** when the two Möbius values are both negative or both nonnegative. Zero belongs to the nonnegative class.

### B. Calculate the additional diagonal bit

Use two coordinate-based arguments and the GP sum of the original source:

$$
G=\gcd\bigl(n_1(M),n_3(Z)\bigr),
$$

$$
T=GP(u)+GP(h)+GP(z),\qquad A=n_0(M)+n_3(Z).
$$

The proposed bit is:

$$
\boxed{d=\mathbf1[\mu(G)<0]\oplus\mathbf1[\mu(T)>0]\oplus\mathbf1[\mu(A)\ne0].}
$$

Each indicator is **1 when its condition is true and 0 otherwise**. The symbol ⊕ means XOR, or addition modulo 2.

| Term | Contributes 1 when |
| :--- | :--- |
| First | μ(G) is negative |
| GP term | μ(T) is positive |
| Third | A is squarefree: μ(A) is either +1 or −1 |

These are three different tests. A zero Möbius value contributes 0 in each term. The result **d=1 predicts a diagonal**; **d=0 predicts a horizontal or vertical source**.

### C. Select the exact axis

$$
\boxed{\mathrm{axis}_{i+1}=2b+d}
$$

Use the numbering in Section 1. The calculation needs no following plaintext, next-source coordinates or rune values, chosen next length, block number, or accumulated phase S.

### Direct implementation

Supply the current original source coordinates in **outer–center–outer** order. `current_cipher_cells` is a nonempty list of all current ciphertext coordinates, in reading order. Coordinates are integer pairs in 1…27. `original_node_runes` contains the three corresponding **original rune indices**, 0…28, before any center transformation or cyclic alignment.

The supplied `mu` function evaluates Möbius on positive integers through at least **1458**; the function from [Report 00](00-decryption-method.md) is suitable. The GP prime table is included. `expected_next_key_axis` returns **0=horizontal, 1=NW–SE, 2=vertical, 3=NE–SW**. The acceptance helper compares this forecast with a proposed next source's physical axis.

The code includes Report 13's group calculation, so no function from that report needs to be imported. The caller must supply rune indices from the same source cells as `current_node`.

```python
from math import gcd


GP_PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109,
)


def original_key_axis(node):
    """Return 0=H, 1=NW-SE, 2=V, 3=NE-SW for an equally spaced node."""
    if len(node) != 3:
        raise ValueError("The source must contain three coordinates.")
    first, center, last = node
    if (2 * center[0], 2 * center[1]) != (
        first[0] + last[0], first[1] + last[1]
    ):
        raise ValueError("The center must bisect the two outer cells.")

    dr, dc = last[0] - first[0], last[1] - first[1]
    if dr == 0 and dc != 0:
        return 0
    if dc == 0 and dr != 0:
        return 2
    if dr != 0 and abs(dr) == abs(dc):
        return 1 if dr * dc > 0 else 3
    raise ValueError("The source must have a nondegenerate four-axis geometry.")


def expected_next_key_axis(
    current_node, current_cipher_cells, original_node_runes, mu
):
    """Predict one exact next-source axis using current-block inputs only."""
    original_key_axis(current_node)  # Check source spacing and axis.
    if not current_cipher_cells:
        raise ValueError("The current ciphertext must be nonempty.")
    if len(original_node_runes) != 3 or any(
        not 0 <= k <= 28 for k in original_node_runes
    ):
        raise ValueError("Supply three original rune indices in 0..28.")

    M = current_node[1]
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

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

    X = n90(M) + n180(Z)
    Y = n90(L) + n180(Z)
    group = int((mu(X) < 0) == (mu(Y) < 0))

    G = gcd(n90(M), n270(Z))
    T = sum(GP_PRIMES[k] for k in original_node_runes)
    A = n0(M) + n270(Z)
    diagonal = int(mu(G) < 0) ^ int(mu(T) > 0) ^ int(mu(A) != 0)
    return 2 * group + diagonal


def accepts_next_key_axis(
    current_node, current_cipher_cells, original_node_runes, next_node, mu
):
    """Check a proposed next original source against the exact-axis forecast."""
    predicted = expected_next_key_axis(
        current_node, current_cipher_cells, original_node_runes, mu
    )
    return original_key_axis(next_node) == predicted


# Keep a proposed next source only if:
# accepts_next_key_axis(
#     current_node, current_cipher_cells, original_node_runes, next_node, mu
# )
```
