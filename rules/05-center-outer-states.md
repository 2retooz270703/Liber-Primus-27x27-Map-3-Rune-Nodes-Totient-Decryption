# 05 — Center / Outer States

The Möbius calculation does more than rotate a key. Its three individual values form a **state** that can be compared with the geometric role of the next ciphertext endpoint. In the route examined here, two patterns recur: **`(0,+1,0)` accompanies a CENTER endpoint**, while **`(+1,0,+1)` accompanies an OUTER endpoint**.

This adds a structural question to the earlier rules. [`03-totient-movement.md`](./03-totient-movement.md) examines **how far** to move, and [`04-coordinate-selector.md`](./04-coordinate-selector.md) examines **which directions** are compatible. The full Möbius state helps identify **what kind of position** is relevant when the route reaches another mirror.

## 1. Keep the whole Möbius state, not only its sum

For a generated three-rune key `k₁-k₂-k₃`, first calculate the totient signature, then apply the Möbius function to each entry:

```text
Totient signature: (φ(k₁), φ(k₂), φ(k₃))
Möbius state M:    (μ(φ(k₁)), μ(φ(k₂)), μ(φ(k₃)))
```

The key-phase rule, explained in [`02-key-phase-selection.md`](./02-key-phase-selection.md), **adds those three values modulo 3**:

```text
M = (a,b,c)
p = (a + b + c) mod 3
```

The phase is sufficient to decide how the key rotates, but it discards the positions of the individual signs. For a **symmetric key** `outer-center-outer`, the full state has the form:

```text
M = (a,b,a)

a = μ(φ(outer rune))
b = μ(φ(center rune))
```

Here, the distinction between the **middle** and the **two outer** entries can be meaningful. It allows the model to distinguish a state that emphasizes the center from one that emphasizes the outers, even if the two states produce the same numerical phase.

## 2. CENTER: the pattern (0,+1,0)

In this state, the two outer entries have Möbius value **0** and the center has **+1**. The route repeatedly ends its ciphertext at the **center of a different mirrored structure** after using this type of key.

### COLD: the final A is a mirror center

[`04-COLD.md`](../plaintext-i-found/04-COLD.md) transforms `H-TH-H` into `H-U-H`. Its arithmetic is:

```text
H-U-H
φ → (4,1,4)
μ → (0,+1,0)
```

`COLD` ends at **A(11,7)**, which is the center of a vertical `EA-A-EA` mirror:

```text
EA(10,7)
   |
 A(11,7)  ← COLD endpoint; CENTER
   |
EA(12,7)
```

Thus the key's full state is `(0,+1,0)`, and the final ciphertext cell occupies a **CENTER** position in the next local structure.

### IDEA: the final D is the center of J-D-J

[`08-IDEA.md`](../plaintext-i-found/08-IDEA.md) uses the transformed key `A-U-A`:

```text
A-U-A
φ → (8,1,8)
μ → (0,+1,0)
```

The ciphertext ends at **D(17,18)**. This is the center of the diagonal mirror:

```text
J(15,20) ── 2 ── D(17,18) ── 2 ── J(19,16)
                     ↑
                IDEA endpoint
```

The same three-valued state therefore coincides with another **CENTER** endpoint. The two outer `J` cells also connect this mirror to the surrounding route: `J(15,20)` ends `NOW THE`, while `J(19,16)` was used in its key-generation geometry.

### IS: the final D is the center of E-D-E

[`11-IS.md`](../plaintext-i-found/11-IS.md) generates `H-TH-H` from a nearby `H-R-H` mirror. Its signature and state are:

```text
H-TH-H
φ → (4,1,4)
μ → (0,+1,0)
```

`IS` ends at **D(21,10)**, the center of another diagonal mirror:

```text
E(19,12) ── 2 ── D(21,10) ── 2 ── E(23,8)
                     ↑
                 IS endpoint
```

Here the role is again **CENTER**. Across `COLD`, `IDEA`, and `IS`, the same Möbius arrangement is followed by a ciphertext endpoint that is the **middle rune of a mirror**, despite the different locations and key structures.

## 3. OUTER: the pattern (+1,0,+1)

This state reverses the distribution: the **outer entries are +1**, while the center is **0**. In three recorded stages, the ciphertext ends on an **outer rune** of a nearby mirrored structure rather than at its center.

### WEATHER: the outer E of a diagonal E-NG-E

[`02-WEATHER.md`](../plaintext-i-found/02-WEATHER.md) generates `X-I-X`:

```text
X-I-X
φ → (6,4,6)
μ → (+1,0,+1)
```

The word ends at **E(14,18)**. That cell is one outer of a diagonal mirror with radius **4 diagonal steps**:

```text
E(6,10) ── 4 ── NG(10,14) ── 4 ── E(14,18)
                                          ↑
                                    WEATHER endpoint
```

The project's reported scan of the **27×27 grid**, covering horizontal, vertical, and both 45-degree diagonal symmetric triples at all integer radii, finds **one `E-NG-E` mirror**: precisely this one. This makes the identified outer position particularly specific within that geometric search.

### NOW THE: the outer J of J-D-J

[`07-NOW-THE.md`](../plaintext-i-found/07-NOW-THE.md) uses `OE-I-OE` as its transformed key:

```text
OE-I-OE
φ → (10,4,10)
μ → (+1,0,+1)
```

The last ciphertext rune is **J(15,20)**, an outer of the same `J-D-J` mirror encountered in `IDEA`:

```text
J(15,20) ── 2 ── D(17,18) ── 2 ── J(19,16)
    ↑
NOW THE endpoint; OUTER
```

This gives a useful paired observation: **`NOW THE` ends at an OUTER of `J-D-J`, whereas `IDEA` ends at its CENTER**. Their corresponding key states are `(+1,0,+1)` and `(0,+1,0)` respectively. The distinction is visible within one and the same mirror, not merely across unrelated structures.

### END: the outer I of I-R-I

[`10-END.md`](../plaintext-i-found/10-END.md) generates `J-T-J`:

```text
J-T-J
φ → (10,8,10)
μ → (+1,0,+1)
```

The word ends at **I(21,23)**, the right outer of a small horizontal mirror:

```text
I(21,21) ── 1 ── R(21,22) ── 1 ── I(21,23)
                                          ↑
                                    END endpoint; OUTER
```

The `R(21,22)` center subsequently connects the `I-R-I` mirror to the larger `H-R-H` structure used in `IS`. Again, the ciphertext ends at an **OUTER** after a key state of `(+1,0,+1)`.

## 4. What the six endpoint checks show

The direct comparisons are easiest to see side by side:

| Stage | Generated key | Möbius state | Final ciphertext cell | Role in the connected mirror |
|---|---|---|---|---|
| [COLD](../plaintext-i-found/04-COLD.md) | `H-U-H` | `(0,+1,0)` | `A(11,7)` | **CENTER** of `EA-A-EA` |
| [IDEA](../plaintext-i-found/08-IDEA.md) | `A-U-A` | `(0,+1,0)` | `D(17,18)` | **CENTER** of `J-D-J` |
| [IS](../plaintext-i-found/11-IS.md) | `H-TH-H` | `(0,+1,0)` | `D(21,10)` | **CENTER** of `E-D-E` |
| [WEATHER](../plaintext-i-found/02-WEATHER.md) | `X-I-X` | `(+1,0,+1)` | `E(14,18)` | **OUTER** of `E-NG-E` |
| [NOW THE](../plaintext-i-found/07-NOW-THE.md) | `OE-I-OE` | `(+1,0,+1)` | `J(15,20)` | **OUTER** of `J-D-J` |
| [END](../plaintext-i-found/10-END.md) | `J-T-J` | `(+1,0,+1)` | `I(21,23)` | **OUTER** of `I-R-I` |

These are **endpoint correspondences**: they compare a key's calculated state with the geometric role of the **last ciphertext rune**. They do not, by themselves, prove that the state uniquely chooses a mirror or guarantees a valid next move. Their value is that the role assignments repeat across different words and that `NOW THE → IDEA` exhibits both roles in the same `J-D-J` geometry.

The two strongest working associations are therefore:

```text
(0,+1,0)  → CENTER-compatible
(+1,0,+1) → OUTER-compatible
```

## 5. Other symmetric states and their possible roles

The route also contains other full Möbius states. Their interpretation is less constrained by repeated endpoint examples, so they are useful as **working classifications**, not yet as deterministic instructions.

| State | Working interpretation | What is observed or proposed |
|---|---|---|
| `(0,0,0)` | **NEUTRAL / INHERIT** | No local CENTER/OUTER indication; earlier values or roles may carry forward. |
| `(+1,-1,+1)` | **REFLECT / propagate OUTER** | The `E-G-E` signature `(6,2,6)` yields this state in `CRY`; its outer value `6` is reused in movement and later mirror radii. |
| `(+1,+1,+1)` | **SWAP / role equivalence** | A possible class for changes or equivalences of structural roles; its precise geometric action has not been established. |

The `CRY` example makes the **REFLECT** label understandable without treating it as a proven instruction. Its key has:

```text
E-G-E
φ → (6,2,6)
μ → (+1,-1,+1)
```

The outer **6** is used to move from `X(25,16)` to `J(19,16)`. After `CRY`, the same **6** reappears in the radii of `S-IA-S` and `TH-IA-TH`, and in the movement to the starting `TH` of `NOW THE`. The numeric connection is observable; the exact general meaning of the complete `(+1,-1,+1)` pattern remains open.

Each non-neutral symmetric state also has a **sign-reversed partner**:

```text
(0,+1,0)    ↔ (0,-1,0)
(+1,0,+1)   ↔ (-1,0,-1)
(+1,-1,+1)  ↔ (-1,+1,-1)
(+1,+1,+1)  ↔ (-1,-1,-1)
```

Only the **positive forms** above have the stated route examples here. The negative partners are possible states of the arithmetic, but their corresponding CENTER, OUTER, reflection, or reversal behavior is **not established** by the examples in this file. In particular, changing the signs should not automatically be interpreted as reversing a movement direction.

## 6. Why the full state matters even when the phase is known

For a symmetric state `M=(a,b,a)`, the key-phase formula simplifies to:

```text
p = (a+b+a) mod 3
  = (2a+b) mod 3
  = (b-a) mod 3
```

For the two strongest examples:

```text
CENTER: (0,+1,0)  → p = 1
OUTER:  (+1,0,+1) → p = 2
```

But phase and state are **not interchangeable**. For instance, the `CRY` state `(+1,-1,+1)` also yields **phase 1**:

```text
(+1,-1,+1) → (1-1+1) mod 3 = 1
(0,+1,0)   → (0+1+0) mod 3 = 1
```

Those two patterns produce the **same key rotation** but retain different distributions of Möbius signs. Similarly, `(0,0,0)` and `(+1,+1,+1)` both have phase 0. That is why the complete three-value state is worth retaining after calculating `p`.

The functions of these layers remain distinct: **phase** rotates the key and selects a coordinate layer; **totient inheritance** supplies candidate distances; **the coordinate selector** constrains direction; and **the full Möbius state** provides a potential CENTER/OUTER constraint on the next relevant mirror position.

## 7. Using the state as a route constraint

When a candidate continuation reaches a mirrored triple, check whether the proposed endpoint role matches the current state's strongest association:

- With **`(0,+1,0)`**, test whether the endpoint lies at a mirror's **center**.
- With **`(+1,0,+1)`**, test whether the endpoint lies at one of a mirror's **outer** positions.

A matching role can strengthen a candidate already supported by the ciphertext, totient-derived distances, and local geometry. It should not replace those independent conditions or be used to select a destination solely because that destination yields an appealing word.

The repeated CENTER and OUTER matches provide the clearest evidence for this layer of the model. The neutral, reflection-like, homogeneous, and negative-partner states remain less fully specified. The next rule, [`06-hidden-value-rule.md`](./06-hidden-value-rule.md), examines how values already present in one structure can remain active as the route moves to another.
