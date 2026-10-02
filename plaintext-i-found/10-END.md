# 10 — END

> **Recovered plaintext:** `END`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

This chapter continues from the exact endpoint of `THE`:

```text
J(19,16)
```

Immediately beside that endpoint is:

```text
F(19,15)
```

That `F` is not treated as ordinary ciphertext yet. It is the outer rune of an exact radius-4 mirror:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

At the same time, the `THE` endpoint `J(19,16)` belongs to another radius-4 structure:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

The first radius-4 mirror identifies the new ciphertext start.  
The second generates the key.

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

---

## 1. THE ends at J(19,16)

The previous chapter recovered:

```text
THE
```

from:

```text
A(19,17) → J(19,16)
```

So the exact endpoint is:

```text
J(19,16)
```

Immediately one cell to its left is:

```text
F(19,15)
```

The route does not simply start reading downward from this first `F`.

Instead, the local geometry shows that:

```text
F(19,15)
```

is part of a larger exact mirror.

---

## 2. F(19,15) is the outer rune of F-X-F

In row 19 we have:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

The distances are exact:

```text
19 - 15 = 4
23 - 19 = 4
```

So:

```text
F-X-F
```

is a radius-4 mirrored structure centered at:

```text
X(19,19)
```

The current `F(19,15)` is the left outer rune.

The opposite outer rune is:

```text
F(19,23)
```

This gives a geometric relocation:

```text
F(19,15)
   ↓
across the radius-4 mirror
   ↓
F(19,23)
```

That second `F` becomes the actual start of the `END` ciphertext.

---

## 3. The same X is also the center of a perpendicular radius-4 mirror

The center:

```text
X(19,19)
```

is not only the center of:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

It is also the center of a vertical radius-4 mirror:

```text
Y(15,19)
    |
    | 4
    |
X(19,19)
    |
    | 4
    |
Y(23,19)
```

So the same point is the center of two perpendicular structures:

```text
horizontal:
F —4— X —4— F

vertical:
Y
|
4
|
X
|
4
|
Y
```

This perpendicular symmetry is a supporting geometric check.

It is not itself required to decrypt `END`, but it makes the radius-4 role of `X(19,19)` much less isolated.

---

## 4. The THE endpoint belongs to another radius-4 mirror

At the same time, the exact `THE` endpoint:

```text
J(19,16)
```

is an outer rune of another mirror:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

So the local region now contains two distinct radius-4 structures:

```text
F-X-F
radius = 4

J-B-J
radius = 4
```

They have different jobs:

```text
F-X-F
→ relocates the route to F(19,23)

J-B-J
→ generates the key for END
```

The fact that both use the same radius `4` is one of the strongest local structural links in this transition.

---

## 5. Compile J-B-J into the new key

The key-generating mirror is:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

Its center is:

```text
B = 17
```

Apply Euler's totient:

```text
φ(17) = 16
```

Gematria Primus index `16` is:

```text
T
```

Therefore:

```text
J-B-J
   ↓
φ(B=17)=16=T
   ↓
J-T-J
```

So the generated key is:

```text
KEY = J-T-J
```

---

## 6. Totient signature of J-T-J

Using the 0-based Gematria Primus indices:

```text
J = 11
T = 16
J = 11
```

apply Euler's totient:

```text
φ(11) = 10
φ(16) = 8
φ(11) = 10
```

Therefore:

```text
J-T-J → 10-8-10
```

So the key signature is:

```text
10-8-10
```

---

## 7. Möbius phase of J-T-J

Apply the Möbius function to:

```text
10-8-10
```

We get:

```text
μ(10) = +1
μ(8)  = 0
μ(10) = +1
```

Therefore:

```text
p = (+1 + 0 + +1) mod 3
p = 2
```

So the original key:

```text
J-T-J
```

rotates to phase 2:

```text
J-J-T
```

Therefore the active key is:

```text
ACTIVE KEY = J-J-T
```

Again, the phase is fixed numerically before evaluating the plaintext.

---

## 8. Move across F-X-F to the real ciphertext start

Return to the local pointer mirror:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

The first `F(19,15)` sits immediately beside the `THE` endpoint.

The opposite outer rune is:

```text
F(19,23)
```

So the geometric transition is:

```text
J(19,16)
↓
F(19,15)
↓
across F-X-F
↓
F(19,23)
```

This second `F` is where the `END` ciphertext begins.

---

## 9. The END ciphertext

Starting from:

```text
F(19,23)
```

read downward:

```text
F(19,23)
L(20,23)
I(21,23)
```

Therefore:

```text
CIPHERTEXT = F-L-I
```

The active key is:

```text
KEY = J-J-T
```

Align them:

```text
Ciphertext:  F   L   I
Key:         J   J   T
```

---

## 10. Decryption: C − K mod 29

As before:

```text
P = (C - K) mod 29
```

The values needed here are:

```text
F = 0
L = 20
I = 10

J = 11
T = 16
```

Now decrypt each position:

| # | Ciphertext | C | Key | K | `(C - K) mod 29` | Plaintext |
|---:|---|---:|---|---:|---:|---|
| 1 | `F(19,23)` | 0 | `J` | 11 | `0 - 11 = -11 ≡ 18` | `E` |
| 2 | `L(20,23)` | 20 | `J` | 11 | `20 - 11 = 9` | `N` |
| 3 | `I(21,23)` | 10 | `T` | 16 | `10 - 16 = -6 ≡ 23` | `D` |

Therefore:

```text
Ciphertext:
F-L-I

Key:
J-J-T

(C - K) mod 29

Result:
E-N-D
```

which reads:

# **END**

The plaintext sequence is now:

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END**

---

## 11. The whole END route in one view

```text
THE ends at:
J(19,16)

↓
adjacent:
F(19,15)

↓
F is outer of:

F(19,15) —4— X(19,19) —4— F(19,23)

↓
opposite outer:
F(19,23)

↓
this becomes the ciphertext start


Meanwhile:

J(19,16) —4— B(23,12) —4— J(27,8)

↓
J-B-J

↓
φ(B=17)=16=T

↓
J-T-J

↓
totient signature:
10-8-10

↓
Möbius:
+1,0,+1

↓
phase:
p=2

↓
active key:
J-J-T


ciphertext:

F(19,23)
L(20,23)
I(21,23)

↓
CIPHERTEXT = F-L-I

↓
P = (C - K) mod 29

↓
E-N-D

↓
END
```

---

## 12. Strong cross-check: the same radius 4 controls both geometry and key discovery

The transition contains two exact radius-4 structures:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

and:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

The first controls where the ciphertext begins.

The second supplies the key generator.

So the same local scale:

```text
4
```

appears simultaneously in:

```text
route relocation
+
key-generating geometry
```

This is similar to earlier stages where one inherited number reappears in more than one structural role.

---

## 13. Later full-state cross-check: (+1,0,+1) again leads to an OUTER endpoint

The key signature was:

```text
10-8-10
```

Its full Möbius state is:

```text
μ(10), μ(8), μ(10)
=
+1,0,+1
```

therefore:

```text
M = (+1,0,+1)
```

This is the same full state previously seen for `NOW THE`:

```text
OE-I-OE → 10-4-10 → (+1,0,+1)
```

After `NOW THE`, the endpoint:

```text
J(15,20)
```

became an outer rune of:

```text
J-D-J
```

Now, after `END`, the endpoint:

```text
I(21,23)
```

is again an outer rune of the next mirror:

```text
I(21,21) — R(21,22) — I(21,23)
```

So the two clean observations are:

```text
NOW THE
(+1,0,+1)
→ endpoint becomes OUTER of J-D-J

END
(+1,0,+1)
→ endpoint becomes OUTER of I-R-I
```

This is the strongest evidence behind the later working interpretation:

```text
(+1,0,+1) → OUTER-active
```

It remains a working model, but this is its second clean documented case.

---

## 14. Later coordinate check after THE: partial, so geometry is required

Before `END`, the route is at:

```text
J(19,16)
```

with the incoming phase:

```text
p = 2
```

The later coordinate selector gives:

```text
V₂(19,16) = (+1,0)
```

This is a **partial selector**.

So the coordinate rule does not supply a complete two-dimensional direction.

That is exactly where the route uses the local radius-4 geometry:

```text
F-X-F
J-B-J
```

instead of forcing a coordinate arrow.

This supports the separation:

```text
partial coordinate state
→ inspect compatible local geometry
```

---

## 15. END ends inside I-R-I

The final ciphertext rune of `END` is:

```text
I(21,23)
```

That exact cell is the right outer rune of:

```text
I(21,21) — R(21,22) — I(21,23)
```

So the endpoint already opens the next structural node:

```text
I-R-I
```

This continues the recurring rule:

```text
plaintext endpoint
→ immediately becomes part of next mirror
```

---

## 16. Compile I-R-I

The center is:

```text
R = 4
```

Apply Euler's totient:

```text
φ(4) = 2
```

Gematria Primus index `2` is:

```text
TH
```

Therefore:

```text
I-R-I
   ↓
φ(R=4)=2=TH
   ↓
I-TH-I
```

So the transformed structure is:

```text
I-TH-I
```

---

## 17. The post-END signature returns to 4-1-4

Now calculate the totient signature:

```text
I  = 10 → φ(10) = 4
TH = 2  → φ(2)  = 1
I  = 10 → φ(10) = 4
```

Therefore:

```text
I-TH-I → 4-1-4
```

This is an exact recurrence of a previously important signature.

Earlier:

```text
H-U-H → 4-1-4
```

and now:

```text
I-TH-I → 4-1-4
```

So:

```text
φ(H-U-H)
=
φ(I-TH-I)
=
4-1-4
```

The same three-position fingerprint has returned after `END`.

---

## 18. The same center R opens a larger H-R-H mirror

The center:

```text
R(21,22)
```

does not belong only to the small:

```text
I-R-I
```

mirror.

It is also the center of a larger horizontal mirror:

```text
H(21,17) — R(21,22) — H(21,27)
```

Apply the same center transformation:

```text
R = 4
φ(4) = 2 = TH
```

Therefore:

```text
H-R-H
   ↓
H-TH-H
```

Its signature is again:

```text
4-1-4
```

So around the same physical center we get:

```text
I-R-I → I-TH-I → 4-1-4

H-R-H → H-TH-H → 4-1-4
```

This reconnects the route to the already known `H-TH-H` structural family.

---

## 19. Later coordinate check after END: another partial state

The endpoint is:

```text
I(21,23)
```

with incoming phase:

```text
p = 2
```

Apply the later selector:

```text
V₂(21,23)
=
( μ(φ²(21)), μ(φ²(23)) )
```

For the row:

```text
21 → φ(21)=12 → φ(12)=4 → μ(4)=0
```

For the column:

```text
23 → φ(23)=22 → φ(22)=10 → μ(10)=+1
```

Therefore:

```text
V₂(21,23) = (0,+1)
```

Again this is only a **partial** coordinate state.

The actual continuation is therefore recovered from the exact local mirror system around:

```text
R(21,22)
```

rather than treating `+1` as a literal immediate rightward instruction.

---

## 20. Where the next chapter starts

The post-`END` state is now:

```text
endpoint:
I(21,23)

endpoint mirror:
I(21,21)-R(21,22)-I(21,23)

compiled form:
I-TH-I

signature:
4-1-4
```

The same center also opens:

```text
H(21,17)-R(21,22)-H(21,27)
```

which compiles to:

```text
H-TH-H
```

with the same signature:

```text
4-1-4
```

That larger mirror becomes the key family for the next plaintext:

```text
IS
```

The next chapter continues from:

```text
AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END
```

to:

```text
AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS
```

---

[← 09 — OF THE](./09-OF-THE.md)  
[← Back to the main page](../README.md)
