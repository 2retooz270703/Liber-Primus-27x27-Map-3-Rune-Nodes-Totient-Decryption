# Cicada 3301 Liber Primus 0-2
## 27x27 Rune Matrix Decryption - Volume 6

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.
**Date:** 15.09.2026

> **Current plaintext candidate**
>
> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH.**

This document is the technical Markdown edition of the **Coordinate / Geometry Selector Rule** developed after Volumes 1-5.

Volume 6 does **not** introduce a new plaintext segment. Its purpose is to formalize a possible missing navigation rule: the already established Mobius phase may also select a layer of the **current grid coordinates**, and the resulting values may tell us whether the next move can be chosen arithmetically or must be recovered from local mirror geometry.

The main new proposal is:

```text
phase p
  -> apply the same phase to row and column
  -> Mobius values in {-1,0,+1}
  -> measure how complete the coordinate direction signal is
```

The strongest route-wide observation is that the first three clear cases with **two non-zero coordinate values** reproduce the known movement directions exactly, while the later transitions with zeros are precisely the places where the existing Volumes rely heavily on local mirror geometry.

---

## Quick reference

| Item | Volume 6 result |
|---|---|
| Subject | Coordinate / geometry selector for the existing 27x27 route |
| New plaintext | None |
| Existing phase rule | `p = [mu(phi(k1)) + mu(phi(k2)) + mu(phi(k3))] mod 3` |
| Coordinate layer | `sigma_j(n) = mu(phi^j(n))`, `j = 0,1,2` |
| Coordinate selector | `V_p(r,c) = (sigma_p(r), sigma_p(c))` |
| Row signs | `-1 = UP`, `+1 = DOWN` |
| Column signs | `-1 = LEFT`, `+1 = RIGHT` |
| Two non-zero values | complete branch selector |
| One zero | partial selector; geometry is required |
| Two zeros | no coordinate branch information; geometry dominates |
| Distance source | active totient state and/or exact mirror radius |
| Strong new distance pattern | second distance is repeatedly tied to `phi(active center)` |
| Bootstrap hypothesis | `AS I GO THE` behaves like a single `3^0` initialization stage |
| Presentation hypothesis | possible `3^0 -> 3^1 -> 3^2` organization |
| Status | promising selector hypothesis; not yet a complete deterministic state machine |

---

# PART I - SCOPE AND EVIDENCE LEVELS

## 1. What this volume is trying to solve

Volumes 1-5 already establish several recurring mechanisms:

- a 27x27 rune matrix;
- mirrored or structured 3-rune nodes;
- Euler-totient transformation of node centers;
- 3-rune keys;
- the Mobius phase rule;
- Gematria Primus subtraction modulo 29;
- inherited totient values;
- exact mirror radii;
- local geometric handoffs between nodes.

What remained unclear was a deterministic answer to questions such as:

```text
Why UP instead of DOWN?
Why RIGHT instead of LEFT?
When should a totient value be used as movement?
When should the route stop using arithmetic movement and inspect geometry instead?
```

Volume 6 tests whether the **same phase p already used for key rotation** also acts on the coordinates of the current cell.

---

## 2. Evidence labels used in this file

To keep the document easy to parse by humans and AI systems, claims are separated into three levels.

### [R] Recorded route fact

A coordinate, phase, mirror, movement, key, or plaintext already recorded in Volumes 1-5.

### [D] Derived result

A result obtained directly from recorded data by applying the stated formula. Example:

```text
A(14,19), p=2
-> phi^2(14)=2
-> phi^2(19)=6
-> mu(2)=-1
-> mu(6)=+1
-> V_2(14,19)=(-1,+1)
```

### [H] Working hypothesis

An interpretation suggested by the repeated pattern but not yet proven universal. Examples:

- zero means the route should defer to geometry;
- the second movement distance is controlled by the active center;
- the route may be organized in blocks of `3^0`, `3^1`, and `3^2`.

This distinction is important. Volume 6 is intended to help future analysis, not hide uncertainty.

---

# PART II - THE COORDINATE SELECTOR

## 3. Three coordinate layers

For any integer `n`, define:

```text
sigma_j(n) = mu(phi^j(n)),    j = 0,1,2
```

with:

```text
phi^0(n) = n
phi^1(n) = phi(n)
phi^2(n) = phi(phi(n))
```

So each coordinate has three possible Mobius layers:

```text
sigma_0(n) = mu(n)
sigma_1(n) = mu(phi(n))
sigma_2(n) = mu(phi(phi(n)))
```

Because `mu` returns only `-1`, `0`, or `+1`, each layer reduces a coordinate to a very small signal.

---

## 4. Reuse the already established phase

For the current 3-rune key:

```text
K = (k1,k2,k3)
```

the existing phase rule is:

```text
p = [sigma_1(k1) + sigma_1(k2) + sigma_1(k3)] mod 3
```

or equivalently:

```text
p = [mu(phi(k1)) + mu(phi(k2)) + mu(phi(k3))] mod 3
```

Volume 6 proposes that **the same phase** is then applied to the coordinates of the current cell:

```text
P = (r,c)

V_p(r,c) = (sigma_p(r), sigma_p(c))
```

No second phase rule is introduced.

The same `p` that selects the cyclic key layer is reused as the coordinate layer.

---

## 5. Direction convention

For the row component:

```text
-1 = UP
+1 = DOWN
 0 = no complete vertical decision
```

For the column component:

```text
-1 = LEFT
+1 = RIGHT
 0 = no complete horizontal decision
```

When both components are non-zero, the four possible sign pairs are:

| `V_p(r,c)` | Directional branch |
|---|---|
| `(-1,+1)` | UP + RIGHT |
| `(+1,-1)` | DOWN + LEFT |
| `(+1,+1)` | DOWN + RIGHT |
| `(-1,-1)` | UP + LEFT |

The signs are **not distances**.

They answer a different question:

```text
Which directional branch is compatible with the current phase?
```

---

## 6. Three selector-completeness states

The original working note can be made more precise by separating three cases.

### Case A - complete selector

```text
V_p(r,c) = (+/-1, +/-1)
```

Both components carry directional information.

Working interpretation:

```text
coordinates can select the branch
```

The movement magnitudes must still come from the active arithmetic or geometric state.

### Case B - partial selector

```text
V_p(r,c) = (+/-1, 0)
```

or:

```text
V_p(r,c) = (0, +/-1)
```

Only one coordinate carries a non-zero value.

Working interpretation:

```text
coordinates alone are insufficient
-> inspect local geometry
```

Important caution: the surviving non-zero sign is **not yet proven to be a literal immediate arrow**. In several one-zero cases the next physical mirror step does not simply move in that sign's direction.

### Case C - null selector

```text
V_p(r,c) = (0,0)
```

The coordinate calculation supplies no directional branch at all.

Working interpretation:

```text
stop forcing a coordinate arrow
-> recover the continuation from local geometry
```

This three-state interpretation is more accurate than treating the rule as a strict binary switch.

---

# PART III - ROUTE-WIDE TEST

## 7. Test method

For each important endpoint or branch point already recorded in Volumes 1-5:

1. take the phase `p` of the active key/state already established before the next transition;
2. take the recorded grid coordinate `(r,c)`;
3. calculate `phi^p(r)` and `phi^p(c)`;
4. apply `mu` to both;
5. compare the resulting sign pair with the recorded navigation behavior.

No plaintext is used to choose the sign pair.

---

## 8. Full selector table

| Route location | Cell | `p` | `V_p(r,c)` | Selector state | Recorded behavior |
|---|---:|---:|---:|---|---|
| WEATHER -> TURNS | `A(14,19)` | 2 | `(-1,+1)` | complete | `UP 10`, `RIGHT 4` |
| TURNS -> COLD | `A(14,19)` | 0 | `(+1,-1)` | complete | `DOWN 12`, `LEFT 12` |
| COLD -> I MAY | `A(11,7)` | 1 | `(+1,+1)` | complete | `DOWN 4`, `RIGHT 1` |
| after I MAY | `E(26,16)` | 0 | `(+1,0)` | partial | endpoint enters `E-X-E`; geometry required |
| after CRY | `S(17,16)` | 1 | `(0,0)` | null | radius-6 mirror geometry |
| after NOW THE | `J(15,20)` | 2 | `(0,0)` | null | local mirror continuation into IDEA |
| after IDEA | `D(17,18)` | 1 | `(0,+1)` | partial | center of `J-D-J`, radius 2 |
| after OF | `OE(18,16)` | 0 | `(0,0)` | null | local `OE-J-OE` handoff |
| after THE | `J(19,16)` | 2 | `(+1,0)` | partial | radius-4 local geometry |
| after END | `I(21,23)` | 2 | `(0,+1)` | partial | `I-R-I` / shared-center mirror chain |
| after IS | `D(21,10)` | 1 | `(0,0)` | null | center of `E-D-E`, radius 2 |
| B branch before DEATH | `B(23,12)` | 2 | `(+1,-1)` | complete | selects the down-left outer `J(27,8)` |

This table is the main empirical test of the Volume 6 rule.

---

## 9. Complete case 1 - WEATHER -> TURNS

[R] Volume 1 identifies:

```text
A(14,19)
```

as a crossroads and records the movements:

```text
UP 10
RIGHT 4
```

[R] The active phase arriving from the WEATHER key `X-I-X` is:

```text
p = 2
```

[D] Apply phase 2 to the coordinates:

```text
14 -> phi(14)=6 -> phi(6)=2 -> mu(2)=-1
19 -> phi(19)=18 -> phi(18)=6 -> mu(6)=+1
```

Therefore:

```text
V_2(14,19) = (-1,+1)
```

which gives:

```text
UP + RIGHT
```

This matches the recorded directions exactly.

The coordinate rule does not create `10` and `4`; it only gives the signs/orientation of those already active values.

---

## 10. Complete case 2 - TURNS -> COLD

The same physical cell is reused:

```text
A(14,19)
```

but the active phase has changed to:

```text
p = 0
```

[D] Therefore:

```text
V_0(14,19)
= (mu(14), mu(19))
= (+1,-1)
```

which gives:

```text
DOWN + LEFT
```

[R] Volume 1 uses the new control value:

```text
phi(NG) = 12
```

in both directions:

```text
DOWN 12
LEFT 12
```

Again, the signs match exactly.

This is particularly important because the **same cell** changes branch when the phase changes:

```text
p=2 -> UP + RIGHT
p=0 -> DOWN + LEFT
```

That behavior is difficult to explain as a fixed geometric arrow attached to `A(14,19)` alone.

---

## 11. Complete case 3 - COLD -> I MAY

[R] COLD ends at:

```text
A(11,7)
```

The inherited state is:

```text
H-U-H -> 4-1-4
```

and the active phase is:

```text
p = 1
```

[D] Apply phase 1 to the coordinates:

```text
11 -> phi(11)=10 -> mu(10)=+1
 7 -> phi(7)=6  -> mu(6)=+1
```

Therefore:

```text
V_1(11,7) = (+1,+1)
```

which gives:

```text
DOWN + RIGHT
```

[R] Volume 2 records:

```text
A(11,7) -> DOWN 4 -> S(15,7) -> RIGHT 1 -> B(15,8)
```

Again, the selector signs match the recorded direction pair exactly.

These are the three clearest cases where both coordinate components are non-zero and a separate geometric search is not needed to decide the direction pair.

---

## 12. Null case - CRY -> NOW THE

[R] CRY ends at:

```text
S(17,16)
```

with phase:

```text
p = 1
```

[D] The coordinate selector becomes:

```text
phi(17)=16 -> mu(16)=0
phi(16)=8  -> mu(8)=0
```

so:

```text
V_1(17,16) = (0,0)
```

The coordinate rule supplies no branch direction.

At exactly this point the recorded continuation is geometric.

[R] The endpoint belongs to:

```text
S(17,4) --6-- IA/O(17,10) --6-- S(17,16)
```

and the same center belongs to another radius-6 mirror:

```text
TH(11,16) --6-- IA/O(17,10) --6-- TH(23,4)
```

The route uses:

```text
S(17,16) -> UP 6 -> TH(11,16)
```

This is the cleanest example of:

```text
(0,0) -> no coordinate branch -> inspect geometry
```

---

## 13. Partial cases are genuinely different from `(0,0)`

The one-zero cases should not be collapsed into the same category as `(0,0)`.

Examples include:

```text
E(26,16), p=0  -> (+1,0)
D(17,18), p=1  -> (0,+1)
J(19,16), p=2  -> (+1,0)
I(21,23), p=2  -> (0,+1)
```

These positions still retain one non-zero coordinate value, but their continuations depend on exact local structures:

- `E(26,16)` is an outer node of `E-X-E`;
- `D(17,18)` is the center of `J-D-J`;
- `J(19,16)` belongs to radius-4 structures and is adjacent to the `F-X-F` pointer;
- `I(21,23)` is an outer node of `I-R-I`, whose center is shared with a larger `H-R-H` mirror.

[H] The safest current interpretation is:

```text
one zero = coordinate information is incomplete
         = geometry must supply the missing structure
```

The remaining non-zero sign may still act as a filter at some level, but the current route does not justify treating it as an unconditional immediate arrow.

For example, `I(21,23)` gives `(0,+1)`, yet the local `I-R-I` mirror reaches its center by moving left. Therefore `+1` cannot simply mean "the next physical step must be RIGHT" whenever the other component is zero.

---

## 14. Complete selector can coexist with geometry

The strongest refinement appears near DEATH.

[R] The route reaches:

```text
B(23,12)
```

which is the center of:

```text
J(19,16) -- B(23,12) -- J(27,8)
```

The active `J-T-J` state has:

```text
p = 2
```

[D] Apply phase 2 to B's coordinates:

```text
23 -> 22 -> 10 -> mu(10)=+1
12 ->  4 ->  2 -> mu(2) =-1
```

Therefore:

```text
V_2(23,12) = (+1,-1)
```

which means:

```text
DOWN + LEFT
```

The two outer J nodes are already supplied by geometry. The new/unused outer node is:

```text
J(27,8)
```

and relative to `B(23,12)` its displacement is:

```text
(+4,-4) = DOWN + LEFT
```

So the coordinate signs point exactly toward the selected outer J.

This is important because it refines the earlier binary interpretation.

The rule is probably **not**:

```text
non-zero -> ignore geometry
zero     -> use geometry
```

A better interpretation is:

```text
geometry and arithmetic may both provide candidates
coordinate completeness tells us how much the phase-coordinate field can select among them
```

---

# PART IV - WHERE THE MOVEMENT DISTANCES COME FROM

## 15. Signs and magnitudes are separate

The coordinate field gives only:

```text
-1, 0, +1
```

These are direction/selection values, not movement lengths.

A useful factorization is:

```text
V_p(r,c) = (s_r, s_c)
```

and, when two movement magnitudes are available:

```text
Delta r = s_r * d_r
Delta c = s_c * d_c
```

where:

```text
(s_r, s_c) = coordinate signs
(d_r, d_c) = active movement magnitudes
```

The open problem is therefore split into two smaller questions:

```text
1. Which direction?  -> coordinate selector
2. How far?          -> active totient state / mirror geometry
```

---

## 16. The three clean totient-driven distance cases

The same three complete-selector examples also reveal a possible rule for movement magnitudes.

### Case 1 - WEATHER -> TURNS

[R] The previous active chain gives:

```text
OE -> phi(OE)=10=I
I  -> phi(I)=4
```

The two values reused at `A(14,19)` are:

```text
(10,4)
```

With:

```text
V_2(14,19)=(-1,+1)
```

this becomes:

```text
UP 10
RIGHT 4
```

### Case 2 - TURNS -> COLD

[R] The active center is:

```text
NG = 21
```

and:

```text
phi(NG)=12
```

Only one new movement magnitude is used, so it is applied to both branches:

```text
(12,12)
```

With:

```text
V_0(14,19)=(+1,-1)
```

this becomes:

```text
DOWN 12
LEFT 12
```

### Case 3 - COLD -> I MAY

[R] The active mirrored key family is:

```text
H-U-H
```

with totient signature:

```text
4-1-4
```

The movement uses:

```text
(4,1)
```

With:

```text
V_1(11,7)=(+1,+1)
```

this becomes:

```text
DOWN 4
RIGHT 1
```

---

## 17. New center-linked distance pattern

Across all three clear non-geometric complete-selector cases, the **second movement distance** is tied to the active center value.

```text
active center I  -> phi(I)  = 4
active center NG -> phi(NG) = 12
active center U  -> phi(U)  = 1
```

The observed movement pairs are:

```text
(10,4)
(12,12)
(4,1)
```

So the repeated relation is:

```text
second movement magnitude = phi(active center)
```

This is one of the strongest new observations in Volume 6 because it holds in **all three** clean cases where:

1. both coordinate components are non-zero; and
2. the direction pair is not being recovered from mirror geometry.

The first movement magnitude is less fully formalized.

Observed first values are:

```text
10  -> companion control carried from I
12  -> the same single NG-derived control value
4   -> outer value of the 4-1-4 state
```

[H] A provisional description is therefore:

```text
first distance  = companion/outer control value of the active state
second distance = phi(active center)
```

This should be treated as a testable hypothesis, not yet a universal law.

---

## 18. Geometry supplies its own scale

When an exact mirror is already visible, its radius supplies a natural structural scale.

For a mirror:

```text
outer_1 --R-- center --R-- outer_2
```

we have:

```text
outer -> center           = R
center -> outer           = R
outer -> opposite outer   = 2R
```

So the mirror radius is a **structural scale**, not automatically the total displacement of every transition.

Examples from the existing route:

### Radius 6 after CRY

```text
S --6-- IA/O --6-- S
```

The route uses one radius:

```text
S(17,16) -> UP 6 -> TH(11,16)
```

### Radius 4 after THE

```text
F(19,15) --4-- X(19,19) --4-- F(19,23)
```

The two outer F nodes are physically 8 columns apart:

```text
outer -> opposite outer = 2 * 4 = 8
```

### Radius 2 near DEATH

```text
C/K(26,3) --2-- OE(26,5) --2-- C/K(26,7)
```

Again, opposite outer nodes are separated by 4 cells even though the mirror radius is 2.

This distinction prevents the common error:

```text
mirror radius = always the full movement length
```

---

## 19. Strongest scale evidence: arithmetic and geometry agree

The strongest movement values are not values selected because they happen to land on useful cells.

They are values supported independently by more than one layer.

The post-CRY value `6` is the clearest example in the research note:

```text
inherited active value = 6
local mirror radius     = 6
additional totient link = 6
```

When arithmetic and exact geometry independently produce the same scale, that value is much stronger than an arbitrary historical totient.

[H] A good future rule is therefore:

```text
prefer locally confirmed values
avoid choosing old totients only because they produce a useful landing point
```

---

# PART V - AS I GO THE AS A BOOTSTRAP STAGE

## 20. The beginning behaves differently

The first plaintext stage does not begin with the new coordinate selector.

[R] The starting node is:

```text
AE-J-EA
```

Its center transforms as:

```text
J = 11
phi(J) = 10 = I
```

which compiles:

```text
AE-J-EA -> AE-I-EA
```

[R] For the key `AE-I-EA`, Volume 1 records:

```text
phi(K) = 20,4,12
mu(phi(K)) = 0,0,0
```

Therefore:

```text
p = 0
```

This is a **fully zero key-phase signature**. It should not be confused with a coordinate result `V_p(r,c)=(0,0)`; the two calculations act on different objects.

The important point is that the opening movement is generated directly from the center-totient chain:

```text
J -> 10 = I
I -> 4
10 + 4 = 14
-> RIGHT 14
```

This leads to:

> **AS I GO THE**

So the opening stage acts like an initialization step that creates the first control values before the coordinate-selector behavior becomes visible.

---

## 21. AS I GO THE immediately opens X-OE-X

[R] The final ciphertext rune of `AS I GO THE` is `X`.

That endpoint is immediately adjacent to the mirror:

```text
X-OE-X
```

Its center transforms:

```text
OE -> phi(OE)=10=I
```

so:

```text
X-OE-X -> X-I-X
```

The new key has:

```text
phi(X-I-X) = 6-4-6
mu = +1,0,+1
sum = 2 mod 3
p = 2
```

The same center-derived value `10` gives:

```text
RIGHT 10 -> central NG
```

and the next plaintext is:

> **WEATHER**

This transition appears to connect the bootstrap arithmetic to the later phase system.

---

## 22. WEATHER contains a possible phase hint

Volume 1 notes a visual feature above the WEATHER ciphertext:

```text
W-EA-TH
```

These are three rune tokens.

Volume 1 interprets them as a possible visual clue toward a **three-position phase rule**.

This becomes especially interesting in Volume 6 because the phase is then reused at the next crossroads.

The sequence can be read as:

```text
1. X-OE-X generates X-I-X
2. Mobius fixes p=2
3. WEATHER visually carries a three-rune hint W-EA-TH
4. route reaches A(14,19)
5. the same p=2 is applied to A's coordinates
6. V_2(14,19)=(-1,+1)
7. known values 10 and 4 become UP 10 and RIGHT 4
```

[H] This creates a plausible teaching/progression pattern:

```text
first show phase on the key
then reuse the same phase on the coordinates
```

---

# PART VI - THE 3^0 / 3^1 / 3^2 PRESENTATION HYPOTHESIS

## 23. A possible power-of-three organization

A secondary observation is that the recovered route can be grouped suggestively around powers of three.

### `3^0 = 1` - bootstrap

One opening stage:

```text
AS I GO THE
```

Behavior:

```text
initial node
-> center totient chain
-> direct RIGHT 14 movement
-> first plaintext
-> immediate X-OE-X mirror
```

This stage initializes the system rather than demonstrating the later coordinate selector in full.

### `3^1 = 3` - three complete selector demonstrations

The first three clear complete coordinate cases are:

```text
WEATHER -> TURNS   : (-1,+1)
TURNS   -> COLD    : (+1,-1)
COLD    -> I MAY   : (+1,+1)
```

All three have:

```text
no zero coordinate component
```

and all three reproduce the recorded direction pair.

### `3^2 = 9` - geometry-heavy continuation

The later recovered plaintext can be segmented into nine pieces:

```text
I MAY
CRY
NOW THE
IDEA
OF
THE
END
IS
DEATH
```

This part of the route is dominated by exact local mirrors, shared centers, radii, endpoint-to-node handoffs, and structural recursion.

---

## 24. Important caution about the 1-3-9 pattern

The `3^0 -> 3^1 -> 3^2` pattern is **not yet an algorithmic proof**.

There are two reasons to be careful:

1. `I MAY` is reached by the complete selector at `A(11,7)`, so the boundary between the `3` block and the `9` block is not a perfect binary change of mechanism.
2. Near DEATH, `B(23,12)` again has a complete selector `(+1,-1)` even though exact mirror geometry is also active.

Therefore the strongest defensible statement is:

```text
The route may be PRESENTED in 1, 3, and 9 stage blocks,
while the actual navigation mechanisms can overlap.
```

[H] If intentional, the route may be exposing progressively richer behavior:

```text
3^0: initialize arithmetic state
3^1: demonstrate direct coordinate branch selection
3^2: demonstrate how the same arithmetic interacts with mirror geometry
```

This is a useful pattern to test on any continuation beyond DEATH, but it should not be assumed in advance.

---

# PART VII - REFINED NAVIGATION MODEL

## 25. The selector is better understood as a completeness test

The original wording "coordinate mode versus geometry mode" is useful, but the route suggests a more precise model.

The coordinate field does not draw the whole route.

It measures how much directional information is available from the current phase and coordinates.

```text
V_p = (+/-1,+/-1)
-> complete directional selector

V_p = (+/-1,0) or (0,+/-1)
-> partial directional selector
-> geometry required

V_p = (0,0)
-> no coordinate branch information
-> geometry determines the continuation
```

Geometry may still be present when both values are non-zero. In that case the coordinate signs can select among geometry-provided candidates, as at `B(23,12)`.

---

## 26. Proposed order of operations

The current working model can be written as:

```text
CURRENT KEY / STATE
        |
        v
calculate phase p
        |
        +----------------------+
        |                      |
        v                      v
rotate key               select coordinate layer p
                               |
                               v
                    V_p(r,c) = (s_r,s_c)
                               |
             +-----------------+-----------------+
             |                 |                 |
             v                 v                 v
        no zeros           one zero          two zeros
             |                 |                 |
             v                 v                 v
     complete selector    partial selector   null selector
             |                 |                 |
             +-----------+-----+-----------------+
                         |
                         v
              inspect active local state
                         |
              +----------+----------+
              |                     |
              v                     v
        active totient values   exact mirror geometry
              |                     |
              v                     v
        movement magnitudes      radius / candidates
              |                     |
              +----------+----------+
                         |
                         v
                choose next branch
```

This model separates three jobs that were previously mixed together:

```text
phase       -> which layer is active
coordinates -> branch information
state/map   -> movement magnitude and structural candidates
```

---

## 27. Deterministic working algorithm

The following is the strongest current algorithmic form.

### Step 1 - calculate phase

```text
p = [mu(phi(k1)) + mu(phi(k2)) + mu(phi(k3))] mod 3
```

This is already established by the earlier Volumes.

### Step 2 - calculate coordinate selector

```text
V_p(r,c) = (mu(phi^p(r)), mu(phi^p(c)))
```

### Step 3 - classify selector completeness

```text
2 non-zero components -> complete
1 non-zero component  -> partial
0 non-zero components -> null
```

### Step 4 - enumerate legitimate movement data

Use only values that are structurally active, such as:

- the current center totient;
- current control values inherited from the active state;
- an exact mirror radius;
- a repeated exact totient signature tied to the current structure.

Do not search arbitrary old totients until one lands somewhere useful.

### Step 5 - resolve movement

If the selector is complete:

```text
use the signs to choose/orient the available movement values or geometric candidates
```

If the selector is partial:

```text
geometry must provide the missing structure
```

If the selector is null:

```text
geometry must provide the continuation almost entirely
```

### Step 6 - verify destination structurally

A valid move should land on a meaningful feature already used by the model:

- a mirror center;
- an outer mirror node;
- a shared node;
- ciphertext start;
- key-generating node;
- exact signature match;
- another locally connected structural feature.

---

## 28. Compact pseudocode

```text
INPUT:
    current key K=(k1,k2,k3)
    current cell P=(r,c)
    active structural state S

PHASE:
    p = sum(mu(phi(ki))) mod 3

SELECTOR:
    sr = mu(phi^p(r))
    sc = mu(phi^p(c))
    V  = (sr,sc)

CANDIDATES:
    G = local geometric candidates around P
    D = movement magnitudes justified by current state S

IF sr != 0 AND sc != 0:
    mode = COMPLETE
    use signs to select/orient D and/or G

ELSE IF exactly one of sr,sc is zero:
    mode = PARTIAL
    require geometry G
    do not treat the surviving sign as a guaranteed immediate arrow

ELSE:
    mode = NULL
    require geometry G to determine continuation

VERIFY:
    next point must have a structural reason
    do not accept a move only because it gives readable plaintext
```

---

# PART VIII - WHAT THE NEW RULE EXPLAINS

## 29. It explains the direction change at the same crossroads

At the same physical cell:

```text
A(14,19)
```

two phases give opposite branch patterns:

```text
p=2 -> (-1,+1) -> UP + RIGHT
p=0 -> (+1,-1) -> DOWN + LEFT
```

This explains why one fixed geometric arrow at A is insufficient.

---

## 30. It explains why CRY needs geometry

At:

```text
S(17,16), p=1
```

the selector is:

```text
(0,0)
```

and the route is resolved from the exact radius-6 mirror geometry.

This is the cleanest null-selector example.

---

## 31. It explains why one-zero cases should not be forced

At several later endpoints the selector has only one non-zero component.

The existing route already solves those positions using mirrors, shared centers, and radii.

Volume 6 therefore removes the need to invent a missing coordinate direction.

---

## 32. It gives a new interpretation of B before DEATH

At:

```text
B(23,12), p=2
```

geometry supplies two outer J candidates, while:

```text
V_2(23,12)=(+1,-1)
```

points to the down-left one:

```text
J(27,8)
```

This is a useful example of arithmetic and geometry cooperating rather than replacing each other.

---

## 33. It narrows the distance problem

The selector removes one major ambiguity:

```text
Mobius + coordinates do not need to explain distance.
```

Distance can now be investigated separately through:

- center totients;
- companion control values;
- inherited active signatures;
- exact mirror radii.

The repeated relation:

```text
second distance = phi(active center)
```

is therefore a concrete next target for verification.

---

# PART IX - WHAT REMAINS UNRESOLVED

## 34. The first distance is not yet fully formalized

The three clean pairs are:

```text
(10,4)
(12,12)
(4,1)
```

The second component has a clean center relation:

```text
I  -> 4
NG -> 12
U  -> 1
```

The first component currently has only a descriptive rule:

```text
companion / outer / carried control value
```

A deterministic formula for that first component is still needed.

---

## 35. One-zero semantics are not fully solved

We know that one-zero cases require geometry.

We do **not** yet know exactly what the surviving sign does.

Possible roles include:

- filtering a set of geometric candidates;
- selecting orientation only after a mirror is identified;
- indicating which coordinate remains arithmetically active;
- carrying state information rather than a literal movement arrow.

A future test should compare all one-zero cases without using plaintext as feedback.

---

## 36. Geometry activation still needs a formal candidate-generation rule

When the selector is partial or null, we still need to define exactly which structures count as local candidates.

A strict implementation should specify a search order such as:

1. mirrors containing the current endpoint;
2. mirrors sharing the same center;
3. mirrors sharing the current cell as center or outer node;
4. exact radius matches with active values;
5. exact totient-signature matches;
6. previously used connected nodes;
7. unused opposite outer nodes.

Without a fixed candidate-generation rule, geometry can still become too flexible.

---

## 37. The 3^0 / 3^1 / 3^2 pattern remains interpretive

The `1 -> 3 -> 9` grouping is visually and conceptually attractive, especially because the entire model already depends on 3-rune keys and three phases.

However, a valid continuation should confirm the pattern **before** it is promoted to a rule.

The strongest future evidence would be another structured regime change after the current `3^2` block.

---

# PART X - FALSIFICATION TESTS

## 38. Route-wide test without plaintext

A future verifier should perform the following test for every endpoint:

```text
1. obtain phase from the current key only
2. compute V_p(r,c)
3. classify complete / partial / null
4. enumerate local geometry before examining next plaintext
5. enumerate only structurally active movement values
6. predict candidate movement(s)
7. compare prediction with recorded route
```

If the rule only works after the next plaintext is known, it is not deterministic enough.

---

## 39. Test every 27x27 cell under all three phases

The selector can be precomputed for the entire map.

For every cell `(r,c)` calculate:

```text
V_0(r,c)
V_1(r,c)
V_2(r,c)
```

This creates three complete direction/completeness fields over the 27x27 map.

Useful questions:

- Do known crossroads concentrate in complete-selector cells?
- Do known geometry-heavy transitions concentrate in partial/null cells?
- Are mirror centers statistically enriched for zeros?
- Do phase changes systematically flip branches at reused cells?

This test is independent of English plaintext.

---

## 40. Test the center-distance relation

For every future complete-selector movement that does not require geometry, record:

```text
active center rune/value
phi(active center)
first movement magnitude
second movement magnitude
```

The current hypothesis predicts:

```text
second movement magnitude = phi(active center)
```

A single clean counterexample would require revising this rule.

---

## 41. Test the partial-selector sign

For all one-zero cases:

```text
(+/-1,0)
(0,+/-1)
```

enumerate the geometry first and ask whether the surviving sign consistently selects:

- one side of a mirror;
- one orientation;
- one candidate structure;
- or nothing at all.

This is currently one of the highest-value unresolved questions.

---

# PART XI - MACHINE-READABLE SUMMARY

## 42. Core formulas

```text
COORDINATE_LAYER:
sigma_j(n) = mu(phi^j(n))
j in {0,1,2}

PHASE:
p = [sigma_1(k1)+sigma_1(k2)+sigma_1(k3)] mod 3

COORDINATE_SELECTOR:
V_p(r,c) = (sigma_p(r),sigma_p(c))

ROW:
-1 = UP
+1 = DOWN
0  = incomplete vertical information

COLUMN:
-1 = LEFT
+1 = RIGHT
0  = incomplete horizontal information
```

---

## 43. Selector classification

```text
COMPLETE:
sr != 0 AND sc != 0
meaning = coordinate field can select a directional branch

PARTIAL:
exactly one of sr,sc is 0
meaning = geometry required; one coordinate signal remains

NULL:
sr == 0 AND sc == 0
meaning = coordinate field gives no directional branch; geometry dominates
```

---

## 44. Route trace

```text
BOOTSTRAP:
node = AE-J-EA
compile = AE-I-EA
key_phi = 20,4,12
key_mu = 0,0,0
phase = 0
movement_basis = 10 + 4
movement = RIGHT 14
plaintext = AS I GO THE
next_mirror = X-OE-X

WEATHER_KEY:
X-OE-X -> X-I-X
phase = 2
movement = RIGHT 10 -> central NG
plaintext = WEATHER
possible_phase_hint = W-EA-TH

SELECTOR_1:
point = A(14,19)
phase = 2
V = (-1,+1)
state = COMPLETE
active_magnitudes = 10,4
movement = UP 10; RIGHT 4
plaintext_next = TURNS

SELECTOR_2:
point = A(14,19)
phase = 0
V = (+1,-1)
state = COMPLETE
active_magnitudes = 12,12
movement = DOWN 12; LEFT 12
plaintext_next = COLD

SELECTOR_3:
point = A(11,7)
phase = 1
V = (+1,+1)
state = COMPLETE
active_magnitudes = 4,1
movement = DOWN 4; RIGHT 1
next_node = B(15,8)
plaintext_next = I MAY

PARTIAL_1:
point = E(26,16)
phase = 0
V = (+1,0)
state = PARTIAL
geometry = E-X-E

NULL_1:
point = S(17,16)
phase = 1
V = (0,0)
state = NULL
geometry = radius-6 shared-center mirrors
movement = UP 6 -> TH(11,16)
plaintext_next = NOW THE

NULL_2:
point = J(15,20)
phase = 2
V = (0,0)
state = NULL
geometry = local mirror continuation
plaintext_next = IDEA

PARTIAL_2:
point = D(17,18)
phase = 1
V = (0,+1)
state = PARTIAL
geometry = center of J-D-J radius 2
plaintext_next = OF

NULL_3:
point = OE(18,16)
phase = 0
V = (0,0)
state = NULL
geometry = OE-J-OE
plaintext_next = THE

PARTIAL_3:
point = J(19,16)
phase = 2
V = (+1,0)
state = PARTIAL
geometry = radius-4 F-X-F and J-B-J region
plaintext_next = END

PARTIAL_4:
point = I(21,23)
phase = 2
V = (0,+1)
state = PARTIAL
geometry = I-R-I / H-R-H shared center
plaintext_next = IS

NULL_4:
point = D(21,10)
phase = 1
V = (0,0)
state = NULL
geometry = center of E-D-E radius 2
next_point = B(23,12)

SELECTOR_4_WITH_GEOMETRY:
point = B(23,12)
phase = 2
V = (+1,-1)
state = COMPLETE
geometry = J(19,16)-B(23,12)-J(27,8)
selected_outer = J(27,8)
direction = DOWN + LEFT
plaintext_next = DEATH chain
```

---

## 45. Distance trace

```text
DISTANCE_CASE_1:
movement_pair = 10,4
center_state = I
phi(I) = 4
second_distance = 4

DISTANCE_CASE_2:
movement_pair = 12,12
center_state = NG
phi(NG) = 12
second_distance = 12

DISTANCE_CASE_3:
movement_pair = 4,1
center_state = U
phi(U) = 1
second_distance = 1

CURRENT_PATTERN:
second_distance = phi(active_center)
status = observed in all 3 clean totient-driven complete-selector cases
```

---

# PART XII - RESEARCH CONCLUSION

## 46. Main result of Volume 6

The strongest interpretation is no longer that the Mobius-coordinate formula should generate every movement by itself.

Instead:

```text
Mobius phase selects a coordinate layer.
The coordinate layer measures directional completeness.
The active totient state or mirror geometry supplies movement scale and candidates.
```

The route therefore appears to combine two information systems:

```text
ARITHMETIC
phase + coordinates + totients

GEOMETRY
mirrors + centers + radii + shared nodes
```

The new selector may be the missing connection between them.

The compact working rule is:

```text
NO ZEROS
-> coordinates can choose the directional branch

ONE ZERO
-> coordinate signal is incomplete
-> geometry must complete the move

TWO ZEROS
-> coordinates give no branch
-> geometry determines the continuation
```

with the important refinement:

```text
complete coordinates do not eliminate geometry;
they can also select among geometric candidates
```

The three earliest complete-selector cases reproduce the recorded directions exactly:

```text
A(14,19), p=2 -> (-1,+1) -> UP 10, RIGHT 4
A(14,19), p=0 -> (+1,-1) -> DOWN 12, LEFT 12
A(11,7),  p=1 -> (+1,+1) -> DOWN 4, RIGHT 1
```

and all three reveal the same new distance relation:

```text
second movement distance = phi(active center)

I  -> 4
NG -> 12
U  -> 1
```

The later route then supplies a natural stress test: partial and null coordinate signals repeatedly occur exactly where the previous Volumes already required local mirror geometry.

This does not yet complete the state machine, but it substantially narrows the unresolved movement problem and provides a concrete, falsifiable rule for future route analysis.

---

# References inside this repository

- [Volume 1](./Volume-1.md) - map construction, first nodes, phase rule, `AS I GO THE WEATHER TURNS COLD`, A(14,19) crossroads.
- [Volume 2](./Volume-2.md) - inherited `4-1-4`, `I MAY CRY`, hidden node B, `E-X-E`.
- [Volume 3](./Volume-3.md) - radius-6 geometry after CRY, `NOW THE`.
- [Volume 4](./Volume-4.md) - `IDEA OF THE END`, local mirror chain, radius-4 geometry.
- [Volume 5](./Volume-5.md) - `IS DEATH`, shared centers, perpendicular radius-2 transition, reused `J-B-J` structure.

---

## Final status

**Coordinate / Geometry Selector Rule:** promising and route-consistent across the currently tested endpoints.

**Center-linked second-distance rule:** observed in all three clean totient-driven complete-selector cases; requires further testing.

**3^0 / 3^1 / 3^2 organization:** interesting presentation hypothesis; not yet established as an algorithmic law.

**Overall solution status:** proposed, ongoing, not officially verified.
