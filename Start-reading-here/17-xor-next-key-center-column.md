# Report 17 — XOR Filter for the Next Key-Center Column

## 1. What the filter does

Given the physical center of the current original three-rune key node, the filter determines which columns remain admissible for the next key center. Apply it to candidate nodes that pass Reports 00–15. Row, radius, axis, and reading order come from the rest of the search.

## 2. Coordinates and rule

Use 1-based `(row, column)` coordinates on the 27 × 27 matrix. Rows increase downward, and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| $M=(r,c)$ | Physical center of the current original key node |
| $M'=(r',c')$ | Physical center of a proposed next original key node |
| $n_3(M)$ | Row-major index of $M$ after a 270° clockwise rotation |
| $\mu$ | Möbius function, as in [Report 00](00-decryption-method.md) |
| $\oplus$ | Bitwise XOR of two integers, written `^` in Python |

Under the rotation convention of [Report 02](02-leftmost-cell-and-rotations.md), $(r,c)$ maps to $(28-c,r)$. Its rotated row-major index is therefore

$$
n_3(M)=27(27-c)+r.
$$

For each candidate column $c'$, compute $x=n_3(M)\oplus c'$. Keep the candidate when

$$
\boxed{\mu\bigl(n_3(M)\oplus c'\bigr)\le 0 \qquad (x>0).}
$$

The filter rejects a positive XOR value exactly when it is squarefree with an even number of distinct prime factors. This includes $x=1$, since $\mu(1)=+1$. For $x=0$, leave the column admissible because the Möbius test is undefined. No recorded transition in this report has $x=0$.

Candidates in the same column receive the same result. The allowed columns can be computed once per current center and reused for the entire candidate list.

## 3. Worked example after I ASK

The current key center is $M=(12,13)$, so $n_3(M)=27(27-13)+12=390$.

| Candidate column $c'$ | $390\oplus c'$ | Möbius value | Decision |
| ---: | ---: | ---: | :--- |
| 2 | 388 | 0 | Keep |
| 3 | 389 | −1 | Keep |
| 4 | 386 | +1 | Reject |

The search based on Reports 00–15 produced **52 distinct candidate centers** after I ASK. This filter leaves **39**. The rejected centers occupy columns 4, 8, and 12. The calculation describes possible continuations within the model.

## 4. Route check

Across the 38 main-route blocks, the rule keeps the proposed next center in **37 of 37 transitions**. For each transition, I enumerated distinct next centers from assignments satisfying Reports 00–15, calculated the fraction removed, and averaged those fractions equally across transitions. The resulting mean reduction was **19.1%**.

The formula was found retrospectively. In a control that sampled one admissible center per transition and repeated the formula search, a single filter with equal or better coverage and pruning appeared in about **0.8%** of runs within the XOR family and **3.1%** within the wider family that also tested sum, absolute difference, AND, OR, and GCD. These percentages describe those controls. An independent route would test whether the filter generalizes.

## 5. Direct implementation and verification

Copy the Python block into a file and run it with Python 3. It checks all 37 recorded transitions and the worked example. To use the filter in a search, call `accepts_next_center(current_center, candidate_center)` or precompute `allowed_next_columns(current_center)`.

```python
from operator import index as integer_index


GRID_SIZE = 27


def mu(n):
    """Return the Mobius value of a positive integer."""
    n = integer_index(n)
    if n < 1:
        raise ValueError("mu requires a positive integer.")

    sign = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            sign = -sign
            if n % factor == 0:
                return 0
        factor += 1
    return -sign if n > 1 else sign


def grid_coordinate(value):
    """Validate one 1-based coordinate component."""
    value = integer_index(value)
    if not 1 <= value <= GRID_SIZE:
        raise ValueError("Grid coordinates must be in 1..27.")
    return value


def n3(cell):
    """Return the 1-based row-major index after 270 degrees clockwise."""
    row, column = map(grid_coordinate, cell)
    return GRID_SIZE * (GRID_SIZE - column) + row


def allowed_next_columns(current_center):
    """Return the columns admitted by the XOR-Mobius filter."""
    rotated_index = n3(current_center)
    allowed = []
    for column in range(1, GRID_SIZE + 1):
        value = rotated_index ^ column
        if value == 0 or mu(value) <= 0:
            allowed.append(column)
    return tuple(allowed)


def accepts_next_center(current_center, candidate_center):
    """Test the proposed center using its column."""
    _, column = map(grid_coordinate, candidate_center)
    value = n3(current_center) ^ column
    return value == 0 or mu(value) <= 0


# Physical centers in the order of the 38 recorded main-route blocks.
ROUTE_CENTERS = (
    (13, 12), (14, 5), (14, 23), (26, 19), (15, 8),
    (25, 16), (19, 16), (11, 16), (17, 18), (19, 16),
    (23, 12), (21, 22), (23, 12), (25, 6), (16, 16),
    (25, 7), (26, 22), (20, 17), (12, 16), (17, 9),
    (8, 25), (12, 14), (17, 17), (14, 4), (13, 17),
    (19, 26), (24, 1), (16, 9), (14, 13), (20, 9),
    (10, 20), (14, 7), (9, 17), (21, 22), (7, 20),
    (13, 11), (6, 16), (12, 13),
)


if __name__ == "__main__":
    failures = [
        (block, block + 1)
        for block, (current, following) in enumerate(
            zip(ROUTE_CENTERS, ROUTE_CENTERS[1:]), start=1
        )
        if not accepts_next_center(current, following)
    ]
    transition_count = len(ROUTE_CENTERS) - 1
    assert transition_count == 37 and not failures, failures

    assert n3((12, 13)) == 390
    assert accepts_next_center((12, 13), (1, 2))
    assert accepts_next_center((12, 13), (1, 3))
    assert not accepts_next_center((12, 13), (1, 4))
    assert 6 in allowed_next_columns((6, 27))  # XOR argument is zero.
    print(f"Recorded transitions passed: {transition_count}/{transition_count}")
```
