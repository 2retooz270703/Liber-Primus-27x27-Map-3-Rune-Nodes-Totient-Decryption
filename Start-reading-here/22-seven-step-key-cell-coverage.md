# Report 22 — Seven-Step Coverage by a Single Key Cell

A seven-step compatibility test between the next ciphertext and its original key node preserves **all 38 recorded transitions** through **I ASK → DIE**. After Report 21, it reduces the search from **19,183 to 9,369 geometries**. With the recorded successor length fixed at each transition, it reduces the count from **2,185 to 1,564**. After **GO (22)**, the only surviving geometry decrypts to **TO**. [Report 21](21-conditional-seven-step-bound.md) · [GO (22)](../plaintext-i-found/22-go.md)

## 1. Acceptance test

Use 1-based $(row,column)$ coordinates on the 27 × 27 matrix. All inputs to this test come from the proposed next block.

| Symbol | Meaning |
| :--- | :--- |
| $C'$ | Ordered ciphertext cells |
| $B'$ | First cell of $C'$ in reading order |
| $L'$ | Cell of $C'$ in the smallest column, with the bottommost cell chosen in a tie |
| $U',M',Z'$ | Three actual cells of the original key node, with $M'$ its center |
| $c(X)$ | Column of cell $X$ |
| $d_\infty(X,Y)$ | Chebyshev distance, $\max(|r(X)-r(Y)|,\lvert c(X)-c(Y)\rvert)$ |

Compute the minimum column gap $\Delta$ and the minimum distance $D$ needed for a single key cell to reach both ciphertext anchors:

$$
\begin{aligned}
\Delta &= \min_{Y\in C'} |c(Y)-c(M')|,\\
D &= \min_{X\in\{U',M',Z'\}}
     \max\bigl(d_\infty(X,B'),\,d_\infty(X,L')\bigr).
\end{aligned}
$$

$$
\boxed{\Delta\le 7\quad\Longrightarrow\quad D\le 7.}
$$

If the ciphertext touches the strip extending seven columns to either side of the key center, at least one of the three original key cells must lie in the intersection of the two radius-seven squares centered at $B'$ and $L'$. The **same** key cell must satisfy both distances. When $B'=L'$, the two squares coincide. If the entire ciphertext lies outside the strip, this filter accepts the candidate.

Report 19 measures distances from the current ciphertext to the next start. Report 21 uses the current key and ciphertext to impose a size bound on the next block. Report 22 checks how the candidate successor's own ciphertext and key fit together. [Report 02](02-leftmost-cell-and-rotations.md) · [Report 19](19-predicting-next-ciphertext-start-distance.md) · [Report 21](21-conditional-seven-step-bound.md)

## 2. GO → TO versus BE

After **GO (22)**, seven geometries survive Report 21. **TO** and **BE** use the same original key node, $(11,11)\to(17,17)\to(23,23)$. Their ciphertext positions distinguish them. [GO (22)](../plaintext-i-found/22-go.md) · [TO (23)](../plaintext-i-found/23-to.md)

| Reading | Ordered ciphertext | $\Delta$ | $D$ | Decision |
| :--- | :--- | ---: | ---: | :--- |
| **TO** | (12,23) → (12,22) | 5 | **6** | Accept |
| **BE** | (8,21) → (8,20) | 3 | **9** | Reject |

For TO, the center $(17,17)$ is six steps from $B'$ and five from $L'$. For BE, the best shared key cell is also $(17,17)$, at nine steps from each. The new filter rejects the other five geometries as well. The result is **7 → 1** across all lengths and **5 → 1** at two runes, before the whole-word check in Report 16. [Report 16](16-whole-word-block-boundaries.md)

## 3. I ASK → DIE and other readings

After **I ASK**, the filter reduces the pool from **268 to 138 geometries** across all eligible lengths, and from **180 to 96** at three runes. All seven ordered three-rune segments still have at least one candidate key. The reduction at this length comes from eliminating key–segment pairings. [I ASK (38)](../plaintext-i-found/38-i-ask.md) · [DIE (39)](../plaintext-i-found/39-DIE.md)

| Reading | Original key center | Ordered ciphertext | $\Delta$ | $D$ | Decision |
| :--- | :--- | :--- | ---: | ---: | :--- |
| **DIE** | (18,14) | (3,22) → (4,23) → (5,24) | **8** | 15 | Accept |
| **SLY** | (6,18) | (3,22) → (4,23) → (5,24) | 4 | **3** | Accept |
| **ANT** | (16,20) | (7,18) → (8,19) → (9,20) | 0 | **9** | Reject |
| **WET** | (12,20) | (1,24) → (2,25) → (3,26) | 4 | **11** | Reject |

DIE lies outside the seven-column strip. SLY survives on the same segment with another key, inside the strip. The filter also rejects the three-rune placements for **AIM**, **DING**, and **DUNG**.

## 4. Route validation and selectivity

The route has 39 recorded blocks and 38 incoming transitions. All **38/38** survive, including **19** whose recorded successor enters the strip. The new test removes alternatives at **31** of the 38 current states.

Each pool begins at the recorded current geometry with its accumulated phase state. A geometry counts once per physical key node and ordered ciphertext segment, even if several aligned keys produce different readings. The counts below use the geometric and arithmetic enumeration from Report 21, before the whole-word check. Each percentage in the last column uses the summed pool sizes. [Report 21](21-conditional-seven-step-bound.md)

| Successor pool | After Report 21 | With Report 22 | Geometries removed |
| :--- | ---: | ---: | ---: |
| All eligible lengths | 19,183 | **9,369** | **51.2%** |
| Recorded successor length fixed | 2,185 | **1,564** | **28.4%** |
| Two to seven runes | 9,099 | **5,935** | **34.8%** |

Giving each transition equal weight, the mean shares removed are **32.54%** across all lengths and **24.76%** at the recorded lengths. After **THEN (17)**, the full geometric pool shrinks from **31 to 19**. The restricted Agent27 benchmark shrinks from **16 to 8** key–segment pairs and from **12 to 8** ordered segments. THE survives on J–W. [THEN (17)](../plaintext-i-found/17-then.md) · [Report 20](20-two-orientation-gcd-filter.md)

### One-step lookahead

With Report 21's optional hypothesis of at most seven runes per block, require each intermediate candidate to have at least one geometrically admissible successor. Apply Report 22 both to the intermediate candidate and in its successor search. This preserves the **37/37 recorded intermediate placements**, reducing the earlier lookahead pool from **3,351 to 2,084** geometries. At the recorded successor lengths, the count drops from **802 to 563**. The terminal placement of DIE is covered by the incoming test above. [Report 21](21-conditional-seven-step-bound.md) · [Terminal-block check](../plaintext-i-found/40-why-die-is-the-final-word.md)

## 5. Chronological replay and controls

The proposed test was selected retrospectively. In a chronological replay with both cutoffs fixed at seven, the search considered **1,408** combinations of projection and coverage tests. Among the formulas that passed the first **28** transitions, this formula ranked first by mean removal with the successor length fixed, with mean removal across all lengths as the tiebreaker. It then preserved the last **10/10**, including four recorded successors inside the strip. With a cutoff after **24** transitions, the top test used the ciphertext beginning and end as the coverage anchors. It failed **THE (27) → MAP LIFE (28)**. [MAP LIFE (28)](../plaintext-i-found/28-map-life.md)

The control sampled a geometry uniformly and independently from each of the 38 post-Report-21 pools at the corresponding recorded length. The search family combined 22 row or column projections with 64 coverage measurements. Projections used the candidate center and individual ciphertext anchors, pairs of anchors, or the full ciphertext. Coverage used the original node, its outer cells, its center, or its full geometric span, and tested distances to single anchors or groups of anchors. Each trial counted if any tested formula kept all 38 sampled geometries and matched or exceeded the observed mean removal of **24.76%**.

| Search family in the control | Trials meeting both criteria |
| :--- | ---: |
| Both thresholds fixed at 7 (1,408 expressions) | **0 / 24,000** |
| Both thresholds independently varied from 4 through 10 (68,992 expressions) | **1 / 24,000** |

The frequencies describe these search families and candidate pools. The rule remains an empirical filter on the recorded route. A prospective check can fix the formula and both thresholds before examining a new route.

## 6. Direct implementation and reproduction

Save the Python block as `verify_report22.py` and run it from the project root. It uses the first Python example in the trusted local Report 21 to reproduce its baseline search. The default run verifies the route, pool totals, and worked examples. Use `--lookahead` to verify the optional lookahead counts. The search-family controls are described in Section 5.

```bash
python3 verify_report22.py
python3 verify_report22.py --lookahead
```

```python
from argparse import ArgumentParser
from pathlib import Path
from statistics import mean
from types import ModuleType
import re
import sys


LIMIT = 7


def chebyshev(first, second):
    return max(abs(first[0] - second[0]), abs(first[1] - second[1]))


def column_gap(key_node, ciphertext):
    center_column = key_node[1][1]
    return min(abs(column - center_column) for _, column in ciphertext)


def shared_distance(key_node, ciphertext):
    beginning = ciphertext[0]
    left = min(ciphertext, key=lambda cell: (cell[1], -cell[0]))
    return min(max(chebyshev(cell, beginning), chebyshev(cell, left))
               for cell in key_node)


def passes_report22(key_node, ciphertext):
    return (column_gap(key_node, ciphertext) > LIMIT
            or shared_distance(key_node, ciphertext) <= LIMIT)


def load_report21(root):
    path, = (root / "Start-reading-here").glob("21-*.md")
    pattern = r"```python[ \t]*\n(.*?)\n```"
    example = re.search(pattern, path.read_text(encoding="utf-8"), re.S)
    module = ModuleType("_report22_dependency_21")
    sys.modules[module.__name__] = module
    exec(compile(example[1], str(path), "exec"), vars(module))
    return module


def verify_pools(report21, search, route, before, agent):
    after = [[entry for entry in pool if passes_report22(*entry[:2])]
             for pool in before]
    assert len(route) == 39
    assert all(report21.contains_block(pool, block)
               for pool, block in zip(after, route[1:]))
    assert sum(column_gap(*block) <= LIMIT for block in route[1:]) == 19
    assert sum(len(new) < len(old) for old, new in zip(before, after)) == 31

    lengths = [len(ciphertext) for _, ciphertext in route[1:]]
    for label, eligible, expected in (
        ("All lengths", lambda n, recorded: True, (19183, 9369, 32.54)),
        ("Recorded lengths", lambda n, recorded: n == recorded, (2185, 1564, 24.76)),
        ("Two to seven runes", lambda n, recorded: n <= LIMIT, (9099, 5935, None)),
    ):
        old_counts = [sum(eligible(len(c), n) for _, c, _ in pool)
                      for n, pool in zip(lengths, before)]
        new_counts = [sum(eligible(len(c), n) for _, c, _ in pool)
                      for n, pool in zip(lengths, after)]
        assert (sum(old_counts), sum(new_counts)) == expected[:2]
        if expected[2] is not None:
            removed = mean(1 - new / old for old, new in zip(old_counts, new_counts))
            assert round(100 * removed, 2) == expected[2]
        print(f"{label}: {sum(old_counts):,} -> {sum(new_counts):,}.")

    assert (len(before[21]), len(after[21])) == (7, 1)
    assert search.readings(after[21][0]) == {"TO"}
    be, = [entry for entry in before[21] if "BE" in search.readings(entry)]
    to, = after[21]
    assert be[0] == to[0]
    assert (column_gap(*to[:2]), shared_distance(*to[:2])) == (5, 6)
    assert (column_gap(*be[:2]), shared_distance(*be[:2])) == (3, 9)
    print("After GO (22): TO is the sole surviving geometry.")

    assert (len(before[37]), len(after[37])) == (268, 138)
    before_three = [entry for entry in before[37] if len(entry[1]) == 3]
    after_three = [entry for entry in after[37] if len(entry[1]) == 3]
    assert (len(before_three), len(after_three)) == (180, 96)
    assert report21.segment_count(before_three) == report21.segment_count(after_three) == 7
    for word, keep in (("DIE", True), ("SLY", True), ("AIM", False),
                       ("ANT", False), ("DING", False), ("DUNG", False), ("WET", False)):
        entry, = [item for item in before_three if word in search.readings(item)]
        assert (entry in after_three) == keep, word
    print("After I ASK: 268 -> 138 geometries, or 180 -> 96 at three runes.")

    agent_after = [entry for entry in agent if passes_report22(*entry[:2])]
    assert (len(before[16]), len(after[16])) == (31, 19)
    assert (len(agent), len(agent_after)) == (16, 8)
    assert (report21.segment_count(agent), report21.segment_count(agent_after)) == (12, 8)
    assert report21.contains_block(agent_after, route[17])
    print("Restricted Agent27 pool after THEN: 16 -> 8 pairs.")


def verify_lookahead(report21, search, route, states, before):
    old_total = new_total = old_matched = new_matched = 0
    for i, pool in enumerate(before[:-1]):
        recorded = route[i + 1]
        survivors = []
        for entry in pool:
            if len(entry[1]) > LIMIT:
                continue
            successors = search.successors(
                entry[:2], route[i][1][0], states[i + 1], use_report21=True, cap=True
            )
            first = next(successors, None)
            if first is None:
                continue
            matched = len(entry[1]) == len(recorded[1])
            old_total += 1
            old_matched += matched

            if not passes_report22(*entry[:2]):
                continue
            if (passes_report22(*first[:2])
                    or any(passes_report22(*candidate[:2]) for candidate in successors)):
                new_total += 1
                new_matched += matched
                survivors.append(entry)
        assert report21.contains_block(survivors, recorded), i + 1

    assert (old_total, new_total, old_matched, new_matched) == (3351, 2084, 802, 563)
    print("Lookahead: 37/37 intermediate placements, 3,351 -> 2,084 geometries.")
    print("At the recorded lengths: 802 -> 563.")


if __name__ == "__main__":
    parser = ArgumentParser(description="Reproduce Report 22 in a local project checkout.")
    parser.add_argument("repo", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--lookahead", action="store_true")
    args = parser.parse_args()

    report21 = load_report21(args.repo)
    search = report21.Search(args.repo)
    route = report21.verify_route(search)
    states, _, before, _, agent = report21.verify_pools(search, route)
    verify_pools(report21, search, route, before, agent)
    if args.lookahead:
        verify_lookahead(report21, search, route, states, before)
```
