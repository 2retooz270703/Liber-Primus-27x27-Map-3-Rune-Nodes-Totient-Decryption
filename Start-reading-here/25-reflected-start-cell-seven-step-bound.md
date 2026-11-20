# Report 25 — Reflected Start-Cell Offset Bound (Seven-Step Margin)

This report proposes a **local, one-step geometric filter** for the next ciphertext start. It uses only the current block's original key node and ciphertext start, plus the proposed next ciphertext start. It does **not** use the proposed plaintext, a fixed terminal block, a full-route closure condition, or the next key's content.

Applied after Reports 00–24, the filter retains **38/38 recorded transitions**. Across those 38 independently enumerated successor pools, it reduces **4,125 to 2,960 geometric candidates** (28.2% removed) and **857 to 600 distinct dictionary readings** (30.0% removed). The largest reading reductions occur after **TO (block 23)** and **BE (block 30)**. These are retrospective results, not independent evidence of a cipher rule. [Report 24](24-mod-seven-key-center-ciphertext-alignment.md)

## 1. Acceptance test

Use 1-based `(row, column)` coordinates on the 27 × 27 map.

- `B`: **first cell** of the current ciphertext in its recorded reading direction.
- `Z`: the **lower geometric extreme** of the current original three-cell key node; for a horizontal node, take its rightmost extreme. Equivalently, `Z = max(node)` when cells are sorted by `(row, column)`.
- `B'`: first cell of a proposed next ciphertext, in its proposed reading direction.
- `R(r, c) = (28 - r, 28 - c)`: 180-degree rotation of a map cell.

Define the nonnegative distances:

```text
dc = abs(column(B') - column(R(Z)))
dr = abs(row(B')    - row(R(B)))
```

**Accept the next block if and only if:**

```text
dc <= dr + 7
```

Equivalently, reject when `dc - dr > 7`. Both coordinates used in the comparison are rotated, but they come from **different current-block cells**: the key extreme `Z` contributes the column and the ciphertext start `B` contributes the row. The next candidate contributes only `B'`.

This is a deterministic *accept/reject test*, **not** a deterministic choice of one unique next block. It is applied after the preceding rules, not as a replacement for them.

## 2. Three transitions exactly on the boundary

Exactly **3 of the 38 recorded transitions** have `dc = dr + 7`; all other 35 have `dc - dr < 7`. The three equality cases are:

| Transition | `B` | `Z` | `B'` | `dc` | `dr` | `dc - dr` |
| :--- | :---: | :---: | :---: | ---: | ---: | ---: |
| **21 TO → 22 GO** | (9,16) | (11,25) | (9,20) | 17 | 10 | **7** |
| **23 TO → 24 THE** | (12,23) | (23,23) | (9,19) | 14 | 7 | **7** |
| **26 OF → 27 THE** | (6,12) | (20,25) | (20,12) | 9 | 2 | **7** |

For example, at **23 TO → 24 THE**, `R(Z) = (5,5)` and `R(B) = (16,5)`. Hence:

```text
dc = abs(19 - 5) = 14
dr = abs(9 - 16) = 7
14 <= 7 + 7  ->  ACCEPT
```

The constant **7 is the maximum observed `dc - dr` on the recorded route**. Lowering it to 6 would reject all three transitions above. The repeated appearance of seven elsewhere in the project provides a motivation for investigating this threshold, **but does not independently derive or validate this particular inequality**. [Report 19](19-predicting-next-ciphertext-start-distance.md) · [Report 21](21-conditional-seven-step-bound.md) · [Report 22](22-seven-step-key-cell-coverage.md)

## 3. Measured effect after Reports 00–24

Each row starts at a *recorded* current block with its recorded phase history. The enumerator considers all eligible next lengths, keys and ciphertext segments under Reports 00–24, then applies the new inequality. One geometry is a physical key node paired with an ordered ciphertext segment; alternative aligned keys on the same geometry are not double-counted. Dictionary readings are distinct strings **within each row**, and may contain multiple complete words. They are evaluated using Hunspell `en_US`, the project's rune transliteration alternatives, and word breaks only between runes. Abbreviations accepted by the dictionary are not excluded.

| Successor pools over 38 transitions | Rules 00–24 | Rules 00–25 | Removed |
| :--- | ---: | ---: | ---: |
| Geometries, all successor lengths | 4,125 | **2,960** | **28.2%** |
| Geometries, recorded successor lengths | 715 | **523** | **26.9%** |
| Distinct dictionary readings, all lengths | 857 | **600** | **30.0%** |
| Distinct dictionary readings, recorded lengths | 333 | **252** | **24.3%** |

**The largest local effects:**

| Current block | Geometries | Dictionary readings | Known successor |
| :--- | ---: | ---: | :--- |
| **07 NOW THE** | 22 → 4 | **11 → 3** | IDEA |
| **23 TO** | 775 → 127 | **181 → 36** | THE |
| **26 OF** | 557 → 489 | **87 → 71** | THE |
| **27 THE** | 261 → 138 | **33 → 18** | MAP LIFE |
| **30 BE** | 332 → 90 | **117 → 45** | THE |
| **37 AS** | 581 → 528 | **127 → 126** | I ASK |

There are four additional transitions where geometries decrease but the number of distinct dictionary readings does not: **09 OF**, **10 THE**, **33 OF**, and **34 YOU**. Thus the filter changes the geometric pool at **10/38** transitions and the dictionary-reading count at **6/38** transitions. After **I ASK**, the same five readings remain **A YR**, **AS AE**, **DIE**, **DO AE**, and **WINGING**. [Report 16](16-whole-word-block-boundaries.md) · [I ASK](../plaintext-i-found/38-i-ask.md) · [DIE](../plaintext-i-found/39-DIE.md)

The totals above **sum per-transition counts**, so the same string (for example `THE`) appearing in two different rows contributes twice to the aggregate. They are not counts of unique strings over the entire 39-block route, nor counts of complete paths.

## 4. Limits of the claim

1. **38/38 is in-sample.** The margin `+7` is the observed maximum over the same 38 transitions used for evaluation. The fact that the three boundary cases are retained therefore does not constitute a prospective test.
2. **Selective rather than uniformly strong.** The 28.2% aggregate geometry reduction is dominated by a few broad successor pools. Ten transitions lose at least one geometry; the other 28 are unchanged. A stronger claim would require testing the fixed formula on new, unseen transitions or a separately specified null model that accounts for searching many candidate formulas.
3. **Not an exact next-word rule.** This test depends on coordinates and filters candidates before dictionary checking. It preserves multiple readings and does not prove that the proposed plaintext is the original Liber Primus text.
4. **No semantic selection.** Dictionary membership and optional word segmentation do not assess whether the candidate makes grammatical or contextual sense.

**Status:** reproducible **empirical candidate for Report 25**, suitable for comparing against new local rules. Do not treat it as a proven cipher mechanism.

## 5. Reproduce the results

Save the following code as `verify_report25.py` in the project root. It loads the embedded Python implementation from Report 24 and its existing dependencies, so the same map, key geometry, phase history and candidate generator are used. A normal run verifies the geometric counts and all 38 recorded transitions; the optional Hunspell check verifies the word totals. No dictionary is required for the geometric check.

```bash
python3 verify_report25.py
python3 verify_report25.py --dictionary /usr/share/hunspell/en_US
```

```python
from argparse import ArgumentParser
from ctypes import CDLL, c_char_p, c_void_p, c_int
from ctypes.util import find_library
from functools import cache
from itertools import product
from pathlib import Path
from types import ModuleType
import re
import sys


def passes25(current, candidate):
    node, ciphertext = current[:2]
    _, next_ciphertext = candidate[:2]
    beginning = ciphertext[0]
    lower_extreme = max(node)
    next_beginning = next_ciphertext[0]
    rotated_extreme = (28 - lower_extreme[0], 28 - lower_extreme[1])
    rotated_beginning = (28 - beginning[0], 28 - beginning[1])
    dc = abs(next_beginning[1] - rotated_extreme[1])
    dr = abs(next_beginning[0] - rotated_beginning[0])
    return dc <= dr + 7


def load_report24(repo):
    path, = (repo / "Start-reading-here").glob("24-*.md")
    source = re.search(
        r"\x60{3}python[ \t]*\n(.*?)\n\x60{3}",
        path.read_text(encoding="utf-8"), re.S,
    )[1]
    module = ModuleType("_report25_dependency_24")
    sys.modules[module.__name__] = module
    exec(compile(source, str(path), "exec"), vars(module))
    return module


def load_hunspell(prefix):
    library = find_library("hunspell-1.7") or find_library("hunspell")
    if library is None:
        raise SystemExit("Hunspell C library not installed")
    dll = CDLL(library)
    dll.Hunspell_create.argtypes = [c_char_p, c_char_p]
    dll.Hunspell_create.restype = c_void_p
    dll.Hunspell_spell.argtypes = [c_void_p, c_char_p]
    dll.Hunspell_spell.restype = c_int
    dll.Hunspell_destroy.argtypes = [c_void_p]
    aff, dic = prefix.with_suffix(".aff"), prefix.with_suffix(".dic")
    if not aff.is_file() or not dic.is_file():
        raise SystemExit("Expected dictionary files: " + str(aff) + ", " + str(dic))
    handle = dll.Hunspell_create(str(aff).encode(), str(dic).encode())
    if not handle:
        raise SystemExit("Unable to open Hunspell dictionary")
    return dll, handle


def reading_sets(search, pools, hunspell, handle):
    runes = search.report[20].RUNES

    @cache
    def is_word(token):
        if len(token) == 1:
            return token in {"A", "I"}
        return hunspell.Hunspell_spell(handle, token.lower().encode("ascii")) != 0

    @cache
    def split_words(labels):
        if not labels:
            return ((),)
        return tuple(
            (token,) + rest
            for stop in range(1, len(labels) + 1)
            if is_word(token := "".join(labels[:stop]))
            for rest in split_words(labels[stop:])
        )

    def one_pool(pool):
        return {
            " ".join(words)
            for _, cells, keys in pool
            for key in keys
            for labels in product(*(
                runes[(search.grid[cell] - key[i % 3]) % 29].split("/")
                for i, cell in enumerate(cells)
            ))
            for words in split_words(labels)
        }

    return [one_pool(pool) for pool in pools]


def main(repo, dictionary):
    r24 = load_report24(repo)
    r23 = r24.load_report23(repo)
    r22 = r23.load_report22(repo)
    r21 = r22.load_report21(repo)
    search = r21.Search(repo)
    route = r21.verify_route(search)
    _, _, after21, _, _ = r21.verify_pools(search, route)

    def passes23(current, candidate):
        return (r23.observed(candidate[0], search.rot, search.mu)
                == r23.forecast(*current[:2], search.rot, search.mu))

    def passes24(current, candidate):
        return (r24.observed(*candidate[:2], search.rot)
                == r24.forecast(*current[:2], search.rot, search.mu))

    before = [
        [e for e in pool
         if r22.passes_report22(*e[:2])
         and passes23(block, e)
         and passes24(block, e)]
        for block, pool in zip(route, after21)
    ]
    after = [
        [e for e in pool if passes25(block, e)]
        for block, pool in zip(route, before)
    ]
    assert len(before) == len(after) == 38
    assert all(r21.contains_block(pool, recorded)
               for pool, recorded in zip(after, route[1:]))
    assert (sum(map(len, before)), sum(map(len, after))) == (4125, 2960)

    def at_recorded_lengths(pools):
        return sum(
            len([e for e in pool if len(e[1]) == len(route[i + 1][1])])
            for i, pool in enumerate(pools)
        )

    assert (at_recorded_lengths(before), at_recorded_lengths(after)) == (715, 523)
    assert sum(len(a) > len(b) for a, b in zip(before, after)) == 10
    print("Recorded transitions: 38/38")
    print("Geometries: 4,125 -> 2,960; fixed length: 715 -> 523")

    tight = []
    for i, (current, recorded) in enumerate(zip(route, route[1:]), 1):
        node, ciphertext = current
        next_beginning = recorded[1][0]
        z, b = max(node), ciphertext[0]
        dc = abs(next_beginning[1] - (28 - z[1]))
        dr = abs(next_beginning[0] - (28 - b[0]))
        assert dc - dr <= 7
        if dc - dr == 7:
            tight.append((i, dc, dr))
    assert tight == [(21, 17, 10), (23, 14, 7), (26, 9, 2)]
    print("Exact boundary cases (current block, dc, dr):", tight)

    if dictionary is not None:
        dll, handle = load_hunspell(dictionary)
        try:
            old = reading_sets(search, before, dll, handle)
            new = reading_sets(search, after, dll, handle)
            assert (sum(map(len, old)), sum(map(len, new))) == (857, 600)
            assert (len(old[22]), len(new[22])) == (181, 36)
            assert (len(old[29]), len(new[29])) == (117, 45)
            assert (len(old[36]), len(new[36])) == (127, 126)
            assert new[-1] == {"DIE", "A YR", "AS AE", "DO AE", "WINGING"}
            fixed_old = [
                [e for e in pool if len(e[1]) == len(route[i + 1][1])]
                for i, pool in enumerate(before)
            ]
            fixed_new = [
                [e for e in pool if len(e[1]) == len(route[i + 1][1])]
                for i, pool in enumerate(after)
            ]
            assert (sum(map(len, reading_sets(search, fixed_old, dll, handle))),
                    sum(map(len, reading_sets(search, fixed_new, dll, handle)))) == (333, 252)
            print("Hunspell readings: 857 -> 600; fixed length: 333 -> 252")
            print("After TO #23: 181 -> 36; after BE #30: 117 -> 45")
        finally:
            dll.Hunspell_destroy(handle)


if __name__ == "__main__":
    parser = ArgumentParser(description="Reproduce Report 25")
    parser.add_argument("repo", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--dictionary", type=Path, default=None)
    args = parser.parse_args()
    main(args.repo, args.dictionary)
```
