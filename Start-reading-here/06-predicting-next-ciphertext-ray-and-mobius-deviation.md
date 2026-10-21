# Predicting the Next Ciphertext's Ray and Möbius-Gated Deviation

**A Ciphertext-to-Ciphertext Geometry Report**

*27 × 27 matrix · Leftmost-cell rays · 0° and 270° Möbius tests · One-cell deviations · SEE / YOU mirror geometry*

---

The earlier reports explain how the recorded reading of *Liber Primus* LP2, pages 0–2, predicts the next key's signature, the next ciphertext's reading axis and direction, and certain coordinate parities. This report investigates a different question: **does the current ciphertext constrain the position at which the next ciphertext begins?**

The central observation is geometric. Draw the eight horizontal, vertical, and diagonal rays from the **leftmost cell of the current ciphertext**. On the 16 recorded transitions, the beginning of the next ciphertext always lies **on one of those rays or at most one grid cell off it**. A new conditional version is more restrictive: **the one-cell allowance is enabled only when the current ciphertext's ending cell has Möbius value zero in both the original indexing and the project's 270° rotated indexing**.

This conditional rule preserves **16/16 recorded transitions**. Of the 16, twelve are exact ray alignments and four have a one-cell deviation. All four deviations occur under the double-zero Möbius condition. There is one especially revealing fifth double-zero case, **SEE → YOU**, which takes an exact ray instead of using the permitted deviation. Its two ciphertext paths form an exact reversed mirror pair about column 16.

**Status:** this is an empirical fit to a *research reconstruction* of 17 ciphertext blocks, **not an independently authenticated LP2 plaintext or a proven Cicada 3301 traversal rule**. The formula does not yet determine the next ray, movement length, key, or word uniquely.

**Contents**

[01. Foundations](#foundations) · [02. The eight-ray observation](#the-eight-ray-observation) · [03. The Möbius-gated rule](#the-möbius-gated-rule) · [04. Verification of all 16 transitions](#verification-of-all-16-transitions) · [05. The four one-cell cases](#the-four-one-cell-cases) · [06. The special SEE → YOU geometry](#the-special-see--you-geometry) · [07. Selectivity and rarity](#selectivity-and-rarity) · [08. Conditional test after THEN](#conditional-test-after-then) · [09. Interpretation and limitations](#interpretation-and-limitations) · [Formula reference](#formula-reference)

---

## Foundations

### Coordinates and the three relevant ciphertext cells

The matrix uses **one-based** coordinates `(row, column)`: `(1,1)` is the upper-left cell; rows increase downward and columns increase rightward.

For two consecutive ciphertext blocks, define:

| Symbol | Meaning |
|---|---|
| **L** | **Leftmost cell of the current ciphertext**, chosen by minimum column; if there is a tie, choose the bottommost cell. It is a geometric anchor and need not be the first cell read. |
| **E** | **Endpoint of the current ciphertext**: the last cell in reading order. |
| **B′** | **Beginning of the next ciphertext**: its first cell in reading order. |
| **μ(n)** | Ordinary Möbius function: `0` when a prime square divides `n`, otherwise `+1` or `−1`. |
| **n₀(X)** | Absolute row-major index of cell `X` in the unrotated matrix. |
| **n₃(X)** | Absolute index of the same cell under the project's 270° rotation convention. |

**L, E, and B′ are not interchangeable.** The proposed transition is specifically **`L(current) → B(next)`**, while the numerical condition is evaluated at **`E(current)`**.

### Absolute indexing and rotation

For any `(r,c)`:

$$
n_0(r,c)=27(r-1)+c.
$$

The project's 270° indexing convention gives:

$$
\boxed{n_3(r,c)=27(27-c)+r.}
$$

Both indices lie between **1 and 729**. The rotation affects the **number used by μ**; it does not move the actual ciphertext inside the original matrix.

For background on the special status of leftmost cells and rotational indexing, see [Report 02 — The Leftmost Cell and Rotations](02-leftmost-cell-and-rotations.md).

---

## The Eight-Ray Observation

### One anchor, eight possible directions

From the current leftmost cell `L`, draw the eight compass rays:

```text
  NW     N     NE
     \   |   /
  W ---- L ---- E
     /   |   \
  SW     S     SE
```

These are not eight selected points, but **eight entire rays extending across the grid**. Therefore a distant cell can still lie on a ray exactly; the observation is not a rule favoring nearby ciphertexts.

Let `Δr = r(B′) − r(L)` and `Δc = c(B′) − c(L)`. The integer-grid deviation from the closest of the eight ray directions is:

$$
\boxed{d_8(L,B')=\min\left(|\Delta r|,|\Delta c|,\bigl||\Delta r|-|\Delta c|\bigr|\right).}
$$

This measures a **grid-cell offset** from the nearest horizontal, vertical, or 45° diagonal line—not Euclidean perpendicular distance. It is zero exactly when the points share a row, share a column, or have equal absolute row/column differences.

### Original observation

Across the 16 recorded transitions:

- **12/16** beginnings lie **exactly** on one of the rays: `d₈ = 0`.
- The remaining **4/16** have **exactly** `d₈ = 1`.
- Thus the simple bound **`d₈(L,B′) ≤ 1`** holds on **16/16** transitions.

The sequence of deviations, in reading order, is:

```text
0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0
```

This alone is not deterministic: it allows a one-cell offset at every transition. The next section examines whether that allowance can be decided from an already-known property of the current ciphertext.

---

## The Möbius-Gated Rule

### A conditional allowance from the previous endpoint

Evaluate **two Möbius values at the current endpoint `E`**:

$$
\mu\bigl(n_0(E)\bigr),\qquad \mu\bigl(n_3(E)\bigr).
$$

Define a binary allowance `q(E)`:

$$
\boxed{
q(E)=
\begin{cases}
1,&\mu(n_0(E))=0\ \text{and}\ \mu(n_3(E))=0,\\
0,&\text{otherwise}.
\end{cases}
}
$$

The proposed **Möbius-gated ray rule** is:

$$
\boxed{d_8\bigl(L_i,B_{i+1}\bigr)\le q(E_i).}
$$

Its practical interpretation is simple:

| Current endpoint's Möbius state | Allowed next beginning |
|---|---|
| At least one of `μ(n₀(E))`, `μ(n₃(E))` is nonzero | Must be **exactly on a ray**: `d₈ = 0`. |
| Both values are zero | May be on a ray **or one cell off**: `d₈ ≤ 1`. |

The condition is a **permission**, not an instruction to shift. A double zero does **not** entail `d₈ = 1`; `SEE → YOU` is the explicit counterexample.

This rule uses only cells from the already-read ciphertext to decide the *allowed deviation*. It still requires a proposed `B′` to test whether that location satisfies the inequality.

---

## Verification of All 16 Transitions

The following table uses the recorded 17-block reconstruction, with the **current leftmost cell** as anchor, the **current endpoint** for the Möbius gate, and the **next ciphertext beginning** as the target.

| # | Recorded transition | Current L | Next B′ | `d₈` | `μ(n₀(E)), μ(n₃(E))` | `q` | Pass |
|---:|---|---|---|---:|:---:|---:|:---:|
| 1 | AS I GO THE → WEATHER | `(14,1)` | `(14,14)` | 0 | `+1, +1` | 0 | ✓ |
| 2 | WEATHER → TURNS | `(14,14)` | `(14,19)` | 0 | `0, −1` | 0 | ✓ |
| 3 | TURNS → COLD | `(14,19)` | `(14,7)` | 0 | `+1, +1` | 0 | ✓ |
| 4 | COLD → I MAY | `(14,7)` | `(26,19)` | 0 | `−1, +1` | 0 | ✓ |
| 5 | I MAY → CRY | `(26,16)` | `(19,16)` | 0 | `−1, +1` | 0 | ✓ |
| 6 | CRY → NOW THE | `(19,16)` | `(11,16)` | 0 | `0, +1` | 0 | ✓ |
| 7 | NOW THE → IDEA | `(11,16)` | `(15,20)` | 0 | `+1, 0` | 0 | ✓ |
| **8** | **IDEA → OF** | `(17,18)` | `(18,15)` | **1** | **`0, 0`** | **1** | **✓** |
| **9** | **OF → THE** | `(18,15)` | `(19,17)` | **1** | **`0, 0`** | **1** | **✓** |
| 10 | THE → END | `(19,16)` | `(19,23)` | 0 | `+1, 0` | 0 | ✓ |
| 11 | END → IS | `(21,23)` | `(21,9)` | 0 | `−1, +1` | 0 | ✓ |
| **12** | **IS → DEATH** | `(21,9)` | `(26,3)` | **1** | **`0, 0`** | **1** | **✓** |
| **13** | **DEATH → SEE** | `(26,1)` | `(25,16)` | **1** | **`0, 0`** | **1** | **✓** |
| **14** | **SEE → YOU** | `(27,14)` | `(27,18)` | **0** | **`0, 0`** | **1** | **✓** |
| 15 | YOU → SOON | `(25,16)` | `(25,16)` | 0 | `0, −1` | 0 | ✓ |
| 16 | SOON → THEN | `(25,16)` | `(25,25)` | 0 | `+1, −1` | 0 | ✓ |

**Summary:** **16/16 pass**. The gate equals `1` for **five** transitions; four actually deviate by one cell, while one (`SEE → YOU`) still uses an exact ray. The other **11** transitions have `q=0` and all lie exactly on a ray.

This is a constraint on the *recorded locations*, not 16 uniquely predicted next ciphertexts.

---

## The Four One-Cell Cases

The four deviations occur in two consecutive pairs: **IDEA → OF → THE** and **IS → DEATH → SEE**. For each, both absolute endpoint indices have a squared prime factor, so their Möbius values vanish.

| Transition | Current endpoint E | `n₀(E)` | `n₃(E)` | Möbius pair | `d₈` |
|---|---|---:|---:|:---:|---:|
| IDEA → OF | `(17,18)` | 450 | 260 | `(0,0)` | 1 |
| OF → THE | `(18,16)` | 475 | 315 | `(0,0)` | 1 |
| IS → DEATH | `(21,10)` | 550 | 480 | `(0,0)` | 1 |
| DEATH → SEE | `(26,1)` | 676 | 728 | `(0,0)` | 1 |

The zeros can be checked directly:

$$
\begin{aligned}
450&=2\cdot 3^2\cdot5^2, &260&=2^2\cdot5\cdot13,\\
475&=5^2\cdot19, &315&=3^2\cdot5\cdot7,\\
550&=2\cdot5^2\cdot11, &480&=2^5\cdot3\cdot5,\\
676&=26^2, &728&=2^3\cdot7\cdot13.
\end{aligned}
$$

### Example — IDEA → OF

`L_IDEA = (17,18)` and `B_OF = (18,15)`, so:

$$
(\Delta r,\Delta c)=(+1,-3),\quad
 d_8=\min(1,3,2)=1.
$$

The previous endpoint is also `(17,18)`; its indices are **450 and 260**, both with μ=0. Thus `q=1` and the offset passes.

### Example — OF → THE

`L_OF = (18,15)` and `B_THE = (19,17)` give:

$$
(\Delta r,\Delta c)=(+1,+2),\quad
 d_8=\min(1,2,1)=1.
$$

Here the endpoint is `E_OF = (18,16)` rather than `L_OF`. Its indices **475** and **315** again have μ=0, enabling the offset.

### Why these four matter

A blanket `±1` rule would admit off-ray positions for every step. The two-zero condition identifies **exactly the five current endpoints** on the recorded route where such a deviation is allowed. **All four observed deviations occur among those five**.

It does **not** explain *which side* of a ray to use, *which ray* to follow, or *how far* to travel.

---

## The Special SEE → YOU Geometry

### The one double-zero case with no deviation

For the recorded `SEE` block:

- Reading path: `(25,16) → (26,15) → (27,14)`.
- Leftmost cell and endpoint: `L_SEE = E_SEE = (27,14)`.

For the following `YOU` block:

- Reading path: `(27,18) → (26,17) → (25,16)`.
- Beginning: `B_YOU = (27,18)`.

Thus:

$$
(\Delta r,\Delta c)=(0,+4),\qquad
\boxed{d_8(L_{\mathrm{SEE}},B_{\mathrm{YOU}})=0}.
$$

Nevertheless the previous endpoint satisfies the double-zero gate:

$$
\begin{aligned}
n_0(27,14)&=716=2^2\cdot179,\\
n_3(27,14)&=378=2\cdot3^3\cdot7,\\
\mu(716)&=\mu(378)=0,\quad q=1.
\end{aligned}
$$

**Interpretation:** `SEE → YOU` does not violate the inequality. It disproves the stronger, unwarranted claim that `d₈` must *equal* `q`. The gate permits one-cell deviation; it does not require it.

### An exact reflection with reversed reading order

The two entire three-cell ciphertext paths are mirror images across **column 16**, if `YOU` is listed in reverse reading order:

$$
\boxed{R(r,c)=(r,32-c).}
$$

| SEE, in reading order | Reflection `R(SEE)` | YOU, in reverse reading order |
|---|---|---|
| `(25,16)` | `(25,16)` | `(25,16)` |
| `(26,15)` | `(26,17)` | `(26,17)` |
| `(27,14)` | `(27,18)` | `(27,18)` |

The matching covers **all three cells**, not merely an aligned endpoint.

```text
                  column 16 (mirror axis)
                         |
 row 25:                 ●  = SEE begins / YOU ends
                        / \
 row 26:         SEE  ●     ●  YOU
                      /       \
 row 27:         SEE ●         ● YOU begins

              SEE is read downward-left.
              YOU is read upward-left.
```

The common cell **`(25,16)`** is also the beginning of the later `SOON` ciphertext: a three-block reuse of the same matrix position (`SEE` beginning, `YOU` ending, `SOON` beginning).

This is a **local geometric explanation** for the exact ray alignment despite `q=1`: the selected `YOU` path returns through a reflected copy of `SEE`. There is not yet a general rule that predicts when the mirrored-return construction must be used.

Within the **17 recorded blocks**, `SEE → YOU` was the **only** anchored full-path reflection/reversal of this kind found when comparing equal-length ordered pairs and the four grid-reflection directions. This is descriptive uniqueness within the reconstruction, not a probability that Cicada deliberately placed it there.

### A second exact relationship: the index 720

Report 03 uses the intermediate quantity:

$$
A=n_2(B_{\mathrm{current}})+n_0(M_{\mathrm{current}}),
$$

where `B_current` is the current ciphertext beginning and `M_current` the center of the current **original** key node.

For `SEE`:

$$
\begin{aligned}
B_{\mathrm{SEE}}&=(25,16),\\
n_0(B_{\mathrm{SEE}})&=664,\\
n_2(B_{\mathrm{SEE}})&=730-664=66,\\
M_{\mathrm{SEE}}&=(25,6),\\
n_0(M_{\mathrm{SEE}})&=654.
\end{aligned}
$$

Therefore:

$$
\boxed{A=66+654=720=n_0(27,18)=n_0(B_{\mathrm{YOU}}).}
$$

This equality was unique among the 16 recorded transitions. **It is not a universal coordinate formula**: the same intermediate quantity does not identify next beginnings elsewhere and may fall outside the valid cell-index range.

The `720` equality and mirrored geometry reference the **same selected beginning** of `YOU`; they should not be treated as statistically independent discoveries.

### Cryptographically constrained YOU alternatives

A previous enumeration held fixed the **known next plaintext `YOU`**, its reading orientation, admissible key signatures, and the leftmost-cell Möbius class:

| Test | Number of placements |
|---|---:|
| Placements capable of decrypting to `YOU` | 37 |
| Pass the Möbius-gated ray from `SEE` | 11 |
| Exactly on a ray (`d₈=0`) | 6 |
| Exact anchored mirror/reversal of `SEE` | **1** |

The mirror is therefore a selective additional feature **within this word-conditioned set**. This does not show that the next plaintext could have been predicted to be `YOU` before knowing the word.

---

## Selectivity and Rarity

### Double-zero cells are not inherently rare

Across all **729** cells of the 27 × 27 grid, **142** have both `μ(n₀)=0` and `μ(n₃)=0`—approximately **19.48%**.

What is unusual in the selected route is **not** the occurrence of double zeros by itself. It is the alignment between those zeros and **all four** of the observed one-cell deviations.

### Comparison of rotational pairs

There are six unordered pairs from the four rotations `0°`, `90°`, `180°`, and `270°`. Of those six pairs, **only `(0°,270°)` covers all four recorded `d₈=1` transitions** when both Möbius values are required to be zero.

In a *restricted conditional test*, keeping the same 16 endpoint positions and randomly reassigning which four steps have unit deviations:

| Assumption in the restricted test | Conditional frequency |
|---|---:|
| The `(0°,270°)` pair is fixed before examining deviations | `5 / C(16,4) ≈ 0.275%` |
| Choose the best of the six rotation pairs | `12 / C(16,4) ≈ 0.659%` |
| Choose among 24 tested anchor/rotation-pair definitions | `33 / C(16,4) ≈ 1.813%` |

**These are not fully corrected p-values for an authentic Cicada mechanism.** The formulas were found after examining the route, and the controls do not account for every explored geometric function, rune-key constraint, plaintext choice, or route-selection decision.

### How much does the filter actually eliminate?

Two complementary baselines were previously computed:

| Candidate placement baseline | Always allow `d₈≤1` | Möbius-gated `d₈≤q(E)` |
|---|---:|---:|
| Geometry-only placements preserving the next block's length, direction, and leftmost μ class | 33.3% pass | **18.3% pass** |
| Placements additionally capable of producing the **already-known next plaintext** with an admissible key | 53.2% pass | **48.8% pass** |

The new gate is noticeably more selective spatially, but only modestly more selective **when the correct next word is already imposed**.

An important negative result: in this particular **word-conditioned** 16-transition test, the simpler requirement `μ(n₀(E))=0` alone gave the **same candidate counts** as the two-zero gate. The 270° test improves the broader spatial control, but its incremental cryptographic benefit has **not** been established on the selected words.

### Choice of anchor matters

Using the **same endpoint-derived gate**, but changing the ray origin while keeping the recorded next beginning:

| Ray origin | Matches among 16 |
|---|---:|
| **Current leftmost cell L** | **16/16** |
| Current endpoint E | 13/16 |
| Current beginning B | 12/16 |
| Current original key-node center M | 10/16 |

This supports investigating the **leftmost cell as a distinguished geometric anchor**. The comparison is also retrospective, so it should not be taken as a proof that the anchor was uniquely determined by the historical cipher design.

---

## Conditional Test After THEN

The next step of the candidate route is not independently authenticated. Nevertheless, the new rule can be calculated **before choosing a next word**.

For recorded `THEN`:

$$
L_{\mathrm{THEN}}=(25,25),\qquad E_{\mathrm{THEN}}=(25,27).
$$

The current endpoint has:

$$
\begin{aligned}
n_0(25,27)&=675, &\mu(675)&=0,\\
n_3(25,27)&=25, &\mu(25)&=0.
\end{aligned}
$$

Consequently **`q(THEN)=1`**, and the next ciphertext beginning may be on a ray or one grid cell away.

The proposed `THE` ciphertext starts at **`(24,27)`** and continues to `(23,26)`. Relative to `L_THEN=(25,25)`:

$$
(\Delta r,\Delta c)=(-1,+2),\qquad
\boxed{d_8=1\le q=1.}
$$

So the **candidate `THEN → THE` passes**. It also starts one cell directly above the endpoint of `THEN`, `(25,27)`, but that separate endpoint-to-start alignment is observed on only part of the historical route and is **not** part of the universal 16/16 inequality.

For the proposed `THE` endpoint `(23,26)`, both `n₀=620` and `n₃=50` have Möbius value zero. The rule therefore also **permits**, but does not select, a one-cell deviation for the following transition. One previously considered `SEA` placement starts at `(20,27)` and satisfies this bound.

**Crucially, the ray inequality does not make `THE` unique.** A previous geometric count, even after fixing a two-rune up-left reading path, a particular next-leftmost μ class, and an endpoint-row parity, still found **84 candidate starts** passing the Möbius-gated ray after `THEN`. Those 84 are geometric placements under the stated assumptions, not 84 verified correct plaintexts.

---

## Interpretation and Limitations

### What is established for the recorded reconstruction

1. The simple geometric statement **`d₈(L,B′)≤1` holds on all 16 transitions**: twelve exact rays, four one-cell offsets.
2. A more restrictive, endpoint-dependent rule **`d₈(L,B′)≤q(E)` also holds on all 16**.
3. **All four unit offsets** are among the **five current endpoints** having `μ(n₀(E))=μ(n₃(E))=0`.
4. The remaining double-zero case, **`SEE → YOU`**, has an exact **full-path reflection and reversed reading order** around column 16.
5. The previously used axis calculation gives a distinctive local equality **`A=720=n₀(B_YOU)`**, but not a general next-position formula.

### What remains a hypothesis

- A **double zero may enable** a sideways one-cell move; it does **not require** one. `SEE → YOU` is decisive on this point.
- The **direction of the ray**, **distance traveled**, and **sign/side of the one-cell offset** are not predicted by this rule.
- It does not determine the next **full key**, **ciphertext**, or **plaintext** from previous-block data alone.
- The mirror arrangement of `SEE → YOU` has no independently validated **universal switching condition**.
- The results are **retrospective fits** to a reconstructed route; selection of both plaintexts and rules introduces a potentially large multiple-testing effect.

A more elaborate condition involving the 180° Möbius value separates `d₈=0` from `d₈=1` perfectly on these 16 examples, but excludes the proposed `THEN → THE` move. That is a useful warning: **a sharper fit to the historical sample can be a worse predictive rule**.

The most informative next test would fix the gate and any additional direction/distance formula **before evaluating a new, independently supported ciphertext transition**. Successful prediction of the actual next beginning—and preferably its key and plaintext—would provide much stronger evidence than another retrospective 16/16 match.

---

## Formula Reference

| Object | Formula / definition |
|---|---|
| Absolute original index | `n₀(r,c) = 27(r−1)+c` |
| Absolute 270° index | `n₃(r,c) = 27(27−c)+r` |
| Leftmost cell `L` | Occupied cell of minimal column; bottommost in a tie |
| Previous endpoint `E` | Last cell of current ciphertext in reading order |
| Next beginning `B′` | First cell of next ciphertext in reading order |
| Relative movement | `Δr=r(B′)−r(L)`, `Δc=c(B′)−c(L)` |
| Eight-ray grid deviation | `d₈=min(|Δr|, |Δc|, ||Δr|−|Δc||)` |
| Double-zero Möbius gate | `q(E)=1` iff `μ(n₀(E))=μ(n₃(E))=0`; otherwise `0` |
| **Proposed transition filter** | **`d₈(L,B′) ≤ q(E)`** |
| Recorded verification | **16/16**, consisting of **12 exact** and **4 unit-offset** transitions |

### Related project reports

- [00 — The 27 × 27 Matrix / Decryption Method](00-decryption-method.md)
- [01 — Predicting the Next Key](01-next-key-signature.md)
- [02 — The Leftmost Cell and Rotations](02-leftmost-cell-and-rotations.md)
- [03 — Predicting the Next Ciphertext's Axis and Reading Direction](03-predicting-axis-and-reading-direction.md)
- [05 — Predicting the Next Ciphertext's Row Parity](05-predicting-next-ciphertext-row-parity.md)

**Data provenance:** recorded coordinate path from the LP2 0–2 project research; independently recalculated ray deviations and endpoint Möbius values against `LP2_mobius_ray_all_16.csv`; comparative statistics and `SEE → YOU` checks from the reproducible analysis accompanying `LP2_mobius_gated_ray_report.md` and `LP2_SEE_YOU_mobius_rarity_audit.md` (21 October 2026). All 16 transitions are observations from the **selected route**, not independently verified plaintext blocks.
