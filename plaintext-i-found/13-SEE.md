# 13 — SEE

> **Recovered plaintext candidate:** `SEE`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE`  
> **Status:** strongest current post-`DEATH` candidate; still proposed, not officially verified.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. Starting state after DEATH

`DEATH` ends at:

```text
E(26,1)
```

The active pre-rotation structure is:

```text
J-T-J
```

with:

```text
signature = 10-8-10
M = (+1,0,+1)
phase = 2
```

The later route model associates:

```text
(+1,0,+1)
```

with an **OUTER-compatible** continuation.

The coordinate selector at the endpoint is:

```text
V₂(26,1)
=
( μ(φ²(26)), μ(φ²(1)) )
=
(0,+1)
```

So the next structure should be searched on a **RIGHT-compatible** side, while the vertical component remains unresolved.

---

## 2. Proposed route-selection rule: 12 → 4

The central rune of the 27×27 grid is:

```text
NG = 21
```

and:

```text
φ(21) = 12
```

This value already controls the earlier `TURNS → COLD` transition.

The route through `DEATH` can be grouped into 12 major recovered blocks:

```text
1. AS I GO THE
2. WEATHER
3. TURNS
4. COLD
5. I MAY
6. CRY
7. NOW THE
8. IDEA
9. OF THE
10. END
11. IS
12. DEATH
```

Applying `φ` again:

```text
φ(12) = 4
```

This suggests the post-`DEATH` search rule:

```text
OUTER-compatible
+
RIGHT-compatible
+
radius 4
```

This is the main new hypothesis of this chapter.

---

## 3. The matching radius-4 mirror

One cell up-right from `E(26,1)` is:

```text
EA(25,2)
```

and it is the left outer of the exact mirror:

```text
EA(25,2) —4— J(25,6) —4— EA(25,10)
```

So:

```text
EA-J-EA
```

matches all three filters:

```text
OUTER
RIGHT-compatible
radius 4
```

A scan of the standard horizontal, vertical, and 45° mirror axes finds this as the only standard `EA-J-EA` occurrence in the grid.

Therefore the proposed handoff is:

```text
E(26,1)
→ EA(25,2)
```

with the route-selection logic:

```text
M=(+1,0,+1)
→ OUTER

V₂=(0,+1)
→ RIGHT-compatible

φ(12)=4
→ radius 4
```

---

## 4. Generate the key

The center of:

```text
EA-J-EA
```

is:

```text
J = 11
```

Apply Euler's totient:

```text
φ(11)=10=I
```

Therefore:

```text
EA-J-EA
→
EA-I-EA
```

So the key is:

```text
KEY = EA-I-EA
```

Its totient signature is:

```text
φ(EA=28)=12
φ(I=10)=4
φ(EA=28)=12
```

therefore:

```text
12-4-12
```

This independently repeats the same:

```text
12 → 4
```

relation used to select the radius.

The Möbius state is:

```text
μ(12), μ(4), μ(12)
=
0,0,0
```

so:

```text
M=(0,0,0)
phase=0
```

and the key remains:

```text
EA-I-EA
```

---

## 5. Reuse the original J movement rule

The same `J` center already generated the first route movement:

```text
J = 11
φ(J)=10
φ(10)=4

10+4=14
```

So the old movement rule is reused unchanged:

```text
RIGHT 14
```

Starting from:

```text
EA(25,2)
```

gives:

```text
EA(25,2)
→ RIGHT 14
→ X(25,16)
```

The landing point is exact.

---

## 6. X(25,16) gives the ciphertext

`X(25,16)` is the center of the already known mirror:

```text
E(24,16)
X(25,16)
E(26,16)
```

or:

```text
E-X-E
```

This same structure was already used in the `I MAY → CRY` transition.

From `X(25,16)` the grid contains the direct diagonal:

```text
X(25,16)
EA(26,15)
B(27,14)
```

So:

```text
CIPHERTEXT = X-EA-B
```

A scan of all eight adjacent straight directions finds only one contiguous `X-EA-B` occurrence in the grid.

---

## 7. Decryption

Use the established rule:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: X   EA  B
Key:        EA  I   EA
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `X=14` | `EA=28` | `14-28 ≡ 15 = S` |
| 2 | `EA=28` | `I=10` | `28-10 = 18 = E` |
| 3 | `B=17` | `EA=28` | `17-28 ≡ 18 = E` |

Therefore:

```text
X-EA-B
-
EA-I-EA
=
S-E-E
```

# **SEE**

---

## 8. Why this branch is strong

The branch reuses old rules instead of creating new ones:

```text
1. DEATH has a fixed endpoint and phase.
2. M=(+1,0,+1) points to an OUTER-type continuation.
3. V₂(26,1)=(0,+1) restricts the search to the right-compatible side.
4. φ(NG=21)=12 and the route reaches DEATH after 12 major blocks.
5. φ(12)=4 matches the radius of EA-J-EA.
6. EA-J-EA compiles by the established center rule to EA-I-EA.
7. The key signature itself is 12-4-12.
8. The original J → 10 → 4 → 14 movement rule is reused.
9. RIGHT 14 lands exactly on the old E-X-E center X(25,16).
10. The unique contiguous X-EA-B line decrypts directly to SEE.
```

The readable word appears only after the route and key are selected.

---

## 9. What remains unproven

The main hypothesis is still:

```text
12 major route blocks
=
φ(NG)

↓
φ(12)=4

↓
use radius 4 as the next mirror scale
```

This gives a much cleaner explanation of:

```text
E(26,1) → EA(25,2)
```

than the earlier version, but it has not yet been independently confirmed at another macro-transition.

So the correct status is:

```text
SEE = strongest current continuation
12 → 4 radius rule = proposed missing route-selection rule
```

---

## 10. Next state

`SEE` ends at:

```text
B(27,14)
```

with key:

```text
EA-I-EA
```

and:

```text
M=(0,0,0)
phase=0
```

The post-`SEE` selector is:

```text
V₀(27,14)
=
(0,+1)
```

and the neutral state is interpreted as inheritance.

The inherited center gives:

```text
I=10
φ(I)=4
φ²(I)=2
```

so the next working movement is:

```text
RIGHT 2
```

toward:

```text
P(27,16)
```

which begins the next candidate word:

```text
YOU
```
