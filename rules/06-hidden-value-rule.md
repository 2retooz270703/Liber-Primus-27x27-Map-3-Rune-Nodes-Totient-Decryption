# 06 — Hidden Value Rule

> **Purpose:** preserve the pre-Möbius coordinate value when the coordinate selector produces `0`.  
> A zero removes the **sign**, but does not necessarily erase the **totient-derived value** that produced it.

---

## 1. The missing information in the coordinate selector

The coordinate selector is defined as:

```text
V_p(r,c)
=
( μ(φ^p(r)), μ(φ^p(c)) )
```

and reduces each coordinate component to:

```text
-1
 0
+1
```

This is sufficient when both components are non-zero, because the signs select a directional branch.

But when a component becomes:

```text
0
```

the current model treats that axis as unresolved.

The important observation is that the zero is only the **final Möbius output**.

Before applying `μ`, there is still a concrete value:

```text
φ^p(n) = t
```

and only then:

```text
μ(t)=0
```

So the full information chain is:

```text
coordinate n
↓
φ^p(n)=t
↓
μ(t)=0
```

The new rule is:

```text
μ(t)=0
does not imply
"t is lost"
```

Instead:

```text
0 removes the directional sign,
but t remains available as an unsigned structural value.
```

---

## 2. Retain the pre-Möbius layer

Define the pre-Möbius coordinate state:

```text
T_p(r,c)
=
( φ^p(r), φ^p(c) )
```

Then the ordinary selector is obtained by applying `μ` componentwise:

```text
V_p(r,c)
=
μ(T_p(r,c))
```

The route should therefore retain **both** layers:

```text
T_p(r,c) = numerical layer
V_p(r,c) = sign layer
```

Example notation:

```text
T_p = (6,4)
V_p = (+1,0)
```

or, in compact annotated form:

```text
(+1, 0[4])
```

where:

```text
0[4]
```

means:

```text
Möbius sign = 0
hidden pre-Möbius value = 4
```

This is **not** the statement:

```text
0 = 4
```

It means only:

```text
4 → μ(4)=0
```

and the value `4` is retained after its sign disappears.

---

## 3. Working interpretation

For a selector component:

```text
μ(t)=+1
```

or:

```text
μ(t)=-1
```

the component supplies a directional sign in the usual way.

For:

```text
μ(t)=0
```

the component supplies no sign, but the underlying value:

```text
t = φ^p(n)
```

remains structurally active.

So a partial selector such as:

```text
(+1,0)
```

should be read more precisely as something like:

```text
(+1, 0[t])
```

meaning:

```text
one directional constraint survives
+
one unsigned structural value survives
```

The exact role of `t` depends on the local geometry.

Observed uses include:

```text
radius
center value
local structural scale
```

The current evidence does **not** prove that every retained zero-value must always be used in the same way.

---

## 4. Example: THE → END

`THE` ends at:

```text
J(19,16)
```

with active phase:

```text
p=2
```

Before Möbius reduction:

```text
row:
19 → φ(19)=18 → φ(18)=6

column:
16 → φ(16)=8 → φ(8)=4
```

Therefore:

```text
T₂(19,16)=(6,4)
```

Now apply Möbius:

```text
μ(6)=+1
μ(4)=0
```

so:

```text
V₂(19,16)=(+1,0)
```

The old reading is only:

```text
DOWN-compatible
horizontal direction unresolved
```

The retained reading is:

```text
(+1, 0[4])
```

and the local continuation to `END` immediately uses radius-4 geometry:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

and:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

So the value hidden under the zero is:

```text
4
```

and the next route region is dominated by the same scale:

```text
radius 4
```

This is a supporting cross-check for retention.

---

## 5. Example: END → IS

`END` finishes at:

```text
I(21,23)
```

The active key state still has:

```text
p=2
```

Calculate the pre-Möbius coordinate layer.

Row:

```text
21
→ φ(21)=12
→ φ(12)=4
```

Column:

```text
23
→ φ(23)=22
→ φ(22)=10
```

Therefore:

```text
T₂(21,23)=(4,10)
```

Apply Möbius:

```text
μ(4)=0
μ(10)=+1
```

so:

```text
V₂(21,23)=(0,+1)
```

The ordinary selector says:

```text
RIGHT-compatible
vertical direction unresolved
```

But the retained form is:

```text
(0[4], +1)
```

Now look at the exact structure occupied by the endpoint:

```text
I(21,21) — R(21,22) — I(21,23)
```

Its center is:

```text
R = 4
```

So the value hidden under the zero:

```text
4
```

is immediately reproduced as the numerical value of the next mirror center.

This is stronger than a general radius coincidence:

```text
φ²(21)=4
↓
μ(4)=0
↓
END endpoint enters I-R-I
↓
R=4
```

---

## 6. Example: DEATH → SEE

`DEATH` ends at:

```text
E(26,1)
```

with:

```text
p=2
```

Calculate the underlying coordinate values.

Row:

```text
26
→ φ(26)=12
→ φ(12)=4
```

Column:

```text
1
→ φ(1)=1
→ φ(1)=1
```

Therefore:

```text
T₂(26,1)=(4,1)
```

Apply Möbius:

```text
μ(4)=0
μ(1)=+1
```

so:

```text
V₂(26,1)=(0,+1)
```

The retained form is:

```text
(0[4], +1)
```

The active key state is:

```text
M=(+1,0,+1)
```

which is already associated with:

```text
OUTER
```

The surviving coordinate sign gives:

```text
RIGHT-compatible
```

and the hidden coordinate value gives:

```text
4
```

So the local search constraints become:

```text
OUTER
+
RIGHT-compatible
+
structural value 4
```

The matching nearby mirror is:

```text
EA(25,2) —4— J(25,6) —4— EA(25,10)
```

or:

```text
EA-J-EA
```

This gives a direct local source for the `4` used after `DEATH`.

It is therefore stronger than deriving `4` indirectly from the number of recovered plaintext blocks:

```text
12 blocks
→ φ(12)=4
```

The block-count relation can remain a numerical cross-check, but it is no longer required as the primary route-selection mechanism.

---

## 7. Three consecutive appearances of the hidden 4

The late route gives three closely related examples:

| Endpoint | Phase | Pre-Möbius layer `T_p` | Selector `V_p` | Value hidden by `0` | Local continuation |
|---|---:|---|---|---:|---|
| `J(19,16)` after `THE` | `2` | `(6,4)` | `(+1,0)` | `4` | radius-4 `F-X-F` / `J-B-J` geometry |
| `I(21,23)` after `END` | `2` | `(4,10)` | `(0,+1)` | `4` | enters `I-R-I`, where `R=4` |
| `E(26,1)` after `DEATH` | `2` | `(4,1)` | `(0,+1)` | `4` | radius-4 `EA-J-EA` candidate for `SEE` |

The important repetition is not merely:

```text
0 appears three times
```

but:

```text
the same hidden value 4
appears under the zero
and is immediately relevant to the next local structure.
```

---

## 8. Relationship to the existing rules

This rule does not replace the coordinate selector.

It refines it.

The current division becomes:

```text
01 Core Mechanics
→ arithmetic / rune operations

02 Key Phase Selection
→ choose active key rotation

03 Totient Movement
→ movement magnitudes

04 Coordinate Selector
→ directional signs

05 Center / Outer States
→ structural role

06 Hidden Value Rule
→ preserve the unsigned value hidden beneath selector zero
```

The combined route logic can now be written as:

```text
active key
↓
phase p
↓
T_p(r,c) = (φ^p(r), φ^p(c))
↓
V_p(r,c) = μ(T_p)
↓

non-zero components
→ directional constraints

zero components
→ no directional sign
→ retain their pre-Möbius values

full key Möbius state
→ CENTER / OUTER role

local geometry
→ resolves the compatible structure
```

---

## 9. Important limitation

The evidence currently supports **retention**, not a universal interpretation of every retained value.

In particular, the rule should **not** be written as:

```text
selector zero means radius 4
```

That would be too specific and mathematically incorrect.

The correct rule is:

```text
if μ(φ^p(n))=0,
retain φ^p(n)
as an unsigned structural value.
```

For the strongest observed late-route cases:

```text
φ^p(n)=4
```

which is why:

```text
0[4]
```

repeats.

Other squareful pre-Möbius values could also produce `0` and would need to be tested separately.

---

## 10. Evidence status

The strongest evidence is:

```text
END → IS

φ²(21)=4
μ(4)=0
↓
I(21,23) is an outer of I-R-I
↓
R=4
```

and:

```text
DEATH → SEE

φ²(26)=4
μ(4)=0
↓
OUTER + RIGHT-compatible + 4
↓
EA(25,2) —4— J(25,6) —4— EA(25,10)
```

Together with the `THE → END` radius-4 cross-check, the repeated pattern suggests that Möbius zero is not an information-destroying state.

The current working rule is therefore:

# **Hidden Value Rule**

```text
A coordinate selector zero cancels directional sign,
not the pre-Möbius totient value that produced it.

If:

φ^p(n)=t
and
μ(t)=0,

then:

0 → direction unresolved
and
t → retained as an unsigned structural parameter.
```

This retained value can then be matched against the local mirror geometry together with the surviving coordinate sign and the active CENTER / OUTER state.
