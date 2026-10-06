# 05 — Center / Outer States

> **Purpose:** explain how the full Möbius state of a symmetric 3-rune key can indicate whether the next important route position behaves as a **CENTER** or an **OUTER** point.

---

## 1. Why phase is not enough

The key phase uses the sum of three Möbius values:

```text
p = [a+b+c] mod 3
```

But this compresses the full state into only one number:

```text
0
1
2
```

The full Möbius pattern keeps more information.

For a symmetric key, write:

```text
M = (a,b,a)
```

where:

```text
a = μ(φ(outer rune))
b = μ(φ(center rune))
```

This full pattern can distinguish structures that may share the same phase.

---

## 2. The two strongest observed states

Two patterns repeat cleanly across the recovered route:

```text
(0,+1,0)  → CENTER
(+1,0,+1) → OUTER
```

These are not arbitrary labels.

They describe the structural role occupied by the next important endpoint.

---

## 3. CENTER state

The strongest CENTER pattern is:

```text
M = (0,+1,0)
```

Working interpretation:

```text
the next route endpoint is the center
of a mirrored structure
```

This appears repeatedly.

---

## 4. CENTER example: COLD

The active structure is:

```text
H-U-H
```

Its totient signature is:

```text
4-1-4
```

Apply Möbius:

```text
μ(4)=0
μ(1)=+1
μ(4)=0
```

so:

```text
M=(0,+1,0)
```

The plaintext is:

```text
COLD
```

and the endpoint is:

```text
A(11,7)
```

That cell is the center of:

```text
EA(10,7)
A(11,7)
EA(12,7)
```

So the observed relation is:

```text
(0,+1,0)
→ COLD
→ endpoint is CENTER
```

---

## 5. CENTER example: IDEA

The key structure is:

```text
A-U-A
```

with signature:

```text
8-1-8
```

Apply Möbius:

```text
μ(8)=0
μ(1)=+1
μ(8)=0
```

therefore:

```text
M=(0,+1,0)
```

The plaintext is:

```text
IDEA
```

and its endpoint is:

```text
D(17,18)
```

which is the center of:

```text
J(15,20)
D(17,18)
J(19,16)
```

Again:

```text
(0,+1,0)
→ endpoint is CENTER
```

---

## 6. CENTER example: IS

The active structure is:

```text
H-TH-H
```

Its signature is:

```text
4-1-4
```

so again:

```text
M=(0,+1,0)
```

The plaintext is:

```text
IS
```

and the endpoint:

```text
D(21,10)
```

is the center of:

```text
E(19,12)
D(21,10)
E(23,8)
```

This gives a third independent occurrence of the same pattern.

---

## 7. CENTER rule

The repeated observation is:

```text
(0,+1,0)
↓
CENTER-active
↓
next endpoint occupies the center
of a mirrored structure
```

This is one of the strongest state correspondences in the current model.

---

## 8. OUTER state

The strongest OUTER pattern is:

```text
M=(+1,0,+1)
```

Working interpretation:

```text
the next important endpoint occupies
an outer position of a mirrored structure
```

This also repeats.

---

## 9. OUTER example: WEATHER

The active symmetric key structure is:

```text
X-I-X
```

Its totient signature is:

```text
6-4-6
```

Apply Möbius:

```text
μ(6)=+1
μ(4)=0
μ(6)=+1
```

so:

```text
M=(+1,0,+1)
```

The plaintext is:

```text
WEATHER
```

and its endpoint is:

```text
E(14,18)
```

That cell is an outer point of the diagonal mirrored structure:

```text
E(6,10)
   \
    \
     NG(10,14)
        \
         \
          E(14,18)
```

with equal radius:

```text
E(6,10)
— 4 diagonal steps —
NG(10,14)
— 4 diagonal steps —
E(14,18)
```

Therefore:

```text
(+1,0,+1)
→ WEATHER
→ endpoint is OUTER
```

A full scan of the 27×27 grid over horizontal, vertical, and both 45° diagonal symmetric 3-rune structures, at all possible integer radii, finds exactly **one** `E-NG-E` mirror:

```text
E(6,10) — NG(10,14) — E(14,18)
```

So the `WEATHER` endpoint is not one of several competing `E-NG-E` mirrors. It gives an additional direct occurrence of the same OUTER-state rule.

---

## 10. OUTER example: NOW THE

The active structure is:

```text
OE-I-OE
```

Its signature is:

```text
10-4-10
```

Apply Möbius:

```text
μ(10)=+1
μ(4)=0
μ(10)=+1
```

so:

```text
M=(+1,0,+1)
```

The plaintext is:

```text
NOW THE
```

and the endpoint is:

```text
J(15,20)
```

That cell is an outer point of:

```text
J(15,20)
D(17,18)
J(19,16)
```

Therefore:

```text
(+1,0,+1)
→ endpoint is OUTER
```

---

## 11. OUTER example: END

The active structure is:

```text
J-T-J
```

Its signature is:

```text
10-8-10
```

Apply Möbius:

```text
μ(10)=+1
μ(8)=0
μ(10)=+1
```

so:

```text
M=(+1,0,+1)
```

The plaintext is:

```text
END
```

and the endpoint:

```text
I(21,23)
```

is an outer point of:

```text
I(21,21)
R(21,22)
I(21,23)
```

Again:

```text
(+1,0,+1)
→ endpoint is OUTER
```

---

## 12. OUTER rule

The repeated observation is:

```text
(+1,0,+1)
↓
OUTER-active
↓
next endpoint occupies an outer
position of a mirrored structure
```

This is the second strongest state correspondence in the current model.

---

## 13. Other observed states

Other symmetric Möbius states also appear, but their meanings are less secure.

### Neutral

```text
(0,0,0)
```

Current working meaning:

```text
INHERIT / no local role selector
```

This suggests that the route may preserve an earlier structural value or role instead of choosing a new CENTER / OUTER state locally.

This remains provisional.

---

### Reflect-like state

```text
(+1,-1,+1)
```

Current working meaning:

```text
REFLECT
or
propagate OUTER
```

This appears in the `E-G-E` state:

```text
6-2-6
→ (+1,-1,+1)
```

The later route reuses the outer value `6` through movement and mirror geometry.

The exact semantic rule is still unresolved.

---

### Homogeneous state

```text
(+1,+1,+1)
```

Current working meaning:

```text
SWAP
or
role equivalence
```

This is weaker than the CENTER / OUTER correspondence and should remain provisional.

---

## 14. Negative partner states

Each non-neutral symmetric state has a sign-reversed partner:

```text
(0,+1,0)    ↔ (0,-1,0)

(+1,0,+1)   ↔ (-1,0,-1)

(+1,-1,+1)  ↔ (-1,+1,-1)

(+1,+1,+1)  ↔ (-1,-1,-1)
```

The recovered route currently uses the positive forms.

The negative forms have not yet been observed clearly enough to assign exact route behavior.

So they should be treated as:

```text
predicted partner states
not established movement rules
```

---

## 15. State classes

The current working classification is:

```text
000
→ NEUTRAL / INHERIT
→ provisional

±010
→ CENTER class
→ strong for +010

±101
→ OUTER class
→ strong for +101

±(1,-1,1)
→ REFLECT / OUTER-PROPAGATION class
→ provisional

±111
→ SWAP / ROLE-EQUIVALENCE class
→ provisional
```

The sign may encode polarity or orientation, but that interpretation is not yet proven.

---

## 16. Relationship to phase

For symmetric states:

```text
M=(a,b,a)
```

the phase is:

```text
p = (b-a) mod 3
```

So CENTER / OUTER state and key phase are related, but they are not the same thing.

Example:

```text
M=(0,+1,0)
→ p=1
→ CENTER class
```

while:

```text
M=(+1,0,+1)
→ p=2
→ OUTER class
```

The phase controls:

```text
key rotation
and
coordinate layer
```

while the full state appears to preserve:

```text
structural role information
```

---

## 17. Why this matters for route selection

The coordinate selector can tell us:

```text
which directional branch is compatible
```

Totient movement can tell us:

```text
how far to move
```

The CENTER / OUTER state adds another constraint:

```text
what kind of structural position
the route should arrive at
```

So the combined logic becomes:

```text
totient values
→ movement scale

phase + coordinates
→ directional branch

full Möbius state
→ CENTER / OUTER structural role
```

This sharply reduces the number of plausible next-route candidates.

---

## 18. Evidence status

Strongly supported:

```text
(0,+1,0)  → CENTER
(+1,0,+1) → OUTER
```

because both patterns repeat across independent stages.

Still provisional:

```text
000
(+1,-1,+1)
(+1,+1,+1)
negative partner states
```

These should not yet be treated as fully deterministic rules.

---

## 19. Compact model

```text
3-rune key
↓
totient signature
↓
full Möbius state M
↓
structural role
```

Observed strongest mappings:

```text
(0,+1,0)
→ CENTER

(+1,0,+1)
→ OUTER
```

This is the current state-role layer of the route model.
