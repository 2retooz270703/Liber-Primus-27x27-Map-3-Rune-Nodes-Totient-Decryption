# Report 19 — Predicting the Next Ciphertext Start with Two Distances

## 1. What the rule predicts

A single bit predicts whether the next ciphertext begins within seven grid steps of **both** the current beginning and the current leftmost cell, or farther than seven steps from **both**. A proposed start that falls within the limit for exactly one reference cell fails the test.

The forecast uses the current block and the beginning of the preceding ciphertext block. It checks the start of a proposed next segment after the applicable filters in [Report 18](18-predicting-next-ciphertext-start-and-end.md).

## 2. Coordinates and formula

Use 1-based `(row, column)` coordinates on the 27 × 27 matrix. Rows increase downward and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| $U$ | First cell of the current original key node in lexicographic `(row, column)` order. It is the upper extreme, or the left extreme for a horizontal node. |
| $B,E$ | First and last current ciphertext cells in reading order |
| $L$ | Current ciphertext cell in the smallest occupied column. At equal columns, choose the larger row. |
| $B_{\mathrm{prev}}$ | Beginning of the preceding ciphertext block. Initialize it to $B$ on the first transition. |
| $B'$ | First cell in reading order of a proposed next ciphertext segment |
| $[P]$ | 1 when $P$ is true, otherwise 0 |
| $\oplus$ | Bitwise XOR of nonnegative integers, written `^` in Python |

For a cell $X=(r,c)$, the ordinary and 180° rotated row-major indices from [Report 02](02-leftmost-cell-and-rotations.md) are

$$
\begin{aligned}
n_0(X) &= 27(r-1)+c \\
n_2(X) &= 730-n_0(X)
\end{aligned}
$$

Use the Möbius function $\mu$ from [Report 00](00-decryption-method.md). Evaluate

$$
\begin{aligned}
a &= [(n_2(B)\oplus n_2(B_{\mathrm{prev}}))\bmod 7=0] \\
b &= [\mu(n_0(U)+n_0(E))<0]
\end{aligned}
$$

The XOR is evaluated before the remainder. The predicted bit is $\widehat{h}=[a=b]$. For two cells $X,Y$, let

$$
d_\infty(X,Y)=\max\{|r(X)-r(Y)|,\ |c(X)-c(Y)|\}
$$

Accept $B'$ when

$$
[d_\infty(B',B)\le 7]
=[d_\infty(B',L)\le 7]
=\widehat{h}
$$

A start at distance exactly seven is classed as near. Select $L$ from all current ciphertext cells, including both rows when the recorded block wraps. After accepting the next block, carry the old $B$ forward as its $B_{\mathrm{prev}}$.

## 3. Results on the recorded route

The test passes **37 of 37 transitions** among the 38 recorded blocks from **AS I GO THE (01)** through **I ASK (38)**. It predicts the near class 21 times and the far class 16 times. Each transition was tested against the candidate pool obtained under Reports 00–15, 17 and 18, with the current block and its prefix fixed. Candidate counts were calculated without a word dictionary.

A geometry consists of three physical key cells and an ordered ciphertext segment. Alternate orders or transformations of the same physical key count once. A segment is counted once per pool regardless of how many keys support it.

| Candidate pool | After Report 18 | With Report 19 | Removed |
| :--- | ---: | ---: | ---: |
| Geometries summed over 37 transitions | 41,791 | **24,547** | 41.3% |
| Ordered ciphertext segments summed over 37 transitions | 2,844 | **1,413** | 50.3% |
| Geometries beyond I ASK | 1,080 | **966** | 10.6% |
| Ordered ciphertext segments beyond I ASK | 21 | **19** | 9.5% |
| Distinct starts beyond I ASK | 6 | **5** | 16.7% |

With equal weight per transition, the filter removes an average of **42.7%** of ordered segments. Restricting each pool to the recorded successor length gives a mean removal of **36.0%**. These averages give small and large pools equal weight.

### Chronological check and random controls

For the specified target $[d_\infty(B',L)\le 7]$, the formula was the only match in the tested family using the first 24 transitions. With the formula fixed, it matched **13 of 13** remaining transitions. The distance targets and the threshold of seven were identified using the full route, so this split measures recovery of the formula for a specified target.

Each random trial drew one successor independently from each of the 37 candidate pools and repeated the search over the tested single targets and pairs of distance targets, with Boolean formulas of up to two input predicates. A trial counted when a formula matched all 37 sampled outcomes and discarded at least the observed mean fraction of candidates under the same weighting. For a paired target, both observed bits had to equal its prediction at every transition.

| Control | Trials with a result at least as selective |
| :--- | ---: |
| Equal weight per ordered segment | 70 / 6,000 (1.17%) |
| Equal weight per geometry | 62 / 6,000 (1.03%) |
| Equal weight per ordered segment, fixing the recorded successor length | 227 / 6,000 (3.78%) |
| Equal weight per geometry, fixing the recorded successor length | 208 / 6,000 (3.47%) |

In the segment-weighted trials, a compatible geometry was sampled uniformly within each selected segment. These frequencies depend on the tested search family and the candidate pools. The formula remains an empirical filter whose performance on new transitions is open.

## 4. Worked example after I ASK

For **I ASK (38)**, use $B=(5,17)$, $E=L=(8,17)$, $U=(11,13)$ and $B_{\mathrm{prev}}=(22,2)$, the start of **AS (37)**. Then

$$
\begin{aligned}
n_2(B)\oplus n_2(B_{\mathrm{prev}})&=605\oplus161=764,\qquad 764\bmod 7=1 \\
n_0(U)+n_0(E)&=283+206=489=3\cdot163,\qquad \mu(489)=+1
\end{aligned}
$$

Both bits are zero, so the next start must be near both reference cells.

| Start allowed by Report 18 | Distance from $B$ | Distance from $L$ | Report 19 |
| :--- | ---: | ---: | :--- |
| `(1,24)` | 7 | 7 | Pass |
| `(3,22)` | 5 | 5 | Pass |
| `(5,20)` | 3 | 3 | Pass |
| `(7,18)` | 2 | 1 | Pass |
| `(9,18)` | 4 | 1 | Pass |
| `(15,24)` | 10 | 7 | Fail |

The **DIE** reading in Report 18 starts at `(3,22)` and follows `(4,23)` and `(5,24)`. The segment therefore passes Report 19. Its ciphertext indices $(17,8,23)$ and aligned key indices $(23,27,5)$ give $(23,10,18)$ modulo 29, or `D · I · E`.

## 5. Direct implementation and verification

The following standalone Python 3.9+ code checks all 37 recorded transitions and the six starts after I ASK. Supply the original key cells and the ciphertext in reading order to `block_geometry` when applying the same functions to newly enumerated candidates. The pool totals and random controls in Section 3 were computed with a separate candidate enumerator. The route coordinates come from [Report 18 at the recorded source revision](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/blob/49673d25d4faf4b3b7bf145f1d815d4f9d41672b/Start-reading-here/18-predicting-next-ciphertext-start-and-end.md).

```python
from dataclasses import dataclass


GRID_SIZE = 27
DISTANCE_LIMIT = 7


@dataclass(frozen=True)
class BlockGeometry:
    upper_key_end: tuple[int, int]
    beginning: tuple[int, int]
    end: tuple[int, int]
    leftmost: tuple[int, int]


def block_geometry(original_key_cells, ciphertext_reading_order):
    """Extract the four cells used by the forecast and distance test."""
    ciphertext = tuple(ciphertext_reading_order)
    return BlockGeometry(
        upper_key_end=min(original_key_cells),
        beginning=ciphertext[0],
        end=ciphertext[-1],
        leftmost=min(ciphertext, key=lambda cell: (cell[1], -cell[0])),
    )


def mobius(n):
    """Return the Möbius value of a positive integer."""
    if n < 1:
        raise ValueError("The Möbius function requires a positive integer.")
    sign = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            if n % factor == 0:
                return 0
            sign = -sign
        factor += 1
    return -sign if n > 1 else sign


def row_major(cell):
    row, column = cell
    return GRID_SIZE * (row - 1) + column


def rotated_180(cell):
    return GRID_SIZE**2 + 1 - row_major(cell)


def forecast_near(current, previous_beginning=None):
    """Return True for a near start and False for a far start."""
    if previous_beginning is None:
        previous_beginning = current.beginning
    start_xor = rotated_180(current.beginning) ^ rotated_180(previous_beginning)
    index_sum = row_major(current.upper_key_end) + row_major(current.end)
    divisible_by_seven = start_xor % 7 == 0
    negative_mobius = mobius(index_sum) < 0
    return divisible_by_seven == negative_mobius


def grid_distance(first, second):
    return max(abs(first[0] - second[0]), abs(first[1] - second[1]))


def accepts_next_beginning(current, next_beginning, near_required):
    near_beginning = grid_distance(current.beginning, next_beginning) <= DISTANCE_LIMIT
    near_leftmost = grid_distance(current.leftmost, next_beginning) <= DISTANCE_LIMIT
    return near_beginning == near_leftmost == near_required


# Each row lists U, B, E and L for one recorded block.
ROUTE = (
    ((13, 11), (13, 25), (14, 4), (14, 1)),  # 01 AS I GO THE
    ((14, 4), (14, 14), (14, 18), (14, 14)),  # 02 WEATHER
    ((4, 23), (14, 19), (10, 19), (14, 19)),  # 03 TURNS
    ((25, 19), (14, 7), (11, 7), (14, 7)),  # 04 COLD
    ((13, 8), (26, 19), (26, 16), (26, 16)),  # 05 I MAY
    ((24, 16), (19, 16), (17, 16), (19, 16)),  # 06 CRY
    ((18, 16), (11, 16), (15, 20), (11, 16)),  # 07 NOW THE
    ((8, 13), (15, 20), (17, 18), (17, 18)),  # 08 IDEA
    ((15, 20), (18, 15), (18, 16), (18, 15)),  # 09 OF
    ((18, 16), (19, 17), (19, 16), (19, 16)),  # 10 THE
    ((19, 16), (19, 23), (21, 23), (21, 23)),  # 11 END
    ((21, 17), (21, 9), (21, 10), (21, 9)),  # 12 IS
    ((19, 16), (26, 3), (26, 1), (26, 1)),  # 13 DEATH
    ((25, 2), (25, 16), (27, 14), (27, 14)),  # 14 SEE
    ((5, 16), (27, 18), (25, 16), (25, 16)),  # 15 YOU
    ((25, 4), (25, 16), (25, 19), (25, 16)),  # 16 SOON
    ((25, 22), (25, 25), (25, 27), (25, 25)),  # 17 THEN
    ((17, 17), (22, 21), (21, 20), (21, 20)),  # 18 THE
    ((11, 16), (21, 4), (19, 4), (21, 4)),  # 19 KEY
    ((17, 3), (18, 7), (19, 6), (19, 6)),  # 20 IS
    ((5, 25), (9, 16), (8, 17), (9, 16)),  # 21 TO
    ((5, 14), (9, 20), (9, 21), (9, 20)),  # 22 GO
    ((11, 11), (12, 23), (12, 22), (12, 22)),  # 23 TO
    ((11, 4), (9, 19), (9, 18), (9, 18)),  # 24 THE
    ((6, 10), (14, 24), (16, 22), (16, 22)),  # 25 EAST
    ((18, 27), (6, 12), (7, 13), (6, 12)),  # 26 OF
    ((23, 1), (20, 12), (20, 13), (20, 12)),  # 27 THE
    ((15, 9), (19, 11), (13, 17), (19, 11)),  # 28 MAP LIFE
    ((11, 13), (18, 11), (18, 13), (18, 11)),  # 29 MAY
    ((14, 15), (25, 12), (26, 11), (26, 11)),  # 30 BE
    ((6, 24), (11, 11), (11, 12), (11, 11)),  # 31 THE
    ((14, 1), (10, 10), (12, 8), (12, 8)),  # 32 DEATH
    ((9, 13), (12, 18), (12, 17), (12, 17)),  # 33 OF
    ((21, 17), (6, 11), (6, 13), (6, 11)),  # 34 YOU
    ((3, 16), (7, 2), (8, 1), (8, 1)),  # 35 GO
    ((13, 1), (27, 1), (27, 2), (27, 1)),  # 36 DO
    ((4, 14), (22, 2), (22, 1), (22, 1)),  # 37 AS
    ((11, 13), (5, 17), (8, 17), (8, 17)),  # 38 I ASK
)


if __name__ == "__main__":
    route = tuple(BlockGeometry(*cells) for cells in ROUTE)
    previous_beginning = None
    near_count = 0
    for step, (current, following) in enumerate(zip(route, route[1:]), start=1):
        near_required = forecast_near(current, previous_beginning)
        if not accepts_next_beginning(current, following.beginning, near_required):
            raise AssertionError(f"Transition {step} -> {step + 1} failed.")
        near_count += near_required
        previous_beginning = current.beginning

    assert len(route) == 38 and near_count == 21
    print(f"{len(route) - 1}/{len(route) - 1} transitions passed.")

    current = route[-1]
    near_required = forecast_near(current, previous_beginning)
    starts_after_i_ask = ((1, 24), (3, 22), (5, 20), (7, 18), (9, 18), (15, 24))
    kept = tuple(
        start
        for start in starts_after_i_ask
        if accepts_next_beginning(current, start, near_required)
    )
    assert near_required and kept == starts_after_i_ask[:-1]
    assert (3, 22) in kept
    print(f"{len(kept)}/{len(starts_after_i_ask)} starts after I ASK passed. DIE passed.")
```
