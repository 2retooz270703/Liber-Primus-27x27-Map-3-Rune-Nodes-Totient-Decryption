# Predicting the Next Key-Node Axis Group

**Status: retrospective candidate filter; 33/33 agreement with the selected 34-block route.** The proposed formula predicts one bit of the next **original key node's** undirected axis. It adds a restriction to the earlier filters and reduces the number of distinct decrypted rune strings. Its agreement with the recorded route has been reproduced, but its place in Cicada 3301's intended method remains unestablished.

## 1. What is new?

The earlier reports constrain the next key's signature, phase, center parity, and mirror status, together with several properties of the next ciphertext. In particular, [Report 03](03-predicting-axis-and-reading-direction.md) predicts the **ciphertext's** axis and reading boundary.

The present proposal concerns a different object: the three equally spaced cells of the **original source node from which the next key is derived**. Before applying a center transformation or cyclic key rotation, that node lies on one of four undirected axes:

| Axis number | Original key-node axis | Predicted bit b |
| ---: | --- | :---: |
| 0 | Horizontal, W–E | 0 |
| 1 | Diagonal, NW–SE | 0 |
| 2 | Vertical, N–S | 1 |
| 3 | Diagonal, NE–SW | 1 |

The formula chooses **one of these two groups**, leaving two possible axes. It does not select a complete axis, source position, radius, or plaintext word.

## 2. Coordinates and inputs

Use the project's **27 × 27** matrix with 1-based `(row, column)` coordinates. Rows increase downward; columns increase to the right.

All three inputs belong to the **current** block:

| Symbol | Meaning |
| --- | --- |
| M | Center of the current original three-rune key node |
| Z | Lower outer cell of that node; for a horizontal node, the right outer cell |
| L | Leftmost current ciphertext cell: smallest column, bottommost on ties |

These are geometric definitions. Reversing the recorded order of the same physical source node does not change M or Z. Likewise, L need not be the first ciphertext cell read.

Let the absolute row-major cell indices at 0°, 90°, and 180° clockwise rotation be

$$
n_0(r,c)=27(r-1)+c,
$$

$$
n_1(r,c)=27(c-1)+28-r,
\qquad
n_2(r,c)=730-n_0(r,c).
$$

Here `n₁` and `n₂` are indices of the same original cell after rotating its coordinates. They do not designate additional locations from which runes are read.

## 3. Proposed rule

Calculate

$$
\boxed{X=n_1(M)+n_2(Z),\qquad Y=n_1(L)+n_2(Z).}
$$

Then compare **whether the two Möbius values are negative**:

| Comparison of μ(X) and μ(Y) | Permitted next original key-node axes |
| --- | --- |
| Both negative, or both nonnegative | **Vertical or NE–SW** |
| Exactly one negative | **Horizontal or NW–SE** |

**Zero is nonnegative.** This is a test of `μ < 0`, not merely of squarefreeness or equality of the two Möbius values. For example, `μ(X)=0` and `μ(Y)=+1` belong to the same nonnegative class.

Writing

$$
\chi(n)=\mathbf1[\mu(n)<0],
$$

the predicted bit is

$$
\boxed{b_{i+1}=1\oplus\chi(X)\oplus\chi(Y).}
$$

The symbol `⊕` denotes addition modulo 2. Equivalently, `b = 1` when the two negativity indicators agree, and `b = 0` when they differ.

The inputs are only M, Z, and L from the current block. The formula uses no following plaintext, next-block length, next key values, block number, or accumulated phase S. Its Möbius arguments are positive integers in the range 2…1458.

### Direct implementation

The supplied `mu` function must evaluate the Möbius function on positive integers.

```python
def expected_next_key_axis_group(current_node, current_cipher_cells, mu):
    """0: H or NW-SE; 1: V or NE-SW. Coordinates are 1-based."""
    M = current_node[1]
    Z = max(current_node, key=lambda cell: (cell[0], cell[1]))
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))

    def n90(cell):
        r, c = cell
        return 27 * (c - 1) + 28 - r

    def n180(cell):
        r, c = cell
        return 730 - (27 * (r - 1) + c)

    X = n90(M) + n180(Z)
    Y = n90(L) + n180(Z)
    return int((mu(X) < 0) == (mu(Y) < 0))


def original_key_axis_group(node):
    """For a valid, nondegenerate three-cell node on one of the four axes."""
    dr = node[-1][0] - node[0][0]
    dc = node[-1][1] - node[0][1]
    return int(dr != 0 and dr * dc <= 0)


# Keep a proposed next source only if:
# original_key_axis_group(next_node) == expected_next_key_axis_group(
#     current_node, current_cipher_cells, mu
# )
```

## 4. Worked example: THEN (17) → THE (18)

For the recorded THEN block:

$$
M=(26,22),\qquad Z=(27,22),\qquad L=(25,25).
$$

The rotated indices are

$$
n_1(M)=569,\qquad n_2(Z)=6,\qquad n_1(L)=651.
$$

Consequently,

$$
X=575=5^2\cdot23,\qquad Y=657=3^2\cdot73.
$$

Both Möbius values are zero, so both are **nonnegative**. The rule predicts a **vertical or NE–SW** source for the next key.

The recorded source for THE (18), `(17,17)–(20,17)–(23,17)`, is vertical and satisfies that prediction. The zero–zero case therefore belongs to the V / NE–SW group.

## 5. Agreement across the recorded route

The selected route has **34 blocks, 105 plaintext runes, and 33 transitions**. The formula agrees with the next recorded source's axis group in every transition. The complete numerical trace is included in the appendix.

All nine possible pairs of Möbius values occur:

| μ(X) | μ(Y) | Predicted group | Transitions |
| ---: | ---: | --- | ---: |
| −1 | −1 | V / NE–SW | 3 |
| −1 | 0 | H / NW–SE | 4 |
| −1 | +1 | H / NW–SE | 4 |
| 0 | −1 | H / NW–SE | 1 |
| 0 | 0 | V / NE–SW | 5 |
| 0 | +1 | V / NE–SW | 2 |
| +1 | −1 | H / NW–SE | 2 |
| +1 | 0 | V / NE–SW | 5 |
| +1 | +1 | V / NE–SW | 7 |

Independent integer factorization reproduced the Möbius values for every integer from 1 through 1458. All **132 combinations of reversing the current and next source orders** across the 33 transitions gave the same result.

In every one of the 33 local searches, **both axis groups remain possible after the earlier filters and their continuation check**. The new rule therefore removes alternatives at every position; it does not simply restate a bit already forced there.

## 6. Candidate reduction and plaintext effect

The comparison uses the previous audit's search domain:

- **10,891 source-and-operation assignments**, using a canonical source order;
- equally spaced three-cell nodes on the four axes, with nonzero rune indices;
- either the original center or its Euler-totient transformation, with duplicate identical operations omitted;
- **62,712 directed straight ciphertext blocks** of length 2…27;
- the incoming constraints of Reports 01–11.

The baseline also requires each proposed next assignment to admit at least one further assignment under the earlier model. No next word or prescribed next-block length is used in this local enumeration.

The additional ray filter in the table is the exact-deviation proposal from [Report 12](12-predicting-exact-ray-deviation.md), `d₈(L,B′)=q(1−z)`.

| Filters, added to the same baseline | Source + ciphertext assignments | Distinct plaintext rune strings | Ciphertext geometries |
| --- | ---: | ---: | ---: |
| Earlier constraints and earlier continuation check | 952,484 | 735,331 | 10,752 |
| + this key-axis group rule | 499,283 | 428,690 | 10,727 |
| + only Report 12 | 762,553 | 584,146 | 8,913 |
| + both new filters | 397,989 | 341,707 | 8,888 |
| + both, also required in the further-step existence check | 397,436 | 341,199 | 8,888 |

**These are sums of 33 separate local searches with the current recorded block fixed, not counts of complete routes.** Distinct strings are counted once within each local search and then summed. Here *plaintext* means the rune sequence produced by subtraction modulo 29; no English dictionary or language score is applied.

The axis rule alone removes **47.58% of assignments** and **41.70% of distinct rune strings** from the baseline. Its effect therefore extends beyond deleting duplicate sources of the same output. Its main selectivity concerns the key source: the number of possible ciphertext geometries changes only slightly.

Together with Report 12, it removes **58.22% of assignments** and **53.53% of distinct strings**. Requiring a further step that satisfies both new filters removes another **553 assignments**. Every recorded transition survives all rows. These combined results demonstrate compatible pruning, not statistical independence of the filters.

The counts retain the cyclic phase extension of [Report 11](11-seven-thresholds-and-cyclic-phase-modes.md) where needed at or beyond S=28. The axis formula itself does not depend on that extension.

## 7. Alternative sources and complete text-conditioned routes

### THE (10)

For THE **block 10**, the earlier model permits the recorded vertical source centered at **(19,16)** and two center-operation assignments for a diagonal source:

$$
(9,6)\;–\;(11,8)\;–\;(13,10).
$$

The incoming axis prediction is V / NE–SW. It retains the vertical source and excludes both assignments of the NW–SE source. Substituting that diagonal source also makes its outgoing axis prediction disagree with the recorded END source.

This is a selection among sources that produce the same local plaintext, rather than a rejection of an unrelated unreadable candidate.

### Full routes with the proposed plaintext fixed

A separate enumeration fixes the **entire proposed plaintext rune sequence, its division into 34 blocks, and the first recorded assignment**. It allows the following source nodes and ciphertext positions to vary throughout the stated domain. Each transition is evaluated from the candidate state actually reached. No successor is required after the final YOU.

Routes are counted separately when a source, its order, or its center operation differs, even if the resulting text and ciphertext positions coincide.

| Permitted source orders | Earlier model | + axis rule | + only Report 12 | + both |
| --- | ---: | ---: | ---: | ---: |
| Canonical orders only | 3 | 1 | 3 | 1 |
| Including reversed orders: 20,967 source-and-operation assignments | 9 | 2 | 9 | 2 |

All complete surviving routes use the **recorded ciphertext geometries**. The earlier alternatives concern THE (10) and, when reversed orders are allowed, BE (30). After the axis rule, THE's source is resolved, while BE retains two choices:

| BE source in key order | Axis |
| --- | --- |
| `(14,15) → (20,9) → (26,3)` | NE–SW |
| `(24,25) → (16,25) → (8,25)` | Vertical |

The NW–SE source `(27,16) → (20,9) → (13,2)` is excluded on entry.

This establishes improved source selection **conditional on the proposed text and segmentation**. It does not establish that this text is unique among other possible messages. The canonical-order result must also be read alongside the two surviving routes when reversed source orders are admitted.

## 8. Retrospective robustness and selection controls

### A defined family of short geometric formulas

The structural comparison examined expressions of the form

$$
\mathbf1[\mu(n_a(P)+n_b(R))=s]
\oplus
\mathbf1[\mu(n_a(Q)+n_b(R))=s],
$$

where P and Q are different members of `{B,E,L,M,Z,U}`, R is any member of that set, U is the upper/left source arm, a and b are the four rotations, and s is −1, 0, or +1. B and E are the current ciphertext's first and last cells in reading order.

There are **4,320 structural templates**, or **8,640 models including the overall output inversion**, for a fixed binary target. The reported formula is the **only 33/33 model in this family** for the axis-group target. The next-best distinct prediction pattern matches 29/33.

For this target, selection within the same family gives:

| Transitions used to select exact models | Models remaining | Agreement on the rest |
| --- | ---: | ---: |
| First 16 | 1 | 17/17 |
| Last 17 | 1 | 16/16 |
| Odd-numbered transitions | 1 | 16/16 |
| Even-numbered transitions | 1 | 17/17 |
| Any 32, omitting one transition | 1 in each of 33 checks | 1/1 in every check |

With this target fixed, the model is already unique after the first 11 transitions. If the target is also selected among the **three ways of partitioning four axes into two pairs**, ten exact models remain after those 11 transitions; only this model remains after the first 16.

Simple substitutions also change the fit: using B instead of L gives 29/33; E instead of L gives 25/33; the opposite source arm instead of Z gives 19/33. Testing equality of the `μ=0` indicators instead of the `μ<0` indicators gives 20/33; using `μ>0` gives 21/33, with the output convention held fixed.

**These are retrospective robustness checks.** The family and target were investigated after the whole route was available. The remaining 17 transitions are therefore not an independently withheld test. Uniqueness here is limited to the declared family, not to all possible formulas.

### Broader search controls

The broader search considered **2,630 distinct nonconstant binary feature patterns** and **39 binary targets defined on all 33 transitions**. For controls, the current recorded inputs are held fixed, and one assignment is sampled uniformly from the earlier admissible next-assignment pool at each position, after the baseline continuation check. Information is measured as the negative base-2 logarithm of a target pattern's probability under this conditional model.

For the fixed axis-group target, exact summation over the **3,443,431 distinct affine prediction patterns using at most two features, counted up to overall inversion**, gives a conditional probability of **0.07488%** that some model in that class fits exactly. When target selection is included, **218 of 10,000** saved control sets contain a two-feature fit at least as informative as the observed one: **2.18%**.

These reproduce the earlier audit's conditional controls. They account for the declared feature search to the stated extent; they do not reproduce the prior selection of the plaintext, source geometries, or all research choices. They are not probabilities that Cicada designed this rule or that the proposed plaintext is correct.

## 9. A fixed prediction after YOU (34)

The last recorded YOU has

$$
M=(21,22),\qquad Z=(21,27),\qquad L=(6,11).
$$

It gives

$$
X=737=11\cdot67,\quad\mu(X)=+1,
$$

$$
Y=455=5\cdot7\cdot13,\quad\mu(Y)=-1.
$$

Exactly one value is negative. Therefore, **if the route continues**, the next original key node is predicted to be

$$
\boxed{\text{horizontal or NW–SE}.}
$$

Report 12 separately predicts

$$
\boxed{d_8((6,11),B_{35})=1.}
$$

Both constraints can be checked before inspecting a proposed continuation's plaintext. Neither requires extending the phase schedule beyond S=28.

If the cyclic phase extension and other earlier constraints are additionally adopted, the next-block enumeration is:

| Search after YOU | Assignments | Distinct plaintext rune strings |
| --- | ---: | ---: |
| Earlier incoming constraints, without the continuation check | 10,631 | — |
| + axis rule, still without the continuation check | 9,174 | — |
| Earlier constraints and earlier continuation check | 6,916 | 6,352 |
| + axis rule | 5,953 | 5,465 |
| + both new filters | 2,137 | 1,947 |

The final row contains **13 source-and-operation assignments and 325 ciphertext geometries**. Requiring a further step satisfying both new filters leaves it unchanged. A dash means that the distinct-string count was not reported for that row.

**No next word is established.** The remaining rune outputs are alternatives, not recovered English continuations. An ending at the recorded YOU also remains possible.

## 10. Interpretation and audit scope

The result is a compact additional constraint with reproducible agreement and a measured effect on decrypted outputs. Its useful contribution is a previously free bit of source geometry. Complete four-axis selection, radius, exact position, and next-block length remain unresolved by this formula.

The main outstanding test is a transition established on other grounds and evaluated with the formula held fixed. Searches with and without this filter should remain distinguishable so that an incompatible new candidate can be assessed without silently changing the rule.

The audit used the 7 November 2026 project snapshot with SHA-256:

```text
d4d4ff04ec907c895643efbbae490d811bd1a4528db7d13acba4c4f08a9c7e4f
```

The recorded route uses the source for SOON centered at `(25,7)`, as in the preceding full audit. Agreement is conditional on those selected source assignments, with alternatives examined as described above.

The separately distributed `LP2_axis_candidate_deep_check_reproducibility.zip` contains the input archive, the earlier audit data, and the new calculations. With Python 3.10+ and NumPy, `python3 run_reproduction.py` repeats the checks. Key result files are:

- `investigation/independent_trace.json` — the formula's inputs, Möbius values, and predictions;
- `investigation/combined_counts.json` and `combined_totals.json` — local pruning and distinct-output counts;
- `investigation/template_stability.json` — the structural-family and split checks;
- `investigation/literal_route_totals.json` and `literal_route_totals_reversed.json` — complete routes conditional on the proposed text;
- `investigation/after_YOU_sources.json` and `after_YOU_candidates.jsonl` — the remaining next-block assignments.

## Appendix: all 33 recorded transitions

Every recorded next source lies in the predicted group. Block numbers distinguish repeated readings such as THE, OF, and YOU.

| Transition | Current → next reading | X | Y | μ(X) | μ(Y) | Predicted next key group |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 01→02 | AS I GO THE → WEATHER | 705 | 407 | −1 | +1 | H / NW–SE |
| 02→03 | WEATHER → TURNS | 495 | 738 | 0 | 0 | V / NE–SW |
| 03→04 | TURNS → COLD | 694 | 586 | +1 | +1 | V / NE–SW |
| 04→05 | COLD → I MAY | 497 | 185 | +1 | +1 | V / NE–SW |
| 05→06 | I MAY → CRY | 492 | 697 | 0 | +1 | V / NE–SW |
| 06→07 | CRY → NOW THE | 447 | 453 | +1 | +1 | V / NE–SW |
| 07→08 | NOW THE → IDEA | 615 | 623 | −1 | +1 | H / NW–SE |
| 08→09 | IDEA → OF | 782 | 830 | −1 | −1 | V / NE–SW |
| 09→10 | OF → THE | 698 | 616 | +1 | 0 | V / NE–SW |
| 10→11 | THE → END | 615 | 615 | −1 | −1 | V / NE–SW |
| 11→12 | END → IS | 322 | 621 | −1 | 0 | H / NW–SE |
| 12→13 | IS → DEATH | 737 | 386 | +1 | +1 | V / NE–SW |
| 13→14 | DEATH → SEE | 322 | 22 | −1 | +1 | H / NW–SE |
| 14→15 | SEE → YOU | 210 | 424 | +1 | 0 | V / NE–SW |
| 15→16 | YOU → SOON | 429 | 420 | −1 | 0 | H / NW–SE |
| 16→17 | SOON → THEN | 237 | 480 | +1 | 0 | V / NE–SW |
| 17→18 | THEN → THE | 575 | 657 | 0 | 0 | V / NE–SW |
| 18→19 | THE → KEY | 559 | 639 | +1 | 0 | V / NE–SW |
| 19→20 | KEY → IS | 811 | 478 | −1 | +1 | H / NW–SE |
| 20→21 | IS → TO | 510 | 427 | +1 | +1 | V / NE–SW |
| 21→22 | TO → GO | 1103 | 859 | −1 | −1 | V / NE–SW |
| 22→23 | GO → TO | 597 | 762 | +1 | −1 | H / NW–SE |
| 23→24 | TO → THE | 556 | 696 | 0 | 0 | V / NE–SW |
| 24→25 | THE → EAST | 389 | 772 | −1 | 0 | H / NW–SE |
| 25→26 | EAST → OF | 640 | 772 | 0 | 0 | V / NE–SW |
| 26→27 | OF → THE | 876 | 511 | 0 | +1 | V / NE–SW |
| 27→28 | THE → MAP LIFE | 85 | 386 | +1 | +1 | V / NE–SW |
| 28→29 | MAP LIFE → MAY | 517 | 568 | +1 | 0 | V / NE–SW |
| 29→30 | MAY → BE | 623 | 565 | +1 | +1 | V / NE–SW |
| 30→31 | BE → THE | 276 | 324 | 0 | 0 | V / NE–SW |
| 31→32 | THE → DEATH | 894 | 650 | −1 | 0 | H / NW–SE |
| 32→33 | DEATH → OF | 542 | 571 | +1 | −1 | H / NW–SE |
| 33→34 | OF → YOU | 944 | 941 | 0 | −1 | H / NW–SE |

---

**Related reports:** [00 — Decryption method](00-decryption-method.md) · [03 — Ciphertext axis and direction](03-predicting-axis-and-reading-direction.md) · [04 — Key-center parity](04-predicting-next-key-center-parity.md) · [07 — Key mirror status](07-predicting-next-key-mirror-status.md) · [11 — Phase thresholds and cyclic modes](11-seven-thresholds-and-cyclic-phase-modes.md) · [12 — Exact ray deviation](12-predicting-exact-ray-deviation.md).
