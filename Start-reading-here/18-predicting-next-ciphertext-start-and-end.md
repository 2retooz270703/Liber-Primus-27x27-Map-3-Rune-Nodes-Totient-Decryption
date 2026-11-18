# Report 18 — Predicting Three Bits of the Next Ciphertext's Geometry

## 1. What the rule predicts

[Report 17](17-xor-next-key-center-column.md) filters columns of the next original key center. The three tests here filter the next **ciphertext segment**. They predict:

1. Whether the vertical displacement of its end from the current original key node's first geometric extreme is at least the horizontal displacement.
2. Whether its end has a negative Möbius value in the unrotated row-major numbering.
3. Whether its beginning is strictly to the right of the current ciphertext beginning.

Apply the tests to candidates that satisfy the applicable earlier reports. Each test contributes one bit. A candidate passes the combined filter when all three observed bits agree with their predictions.

## 2. Coordinates and inputs

Use 1-based `(row, column)` coordinates on the 27 × 27 matrix. Rows increase downward and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| \(U,M,Z\) | Three cells of the current **original** key node, in lexicographic `(row, column)` order. \(U\) is the upper extreme, or the left extreme for a horizontal node. \(M\) is the midpoint. \(Z\) is the opposite extreme. |
| \(B,E\) | First and last **current ciphertext** cells in reading order |
| \(L\) | Leftmost current ciphertext cell. At equal columns, choose the larger row. |
| \(B',E'\) | Beginning and end of a proposed **next ciphertext** segment in reading order |
| \(X_k=n_k(X)\) | Row-major index of cell \(X\) after a \(90k^\circ\) clockwise rotation |
| \([P]\) | 1 when proposition \(P\) holds, otherwise 0 |
| \(\oplus\) | XOR of bits, written `^` in Python |

As in [Report 02](02-leftmost-cell-and-rotations.md) and [Report 14](14-predicting-exact-next-key-axis.md), the four indices are

$$
\begin{aligned}
n_0(r,c)&=27(r-1)+c, & n_1(r,c)&=27(c-1)+28-r,\\
n_2(r,c)&=730-n_0(r,c), & n_3(r,c)&=730-n_1(r,c).
\end{aligned}
$$

Use the Möbius function from [Report 00](00-decryption-method.md). Define

$$
g_-(a,b)=[\mu(\gcd(a,b))<0],
\qquad
g_0(a,b)=[\mu(\gcd(a,b))=0].
$$

The second indicator is 1 exactly when both arguments share a prime-square factor. The geometric order \(U,M,Z\) stays the same if the original key is read in reverse. For a current block that wraps between rows, use its entire recorded ciphertext sequence to choose \(L\).

## 3. The three XOR formulas

### A. Sector of the next endpoint

$$
\begin{aligned}
\widehat v
&=g_-(M_2,L_3)\oplus[\mu(Z_3+B_2)>0]\oplus g_-(M_3,L_2),\\
v(B',E')
&=[\,|r(E')-r(U)|\ge |c(E')-c(U)|\,].
\end{aligned}
$$

A tie goes in the vertical sector. The two outer terms use the same pair \(M,L\), with the 180° and 270° rotations exchanged.

### B. Möbius sign at the next endpoint

$$
\begin{aligned}
\widehat m
&=g_0(M_2,L_0)\oplus g_0(M_1,B_1)\oplus g_0(M_2,E_0),\\
m(B',E')&=[\mu(n_0(E'))<0].
\end{aligned}
$$

Here \(\widehat m=0\) admits either \(\mu(n_0(E'))=0\) or \(\mu(n_0(E'))=+1\).

### C. Side of the next beginning

$$
\begin{aligned}
\widehat h
&=g_0(U_1,E_0)\oplus g_-(U_0,B_2)
   \oplus\left(\left\lfloor\frac{E_3}{4}\right\rfloor\bmod 2\right),\\
h(B',E')&=[\,c(B')>c(B)\,].
\end{aligned}
$$

The division extracts bit 2 of \(E_3\), counting the least significant bit as bit 0. Equal columns give \(h=0\).

The complete acceptance test is \((v,m,h)=(\widehat v,\widehat m,\widehat h)\). Every input to the forecast comes from the current block.

## 4. Results on the recorded route

A distinct geometry identifies the three physical key cells and the **ordered** beginning and end of a ciphertext segment. Different key orders or center-totient choices at the same cells count once. For each current block, the candidate geometries were enumerated under Reports 00–15 and then filtered by Report 17. No word dictionary entered these enumeration counts.

| Filters | Sum of distinct geometries over the 37 transitions |
| :--- | ---: |
| Reports 00–15 | 165,626 |
| Reports 00–15 and 17 | 120,222 |
| Add Rule A | 75,023 |
| Add all three rules in Report 18 | **41,791** |

All **37 recorded transitions** pass each rule and the combined filter. Averaging the fraction removed separately for each transition gives a **69.4%** reduction after Report 17. Sampling with equal weight per ordered ciphertext segment gives a **69.5%** mean reduction. The combined filter leaves **2,844** of **10,168** ordered segments summed over the 37 transitions.

### Search-conditioned controls

For each simulated dataset, one eligible successor was sampled per transition. The search was rerun across geometric target bits and the tested family of XOR predictors using up to three current-block predicates. That family used rotated cell indices, coordinate bits, phase or length inputs, and Möbius predicates of single indices, sums, and GCDs. A simulated result counted when it reproduced all 37 sampled outcomes and rejected at least as many candidates on average as the observed formula or combination under the same weighting.

| Control | Rule A or a single rule at least as selective | Rule B or a single rule at least as selective | Rule C or a single rule at least as selective | A combination at least as selective as all three |
| :--- | ---: | ---: | ---: | ---: |
| Equal weight per ciphertext segment | 410/4,000 (10.3%) | 2,051/4,000 (51.3%) | 2,105/4,000 (52.6%) | **227/4,000 (5.7%)** |
| Equal weight per segment, with recorded successor length fixed at each transition | 492/4,000 (12.3%) | 2,158/4,000 (54.0%) | 1,601/4,000 (40.0%) | **319/4,000 (8.0%)** |

With recorded lengths fixed, the combined filter still removes **66.4%** of distinct ordered segments on average. In the geometry-weighted controls, the corresponding frequencies for the combined filter were **272/5,000 (5.4%)** and **380/5,000 (7.6%)**. These estimates apply to the tested search family and candidate pools.

Rule A retains only 25–27 transitions when any one of its three terms is omitted. A global offset of 90°, 180°, or 270° in its input rotations yields 21, 25, or 16 matches, respectively. Rule B predicts a negative Möbius value on five transitions. The first term of Rule C is active only after **YOU (15)** and **BE (30)**, and removing it leaves 35 matches.

The three formulas were selected retrospectively on the recorded route. In an exploratory chronological check that selected the strongest geometric bit using only the first 33 transitions, the selected predictor matched **one of the final four**. Report 18 is an experimental filter. Its reliability on a new route remains to be tested with the formulas fixed in advance.

## 5. Worked example after I ASK

The original key node of **I ASK (38)** has \(U=(11,13)\), \(M=(12,13)\), and \(Z=(13,13)\). Its ciphertext starts at \(B=(5,17)\) and ends at \(E=L=(8,17)\). The forecast is **\((0,0,1)\)**.

If the same transition rules are continued beyond I ASK, Report 17 leaves **7,171** geometries representing **132** ordered ciphertext segments. Adding all three rules leaves **1,080** geometries representing **21** ordered segments. The number of distinct starts falls from 15 to six, and the number of distinct ends falls from 72 to 17. All **39** previously admissible next key centers still occur in at least one surviving geometry.

The remaining start coordinates are

$$
(1,24),\ (3,22),\ (5,20),\ (7,18),\ (9,18),\ (15,24).
$$

### A surviving reading of DIE

The ciphertext segment \((3,22)\to(4,23)\to(5,24)\) contains `B · H · D`, with rune indices \((17,8,23)\). The source node at \((18,10),(18,14),(18,18)\) gives `C/K · D · IA`. With phase 1 the aligned key is `D · IA · C/K`, with indices \((23,27,5)\). Subtraction modulo 29 gives

$$
(17,8,23)-(23,27,5)\equiv(23,10,18),
$$

or **`D · I · E`**.

- The end \((5,24)\) lies 6 rows and 11 columns away from \(U\), so \(v=0\).
- The endpoint's unrotated index is 132, with \(\mu(132)=0\), so \(m=0\).
- The start has column 22, greater than the current beginning's column 17, so \(h=1\).

This is one admissible continuation. The same filters also admit **HOW**.

## 6. Direct implementation and verification

The following Python 3 code has no third-party dependencies. It checks the three formulas on all 37 recorded transitions and verifies the Report 17 and 18 tests and modular subtraction for the DIE example. The included checks use the recorded route as input. The enumeration totals and random controls above come from the separate candidate search.

```python
from math import gcd
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


def cell(coordinates):
    """Validate and normalize one 1-based grid cell."""
    row, column = map(integer_index, coordinates)
    if not (1 <= row <= GRID_SIZE and 1 <= column <= GRID_SIZE):
        raise ValueError("Cell coordinates must be in 1..27.")
    return row, column


def rotated_indices(coordinates):
    """Return row-major indices for 0, 90, 180 and 270 degrees clockwise."""
    row, column = cell(coordinates)
    n0 = GRID_SIZE * (row - 1) + column
    n1 = GRID_SIZE * (column - 1) + GRID_SIZE + 1 - row
    opposite = GRID_SIZE ** 2 + 1
    return n0, n1, opposite - n0, opposite - n1


def sorted_key_node(node):
    """Return the equally spaced original key cells in geometric order."""
    upper, middle, lower = sorted(map(cell, node))
    dr = middle[0] - upper[0]
    dc = middle[1] - upper[1]
    if (dr, dc) == (0, 0) or not (dr == 0 or dc == 0 or abs(dr) == abs(dc)):
        raise ValueError("The key node must lie on a nondegenerate four-axis line.")
    if (middle[0] + dr, middle[1] + dc) != lower:
        raise ValueError("The middle key cell must bisect its two extremes.")
    return upper, middle, lower


def predict_next_ciphertext_bits(current_node, current_cipher_cells):
    """Return the three forecast bits (vertical sector, negative mu, right)."""
    U, M, Z = map(rotated_indices, sorted_key_node(current_node))
    cipher = tuple(map(cell, current_cipher_cells))
    if not cipher:
        raise ValueError("The current ciphertext must be nonempty.")
    B = rotated_indices(cipher[0])
    E = rotated_indices(cipher[-1])
    L = rotated_indices(min(cipher, key=lambda x: (x[1], -x[0])))

    vertical = (
        (mu(gcd(M[2], L[3])) < 0)
        ^ (mu(Z[3] + B[2]) > 0)
        ^ (mu(gcd(M[3], L[2])) < 0)
    )
    negative = (
        (mu(gcd(M[2], L[0])) == 0)
        ^ (mu(gcd(M[1], B[1])) == 0)
        ^ (mu(gcd(M[2], E[0])) == 0)
    )
    right = (
        (mu(gcd(U[1], E[0])) == 0)
        ^ (mu(gcd(U[0], B[2])) < 0)
        ^ ((E[3] // 4) % 2 == 1)
    )
    return int(vertical), int(negative), int(right)


def observed_next_ciphertext_bits(current_node, current_beginning, beginning, end):
    """Evaluate the three properties on a proposed next ciphertext segment."""
    u_row, u_column = sorted_key_node(current_node)[0]
    _, current_column = cell(current_beginning)
    _, next_column = cell(beginning)
    end_row, end_column = cell(end)
    return (
        int(abs(end_row - u_row) >= abs(end_column - u_column)),
        int(mu(rotated_indices(end)[0]) < 0),
        int(next_column > current_column),
    )


def accepts_next_ciphertext_segment(current_node, current_cipher_cells, beginning, end):
    """Test a segment that was admitted by the applicable earlier reports."""
    cipher = tuple(current_cipher_cells)
    prediction = predict_next_ciphertext_bits(current_node, cipher)
    observed = observed_next_ciphertext_bits(
        current_node, cipher[0], beginning, end
    )
    return prediction == observed


# Each entry contains the original key node and the ciphertext in reading order.
ROUTE = (
    (((13, 11), (13, 12), (13, 13)), ((13, 25), (13, 26), (13, 27), (14, 1), (14, 2), (14, 3), (14, 4))),  # 01 AS I GO THE
    (((14, 4), (14, 5), (14, 6)), ((14, 14), (14, 15), (14, 16), (14, 17), (14, 18))),  # 02 WEATHER
    (((4, 23), (14, 23), (24, 23)), ((14, 19), (13, 19), (12, 19), (11, 19), (10, 19))),  # 03 TURNS
    (((25, 19), (26, 19), (27, 19)), ((14, 7), (13, 7), (12, 7), (11, 7))),  # 04 COLD
    (((13, 8), (15, 8), (17, 8)), ((26, 19), (26, 18), (26, 17), (26, 16))),  # 05 I MAY
    (((24, 16), (25, 16), (26, 16)), ((19, 16), (18, 16), (17, 16))),  # 06 CRY
    (((18, 16), (19, 16), (20, 16)), ((11, 16), (12, 17), (13, 18), (14, 19), (15, 20))),  # 07 NOW THE
    (((8, 13), (11, 16), (14, 19)), ((15, 20), (16, 19), (17, 18))),  # 08 IDEA
    (((15, 20), (17, 18), (19, 16)), ((18, 15), (18, 16))),  # 09 OF
    (((18, 16), (19, 16), (20, 16)), ((19, 17), (19, 16))),  # 10 THE
    (((19, 16), (23, 12), (27, 8)), ((19, 23), (20, 23), (21, 23))),  # 11 END
    (((21, 17), (21, 22), (21, 27)), ((21, 9), (21, 10))),  # 12 IS
    (((19, 16), (23, 12), (27, 8)), ((26, 3), (26, 2), (26, 1))),  # 13 DEATH
    (((25, 2), (25, 6), (25, 10)), ((25, 16), (26, 15), (27, 14))),  # 14 SEE
    (((5, 16), (16, 16), (27, 16)), ((27, 18), (26, 17), (25, 16))),  # 15 YOU
    (((25, 4), (25, 7), (25, 10)), ((25, 16), (25, 17), (25, 18), (25, 19))),  # 16 SOON
    (((25, 22), (26, 22), (27, 22)), ((25, 25), (25, 26), (25, 27))),  # 17 THEN
    (((17, 17), (20, 17), (23, 17)), ((22, 21), (21, 20))),  # 18 THE
    (((11, 16), (12, 16), (13, 16)), ((21, 4), (20, 4), (19, 4))),  # 19 KEY
    (((17, 3), (17, 9), (17, 15)), ((18, 7), (19, 6))),  # 20 IS
    (((5, 25), (8, 25), (11, 25)), ((9, 16), (8, 17))),  # 21 TO
    (((5, 14), (12, 14), (19, 14)), ((9, 20), (9, 21))),  # 22 GO
    (((11, 11), (17, 17), (23, 23)), ((12, 23), (12, 22))),  # 23 TO
    (((11, 4), (14, 4), (17, 4)), ((9, 19), (9, 18))),  # 24 THE
    (((6, 10), (13, 17), (20, 24)), ((14, 24), (15, 23), (16, 22))),  # 25 EAST
    (((18, 27), (19, 26), (20, 25)), ((6, 12), (7, 13))),  # 26 OF
    (((23, 1), (24, 1), (25, 1)), ((20, 12), (20, 13))),  # 27 THE
    (((15, 9), (16, 9), (17, 9)), ((19, 11), (18, 12), (17, 13), (16, 14), (15, 15), (14, 16), (13, 17))),  # 28 MAP LIFE
    (((11, 13), (14, 13), (17, 13)), ((18, 11), (18, 12), (18, 13))),  # 29 MAY
    (((14, 15), (20, 9), (26, 3)), ((25, 12), (26, 11))),  # 30 BE
    (((6, 24), (10, 20), (14, 16)), ((11, 11), (11, 12))),  # 31 THE
    (((14, 1), (14, 7), (14, 13)), ((10, 10), (11, 9), (12, 8))),  # 32 DEATH
    (((9, 13), (9, 17), (9, 21)), ((12, 18), (12, 17))),  # 33 OF
    (((21, 17), (21, 22), (21, 27)), ((6, 11), (6, 12), (6, 13))),  # 34 YOU
    (((3, 16), (7, 20), (11, 24)), ((7, 2), (8, 1))),  # 35 GO
    (((13, 21), (13, 11), (13, 1)), ((27, 1), (27, 2))),  # 36 DO
    (((4, 14), (6, 16), (8, 18)), ((22, 2), (22, 1))),  # 37 AS
    (((11, 13), (12, 13), (13, 13)), ((5, 17), (6, 17), (7, 17), (8, 17))),  # 38 I ASK
)


if __name__ == "__main__":
    failures = []
    for step, (current, following) in enumerate(zip(ROUTE, ROUTE[1:]), start=1):
        node, cipher = current
        _, next_cipher = following
        if not accepts_next_ciphertext_segment(
            node, cipher, next_cipher[0], next_cipher[-1]
        ):
            failures.append((step, step + 1))

    total = len(ROUTE) - 1
    if total != 37 or failures:
        raise AssertionError(f"Route fixture or prediction failed: {failures}")

    i_ask_node, i_ask_cipher = ROUTE[-1]
    die_node = ((18, 10), (18, 14), (18, 18))
    die_beginning, die_end = (3, 22), (5, 24)
    forecast = predict_next_ciphertext_bits(i_ask_node, i_ask_cipher)
    column_mask = rotated_indices(i_ask_node[1])[3] ^ die_node[1][1]

    assert forecast == (0, 0, 1)
    assert column_mask == 392 and mu(column_mask) == 0  # Report 17.
    assert accepts_next_ciphertext_segment(
        i_ask_node, i_ask_cipher, die_beginning, die_end
    )
    encrypted = (17, 8, 23)      # B, H, D
    aligned_key = (23, 27, 5)    # D, IA, C/K
    assert tuple((x - k) % 29 for x, k in zip(encrypted, aligned_key)) == (
        23, 10, 18               # D, I, E
    )
    print(f"Recorded transitions passed: {total}/{total}")
    print("I ASK -> DIE: Reports 17 and 18 checks passed")
```
