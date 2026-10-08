# 06 — Hidden Value Rule

A **zero in the coordinate selector removes a directional sign, not the number that produced it**. The Hidden Value Rule keeps that earlier number available when the route encounters a partial or null selector. In three late-stage transitions, the value concealed by a zero is **4**, and each continuation contains a nearby mirror whose geometry or center also uses **4**.

This rule extends [`04-coordinate-selector.md`](./04-coordinate-selector.md). It does not replace the selector or the CENTER / OUTER constraints described in [`05-center-outer-states.md`](./05-center-outer-states.md).

## 1. What remains when Möbius returns zero

The coordinate selector uses the key's active phase `p` and the current position `(r,c)`:

```text
Vₚ(r,c) = (μ(φᵖ(r)), μ(φᵖ(c)))
```

Each component becomes `−1`, `0`, or `+1`. A nonzero result supplies a direction: for rows, `−1` means UP and `+1` means DOWN; for columns, `−1` means LEFT and `+1` means RIGHT. A zero supplies **no direction on that axis**.

But the Möbius result is the final step of a longer calculation. Before applying `μ`, the totient layer has already produced a specific integer `t`:

```text
coordinate n → φᵖ(n) = t → μ(t)
```

For example, `μ(4)=0` because **4 contains a squared prime factor** (`4=2²`). The sign becomes zero, but the preceding calculation still produced the number **4**. The Hidden Value Rule proposes retaining that number as an **unsigned structural parameter** when looking for the next compatible mirror.

To keep the two layers distinct, define:

```text
Tₚ(r,c) = (φᵖ(r), φᵖ(c))       numerical layer
Vₚ(r,c) = (μ(φᵖ(r)), μ(φᵖ(c)))  directional layer
```

The active phase is unchanged; both calculations use the phase already selected for the key. `μ` is applied to the two entries of `Tₚ` separately to obtain `Vₚ`.

If the result is:

```text
T₂ = (6,4)
V₂ = (+1,0)
```

we can annotate it as **`(+1,0[4])`**. The notation `0[4]` means that the direction is unresolved on this axis while its pre-Möbius value was **4**. It does **not** mean `0=4`, nor does it turn that zero into a directional command. The next structure must still be checked against the grid.

## 2. OF THE → END: a zero retains the mirror radius

The ciphertext for **THE**, at the end of [`09-OF-THE.md`](../plaintext-i-found/09-OF-THE.md), finishes at **J(19,16)**. Its key has phase **2**, so each coordinate passes through Euler's totient twice before Möbius:

```text
Row:    19 → φ(19)=18 → φ(18)=6
Column: 16 → φ(16)=8  → φ(8)=4

T₂(19,16) = (6,4)

μ(6) = +1
μ(4) =  0

V₂(19,16) = (+1,0) = (+1,0[4])
```

The selector retains a **DOWN-compatible** sign, but gives no horizontal direction. At the same time, its unresolved column contains the value **4**. The continuation to [`10-END.md`](../plaintext-i-found/10-END.md) contains two exact mirrors of that radius.

Immediately left of the final `J` is **F(19,15)**, an outer of the horizontal mirror:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

The final `J` itself is the upper outer of a diagonal mirror:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

Both structures use **4 steps from center to outer**. The `F-X-F` structure leads toward the ciphertext for `END`, while `J-B-J` supplies its key. Thus the same value that becomes invisible in the column's directional sign matches the scale of **both connected route structures**. The selector alone does not determine the full path; the mirrors supply the missing geometric information.

## 3. END → IS: the hidden value becomes a mirror center

[`10-END.md`](../plaintext-i-found/10-END.md) ends at **I(21,23)** with the same active phase **2**. This time the zero appears in the **row** component:

```text
Row:    21 → φ(21)=12 → φ(12)=4
Column: 23 → φ(23)=22 → φ(22)=10

T₂(21,23) = (4,10)

μ(4)  = 0
μ(10) = +1

V₂(21,23) = (0,+1) = (0[4],+1)
```

The surviving sign is **RIGHT-compatible**, with vertical direction unresolved. The retained row value is again **4**. Now examine the exact mirror containing the final ciphertext cell:

```text
I(21,21) — R(21,22) — I(21,23)
                                  ↑
                              END endpoint
```

This is an `I-R-I` mirror, and its **center rune `R` has value 4** in the 0-based Gematria Primus system:

```text
φ²(21) = 4
μ(4)   = 0
R      = 4
```

Here the retained number does **not** appear as a radius. Instead, it matches the numerical value of the center of the mirror already occupied by the `END` endpoint. This is the local structure from which the route continues toward [`11-IS.md`](../plaintext-i-found/11-IS.md).

The distinction matters: **the rule retains a number; the local geometry determines what that number can describe**.

## 4. DEATH → SEE: a hidden 4 helps identify the next mirror

[`12-DEATH.md`](../plaintext-i-found/12-DEATH.md) finishes at **E(26,1)**. Its key again has phase **2**, with full Möbius state **`(+1,0,+1)`**, the pattern associated with an **OUTER** position in the project's route model.

At the endpoint, the coordinate calculation gives:

```text
Row:    26 → φ(26)=12 → φ(12)=4
Column:  1 → φ(1)=1   → φ(1)=1

T₂(26,1) = (4,1)

μ(4) = 0
μ(1) = +1

V₂(26,1) = (0,+1) = (0[4],+1)
```

Three constraints can now be considered together: **OUTER** from the key state, **RIGHT-compatible** from the surviving column sign, and **4** retained from the unresolved row component.

One step diagonally up-right from `E(26,1)` lies **EA(25,2)**. It is the left outer of an exact horizontal mirror:

```text
EA(25,2) —4— J(25,6) —4— EA(25,10)
    ↑
  OUTER
```

The mirror is `EA-J-EA`, and its radius is **4**. Its left outer lies on the right-compatible side of the `DEATH` endpoint, matching the structural role indicated by the full Möbius state. This provides a local source for the radius used to open [`13-SEE.md`](../plaintext-i-found/13-SEE.md).

An earlier interpretation also noticed that the plaintext through `DEATH` forms **12 route blocks**, with `φ(12)=4`. That remains a numerical cross-check, but **the pre-Möbius coordinate value `φ²(26)=4` supplies the more direct local connection**. There is no need to derive the search radius from the number of chapters.

The move to `EA(25,2)` also illustrates why a surviving sign is a **compatibility constraint**, not necessarily a literal single-axis instruction: the row sign is unresolved, so the geometry can supply the upward part of a diagonal approach.

## 5. What the three appearances of 4 establish

The three cases can be compared without conflating a geometric radius with a rune's numerical value:

| Transition | Endpoint | `T₂` | `V₂` | Where the retained `4` appears |
|---|---|---|---|---|
| [`OF THE → END`](../plaintext-i-found/10-END.md) | `J(19,16)` | `(6,4)` | `(+1,0)` | Radius of `F-X-F` and `J-B-J` |
| [`END → IS`](../plaintext-i-found/11-IS.md) | `I(21,23)` | `(4,10)` | `(0,+1)` | Center rune `R=4` of `I-R-I` |
| [`DEATH → SEE`](../plaintext-i-found/13-SEE.md) | `E(26,1)` | `(4,1)` | `(0,+1)` | Radius of `EA-J-EA` |

In all three cases, **the coordinate component reduced to zero had the pre-Möbius value 4**, and the next local structure contains a matching numerical or geometric feature. The examples support retaining that value for structural comparison. They do not establish that every zero must indicate radius 4—or that a match by itself uniquely determines the next step.

Mathematically, `μ(t)=0` whenever `t` is divisible by the square of a prime. Other values besides 4 can therefore occur beneath a zero, including **8** and **12**. The general rule is to retain **the actual `φᵖ(n)`**, not to substitute 4 automatically.

## 6. How the rule fits the route

Each earlier rule supplies a different part of the search. [`02-key-phase-selection.md`](./02-key-phase-selection.md) establishes the active phase; [`03-totient-movement.md`](./03-totient-movement.md) explains inherited movement magnitudes; [`04-coordinate-selector.md`](./04-coordinate-selector.md) converts phase and coordinates into directional constraints; and [`05-center-outer-states.md`](./05-center-outer-states.md) relates the full key state to mirror roles.

The **Hidden Value Rule** adds one instruction: **keep the numerical value before Möbius reduction whenever the selector returns zero**. Match it against nearby mirror radii, center rune values, or other explicitly identifiable structural scales, while respecting the surviving signs and CENTER / OUTER information.

This is a rule for **preserving a candidate constraint**, not a theorem that every retained value has a single fixed meaning. The three observed transitions give concrete tests of the idea; determining when a particular hidden value should be activated remains part of the broader route-selection problem.
