# 01 — The Red Heading: A Geometric `J–TH–TH` Key and the Candidate Plaintext `RATIO`

*Liber Primus LP2, pages 0–2 · 27×27 rune matrix · Research note dated 28 October 2026*

> **Status: reproducible candidate, not a confirmed Cicada 3301 decryption.**
> The second red-heading word decrypts exactly to `RATIO` under a key derived from
> two real, equally spaced three-rune nodes. One node has a striking geometric
> connection to the selected `MAP` endpoint and the route's opening `J(13,12)`.
> The first red-heading word remains unsolved, and this candidate does **not**
> satisfy every predictive condition for the next *sequential* block after `MAP`.

## 1. Research question and fixed input

The hypothesis under investigation is that the **red headings** of Liber Primus
may contain actual words encrypted linearly, using hidden keys recoverable from
the matrix's geometry, even if the larger body of black runes functions as a
nonlinear spatial construction rather than a single linearly decrypted stream.
This is a hypothesis about the cipher's organization, **not** an established
distinction between two proven encryption methods.

The red heading at the beginning of LP2 pages 0–2 is:

```text
ᛋᚻᛖᚩᚷᛗᛡᚠ • ᛋᚣᛖᛝᚳ
S–H–E–O–G–M–IA–F • S–Y–E–NG–C
```

It contains **13 runes** in two words of **8 and 5 runes**. The runes themselves
are included in the project's 729-rune transcription: they occupy exactly
**row 1, columns 1–13** of the 27×27 matrix. The word separator is excluded
from the matrix cells. This fixes the target ciphertext before selecting any
key and retains its original word boundary.

The second word, considered independently, is:

| Position | Rune | Transliteration | Gematria Primus index |
|---:|:---:|:---:|---:|
| 1 | ᛋ | S | 15 |
| 2 | ᚣ | Y | 26 |
| 3 | ᛖ | E | 18 |
| 4 | ᛝ | NG | 21 |
| 5 | ᚳ | C/K | 5 |
| **Total** | | **5 runes** | **85** |

All rune indices in this note are **0–28**, not Gematria Primus prime weights.
Coordinates are **1-based `(row,column)`**. The project's decryption equation is:

$$
P_i=(C_i-K_i)\bmod 29,
$$

where a three-rune key is repeated when the ciphertext block is longer than
three runes. Euler's totient is denoted by $\varphi$, and the Möbius function
by $\mu$.

## 2. The existing `MAP` geometry

The supplied project's **candidate block 28** decrypts the following selected
ciphertext diagonally upward and rightward:

| Role | Coordinate | Matrix rune |
|---|:---:|:---:|
| Beginning | (19,11) | R |
| Interior | (18,12) | C/K |
| Endpoint | **(17,13)** | **AE** |

Its original source node is the non-mirror `EO–X–I`, centered on **`X(16,9)`**.
The selected key is used without transforming this center, and phase 1 rotates
it to `X–I–EO`. The corresponding differences are `M–A–P`. These facts are
documented in the repository's `plaintext-i-found/28-map.md`.

Two **pre-existing, distinguished points** therefore enter the new geometric
observation:

- Original MAP-key center: **`X(16,9)`**.
- Final MAP-ciphertext cell: **`AE(17,13)`**.

From the first point to the second, the movement is **one row down and four
columns right**:

$$
\Delta=(17-16,\;13-9)=(+1,+4).
$$

**Repeat exactly the same movement once more from the endpoint**:

$$
(16,9)\xrightarrow{(+1,+4)}(17,13)
\xrightarrow{(+1,+4)}\boxed{(18,17)}.
$$

The matrix cell **`(18,17)` is `R`**. Equivalently, `AE(17,13)` is the exact
midpoint of the two points `(16,9)` and `(18,17)`. No rune was changed in
performing this geometric continuation.

## 3. The starting `J` fixes the entire new key node

The research route originally began from **`J(13,12)`**, the center of its
opening `AE–J–EA` source node. Using this established opening cell as one arm,
the newly reached **`R(18,17)`** as a center, and reflecting the opening arm
through that center gives the opposite arm:

$$
2(18,17)-(13,12)=(23,22).
$$

The matrix rune at `(23,22)` is **`TH`**.

| Source-node position | Coordinate | Rune | Displacement from center |
|---|:---:|:---:|:---:|
| First outer arm — original opening cell | **(13,12)** | **J** | (−5,−5) |
| **Center — one extension beyond MAP** | **(18,17)** | **R** | (0,0) |
| Second outer arm — fixed by reflection | **(23,22)** | **TH** | (+5,+5) |

Thus the original matrix contains the exact diagonal, equal-radius structure:

```text
J(13,12) ──(+5,+5)── R(18,17) ──(+5,+5)── TH(23,22)
```

This is a **non-mirror rune node**, because its outer symbols differ:
`J ≠ TH`. “Non-mirror” here refers to the equality of the outer *runes*;
its three **coordinates** are nevertheless perfectly symmetric.

The significant feature is not merely that some symmetric triple exists.
**The MAP center and endpoint determine the new center `R`, while the
independently recorded opening cell `J` determines the remaining arm.**

## 4. Derivation of the repeating key

Apply the project's familiar **center-only Euler totient transformation** to
the newly identified original node. The Gematria Primus index of `R` is `4`:

$$
\varphi(4)=2=\mathrm{TH}.
$$

The outer runes remain unchanged:

```text
J–R–TH  →  J–TH–TH
```

| Derived key element | Rune index | Totient of index | Möbius of totient |
|:---:|---:|---:|---:|
| J | 11 | $\varphi(11)=10$ | $\mu(10)=+1$ |
| TH | 2 | $\varphi(2)=1$ | $\mu(1)=+1$ |
| TH | 2 | $\varphi(2)=1$ | $\mu(1)=+1$ |

The derived key's full signature is **`(+1,+1,+1)`**, and its cyclic rotation
phase is:

$$
p=(1+1+1)\bmod3=0.
$$

**No rotation is needed.** For a five-rune target, repeat the three-rune key:

```text
Derived key:       J  TH TH
Aligned key:       J  TH TH
Five-rune stream:  J  TH TH J  TH
Index stream:     11   2  2 11   2
```

This is a key obtained from actual matrix cells using the project's documented
type of center transformation, signature, rotation, and modular subtraction.
It is **not** one of the 28 aligned key streams already consumed in the selected
plaintext path; it is an additional candidate source node.

## 5. Exact decryption of the second red-heading word

Apply the project's subtraction rule to the **five original red runes**, in
their existing left-to-right order, starting the derived key at its phase-0
position:

| # | Red ciphertext | Cipher index | Key | Key index | Difference mod 29 | Plaintext rune |
|---:|:---:|---:|:---:|---:|---:|:---:|
| 1 | S | 15 | J | 11 | 15 − 11 = 4 | **R** |
| 2 | Y | 26 | TH | 2 | 26 − 2 = 24 | **A** |
| 3 | E | 18 | TH | 2 | 18 − 2 = 16 | **T** |
| 4 | NG | 21 | J | 11 | 21 − 11 = 10 | **I** |
| 5 | C/K | 5 | TH | 2 | 5 − 2 = 3 | **O** |

```text
S–Y–E–NG–C  →  R–A–T–I–O  →  RATIO
```

**Candidate plaintext: `RATIO`.** Every subtraction is already nonnegative,
so none of these five differences even needs modulo wrapping. The index sums
provide a simple checksum:

$$
85-(11+2+2+11+2)=57.
$$

Here, **85** is the ciphertext index sum, **28** is the sum of the five
key indices, and **57** is the resulting plaintext index sum.

The five output indices are `(4,24,16,10,3)`, which decode unambiguously to
`R–A–T–I–O` in the project's 29-rune alphabet. `RATIO` is a recognizable
English/Latin word. **The calculation is exact; the claim that it was
intentionally encoded by Cicada is a separate, unproven interpretation.**

## 6. A second original matrix source for the identical key

A separate equally spaced node appears on the **first row, beyond the red
heading's thirteen cells**:

| Role | Coordinate | Rune |
|---|:---:|:---:|
| First outer | (1,19) | J |
| Center | (1,21) | O |
| Second outer | (1,23) | TH |

The arms lie two columns from the center. Since the rune index of `O` is `3`,

$$
\varphi(3)=2=\mathrm{TH}.
$$

```text
J–O–TH  →  J–TH–TH
```

This gives **the same derived key and the same `RATIO` arithmetic**.

The two source nodes are therefore:

1. `J(1,19)–O(1,21)–TH(1,23)` — horizontal, entirely in the first row after
   the heading.
2. `J(13,12)–R(18,17)–TH(23,22)` — diagonal, tied to the opening `J` and
   the one-step extension of the MAP-center-to-endpoint movement.

Both were verified against the project's 27×27 transcription. They are not
two *independent plaintext decodings*: they produce an identical key, which
is applied to an identical word. Their distinct **locations** are the added
geometric observation.

## 7. A finite selectivity test across all 28 documented stages

To check whether the MAP construction is merely a generic geometry that also
works everywhere, apply **one identical rule** to all 28 recorded stages:

1. Take the selected stage's **original key-node center** `M` and ciphertext
   **endpoint** `E`.
2. Extend that movement by exactly one more copy: `R′ = 2E − M`.
3. Keep the route's **fixed opening cell** `J = (13,12)` as one outer arm.
4. Reflect it through `R′` to get the second arm: `Z′ = 2R′ − J`.
5. Keep the candidate only if both points are inside the 27×27 matrix and
   `J–R′–Z′` is horizontal, vertical, or exactly 45° diagonal, with equal
   spacing.
6. Read the three actual runes, test their original and center-totient keys,
   compute their own phase, and apply the result to the same fixed five-rune
   red ciphertext `S–Y–E–NG–C`.

Using the recorded source centers and primary ciphertext endpoints, only
**two of the 28 stages** produce a valid three-cell geometry:

| Stage | Extended center | Opposite arm | Original source | Tested result |
|---|:---:|:---:|---|---|
| **06 — CRY** | (9,16), U | (5,20), Y | J–U–Y | `E–S–B–A–D` (phase 2) |
| **28 — MAP** | **(18,17), R** | **(23,22), TH** | **J–R–TH** | **`R–A–T–I–O`** (φ center, phase 0) |

The `CRY` key has signature `(+1,+1,0)`, rotates by phase 2 into `Y–J–U`,
and yields `ESBAD`. The MAP-derived node yields `RATIO` after transforming
its center and using phase 0.

**Interpretation:** under this *fixed geometric recipe and selected 28-stage
record*, MAP is the only stage that leads to a recognizable five-rune word.
That selectivity is worth investigating. However, the recipe itself was
noticed **after** searching for ways to decrypt the heading, so 1-out-of-28
is **not** a calibrated discovery probability or a proof of intent.

### How common is the key shape in the full matrix?

Enumerating horizontal, vertical, and the two 45° diagonal directions at all
possible integer radii gives **14,976** equally spaced, oriented three-cell
positions in a 27×27 matrix. Exactly **two** original nodes produce the
derived `J–TH–TH` via center-only totient: the `J–O–TH` and `J–R–TH` nodes
listed above. Neither is a directly matching untransformed `J–TH–TH` source.

This number **by itself is not unusual**. With the observed rune frequencies
(`J`: 24, `TH`: 30, `O/R/G`: 20/22/29), a rough random-permutation baseline
predicts approximately

$$
14976\times\frac{24}{729}\times\frac{30}{728}
\times\frac{20+22+29}{727}\approx1.98
$$

such center-totient source nodes for this *already specified* key. Thus the
global count of two is not statistical confirmation. The narrower finding is
the **particular spatial alignment** with the chosen MAP geometry and the
opening `J`.

## 8. Important equivalence with the earlier `THEN` key

The project's stage 17 (`THEN`) uses the aligned key `E–IA–IA`, with indices
`(18,27,27)`. Those are the exact additive inverses of the newly derived
`J–TH–TH` indices `(11,2,2)` modulo 29:

```text
E  (18) + J  (11) = 29
IA (27) + TH  (2) = 29
IA (27) + TH  (2) = 29
```

Consequently,

$$
C-(\mathrm{J},\mathrm{TH},\mathrm{TH})
\equiv C+(\mathrm{E},\mathrm{IA},\mathrm{IA})\pmod{29}.
$$

Adding the `THEN` key to the second heading word also yields `RATIO` **if
that key is restarted at the word boundary**. This is the *same mathematical
match* expressed using the complementary key and opposite arithmetic sign;
it must **not** be counted as a second independent success. The new element
is the spatial source `J–R–TH` obtained by continuing the MAP geometry.

## 9. Relationships already present in the red heading

The two word groups have the following rune-index sums:

| Group | Rune count | Index sum |
|---|---:|---:|
| `S–H–E–O–G–M–IA–F` | 8 | 96 |
| `S–Y–E–NG–C` | 5 | 85 |
| **Entire heading** | **13** | **181** |

Their difference equals the index of the opening rune `J`:

$$
96-85=11=\mathrm{J}.
$$

The previously recorded opening argument also used the heading's 13-rune
length and `φ(13)=12` to identify the coordinate `J(13,12)`. The new key
geometrically reuses exactly that same original `J` cell.

These equalities are **reproducible numerical observations**, not independent
evidence that subtraction of the two group sums was an intended instruction.
They should not be added as independent probabilities or used to retrofit
additional key choices.

## 10. Why this does not yet solve the red heading

### 10.1 The first word fails under the same key

Applying `J–TH–TH` with phase 0 directly to the first eight heading runes
produces:

```text
Ciphertext:  S  H  E  O  G  M  IA F
Plaintext:   R  G  T  NG R  B  T  IA
```

This is **not** recognizable plaintext. No deterministic second key for the
first word has yet been derived from the documented constraints. The idea
that **each red word has its own hidden key** therefore remains an open
hypothesis, not a demonstrated rule.

### 10.2 The candidate is not admissible as the immediate next stage after MAP

The selected MAP phase and cumulative phase total place the proposed route
in its `Direct/+0` mode. The three MAP ciphertext cells have absolute
positions `497`, `471`, and `445`, each with Möbius value `+1`. The project's
Report 01 therefore predicts the **next phase 0**, but its complete
**next-key signature `(0,0,0)`**.

The new key's actual signature is **`(+1,+1,+1)`**. Although both give phase
0, they are **different signatures**. The new source also passes the predicted
**even-row/odd-column center parity** (`18,17`) and the **non-mirror** source
class, but these partial matches do not cancel the signature failure.

Under the same proposed Reports 02–06, the next ordinary ciphertext after
MAP should also have a **right-going diagonal** orientation, with **even-row
endpoint and leftmost cell** and a constrained incoming ray. The second red
word, however, already occupies **row 1, columns 9–13**, and is **horizontal**.
It therefore cannot be presented as the direct next sequential block under
all those rules.

The candidate must instead be investigated as a **separate title/heading
reading**, possibly involving a return from the MAP geometry to an earlier
matrix region. This possibility has not been proven as a general rule.

### 10.3 Key-search freedom and short-word coincidences

The broader computational audit reconstructed the 28 chosen stage keys and
all 86 consumed ciphertext, key, and proposed plaintext runes; all selected
`C−K≡P (mod 29)` calculations check out. Sliding 13-rune windows of those
three streams through the heading, in two arithmetic directions and forward
or reverse key order, produced **888 tested variants**. Their longest exact
overlap with the previously proposed plaintext was **four runes** (`C–E–Y–I`);
none reached five. In a control using **500 random permutations** of the
heading's 13 runes, **278/500** produced at least a four-rune overlap by
the same search. This demonstrates why a short match obtained after a broad
search cannot be accepted alone.

A further exploratory search of eastern-half, parity-compatible, non-mirror
source nodes with the *predicted* after-MAP signature `(0,0,0)` found **614
eligible node realizations**, representing **555 distinct derived keys**
when direct and center-totient variants were permitted. None established a
convincing full-heading plaintext. This also illustrates the large remaining
key-selection freedom.

## 11. Verification recipe (standard Python, no external packages)

The following code reproduces the decisive geometric and arithmetic claims.
It intentionally tests only the **fixed** RATIO candidate, not an
unconstrained English-word search.

```python
from math import gcd

alphabet = "F U TH O R C G W H N I J EO P X S T B E M L NG OE D A AE Y IA EA".split()
index = {rune: number for number, rune in enumerate(alphabet)}

def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))

opening = (13, 12)             # J
map_center = (16, 9)          # X
map_endpoint = (17, 13)      # AE

step = (map_endpoint[0] - map_center[0],
        map_endpoint[1] - map_center[1])
assert step == (1, 4)

new_center = (map_endpoint[0] + step[0],
              map_endpoint[1] + step[1])
assert new_center == (18, 17)  # R

opposite_arm = (2 * new_center[0] - opening[0],
                2 * new_center[1] - opening[1])
assert opposite_arm == (23, 22)  # TH

# Matrix lookups, independently verified in the supplied 27x27 source:
assert (index["J"], index["R"], index["TH"]) == (11, 4, 2)
derived_key = [index["J"], phi(index["R"]), index["TH"]]
assert derived_key == [11, 2, 2]

ciphertext = [index[r] for r in ["S", "Y", "E", "NG", "C"]]
plaintext = [(c - derived_key[i % 3]) % 29
             for i, c in enumerate(ciphertext)]

assert plaintext == [4, 24, 16, 10, 3]
assert "".join(alphabet[n] for n in plaintext) == "RATIO"
print("SYENGC -> RATIO")
```

## 12. What would constitute a stronger test?

The next goal is **not** to generate more words by trying arbitrary triples.
The useful tests are predictive and should be recorded **before** evaluating
their outputs:

1. **Predict the key for the first eight red runes** using a unique geometric
   rule tied to the same opening/MAP construction, without choosing a desired
   English phrase first.
2. **Explain word-level key boundaries**: why and when a red heading word
   should restart a key, especially if black text is encoded differently.
3. **Reconcile or explicitly separate the signature rules**: demonstrate why
   a heading key would be allowed to have `(+1,+1,+1)` when the next normal
   post-MAP key is predicted to have `(0,0,0)`.
4. **Run falsification controls** on other predefined heading words or other
   sections, and on rune-shuffled matrices with the same fixed selection
   algorithm. Report the complete search space and all negative outcomes.
5. **Compare against alternative geometric constructions** with similar
   complexity. MAP's apparent uniqueness across the 28 stages should be
   interpreted only relative to the construction selected here.

## Conclusion

The candidate **`SYENGC → RATIO`** is an exact, transparent, five-rune modular
decryption with a mathematically well-defined key `J–TH–TH`. Two real source
nodes yield that key. The most interesting source is the diagonal
`J(13,12)–R(18,17)–TH(23,22)`: its center is reached by continuing the
selected MAP-center-to-endpoint displacement **one row down and four columns
right**, and its outer cells are then fixed by the opening `J` and reflection.

Among the **28 chosen stages**, applying that same construction produced only
two admissible geometries, and the MAP case alone produced `RATIO`.
**This is a promising geometric and arithmetic clue, not yet a demonstrated
full heading decryption or proof of Cicada's intended method.** Its value is
that the precise coordinates, operations, success, and failures can all be
checked or falsified.

---

### Project sources and scope

Based on the supplied snapshot of
`Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption-main`, particularly:

- `0-2-live-map.html` — the full 27×27 transcription and cell annotations.
- `plaintext-i-found/01-as-i-go-the.md` — opening `AE–J–EA` source and `J(13,12)`.
- `plaintext-i-found/17-then.md` — the `E–IA–IA` aligned key.
- `plaintext-i-found/28-map.md` — the selected MAP ciphertext, key center,
  phase, and reported geometric closure.
- `Start-reading-here/00-decryption-method.md` — core key/totient/signature/
  phase/subtraction definitions.
- `Start-reading-here/01-next-key-signature.md` and Reports 02–08 — the
  conditional next-block prediction framework.

The first 17 stages form the project's original reconstructed route; stages
18–28, including MAP, are **candidate extensions**. Any claim about the red
heading based on MAP inherits that conditional status.
