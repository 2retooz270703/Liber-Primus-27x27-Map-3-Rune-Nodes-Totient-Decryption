# Predicting the Parity of the Next Key-Node Radius

It removes **48.70%** of the physical source-node candidates.

## 1. What the rule predicts

[Report 14](14-predicting-exact-next-key-axis.md) selects the next original key node's undirected axis. This report proposes one more bit: whether that node's **physical radius is even or odd**.

The radius is the number of grid steps from the original source's center to either outer cell:

$$
R=\max\bigl(|r_U-r_M|,\;|c_U-c_M|\bigr),
$$

where `U` is either outer cell. A diagonal source with displacement `(3,3)` has radius **3**, not its Euclidean length. Valid equally spaced three-cell nodes in the 27 × 27 grid have `1≤R≤13`.

The proposed rule predicts **only parity**. It does not determine the exact radius, center, source runes, next ciphertext, block length, or plaintext.

## 2. Coordinates and current-block inputs

Use **1-based** coordinates `(row, column)`, with rows increasing downward and columns to the right.

| Symbol | Current-block input |
| :--- | :--- |
| M | Center of the original three-rune source, before any center transformation |
| Z | Lower original outer cell; for a horizontal source, the right outer cell |
| B | First ciphertext cell in the established reading order |
| E | Last ciphertext cell in that order |
| L | Ciphertext's leftmost cell: smallest column, bottommost on a tie |
| R′ | Radius of the proposed next original source; the comparison target |

**L need not equal B.** The selected source coordinates matter even when different physical sources produce the same transformed numerical key. Reversing a source triple preserves M and the geometrically defined Z.

For any original cell `X=(r,c)`, define:

$$
n_0(X)=27(r-1)+c,\qquad
n_1(X)=27(c-1)+28-r,
$$

$$
n_2(X)=730-n_0(X),\qquad
n_3(X)=730-n_1(X).
$$

These are the absolute indices of the same cell after clockwise rotations by 0°, 90°, 180° and 270°. They do not instruct the reader to select different rune cells. Keep index sums as **ordinary integers**; do not reduce them modulo 729 or 29.

The Möbius function has values −1, 0 and +1. It vanishes when an integer has a squared prime factor; otherwise its sign records the parity of the number of distinct prime factors, with μ(1)=+1.

## 3. Proposed parity rule

Calculate:

$$
a=\bigl(|r_M-r_B|+|c_M-c_B|\bigr)\bmod2,
$$

$$
g=\gcd\bigl(n_2(Z),n_2(L)\bigr),\qquad
b=\mathbf1[\mu(g)<0],
$$

$$
s=n_1(B)+n_1(E),\qquad
c=\mathbf1[\mu(s)>0].
$$

Then:

$$
\boxed{R'\bmod2=a\oplus b\oplus c.}
$$

Here **⊕ is XOR**, or addition modulo 2. Each indicator is 1 when its condition is true and 0 otherwise.

| Output | Interpretation |
| :---: | :--- |
| 0 | Keep next original sources with even radius |
| 1 | Keep next original sources with odd radius |

The two Möbius sign tests are different: **b tests negativity; c tests positivity.** A zero Möbius value contributes 0 in both tests. Replacing these indicators with μ itself modulo 2 would change the rule.

Every input is available from the current selected block. The calculation uses no next plaintext, next-source coordinates, next radius, accumulated phase, block number, Gematria Primus weights, or rune identities.

### A simpler interpretation of the first term

For integers, `|x−y|≡x+y (mod 2)`. Therefore:

$$
a=(r_M+c_M+r_B+c_B)\bmod2.
$$

Thus **a simply compares the checkerboard colors of M and B**: it is 1 when they differ. The Manhattan-distance notation adds no extra metric information at parity level.

Also:

$$
s=27(c_B+c_E)+2-r_B-r_E.
$$

These identities simplify implementation. They do not explain why the two Möbius corrections should predict a future radius. That cross-block relationship remains the empirical claim.

## 4. Direct implementation

Supply each source in **outer–center–outer** order, including when the order is reversed. Supply all current ciphertext coordinates in their established reading order. The `mu` argument is a Möbius implementation on positive integers; support through 1458 is sufficient for these formulas.

```python
from math import gcd


def original_key_radius(node):
    """Radius in grid steps for a nondegenerate four-axis source."""
    if len(node) != 3:
        raise ValueError("Supply three source coordinates.")
    first, center, last = node
    if any(
        len(cell) != 2 or any(not 1 <= v <= 27 for v in cell)
        for cell in node
    ):
        raise ValueError("Source coordinates must lie in 1..27.")
    if (first[0] + last[0], first[1] + last[1]) != (
        2 * center[0], 2 * center[1]
    ):
        raise ValueError("The center must bisect the source.")
    dr = first[0] - center[0]
    dc = first[1] - center[1]
    if (dr, dc) == (0, 0) or not (
        dr == 0 or dc == 0 or abs(dr) == abs(dc)
    ):
        raise ValueError("Use a nondegenerate four-axis source.")
    return max(abs(dr), abs(dc))


def expected_next_key_radius_parity(
    current_node, current_cipher_cells, mu
):
    """Return 0=even or 1=odd, using current-block inputs only."""
    original_key_radius(current_node)
    if not current_cipher_cells:
        raise ValueError("The current ciphertext must be nonempty.")
    if any(
        len(cell) != 2 or any(not 1 <= v <= 27 for v in cell)
        for cell in current_cipher_cells
    ):
        raise ValueError("Ciphertext coordinates must lie in 1..27.")

    M = current_node[1]
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    B = current_cipher_cells[0]
    E = current_cipher_cells[-1]
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

    def n90(cell):
        r, col = cell
        return 27 * (col - 1) + 28 - r

    def n180(cell):
        r, col = cell
        return 730 - (27 * (r - 1) + col)

    a = (M[0] + M[1] + B[0] + B[1]) % 2
    b = int(mu(gcd(n180(Z), n180(L))) < 0)
    c = int(mu(n90(B) + n90(E)) > 0)
    return a ^ b ^ c


def accepts_next_key_radius_parity(
    current_node, current_cipher_cells, next_node, mu
):
    predicted = expected_next_key_radius_parity(
        current_node, current_cipher_cells, mu
    )
    return original_key_radius(next_node) % 2 == predicted
```

The acceptance helper compares a candidate with the forecast. It does not select a source or establish a new plaintext.

## 5. Worked examples

### WEATHER (02) → TURNS (03): even

The current inputs are:

$$
M=(14,5),\quad Z=(14,6),\quad
B=L=(14,14),\quad E=(14,18).
$$

The center-to-beginning checkerboard difference is:

$$
a=(0+9)\bmod2=1.
$$

The arithmetic arguments are:

$$
g=\gcd(373,365)=1,\qquad \mu(g)=+1,
$$

$$
s=365+473=838=2\cdot419,\qquad \mu(s)=+1.
$$

Thus `b=0`, `c=1` and:

$$
R'\bmod2=1\oplus0\oplus1=0.
$$

The recorded TURNS source has radius **10**, agreeing with the even forecast.

### SOON (16) → THEN (17): odd

For the selected SOON source `(25,4)–(25,7)–(25,10)`:

$$
M=(25,7),\quad Z=(25,10),\quad
B=L=(25,16),\quad E=(25,19).
$$

Then:

$$
a=9\bmod2=1,
$$

$$
g=\gcd(72,66)=6,\qquad \mu(6)=+1,
$$

$$
s=408+489=897=3\cdot13\cdot23,\qquad \mu(897)=-1.
$$

Therefore `b=c=0` and the predicted parity is **odd**. The recorded THEN source has radius **1**.

### All 33 transitions

The values g and s are the integer arguments defined in Section 3. “Prediction” is the forecast for the **next** original source.

| No. | Current → next reading | a | g | μ(g) | s | μ(s) | Prediction | Recorded R′ |
| :--- | :--- | :---: | ---: | :---: | ---: | :---: | :---: | ---: |
| 01→02 | AS I GO, THE → WEATHER | 1 | 3 | -1 | 758 | +1 | Odd | 1 |
| 02→03 | WEATHER → TURNS | 1 | 1 | +1 | 838 | +1 | Even | 10 |
| 03→04 | TURNS → COLD | 0 | 2 | -1 | 1004 | 0 | Odd | 1 |
| 04→05 | COLD → I MAY | 0 | 3 | -1 | 355 | +1 | Even | 2 |
| 05→06 | I MAY → CRY | 0 | 1 | +1 | 895 | +1 | Odd | 1 |
| 06→07 | CRY → NOW THE | 0 | 3 | -1 | 830 | -1 | Odd | 1 |
| 07→08 | NOW THE → IDEA | 0 | 3 | -1 | 948 | 0 | Odd | 3 |
| 08→09 | IDEA → OF | 0 | 40 | 0 | 996 | 0 | Even | 2 |
| 09→10 | OF → THE | 0 | 4 | 0 | 803 | +1 | Odd | 1 |
| 10→11 | THE → END | 1 | 3 | -1 | 855 | 0 | Even | 4 |
| 11→12 | END → IS | 1 | 1 | +1 | 1204 | 0 | Odd | 5 |
| 12→13 | IS → DEATH | 1 | 1 | +1 | 473 | +1 | Even | 4 |
| 13→14 | DEATH → SEE | 0 | 2 | -1 | 58 | +1 | Even | 4 |
| 14→15 | SEE → YOU | 0 | 2 | -1 | 760 | 0 | Odd | 11 |
| 15→16 | YOU → SOON | 1 | 6 | +1 | 868 | 0 | Odd | 3 |
| 16→17 | SOON → THEN | 1 | 6 | +1 | 897 | -1 | Odd | 1 |
| 17→18 | THEN → THE | 0 | 3 | -1 | 1356 | 0 | Odd | 3 |
| 18→19 | THE → KEY | 0 | 17 | -1 | 1066 | -1 | Odd | 1 |
| 19→20 | KEY → IS | 1 | 6 | +1 | 178 | +1 | Even | 6 |
| 20→21 | IS → TO | 1 | 1 | +1 | 316 | 0 | Odd | 3 |
| 21→22 | TO → GO | 0 | 3 | -1 | 876 | 0 | Odd | 7 |
| 22→23 | GO → TO | 1 | 2 | -1 | 1091 | -1 | Even | 6 |
| 23→24 | TO → THE | 1 | 1 | +1 | 1193 | -1 | Odd | 3 |
| 24→25 | THE → EAST | 0 | 2 | -1 | 983 | -1 | Odd | 7 |
| 25→26 | EAST → OF | 0 | 1 | +1 | 1214 | +1 | Odd | 1 |
| 26→27 | OF → THE | 1 | 1 | +1 | 664 | 0 | Odd | 1 |
| 27→28 | THE → MAPLIFE | 1 | 1 | +1 | 637 | 0 | Odd | 1 |
| 28→29 | MAPLIFE → MAY | 1 | 1 | +1 | 726 | 0 | Odd | 3 |
| 29→30 | MAY → BE | 0 | 5 | -1 | 614 | +1 | Even | 6 |
| 30→31 | BE → THE | 0 | 4 | 0 | 572 | 0 | Even | 4 |
| 31→32 | THE → DEATH | 0 | 1 | +1 | 601 | -1 | Even | 6 |
| 32→33 | DEATH → OF | 1 | 1 | +1 | 466 | +1 | Even | 4 |
| 33→34 | OF → YOU | 0 | 1 | +1 | 923 | +1 | Odd | 5 |

## 6. A fixed forecast after YOU (34)

The last documented block has:

$$
M=(21,22),\quad Z=(21,27),\quad
B=L=(6,11),\quad E=(6,13).
$$

Its arguments are:

$$
a=(15+11)\bmod2=0,
$$

$$
g=\gcd(163,584)=1,\qquad \mu(g)=+1,
$$

$$
s=292+346=638=2\cdot11\cdot29,\qquad \mu(s)=-1.
$$

Thus:

$$
\boxed{\text{If a next original source follows, its radius is predicted EVEN.}}
$$
