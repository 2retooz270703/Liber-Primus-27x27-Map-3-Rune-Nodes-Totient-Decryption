# Candidate Report 23 — A seven-step ray bound between the key and the ciphertext

On the 27 × 27 body map, the complete line between the two outer key cells and the ciphertext satisfy the same geometric bound in **all 39 recorded blocks**. Applying the bound after Report 22 removes **1,755 of 9,369** candidate geometries across the 38 incoming transitions. A separate convention for selecting one aligned key per surviving geometry reproduces the documented rune sequences in **39 of 39** blocks.

The replay uses the body map and Reports 00–22. The red heading uses a separate key construction. The 3301 checks in the archive apply to a particular ending.

## 1. Proposed Rule 23

Sort the three physical source cells by row, then column. Write them as $U,M,Z$. Let $H(K)$ contain **every grid cell** from $U$ through $M$ to $Z$, at unit spacing along the source axis. Only the three original runes supply key values. The intermediate cells appear in the geometric test. Let $C$ contain every cell actually read for the candidate ciphertext.

For two cells let $u=|r_X-r_Y|$ and $v=|c_X-c_Y|$. Use the eight-ray offset already defined in Reports 06 and 12.

$$
d_8(X,Y)=\min(u,v,|u-v|),\qquad
Q(K,C)=\max_{X\in H(K),\,Y\in C}d_8(X,Y).
$$

**Accept the candidate when $Q(K,C)\le 7$.** Each pair of cells may satisfy the bound using a different row, column or diagonal direction. A single pair with offset eight is enough to reject a geometry. The number seven measures the ray offset. The search admits ciphertexts up to 27 runes, and at least one 27-rune candidate survives.

Reports 06 and 12 use $d_8$ to connect the previous ciphertext's leftmost cell to the next beginning. Report 22 checks whether a single original key cell can reach two anchors under a column condition. The proposed rule uses all pairs of cells in the candidate's own key span and ciphertext. It applies even when Report 22's column condition is inactive. [Report 06](./06-predicting-next-ciphertext-ray-and-mobius-deviation.md) · [Report 12](./12-predicting-exact-ray-deviation.md) · [Report 22](./22-seven-step-key-cell-coverage.md)

### SEE → YOU versus FOX

After **SEE (14)**, an alternative that passes Report 22 decrypts to **FOX**. Its physical key cells are $(11,4),(18,4),(25,4)$. Its ciphertext is $(21,20),(22,19),(23,18)$. Testing only those three key cells gives a maximum offset of **6**. The intermediate cell $(13,4)$ and the first ciphertext cell $(21,20)$ give displacements 8 and 16, so their ray offset is **8**. Rule 23 rejects FOX. The recorded **YOU (15)** has $Q=2$. [SEE](../plaintext-i-found/14-see.md) · [YOU](../plaintext-i-found/15-YOU.md)

**DIE** reaches the bound exactly. Its key center $(18,14)$ and first ciphertext cell $(3,22)$ give $d_8=\min(15,8,7)=7$. The maximum over the complete placement is 7. The six recorded successors on this boundary are **END (11), DEATH (13), THE (24), YOU (34), DO (36)** and **DIE (39)**. A limit of six removes all six. Raising the limit to eight admits 8,447 geometries across the 38 pools. [DIE](../plaintext-i-found/39-DIE.md)

## 2. Measured reduction

Each pool starts from one recorded block and its incoming phase state. One geometry means one physical source node paired with one ordered ciphertext segment. An assignment additionally specifies one numerically distinct aligned key. Each new search restarts from its recorded prefix.

| Search scope | Geometries after 22 | Geometries with 23 | Aligned-key assignments after 22 | Assignments with geometric Rule 23 | Assignments with both findings |
|---|---:|---:|---:|---:|---:|
| All eligible lengths, 38 transitions | 9,369 | **7,614** | 23,150 | 18,739 | **7,614** |
| Actual successor length supplied at each transition | 1,564 | **1,319** | 3,902 | 3,261 | **1,319** |
| Lengths two through seven, as a sensitivity check | 5,935 | **4,953** | 14,302 | 11,867 | **4,953** |
| After I ASK, all eligible lengths | 138 | **115** | 348 | 284 | **115** |
| After I ASK, three runes | 96 | **78** | 240 | 186 | **78** |

The geometric rule reduces the pool at **28 of 38** states. Across all lengths it removes **18.73%** of the summed geometries, or **15.03%** when each state receives equal weight. With the recorded lengths supplied, the corresponding figures are **15.66%** and **13.34%**. The seed block crosses the row boundary. Its test uses the actual seven recorded cells.

## 3. A deterministic choice of aligned key on a fixed placement

The current ciphertext and carried state determine the next signature in Reports 01 and 11. Write it as $(a,s,a)$. If $p$ is the predicted phase, $s$ is the representative of $p-2a \pmod 3$ in $\{-1,0,1\}$. For a proposed original center rune $h$, the derived center must be either $t=h$ or $t=\varphi(h)$ and must satisfy $\mu(\varphi(t))=s$. Reversing the outer values preserves the signature. The existing transition filters therefore leave some center and source-order decisions open. [Report 00](./00-decryption-method.md) · [Report 01](./01-next-key-signature.md) · [Report 11](./11-seven-thresholds-and-cyclic-phase-modes.md)

1. Sort the source coordinates by row and column. Call their **original** rune indices $u,h,z$. Read in this order. If $u=h\ne z$, read in reverse, starting at the outer rune different from the center.
2. Check the full predicted signature for both allowed center choices. Discard the node if neither fits. If exactly one distinct center survives, use it. If both survive, use $h$ when the three original indices are all distinct, and $\varphi(h)$ when any original index repeats.
3. Rotate the resulting triple left by $p$, repeat it, and subtract it modulo 29 as in Report 00.

The rule takes the forecast and the raw node as inputs. The documented plaintext supplies the comparison only after the key has been chosen. With both choices initially allowed, the 39 recorded placements admit **74** aligned keys in total. **23** placements admit more than one. Selecting a single key per placement reproduces all **39 documented rune sequences**, including the seed checked with its given signature. The route uses **36 distinct physical nodes**.

Both center values were admissible on **13** blocks. The plaintext distinguishes them on **12**. On **AS (37)**, the differing third aligned component is unused, so either operation yields the same text. The convention selects the direct key documented in the main walkthrough. Of **16** non-mirror blocks, **15** use the sorted order. The only observed reversal is **DO (36)**, whose sorted raw indices are $(25,25,5)$. Starting with the distinct 5 and transforming the repeated 25 gives $(5,20,25)$ at phase zero. [DO](../plaintext-i-found/36-do.md) · [AS](../plaintext-i-found/37-as.md)

Reading in sorted coordinate order, using the only compatible center when forced, and preferring the totient only for equal outer runes already recovers **38/39** recorded blocks. DO is the single observation distinguishing the expanded convention. A new admissible non-mirror node whose first two sorted runes coincide would directly test that provision.

### How the two findings distinguish readings after I ASK

| Reading under Reports 00–22 | Key center | Ciphertext start → end | $Q$ | Reading under the key convention |
|---|---|---|---:|---|
| DIE | (18,14) | (3,22) → (5,24) | 7 | **DIE** |
| SLY | (6,18) | (3,22) → (5,24) | 3 | **SJG** |
| SOY | (2,22) | (3,22) → (1,24) | 1 | **SOY** |
| DEAF | (12,20) | (7,18) → (9,20) | 2 | **DEAF** |

All four geometries pass the ray bound. The **DIE** node has three distinct raw indices $(5,23,27)$. Both center operations fit the forecast, so the convention keeps 23. The aligned key $(23,27,5)$ decrypts ciphertext $(17,8,23)$ to $(23,10,18)$, or **D·I·E**. At the **SLY** node, the center operation is forced. Its physical order is **B–G–Y**. The reverse order produced SLY. The sorted order gives the aligned key $(2,26,17)$, hence **S·J·G**. The alternatives **SOY** and **DEAF** keep their respective readings and also have no geometric successor even through Report 20. An empty outgoing pool by itself therefore leaves several possible endpoints.

## 4. Validation and search controls

With the limit fixed at seven, a chronological replay compared **1,008** local geometric tests. The full-span bound tied for first on the first **17** and **24** transitions with a version that used only the two ciphertext endpoints. On the first **28**, the full-span, all-cells version ranked first on its own by mean removal at the actual successor lengths. It then passed the remaining **10/10**. The construction and this retrospective replay use the same recorded route.

The control sampled one geometry uniformly and independently from each of the 38 post-22 pools at the actual successor length. It counted a trial when *any* tested formula passed all 38 sampled geometries and removed at least the observed **13.34%** on average. The family used six key subsets, six ciphertext subsets, seven distance measures, and four ways of reducing their pairwise scores. The code below specifies all choices. The adjustable-limit search includes each integer from 0 through 26.

| Search performed on each random sample | Trials meeting both criteria |
|---|---:|
| 1,008 formulas, limit fixed at 7 | **46 / 20,000 (0.23%)** |
| Same formulas, limit also selected | **911 / 20,000 (4.56%)** |

These frequencies apply to this geometric search family and its uniform, length-conditioned null model. Earlier route selection, the derivation of Reports 00–22, other exploratory families, and English-word selection fall outside this null model. The key convention was inferred separately from the same walkthroughs. A prospective test would freeze both formulas before choosing the next independent placements.

### Word check

As an additional measurement, a fixed English word list was used to implement the segmentation step of Report 16. This counts geometries with at least one complete spelling, including multiword parses. Grammar and meaning require a separate assessment. [Report 16](./16-whole-word-block-boundaries.md)

| Geometries with a complete word-list parse | Reports through 22 | Add the ray bound alone | Add the key convention alone | Apply both |
|---|---:|---:|---:|---:|
| Sum across 38 transitions, all lengths | 1,535 | 1,274 | 813 | **667** |
| After I ASK, all lengths | 33 | 28 | 14 | **13** |

The word list contains **112,794** spellings obtained from lowercase alphabetic headwords of the tested US English Hunspell file and its compatible affixes, plus single-letter A and I. It admits some abbreviations and dialect words. Rune aliases follow the labels in Report 20, and word boundaries fall between runes. Both geometric and aligned-key totals above are independent of this dictionary. The two input file SHA-256 values are `829a043cf078d1e80e886289a13823454977f442a239a859d2133ea61944aa60` for en_US.dic and `70fe5778717d097ce2f3326baaa5c1e4d2206d81a5a81d3ea8e11c4770806dd5` for en_US.aff.

## 5. Per-transition audit

<details>
<summary>All 38 local searches from their recorded current states</summary>

| Current → recorded successor | All geometries, 22 → 23 | Actual length, 22 → 23 | Word-list geometries, 22 → both |
|---|---:|---:|---:|
| 01 AS I GO THE → WEATHER | 3 → 3 | 1 → 1 | 1 → 1 |
| 02 WEATHER → TURNS | 201 → 171 | 22 → 17 | 22 → 6 |
| 03 TURNS → COLD | 18 → 14 | 8 → 7 | 6 → 4 |
| 04 COLD → I MAY | 17 → 9 | 3 → 2 | 1 → 1 |
| 05 I MAY → CRY | 3 → 3 | 1 → 1 | 1 → 1 |
| 06 CRY → NOW THE | 20 → 19 | 3 → 2 | 3 → 3 |
| 07 NOW THE → IDEA | 24 → 24 | 4 → 4 | 7 → 6 |
| 08 IDEA → OF | 113 → 100 | 13 → 12 | 5 → 2 |
| 09 OF → THE | 46 → 43 | 20 → 20 | 10 → 9 |
| 10 THE → END | 4 → 4 | 2 → 2 | 1 → 1 |
| 11 END → IS | 43 → 43 | 12 → 12 | 8 → 8 |
| 12 IS → DEATH | 20 → 20 | 5 → 5 | 10 → 9 |
| 13 DEATH → SEE | 62 → 59 | 30 → 30 | 4 → 4 |
| 14 SEE → YOU | 80 → 74 | 18 → 16 | 12 → 11 |
| 15 YOU → SOON | 1,246 → 1,151 | 57 → 50 | 126 → 58 |
| 16 SOON → THEN | 8 → 2 | 4 → 1 | 2 → 2 |
| 17 THEN → THE | 19 → 19 | 9 → 9 | 5 → 5 |
| 18 THE → KEY | 6 → 6 | 2 → 2 | 3 → 3 |
| 19 KEY → IS | 37 → 35 | 5 → 4 | 3 → 3 |
| 20 IS → TO | 16 → 11 | 10 → 7 | 4 → 3 |
| 21 TO → GO | 81 → 59 | 8 → 5 | 13 → 3 |
| 22 GO → TO | 1 → 1 | 1 → 1 | 1 → 1 |
| 23 TO → THE | 1,134 → 827 | 210 → 187 | 235 → 101 |
| 24 THE → EAST | 627 → 365 | 134 → 85 | 129 → 44 |
| 25 EAST → OF | 40 → 30 | 5 → 4 | 5 → 2 |
| 26 OF → THE | 814 → 560 | 62 → 46 | 97 → 33 |
| 27 THE → MAP LIFE | 517 → 413 | 95 → 85 | 47 → 20 |
| 28 MAP LIFE → MAY | 1,007 → 873 | 42 → 42 | 90 → 40 |
| 29 MAY → BE | 38 → 33 | 21 → 19 | 13 → 8 |
| 30 BE → THE | 732 → 679 | 128 → 121 | 181 → 75 |
| 31 THE → DEATH | 153 → 145 | 21 → 19 | 26 → 15 |
| 32 DEATH → OF | 237 → 223 | 93 → 86 | 63 → 27 |
| 33 OF → YOU | 39 → 39 | 15 → 15 | 4 → 4 |
| 34 YOU → GO | 15 → 9 | 2 → 2 | 1 → 1 |
| 35 GO → DO | 354 → 330 | 31 → 26 | 41 → 14 |
| 36 DO → AS | 90 → 65 | 35 → 28 | 30 → 14 |
| 37 AS → I ASK | 1,366 → 1,038 | 336 → 266 | 292 → 112 |
| 38 I ASK → DIE | 138 → 115 | 96 → 78 | 33 → 13 |

</details>

## 6. Reproduction

Save the Python block as `verify_report23.py` in the root of the unpacked project. The core replay uses Python 3.9+ and the archive’s own Reports 21 and 22. It reads the matrix, reconstructs the candidate pools and compares the chosen keys’ plaintext rune by rune with the 39 walkthroughs. The optional word counts use the dictionary pair specified above. The random control uses NumPy and seed 2307.

```bash
python3 verify_report23.py .
python3 verify_report23.py . --lexicon /usr/share/hunspell/en_US --controls 20000
```

The attached snapshot’s ZIP SHA-256 is `6c8e403ab1f5d9ca7da3b318fcdc87a1d0678729e4b57d4e0adfd090ad10bc20`. The map HTML SHA-256 is `5d783abb3594c916b3eb16088fa92be03aed8eda526d419745d22f325fc02d8f`.

<details>
<summary>Verification script</summary>

```python
import argparse
import hashlib
import re
from functools import lru_cache
from pathlib import Path
from types import ModuleType


def report(repo, number):
    path, = (repo / "Start-reading-here").glob(f"{number:02d}-*.md")
    code = re.search(r"```python[ \t]*\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S)
    module = ModuleType(f"_local_report_{number}")
    exec(compile(code[1], str(path), "exec"), vars(module))
    return module


@lru_cache(None)
def key_span(node):
    upper, middle, lower = sorted(node)
    dr, dc = middle[0] - upper[0], middle[1] - upper[1]
    radius = max(abs(dr), abs(dc))
    dr, dc = dr // radius, dc // radius
    return tuple((upper[0] + j * dr, upper[1] + j * dc)
                 for j in range(2 * radius + 1))


def ray_offset(x, y):
    dr = abs(x[0] - y[0])
    dc = abs(x[1] - y[1])
    return min(dr, dc, abs(dr - dc))


def score(node, cipher):
    return max(ray_offset(x, y) for x in key_span(node) for y in cipher)


def selected_key(search, node, signature):
    upper, center, lower = sorted(node)
    u, h, z = (search.grid[cell] for cell in (upper, center, lower))
    if u == h and z != h:
        u, z = z, u
    transformed = search.phi(h)
    options = (h, transformed) if len({u, h, z}) == 3 else (transformed, h)
    phase = sum(signature) % 3
    for middle in options:
        key = (u, middle, z)
        if tuple(search.mu(search.phi(k)) for k in key) == signature:
            return key[phase:] + key[:phase]
    return None


def target_signature(state):
    _, outer, phase = state
    return outer, (phase - 2 * outer + 1) % 3 - 1, outer


def plaintext(grid, cells, key):
    return tuple((grid[cell] - key[i % 3]) % 29 for i, cell in enumerate(cells))


def canonical(search, seq):
    return "".join(search.report[20].RUNES[k].split("/")[0] for k in seq)


def walkthrough_target(path, search, length):
    labels = search.report[20].RUNES
    aliases = {alias: i for i, label in enumerate(labels)
               for alias in [label, *label.split("/")]}
    expected = path.stem[3:].replace("-", "").upper().translate(str.maketrans("KVZ", "CUS"))
    sequences = set()
    for fragment in re.findall(r"`([^`\n]*·[^`\n]*)`", path.read_text(encoding="utf-8")):
        tokens = [value.strip() for value in fragment.split("·")]
        if len(tokens) == length and all(t in aliases for t in tokens):
            seq = tuple(aliases[t] for t in tokens)
            if canonical(search, seq) == expected:
                sequences.add(seq)
    if len(sequences) != 1:
        raise ValueError(f"Expected one documented rune sequence in {path.name}: {sequences}")
    return sequences.pop()


def aligned_keys(search, node, signature):
    raw = tuple(search.grid[cell] for cell in sorted(node))
    phase = sum(signature) % 3
    keys = set()
    for a, h, z in (raw, raw[::-1]):
        for middle in {h, search.phi(h)}:
            key = (a, middle, z)
            if tuple(search.mu(search.phi(k)) for k in key) == signature:
                keys.add(key[phase:] + key[:phase])
    return keys


def lexical_checker(base, labels):
    aff = base.with_suffix(".aff")
    dic = base.with_suffix(".dic")
    for source in (dic, aff):
        print(source.name, hashlib.sha256(source.read_bytes()).hexdigest())
    pairs, cross = {}, {}
    for row in aff.read_text(encoding="utf-8").splitlines():
        fields = row.split()
        if not fields or fields[0] not in ("PFX", "SFX"):
            continue
        if len(fields) == 4:
            cross[fields[1]] = fields[2] == "Y"
        elif len(fields) == 5:
            kind, flag, strip, added, pattern = fields
            regex = "^" + pattern if kind == "PFX" else pattern + "$"
            pairs.setdefault(flag, []).append((kind, strip, added, re.compile(regex)))
    words = {"A", "I"}
    for row in dic.read_text(encoding="utf-8").splitlines()[1:]:
        word, _, flags = row.partition("/")
        if not re.fullmatch("[a-z]+", word):
            continue
        prefixes, suffixes = [("", True)], {(word, True)}
        for flag in flags:
            for kind, strip, added, regex in pairs.get(flag, ()):
                if not regex.search(word) or "'" in added:
                    continue
                if kind == "PFX":
                    assert strip == "0"
                    prefixes.append((added, cross[flag]))
                elif strip == "0" or word.endswith(strip):
                    stem = word if strip == "0" else word[:-len(strip)]
                    suffixes.add((stem + added, cross[flag]))
        for prefix, pc in prefixes:
            for form, sc in suffixes:
                if prefix and form != word and not (pc and sc):
                    continue
                if len(prefix + form) >= 2:
                    words.add((prefix + form).upper())
    print("Lexicon entries", len(words))
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node[None] = True

    @lru_cache(None)
    def readable(seq):
        frontier, complete = [trie], False
        for rune in seq:
            next_nodes, complete = [], False
            for start in frontier:
                for spelling in labels[rune].split("/"):
                    node = start
                    for char in spelling:
                        node = node.get(char)
                        if node is None:
                            break
                    if node is not None:
                        next_nodes.append(node)
                        complete |= None in node
            if not next_nodes:
                return False
            if complete:
                next_nodes.append(trie)
            frontier = next_nodes
        return complete
    return readable


def replay(repo, lexicon=None):
    r21, r22 = report(repo, 21), report(repo, 22)
    search = r21.Search(repo)
    route = r21.verify_route(search)
    states, _, p21, _, _ = r21.verify_pools(search, route)
    pools = [[entry for entry in pool if r22.passes_report22(*entry[:2])] for pool in p21]
    walkthroughs = sorted((repo / "plaintext-i-found").glob("[0-9][0-9]-*.md"))[:39]
    assert len(walkthroughs) == len(route) == 39
    old_key_count = ambiguous_keys = two_centers = nonmirror = reversals = 0
    observable_center_choices = 0
    for path, state, (node, cipher) in zip(walkthroughs, states, route):
        expected = walkthrough_target(path, search, len(cipher))
        sig = target_signature(state)
        keys = aligned_keys(search, node, sig)
        key = selected_key(search, node, sig)
        assert key in keys and plaintext(search.grid, cipher, key) == expected
        old_key_count += len(keys)
        ambiguous_keys += len(keys) > 1
        mid = (1 - state[2]) % 3
        centers = {k[mid] for k in keys}
        two_centers += len(centers) > 1
        matching = {k[mid] for k in keys if plaintext(search.grid, cipher, k) == expected}
        observable_center_choices += len(centers) > 1 and len(matching) == 1
        a, h, z = (search.grid[cell] for cell in sorted(node))
        nonmirror += a != z
        reversals += a == h and h != z
    assert (old_key_count, ambiguous_keys, two_centers, observable_center_choices,
            nonmirror, reversals) == (74, 23, 13, 12, 16, 1)
    tight = [i for i, (node, c) in enumerate(route, 1) if score(node, c) == 7]
    assert tight == [11, 13, 24, 34, 36, 39]
    assert max(score(*block) for block in route) == 7
    read = lexical_checker(lexicon, search.report[20].RUNES) if lexicon else None
    stats, rows, final_words, example = {}, [], {}, None
    for i, pool in enumerate(pools):
        sig = target_signature(states[i+1])
        actual_node, actual_cipher = route[i+1]
        actual = (tuple(sorted(actual_node)), actual_cipher)
        assert any(e[:2] == actual for e in pool)
        by_band = {key: [0] * 5 for key in ("all", "given", "to7")}
        lex_counts = [0, 0, 0, 0]
        for node, cipher, keys in pool:
            key = selected_key(search, node, sig)
            assert key in keys
            q = score(node, cipher)
            passes = q <= 7
            for band in ["all"] + (["given"] if len(cipher) == len(actual_cipher) else []) + (["to7"] if len(cipher) <= 7 else []):
                tally = by_band[band]
                for j, value in enumerate((1, passes, len(keys), len(keys) if passes else 0, passes)):
                    tally[j] += value
            if read:
                old_lex = any(read(plaintext(search.grid, cipher, k)) for k in keys)
                new_lex = read(plaintext(search.grid, cipher, key))
                for j, value in enumerate((old_lex, passes and old_lex, new_lex, passes and new_lex)):
                    lex_counts[j] += value
            if i in (13, 37):
                readings = {canonical(search, plaintext(search.grid, cipher, k)) for k in keys}
                chosen = canonical(search, plaintext(search.grid, cipher, key))
                if i == 13 and "FOX" in readings:
                    example = node, cipher, q, max(ray_offset(x, y) for x in node for y in cipher)
                if i == 37 and readings & {"DIE", "SLY", "DEAF", "SOY"}:
                    final_words[chosen] = (q, node, cipher)
        for band, value in by_band.items():
            stats.setdefault(band, []).append(value)
        rows.append(lex_counts)
        print(f"{i+1:02}", *by_band["all"][:2], *by_band["given"][:2], *lex_counts)
    assert example[2:] == (8, 6)
    assert {k: x[0] for k, x in final_words.items()} == {"DIE":7,"SJG":3,"SOY":1,"DEAF":2}
    for w in ("DIE", "SOY", "DEAF"):
        _, node, cipher = final_words[w]
        assert next(search.successors((node, cipher), route[-2][1][0], states[-1]), None) is None
    for band, expected in (("all", (9369,7614,23150,18739,7614)),
                           ("given", (1564,1319,3902,3261,1319)),
                           ("to7", (5935,4953,14302,11867,4953))):
        totals = tuple(map(sum,zip(*stats[band])))
        print(band, totals)
        assert totals == expected, (band, totals)
    assert stats["all"][-1] == [138,115,348,284,115]
    assert stats["given"][-1] == [96,78,240,186,78]
    if read:
        print("Lexical totals", tuple(map(sum,zip(*rows))), "after I ASK", rows[-1])
    return pools, route


def controls(pools, route, trials):
    import numpy as np
    from itertools import product
    catalog, refs, boundaries = [], [], [0]
    for pool, (node, cipher) in zip(pools, route[1:]):
        fixed = [e for e in pool if len(e[1]) == len(cipher)]
        refs.append(len(catalog) + next(i for i,e in enumerate(fixed)
                                        if e[:2] == (tuple(sorted(node)),cipher)))
        catalog.extend(fixed)
        boundaries.append(len(catalog))
    names = list(product(("U","M","Z","outer","three","full"),
                         ("B","E","L","BE","BL","all"),
                         ("row","col","cheb","man","axis","diag","ray"),
                         ("min","max","shared","cover")))
    scores = np.empty((len(names),len(catalog)),dtype=np.int8)
    for j, (node, cipher, _) in enumerate(catalog):
        line = key_span(node)
        z, e = len(line)-1, len(cipher)-1
        l = min(range(e+1),key=lambda i: (cipher[i][1],-cipher[i][0]))
        source = [(0,), (z//2,), (z,), (0,z), (0,z//2,z), tuple(range(z+1))]
        targets = [(0,), (e,), (l,), (0,e), (0,l), tuple(range(e+1))]
        dr, dc = np.abs(np.array(line)[:,None,:] - np.array(cipher)[None,:,:]).transpose(2,0,1)
        delta, axis = np.abs(dr-dc), np.minimum(dr,dc)
        matrix = np.stack((dr,dc,np.maximum(dr,dc),dr+dc,axis,delta,np.minimum(axis,delta)))
        offset = 0
        for subset in source:
            for anchors in targets:
                sub = matrix[:,subset,:][:,:,anchors]
                mins, maxs = sub.min(axis=2), sub.max(axis=2)
                scores[offset:offset+28,j] = np.stack((mins.min(axis=1), maxs.max(axis=1),
                                                      maxs.min(axis=1), mins.max(axis=1)),axis=1).ravel()
                offset += 28
    spans = list(zip(boundaries,boundaries[1:]))
    def rate(reject, intervals):
        return sum(reject[:,lo:hi].mean(axis=1) for lo,hi in intervals) / len(intervals)
    selected = names.index(("full","all","ray","max"))
    cutoff = rate(scores[selected:selected+1] > 7, spans)[0]
    for n in (17,24,28):
        training = rate(scores > 7,spans[:n])
        valid = (scores[:,refs[:n]] <= 7).all(axis=1)
        best = np.flatnonzero(valid & (abs(training - training[valid].max()) < 1e-12))
        print("Training",n,[(names[i],int((scores[i,refs[n:]]>7).sum())) for i in best])
    for limits in ([7],range(27)):
        eligible = []
        for t in limits:
            reject = scores > t
            eligible.append(reject[rate(reject,spans)>=cutoff-1e-12])
        masks = np.unique(np.concatenate(eligible),axis=0)
        allowed_bits = [int.from_bytes(np.packbits(row,bitorder="little").tobytes(),"little")
                        for row in (~masks).T]
        rng = np.random.default_rng(2307)
        draws = np.stack([rng.integers(lo,hi,size=trials) for lo,hi in spans])
        hits = 0
        for sample in draws.T:
            possible = allowed_bits[sample[0]]
            for ix in sample[1:]:
                possible &= allowed_bits[ix]
                if not possible:
                    break
            hits += bool(possible)
        print("Thresholds",list(limits),"qualifying masks",len(masks),"hits",hits,"of",trials)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("repo",type=Path,nargs="?",default=Path("."))
    parser.add_argument("--lexicon",type=Path,help="Base path of the tested en_US.dic / en_US.aff pair")
    parser.add_argument("--controls",type=int,default=0,help="Run this many matched-length trials with NumPy")
    args = parser.parse_args()
    candidates, blocks = replay(args.repo,args.lexicon)
    if args.controls:
        controls(candidates,blocks,args.controls)
```

</details>
