# Report 27 — Key Alignment from Node Geometry

Rules 00–27 retain **38/38 recorded transitions**. The two clauses in this report reduce the number of local dictionary readings from **410 to 208** and admit **DIE** and **WINGING** after **I ASK**. In a replay from the recorded opening, two geometric routes stop at block 39. Each yields a sequence of **118 plaintext runes**, and they share their first 38 blocks. [Report 26](26-mod-seven-next-key-center-start-distance.md)

## 1. The two clauses

Use 1-based (row, column) coordinates on the 27 × 27 map. Order the three cells of the current original key node by row and then column, giving $U$, $M$, and $Z$. Thus $M$ is the center, and $U$ and $Z$ are the upper and lower extremes. For a horizontal node they are the left and right extremes. Let $B$ be the first ciphertext cell of the current block in reading order.

For a candidate successor, let $C_{\rm end}$ be the ordinary index of its last ciphertext rune. Let $K_1$ be the first rune index of its aligned key, and $K_{\rm end}$ the key rune index actually used at the last ciphertext position. With a three-rune key and ciphertext length $L$, $K_{\rm end}$ is component $1+((L-1)\bmod 3)$, counting from 1. Alignment and key repetition follow the standard decryption method. [Report 00](00-decryption-method.md)

### A. Final-position difference modulo three

Measure the distance from the current lower extreme $Z$ to the current ciphertext start $B$. Use Chebyshev distance, defined as the greater of the absolute row and column differences. The candidate must satisfy

$$
d_\infty(Z,B)\not\equiv 0\pmod 3
\quad\Longrightarrow\quad
|C_{\rm end}-K_{\rm end}|\not\equiv 1\pmod 3.
$$

The right-hand side uses the absolute difference of two ordinary rune indices. Take the remainder modulo 3 directly. This clause is active on **25/38** recorded transitions.

### B. GCD of the rotated extreme and the key center

Define the row-major address of a cell by $n_0(r,c)=27(r-1)+c$. Rotating a cell by 180° gives address $730-n_0(r,c)$. The candidate must satisfy

$$
\gcd(730-n_0(U),\,n_0(M))>1
\quad\Longrightarrow\quad
|K_1-C_{\rm end}|>7.
$$

This clause is active on **13/38** recorded transitions. **Evaluate both clauses on the same aligned key.** A geometry survives if it retains at least one alignment. Both checks can run before converting the candidate's decrypted runes to text.

## 2. What each clause resolves

### I ASK → DIE and WINGING

At block 38, $Z=(13,13)$ and $B=(5,17)$, so their Chebyshev distance is **8**. Clause A is active. The three rejected readings have a final-position difference of 4 and therefore remainder 1. **DIE** has remainder 0, and **WINGING** has remainder 2. [I ASK walkthrough](../plaintext-i-found/38-i-ask.md) · [DIE walkthrough](../plaintext-i-found/39-DIE.md)

| Reading with 00–26 | $C_{\rm end}$ | $K_{\rm end}$ | Absolute difference | Modulo 3 | Clause A |
| :--- | ---: | ---: | ---: | ---: | :--- |
| `A YR` | 9 | 5 | 4 | 1 | Reject |
| `AS AE` | 17 | 21 | 4 | 1 | Reject |
| `DO AE` | 23 | 27 | 4 | 1 | Reject |
| **`DIE`** | **23** | **5** | **18** | **0** | **Keep** |
| **`WINGING`** | **13** | **21** | **8** | **2** | **Keep** |

`DIE` and `DO AE` use the same key node and ciphertext segment. The last-position test distinguishes their aligned keys. Clause B is inactive at block 38 because $\gcd(447,310)=1$. `WINGING` uses the node `(16,14) → (16,16) → (16,18)`, the ordered ciphertext cells `(1,24), (2,25), (3,26)`, and aligned key indices `(2,5,21)`. Subtraction modulo 29 gives `(7,21,21)`, read as W·ING·ING.

### GO → DO

At block 35, $U=(3,16)$ and $M=(7,20)$ have row-major addresses 70 and 182. Their gate is $\gcd(730-70,182)=\gcd(660,182)=2$, so clause B is active. For the recorded successor geometry, the last ciphertext rune has index 23. [GO walkthrough](../plaintext-i-found/35-go.md) · [DO walkthrough](../plaintext-i-found/36-do.md)

| Reading on the recorded successor geometry | Aligned key | Absolute difference between $K_1$ and $C_{\rm end}$ | Clause B |
| :--- | :--- | ---: | :--- |
| **`DO`** | **(5, 20, 25)** | **18** | **Keep** |
| `OO` | (25, 20, 5) | 2 | Reject |

Clause A admits both alignments at this transition. Clause B resolves this alignment ambiguity on the shared prefix. Both terminal branches remain.

## 3. What remains after applying 00–27 together

For each local pool, the current block and its recorded phase history are fixed. All eligible successor lengths are considered. A geometry is an original key-node/ciphertext-segment pair. An alignment is one candidate key on that geometry. A reading is a distinct string in its transition pool after Hunspell en_US admission, single-rune transliteration alternatives (including NG and ING for ᛝ), and segmentation at rune boundaries. The table retains every dictionary reading, including abbreviations. [Report 16](16-whole-word-block-boundaries.md) · [Report 26](26-mod-seven-next-key-center-start-distance.md)

| Local successor pools | 00–26 | + A only | + B only | **00–27 (A and B)** |
| :--- | ---: | ---: | ---: | ---: |
| Geometries | 1,928 | 1,611 | 1,622 | **1,348** |
| Aligned-key assignments | 4,377 | 3,035 | 3,479 | **2,414** |
| Dictionary readings | 410 | 293 | 293 | **208** |
| Dictionary readings at recorded successor lengths | 178 | 138 | 116 | **92** |
| Transitions with a single reading | 6 | 8 | 8 | **10** |

Together the clauses eliminate **202 of 410 readings (49.3%)** and reduce the reading count at **23/38 transitions**. Requiring each candidate to permit up to three further geometrically and algebraically valid transitions reduces the pools further to **67 readings**, with single readings at **22/38** transitions. This optional lookahead tests candidate geometry and alignments before dictionary admission on the future hops. It checks the stopping condition when the lookahead reaches block 39.

### All surviving local readings

| Block | Recorded transition | 00–26 | 00–27 | Readings that pass 00–27 |
| ---: | :--- | ---: | ---: | :--- |
| 01 | AS I GO THE → WEATHER | 1 | 1 | `WEATHER` |
| 02 | WEATHER → TURNS | 10 | 9 | `A LL`, `AE I ME A`, `ALL`, `CA OOF FO`, `CM FO A YO`, `HI IV A`, `KA OOF FO`, `KM FO A YO`, `TURNS` |
| 03 | TURNS → COLD | 3 | 2 | `CO`, `COLD` |
| 04 | COLD → I MAY | 1 | 1 | `I MAY` |
| 05 | I MAY → CRY | 1 | 1 | `CRY` |
| 06 | CRY → NOW THE | 5 | 2 | `NOW THE`, `NOW THE PING` |
| 07 | NOW THE → IDEA | 3 | 3 | `ID EA`, `IDEA`, `NEAR` |
| 08 | IDEA → OF | 3 | 1 | `OF` |
| 09 | OF → THE | 8 | 4 | `BX`, `DE`, `LN`, `THE` |
| 10 | THE → END | 1 | 1 | `END` |
| 11 | END → IS | 3 | 2 | `I PI`, `IS` |
| 12 | IS → DEATH | 10 | 10 | `DEATH`, `FA`, `FA FO`, `FA VO`, `GO`, `JR`, `KEAS`, `LEA`, `NR`, `OD` |
| 13 | DEATH → SEE | 5 | 2 | `SEE`, `ZEE` |
| 14 | SEE → YOU | 7 | 5 | `CAW`, `CW`, `KW`, `YOU`, `YOUNG I` |
| 15 | YOU → SOON | 24 | 16 | `BD HEATH`, `DZ VB`, `HF`, `HF BE`, `HF BE MA`, `HF BEMA`, `HING`, `I AH`, `IX`, `JA`, `LB`, `LS`, `SO ON`, `SOON`, `ZOO`, `ZOON` |
| 16 | SOON → THEN | 2 | 2 | `THE`, `THEN` |
| 17 | THEN → THE | 2 | 2 | `HE`, `THE` |
| 18 | THE → KEY | 2 | 1 | `KEY` |
| 19 | KEY → IS | 2 | 2 | `IS`, `THINGS` |
| 20 | IS → TO | 3 | 1 | `TO` |
| 21 | TO → GO | 4 | 4 | `AD`, `AD PIG`, `AD PIG EA`, `GO` |
| 22 | GO → TO | 1 | 1 | `TO` |
| 23 | TO → THE | 33 | 9 | `BRIO`, `DE`, `DG`, `TEAK`, `THE`, `TING`, `TRIO`, `TYG`, `WEN` |
| 24 | THE → EAST | 2 | 2 | `EA ST`, `EAST` |
| 25 | EAST → OF | 3 | 3 | `OD`, `OD OP`, `OF` |
| 26 | OF → THE | 66 | 15 | `AE EA LX`, `BY`, `CD`, `CL`, `EX ANTE`, `GDS`, `GS`, `KL`, `PING`, `PL`, `RE`, `RE PUL`, `RE PUL ENG`, `THE`, `THE PEAL` |
| 27 | THE → MAP LIFE | 16 | 5 | `MAP LIFE`, `MIC`, `OHS`, `OHS RD`, `YOB` |
| 28 | MAP LIFE → MAY | 36 | 24 | `AE KB`, `AE SI CO FTH`, `AE SIC`, `BK`, `BUS GS ON AE EA COO`, `I AD`, `I AGIO`, `JAB`, `JAY`, `MAD`, `MAY`, `MAY WRY`, `PC`, `PG`, `PK`, `PS`, `RS`, `TB`, `TS`, `WAG`, `WAG A`, `WAY`, `WAY A`, `WK` |
| 29 | MAY → BE | 15 | 7 | `BE`, `EON`, `ES`, `HO`, `LING`, `LX`, `RING` |
| 30 | BE → THE | 36 | 16 | `AE CM`, `AE EM`, `AE KM`, `EA AE`, `EA AE A`, `EA YA`, `EAU`, `HAE GM TING`, `SH AE`, `THE`, `THING`, `THY`, `WK RE AE`, `YE`, `YE EH NR`, `ZINGY` |
| 31 | THE → DEATH | 16 | 14 | `BE`, `BIO`, `BL`, `DEATH`, `EA A AE CA`, `EA A AE KA`, `EA BIO KB`, `EA DING`, `EX`, `NO`, `OS`, `OZ`, `PD`, `TEL NO` |
| 32 | DEATH → OF | 33 | 10 | `A BI BIB`, `A BIB IB`, `AB I BIB`, `AB IB IB`, `AS`, `BL RING`, `GL YE`, `OB`, `OF`, `WE` |
| 33 | OF → YOU | 2 | 2 | `YO`, `YOU` |
| 34 | YOU → GO | 1 | 1 | `GO` |
| 35 | GO → DO | 4 | 1 | `DO` |
| 36 | DO → AS | 10 | 5 | `AS`, `EWE`, `HO`, `THO`, `THY MG FOES` |
| 37 | AS → I ASK | 31 | 19 | `AB`, `AL`, `EN`, `FF`, `HING`, `I A SC`, `I A SC EL JG`, `I A SC EL JG RT TA`, `I AN KEX JG`, `I ASK`, `I ASK EL JG`, `I ASK EL JG RT TA`, `KING`, `LB`, `PING`, `SH`, `SING`, `UH`, `ZING` |
| 38 | I ASK → DIE or WINGING | 5 | 2 | `DIE`, `WINGING` |
| 39 | DIE or WINGING → stop | 0 | 0 | — |
| | **Total** | **410** | **208** | |

## 4. Two complete routes

The full replay fixes the recorded opening block and starting state, then carries phase history and the previous ciphertext start along each branch. It allows the same candidate lengths and dictionary readings as the local pools. A 39-block route qualifies as stopped when block 39 has zero geometric successors under 00–25 before dictionary admission. The replay uses the 39-block horizon and the same stopping test in each row. [Opening block](../plaintext-i-found/01-as-i-go-the.md) · [Terminal test](../plaintext-i-found/40-why-die-is-the-final-word.md)

| Rules applied along each branch | Geometric routes reaching block 39 | Geometric routes stopping at block 39 | Distinct rune sequences on stopping routes |
| :--- | ---: | ---: | ---: |
| 00–26 | 8 | 6 | 42 |
| 00–26 + A | 2 | 2 | 4 |
| 00–26 + B | 4 | 3 | 8 |
| **00–27 (A and B)** | **2** | **2** | **2** |

After clause A, each terminal geometry has two rune sequences because block 36 can read `DO` or `OO`. Clause B leaves `DO` on the common prefix. The remaining terminal rune triples are **(23,10,18)**, read as **DIE**, and **(7,21,21)**, read as **WINGING**. Adding the terminal GP sums of **187** and **177** to the common prefix sum of **5,173** gives **5,360** and **5,350**. The DIE branch is transcribed here with the repository's punctuation.

> As I go, the weather turns cold.  
> I may cry now.
>
> The idea of the end is death.  
> See you soon, then.  
> The key is to go to the east of the map.
>
> Life may be the death of you.  
> Go, do as I ask.
>
> Die.

The full-route search uses the two clauses, dictionary admission, and the terminal test. It proceeds independently of the mirror-closure and GP-sum checks in earlier reports. The baseline rules are applied as specified, including the GP feature in Rule 14. The clauses in Rule 27 were fitted on the recorded transitions, so **38/38 measures retrospective retention**. The standalone decoder also checks the paired QU reading and uses its bundled English frequency lexicon. On the included matrix it reports 192 ranked English readings across the same two terminal geometries, with 96 on each. [Decoder](../README.md#experimental-python-decoder) · [Report 14](14-predicting-exact-next-key-axis.md)

## 5. Reproduce the results

Use the project revision containing this report and its companion reports. Copy the Python block to `verify_report27.py` in the repository root. The verifier uses Python 3.9+ and the embedded functions from Report 26. The dictionary argument is the prefix of the Hunspell en_US .aff and .dic files. The Hunspell shared library must also be available. The default run prints the complete table of local readings. Add both flags to replay the full routes and check the three-transition lookahead.

```bash
python3 verify_report27.py --dictionary /usr/share/hunspell/en_US --routes --lookahead
```

```python
from argparse import ArgumentParser
from collections import defaultdict
from functools import cache
from itertools import product
from math import gcd
from pathlib import Path
from types import ModuleType
import re
import sys


RECORDED = (
    "AS I GO THE", "WEATHER", "TURNS", "COLD", "I MAY", "CRY", "NOW THE",
    "IDEA", "OF", "THE", "END", "IS", "DEATH", "SEE", "YOU", "SOON", "THEN",
    "THE", "KEY", "IS", "TO", "GO", "TO", "THE", "EAST", "OF", "THE",
    "MAP LIFE", "MAY", "BE", "THE", "DEATH", "OF", "YOU", "GO", "DO",
    "AS", "I ASK", "DIE",
)


def load_report26(repo):
    path, = (repo / "Start-reading-here").glob("26-*.md")
    code = re.search(r"\x60{3}python[ \t]*\n(.*?)\n\x60{3}", path.read_text(encoding="utf-8"), re.S)[1]
    module = ModuleType("report27_dependency_26")
    sys.modules[module.__name__] = module
    exec(compile(code, str(path), "exec"), vars(module))
    return module


def address(cell):
    row, col = cell
    return 27 * (row - 1) + col


def gates(current):
    node, cells = current[:2]
    upper, center, lower = sorted(node)
    start = cells[0]
    distance = max(abs(lower[0] - start[0]), abs(lower[1] - start[1]))
    return distance % 3 != 0, gcd(730 - address(upper), address(center)) > 1


def accepts(grid, candidate, key, use_a, use_b):
    cells = candidate[1]
    last_cipher = grid[cells[-1]]
    last_key = key[(len(cells) - 1) % 3]
    return ((not use_a or abs(last_cipher - last_key) % 3 != 1)
            and (not use_b or abs(key[0] - last_cipher) > 7))


def filter_keys(grid, current, candidate, clauses):
    use_a, use_b = gates(current)
    use_a &= "A" in clauses
    use_b &= "B" in clauses
    node, cells, keys = candidate
    return node, cells, tuple(key for key in keys if accepts(grid, candidate, key, use_a, use_b))


def pool_readings(pool, readings):
    return set().union(*(readings(entry) for entry in pool))


def count_assignments(pools):
    return sum(len(entry[2]) for pool in pools for entry in pool)


def local_results(search, route, base, readings):
    results = {}
    for clauses in ("", "A", "B", "AB"):
        pools = [
            [entry for candidate in pool
             if (entry := filter_keys(search.grid, current, candidate, clauses))[2]]
            for current, pool in zip(route, base)
        ]
        words = [pool_readings(pool, readings) for pool in pools]
        fixed = [pool_readings(
            (entry for entry in pool if len(entry[1]) == len(following[1])), readings,
        ) for pool, following in zip(pools, route[1:])]
        # This post-search check compares the result with the recorded route.
        for i, (pool, following, expected) in enumerate(zip(pools, route[1:], RECORDED[1:]), 1):
            assert any(e[:2] == (tuple(sorted(following[0])), following[1])
                       and expected in readings(e) for e in pool), i
        results[clauses] = (pools, words)
        observed = (sum(map(len, pools)), count_assignments(pools), sum(map(len, words)),
                    sum(map(len, fixed)), sum(len(w) == 1 for w in words))
        expected = {
            "": (1928, 4377, 410, 178, 6),
            "A": (1611, 3035, 293, 138, 8),
            "B": (1622, 3479, 293, 116, 8),
            "AB": (1348, 2414, 208, 92, 10),
        }[clauses]
        assert observed == expected, (clauses, observed)
        print(f"{clauses or '00–26'}: {observed} "
              "(geometries, alignments, readings, fixed-length readings, single-reading pools)")
    assert results[""][1][-1] == results["B"][1][-1] == {
        "A YR", "AS AE", "DIE", "DO AE", "WINGING",
    }
    assert results["A"][1][-1] == results["AB"][1][-1] == {"DIE", "WINGING"}
    assert tuple(sum(flags) for flags in zip(*(gates(current) for current in route[:-1]))) == (25, 13)
    assert sum(a != b for a, b in zip(map(len, results[""][1]), map(len, results["AB"][1]))) == 23
    winging_node = ((16, 14), (16, 16), (16, 18))
    winging_cells = ((1, 24), (2, 25), (3, 26))
    winging_key = (2, 5, 21)
    assert search.grid[winging_cells[-1]] == 13
    assert any(
        (node, cells) == (winging_node, winging_cells)
        and winging_key in keys and "WINGING" in readings((node, cells, (winging_key,)))
        for node, cells, keys in results["AB"][0][-1]
    )
    print("38/38 recorded transitions retained by both clauses")
    return results


def transition_table(results, lookahead):
    baseline, combined = results[""][1], results["AB"][1]
    print("| Block | Recorded transition | 00–26 | 00–27 | Readings that pass 00–27 |")
    print("| ---: | :--- | ---: | ---: | :--- |")
    for i, (current, following, old, new) in enumerate(zip(RECORDED, RECORDED[1:], baseline, combined), 1):
        candidates = ", ".join(f"\x60{reading}\x60" for reading in sorted(new))
        label = following if i < 38 else "DIE or WINGING"
        print(f"| {i:02d} | {current} → {label} | {len(old)} | {len(new)} | {candidates} |")
    print("| 39 | DIE or WINGING → stop | 0 | 0 | — |")
    print(f"| | **Total** | **{sum(map(len, baseline))}** | **{sum(map(len, combined))}** | |")
    if lookahead is not None:
        print("Three-transition lookahead per pool:", list(map(len, lookahead)))


def main():
    parser = ArgumentParser()
    parser.add_argument("repo", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--dictionary", type=Path, default=Path("/usr/share/hunspell/en_US"))
    parser.add_argument("--routes", action="store_true")
    parser.add_argument("--lookahead", action="store_true")
    args = parser.parse_args()

    r26 = load_report26(args.repo)
    r25, r21, search, route, states, after21, keep25 = r26.reports(args.repo)
    base = [
        [e for e in keep25(current, pool) if r26.observed(e) == r26.forecast(current)]
        for current, pool in zip(route, after21)
    ]
    readings, decodings, indices, close = r26.decoder(r25, search, args.dictionary)

    @cache
    def next25(node, cells, prior_start, state):
        current = node, cells
        return tuple(keep25(current, search.successors(
            current, prior_start, state, use_report21=True,
        )))

    @cache
    def next_blocks(node, cells, prior_start, state, clauses):
        current = node, cells
        predicted = r26.forecast(current)
        return tuple(filtered for entry in next25(node, cells, prior_start, state)
                     if r26.observed(entry) == predicted
                     and (filtered := filter_keys(search.grid, current, entry, clauses))[2])

    def route_replay(clauses):
        opening = (*route[0], route[0][1][0], (0, 0, 0))
        frontier = {opening: [()]}
        for _ in range(38):
            following = defaultdict(list)
            for (node, cells, prior_start, state), histories in frontier.items():
                new_state = search.next_state(cells, state)
                for entry in next_blocks(node, cells, prior_start, state, clauses):
                    if readings(entry):
                        key = (*entry[:2], cells[0], new_state)
                        following[key].extend((*history, entry) for history in histories)
            frontier = following

        stopped = [path for state, paths in frontier.items() if not next25(*state) for path in paths]
        start_runes = indices(route[0][1], (25, 10, 28))
        rune_paths = {
            sequence for path in stopped
            for sequence in product((start_runes,), *(decodings(entry) for entry in path))
        }
        reached = sum(map(len, frontier.values()))
        geometries = {tuple(entry[:2] for entry in path) for path in stopped}
        print(f"Routes {clauses or '00–26'}: {reached} reach block 39, "
              f"{len(geometries)} stop there, {len(rune_paths)} distinct rune sequences")
        return reached, geometries, rune_paths

    @cache
    def viable(node, cells, prior_start, state, remaining, terminal):
        if remaining == 0:
            return not terminal or not next25(node, cells, prior_start, state)
        new_state = search.next_state(cells, state)
        return any(viable(e[0], e[1], cells[0], new_state, remaining - 1, terminal)
                   for e in next_blocks(node, cells, prior_start, state, "AB"))

    try:
        results = local_results(search, route, base, readings)
        ahead = None
        if args.lookahead:
            ahead = []
            for i, pool in enumerate(results["AB"][0]):
                until_end = 37 - i
                retained = [
                    e for e in pool if viable(e[0], e[1], route[i][1][0], states[i + 1],
                                              min(3, until_end), until_end <= 3)
                ]
                assert any(e[:2] == (tuple(sorted(route[i + 1][0])), route[i + 1][1])
                           and RECORDED[i + 1] in readings(e) for e in retained)
                ahead.append(pool_readings(retained, readings))
            assert sum(map(len, ahead)) == 67
            assert sum(len(w) == 1 for w in ahead) == 22
        assert not next25(*route[-1], route[-2][1][0], states[-1])
        transition_table(results, ahead)
        if args.routes:
            expected = {"": (8, 6, 42), "A": (2, 2, 4), "B": (4, 3, 8), "AB": (2, 2, 2)}
            for clauses, counts in expected.items():
                reached, geometries, rune_paths = route_replay(clauses)
                assert (reached, len(geometries), len(rune_paths)) == counts, clauses
            recorded = tuple((tuple(sorted(node)), cells) for node, cells in route[1:])
            assert recorded in geometries
            assert {geometry[:-1] for geometry in geometries} == {recorded[:-1]}
            assert {geometry[-1] for geometry in geometries} == {
                recorded[-1], (((16, 14), (16, 16), (16, 18)), ((1, 24), (2, 25), (3, 26))),
            }
            assert len({sequence[:-1] for sequence in rune_paths}) == 1
            assert {sequence[-1] for sequence in rune_paths} == {(23, 10, 18), (7, 21, 21)}
            assert all(len(seq) == 39 and sum(map(len, seq)) == 118 for seq in rune_paths)
            primes = search.report[14].GP_PRIMES
            assert {sum(primes[r] for block in seq for r in block) for seq in rune_paths} == {5350, 5360}
            print("Two 118-rune sequences share 38 blocks and end in DIE or WINGING.")
    finally:
        close()


if __name__ == "__main__":
    main()
```
