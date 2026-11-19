# Report 20 — Two-Orientation GCD Filter for the Next Key Center

This rule tests the compatibility of a candidate key center with the first cell of the next ciphertext block. It passes **all 38 recorded transitions**, through **I ASK → DIE**. On the fixed **J–W** segment after **THEN**, it retains **THE** and excludes **YE** using the coordinates of the candidate alone.

## 1. Acceptance test

Use 1-based `(row, column)` coordinates on the 27 × 27 matrix. Rows increase downward, and columns increase to the right.

- $M'$ is the center of the candidate's **original three-cell key node**.
- $B'$ is the **first ciphertext cell in reading order**.

Number cells row by row in the original orientation and after a 180° rotation, following [Report 02](02-leftmost-cell-and-rotations.md).

$$
n_0(r,c)=27(r-1)+c,\qquad n_2(r,c)=730-n_0(r,c)
$$

Compute the two greatest common divisors and apply the same bound to both.

$$
\begin{aligned}
g_0 &= \gcd\bigl(n_0(M')\,n_0(B')\bigr) \\
g_2 &= \gcd\bigl(n_2(M')\,n_0(B')\bigr) \\
\text{Accept} &\quad\Longleftrightarrow\quad \max(g_0,g_2)\le 7
\end{aligned}
$$

Apply this test alongside the earlier constraints. The $g_0$ term uses the same pair of indices as [Report 10](10-squarefree-gcd-compatibility.md), condition G1. Report 10 still applies its squarefree test to that pair. Here the bound also applies to $g_2$, computed with the rotated center and the original ciphertext start. For example, $g_2=4$ passes the bound.

## 2. Resolving THE versus YE after THEN

Agent27 found two complete English readings on the same ordered segment, **J (22,21) → W (21,20)**. Both satisfy the earlier filters in the published enumeration. The first cell is J, so both candidates use $n_0(B')=588$. [Agent27's report](https://github.com/FlareZ123/liber-primus/blob/6e0929fcda701e768121fa9c378fa7b36886d43b/communications/broadcast/20261118T1835Z_agent27_27square_reports17to19_remaining_key_ambiguity.md) · [Reference enumeration](https://github.com/FlareZ123/liber-primus/blob/6e0929fcda701e768121fa9c378fa7b36886d43b/sims/lp2_p0_27square_reports17_19_ambiguity_sft.cjs)

| Reading | Center $M'$ | $n_0(M')$ | $n_2(M')$ | $g_0$ | $g_2$ | Decision |
| :--- | :---: | ---: | ---: | ---: | ---: | :--- |
| **THE** | (20,17) | 530 | 200 | 2 | **4** | **Pass** |
| **YE** | (8,25) | 214 | 516 | 2 | **12** | **Reject** |
| THX | (16,21) | 426 | 304 | 6 | 4 | Pass |
| BC | (18,11) | 470 | 260 | 2 | 4 | Pass |

The derived key is **N–E–N** for THE and **X–E–X** for YE. The two readings tie at $g_0=2$. The rotated-center term separates them: $\gcd(200,588)=4$ and $\gcd(516,588)=12$. After applying the complete-word criterion in [Report 16](16-whole-word-block-boundaries.md), **THE is the only complete English word among these four readings of J–W**. The test can reject the YE key before testing any follow-on reading such as KEY.

### Effect on Agent27's candidate pool

The reference enumeration after THEN uses up-left ciphertext segments and vertically symmetric key nodes with the center totient applied. The counts are **key–segment pairs** before dictionary screening.

| Stage | Pairs | Ordered segments |
| :--- | ---: | ---: |
| After Report 19 | 268 | 67 |
| With Report 20 | **158** | **67** |

The filter removes **110 of 268 pairs (41.0%)** in this enumeration. Every segment retains at least one key. The exact-pool check below reconstructs the four keys from the matrix and verifies these counts.

## 3. Route validation

The rule was evaluated on the 39 recorded blocks from AS I GO THE to DIE, giving **38 incoming transitions**. The distribution of $\max(g_0,g_2)$ is shown below.

| Maximum GCD | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Recorded transitions | 17 | 8 | 3 | 4 | 2 | 3 | 1 |

The unique maximum of **7** occurs on **DEATH (32) → OF (33)**. For [I ASK (38)](../plaintext-i-found/38-i-ask.md) → [DIE (39)](../plaintext-i-found/39-DIE.md), $M'=(18,14)$ and $B'=(3,22)$ give $\gcd(473,76)=1$ and $\gcd(257,76)=1$.

In the route-wide enumeration after Reports 00–15 and 17–19, giving each transition equal weight, the mean share of candidate geometries removed was **15.5%**. With the recorded successor length held fixed, it was **11.4%**. Each geometry is a physical three-cell key node paired with an ordered ciphertext segment.

### Random controls

The formula and cutoff were selected retrospectively. The controls sampled one geometry uniformly from each transition's candidate pool. Each trial repeated the search over 72 GCD expressions and integer cutoffs from 2 through 13. The family used the ciphertext start, end, or leftmost cell, with four rotations for each cell index. It tested both individual GCDs and maxima over opposite orientations of the key center. A trial counted if at least one filter passed all 38 sampled transitions and removed at least as many candidates on average as Report 20 under the same weighting.

| Candidate pools | Control trials meeting both criteria |
| :--- | ---: |
| All eligible lengths | 193 / 12,000 (1.6%) |
| Recorded successor lengths fixed | 1,839 / 12,000 (15.3%) |

The length-matched control gives the more conservative comparison within this family. The observed route fit and the rejection of YE on J–W are exact replay results. The fixed formula provides a criterion to test on future transitions.

## 4. Direct implementation and reproduction

Save the Python block as `verify_report20.py`. Python 3.9 or later and the standard library are sufficient. The route check runs on its own. Pass the project's [map HTML](../0-2-live-map.html) to also rerun the exact Agent27 pool after THEN, including the four J–W readings. The route-wide enumeration and random controls above were run separately.

```bash
python3 verify_report20.py
python3 verify_report20.py 0-2-live-map.html
```

```python
from argparse import ArgumentParser
from collections import Counter
from functools import lru_cache
from math import gcd
from pathlib import Path
import re


SIZE = 27
BOUND = 7
RUNES = (
    "F U/V TH O R C/K G W H N I J EO P X S/Z "
    "T B E M L NG OE D A AE Y IA/IO EA"
).split()


def index0(cell):
    row, column = cell
    if not (1 <= row <= SIZE and 1 <= column <= SIZE):
        raise ValueError(f"Cell outside the matrix: {cell}")
    return SIZE * (row - 1) + column


def index1(cell):
    row, column = cell
    return index0((column, SIZE + 1 - row))


def index2(cell):
    return SIZE**2 + 1 - index0(cell)


def index3(cell):
    return SIZE**2 + 1 - index1(cell)


def gcd_pair(key_center, cipher_start):
    start_index = index0(cipher_start)
    return gcd(index0(key_center), start_index), gcd(index2(key_center), start_index)


def passes_report20(key_center, cipher_start):
    return max(gcd_pair(key_center, cipher_start)) <= BOUND


# Each row contains the original key center and the first ciphertext cell.
ROUTE = (
    ((13, 12), (13, 25)),  # 01 AS I GO THE
    ((14, 5), (14, 14)),  # 02 WEATHER
    ((14, 23), (14, 19)),  # 03 TURNS
    ((26, 19), (14, 7)),  # 04 COLD
    ((15, 8), (26, 19)),  # 05 I MAY
    ((25, 16), (19, 16)),  # 06 CRY
    ((19, 16), (11, 16)),  # 07 NOW THE
    ((11, 16), (15, 20)),  # 08 IDEA
    ((17, 18), (18, 15)),  # 09 OF
    ((19, 16), (19, 17)),  # 10 THE
    ((23, 12), (19, 23)),  # 11 END
    ((21, 22), (21, 9)),  # 12 IS
    ((23, 12), (26, 3)),  # 13 DEATH
    ((25, 6), (25, 16)),  # 14 SEE
    ((16, 16), (27, 18)),  # 15 YOU
    ((25, 7), (25, 16)),  # 16 SOON
    ((26, 22), (25, 25)),  # 17 THEN
    ((20, 17), (22, 21)),  # 18 THE
    ((12, 16), (21, 4)),  # 19 KEY
    ((17, 9), (18, 7)),  # 20 IS
    ((8, 25), (9, 16)),  # 21 TO
    ((12, 14), (9, 20)),  # 22 GO
    ((17, 17), (12, 23)),  # 23 TO
    ((14, 4), (9, 19)),  # 24 THE
    ((13, 17), (14, 24)),  # 25 EAST
    ((19, 26), (6, 12)),  # 26 OF
    ((24, 1), (20, 12)),  # 27 THE
    ((16, 9), (19, 11)),  # 28 MAP LIFE
    ((14, 13), (18, 11)),  # 29 MAY
    ((20, 9), (25, 12)),  # 30 BE
    ((10, 20), (11, 11)),  # 31 THE
    ((14, 7), (10, 10)),  # 32 DEATH
    ((9, 17), (12, 18)),  # 33 OF
    ((21, 22), (6, 11)),  # 34 YOU
    ((7, 20), (7, 2)),  # 35 GO
    ((13, 11), (27, 1)),  # 36 DO
    ((6, 16), (22, 2)),  # 37 AS
    ((12, 13), (5, 17)),  # 38 I ASK
    ((18, 14), (3, 22)),  # 39 DIE
)


def verify_route():
    # The first block has no incoming transition.
    incoming = ROUTE[1:]
    assert len(incoming) == 38
    assert all(passes_report20(*destination) for destination in incoming)
    scores = [max(gcd_pair(*destination)) for destination in incoming]
    assert Counter(scores) == {1: 17, 2: 8, 3: 3, 4: 4, 5: 2, 6: 3, 7: 1}
    assert scores.index(7) + 2 == 33
    assert gcd_pair(*ROUTE[-1]) == (1, 1)
    print("Recorded transitions through DIE: 38/38")


@lru_cache(maxsize=None)
def mobius(value):
    sign = 1
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            value //= factor
            if value % factor == 0:
                return 0
            sign = -sign
        factor += 1
    return -sign if value > 1 else sign


@lru_cache(maxsize=None)
def totient(value):
    return sum(gcd(step, value) == 1 for step in range(1, value + 1))


def read_matrix(map_path):
    html = map_path.read_text(encoding="utf-8")
    tokens = re.findall(r'<span class="rune">([^<]+)</span>', html)
    if len(tokens) != SIZE**2:
        raise ValueError(f"Expected 729 rune cells, found {len(tokens)}.")
    rune_index = {rune: index for index, rune in enumerate(RUNES)}
    return tuple(rune_index[token] for token in tokens)


def mirror_keys_after_then(grid):
    # Reports 00–16 specialize to even rows, odd columns, odd radii,
    # vertical mirrors and the phase-zero signature (+1,+1,+1).
    for row in range(2, SIZE, 2):
        for column in range(1, SIZE + 1, 2):
            center = (row, column)
            for radius in range(1, min(row - 1, SIZE - row) + 1, 2):
                cells = ((row - radius, column), center, (row + radius, column))
                upper, middle, lower = (grid[index0(cell) - 1] for cell in cells)
                if min(upper, middle, lower) < 1 or upper != lower:
                    continue
                key = (upper, totient(middle), lower)
                if all(mobius(totient(value)) == 1 for value in key):
                    yield center, key


def agent27_segments():
    # After THEN the Agent27 benchmark uses the up-left slope.
    # The leftmost cell is the endpoint on every such segment.
    for row in range(2, SIZE + 1):
        for column in range(2, SIZE + 1):
            dr, dc = abs(row - 25), abs(column - 25)
            if min(dr, dc, abs(dr - dc)) != 1:
                continue
            for length in range(2, min(row, column) + 1):
                end = (row - length + 1, column - length + 1)
                if end[0] % 2 != 1 or end[1] % 2 != 0:
                    continue
                if mobius(index1(end)) <= 0:
                    yield (row, column), end


def verify_agent27_pool(grid):
    keys = tuple(mirror_keys_after_then(grid))
    assert [center for center, _ in keys] == [(8, 25), (16, 21), (18, 11), (20, 17)]
    counts = [0] * 5
    segments_before = set()
    segments_after = set()
    readings = {}
    for start, end in agent27_segments():
        for center, key in keys:
            # Report 10. G2 repeats the endpoint check in this benchmark.
            divisors = (
                gcd(index0(center), index0(start)),
                gcd(index0(center), index0(end)),
                gcd(index1(center), index3(end)),
                gcd(index0(center), index2(end)),
            )
            if any(mobius(value) == 0 for value in divisors):
                continue
            counts[0] += 1
            # Report 17, with n3 of the THEN center equal to 161.
            xor_index = 161 ^ center[1]
            if xor_index and mobius(xor_index) > 0:
                continue
            counts[1] += 1
            # Report 18 predicts the bits (1, 0, 0) after THEN.
            upper_row, upper_col = (25, 22)
            end_row, end_col = end
            sector = abs(end_row - upper_row) >= abs(end_col - upper_col)
            negative = mobius(index0(end)) < 0
            right = start[1] > 25
            if (sector, negative, right) != (True, False, False):
                continue
            counts[2] += 1
            # Report 19 predicts near. THEN starts at its leftmost cell.
            if max(abs(start[0] - 25), abs(start[1] - 25)) > 7:
                continue
            counts[3] += 1
            segments_before.add((start, end))
            keep = passes_report20(center, start)
            if keep:
                counts[4] += 1
                segments_after.add((start, end))
            if (start, end) == ((22, 21), (21, 20)):
                cipher = [grid[index0(cell) - 1] for cell in (start, end)]
                assert cipher == [11, 7]
                plain = [(rune - shift) % 29 for rune, shift in zip(cipher, key)]
                word = "".join(RUNES[value].split("/")[0] for value in plain)
                readings[word] = (center, gcd_pair(center, start), keep)
    assert counts == [1104, 1104, 604, 268, 158]
    assert len(segments_before) == len(segments_after) == 67
    assert readings == {
        "THE": ((20, 17), (2, 4), True),
        "YE": ((8, 25), (2, 12), False),
        "THX": ((16, 21), (6, 4), True),
        "BC": ((18, 11), (2, 4), True),
    }
    print("Agent27 pairs through Report 20:", " → ".join(map(str, counts)))
    print("Ordered segments after Reports 19 and 20: 67 → 67")
    for word in ("THE", "YE", "THX", "BC"):
        center, divisors, keep = readings[word]
        print(f"{word:3}  {center}  GCDs={divisors}  {'pass' if keep else 'reject'}")


if __name__ == "__main__":
    parser = ArgumentParser(description="Verify Report 20.")
    parser.add_argument("map_html", type=Path, nargs="?", help="Project 0-2-live-map.html")
    args = parser.parse_args()
    verify_route()
    if args.map_html is not None:
        verify_agent27_pool(read_matrix(args.map_html))
```
