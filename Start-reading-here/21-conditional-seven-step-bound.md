# Report 21 — Conditional Seven-Step Bound on Key Radius and Ciphertext Span

The geometry of the current block limits the combined radius and ciphertext span of the next block. This filter preserves **all 38 recorded transitions** through **I ASK → DIE**. It keeps **DIE** and rejects **HOW**, two three-rune readings that pass Reports 19 and 20. On the fixed **J–W** segment after **THEN**, it leaves the key for **THE** as the sole surviving assignment in the Agent27 benchmark.

## 1. Acceptance test

Use 1-based `(row, column)` coordinates on the 27 × 27 matrix. Let

- $U$ be the first cell of the current **original** three-cell key node in row–column order. This is the upper extreme, or the left extreme for a horizontal node.
- $E$ be the last cell of the current ciphertext in reading order.
- $R'$ be the radius of the proposed next key node, measured from its original center to either outer cell.
- $N'$ be the number of cells in the proposed next ciphertext. A contiguous horizontal, vertical, or 45° diagonal segment of $N'$ cells spans $N'-1$ steps.

Measure distances in Chebyshev steps, counting a one-cell diagonal move as one step. For cells $X,Y$, use $d_\infty(X,Y)=\max(|r_X-r_Y|,|c_X-c_Y|)$.

$$
\boxed{d_\infty(U,E)\le 7\quad\Longrightarrow\quad R'+(N'-1)\le 7.}
$$

For a given current block, compute $d_\infty(U,E)$ once. When the bound applies, a next key node of radius $R'$ permits ciphertext lengths up to $8-R'$. For instance, a radius-6 node permits a two-rune block. When $d_\infty(U,E)>7$, this filter accepts every candidate admitted by the preceding rules.

Report 15 supplies the radius parity. Report 19 uses the same seven-step distance to constrain the next ciphertext start. This test measures the gap from the current key extreme to the current ciphertext end and bounds the combined dimensions of the next block. [Report 15](15-predicting-next-key-radius-parity.md) · [Report 19](19-predicting-next-ciphertext-start-distance.md)

## 2. I ASK → DIE versus HOW

For I ASK, $U=(11,13)$ and $E=(8,17)$, so $d_\infty(U,E)=4$. The filter tests both candidates against the same limit. Both pass Report 19 and have $(g_0,g_2)=(1,1)$ under Report 20. [I ASK walkthrough](../plaintext-i-found/38-i-ask.md) · [Report 20](20-two-orientation-gcd-filter.md)

| Reading | Ordered ciphertext | Original key center | $R'$ | $N'-1$ | Sum | Decision |
| :--- | :--- | :---: | ---: | ---: | ---: | :--- |
| **DIE** | (3,22) → (4,23) → (5,24) | (18,14) | 4 | 2 | **6** | Accept |
| **HOW** | (5,20) → (4,21) → (3,22) | (24,16) | 10 | 2 | **12** | Reject |

The DIE key has outer cells $(18,10)$ and $(18,18)$. The HOW key has outer cells $(24,6)$ and $(24,26)$. The key radii separate the readings at the same ciphertext length. After I ASK the filter retains **268 of 837 geometries**. Holding the next ciphertext length at three runes leaves **180 of 334**.

## 3. THEN → THE on J–W

For THEN, $U=(25,22)$ and $E=(25,27)$, so $d_\infty(U,E)=5$. On the ordered segment **J (22,21) → W (21,20)**, $N'-1=1$ for every candidate. Report 20 already rejects **YE**. [THEN walkthrough](../plaintext-i-found/17-then.md)

| Reading | Original key center | $R'$ | $R'+(N'-1)$ | Decision |
| :--- | :---: | ---: | ---: | :--- |
| **THE** | (20,17) | 3 | **4** | Accept |
| **BC** | (18,11) | 7 | **8** | Reject |
| **THX** | (16,21) | 11 | **12** | Reject |

In the restricted Agent27 enumeration reproduced by Report 20, the filter reduces **158 key–segment pairs to 16** and **67 ordered segments to 12**. These counts precede the whole-word check in Report 16. The surviving J–W assignment uses **N–E–N**. [Report 16](16-whole-word-block-boundaries.md) · [THE walkthrough](../plaintext-i-found/18-the.md)

## 4. Route validation and selectivity

The rule passes all **38 recorded transitions** across 39 blocks. The condition applies on **16** of them. Three reach the limit exactly.

| Recorded transition | $R'$ | $N'-1$ | Sum |
| :--- | ---: | ---: | ---: |
| GO (22) → TO (23) | 6 | 1 | 7 |
| MAY (29) → BE (30) | 6 | 1 | 7 |
| OF (33) → YOU (34) | 5 | 2 | 7 |

The route-wide search starts each pool from a recorded current block and its accumulated phase state. A geometry is one physical three-cell key node paired with one ordered ciphertext segment. Both source reading directions and both center operations are allowed where the signature permits them. Alternative aligned keys on the same geometry count once. The pool includes the arithmetic and geometric filters through Report 20 and is measured before Report 16.

| Pool across 38 transitions | After Report 20 | With Report 21 | Mean fraction removed per transition |
| :--- | ---: | ---: | ---: |
| All eligible lengths | 22,734 | **19,183** | **29.8%** |
| Recorded successor length fixed | 2,451 | **2,185** | **13.7%** |

The formula was found retrospectively. In a chronological replay that fixed both limits at seven and the target to $R'+(N'-1)$, the pair $U,E$ removed the most candidates among nine key-anchor and ciphertext-anchor pairs that kept the first 24 transitions. It then kept all 14 remaining transitions, including four where the bound applied.

A separate geometric control sampled one candidate uniformly from each recorded-length pool. Each of 12,000 trials searched nine anchor pairs, four distance measures (Chebyshev, Manhattan, row, and column), two integer limits independently ranging from 3 to 12, and five target quantities ($R'+s'$, $\max(R',s')$, $R'$, $s'$, and $|R'-s'|$, with $s'=N'-1$). **199 trials (1.66%)** found a filter that preserved all sampled transitions and removed at least as much on average. That frequency describes the tested family and candidate pools. A fresh route is needed to test generalization.

## 5. One-step lookahead

The recorded route has a maximum ciphertext length of seven runes. As a separate search hypothesis, cap ciphertext length at seven and apply the cap and Report 21 to both the proposed geometry and its prospective successor. For a block required to be intermediate, keep it only if it has at least one legal successor under these tests and the earlier geometric and arithmetic filters.

On the 37 recorded intermediate transitions, this reduces **21,897 geometries to 3,351** and preserves all 37 recorded placements. With candidate lengths fixed to the recorded lengths, the count drops **from 2,117 to 802**. After THEN, the restricted Agent27 pool drops further **from 16 pairs to 7** and **from 12 segments to 5**, including THE on J–W. The terminal DIE placement has no successor under the filters through Report 20. [Terminal-block check](../plaintext-i-found/40-why-die-is-the-final-word.md)

## 6. Direct implementation and reproduction

Save the Python block below as `verify_report21.py` and run it from the project root with Python 3.9 or later. It uses the existing local report code and `0-2-live-map.html`, and needs no third-party packages. The default run checks the 38 transitions, the Agent27 benchmark, the DIE/HOW split, and the route-wide counts. The optional run also verifies one-step lookahead. Section 4 describes the separate retrospective control.

```bash
python3 verify_report21.py
python3 verify_report21.py --lookahead
```

```python
from argparse import ArgumentParser
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from statistics import mean
from types import ModuleType
import re
import sys


LIMIT = 7
AXES = ((0, 1), (1, 1), (1, 0), (1, -1))


def distance(first, second):
    return max(abs(first[0] - second[0]), abs(first[1] - second[1]))


def successor_span(next_node, next_ciphertext):
    upper, center, _ = sorted(next_node)
    return distance(upper, center) + len(next_ciphertext) - 1


def passes_report21(current_node, current_ciphertext, next_node, next_ciphertext):
    """Test an equally spaced key node and a contiguous successor segment."""
    current_contact = distance(min(current_node), current_ciphertext[-1])
    return current_contact > LIMIT or successor_span(next_node, next_ciphertext) <= LIMIT


def load_report(directory, number):
    """Load the first Python example in a trusted local project report."""
    path, = sorted(directory.glob(f"{number:02d}-*.md"))
    example = re.search(r"```python[ \t]*\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S)
    module = ModuleType(f"_report21_dependency_{number:02d}")
    sys.modules[module.__name__] = module
    exec(compile(example[1], str(path), "exec"), vars(module))
    return module


def leftmost(ciphertext):
    return min(ciphertext, key=lambda cell: (cell[1], -cell[0]))


def index_key_nodes(grid, mu, phi):
    indexed = defaultdict(lambda: defaultdict(set))
    for row, col in grid:
        center = (row, col)
        for axis, (dr, dc) in enumerate(AXES):
            for radius in range(1, 14):
                upper = (row - dr * radius, col - dc * radius)
                lower = (row + dr * radius, col + dc * radius)
                if upper not in grid or lower not in grid:
                    break
                node = (upper, center, lower)
                first, middle, last = map(grid.__getitem__, node)
                if min(first, middle, last) < 1:
                    continue
                for a, c in {(first, last), (last, first)}:
                    for b in {middle, phi(middle)}:
                        key = (a, b, c)
                        signature = tuple(mu(phi(value)) for value in key)
                        phase = sum(signature) % 3
                        group = (axis, radius % 2, row % 2, col % 2, a == c, signature)
                        indexed[group][node].add(key[phase:] + key[:phase])
    return indexed


def index_segments(grid):
    indexed = defaultdict(list)
    directions = AXES + tuple((-dr, -dc) for dr, dc in AXES)
    for start in grid:
        for dr, dc in directions:
            axis = "horizontal" if dr == 0 else "vertical" if dc == 0 else "diagonal"
            cells = [start]
            for span in range(1, 27):
                end = (start[0] + dr * span, start[1] + dc * span)
                if end not in grid:
                    break
                cells.append(end)
                left = leftmost((start, end))
                group = (axis, start == left, end[0] % 2, left[0] % 2, left[1] % 2)
                indexed[group].append((tuple(cells), start, end, left))
    return indexed


class Search:
    def __init__(self, repo):
        directory = repo / "Start-reading-here"
        self.report = {
            n: load_report(directory, n)
            for n in (3, 4, 5, 7, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20)
        }
        self.matrix = self.report[20].read_matrix(repo / "0-2-live-map.html")
        self.grid = {
            (i // 27 + 1, i % 27 + 1): value for i, value in enumerate(self.matrix)
        }
        self.rot = {cell: self.report[18].rotated_indices(cell) for cell in self.grid}
        self.mu = lru_cache(maxsize=None)(self.report[18].mu)
        self.phi = self.report[20].totient
        self.nodes = index_key_nodes(self.grid, self.mu, self.phi)
        self.segments = index_segments(self.grid)

    def next_state(self, ciphertext, state):
        total, outer, _ = state
        next_phase = self.report[11].expected_next_phase(ciphertext, total, self.mu)
        next_outer = (outer + self.mu(self.rot[leftmost(ciphertext)][1])) % 2
        return total + next_phase, next_outer, next_phase

    def successors(self, current, previous_start, state, *, use_report21=False, cap=False):
        r, mu = self.report, self.mu
        total, _, phase = state
        node, cipher = current
        center = node[1]
        start = cipher[0]
        left = leftmost(cipher)
        raw_runes = tuple(self.grid[cell] for cell in node)
        next_total, next_outer, next_phase = self.next_state(cipher, state)
        if r[11].skips_seven_threshold(total, next_phase):
            return

        middle = (next_phase - 2 * next_outer + 1) % 3 - 1
        signature = (next_outer, middle, next_outer)
        key_axis = r[14].expected_next_key_axis(node, cipher, raw_runes, mu)
        radius_bit = r[15].expected_next_key_radius_parity(node, cipher, mu)
        center_bits = r[4].expected_next_key_center_parities(cipher, center, mu)
        mirror = bool(r[7].expected_next_key_mirror_bit(node, cipher))
        key_group = (key_axis, radius_bit, center_bits["row"], center_bits["column"],
                     mirror, signature)
        keys = [(candidate_node, tuple(sorted(aligned)))
                for candidate_node, aligned in self.nodes[key_group].items()
                if r[17].accepts_next_center(center, candidate_node[1])]
        if not keys:
            return

        axis = r[3].expected_next_axis_and_boundary(cipher, center, raw_runes[1], mu, self.phi)
        rows = r[5].expected_next_row_parities(cipher, center, phase, mu)
        column = r[9].expected_next_column_parity(cipher, center, phase,
                                                  int(raw_runes[0] == raw_runes[2]), mu)
        group = (axis["axis"], bool(axis["leftmost_first"]),
                 rows["endpoint"], rows["leftmost"], column)
        ray = r[12].expected_next_ray_offset(cipher, mu)
        allowed_sign = -1 if next_total // LIMIT % 4 in (1, 2) else 1
        bits = r[18].predict_next_ciphertext_bits(node, cipher)
        geometry = r[19].block_geometry(node, cipher)
        near = r[19].forecast_near(geometry, previous_start)
        active = use_report21 and distance(min(node), cipher[-1]) <= LIMIT

        for cells, begin, end, left_cell in self.segments[group]:
            if cap and len(cells) > LIMIT:
                continue
            if mu(self.rot[left_cell][1]) * allowed_sign < 0:
                continue
            if r[12].ray_offset(left, begin) != ray:
                continue
            if bits != r[18].observed_next_ciphertext_bits(node, start, begin, end):
                continue
            if not r[19].accepts_next_beginning(geometry, begin, near):
                continue
            for candidate_node, aligned in keys:
                if active and successor_span(candidate_node, cells) > LIMIT:
                    continue
                candidate_center = candidate_node[1]
                if not r[20].passes_report20(candidate_center, begin):
                    continue
                if r[10].accepts_next_key_and_ciphertext(candidate_center, cells, mu):
                    yield candidate_node, cells, aligned

    def readings(self, entry):
        _, cells, keys = entry
        runes = self.report[20].RUNES
        return {
            "".join(runes[(self.grid[cell] - key[i % 3]) % 29].split("/")[0]
                    for i, cell in enumerate(cells))
            for key in keys
        }


def segment_count(pool):
    return len({cells for _, cells, _ in pool})


def contains_block(pool, block):
    node, cells = block
    return any(entry[:2] == (tuple(sorted(node)), cells) for entry in pool)


def verify_route(search):
    recorded = search.report[18].ROUTE
    last = (((18, 10), (18, 14), (18, 18)), ((3, 22), (4, 23), (5, 24)))
    route = recorded + (last,)
    active = []
    for block_number, (current, following) in enumerate(zip(route, route[1:]), 1):
        assert passes_report21(*current, *following), block_number
        if distance(min(current[0]), current[1][-1]) <= LIMIT:
            active.append((block_number, successor_span(*following)))
    assert len(route) == 39 and len(active) == 16
    assert [number for number, score in active if score == LIMIT] == [22, 29, 33]
    assert max(len(cells) for _, cells in route) == LIMIT
    print("Recorded transitions: 38/38. Active: 16. Tight transitions: 22, 29, 33.")
    return route


def verify_agent27(search, route, pools):
    report20 = search.report[20]
    current, following = route[16:18]
    benchmark_keys = dict(report20.mirror_keys_after_then(search.matrix))
    benchmark_segments = set(report20.agent27_segments())
    benchmark = [
        (node, cells, (benchmark_keys[node[1]],))
        for node, cells, keys in pools[16]
        if (cells[0], cells[-1]) in benchmark_segments
        and benchmark_keys.get(node[1]) in keys
    ]
    remaining = [entry for entry in benchmark if passes_report21(*current, *entry[:2])]
    assert (len(benchmark), segment_count(benchmark)) == (158, 67)
    assert (len(remaining), segment_count(remaining)) == (16, 12)
    fixed_span = following[1]
    readings = {next(iter(search.readings(entry))): successor_span(*entry[:2])
                for entry in benchmark if entry[1] == fixed_span}
    assert readings == {"THE": 4, "BC": 8, "THX": 12}
    assert [search.readings(entry) for entry in remaining if entry[1] == fixed_span] == [{"THE"}]
    print("Agent27 after THEN: 158 -> 16 pairs, 67 -> 12 segments. J-W: THE.")
    return remaining


def verify_pools(search, route):
    states = [(0, 0, 0)]
    for _, cipher in route[:-1]:
        states.append(search.next_state(cipher, states[-1]))
    pools, retained, matched, retained_matched = [], [], [], []
    for i, (current, following) in enumerate(zip(route, route[1:])):
        previous_start = route[max(0, i - 1)][1][0]
        before = list(search.successors(current, previous_start, states[i]))
        after = [entry for entry in before if passes_report21(*current, *entry[:2])]
        assert contains_block(after, following), i + 1
        pools.append(before)
        retained.append(after)
        length = len(following[1])
        matched.append(sum(len(entry[1]) == length for entry in before))
        retained_matched.append(sum(len(entry[1]) == length for entry in after))

    for before, after, expected in [
        (list(map(len, pools)), list(map(len, retained)), (22734, 19183, 29.84)),
        (matched, retained_matched, (2451, 2185, 13.74)),
    ]:
        average = 100 * mean(1 - y / x for x, y in zip(before, after))
        observed = (sum(before), sum(after), round(average, 2))
        assert observed == expected, observed
        print(f"{sum(before):,} -> {sum(after):,} geometries. Mean removed: {average:.2f}%.")

    assert (len(pools[-1]), len(retained[-1])) == (837, 268)
    assert (matched[-1], retained_matched[-1]) == (334, 180)
    for word, center, start, expected, keep in [
        ("DIE", (18, 14), (3, 22), 6, True),
        ("HOW", (24, 16), (5, 20), 12, False),
    ]:
        alternatives = [entry for entry in pools[-1] if word in search.readings(entry)]
        entry, = alternatives
        assert (entry[0][1], entry[1][0], len(entry[1])) == (center, start, 3)
        assert search.report[20].gcd_pair(center, start) == (1, 1)
        assert successor_span(*entry[:2]) == expected
        assert (entry in retained[-1]) == keep
        print(f"After I ASK, {word}: score {expected}, {'accepted' if keep else 'rejected'}.")

    agent = verify_agent27(search, route, pools)
    return states, pools, retained, matched, agent


def verify_lookahead(search, route, states, pools, retained, matched, agent):
    def has_next(i, entry):
        return next(search.successors(entry[:2], route[i][1][0], states[i + 1],
                                      use_report21=True, cap=True), None) is not None

    remaining = matched_remaining = 0
    for i, pool in enumerate(retained[:-1]):
        eligible = [entry for entry in pool if len(entry[1]) <= LIMIT and has_next(i, entry)]
        assert contains_block(eligible, route[i + 1]), i + 1
        remaining += len(eligible)
        matched_remaining += sum(len(entry[1]) == len(route[i + 1][1]) for entry in eligible)
    assert (sum(map(len, pools[:-1])), remaining) == (21897, 3351)
    assert (sum(matched[:-1]), matched_remaining) == (2117, 802)
    earlier = [entry for entry in agent if len(entry[1]) <= LIMIT and has_next(16, entry)]
    assert (len(earlier), segment_count(earlier)) == (7, 5)
    assert contains_block(earlier, route[17])
    assert next(search.successors(route[-1], route[-2][1][0], states[-1]), None) is None
    print("Lookahead: 37/37 interior transitions; 21,897 -> 3,351 geometries.")
    print("Length-matched: 2,117 -> 802. Agent27: 7 pairs, 5 segments. DIE: no successor.")


if __name__ == "__main__":
    parser = ArgumentParser(description="Reproduce Report 21 from a local project checkout.")
    parser.add_argument("repo", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--lookahead", action="store_true", help="Run the optional one-step test.")
    args = parser.parse_args()
    search = Search(args.repo)
    route = verify_route(search)
    measurements = verify_pools(search, route)
    if args.lookahead:
        verify_lookahead(search, route, *measurements)
```
