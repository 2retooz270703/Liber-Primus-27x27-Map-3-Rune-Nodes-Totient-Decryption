# Predicting the Next Ciphertext’s Ray and Deviation

**Ray alignment and Möbius condition · LP2 pages 0–2**

The current ciphertext’s leftmost cell anchors a position filter for the next beginning. A condition on the current endpoint determines whether a one-cell deviation from an exact ray is allowed.

## 1. Inputs

The matrix has **27 rows and 27 columns**, numbered from 1. Coordinates are `(row, column)`; rows increase downward and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| L | Current leftmost cell: smallest occupied column, bottommost cell in a tie |
| E | Current endpoint: last cell read |
| B′ | Next beginning: first cell read in the next ciphertext |

**The ray starts at L; the numerical condition is evaluated at E.** These cells may differ.

The original and 270° clockwise absolute indices are:

$$
n_0(r,c)=27(r-1)+c,\qquad n_3(r,c)=27(27-c)+r.
$$

Both range from 1 to 729. The Möbius function `μ(n)` is **0** if a prime square divides `n`, and **±1** otherwise. Only the zero/nonzero distinction matters for this filter.

For rotational indexing and leftmost-cell selection, see [Report 02](02-leftmost-cell-and-rotations.md).

## 2. The ray rule

### Measure the offset

From L, consider the eight horizontal, vertical, and 45° diagonal rays. Their length is unrestricted. Define:

$$
\Delta r=r(B')-r(L),\qquad\Delta c=c(B')-c(L),
$$

$$
d_8(L,B')=\min\left(|\Delta r|,|\Delta c|,\bigl||\Delta r|-|\Delta c|\bigr|\right).
$$

This is a **grid-offset score**, not Euclidean distance. It is zero when the cells share a row, column, or 45° diagonal. The anchor itself also qualifies.

### Calculate the allowance

At the current endpoint, test both indices:

$$
q(E)=
\begin{cases}
1,&\mu(n_0(E))=0\ \text{and}\ \mu(n_3(E))=0,\\
0,&\text{otherwise}.
\end{cases}
$$

The proposed filter is:

$$
\boxed{d_8(L,B')\le q(E).}
$$

- **q = 0:** the next beginning must lie exactly on a ray.
- **q = 1:** it may lie on a ray or one cell off it.

**A double zero permits a deviation; it does not require one.** Current-block data determine the allowance, but a proposed B′ is still needed to test its location.

## 3. Check against the recorded route

The table uses the selected 17-block reconstruction. The Möbius pair is evaluated at the **current endpoint**, while the displacement starts at the **current leftmost cell**.

| Transition | Current L | Next B′ | μ(n₀(E)), μ(n₃(E)) | q | d₈ |
| :--- | :--- | :--- | :--- | ---: | ---: |
| AS I GO THE → WEATHER | (14,1) | (14,14) | +1, +1 | 0 | 0 |
| WEATHER → TURNS | (14,14) | (14,19) | 0, −1 | 0 | 0 |
| TURNS → COLD | (14,19) | (14,7) | +1, +1 | 0 | 0 |
| COLD → I MAY | (14,7) | (26,19) | −1, +1 | 0 | 0 |
| I MAY → CRY | (26,16) | (19,16) | −1, +1 | 0 | 0 |
| CRY → NOW THE | (19,16) | (11,16) | 0, +1 | 0 | 0 |
| NOW THE → IDEA | (11,16) | (15,20) | +1, 0 | 0 | 0 |
| IDEA → OF | (17,18) | (18,15) | 0, 0 | 1 | 1 |
| OF → THE | (18,15) | (19,17) | 0, 0 | 1 | 1 |
| THE → END | (19,16) | (19,23) | +1, 0 | 0 | 0 |
| END → IS | (21,23) | (21,9) | −1, +1 | 0 | 0 |
| IS → DEATH | (21,9) | (26,3) | 0, 0 | 1 | 1 |
| DEATH → SEE | (26,1) | (25,16) | 0, 0 | 1 | 1 |
| SEE → YOU | (27,14) | (27,18) | 0, 0 | 1 | 0 |
| YOU → SOON | (25,16) | (25,16) | 0, −1 | 0 | 0 |
| SOON → THEN | (25,16) | (25,25) | +1, −1 | 0 | 0 |

All **16 transitions pass**: **12 exact alignments** and **4 one-cell offsets**. Five endpoints have `q = 1`; four use the allowance, while SEE → YOU remains exact. All 11 cases with `q = 0` are exact.

### The four offsets

They form two consecutive pairs: **IDEA → OF → THE** and **IS → DEATH → SEE**. Every index below contains a prime square:

| Transition | Endpoint E | n₀(E) | n₃(E) |
| :--- | :--- | :--- | :--- |
| IDEA → OF | (17,18) | 450 = 2 × 3² × 5² | 260 = 2² × 5 × 13 |
| OF → THE | (18,16) | 475 = 5² × 19 | 315 = 3² × 5 × 7 |
| IS → DEATH | (21,10) | 550 = 2 × 5² × 11 | 480 = 2⁵ × 3 × 5 |
| DEATH → SEE | (26,1) | 676 = 26² | 728 = 2³ × 7 × 13 |

For **IDEA → OF**, L = `(17,18)` and B′ = `(18,15)`:

$$
(\Delta r,\Delta c)=(1,-3),\qquad d_8=\min(1,3,2)=1.
$$

For **OF → THE**, the displacement from L = `(18,15)` is `(1,2)`, giving `d₈ = 1`. Its gate uses E = `(18,16)`, a different cell from L.

## 4. SEE → YOU: an exact reflected return

SEE’s leftmost cell and endpoint are `(27,14)`; YOU begins at `(27,18)`. Their displacement is `(0,4)`, so **d₈ = 0**.

Yet the endpoint gives `n₀ = 716 = 2² × 179` and `n₃ = 378 = 2 × 3³ × 7`. Both Möbius values are zero, so **q = 1**. This confirms the inequality; the stronger equality `d₈ = q` would fail.

### Reflection across column 16

Reflect a cell by `F(r,c) = (r,32−c)`. The complete SEE path matches YOU in **reverse reading order**:

| SEE, in reading order | YOU, in reverse reading order = F(SEE) |
| :--- | :--- |
| (25,16) | (25,16) |
| (26,15) | (26,17) |
| (27,14) | (27,18) |

The shared cell **(25,16)** is SEE’s beginning, YOU’s endpoint, and SOON’s beginning.

Among equal-length ordered pairs of the 17 recorded blocks, the reported comparison across four reflection directions found only this anchored full-path reflection/reversal. That is uniqueness within the reconstruction. There is no general rule yet for predicting when to use this return.

### The local equality A = 720

[Report 03](03-predicting-axis-and-reading-direction.md) uses `A = n₂(B) + n₀(M)`, where `n₂ = 730−n₀` and M is the original node center.

For SEE, B = `(25,16)` gives `n₀(B) = 664`, hence `n₂(B) = 66`. Its center M = `(25,6)` gives `n₀(M) = 654`:

$$
A=66+654=720=n_0(27,18)=n_0(B_{\mathrm{YOU}}).
$$

This equality occurs only once among the 16 transitions. A is not a universal next-position formula and can exceed 729. The equality and mirror both refer to the same selected YOU beginning, so they are not independent evidence.

### Alternatives with YOU already fixed

A previous enumeration fixed the plaintext **YOU**, its reading orientation, admissible key signatures, and leftmost-cell Möbius class:

| Restriction | Placements |
| :--- | ---: |
| Can decrypt to YOU under those conditions | 37 |
| Pass the ray filter from SEE | 11 |
| Lie exactly on a ray | 6 |
| Form the exact anchored mirror/reversal of SEE | 1 |

The mirror is selective within this set. Since YOU was supplied, this does not test predicting the word itself.

## 5. How selective is the filter?

### Double zeros and restricted frequency tests

Across the full grid, **142/729 cells (19.48%)** have both endpoint Möbius values zero. Double zeros alone are common; the recorded pattern is that all four offsets occur among five such endpoints.

Of the six pairs of rotations, only **(0°,270°)** gives double zeros at all four deviating endpoints.

Restricted tests held the 16 endpoints fixed and reassigned the four offset labels across the **1,820 possible choices**:

| Choice allowed in the test | Conditional frequency |
| :--- | :--- |
| Fix (0°,270°) in advance | 5/1,820 ≈ 0.275% |
| Choose the best of six rotation pairs | 12/1,820 ≈ 0.659% |
| Choose among 24 tested anchor/rotation-pair definitions | 33/1,820 ≈ 1.813% |

These are **restricted conditional frequencies**, not fully corrected p-values. They do not account for the broader search over geometric functions, keys, plaintexts, or routes.

### Candidate rejection

The reported placement comparisons give:

| Candidate set | Always allow d₈ ≤ 1 | Use d₈ ≤ q |
| :--- | ---: | ---: |
| Preserve next-block length, direction, and leftmost Möbius class | 33.3% pass | 18.3% pass |
| Also produce the already-known next plaintext with an admissible key | 53.2% pass | 48.8% pass |

The improvement is larger spatially than when the correct word is imposed. In the latter test, requiring **μ(n₀(E)) = 0 alone** gave the same candidate counts as the two-zero gate. The extra 270° condition’s cryptographic benefit is therefore not established on those words.

### Anchor comparison

With the same endpoint condition and recorded next beginnings:

| Ray origin | Matches |
| :--- | ---: |
| Current leftmost cell L | 16/16 |
| Current endpoint E | 13/16 |
| Current beginning B | 12/16 |
| Current original key-node center M | 10/16 |

L gives the best fit among these tested anchors. This comparison is retrospective.

## 6. Candidate continuation: THE KEY IS TO GO

### THEN → THE

THEN has **L = (25,25)** and **E = (25,27)**. At E, `n₀ = 675` and `n₃ = 25` both have Möbius value zero, giving **q = 1**.

The candidate THE reads **`J(22,21) → W(21,20)`**, using the original N–M–N node centered on **`M(20,17)`**:

$$
(\Delta r,\Delta c)=(-3,-4),\qquad d_8=\min(3,4,1)=1\le q.
$$

### THE → KEY

THE’s endpoint `W(21,20)` has `n₀ = 560`, `n₃ = 210`, and Möbius pair `(0,+1)`. Thus **q = 0**.

KEY begins at **`N(21,4)`**, directly 16 cells left of L = `(21,20)`, so **d₈ = 0**.

### Five candidate checks

| Transition | Current L | Next B′ | μ(n₀(E)), μ(n₃(E)) | q | d₈ |
| :--- | :--- | :--- | :--- | ---: | ---: |
| THEN → THE | (25,25) | (22,21) | 0, 0 | 1 | 1 |
| THE → KEY | (21,20) | (21,4) | 0, +1 | 0 | 0 |
| KEY → IS | (21,4) | (18,7) | 0, 0 | 1 | 0 |
| IS → TO | (19,6) | (9,16) | 0, +1 | 0 | 0 |
| TO → GO | (9,16) | (9,20) | +1, +1 | 0 | 0 |

All five pass. Only THEN → THE uses an offset. KEY → IS is another case where **q = 1 but d₈ = 0**.

Keep the anchor at L: for KEY it is **`N(21,4)`**, not the endpoint `EA(19,4)`; for TO it is **`U(9,16)`**, not `NG(8,17)`. GO begins at **`H(9,20)`**, four cells right of TO’s anchor.

### Shared diagonal

KEY’s beginning **`N(21,4)`**, both IS cells **`X(18,7), OE(19,6)`**, and both TO cells **`U(9,16), NG(8,17)`** lie on **r + c = 25**. IS reads down-left and TO up-right along this same diagonal.

This is an exact relationship within the selected continuation. The filter does not select that diagonal or its travel distances.

## 7. Scope and limits

- The 16/16 result fits a **selected research reconstruction**, not independently authenticated LP2 plaintext.
- The rule does not choose the ray, distance, side of an offset, exact key, or word. No universal condition for the SEE → YOU mirror return is established.
- The five continuation checks use candidates found with the constraints and remain separate from the recorded fit.
- A stricter condition using the 180° Möbius value separates exact and unit offsets on all 16 recorded steps, but rejects THEN → THE. A sharper historical fit can extrapolate worse.

Further tests should keep the rule fixed and use independently supported new transitions.

---

Data: `LP2_mobius_ray_all_16.csv`. Analyses: `LP2_mobius_gated_ray_report.md` and `LP2_SEE_YOU_mobius_rarity_audit.md` (21 October 2026). Counts and comparisons refer to the selected project route.
