# 05 — I MAY

> **Recovered plaintext:** `I MAY`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

This chapter starts from the exact endpoint of `COLD`:

```text
A(11,7)
```

The key used for `COLD` was:

```text
H-U-H
```

and its totient signature was:

```text
4-1-4
```

The `I MAY` stage reuses that inherited numerical state to leave the `COLD` endpoint, locate a new hidden key, and then return to a preserved structure from the previous chapter.

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

---

## 1. The state left behind by COLD

`COLD` ended at:

```text
A(11,7)
```

The parent node that generated the `COLD` key was:

```text
H-TH-H
```

which compiled to:

```text
H-U-H
```

because:

```text
TH = 2
φ(2) = 1 = U
```

The key's totient signature is:

```text
φ(H=8) = 4
φ(U=1) = 1
φ(H=8) = 4
```

so:

```text
H-U-H → 4-1-4
```

That gives the post-`COLD` state:

```text
endpoint:          A(11,7)
parent structure:  H-TH-H
active key family: H-U-H
inherited signal:  4-1-4
```

---

## 2. The COLD endpoint is already inside a new mirror

The endpoint:

```text
A(11,7)
```

is the center of this vertical structure:

```text
EA(10,7)
   |
A(11,7)
   |
EA(12,7)
```

or:

```text
EA-A-EA
```

Now calculate its totient signature:

```text
φ(EA=28) = 12
φ(A=24)  = 8
φ(EA=28) = 12
```

Therefore:

```text
EA-A-EA → 12-8-12
```

Keep that fingerprint:

```text
12-8-12
```

It will reappear in the key found a few steps later.

---

## 3. Reuse the inherited 4-1-4 movement signal

Start from:

```text
A(11,7)
```

Reuse the inherited values from:

```text
H-U-H → 4-1-4
```

The recorded movement is:

```text
DOWN 4
RIGHT 1
```

First:

```text
A(11,7) → DOWN 4 → S(15,7)
```

because:

```text
11 + 4 = 15
```

Then:

```text
S(15,7) → RIGHT 1 → B(15,8)
```

So the complete movement is:

```text
A(11,7)
   ↓ DOWN 4
S(15,7)
   ↓ RIGHT 1
B(15,8)
```

The destination is:

```text
B(15,8)
```

---

## 4. B(15,8) is the center of NG-B-NG

The landing rune:

```text
B(15,8)
```

is not isolated.

Two cells above it is:

```text
NG(13,8)
```

and two cells below it is:

```text
NG(17,8)
```

So:

```text
NG(13,8)
    |
    2
    |
 B(15,8)
    |
    2
    |
NG(17,8)
```

This gives the mirrored structure:

```text
NG-B-NG
```

Because it is mirrored, apply the same center-compilation rule used earlier:

```text
K = (a, φ(b), c)
```

The center is:

```text
B = 17
```

and:

```text
φ(17) = 16
```

Gematria Primus index `16` is:

```text
T
```

Therefore:

```text
NG-B-NG
    ↓
φ(B=17)=16=T
    ↓
NG-T-NG
```

So the new key is:

```text
KEY = NG-T-NG
```

---

## 5. The new key exactly matches the endpoint fingerprint

Now calculate the totient signature of:

```text
NG-T-NG
```

Using:

```text
NG = 21
T  = 16
NG = 21
```

we get:

```text
φ(21) = 12
φ(16) = 8
φ(21) = 12
```

Therefore:

```text
NG-T-NG → 12-8-12
```

But the `COLD` endpoint mirror already gave:

```text
EA-A-EA → 12-8-12
```

So the two structures independently match:

```text
EA-A-EA  → 12-8-12 ←  NG-T-NG
```

This is one of the strongest cross-checks in the `I MAY` stage.

The route does not simply find a random mirrored node. It finds a key whose totient signature is exactly the same as the mirror already sitting at the previous plaintext endpoint.

---

## 6. Möbius phase of NG-T-NG

The key is:

```text
NG-T-NG
```

Its signature is:

```text
12-8-12
```

Apply the Möbius function:

```text
μ(12) = 0
μ(8)  = 0
μ(12) = 0
```

Therefore:

```text
p = (0 + 0 + 0) mod 3
p = 0
```

So the key is used without rotation:

```text
ACTIVE KEY = NG-T-NG
```

For a 4-rune ciphertext:

```text
NG-T-NG-NG
```

The three possible cyclic phases were checked in the original research:

| Phase | Decryption result |
|---:|---|
| 0 | `I M A Y` |
| 1 | `S X A TH` |
| 2 | `I X F Y` |

The Möbius calculation independently selects:

```text
phase 0
```

which is the phase that produces:

```text
I MAY
```

---

## 7. Return to the preserved H-TH-H structure

The new key is not applied around `B(15,8)`.

Instead, the route returns to the preserved parent structure from the `COLD` stage:

```text
H-TH-H
```

Its center is still:

```text
TH(26,19)
```

That structure was already used to generate the `COLD` key:

```text
H-TH-H → H-U-H
```

Now it is reused as the location from which the next ciphertext is read.

Starting at:

```text
TH(26,19)
```

read left:

```text
TH(26,19)
G(26,18)
T(26,17)
E(26,16)
```

Therefore:

```text
CIPHERTEXT = TH-G-T-E
```

This reuse of the same parent structure is important: the stage does not introduce a completely unrelated ciphertext location after finding the new key.

---

## 8. Decryption: C − K mod 29

The ciphertext is:

```text
TH-G-T-E
```

The active key is:

```text
NG-T-NG-NG
```

Align them:

```text
Ciphertext:  TH  G   T   E
Key:         NG  T   NG  NG
```

As before:

```text
P = (C - K) mod 29
```

The values needed here are:

```text
TH = 2
G  = 6
T  = 16
E  = 18

NG = 21
T  = 16
```

Now decrypt each position:

| # | Ciphertext | C | Key | K | `(C - K) mod 29` | Plaintext |
|---:|---|---:|---|---:|---:|---|
| 1 | `TH(26,19)` | 2 | `NG` | 21 | `2 - 21 = -19 ≡ 10` | `I` |
| 2 | `G(26,18)` | 6 | `T` | 16 | `6 - 16 = -10 ≡ 19` | `M` |
| 3 | `T(26,17)` | 16 | `NG` | 21 | `16 - 21 = -5 ≡ 24` | `A` |
| 4 | `E(26,16)` | 18 | `NG` | 21 | `18 - 21 = -3 ≡ 26` | `Y` |

Therefore:

```text
Ciphertext:
TH-G-T-E

Key:
NG-T-NG-NG

(C - K) mod 29

Result:
I-M-A-Y
```

which reads:

# **I MAY**

The plaintext sequence is now:

# **AS I GO THE WEATHER TURNS COLD I MAY**

---

## 9. The whole I MAY route in one view

```text
COLD ends at:
A(11,7)

↓
COLD key:
H-U-H

↓
totient signature:
4-1-4

↓
endpoint mirror:
EA(10,7)-A(11,7)-EA(12,7)

↓
signature:
12-8-12


A(11,7)
↓ DOWN 4
S(15,7)
↓ RIGHT 1
B(15,8)

↓
B is center of:

NG(13,8)
    |
 B(15,8)
    |
NG(17,8)

↓
NG-B-NG

↓
φ(B=17)=16=T

↓
NG-T-NG

↓
signature:
12-8-12

↓
exact match:
EA-A-EA → 12-8-12 ← NG-T-NG

↓
Möbius:
μ(12), μ(8), μ(12)
= 0,0,0

↓
phase p=0

↓
active key:
NG-T-NG-NG

↓
return to preserved H-TH-H center:
TH(26,19)

↓
read left:
TH(26,19)
G(26,18)
T(26,17)
E(26,16)

↓
CIPHERTEXT = TH-G-T-E

↓
P = (C - K) mod 29

↓
I-M-A-Y

↓
I MAY
```

---

## 10. Later cross-check: the endpoint coordinates predict DOWN + RIGHT

One unresolved point in the original `COLD → I MAY` construction was why the inherited values should be taken specifically as:

```text
DOWN 4
RIGHT 1
```

rather than in another directional combination.

A later volume proposed a coordinate-direction selector.

The incoming `COLD` key:

```text
H-U-H
```

has:

```text
phase p = 1
```

Apply phase 1 to the coordinates:

```text
A(11,7)
```

The selector uses:

```text
V₁(11,7)
=
( μ(φ(11)), μ(φ(7)) )
```

For the row:

```text
11 → φ(11)=10 → μ(10)=+1
```

For the column:

```text
7 → φ(7)=6 → μ(6)=+1
```

Therefore:

```text
V₁(11,7) = (+1,+1)
```

with:

```text
+1 row    = DOWN
+1 column = RIGHT
```

So the later rule gives exactly:

```text
DOWN + RIGHT
```

which matches the recorded route:

```text
DOWN 4
RIGHT 1
```

The selector does not generate the distances `4` and `1`; those come from the inherited `4-1-4` state. It supplies the orientation.

This makes the previously unexplained direction choice substantially less arbitrary.

---

## 11. Later interpretation of the 000 state

The key:

```text
NG-T-NG
```

has signature:

```text
12-8-12
```

and full Möbius state:

```text
(0,0,0)
```

A later working model labels this state:

```text
000 → INHERIT / NEUTRAL
```

The idea is not that `000` does nothing.

Rather, it supplies no local center-vs-outer preference of its own, so the route relies on structural information already present:

```text
inherited movement signal: 4-1-4
matching signature:         12-8-12
preserved parent structure: H-TH-H
```

That interpretation is still a hypothesis, not an established Cicada rule, but it fits this stage unusually well.

---

## 12. Why the return to H-TH-H matters

At first glance, finding:

```text
NG-T-NG
```

near `B(15,8)` and then returning to:

```text
TH(26,19)
```

may look like a disconnected jump.

But the route preserves three links:

```text
1. H-U-H supplies the inherited 4-1-4 movement.
2. That movement finds NG-T-NG.
3. NG-T-NG is then applied back to the preserved H-TH-H parent structure.
```

So the sequence is recursive rather than disposable:

```text
H-TH-H
   ↓ generates
H-U-H
   ↓ supplies movement
4-1-4
   ↓ finds
NG-T-NG
   ↓ used back on
H-TH-H
   ↓
I MAY
```

This is a stronger structural picture than treating each discovered key as an isolated object.

---

## 13. The endpoint immediately opens the next stage

`I MAY` ends on the ciphertext rune:

```text
E(26,16)
```

That same `E` is part of a vertical mirrored node:

```text
E(24,16)
   |
X(25,16)
   |
E(26,16)
```

or:

```text
E-X-E
```

So, as happened earlier with the final `X` of `AS I GO THE`, the endpoint of one plaintext block is already part of the structure that begins the next one.

The next chapter starts from:

```text
E-X-E
```

and continues from:

```text
AS I GO THE WEATHER TURNS COLD I MAY
```

to:

```text
AS I GO THE WEATHER TURNS COLD I MAY CRY
```

---

[← 04 — COLD](./04-COLD.md)  
[← Back to the main page](../README.md)
