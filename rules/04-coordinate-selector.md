# 04 — Coordinate Selector

> **Purpose:** explain how the active key phase is reused on grid coordinates to select a movement direction.  
> This rule controls **orientation**, not movement distance.

---

## 1. The problem

`03-totient-movement.md` explains where movement distances such as:

```text
10
4
12
6
```

come from.

But a distance does not tell us whether to move:

```text
UP
DOWN
LEFT
RIGHT
```

The coordinate selector is the proposed rule for choosing that directional branch.

---

## 2. Three coordinate layers

For any integer coordinate `n`, define:

```text
σ_j(n) = μ(φ^j(n))
```

where:

```text
j = 0, 1, 2
```

and:

```text
φ^0(n) = n
φ^1(n) = φ(n)
φ^2(n) = φ(φ(n))
```

Therefore:

```text
σ_0(n) = μ(n)
σ_1(n) = μ(φ(n))
σ_2(n) = μ(φ²(n))
```

Each coordinate is reduced to one of:

```text
-1
 0
+1
```

---

## 3. Reuse the active key phase

The phase `p` is already determined by the key-phase rule.

The coordinate selector introduces **no new phase**.

For the current grid cell:

```text
P = (r,c)
```

use the same active phase:

```text
V_p(r,c) = (σ_p(r), σ_p(c))
```

or equivalently:

```text
V_p(r,c)
=
( μ(φ^p(r)), μ(φ^p(c)) )
```

So the chain is:

```text
active key
↓
phase p
↓
apply the same p to row and column
↓
Möbius signs
↓
directional branch
```

---

## 4. Direction convention

The first component controls the row:

```text
-1 → UP
+1 → DOWN
 0 → vertical direction unresolved
```

The second component controls the column:

```text
-1 → LEFT
+1 → RIGHT
 0 → horizontal direction unresolved
```

Therefore:

```text
(-1,+1) → UP + RIGHT
(+1,-1) → DOWN + LEFT
(+1,+1) → DOWN + RIGHT
(-1,-1) → UP + LEFT
```

These signs are **directions only**.

They do not generate the movement distances.

---

## 5. Complete selector

When both components are non-zero:

```text
V_p(r,c) = (±1,±1)
```

the selector is called:

```text
complete
```

The coordinates can choose the directional branch directly.

The movement magnitudes still come from the active totient state.

---

## 6. Example: WEATHER → TURNS

The route reaches:

```text
A(14,19)
```

with:

```text
p=2
```

Apply two totient steps to each coordinate.

Row:

```text
14
→ φ(14)=6
→ φ(6)=2
→ μ(2)=-1
```

Column:

```text
19
→ φ(19)=18
→ φ(18)=6
→ μ(6)=+1
```

Therefore:

```text
V₂(14,19)=(-1,+1)
```

which means:

```text
UP + RIGHT
```

The already active movement values are:

```text
10 and 4
```

so the route becomes:

```text
UP 10
RIGHT 4
```

This matches the recorded transition to `TURNS`.

---

## 7. Same cell, different phase

The same physical cell:

```text
A(14,19)
```

is later reused with:

```text
p=0
```

Now:

```text
V₀(14,19)
=
(μ(14), μ(19))
=
(+1,-1)
```

therefore:

```text
DOWN + LEFT
```

The active movement value is:

```text
12
```

so the route uses:

```text
DOWN 12
LEFT 12
```

for the transition to `COLD`.

This is a strong test because the same coordinate changes direction when the phase changes:

```text
p=2 → UP + RIGHT
p=0 → DOWN + LEFT
```

So the direction is not a fixed arrow attached to the cell.

---

## 8. Example: COLD → I MAY

`COLD` ends at:

```text
A(11,7)
```

with:

```text
p=1
```

Calculate:

```text
11 → φ(11)=10 → μ(10)=+1
7  → φ(7)=6   → μ(6)=+1
```

therefore:

```text
V₁(11,7)=(+1,+1)
```

which means:

```text
DOWN + RIGHT
```

The inherited movement values are:

```text
4 and 1
```

so:

```text
DOWN 4
RIGHT 1
```

This reaches:

```text
B(15,8)
```

exactly as recorded in the route.

---

## 9. Partial selector

If exactly one component is zero:

```text
(+1,0)
(-1,0)
(0,+1)
(0,-1)
```

the selector is:

```text
partial
```

Only one directional component survives.

Example:

```text
E(26,16)
p=0

V₀(26,16)=(+1,0)
```

This does **not** give a complete move.

At these points, local mirror geometry must supply the missing information.

The surviving sign should therefore be treated as a directional constraint, not automatically as an immediate literal step.

---

## 10. Null selector

If both components are zero:

```text
V_p(r,c)=(0,0)
```

the coordinate layer gives no directional branch.

Example after `CRY`:

```text
S(17,16)
p=1

V₁(17,16)=(0,0)
```

At exactly this point the continuation is found from the radius-6 mirror geometry:

```text
S —6— IA —6— S
```

and its companion:

```text
TH —6— IA —6— TH
```

leading to:

```text
UP 6
```

and then:

```text
NOW THE
```

So the working rule is:

```text
(0,0)
→ stop forcing a coordinate direction
→ use local geometry
```

---

## 11. Complete / partial / null

The selector therefore has three useful states:

```text
NO ZEROS
→ complete
→ coordinates can select the directional branch

ONE ZERO
→ partial
→ one directional constraint survives
→ geometry must complete the move

TWO ZEROS
→ null
→ coordinates give no branch
→ geometry determines the continuation
```

This is more accurate than treating the selector as a rule that always produces a full arrow.

---

## 12. Relationship to movement values

The two layers solve different problems.

Totient movement:

```text
How far?
```

Coordinate selector:

```text
Which direction?
```

Together:

```text
active totient values
→ movement magnitudes

active phase + coordinates
→ directional branch
```

Example:

```text
movement values = 10,4
selector = (-1,+1)

→ UP 10
→ RIGHT 4
```

---

## 13. Evidence status

The strongest complete-selector checks are:

```text
A(14,19), p=2
→ (-1,+1)
→ UP 10, RIGHT 4

A(14,19), p=0
→ (+1,-1)
→ DOWN 12, LEFT 12

A(11,7), p=1
→ (+1,+1)
→ DOWN 4, RIGHT 1
```

These reproduce three previously recorded direction pairs exactly.

Later partial and null cases also occur precisely where the route already requires local geometry.

The current evidence therefore supports:

```text
complete selector
→ strong directional rule

partial selector
→ incomplete directional information

null selector
→ geometry dominates
```

The partial/null interpretation remains a working model rather than a fully proven universal law.
