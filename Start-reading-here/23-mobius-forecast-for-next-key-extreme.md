# Report 23 — Möbius Forecast for the Next Key Extreme

Two tests on the current block predict whether the 180° index of the next key node's first geometric extreme has positive Möbius value. The filter preserves **all 38 recorded transitions** and reduces the pool after Report 22 from **9,369 to 5,997 geometries**. After I ASK, it keeps **DIE** and rejects **SLY** on the same ciphertext segment. [Report 22](22-seven-step-key-cell-coverage.md)

## 1. Acceptance test

Coordinates on the 27 × 27 matrix are 1-based. Let $B$ and $E$ be the first and last cells of the **current** ciphertext in reading order. Let $L$ be its leftmost cell, with the bottommost cell chosen in a tie. Let $M$ be the center of the current original key node. For a proposed next original key node, let $U'$ be the first cell in row–column order. This is the upper extreme, or the left extreme for a horizontal node. Reversing the key's read order leaves $U'$ unchanged. [Report 02](02-leftmost-cell-and-rotations.md)

For $X=(r,c)$, the rotated row-major indices used here are

$$
\begin{aligned}
n_{90}(X) &= 27(c-1)+28-r,\\
n_{180}(X) &= 730-\bigl(27(r-1)+c\bigr),\\
n_{270}(X) &= 730-n_{90}(X).
\end{aligned}
$$

Write $[P]$ for the indicator of a proposition, $\oplus$ for XOR, and $\mu$ for the Möbius function. Compute the two bits from the current block.

$$
\begin{aligned}
a &= \left[3 \mid \gcd\\left(n_{270}(B), n_{90}(L)\right)\right],\\
b &= \left[\mu\\left(n_{270}(M) + n_{270}(E)\right) > 0\right].
\end{aligned}
$$

Accept the proposed key extreme when its observed bit equals the XOR of these two bits.

$$
\boxed{\left[\mu\\left(n_{180}(U')\right) > 0\right] = a \oplus b}
$$

The first bit is equivalent to requiring both rotated indices to be divisible by three. Keep the sum in the second bit as an ordinary integer. A forecast of 1 requires $\mu=+1$ at $U'$. A forecast of 0 accepts either $\mu=-1$ or $\mu=0$. The forecast can be computed once per current block and applied to each candidate original node. The same transition state suffices for this additional test. [Report 00](00-decryption-method.md) · [Report 14](14-predicting-exact-next-key-axis.md) · [Report 20](20-two-orientation-gcd-filter.md)

## 2. I ASK → DIE versus SLY

For **I ASK**, $B=(5,17)$, $E=L=(8,17)$ and $M=(12,13)$. The two bits are zero:

$$
\begin{aligned}
\gcd(n_{270}(B),n_{90}(L)) &= \gcd(275,452)=1,\\
n_{270}(M)+n_{270}(E) &= 390+278=668=4\cdot167,\qquad\mu(668)=0.
\end{aligned}
$$

The forecast therefore accepts an extreme with a nonpositive Möbius value. All three examples below use the ordered ciphertext $(3,22)\to(4,23)\to(5,24)$. Each passes the incoming tests through Report 22. [I ASK (38)](../plaintext-i-found/38-i-ask.md) · [DIE (39)](../plaintext-i-found/39-DIE.md)

| Reading | Key center | Original extreme $U'$ | $n_{180}(U')$ | $\mu(n_{180}(U'))$ | Report 23 |
| :--- | :---: | :---: | ---: | ---: | :--- |
| **DIE** | (18,14) | (18,10) | $261=9\cdot29$ | 0 | Keep |
| **SLY** | (6,18) | (6,16) | $579=3\cdot193$ | +1 | Reject |
| **APP** | (26,6) | (26,2) | $53$ | −1 | Keep |

The retained **DIE** and **APP** placements both have next accumulated phase $S=33$ and zero outgoing geometric continuations under Reports 00–22. The filter therefore leaves two valid terminal readings even on this fixed segment and with the same phase and ending position in the route.

## 3. Route validation and selectivity

The enumeration starts each test at the recorded current block with its recorded transition history. A geometry is one physical original key node paired with one ordered ciphertext segment. Alternate compatible aligned keys within that geometry count once. The geometric counts precede the whole-word test and use all eligible lengths. The length-matched rows fix the recorded successor length separately in each pool. [Report 21](21-conditional-seven-step-bound.md) · [Report 22](22-seven-step-key-cell-coverage.md)

| Successor pool | After Report 22 | With Report 23 | Share removed |
| :--- | ---: | ---: | ---: |
| All eligible lengths across 38 transitions | 9,369 | **5,997** | **36.0%** |
| Recorded successor lengths across 38 transitions | 1,564 | **984** | **37.1%** |
| All eligible lengths after I ASK | 138 | **82** | **40.6%** |
| Three runes after I ASK | 96 | **54** | **43.8%** |

All **38/38** recorded placements pass. The forecast is positive on **9** transitions. With equal weight per transition, the mean geometric reduction is **23.17%** across all lengths and **21.97%** at recorded lengths.

As a separate whole-word check after I ASK, English Hunspell `en_US` accepts **52 → 28** distinct segmented readings. At rune boundaries the accepted outputs go from **22 → 12** single tokens and **30 → 16** multi-token readings. This check uses the rune alphabet’s single-rune transliteration alternatives, including both NG and ING for ᛝ. Distinct keys giving the same segmented output count once. The 12 surviving single tokens are **APP, DIE, OBOE, ROW, SEC, SINGS, SOY, SSH, TINGS, TOY, WINGING, ZINGS**. The dictionary includes abbreviations. Run the Report 24 verifier with `--dictionary` to check these counts. [Report 16](16-whole-word-block-boundaries.md) · [Report 24](24-mod-seven-key-center-ciphertext-alignment.md)

### One-block lookahead

For the 37 recorded intermediate transitions, require a proposed block to have at least one admissible successor. Enumerate all eligible lengths on both steps. With Reports 00–22, this reduces **9,231 → 3,506** geometries. Applying Report 23 to both steps further reduces this to **1,933**, preserving **37/37** recorded intermediate placements. Fixing the length of the first proposed block to the corresponding recorded length gives **1,468 → 627 → 357**.

## 4. Chronological replay and random controls

The forecast was selected retrospectively. The search examined **388** candidate output bits involving positions, distances, parity, and arithmetic properties of a proposed successor. The input family had **8,540** predicates of the current block and phase state before deduplication. It included bits of rotated indices, coordinate and distance predicates, and modular or Möbius predicates of sums, differences, XORs, or GCDs of rotated indices. Forecasts used one or two input predicates combined by XOR, with optional complementation.

For the specified positive Möbius bit at $U'$, fitting the first **24** transitions left **36** distinct predicted sequences over the recorded inputs. Fitting the first **28** left **one** predicted sequence within this family, which matched the remaining **10/10** observations. The target was identified using the full route.

In each random trial, draw one geometry independently and uniformly from each length-matched Report 22 pool. Search for a nonconstant forecast that matches all 38 draws and achieves at least the observed mean removal of **21.97%**. In the broader control, repeat the search across the candidate output bits as well.

| Scope of the repeated search | Trials matching both criteria |
| :--- | ---: |
| Fixed positive Möbius target at $U'$ | **31 / 12,000** (0.26%) |
| All tested targets | **1,823 / 12,000** (15.19%) |

These frequencies describe the tested families and candidate pools. The broader control captures the extra opportunity from choosing the output bit after looking at the route. Report 23 is an empirical filter. Prospective testing can hold the target and both input predicates fixed.

## 5. Reproduce the geometric results

Save the Python block as `verify_report23.py` and run it from the project root with Python 3.9 or later. It loads the first Python example from the trusted local Reports 22 and 21 to construct the baseline pools. The script verifies the 38 recorded transitions, the geometric counts, the I ASK examples, and the terminal checks for DIE and APP. The `--lookahead` argument verifies the two-step enumeration. Section 4 describes the separate search-family controls.

```bash
python3 verify_report23.py
python3 verify_report23.py --lookahead
```

```python
from argparse import ArgumentParser
from math import gcd
from pathlib import Path
from statistics import mean
from types import ModuleType
import re
import sys


def forecast(node, ciphertext, indices, mobius):
    _, center, _ = node
    beginning, end = ciphertext[0], ciphertext[-1]
    leftmost = min(ciphertext, key=lambda cell: (cell[1], -cell[0]))

    # The four slots are 0°, 90°, 180°, and 270°, in that order.
    shared_three = gcd(indices[beginning][3], indices[leftmost][1]) % 3 == 0
    positive_sum = mobius(indices[center][3] + indices[end][3]) > 0
    return shared_three ^ positive_sum


def observed(next_node, indices, mobius):
    upper = min(next_node)
    return mobius(indices[upper][2]) > 0


def load_report22(root):
    path, = (root / "Start-reading-here").glob("22-*.md")
    example = re.search(
        r"```python[ \t]*\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S
    )
    module = ModuleType("_report23_dependency_22")
    sys.modules[module.__name__] = module
    exec(compile(example[1], str(path), "exec"), vars(module))
    return module


def next_geometries(search, report22, entry, previous_beginning, state):
    for candidate in search.successors(
        entry[:2], previous_beginning, state, use_report21=True
    ):
        if report22.passes_report22(*candidate[:2]):
            yield candidate


def verify_route_counts(search, report21, report22, route, states, before, after, predicts):
    assert len(before) == len(after) == 38
    assert all(report21.contains_block(pool, block)
               for pool, block in zip(after, route[1:]))
    assert sum(predicts(block) for block in route[:-1]) == 9
    assert (sum(map(len, before)), sum(map(len, after))) == (9369, 5997)
    assert round(100 * mean(1 - len(new) / len(old)
                           for old, new in zip(before, after)), 2) == 23.17

    lengths = [len(block[1]) for block in route[1:]]
    matched_before = [sum(len(entry[1]) == n for entry in pool)
                      for n, pool in zip(lengths, before)]
    matched_after = [sum(len(entry[1]) == n for entry in pool)
                     for n, pool in zip(lengths, after)]
    assert (sum(matched_before), sum(matched_after)) == (1564, 984)
    assert round(100 * mean(1 - new / old
                           for old, new in zip(matched_before, matched_after)), 2) == 21.97
    print("38/38 transitions. All lengths: 9,369 -> 5,997. Matched: 1,564 -> 984.")

    assert (len(before[-1]), len(after[-1])) == (138, 82)
    assert (matched_before[-1], matched_after[-1]) == (96, 54)
    assert predicts(route[-2]) is False
    final_segment = route[-1][1]
    examples = [
        ("DIE", (18, 14), 261, 0, True),
        ("SLY", (6, 18), 579, 1, False),
        ("APP", (26, 6), 53, -1, True),
    ]
    assert states[-1][0] == 33
    for word, center, index, value, keep in examples:
        entry, = [
            e for e in before[-1]
            if e[0][1] == center and e[1] == final_segment and word in search.readings(e)
        ]
        assert search.rot[min(entry[0])][2] == index
        assert search.mu(index) == value
        assert (entry in after[-1]) == keep
        if keep:
            assert next(next_geometries(
                search, report22, entry, route[-2][1][0], states[-1]
            ), None) is None
    print("After I ASK: 138 -> 82. Three runes: 96 -> 54.")
    print("Fixed segment: DIE and APP survive and terminate. SLY is rejected.")


def verify_lookahead(search, report21, report22, route, states, before, predicts):
    counts = [0, 0, 0]
    matched = [0, 0, 0]
    for i, pool in enumerate(before[:-1]):
        current, recorded = route[i:i + 2]
        prediction = predicts(current)
        survivors = []
        for entry in pool:
            same_length = len(entry[1]) == len(recorded[1])
            counts[0] += 1
            matched[0] += same_length

            successors = next_geometries(search, report22, entry, current[1][0], states[i + 1])
            first = next(successors, None)
            if first is None:
                continue
            counts[1] += 1
            matched[1] += same_length

            if observed(entry[0], search.rot, search.mu) != prediction:
                continue
            next_prediction = predicts(entry[:2])
            if (observed(first[0], search.rot, search.mu) == next_prediction
                    or any(observed(candidate[0], search.rot, search.mu) == next_prediction
                           for candidate in successors)):
                counts[2] += 1
                matched[2] += same_length
                survivors.append(entry)
        assert report21.contains_block(survivors, recorded), i + 1
    assert counts == [9231, 3506, 1933]
    assert matched == [1468, 627, 357]
    print("Lookahead: 37/37 intermediate placements. 9,231 -> 3,506 -> 1,933.")
    print("Matched first-step length: 1,468 -> 627 -> 357.")


if __name__ == "__main__":
    parser = ArgumentParser(description="Verify Report 23 in a local project checkout.")
    parser.add_argument("repo", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--lookahead", action="store_true")
    args = parser.parse_args()

    report22 = load_report22(args.repo)
    report21 = report22.load_report21(args.repo)
    search = report21.Search(args.repo)
    route = report21.verify_route(search)
    states, _, after21, _, _ = report21.verify_pools(search, route)
    before = [[e for e in pool if report22.passes_report22(*e[:2])]
              for pool in after21]

    def predicts(block):
        return forecast(*block, search.rot, search.mu)

    after = []
    for current, pool in zip(route, before):
        prediction = predicts(current)
        after.append([e for e in pool if observed(e[0], search.rot, search.mu) == prediction])
    verify_route_counts(search, report21, report22, route, states, before, after, predicts)
    if args.lookahead:
        verify_lookahead(search, report21, report22, route, states, before, predicts)
```
