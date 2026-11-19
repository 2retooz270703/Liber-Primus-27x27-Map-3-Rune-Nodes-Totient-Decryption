# Report 26 — Modulo-Seven Distance Between the Next Key Center and Ciphertext Start

Applied after Reports 00–25, this geometric filter retains **38/38 recorded transitions**. It reduces **2,960 to 1,928** candidate geometries and **563 to 380** distinct dictionary readings across the 38 successor pools. The largest reductions in readings are **119 → 26** after **AS (37)** and **44 → 4** after **GO (35)**. The formula was selected using the recorded route. [Report 25](25-reflected-start-cell-seven-step-bound.md)

## 1. Acceptance test

Use 1-based (row, column) coordinates. Let $U$ be the first extreme of the current original key node in row–column order, $M$ its center, and $E$ the last ciphertext cell in reading order. For a horizontal node, $U$ is its left extreme. Let $M'$ be the candidate key center and $B'$ the candidate ciphertext start.

Compute two quantities from the current block:

- $x=d_1(U,M)$ is the sum of the absolute row and column differences from the key extreme to its center.
- $y=|c(M)-c(E)|$ is the absolute column difference from the key center to the ciphertext end.

Compute $D=d_\infty(M',B')$ for the candidate, using the larger of the absolute row and column differences. Accept it precisely when

$$
[D\bmod 7=0]=[x\le 13]\oplus[y\le 13].
$$

The brackets denote Boolean values. When exactly one of $x$ and $y$ is at most 13, $D$ must be divisible by seven. When both tests give the same answer, $D$ must be nondivisible by seven. The calculation uses only the five cells above. [Report 19](19-predicting-next-ciphertext-start-distance.md) · [Report 24](24-mod-seven-key-center-ciphertext-alignment.md)

## 2. The four divisible-distance transitions

The rule predicts divisibility at four transitions and nondivisibility at the other 34.

| Recorded transition | $x$ | $y$ | $M'$ | $B'$ | $D$ |
| :--- | ---: | ---: | :---: | :---: | ---: |
| **24 THE → 25 EAST** | 3 | 14 | (13, 17) | (14, 24) | 7 |
| **25 EAST → 26 OF** | 14 | 5 | (19, 26) | (6, 12) | 14 |
| **35 GO → 36 DO** | 8 | 19 | (13, 11) | (27, 1) | 14 |
| **37 AS → 38 I ASK** | 4 | 15 | (12, 13) | (5, 17) | 7 |

For **AS → I ASK**, the current cells are $U=(4,14)$, $M=(6,16)$, and $E=(22,1)$. The two threshold tests give opposite answers because $4\le13$ and $15>13$. The recorded successor has $D=\max(7,4)=7$, so it passes. The successor pool falls from 528 to 119 geometries. [AS walkthrough](../plaintext-i-found/37-as.md) · [I ASK walkthrough](../plaintext-i-found/38-i-ask.md)

## 3. Local selectivity after Reports 00–25

Each successor pool starts from the recorded block and its phase history. A geometry pairs one physical key node with one ordered ciphertext segment. Alternative keys at the same geometry count once. A reading is a distinct string within the current transition's pool, using the project's alternate rune transliterations and Hunspell en_US. Word breaks fall between runes, and accepted abbreviations are included. The reported totals sum the counts across transitions. [Report 16](16-whole-word-block-boundaries.md) · [Report 25](25-reflected-start-cell-seven-step-bound.md)

| Successor pools | 00–25 | 00–26 | Removed |
| :--- | ---: | ---: | ---: |
| Geometries, all lengths | 2,960 | **1,928** | **34.9%** |
| Geometries, recorded lengths | 523 | **338** | **35.4%** |
| Dictionary readings, all lengths | 563 | **380** | **32.5%** |
| Dictionary readings, recorded lengths | 237 | **165** | **30.4%** |

The geometry count decreases at **29/38** transitions. The dictionary count decreases at **17/38**, and **7/38** still have a single reading. With equal weight per transition, the mean removal is **19.4%** for geometries and **15.0%** for dictionary readings across all lengths.

| Current block | Geometries, all lengths | Readings, all lengths | Readings, recorded length |
| :--- | ---: | ---: | ---: |
| **24 THE** | 38 → 7 | 18 → 2 | 2 → 2 |
| **25 EAST** | 16 → 5 | 5 → 3 | 2 → 2 |
| **35 GO** | 290 → 2 | 44 → 4 | 27 → 4 |
| **37 AS** | 528 → 119 | 119 → 26 | 41 → 6 |
| **38 I ASK** | 18 → 17 | 4 → 4 | 4 → 4 |

The four divisible-distance transitions account for **151 of the 183** removed readings. After **I ASK**, the pool still admits **DIE**, **A YR**, **AS AE**, and **DO AE**. [I ASK walkthrough](../plaintext-i-found/38-i-ask.md) · [DIE walkthrough](../plaintext-i-found/39-DIE.md)

## 4. Full-route replay

The replay starts with the recorded opening key and ciphertext geometry. It carries phase and the previous ciphertext start along each branch, allows all eligible block lengths, and admits a candidate block if it has at least one dictionary reading. The replay horizon is 39 blocks. A route stops if its 39th block has zero geometric successors under 00–25, before checking the dictionary. A complete geometry is the ordered sequence of key-node and ciphertext-segment pairs. [Opening block](../plaintext-i-found/01-as-i-go-the.md)

| Replay conditions | Geometric routes |
| :--- | ---: |
| 00–25, reach block 39 | 14,322 |
| 00–25, stop at block 39 | 11,177 |
| Stop at block 39, apply Rule 26 on every transition | **3** |
| Stop at block 39, transpose the opening key node at block 38 | **2** |
| Stop at block 39, transpose the opening key node at block 38, require GP = 5,360 | **1** |

The two routes that satisfy the transposition share the same first 38 block geometries. One final geometry gives **DIE** or **DO AE** under two key alignments. The other gives **AS AE**. With the recorded rune readings of the shared prefix fixed, the three complete GP totals are **5,360**, **5,370**, and **5,424**, respectively. Allowing all dictionary-admissible readings of the shared prefix yields 12 different GP totals. Requiring the opening-key checksum still selects one 118-rune sequence ending in **DIE**. This closure check uses the previously recorded 39-block horizon, transposition, and GP target. [Opening-key checksum](../New-strongest-findings/06-opening-key-and-final-gp-sum.md) · [Why DIE is last](../plaintext-i-found/40-why-die-is-the-final-word.md)

## 5. Search-conditioned random controls

In each trial, sample one geometry uniformly and independently from each of the 38 pools obtained under 00–25. Keep the recorded current blocks and phase histories fixed. For the fixed formula, multiply the 38 per-pool fractions that satisfy Rule 26 to obtain the exact match probability in this model.

The broader control repeats the search over **1,298 candidate outcome bits** and **1,319 current-block input bits**. The input family includes coordinates, rotated indices, distances, modular relations, Möbius values, and phase features. Candidate predictors use one bit or the XOR of two bits, with optional complementation. Retain targets with a nonconstant outcome over the first 24 transitions as in the discovery search. A trial counts when one of those formulas matches all 38 sampled outcomes and removes at least as large a mean fraction of geometries as Rule 26, weighting the 38 transitions equally.

| Null pools | Rule 26 mean removal | Exact probability for the fixed formula | Trials with a discovered formula at least as selective |
| :--- | ---: | ---: | ---: |
| Recorded lengths | 18.37% | $2.34\times10^{-5}$ | **1,905 / 20,000 (9.53%)** |
| All lengths | 19.42% | $8.75\times10^{-7}$ | **3,827 / 20,000 (19.14%)** |

The broader frequencies account for the choice of target and predictor within this feature family. They describe independent draws from local successor pools with recorded prefixes. The **38/38** fit and the full-route reduction are retrospective measurements. With the formula frozen, a future transition provides a prospective test.

## 6. Reproduce the results

The reference archive is commit **ffc87143be67dff4362ee397d64ecb1a1850c70e**. Save the Python block as verify_report26.py in the repository root. The default run uses Python 3.9+ and the embedded enumerator in Report 25. The dictionary flag takes the prefix of the Hunspell .aff and .dic files and requires the Hunspell shared library. The optional route replay takes several minutes. The optional random control uses NumPy and a fixed seed.

```bash
python3 verify_report26.py
python3 verify_report26.py --dictionary /usr/share/hunspell/en_US --routes
python3 verify_report26.py --trials 20000
```

```python
from argparse import ArgumentParser
from collections import defaultdict
from functools import cache
from itertools import combinations, product
from math import gcd, prod
from pathlib import Path
from types import ModuleType
import re
import sys


def forecast(current):
    node, cells = current[:2]
    upper, center, _ = sorted(node)
    end = cells[-1]
    key_steps = abs(upper[0] - center[0]) + abs(upper[1] - center[1])
    end_columns = abs(center[1] - end[1])
    return (key_steps <= 13) ^ (end_columns <= 13)


def observed(candidate):
    node, cells = candidate[:2]
    center = node[1]
    start = cells[0]
    steps = max(abs(center[0] - start[0]), abs(center[1] - start[1]))
    return steps % 7 == 0


def load_report25(repo):
    path, = (repo / "Start-reading-here").glob("25-*.md")
    block = re.search(r"\x60{3}python[ \t]*\n(.*?)\n\x60{3}", path.read_text(), re.S)[1]
    module = ModuleType("report26_dependency_25")
    sys.modules[module.__name__] = module
    exec(compile(block, str(path), "exec"), vars(module))
    return module


def reports(repo):
    r25 = load_report25(repo)
    r24 = r25.load_report24(repo)
    r23 = r24.load_report23(repo)
    r22 = r23.load_report22(repo)
    r21 = r22.load_report21(repo)
    search = r21.Search(repo)
    route = r21.verify_route(search)
    states, _, after21, _, _ = r21.verify_pools(search, route)

    def after25(current, pool):
        p23 = r23.forecast(*current, search.rot, search.mu)
        p24 = r24.forecast(*current, search.rot, search.mu)
        for entry in pool:
            node, cells = entry[:2]
            if (r22.passes_report22(node, cells)
                and r23.observed(node, search.rot, search.mu) == p23
                and r24.observed(node, cells, search.rot) == p24
                and r25.passes25(current, entry)):
                yield entry

    return r25, r21, search, route, states, after21, after25


def success_counts(r21, route, before, after, readings):
    assert all(r21.contains_block(pool, following)
               for pool, following in zip(after, route[1:]))
    assert [i for i, block in enumerate(route[:-1], 1) if forecast(block)] == [24, 25, 35, 37]
    assert sum(a != b for a, b in zip(map(len, before), map(len, after))) == 29
    for fixed in (False, True):
        totals = []
        for pool_set in (before, after):
            pools = [
                [e for e in pool if not fixed or len(e[1]) == len(following[1])]
                for pool, following in zip(pool_set, route[1:])
            ]
            geo = sum(map(len, pools))
            words = [len(set().union(*(readings(e) for e in pool))) for pool in pools] if readings else None
            totals.append((geo, words))
        print("Recorded length" if fixed else "All lengths")
        old, new = totals
        assert (old[0], new[0]) == ((523, 338) if fixed else (2960, 1928))
        print(f"  Geometries: {old[0]:,} -> {new[0]:,}")
        if readings:
            expected = (237, 165) if fixed else (563, 380)
            assert (sum(old[1]), sum(new[1])) == expected
            if not fixed:
                assert sum(a != b for a, b in zip(old[1], new[1])) == 17
            print(f"  Dictionary readings: {expected[0]:,} -> {expected[1]:,}")
            print("  Per-transition readings:", list(zip(old[1], new[1])))


def decoder(r25, search, dictionary):
    dll, handle = r25.load_hunspell(dictionary)
    runes = [symbol.split("/") for symbol in search.report[20].RUNES]

    @cache
    def is_word(token):
        if len(token) == 1:
            return token in {"A", "I"}
        return bool(dll.Hunspell_spell(handle, token.lower().encode("ascii")))

    @cache
    def read_code(code):
        if not code:
            return frozenset(("",))
        results = set()
        for stop in range(1, len(code) + 1):
            tokens = {"".join(parts) for parts in product(*(runes[r] for r in code[:stop]))}
            for token in filter(is_word, tokens):
                for tail in read_code(code[stop:]):
                    results.add(f"{token} {tail}" if tail else token)
        return frozenset(results)

    def indices(cells, key):
        return tuple((search.grid[cell] - key[i % 3]) % 29 for i, cell in enumerate(cells))

    @cache
    def decodings(entry):
        _, cells, keys = entry
        return frozenset(code for key in keys if read_code(code := indices(cells, key)))

    @cache
    def readings(entry):
        return frozenset().union(*(read_code(code) for code in decodings(entry)))

    return readings, decodings, indices, lambda: dll.Hunspell_destroy(handle)


def count_routes(search, route, after25, decodings, indices):
    start = (*route[0], route[0][1][0], (0, 0, 0))
    frontier = {start: [1, 1, 1]}
    history = []
    transposed = tuple(sorted((col, row) for row, col in route[0][0]))

    def next_blocks(state):
        node, cells, prev_start, phase = state
        return after25((node, cells), search.successors(
            (node, cells), prev_start, phase, use_report21=True,
        ))

    for step in range(1, 39):
        forward = defaultdict(lambda: [0, 0, 0])
        parents = defaultdict(list)
        for state, (total, local, closed) in frontier.items():
            node, cells, _, phase = state
            next_phase = search.next_state(cells, phase)
            prediction = forecast(state)
            for entry in next_blocks(state):
                if decodings(entry):
                    next_state = (*entry[:2], cells[0], next_phase)
                    counts = forward[next_state]
                    counts[0] += total
                    if observed(entry) == prediction:
                        counts[1] += local
                    if step < 38 or node == transposed:
                        counts[2] += closed
                        parents[next_state].append((state, entry))
        history.append(parents)
        frontier = forward

    reached = sum(n[0] for n in frontier.values())
    ends = {state: n for state, n in frontier.items() if next(next_blocks(state), None) is None}
    stopped, stopped26, reflected = map(sum, zip(*ends.values()))
    print(f"Reached block 39: {reached:,}")
    print(f"Stopped under 00–25: {stopped:,}, with Rule 26: {stopped26:,}, with reflection: {reflected:,}")
    assert (reached, stopped, stopped26, reflected) == (14322, 11177, 3, 2)

    def backwards(state, depth):
        if depth == 0:
            yield ()
            return
        for prior, entry in history[depth - 1][state]:
            for path in backwards(prior, depth - 1):
                yield (*path, entry)

    opening_cell = route[0][0][0]
    row, col = opening_cell
    target = (27 * (row - 1) + col) * search.grid[(col, row)]
    start_code = indices(route[0][1], (25, 10, 28))
    primes = search.report[14].GP_PRIMES
    passing = []
    reflected_paths = []
    totals = set()
    for state, counts in ends.items():
        if counts[2]:
            for path in backwards(state, 38):
                reflected_paths.append(path)
                for codes in product((start_code,), *(decodings(entry) for entry in path)):
                    total = sum(primes[rune] for block in codes for rune in block)
                    totals.add(total)
                    if total == target:
                        passing.append(codes)
    assert len(reflected_paths) == 2
    assert reflected_paths[0][:-1] == reflected_paths[1][:-1]
    assert len(totals) == 12
    assert target == 5360 and len(passing) == 1
    assert sum(map(len, passing[0])) == 118
    assert passing[0][-1] == (23, 10, 18)
    prefix_gp = sum(primes[rune] for block in passing[0][:-1] for rune in block)
    fixed_prefix_totals = {
        prefix_gp + sum(primes[rune] for rune in code)
        for path in reflected_paths
        for code in decodings(path[-1])
    }
    assert prefix_gp == 5173 and fixed_prefix_totals == {5360, 5370, 5424}
    print("Reflected-route GP totals:", sorted(totals))
    print("GP totals with the recorded shared-prefix readings:", sorted(fixed_prefix_totals))
    print(f"With GP {target:,}: one 118-rune sequence, ending D-I-E")


def features(search, r21, node, cells):
    points = dict(zip("UMZBEL", (*sorted(node), cells[0], cells[-1], r21.leftmost(cells))))
    radius = r21.distance(points["U"], points["M"])
    values = {"N": len(cells), "R": radius, "R+N-1": radius + len(cells) - 1}
    for name, (row, col) in points.items():
        values[f"row({name})"] = row
        values[f"col({name})"] = col
        for turn, address in enumerate(search.rot[(row, col)]):
            values[f"n{turn}({name})"] = address
    for u, v in combinations(points, 2):
        ur, uc = points[u]
        vr, vc = points[v]
        dr, dc = ur - vr, uc - vc
        values[f"d∞({u},{v})"] = max(abs(dr), abs(dc))
        values[f"d1({u},{v})"] = abs(dr) + abs(dc)
        values[f"|dr({u},{v})|"] = abs(dr)
        values[f"|dc({u},{v})|"] = abs(dc)
        values[f"dr({u},{v})"] = dr
        values[f"dc({u},{v})"] = dc
        n0u, n0v = values[f"n0({u})"], values[f"n0({v})"]
        values[f"gcd(n0({u}),n0({v}))"] = gcd(n0u, n0v)
        values[f"n0({u})+n0({v})"] = n0u + n0v
    dr = cells[-1][0] - cells[0][0]
    dc = cells[-1][1] - cells[0][1]
    return values, (dr * dc > 0, dr * dc < 0, dr > 0, dc > 0,
                    search.grid[node[0]] == search.grid[node[-1]])


def flags(search, values):
    result = {}
    for name, value in values.items():
        coordinate = "d" in name or name.startswith(("row", "col"))
        if coordinate or name in ("N", "R", "R+N-1", "phase", "outer", "S"):
            for limit in (0, 7, 13) if coordinate else (2, 3, 7):
                result[f"{name}≤{limit}"] = value <= limit
            for modulus in (2, 3, 7):
                residues = range(modulus) if modulus == 2 or (modulus == 3 and name.startswith("d")) else (0,)
                for remainder in residues:
                    result[f"{name}%{modulus}={remainder}"] = value % modulus == remainder
        if name.startswith(("n", "gcd")):
            for divisor in (2, 3, 7):
                result[f"{name}%{divisor}=0"] = value % divisor == 0
            for mobius in (0, 1, -1):
                result[f"μ({name})={mobius}"] = search.mu(value) == mobius
            result[f"{name} prime"] = value > 1 and search.phi(value) == value - 1
    return result


def controls(search, r21, route, states, before, trials):
    import numpy as np

    @cache
    def block_flags(node, cells):
        values, directional = features(search, r21, node, cells)
        result = flags(search, values)
        result.update(zip(("slope+", "slope-", "down", "right", "mirror"), directional))
        return result

    raw_inputs = []
    for (node, cells), (total, outer, phase) in zip(route[:-1], states):
        inputs = dict(block_flags(node, cells))
        inputs.update(flags(search, {"phase": phase, "outer": outer, "S": total}))
        raw_inputs.append(inputs)

    all_bits = (1 << 38) - 1
    first24 = (1 << 24) - 1
    masks = {sum(int(row[name]) << i for i, row in enumerate(raw_inputs)) for name in raw_inputs[0]}
    masks = {min(mask, all_bits ^ mask) for mask in masks}
    predictors = np.array(sorted({0, *masks, *(a ^ b for a, b in combinations(masks, 2))}), dtype=np.uint64)
    names = tuple(block_flags(*route[0]))
    target = names.index("d∞(M,B)%7=0")
    assert (len(raw_inputs[0]), len(masks), len(names)) == (1319, 755, 1298)
    assert len(predictors) == 282075
    prediction = np.array([forecast(block) for block in route[:-1]])
    for fixed in (True, False):
        matrices = [
            np.array([[block_flags(*entry[:2])[name] for name in names]
                      for entry in pool if not fixed or len(entry[1]) == len(following[1])],
                     dtype=np.uint64)
            for pool, following in zip(before, route[1:])
        ]
        rates = np.stack([matrix.mean(axis=0) for matrix in matrices])
        keep = np.where(prediction, rates[:, target], 1 - rates[:, target])
        cutoff = sum(1 - keep)
        rng = np.random.default_rng(1681326)
        hits = 0
        for start in range(0, trials, 256):
            size = min(256, trials - start)
            outcomes = np.zeros((size, len(names)), dtype=np.uint64)
            for i, matrix in enumerate(matrices):
                draws = rng.integers(0, len(matrix), size=size)
                outcomes |= matrix[draws] << np.uint64(i)
            prefix = outcomes & np.uint64(first24)
            normalized = np.minimum(outcomes, outcomes ^ np.uint64(all_bits))
            idx = np.minimum(np.searchsorted(predictors, normalized), len(predictors) - 1)
            candidates = (predictors[idx] == normalized) & (prefix != 0) & (prefix != first24)
            rows, cols = np.nonzero(candidates)
            bits = (outcomes[rows, cols, None] >> np.arange(38, dtype=np.uint64)) & 1
            reject = np.where(bits, 1 - rates[:, cols].T, rates[:, cols].T).sum(axis=1)
            hits += len(np.unique(rows[reject >= cutoff - 1e-10]))
        label = "recorded lengths" if fixed else "all lengths"
        print(f"Controls, {label}: fixed-rule probability {prod(keep):.9g}, "
              f"mean geometric removal {cutoff / 38:.6%}, broad search {hits}/{trials}")


def main():
    parser = ArgumentParser()
    parser.add_argument("repo", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--dictionary", type=Path, help="Path prefix for the en_US .aff and .dic files")
    parser.add_argument("--routes", action="store_true", help="Also enumerate full 39-block routes")
    parser.add_argument("--trials", type=int, default=0, help="Monte Carlo trials per pool, requires NumPy")
    args = parser.parse_args()
    if args.routes and not args.dictionary:
        parser.error("--routes requires --dictionary")
    if args.trials < 0:
        parser.error("--trials must be nonnegative")

    r25, r21, search, route, states, after21, after25 = reports(args.repo)
    before = [list(after25(block, pool)) for block, pool in zip(route, after21)]
    after = [[entry for entry in pool if forecast(block) == observed(entry)]
             for block, pool in zip(route, before)]
    if args.dictionary:
        readings, decodings, indices, close = decoder(r25, search, args.dictionary)
        try:
            success_counts(r21, route, before, after, readings)
            if args.routes:
                count_routes(search, route, after25, decodings, indices)
        finally:
            close()
    else:
        success_counts(r21, route, before, after, None)
    if args.trials:
        controls(search, r21, route, states, before, args.trials)


if __name__ == "__main__":
    main()
```
