# Predicting the Parity of the Next Key-Node Radius

**Report 15. Status: a proposed geometric constraint with independently reproduced agreement on all 33 selected transitions.** It removes **48.70%** of the physical source-node candidates remaining after the selected earlier geometric filters. Its fit is retrospective; no new plaintext or independently established transition is demonstrated here.

## 1. What the rule predicts

[Report 14](14-predicting-exact-next-key-axis.md) selects the next original key node's undirected axis. This report proposes one more bit: whether that node's **physical radius is even or odd**.

The radius is the number of grid steps from the original source's center to either outer cell:

$$
R=\max\bigl(|r_U-r_M|,\;|c_U-c_M|\bigr),
$$

where `U` is either outer cell. A diagonal source with displacement `(3,3)` has radius **3**, not its Euclidean length. Valid equally spaced three-cell nodes in the 27 × 27 grid have `1≤R≤13`.

The proposed rule predicts **only parity**. It does not determine the exact radius, center, source runes, next ciphertext, block length, or plaintext.

## 2. Coordinates and current-block inputs

Use **1-based** coordinates `(row, column)`, with rows increasing downward and columns to the right.

| Symbol | Current-block input |
| :--- | :--- |
| M | Center of the original three-rune source, before any center transformation |
| Z | Lower original outer cell; for a horizontal source, the right outer cell |
| B | First ciphertext cell in the established reading order |
| E | Last ciphertext cell in that order |
| L | Ciphertext's leftmost cell: smallest column, bottommost on a tie |
| R′ | Radius of the proposed next original source; the comparison target |

**L need not equal B.** The selected source coordinates matter even when different physical sources produce the same transformed numerical key. Reversing a source triple preserves M and the geometrically defined Z.

For any original cell `X=(r,c)`, define:

$$
n_0(X)=27(r-1)+c,\qquad
n_1(X)=27(c-1)+28-r,
$$

$$
n_2(X)=730-n_0(X),\qquad
n_3(X)=730-n_1(X).
$$

These are the absolute indices of the same cell after clockwise rotations by 0°, 90°, 180° and 270°. They do not instruct the reader to select different rune cells. Keep index sums as **ordinary integers**; do not reduce them modulo 729 or 29.

The Möbius function has values −1, 0 and +1. It vanishes when an integer has a squared prime factor; otherwise its sign records the parity of the number of distinct prime factors, with μ(1)=+1. See [NIST DLMF, Eq. 27.2.12](https://dlmf.nist.gov/27.2#E12).

## 3. Proposed parity rule

Calculate:

$$
a=\bigl(|r_M-r_B|+|c_M-c_B|\bigr)\bmod2,
$$

$$
g=\gcd\bigl(n_2(Z),n_2(L)\bigr),\qquad
b=\mathbf1[\mu(g)<0],
$$

$$
s=n_1(B)+n_1(E),\qquad
c=\mathbf1[\mu(s)>0].
$$

Then:

$$
\boxed{R'\bmod2=a\oplus b\oplus c.}
$$

Here **⊕ is XOR**, or addition modulo 2. Each indicator is 1 when its condition is true and 0 otherwise.

| Output | Interpretation |
| :---: | :--- |
| 0 | Keep next original sources with even radius |
| 1 | Keep next original sources with odd radius |

The two Möbius sign tests are different: **b tests negativity; c tests positivity.** A zero Möbius value contributes 0 in both tests. Replacing these indicators with μ itself modulo 2 would change the rule.

Every input is available from the current selected block. The calculation uses no next plaintext, next-source coordinates, next radius, accumulated phase, block number, Gematria Primus weights, or rune identities.

### A simpler interpretation of the first term

For integers, `|x−y|≡x+y (mod 2)`. Therefore:

$$
a=(r_M+c_M+r_B+c_B)\bmod2.
$$

Thus **a simply compares the checkerboard colors of M and B**: it is 1 when they differ. The Manhattan-distance notation adds no extra metric information at parity level.

Also:

$$
s=27(c_B+c_E)+2-r_B-r_E.
$$

These identities simplify implementation. They do not explain why the two Möbius corrections should predict a future radius. That cross-block relationship remains the empirical claim.

## 4. Direct implementation

Supply each source in **outer–center–outer** order, including when the order is reversed. Supply all current ciphertext coordinates in their established reading order. The `mu` argument is a Möbius implementation on positive integers; support through 1458 is sufficient for these formulas.

```python
from math import gcd


def original_key_radius(node):
    """Radius in grid steps for a nondegenerate four-axis source."""
    if len(node) != 3:
        raise ValueError("Supply three source coordinates.")
    first, center, last = node
    if any(
        len(cell) != 2 or any(not 1 <= v <= 27 for v in cell)
        for cell in node
    ):
        raise ValueError("Source coordinates must lie in 1..27.")
    if (first[0] + last[0], first[1] + last[1]) != (
        2 * center[0], 2 * center[1]
    ):
        raise ValueError("The center must bisect the source.")
    dr = first[0] - center[0]
    dc = first[1] - center[1]
    if (dr, dc) == (0, 0) or not (
        dr == 0 or dc == 0 or abs(dr) == abs(dc)
    ):
        raise ValueError("Use a nondegenerate four-axis source.")
    return max(abs(dr), abs(dc))


def expected_next_key_radius_parity(
    current_node, current_cipher_cells, mu
):
    """Return 0=even or 1=odd, using current-block inputs only."""
    original_key_radius(current_node)
    if not current_cipher_cells:
        raise ValueError("The current ciphertext must be nonempty.")
    if any(
        len(cell) != 2 or any(not 1 <= v <= 27 for v in cell)
        for cell in current_cipher_cells
    ):
        raise ValueError("Ciphertext coordinates must lie in 1..27.")

    M = current_node[1]
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    B = current_cipher_cells[0]
    E = current_cipher_cells[-1]
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

    def n90(cell):
        r, col = cell
        return 27 * (col - 1) + 28 - r

    def n180(cell):
        r, col = cell
        return 730 - (27 * (r - 1) + col)

    a = (M[0] + M[1] + B[0] + B[1]) % 2
    b = int(mu(gcd(n180(Z), n180(L))) < 0)
    c = int(mu(n90(B) + n90(E)) > 0)
    return a ^ b ^ c


def accepts_next_key_radius_parity(
    current_node, current_cipher_cells, next_node, mu
):
    predicted = expected_next_key_radius_parity(
        current_node, current_cipher_cells, mu
    )
    return original_key_radius(next_node) % 2 == predicted
```

The acceptance helper compares a candidate with the forecast. It does not select a source or establish a new plaintext.

## 5. Worked examples

### WEATHER (02) → TURNS (03): even

The current inputs are:

$$
M=(14,5),\quad Z=(14,6),\quad
B=L=(14,14),\quad E=(14,18).
$$

The center-to-beginning checkerboard difference is:

$$
a=(0+9)\bmod2=1.
$$

The arithmetic arguments are:

$$
g=\gcd(373,365)=1,\qquad \mu(g)=+1,
$$

$$
s=365+473=838=2\cdot419,\qquad \mu(s)=+1.
$$

Thus `b=0`, `c=1` and:

$$
R'\bmod2=1\oplus0\oplus1=0.
$$

The recorded TURNS source has radius **10**, agreeing with the even forecast.

### SOON (16) → THEN (17): odd

For the selected SOON source `(25,4)–(25,7)–(25,10)`:

$$
M=(25,7),\quad Z=(25,10),\quad
B=L=(25,16),\quad E=(25,19).
$$

Then:

$$
a=9\bmod2=1,
$$

$$
g=\gcd(72,66)=6,\qquad \mu(6)=+1,
$$

$$
s=408+489=897=3\cdot13\cdot23,\qquad \mu(897)=-1.
$$

Therefore `b=c=0` and the predicted parity is **odd**. The recorded THEN source has radius **1**.

## 6. Agreement on the selected route

The verification reconstructs **34 documented blocks and 33 transitions** from the supplied project snapshot. The next radii contain **21 odd and 12 even** outcomes. An always-odd baseline obtains **21/33 = 63.64%**; the proposed formula obtains **33/33**.

The classes are **unequal**, rather than approximately 50:50. Nevertheless, the fit is not explained by a constant majority-class prediction.

### Contribution of each term

| Expression retained | Correct next-radius parities |
| :--- | ---: |
| a ⊕ b, omitting c | 21/33 |
| a ⊕ c, omitting b | 19/33 |
| b ⊕ c, omitting a | 18/33 |
| **a ⊕ b ⊕ c** | **33/33** |

All three terms contribute on this route. In particular, adding c to a ⊕ b corrects exactly 12 errors and spoils no correct cases. These are descriptions of the fitted expression; they are not independent validation of its discovery.

### All 33 transitions

The values g and s are the integer arguments defined in Section 3. “Prediction” is the forecast for the **next** original source.

| No. | Current → next reading | a | g | μ(g) | s | μ(s) | Prediction | Recorded R′ |
| :--- | :--- | :---: | ---: | :---: | ---: | :---: | :---: | ---: |
| 01→02 | AS I GO, THE → WEATHER | 1 | 3 | -1 | 758 | +1 | Odd | 1 |
| 02→03 | WEATHER → TURNS | 1 | 1 | +1 | 838 | +1 | Even | 10 |
| 03→04 | TURNS → COLD | 0 | 2 | -1 | 1004 | 0 | Odd | 1 |
| 04→05 | COLD → I MAY | 0 | 3 | -1 | 355 | +1 | Even | 2 |
| 05→06 | I MAY → CRY | 0 | 1 | +1 | 895 | +1 | Odd | 1 |
| 06→07 | CRY → NOW THE | 0 | 3 | -1 | 830 | -1 | Odd | 1 |
| 07→08 | NOW THE → IDEA | 0 | 3 | -1 | 948 | 0 | Odd | 3 |
| 08→09 | IDEA → OF | 0 | 40 | 0 | 996 | 0 | Even | 2 |
| 09→10 | OF → THE | 0 | 4 | 0 | 803 | +1 | Odd | 1 |
| 10→11 | THE → END | 1 | 3 | -1 | 855 | 0 | Even | 4 |
| 11→12 | END → IS | 1 | 1 | +1 | 1204 | 0 | Odd | 5 |
| 12→13 | IS → DEATH | 1 | 1 | +1 | 473 | +1 | Even | 4 |
| 13→14 | DEATH → SEE | 0 | 2 | -1 | 58 | +1 | Even | 4 |
| 14→15 | SEE → YOU | 0 | 2 | -1 | 760 | 0 | Odd | 11 |
| 15→16 | YOU → SOON | 1 | 6 | +1 | 868 | 0 | Odd | 3 |
| 16→17 | SOON → THEN | 1 | 6 | +1 | 897 | -1 | Odd | 1 |
| 17→18 | THEN → THE | 0 | 3 | -1 | 1356 | 0 | Odd | 3 |
| 18→19 | THE → KEY | 0 | 17 | -1 | 1066 | -1 | Odd | 1 |
| 19→20 | KEY → IS | 1 | 6 | +1 | 178 | +1 | Even | 6 |
| 20→21 | IS → TO | 1 | 1 | +1 | 316 | 0 | Odd | 3 |
| 21→22 | TO → GO | 0 | 3 | -1 | 876 | 0 | Odd | 7 |
| 22→23 | GO → TO | 1 | 2 | -1 | 1091 | -1 | Even | 6 |
| 23→24 | TO → THE | 1 | 1 | +1 | 1193 | -1 | Odd | 3 |
| 24→25 | THE → EAST | 0 | 2 | -1 | 983 | -1 | Odd | 7 |
| 25→26 | EAST → OF | 0 | 1 | +1 | 1214 | +1 | Odd | 1 |
| 26→27 | OF → THE | 1 | 1 | +1 | 664 | 0 | Odd | 1 |
| 27→28 | THE → MAPLIFE | 1 | 1 | +1 | 637 | 0 | Odd | 1 |
| 28→29 | MAPLIFE → MAY | 1 | 1 | +1 | 726 | 0 | Odd | 3 |
| 29→30 | MAY → BE | 0 | 5 | -1 | 614 | +1 | Even | 6 |
| 30→31 | BE → THE | 0 | 4 | 0 | 572 | 0 | Even | 4 |
| 31→32 | THE → DEATH | 0 | 1 | +1 | 601 | -1 | Even | 6 |
| 32→33 | DEATH → OF | 1 | 1 | +1 | 466 | +1 | Even | 4 |
| 33→34 | OF → YOU | 0 | 1 | +1 | 923 | +1 | Odd | 5 |

## 7. How much it narrows the source search

Enumerate every equally spaced physical three-cell source on the four undirected axes, with radius 1…13 and all cells inside the grid. This gives **14,976 source geometries**, counting a source and its reverse once.

For each of the 33 transitions, hold the current recorded block fixed and apply:

- the next source's exact axis from Report 14;
- the next center's row and column parities from [Report 04](04-predicting-next-key-center-parity.md);
- the next source's equal-outer-rune status from [Report 07](07-predicting-next-key-mirror-status.md).

All three forecasts were recomputed from the current state and checked against the next recorded source before counting.

| Filters applied | Physical source-node candidates, summed over 33 local searches |
| :--- | ---: |
| Reports 04, 07 and 14 | 11,896 |
| Those filters plus radius parity | **6,103** |
| Removed by the parity filter | **5,793 — 48.70%** |

These are **sums of separate local source searches**, not complete-route counts, unique global nodes, source/transformation assignments, or distinct plaintext strings. A physical source can be counted at several transitions.

The reduction varies from **28.57% to 61.68%** across the local searches. It demonstrates practical selectivity beyond the stated axis/center/mirror filters. It does not establish statistical independence from those rules or predict the survival rate of complete text routes.

## 8. SOON: source dependence and the earlier filters

The SOON document gives three original sources that all transform to the same numerical key, `L–R–EA`. The parity expression is sensitive to which physical source is supplied.

However, **numerical-key equivalence is not the same as eligibility under the incoming geometric constraints**. From YOU (15), Reports 04 and 14 predict a **horizontal source centered on an odd row and odd column**. Report 07 predicts unequal outer rune symbols.

| SOON source | Center | Physical axis | Outgoing radius-parity forecast | Incoming geometric checks |
| :--- | :---: | :--- | :---: | :--- |
| L–C–EA | (25,7) | Horizontal | Odd — agrees with THEN | Pass |
| L–I–EA | (20,15) | Vertical | Even — disagrees with THEN | Fails axis and center-row parity |
| L–EO–EA | (25,14) | Horizontal | Odd — agrees with THEN | Fails center-column parity |

This sharpens the earlier warning about SOON. The formula is **not invariant under substituting every numerically equivalent source**. But the documented alternative that reverses its prediction is already excluded by the earlier incoming geometric rules. It is therefore not a counterexample within that constrained route.

The correct scope is a rule about **selected physical source states**, not a rule determined by the numerical key alone. This check covers the three documented SOON sources; it does not prove invariance or uniqueness over every possible source assignment.

## 9. How unusual is the formula?

### A narrow, fully specified family

A new exhaustive check held the checkerboard term a and the anchor pairs fixed, while allowing all rotations and Möbius sign tests:

$$
F=a\oplus
t_g\!\left(\mu\!\left(\gcd(n_j(Z),n_k(L))\right)\right)
\oplus
t_s\!\left(\mu\!\left(n_\ell(B)+n_m(E)\right)\right)
\oplus\varepsilon,
$$

with `j,k,ℓ,m∈{0,1,2,3}`, `ε∈{0,1}`, and each test independently chosen from **negative, positive, nonzero**.

There are:

$$
4^4\cdot3^2\cdot2=\boxed{4,608}
$$

parameter combinations. They produced 4,608 distinct prediction vectors on this route. **Exactly one** fitted all 33 labels:

| Parameter | Unique exact choice |
| :--- | :--- |
| GCD rotations (j,k) | (2,2): both 180° |
| Sum rotations (ℓ,m) | (1,1): both 90° |
| GCD Möbius test | Negative |
| Sum Möbius test | Positive |
| Constant ε | 0 |

Thus the selected combination stands out among close rotation/sign substitutions. The family was constructed around the already found expression. Its uniqueness is **relative to this family**, not a corrected significance test for the original discovery or a proof that no simpler formula exists.

### The original broad search

The archived radius report states that a bank of **2,622 distinct binary predicates** produced **four exact three-term XOR representations**. If every unordered triple of distinct columns is allowed, the syntax alone permits:

$$
\binom{2622}{3}=3,000,887,740
$$

triplets. Their predictions are correlated, so this is not a count of independent statistical tests. It does show why discovering a short perfect fit after a broad search needs a control that repeats the same search.

The four original expressions and the complete feature bank were not present in the retrieved verifier. Their reported count is retained as provenance, **not independently reproduced here**. The new 4,608-expression check does not recreate that broader search.

### Conflicting archived shuffle claims

| Available source | Reported result for at least four exact XOR triplets |
| :--- | :--- |
| Supplied screenshot | 0 of 30 shuffled label sets |
| Saved `lp_new_radius_rules_report.md` | 2 of 30 shuffled label sets |

The screenshot additionally reports at least one exact fit in **11 of 30** shuffles. The underlying permutation script and complete search specification were unavailable in the retrieved materials, so the discrepancy cannot be resolved from the surviving counts. **Neither 0/30 nor 2/30 is promoted to a verified significance result in this report. No million-shuffle result is claimed here.**

### Why a frozen-formula probability is insufficient

If all 33 labels were uniformly reassigned while preserving exactly 21 odd and 12 even outcomes, one *previously fixed* prediction vector would match the entire target with probability:

$$
\frac{1}{\binom{33}{12}}
=\frac{1}{354,817,320}
\approx2.82\times10^{-9}.
$$

This is a combinatorial result under that stated label model. It is **not the discovery's p-value**: the formula, feature choices and route were selected after examining the data. The route also contains overlapping cells and repeated sources rather than 33 independent random samples.

A million shuffles of the frozen formula would therefore be expected to give very few exact matches even when a broad search can find other perfect formulas. A meaningful discovery control must repeat the allowed formula search, with its constants, complements, feature construction and source-selection choices specified in advance.

## 10. A fixed forecast after YOU (34)

The last documented block has:

$$
M=(21,22),\quad Z=(21,27),\quad
B=L=(6,11),\quad E=(6,13).
$$

Its arguments are:

$$
a=(15+11)\bmod2=0,
$$

$$
g=\gcd(163,584)=1,\qquad \mu(g)=+1,
$$

$$
s=292+346=638=2\cdot11\cdot29,\qquad \mu(s)=-1.
$$

Thus:

$$
\boxed{\text{If a next original source follows, its radius is predicted EVEN.}}
$$

The geometric rules already predict **NW–SE**, an **odd-row/even-column** center and **equal outer rune symbols**. Within that local physical-source pool:

| Filters after YOU | Sources retained | Radii represented |
| :--- | ---: | :--- |
| Reports 04, 07 and 14 | 21 | — |
| Plus this report's parity | **6** | **2, 4, 6** |

The separate exploratory bound `R′≤φ(r_B)+|c_B−c_E|` from the earlier radius audit would give `R′≤4` and leave **5** of those physical sources, with radii **2 or 4**. That upper bound is a different fitted hypothesis; it is not derived from the parity equation and is not required by this report.

The parity prediction itself does not require extending the phase schedule beyond `S=28`. Selecting a transformed key, signature or new plaintext may require additional assumptions. YOU may also be terminal; no successor is assumed to exist.

## 11. Evidence assessment and practical use

The strongest verified result is **a concise current-state formula that fits every selected next-radius parity and removes nearly half of the stated remaining source candidates**. It is also the only exact expression in the explicitly defined 4,608-variant family.

The principal limitations concern discovery and validation:

- The formula was found on the route it fits. The proposed plaintext and source assignments are not an independent validation set.
- The broad search admits other exact expressions, according to the archived report; its shuffle evidence is inconsistent and was not reproducible from the retrieved script.
- The equation uses coordinates only. It does not by itself authenticate the rune arrangement or the English reading; the relationship between those coordinates and rune-based source selection requires separate evidence.
- No derivation from the decryption mechanism explains why these particular rotations, anchors and opposite Möbius signs should govern the next radius.

For continued exploration, keep the formula fixed and record its forecast **before choosing the next source or reading**. Retain a comparison search without it so that a failing but otherwise supported continuation is visible. A genuinely new source established without using this parity condition would provide a meaningful test.

**Assessment: a useful and locally distinctive research filter, with unestablished global uniqueness and unestablished evidence of intentional design.**

## 12. Verification and source scope

This report independently parsed the **attached** project archive:

```text
Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption-main(20261107-135538).zip
SHA-256:
d4d4ff04ec907c895643efbbae490d811bd1a4528db7d13acba4c4f08a9c7e4f
```

The parsed `0-2-live-map.html` has SHA-256:

```text
80c83b6a18a110150a47b6f010b85504bc2bee94d10a35b6ec340934d1b500d7
```

The attached snapshot predates the archive named in the saved radius audit. Nevertheless, recomputation reproduced **every one of its 33 radius/parity rows and every per-transition source count** used in Section 7.

Parsing retained the documented corrections:

1. Block 09 OF ciphertext is `(18,15)→(18,16)`; the extra shared-node annotation at `(19,16)` is not a ciphertext endpoint.
2. Block 17 THEN reads `(25,25)→(25,26)→(25,27)`; the HTML lacks the usual order tags.
3. SOON uses the original `L–C–EA` source centered at `(25,7)`, as in Report 14. The three documented source alternatives were checked separately.

The audit checked all 729 cells and all four rotation-index maps, verified the Möbius implementation against an independent prime sieve for 1…1458, regenerated all 14,976 physical source geometries, and recomputed incoming Reports 04/07/14 on all 33 transitions.

The documented route makes **105 ciphertext rune uses across 94 distinct matrix cells**. These counts describe the selected reconstruction, not independent evidence that the remaining matrix has been decrypted.

The implementation in Section 4 was executed against all 33 transitions and both source orders. The 4,608-variant family was enumerated exhaustively as defined in Section 9.

**Research and verification date:** 8 November 2026.

## Appendix: complete current-input trace

These are the inputs needed to reproduce every parity prediction without inferring coordinates from the proposed words. The comparison radii and integer arguments appear in Section 6. For a source center M and the canonical outer cell Z, the other outer cell is `2M−Z`.

| Current block | M | Z | B | E | L |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 01 — AS I GO, THE | (13,12) | (13,13) | (13,25) | (14,4) | (14,1) |
| 02 — WEATHER | (14,5) | (14,6) | (14,14) | (14,18) | (14,14) |
| 03 — TURNS | (14,23) | (24,23) | (14,19) | (10,19) | (14,19) |
| 04 — COLD | (26,19) | (27,19) | (14,7) | (11,7) | (14,7) |
| 05 — I MAY | (15,8) | (17,8) | (26,19) | (26,16) | (26,16) |
| 06 — CRY | (25,16) | (26,16) | (19,16) | (17,16) | (19,16) |
| 07 — NOW THE | (19,16) | (20,16) | (11,16) | (15,20) | (11,16) |
| 08 — IDEA | (11,16) | (14,19) | (15,20) | (17,18) | (17,18) |
| 09 — OF | (17,18) | (19,16) | (18,15) | (18,16) | (18,15) |
| 10 — THE | (19,16) | (20,16) | (19,17) | (19,16) | (19,16) |
| 11 — END | (23,12) | (27,8) | (19,23) | (21,23) | (21,23) |
| 12 — IS | (21,22) | (21,27) | (21,9) | (21,10) | (21,9) |
| 13 — DEATH | (23,12) | (27,8) | (26,3) | (26,1) | (26,1) |
| 14 — SEE | (25,6) | (25,10) | (25,16) | (27,14) | (27,14) |
| 15 — YOU | (16,16) | (27,16) | (27,18) | (25,16) | (25,16) |
| 16 — SOON | (25,7) | (25,10) | (25,16) | (25,19) | (25,16) |
| 17 — THEN | (26,22) | (27,22) | (25,25) | (25,27) | (25,25) |
| 18 — THE | (20,17) | (23,17) | (22,21) | (21,20) | (21,20) |
| 19 — KEY | (12,16) | (13,16) | (21,4) | (19,4) | (21,4) |
| 20 — IS | (17,9) | (17,15) | (18,7) | (19,6) | (19,6) |
| 21 — TO | (8,25) | (11,25) | (9,16) | (8,17) | (9,16) |
| 22 — GO | (12,14) | (19,14) | (9,20) | (9,21) | (9,20) |
| 23 — TO | (17,17) | (23,23) | (12,23) | (12,22) | (12,22) |
| 24 — THE | (14,4) | (17,4) | (9,19) | (9,18) | (9,18) |
| 25 — EAST | (13,17) | (20,24) | (14,24) | (16,22) | (16,22) |
| 26 — OF | (19,26) | (20,25) | (6,12) | (7,13) | (6,12) |
| 27 — THE | (24,1) | (25,1) | (20,12) | (20,13) | (20,12) |
| 28 — MAPLIFE | (16,9) | (17,9) | (19,11) | (13,17) | (19,11) |
| 29 — MAY | (14,13) | (17,13) | (18,11) | (18,13) | (18,11) |
| 30 — BE | (20,9) | (26,3) | (25,12) | (26,11) | (26,11) |
| 31 — THE | (10,20) | (14,16) | (11,11) | (11,12) | (11,11) |
| 32 — DEATH | (14,7) | (14,13) | (10,10) | (12,8) | (12,8) |
| 33 — OF | (9,17) | (9,21) | (12,18) | (12,17) | (12,17) |

**Related reports:** [00 — Decryption method](00-decryption-method.md) · [04 — Next-key center parity](04-predicting-next-key-center-parity.md) · [07 — Next-key mirror status](07-predicting-next-key-mirror-status.md) · [14 — Exact next-key axis](14-predicting-exact-next-key-axis.md).

