# 03 — Totient Movement

> **Purpose:** explain how values produced by Euler's totient function are reused as movement distances in the 27×27 grid.  
> This file explains **distance**, not direction. Direction selection is treated separately.

---

## 1. Basic idea

The route repeatedly reuses values already produced by the totient chain.

A value can first appear as:

```text
φ(center)
```

or inside a:

```text
totient signature
```

and later reappear as a movement distance.

So the observed pattern is:

```text
derived totient value
↓
movement distance
↓
new structural location
```

This does **not** mean that every totient value is always used for movement.

The exact activation rule is still unresolved.

---

## 2. First movement: 10 + 4 = 14

The first key-generating center is:

```text
J = 11
```

Apply Euler's totient:

```text
φ(11)=10=I
```

Then apply `φ` again:

```text
φ(10)=4
```

The two values are combined:

```text
10+4=14
```

and used as:

```text
RIGHT 14
```

This leads from the first structure to the ciphertext for:

```text
AS I GO THE
```

So the first observed movement chain is:

```text
J
↓
φ(J)=10
↓
φ(10)=4
↓
10+4=14
↓
movement distance 14
```

---

## 3. A transformed center reused directly

At the next mirror:

```text
X-OE-X
```

the center is:

```text
OE = 22
```

and:

```text
φ(22)=10=I
```

The same `10` is then reused directly as movement:

```text
RIGHT 10
```

which lands on:

```text
NG(14,14)
```

the exact center of the 27×27 grid.

So here:

```text
φ(center)=10
```

serves both as:

```text
key transformation
and
movement distance
```

---

## 4. Reusing 10 and 4 together

The values:

```text
10
and
4
```

remain active at:

```text
A(14,19)
```

They are reused as two movement magnitudes:

```text
UP 10
RIGHT 4
```

These movements locate:

```text
NG(14,23)
```

and the related structure:

```text
H-NG-C
```

used for:

```text
TURNS
```

The important point is that the values are not newly generated at this stage.

They are carried forward from the earlier totient chain:

```text
J
→ 10
→ 4
```

---

## 5. A new center generates a new movement value

The center of:

```text
H-NG-C
```

is:

```text
NG = 21
```

Apply Euler's totient:

```text
φ(21)=12
```

The same value is then used twice from:

```text
A(14,19)
```

as:

```text
DOWN 12
LEFT 12
```

These two movements locate:

```text
H-TH-H
```

and:

```text
G(14,7)
```

which together produce the next stage:

```text
COLD
```

So:

```text
NG=21
↓
φ(NG)=12
↓
movement distance 12
```

---

## 6. Signature values can become movement values

Movement is not limited to a single transformed center.

For:

```text
H-U-H
```

the totient signature is:

```text
4-1-4
```

After `COLD`, the route reuses:

```text
4
and
1
```

as movement distances:

```text
DOWN 4
RIGHT 1
```

Starting from:

```text
A(11,7)
```

this gives:

```text
A(11,7)
→ DOWN 4
→ S(15,7)
→ RIGHT 1
→ B(15,8)
```

`B(15,8)` is the center of:

```text
NG-B-NG
```

which generates the key for:

```text
I MAY
```

This establishes a second movement source:

```text
totient signature
↓
selected signature values
↓
movement distances
```

---

## 7. The value 6 persists across several roles

For:

```text
E-G-E
```

the signature is:

```text
6-2-6
```

The outer value:

```text
6
```

is reused as movement:

```text
X(25,16)
→ UP 6
→ J(19,16)
```

which leads to:

```text
CRY
```

After `CRY`, the same `6` continues to appear as:

```text
radius of S-IA-S
φ²(IA)=6
radius of TH-IA-TH
movement UP 6
```

So this chain is:

```text
signature value 6
↓
movement 6
↓
mirror radius 6
↓
φ²(center)=6
↓
companion mirror radius 6
↓
movement 6
```

This is one of the strongest examples of a totient-derived value persisting across multiple structural roles.

---

## 8. Totient inheritance

The repeated reuse of earlier values is called here:

```text
totient inheritance
```

or:

```text
totient chain
```

The observed behavior is:

```text
derive value
↓
use value cryptographically
↓
carry value forward
↓
reuse it geometrically
```

Known examples include:

```text
10, 4
12
4, 1
6
```

However, the current model does not yet contain a complete universal rule that decides:

```text
when a value remains active
which value is inherited
when it should become movement
```

Those points remain part of the route-selection problem.

---

## 9. Distance is not direction

This distinction is important.

Totient-derived values explain:

```text
how far
```

the route moves.

They do not by themselves always explain:

```text
which direction
```

For example:

```text
10
4
12
6
```

can provide movement magnitudes, while the choice between:

```text
UP
DOWN
LEFT
RIGHT
```

requires another layer.

That directional layer is explained separately in:

```text
04-coordinate-selector.md
```

---

## 10. Compact model

```text
center / key
↓
Euler φ
↓
totient value or signature
↓
value remains structurally active
↓
movement magnitude
↓
new node / mirror / ciphertext
```

Observed examples:

```text
J → 10 → 4 → 14
OE → 10
NG → 12
H-U-H → 4-1-4
E-G-E → 6-2-6
```

The stable claim is therefore:

> **Totient-derived values repeatedly act as movement magnitudes in the recovered route.**

The unresolved question is not whether this happens, but the exact rule that determines **when and which value is activated for the next movement**.
