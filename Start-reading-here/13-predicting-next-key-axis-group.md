# Predicting the Next Key-Node Axis Group

The proposed formula predicts one bit of the next **original key node's** undirected axis.

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

## 4. Worked example: THEN (17) → THE (18)

For the recorded THEN block:

$$
M=(26,22),\qquad Z=(27,22),\qquad L=(25,25).
$$

The rotated indices are

$$
n_1(M)=569,\qquad n_2(Z)=6,\qquad n_1(L)=651.
$$

Consequently,

$$
X=575=5^2\cdot23,\qquad Y=657=3^2\cdot73.
$$

Both Möbius values are zero, so both are **nonnegative**. The rule predicts a **vertical or NE–SW** source for the next key.

The recorded source for THE (18), `(17,17)–(20,17)–(23,17)`, is vertical and satisfies that prediction. The zero–zero case therefore belongs to the V / NE–SW group.

## 5. Agreement across the recorded route

The selected route has **34 blocks, 105 plaintext runes, and 33 transitions**. The formula agrees with the next recorded source's axis group in every transition. The complete numerical trace is included in the appendix.

All nine possible pairs of Möbius values occur:

| μ(X) | μ(Y) | Predicted group | Transitions |
| ---: | ---: | --- | ---: |
| −1 | −1 | V / NE–SW | 3 |
| −1 | 0 | H / NW–SE | 4 |
| −1 | +1 | H / NW–SE | 4 |
| 0 | −1 | H / NW–SE | 1 |
| 0 | 0 | V / NE–SW | 5 |
| 0 | +1 | V / NE–SW | 2 |
| +1 | −1 | H / NW–SE | 2 |
| +1 | 0 | V / NE–SW | 5 |
| +1 | +1 | V / NE–SW | 7 |

Independent integer factorization reproduced the Möbius values for every integer from 1 through 1458. All **132 combinations of reversing the current and next source orders** across the 33 transitions gave the same result.

In every one of the 33 local searches, **both axis groups remain possible after the earlier filters and their continuation check**. The new rule therefore removes alternatives at every position; it does not simply restate a bit already forced there.

## 6. A fixed prediction after YOU (34)

The last recorded YOU has

$$
M=(21,22),\qquad Z=(21,27),\qquad L=(6,11).
$$

It gives

$$
X=737=11\cdot67,\quad\mu(X)=+1,
$$

$$
Y=455=5\cdot7\cdot13,\quad\mu(Y)=-1.
$$

Exactly one value is negative. Therefore, **if the route continues**, the next original key node is predicted to be

$$
\boxed{\text{horizontal or NW–SE}.}
$$

Report 12 separately predicts

$$
\boxed{d_8((6,11),B_{35})=1.}
$$

## Appendix: all 33 recorded transitions

Every recorded next source lies in the predicted group. Block numbers distinguish repeated readings such as THE, OF, and YOU.

| Transition | Current → next reading | X | Y | μ(X) | μ(Y) | Predicted next key group |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 01→02 | AS I GO THE → WEATHER | 705 | 407 | −1 | +1 | H / NW–SE |
| 02→03 | WEATHER → TURNS | 495 | 738 | 0 | 0 | V / NE–SW |
| 03→04 | TURNS → COLD | 694 | 586 | +1 | +1 | V / NE–SW |
| 04→05 | COLD → I MAY | 497 | 185 | +1 | +1 | V / NE–SW |
| 05→06 | I MAY → CRY | 492 | 697 | 0 | +1 | V / NE–SW |
| 06→07 | CRY → NOW THE | 447 | 453 | +1 | +1 | V / NE–SW |
| 07→08 | NOW THE → IDEA | 615 | 623 | −1 | +1 | H / NW–SE |
| 08→09 | IDEA → OF | 782 | 830 | −1 | −1 | V / NE–SW |
| 09→10 | OF → THE | 698 | 616 | +1 | 0 | V / NE–SW |
| 10→11 | THE → END | 615 | 615 | −1 | −1 | V / NE–SW |
| 11→12 | END → IS | 322 | 621 | −1 | 0 | H / NW–SE |
| 12→13 | IS → DEATH | 737 | 386 | +1 | +1 | V / NE–SW |
| 13→14 | DEATH → SEE | 322 | 22 | −1 | +1 | H / NW–SE |
| 14→15 | SEE → YOU | 210 | 424 | +1 | 0 | V / NE–SW |
| 15→16 | YOU → SOON | 429 | 420 | −1 | 0 | H / NW–SE |
| 16→17 | SOON → THEN | 237 | 480 | +1 | 0 | V / NE–SW |
| 17→18 | THEN → THE | 575 | 657 | 0 | 0 | V / NE–SW |
| 18→19 | THE → KEY | 559 | 639 | +1 | 0 | V / NE–SW |
| 19→20 | KEY → IS | 811 | 478 | −1 | +1 | H / NW–SE |
| 20→21 | IS → TO | 510 | 427 | +1 | +1 | V / NE–SW |
| 21→22 | TO → GO | 1103 | 859 | −1 | −1 | V / NE–SW |
| 22→23 | GO → TO | 597 | 762 | +1 | −1 | H / NW–SE |
| 23→24 | TO → THE | 556 | 696 | 0 | 0 | V / NE–SW |
| 24→25 | THE → EAST | 389 | 772 | −1 | 0 | H / NW–SE |
| 25→26 | EAST → OF | 640 | 772 | 0 | 0 | V / NE–SW |
| 26→27 | OF → THE | 876 | 511 | 0 | +1 | V / NE–SW |
| 27→28 | THE → MAP LIFE | 85 | 386 | +1 | +1 | V / NE–SW |
| 28→29 | MAP LIFE → MAY | 517 | 568 | +1 | 0 | V / NE–SW |
| 29→30 | MAY → BE | 623 | 565 | +1 | +1 | V / NE–SW |
| 30→31 | BE → THE | 276 | 324 | 0 | 0 | V / NE–SW |
| 31→32 | THE → DEATH | 894 | 650 | −1 | 0 | H / NW–SE |
| 32→33 | DEATH → OF | 542 | 571 | +1 | −1 | H / NW–SE |
| 33→34 | OF → YOU | 944 | 941 | 0 | −1 | H / NW–SE |
