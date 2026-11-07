# Predicting the Exact Next Key-Node Axis

**Status: proposed GP-based refinement of [Report 13](13-predicting-next-key-axis-group.md), with retrospective agreement on all 33 selected transitions.** The targeted controls below support further investigation; the rule has not been independently validated on a new transition.

## 1. What is new?

Report 13 predicts a group containing two possible axes of the next **original three-rune key node**. The present candidate adds a bit that distinguishes a diagonal from a horizontal or vertical source. Together, the two bits select one exact undirected axis:

| Report 13 group bit b | New diagonal bit d | Axis number 2b+d | Next original key-node axis |
| :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | Horizontal, W–E |
| 0 | 1 | 1 | Diagonal, NW–SE |
| 1 | 0 | 2 | Vertical, N–S |
| 1 | 1 | 3 | Diagonal, NE–SW |

This predicts the source node's axis **before any center transformation or cyclic key alignment**. It leaves the source's radius, center position and reading order unresolved. The next ciphertext's axis is a separate property, addressed by [Report 03](03-predicting-axis-and-reading-direction.md).

## 2. Coordinates and inputs

Use the project's **27 × 27** matrix with 1-based `(row, column)` coordinates. Rows increase downward; columns increase to the right. All inputs belong to the **current** block.

| Symbol | Meaning |
| :--- | :--- |
| M | Center of the current original key node |
| Z | Its lower outer cell; for a horizontal node, its right outer cell |
| L | Current ciphertext's leftmost cell: smallest column, bottommost on ties |
| u, h, z | The three original source-rune indices, before applying φ or rotating the key |
| GP(k) | The prime weight of rune index k |

The source is a valid, equally spaced three-cell node on one of the four axes. Keep its center in the middle of the supplied coordinate triple. Reversing the whole triple preserves M, Z and the GP sum. L is selected geometrically and need not be the first ciphertext cell read.

GP assigns the first 29 primes in rune-index order: **F=2, U=3, TH=5, O=7, R=11, …, EA=109**. Use the original source values, including the **original center h**. The GP sum of a transformed key is a different quantity.

The rotated absolute cell indices are:

$$
n_0(r,c)=27(r-1)+c,\qquad n_1(r,c)=27(c-1)+28-r,
$$

$$
n_2(r,c)=730-n_0(r,c),\qquad n_3(r,c)=730-n_1(r,c).
$$

These number the same original cell after 0°, 90°, 180° and 270° clockwise rotations. They do not select additional cells from which runes are read. Keep sums of indices as ordinary integers, including values greater than 729.

## 3. Proposed exact-axis rule

### A. Retain the group bit from Report 13

Calculate:

$$
X=n_1(M)+n_2(Z),\qquad Y=n_1(L)+n_2(Z).
$$

Then:

$$
b=1\oplus\mathbf1[\mu(X)<0]\oplus\mathbf1[\mu(Y)<0].
$$

Thus **b=1** when the two Möbius values are both negative or both nonnegative. Zero belongs to the nonnegative class.

### B. Calculate the additional diagonal bit

Use two coordinate-based arguments and the GP sum of the original source:

$$
G=\gcd\bigl(n_1(M),n_3(Z)\bigr),
$$

$$
T=GP(u)+GP(h)+GP(z),\qquad A=n_0(M)+n_3(Z).
$$

The proposed bit is:

$$
\boxed{d=\mathbf1[\mu(G)<0]\oplus\mathbf1[\mu(T)>0]\oplus\mathbf1[\mu(A)\ne0].}
$$

Each indicator is **1 when its condition is true and 0 otherwise**. The symbol ⊕ means XOR, or addition modulo 2.

| Term | Contributes 1 when |
| :--- | :--- |
| First | μ(G) is negative |
| GP term | μ(T) is positive |
| Third | A is squarefree: μ(A) is either +1 or −1 |

These are three different tests. A zero Möbius value contributes 0 in each term. The result **d=1 predicts a diagonal**; **d=0 predicts a horizontal or vertical source**.

### C. Select the exact axis

$$
\boxed{\mathrm{axis}_{i+1}=2b+d}
$$

Use the numbering in Section 1. The calculation needs no following plaintext, next-source coordinates or rune values, chosen next length, block number, or accumulated phase S.

### Direct implementation

Supply the current original source coordinates in **outer–center–outer** order. `current_cipher_cells` is a nonempty list of all current ciphertext coordinates, in reading order. Coordinates are integer pairs in 1…27. `original_node_runes` contains the three corresponding **original rune indices**, 0…28, before any center transformation or cyclic alignment.

The supplied `mu` function evaluates Möbius on positive integers through at least **1458**; the function from [Report 00](00-decryption-method.md) is suitable. The GP prime table is included. `expected_next_key_axis` returns **0=horizontal, 1=NW–SE, 2=vertical, 3=NE–SW**. The acceptance helper compares this forecast with a proposed next source's physical axis.

The code includes Report 13's group calculation, so no function from that report needs to be imported. The caller must supply rune indices from the same source cells as `current_node`.

```python
from math import gcd


GP_PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109,
)


def original_key_axis(node):
    """Return 0=H, 1=NW-SE, 2=V, 3=NE-SW for an equally spaced node."""
    if len(node) != 3:
        raise ValueError("The source must contain three coordinates.")
    first, center, last = node
    if (2 * center[0], 2 * center[1]) != (
        first[0] + last[0], first[1] + last[1]
    ):
        raise ValueError("The center must bisect the two outer cells.")

    dr, dc = last[0] - first[0], last[1] - first[1]
    if dr == 0 and dc != 0:
        return 0
    if dc == 0 and dr != 0:
        return 2
    if dr != 0 and abs(dr) == abs(dc):
        return 1 if dr * dc > 0 else 3
    raise ValueError("The source must have a nondegenerate four-axis geometry.")


def expected_next_key_axis(
    current_node, current_cipher_cells, original_node_runes, mu
):
    """Predict one exact next-source axis using current-block inputs only."""
    original_key_axis(current_node)  # Check source spacing and axis.
    if not current_cipher_cells:
        raise ValueError("The current ciphertext must be nonempty.")
    if len(original_node_runes) != 3 or any(
        not 0 <= k <= 28 for k in original_node_runes
    ):
        raise ValueError("Supply three original rune indices in 0..28.")

    M = current_node[1]
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

    def n0(cell):
        r, c = cell
        return 27 * (r - 1) + c

    def n90(cell):
        r, c = cell
        return 27 * (c - 1) + 28 - r

    def n180(cell):
        return 730 - n0(cell)

    def n270(cell):
        return 730 - n90(cell)

    X = n90(M) + n180(Z)
    Y = n90(L) + n180(Z)
    group = int((mu(X) < 0) == (mu(Y) < 0))

    G = gcd(n90(M), n270(Z))
    T = sum(GP_PRIMES[k] for k in original_node_runes)
    A = n0(M) + n270(Z)
    diagonal = int(mu(G) < 0) ^ int(mu(T) > 0) ^ int(mu(A) != 0)
    return 2 * group + diagonal


def accepts_next_key_axis(
    current_node, current_cipher_cells, original_node_runes, next_node, mu
):
    """Check a proposed next original source against the exact-axis forecast."""
    predicted = expected_next_key_axis(
        current_node, current_cipher_cells, original_node_runes, mu
    )
    return original_key_axis(next_node) == predicted


# Keep a proposed next source only if:
# accepts_next_key_axis(
#     current_node, current_cipher_cells, original_node_runes, next_node, mu
# )
```

## 4. Worked examples

### NOW THE (07) → IDEA (08): NW–SE

The current source is `(18,16)–(19,16)–(20,16)`, with original rune indices **(22,11,22)**. Therefore:

$$
T=83+37+83=203,\qquad \mu(T)=+1.
$$

The geometric arguments give **G=1**, **A=819**, with **μ(G)=+1** and **μ(A)=0**. Hence:

$$
d=0\oplus1\oplus0=1.
$$

Report 13 gives **b=0**: `X=615` has μ=−1, while `Y=623` has μ=+1. Consequently **2b+d=1**, predicting **NW–SE**. IDEA's recorded source `(8,13)–(11,16)–(14,19)` has that axis.

### WEATHER (02) → TURNS (03): vertical

For WEATHER, **G=1**, **T=177**, **A=937**, and their Möbius values are **(+1,+1,−1)**. Thus:

$$
d=0\oplus1\oplus1=0.
$$

With Report 13's **b=1**, the exact prediction is **2: vertical**. This matches the original TURNS source `(4,23)–(14,23)–(24,23)`.

## 5. Agreement on the selected route

The route contains **34 blocks, 105 plaintext runes and 33 transitions**. The combined candidate agrees with every next recorded source: **8 horizontal, 16 vertical, 3 NW–SE and 6 NE–SW**. The additional bit correctly separates all **9 diagonal** sources from all **24 horizontal/vertical** sources.

Independent verification checked the original source-rune values against the matrix, regenerated the GP prime weights, and checked μ for every integer from 1 through 1458. All **132 combinations of reversing the current and next source orders** preserve the result. The source-axis classifier was also checked on all **14,976** valid equally spaced physical node geometries, in both orders.

These agreements are conditional on the selected route and source assignments, including the SOON source centered at **(25,7)**. The 33 transitions are not 33 fully independent samples: two current physical sources recur.

### The specific contribution of the GP term

With both geometric terms and the recorded answers fixed:

| Added bit | Errors corrected | Correct cases spoiled | Exact next axes |
| :--- | ---: | ---: | ---: |
| None | — | — | 18/33 |
| Positive μ of the original source's GP sum | **15** | **0** | **33/33** |
| Positive μ of the transformed key's GP sum | 6 | 7 | 17/33 |
| Positive μ of the ordinary original rune-index sum | 4 | 6 | 16/33 |

The successful GP bit flips exactly the 15 initially incorrect cases. This is an observed property of the fitted formula on this route.

## 6. Targeted controls and their interpretation

### Random labels with GP required

The known Report-13 bit b was held fixed. Random targets retained **3 diagonals among the 11 positions with b=0**, and **6 among the 22 positions with b=1**. This preserves the counts of all four axes.

For the principal targeted search, the exact GP bit `μ(T)>0` was mandatory. Up to two other terms and an optional constant could be chosen from the previous feature library. All 26 explicitly GP-derived columns were excluded from that free part, leaving **2,977 columns**. The other terms were allowed to use the remaining current-block features; they were not restricted to coordinates alone.

There are **12,311,145** possible targets in this conditional label space. Counting distinct attainable targets gives the exact fractions below. The Monte Carlo columns use the same million targets, seed `33010801`.

| Mandatory GP condition and permitted additional choices | Exact target-space fraction admitting 33/33 | Fits in 1,000,000 random targets |
| :--- | ---: | ---: |
| Original GP sum, fixed `μ(T)>0`; choose the other ≤2 terms | **10,608 / 12,311,145 = 0.08617%** | **807** |
| Original GP sum; also choose positive, negative or nonzero μ | 46,327 / 12,311,145 = 0.37630% | 3,682 |
| Also choose original or transformed GP sum | 88,049 / 12,311,145 = 0.71520% | 7,074 |

When the entire formula was frozen, the million random targets produced **zero** exact matches. In the broader feature library without a mandatory GP term, the earlier three-feature control produced exact fits for **65.15%** of random targets. These are different search conditions.

### Random prime weights with geometry fixed

The original rune indices, geometric terms and real answers were held fixed. For each trial, the prime weights were reassigned and the GP sums and their Möbius values were recalculated; no other terms were refitted. Repeated runes and source nodes therefore remained coupled.

| Prime-weight randomization | Trials | Exact 33/33 results | Best result |
| :--- | ---: | ---: | ---: |
| Keep F=2; permute the remaining 28 prime weights | 1,000,000 | **0** | 30/33 |
| Permute all 29 prime weights | 1,000,000 | **0** | 30/33 |

The seeds were `33010802` and `33010803`. Zero observed hits does not establish a zero probability. A separate local check found **28 of 378** single exchanges of two odd prime weights that preserve 33/33, so the canonical GP ordering is not uniquely determined by this route.

### Limits of the control evidence

The candidate was discovered by exploring the same 33 transitions. GP was not an obligatory input before the original broad search. Requiring an already successful term afterwards narrows the search, so the targeted fractions cannot replace the assessment of the original search as a whole. They are conditional descriptions of these controls, not probabilities that Cicada intended the formula.

Within a subsequently examined family of **13,824** three-term templates using rotated M/Z GCDs and sums, a GP sign test and a constant, this was the only exact syntactic fit. That family was also examined after the exploratory search. A new transition established on independent grounds remains the essential test.

## 7. A fixed prediction after YOU (34)

The final YOU has:

$$
M=(21,22),\qquad Z=(21,27),\qquad L=(6,11).
$$

Its original source is **H–R–H**, with rune indices **(8,4,8)**. The arguments are:

$$
G=\gcd(574,21)=7,\quad T=23+11+23=57,\quad A=562+21=583.
$$

Since **μ(7)=−1**, **μ(57)=+1** and **μ(583)=+1**:

$$
d=1\oplus1\oplus1=1.
$$

Report 13 gives **b=0**, so the combined conditional prediction is:

$$
\boxed{\text{The next original key node has the NW–SE axis.}}
$$

Both source-reading orders, ↖ and ↘, remain possible. [Report 12](12-predicting-exact-ray-deviation.md) separately requires the next ciphertext beginning to have ray-offset score 1 from `(6,11)`.

In a fresh incoming continuation enumeration using Reports 00–13, the proposed cyclic phase extension, and all straight ciphertext lengths 2…27, the added axis constraint reduces **13 source/mode assignments to 5**, **3,955 source-plus-ciphertext assignments to 1,591**, and **3,270 distinct plaintext rune strings to 1,221**. No word list or chosen next length was used. These counts apply the incoming constraint for block 35; they do not impose the new full-axis rule on an outgoing transition to an unknown block 36.

The reduction is a consequence of applying the candidate, not an independent confirmation of it. No unique next word follows from this axis prediction.

## 8. Scope and reproducibility

This report records a reproducible exact-axis candidate and the controls limiting its interpretation. It does not establish a unique plaintext, source radius, or intended construction. Experiments with the filter should retain a comparison run without it.

The calculations use the selected-route snapshot with SHA-256:

```text
96b5679e8c296bc4f333f7f746fc4fb9537253b4e9f5b43785c458ce94d1f8a4
```

The separately supplied `LP2_exact_next_key_axis_research.zip` and `LP2_GP_specific_controls_repro.zip` contain the route, verification traces, source snapshot and control code. The first archive verifies the fitted axis rule and continuation enumeration; the second reproduces the GP-specific randomization experiments. The direct implementation above needs only standard-library Python and the supplied Möbius function.

## Appendix: all 33 selected transitions

G, T and A are the arguments of the additional bit. The two bits jointly give the predicted exact axis. Block numbers distinguish repeated readings.

| Transition | Current → next reading | G | T | A | μ(G) | μ(T) | μ(A) | b | d | Predicted axis | Recorded axis |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | :---: | :---: | :--- | :--- |
| 01→02 | AS I GO THE → WEATHER | 1 | 247 | 727 | +1 | +1 | −1 | 0 | 0 | H | H |
| 02→03 | WEATHER → TURNS | 1 | 177 | 937 | +1 | +1 | −1 | 1 | 0 | V | V |
| 03→04 | TURNS → COLD | 4 | 115 | 506 | 0 | +1 | −1 | 1 | 0 | V | V |
| 04→05 | COLD → I MAY | 1 | 51 | 937 | +1 | +1 | −1 | 1 | 0 | V | V |
| 05→06 | I MAY → CRY | 2 | 219 | 916 | −1 | +1 | 0 | 1 | 0 | V | V |
| 06→07 | CRY → NOW THE | 17 | 181 | 987 | −1 | −1 | −1 | 1 | 0 | V | V |
| 07→08 | NOW THE → IDEA | 1 | 203 | 819 | +1 | +1 | 0 | 0 | 1 | NW–SE | NW–SE |
| 08→09 | IDEA → OF | 2 | 199 | 516 | −1 | −1 | 0 | 1 | 1 | NE–SW | NE–SW |
| 09→10 | OF → THE | 2 | 163 | 766 | −1 | −1 | +1 | 1 | 0 | V | V |
| 10→11 | THE → END | 1 | 203 | 819 | +1 | +1 | 0 | 1 | 1 | NE–SW | NE–SW |
| 11→12 | END → IS | 2 | 135 | 1146 | −1 | 0 | −1 | 0 | 0 | H | H |
| 12→13 | IS → DEATH | 7 | 57 | 583 | −1 | +1 | +1 | 1 | 1 | NE–SW | NE–SW |
| 13→14 | DEATH → SEE | 2 | 135 | 1146 | −1 | 0 | −1 | 0 | 0 | H | H |
| 14→15 | SEE → YOU | 2 | 255 | 1138 | −1 | −1 | +1 | 1 | 0 | V | V |
| 15→16 | YOU → SOON | 3 | 97 | 745 | −1 | −1 | +1 | 0 | 0 | H | H |
| 16→17 | SOON → THEN | 11 | 195 | 1139 | −1 | −1 | +1 | 1 | 0 | V | V |
| 17→18 | THEN → THE | 1 | 321 | 859 | +1 | +1 | −1 | 1 | 0 | V | V |
| 18→19 | THE → KEY | 1 | 129 | 823 | +1 | +1 | −1 | 1 | 0 | V | V |
| 19→20 | KEY → IS | 1 | 33 | 623 | +1 | +1 | +1 | 0 | 0 | H | H |
| 20→21 | IS → TO | 1 | 69 | 782 | +1 | +1 | −1 | 1 | 0 | V | V |
| 21→22 | TO → GO | 1 | 165 | 279 | +1 | −1 | 0 | 1 | 0 | V | V |
| 22→23 | GO → TO | 1 | 27 | 681 | +1 | 0 | +1 | 0 | 1 | NW–SE | NW–SE |
| 23→24 | TO → THE | 1 | 207 | 580 | +1 | 0 | 0 | 1 | 0 | V | V |
| 24→25 | THE → EAST | 1 | 173 | 993 | +1 | −1 | +1 | 0 | 1 | NW–SE | NW–SE |
| 25→26 | EAST → OF | 1 | 163 | 442 | +1 | −1 | −1 | 1 | 1 | NE–SW | NE–SW |
| 26→27 | OF → THE | 2 | 105 | 586 | −1 | −1 | +1 | 1 | 0 | V | V |
| 27→28 | THE → MAP LIFE | 1 | 57 | 1349 | +1 | +1 | +1 | 1 | 0 | V | V |
| 28→29 | MAP LIFE → MAY | 1 | 119 | 917 | +1 | +1 | +1 | 1 | 0 | V | V |
| 29→30 | MAY → BE | 1 | 243 | 759 | +1 | 0 | −1 | 1 | 1 | NE–SW | NE–SW |
| 30→31 | BE → THE | 2 | 109 | 1196 | −1 | −1 | 0 | 1 | 1 | NE–SW | NE–SW |
| 31→32 | THE → DEATH | 1 | 217 | 574 | +1 | +1 | −1 | 0 | 0 | H | H |
| 32→33 | DEATH → OF | 8 | 105 | 750 | 0 | −1 | 0 | 0 | 0 | H | H |
| 33→34 | OF → YOU | 1 | 137 | 404 | +1 | −1 | 0 | 0 | 0 | H | H |

**Related reports:** [00 — Decryption method](00-decryption-method.md) · [03 — Ciphertext axis and direction](03-predicting-axis-and-reading-direction.md) · [12 — Exact ray deviation](12-predicting-exact-ray-deviation.md) · [13 — Key-node axis group](13-predicting-next-key-axis-group.md).
