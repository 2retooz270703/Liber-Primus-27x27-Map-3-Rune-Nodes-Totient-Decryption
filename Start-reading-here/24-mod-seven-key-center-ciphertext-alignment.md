# Report 24 — Modulo-Seven Alignment of the Next Key Center and Ciphertext

Two arithmetic tests on the current block predict the modulo-seven relation between the next original key center and the leftmost cell of the next ciphertext. The filter preserves **38/38 recorded transitions** and reduces the geometric pool after Report 23 from **5,997 to 4,125**. After **I ASK**, it reduces the pool from **82 to 18** and keeps **DIE** while rejecting **APP** on the same ordered ciphertext segment. [Report 23](23-mobius-forecast-for-next-key-extreme.md)

## 1. Acceptance test

Use 1-based coordinates on the 27 × 27 map. Let `U` be the first geometric extreme of the current original key node in row–column order, `M` its center, and `B` the first cell of the current ciphertext in reading order. Let `M'` be the next original key center and `L'` the next ciphertext's leftmost cell, with the bottommost cell chosen in a tie. The original key's reading direction leaves `U` and `M` fixed. [Report 02](02-leftmost-cell-and-rotations.md)

Use the rotated row-major indices `n_θ` from Report 23. Brackets denote the indicator of a condition. `XOR` combines either two integer indices bitwise or two Boolean bits.

```text
x = n_180(U) XOR n_270(M)
a = [x > 0 and μ(x) = −1]
b = [μ(gcd(n_0(B), n_270(B))) = 0]
```

If `x = 0`, set `a = 0`. This keeps the Möbius input in its positive domain. Accept the proposed next block if the following equality holds.

```text
[(n_0(M') + n_180(L')) mod 7 = 0] = a XOR b
```

## 2. Seven and the derived residue five

On this map, `n_180(X) = 730 − n_0(X)`. The divisibility test is therefore equivalent to the following congruence.

```text
n_0(M') − n_0(L') ≡ −730 ≡ 5 (mod 7)
```

Since `27 ≡ −1 (mod 7)`, this is also equivalent to the following relation between the cells' diagonal coordinates.

```text
(c(M') − r(M')) − (c(L') − r(L')) ≡ 5 (mod 7)
```

A forecast of 1 selects this class of diagonal offsets. A forecast of 0 accepts the other six classes. The residue five follows from the reflected indexing and modulus seven.

Seven recurs in the phase thresholds and 28-unit cycle in Report 11, the start-distance forecast in Report 19, the GCD bound in Report 20, and the geometric bounds in Reports 21 and 22. Here seven governs a periodic positional relation. The recurrence also admits a symbolic reading of seven as a sacred number. [Report 11](11-seven-thresholds-and-cyclic-phase-modes.md) · [Report 19](19-predicting-next-ciphertext-start-distance.md) · [Report 20](20-two-orientation-gcd-filter.md) · [Report 21](21-conditional-seven-step-bound.md) · [Report 22](22-seven-step-key-cell-coverage.md)

## 3. I ASK → DIE versus APP

For **I ASK**, the current cells are `U = (11, 13)`, `M = (12, 13)`, and `B = (5, 17)`. Then `447 XOR 390 = 57` and `μ(57) = +1`. Also, `gcd(125, 275) = 25` and `μ(25) = 0`. Thus `a = 0`, `b = 1`, and the next sum must be divisible by seven.

Both readings use the ordered segment `(3, 22) → (4, 23) → (5, 24)`. Its leftmost cell has `n_180(L') = 654`.

| Reading | Original key center | `n_0(M')` | Sum with 654 | Remainder modulo 7 | Result |
| :--- | :---: | ---: | ---: | ---: | :--- |
| **DIE** | (18,14) | 473 | 1,127 | 0 | Keep |
| APP | (26,6) | 681 | 1,335 | 5 | Reject |

Hunspell `en_US` accepts **28 → 5** segmented readings after I ASK when the search checks boundaries between runes and allows the project's alternate transliterations. The five surviving readings are **A YR**, **AS AE**, **DIE**, **DO AE**, and **WINGING**. **DIE** and **WINGING** are single tokens on separate segments. On the exact DIE segment, the surviving readings are **DIE** and **DO AE**, which share a physical key node and use different key directions. The filter compares cell positions, so both directions on that geometry satisfy the same test. [Report 16](16-whole-word-block-boundaries.md) · [I ASK](../plaintext-i-found/38-i-ask.md) · [DIE](../plaintext-i-found/39-DIE.md)

## 4. Route validation and selectivity

Each local test starts from the recorded current block and its phase history. A geometry counts one physical original key node paired with one ordered ciphertext segment. Aligned keys on the same geometry count once. The counts below precede the word-boundary check.

| Successor pool | With Report 23 | With Report 24 | Share removed |
| :--- | ---: | ---: | ---: |
| All lengths across 38 transitions | 5,997 | **4,125** | 31.2% |
| Recorded successor lengths across 38 transitions | 984 | **715** | 27.3% |
| All lengths after I ASK | 82 | **18** | 78.0% |
| Three runes after I ASK | 54 | **11** | 79.6% |
| One-block lookahead across 37 intermediate transitions | 1,933 | **1,133** | 41.4% |
| Same lookahead with recorded first-step lengths | 357 | **241** | 32.5% |

All **38/38** recorded placements pass. The forecast is 1 on seven transitions. The test removes alternatives at **29/38** current states. Giving each transition equal weight, mean removal is **21.63%** across all lengths and **20.23%** at the recorded lengths.

For lookahead, apply the same rule set at both steps and require a proposed intermediate block to have at least one legal successor. All **37/37** recorded intermediate placements survive. The terminal placement of DIE is checked on its incoming transition.

## 5. Chronological replay and random controls

The filter was selected retrospectively. The search built **8,610** input predicates and **4,746** output predicates before deduplication, using rotated indices, geometric distances, and arithmetic and Möbius tests. Forecasts used up to two input predicates combined by XOR, with optional complementation. With the output predicate fixed, the first **24** recorded transitions left **15** distinct forecast sequences over the 38 input states. The first **28** left **one**, which matched the final **10/10** recorded outcomes. The output predicate itself was chosen with the full route available.

In each control trial, one geometry was drawn uniformly and independently from each Report 23 pool at the recorded successor length. The search retained fits with at least four occurrences of each target bit on the first 24 transitions. It then tested whether any fit reproduced all 38 draws, removed at least **20.23%** on average at recorded lengths, and left at most **18** geometries in the final pool across all lengths. The displayed cutoff is rounded. The comparison used the full measured value.

| Search scope | Matches out of 12,000 trials |
| :--- | ---: |
| Fixed output predicate in Section 1 | 8 (0.07%) |
| All 4,071 distinct output predicates | 1,953 (16.3%) |

These frequencies apply to the tested search families and pools. Report 24 is an empirical filter. A prospective test can fix the three predicates before examining a new route.

## 6. Reproduce the results

Save the Python block below as `verify_report24.py` and run it from the project root. The default run uses the existing Report 23 enumerator and the map, with no third-party packages. The optional `--lookahead` run checks both successive transitions. To reproduce the word counts after I ASK for Reports 23 and 24, pass the prefix of the reference English Hunspell dictionary and use a system installation that exposes the Hunspell C library. [Dictionary details](16-whole-word-block-boundaries.md#4-applying-the-rule-during-searches)

```bash
python3 verify_report24.py
python3 verify_report24.py --lookahead
python3 verify_report24.py --dictionary /usr/share/hunspell/en_US
```

```python
from argparse import ArgumentParser
from functools import cache
from itertools import product
from math import gcd
from pathlib import Path
from statistics import mean
from types import ModuleType
import re
import sys


def forecast(node, ciphertext, indices, mobius):
    upper = min(node)
    center = node[1]
    beginning = ciphertext[0]
    # The index slots represent 0°, 90°, 180°, and 270°, in that order.
    x = indices[upper][2] ^ indices[center][3]
    negative_xor = x > 0 and mobius(x) == -1
    n0, _, _, n270 = indices[beginning]
    nonsquarefree_gcd = mobius(gcd(n0, n270)) == 0
    return negative_xor ^ nonsquarefree_gcd


def observed(next_node, next_ciphertext, indices):
    center = next_node[1]
    leftmost = min(next_ciphertext, key=lambda cell: (cell[1], -cell[0]))
    return (indices[center][0] + indices[leftmost][2]) % 7 == 0


def load_report23(repo):
    path, = (repo / "Start-reading-here").glob("23-*.md")
    source = re.search(
        r"\x60{3}python[ \t]*\n(.*?)\n\x60{3}",
        path.read_text(encoding="utf-8"),
        re.S,
    )[1]
    module = ModuleType("_report24_dependency_23")
    sys.modules[module.__name__] = module
    exec(compile(source, str(path), "exec"), vars(module))
    return module


def verify_counts(report21, search, route, before, after, predicts):
    assert len(before) == len(after) == 38
    assert all(report21.contains_block(pool, block)
               for pool, block in zip(after, route[1:]))
    assert sum(map(predicts, route[:-1])) == 7
    assert sum(len(new) < len(old) for old, new in zip(before, after)) == 29

    lengths = [len(block[1]) for block in route[1:]]
    all_before, all_after = list(map(len, before)), list(map(len, after))
    matched_before = [sum(len(entry[1]) == n for entry in pool)
                      for n, pool in zip(lengths, before)]
    matched_after = [sum(len(entry[1]) == n for entry in pool)
                     for n, pool in zip(lengths, after)]
    assert (sum(all_before), sum(all_after)) == (5997, 4125)
    assert (sum(matched_before), sum(matched_after)) == (984, 715)
    assert (all_before[-1], all_after[-1]) == (82, 18)
    assert (matched_before[-1], matched_after[-1]) == (54, 11)

    for old, new, expected in (
        (all_before, all_after, 21.63),
        (matched_before, matched_after, 20.23),
    ):
        assert round(100 * mean(1 - b / a for a, b in zip(old, new)), 2) == expected

    assert predicts(route[-2])
    last_segment = route[-1][1]
    for word, center, total, keep in [
        ("DIE", (18, 14), 1127, True),
        ("APP", (26, 6), 1335, False),
    ]:
        entry, = [candidate for candidate in before[-1]
                  if candidate[0][1] == center and candidate[1] == last_segment
                  and word in search.readings(candidate)]
        assert search.rot[center][0] + search.rot[last_segment[0]][2] == total
        assert (entry in after[-1]) == keep

    print("38/38 transitions. All lengths: 5,997 -> 4,125. Matched: 984 -> 715.")
    print("After I ASK: 82 -> 18 geometries. Three runes: 54 -> 11.")
    print("On the fixed segment, DIE passes and APP is rejected.")


def verify_lookahead(report21, route, states, before, after, next23, accepts24):
    counts = [0, 0]
    matched = [0, 0]
    for i, recorded in enumerate(route[1:-1]):
        previous_start = route[i][1][0]
        for slot, pool in enumerate((before[i], after[i])):
            survivors = []
            for entry in pool:
                options = next23(entry, previous_start, states[i + 1])
                if any(slot == 0 or accepts24(entry, candidate) for candidate in options):
                    survivors.append(entry)
            assert report21.contains_block(survivors, recorded)
            counts[slot] += len(survivors)
            matched[slot] += sum(len(e[1]) == len(recorded[1]) for e in survivors)
    assert counts == [1933, 1133]
    assert matched == [357, 241]
    print("Lookahead: 37/37 intermediate placements. 1,933 -> 1,133.")
    print("Lookahead at recorded first-step lengths: 357 -> 241.")


def verify_dictionary(search, through22, through23, through24, final_segment, dictionary):
    import ctypes as c
    from ctypes.util import find_library
    from os import fsencode

    names = ("hunspell", "hunspell-1.7", "hunspell-1.6")
    library = next((path for name in names if (path := find_library(name))), None)
    if library is None:
        raise SystemExit("Install a system Hunspell C library to check the word counts.")
    hunspell = c.CDLL(library)
    hunspell.Hunspell_create.argtypes = [c.c_char_p, c.c_char_p]
    hunspell.Hunspell_create.restype = c.c_void_p
    hunspell.Hunspell_spell.argtypes = [c.c_void_p, c.c_char_p]
    hunspell.Hunspell_spell.restype = c.c_int
    hunspell.Hunspell_destroy.argtypes = [c.c_void_p]
    hunspell.Hunspell_destroy.restype = None

    affix = dictionary.with_suffix(".aff")
    words = dictionary.with_suffix(".dic")
    if not affix.is_file() or not words.is_file():
        raise SystemExit(f"Expected both {affix} and {words}.")
    handle = hunspell.Hunspell_create(fsencode(affix), fsencode(words))
    if not handle:
        raise SystemExit("Could not open the Hunspell dictionary.")

    @cache
    def word(token):
        if len(token) == 1:
            return token in {"A", "I"}
        return hunspell.Hunspell_spell(handle, token.lower().encode("ascii")) != 0

    @cache
    def segment(labels):
        if not labels:
            return ((),)
        return tuple(
            (token,) + rest
            for stop in range(1, len(labels) + 1)
            if word(token := "".join(labels[:stop]))
            for rest in segment(labels[stop:])
        )

    def readings(pool):
        rune_options = search.report[20].RUNES
        return {
            " ".join(parts)
            for _, cells, keys in pool
            for key in keys
            for labels in product(*(
                rune_options[(search.grid[cell] - key[i % 3]) % 29].split("/")
                for i, cell in enumerate(cells)
            ))
            for parts in segment(labels)
        }

    try:
        old, filtered = readings(through22), readings(through23)
        assert (len(old), len(filtered)) == (52, 28)
        assert sum(" " not in text for text in old) == 22
        assert {text for text in filtered if " " not in text} == {
            "APP", "DIE", "OBOE", "ROW", "SEC", "SINGS", "SOY", "SSH",
            "TINGS", "TOY", "WINGING", "ZINGS",
        }
        assert readings(through24) == {"DIE", "A YR", "AS AE", "DO AE", "WINGING"}
        fixed = (entry for entry in through24 if entry[1] == final_segment)
        assert readings(fixed) == {"DIE", "DO AE"}
        print("Hunspell en_US after I ASK: 52 -> 28 -> 5 readings (Reports 22, 23, 24).")
    finally:
        hunspell.Hunspell_destroy(handle)


if __name__ == "__main__":
    parser = ArgumentParser(description="Verify Report 24 in a local project checkout.")
    parser.add_argument("repo", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--lookahead", action="store_true")
    parser.add_argument("--dictionary", type=Path, help="Hunspell en_US dictionary prefix")
    args = parser.parse_args()

    report23 = load_report23(args.repo)
    report22 = report23.load_report22(args.repo)
    report21 = report22.load_report21(args.repo)
    search = report21.Search(args.repo)
    route = report21.verify_route(search)
    states, _, after21, _, _ = report21.verify_pools(search, route)

    def accepts23(current, candidate):
        return (report23.observed(candidate[0], search.rot, search.mu)
                == report23.forecast(*current[:2], search.rot, search.mu))

    def predicts(block):
        return forecast(*block[:2], search.rot, search.mu)

    def accepts24(current, candidate):
        return observed(*candidate[:2], search.rot) == predicts(current)

    before = [[e for e in pool
               if report22.passes_report22(*e[:2]) and accepts23(block, e)]
              for block, pool in zip(route, after21)]
    after = [[e for e in pool if accepts24(block, e)]
             for block, pool in zip(route, before)]
    verify_counts(report21, search, route, before, after, predicts)

    if args.lookahead:
        def next23(entry, previous_start, state):
            for candidate in report23.next_geometries(
                search, report22, entry, previous_start, state
            ):
                if accepts23(entry, candidate):
                    yield candidate
        verify_lookahead(report21, route, states, before, after, next23, accepts24)

    if args.dictionary:
        through22 = [e for e in after21[-1] if report22.passes_report22(*e[:2])]
        verify_dictionary(search, through22, before[-1], after[-1], route[-1][1], args.dictionary)
```
