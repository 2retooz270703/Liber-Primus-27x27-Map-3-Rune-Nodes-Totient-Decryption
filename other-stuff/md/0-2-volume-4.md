# Cicada 3301 Liber Primus 0–2
## 27×27 Rune Matrix Decryption — Volume 4

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.  
**Date:** 11.09.2026

> **Strongest plaintext candidate**
>
> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END ...**

This document is the technical Markdown edition of Volume 4.

It continues directly from the `NOW THE` endpoint established in Volume 3 and records the proposed continuation:

```text
IDEA OF THE END
```

The purpose of this edition is to keep the route explicit, searchable, reproducible, and easy to inspect by humans, scripts, and AI systems.

The main structural development of Volume 4 is that the route continues through a chain of **locally connected mirrors**, where endpoints repeatedly become centers or outer nodes of the next structure. Several of these transitions are also reinforced by exact **totient-signature matches**.

---

## Quick reference

| Item | Volume 4 result |
|---|---|
| Subject | Cicada 3301 — Liber Primus pages 0–2 |
| Spatial representation | 27×27 rune matrix |
| Previous plaintext | `AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE` |
| Entry endpoint | `J(15,20)` |
| First local mirror | `A(8,13) —3— TH(11,16) —3— A(14,19)` |
| First compiled key | `A-U/V-A` |
| First Möbius phase | `1` |
| First active key | `U/V-A-A` |
| New plaintext 1 | `IDEA` |
| IDEA endpoint | `D(17,18)` |
| Next mirror | `J(15,20) —2— D(17,18) —2— J(19,16)` |
| Compiled structure | `J-OE-J` |
| Signature link | `φ(J-OE-J) = φ(OE-J-OE) = 10-10-10` |
| New plaintext 2 | `OF THE` |
| Radius-4 pointer mirror | `F(19,15) —4— X(19,19) —4— F(19,23)` |
| END key node | `J(19,16) —4— B(23,12) —4— J(27,8)` |
| Compiled END key | `J-T-J` |
| END Möbius phase | `2` |
| END active key | `J-J-T` |
| New plaintext 3 | `END` |
| Final endpoint | `I(21,23)` |
| Next mirror | `I(21,21) — R(21,22) — I(21,23)` |
| Final signature link | `φ(I-TH-I) = φ(H-U/V-H) = 4-1-4` |
| Current result | `AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END ...` |
| Status | proposed, ongoing, not officially verified |

---

# PART I — ENTRY FROM VOLUME 3

## 1. Purpose of Volume 4

Volume 3 reaches:

> **NOW THE**

and the final ciphertext rune is:

```text
J(15,20)
```

Volume 4 begins from that exact position.

The central question is whether the route can continue without jumping to an unrelated region of the matrix.

The proposed answer is yes.

The endpoint `J(15,20)` lies immediately on the same diagonal as a local mirrored structure:

```text
A(8,13) —3— TH(11,16) —3— A(14,19)
```

That mirror generates the key used for the next plaintext.

The new sequence developed in this volume is:

```text
NOW THE
   ↓
IDEA
   ↓
OF THE
   ↓
END
```

giving the current reading:

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END ...**

---

## 2. Frozen state after NOW THE

Volume 3 decrypts:

```text
TH-AE-B-A-J
-
OE-OE-I-OE-OE
=
N-O-W-TH-E
```

which reads:

```text
NOW THE
```

The last ciphertext position is:

```text
J(15,20)
```

Volume 4 does not restart elsewhere.

Instead, this same `J(15,20)` becomes the first ciphertext rune of the next proposed plaintext block.

So the transition is continuous at the cell level:

```text
NOW THE ends at J(15,20)
                ↓
IDEA begins at J(15,20)
```

---

# PART II — NOW THE → IDEA

## 3. The local A-TH-A mirror

On the same diagonal as the previous route is the mirror:

```text
A(8,13)
   \
    \
     TH(11,16)
        \
         \
          A(14,19)
```

Both outer `A` runes are three diagonal grid steps from the center:

```text
A(8,13) —3— TH(11,16) —3— A(14,19)
```

So this is an exact radius-3 mirrored structure.

The current route has already passed through the lower outer node:

```text
A(14,19)
```

and reaches:

```text
J(15,20)
```

immediately beyond it on the same diagonal.

This makes `A-TH-A` the local structure directly associated with the new ciphertext position.

---

## 4. Transforming A-TH-A into the key

The center of the mirror is:

```text
TH
```

Using zero-based Gematria Primus:

```text
TH = 2
```

Apply Euler's totient:

```text
φ(2) = 1
```

and value `1` corresponds to:

```text
U/V
```

Therefore:

```text
A-TH-A → A-U/V-A
```

The three-rune key structure is:

```text
A-U/V-A
```

This uses the same recurring operation as the earlier volumes:

```text
a-b-a → a-φ(b)-a
```

---

## 5. Totient signature of A-U/V-A

For:

```text
A-U/V-A
```

the relevant values are:

```text
A   = 24
U/V = 1
A   = 24
```

Applying `φ`:

```text
φ(24) = 8
φ(1)  = 1
φ(24) = 8
```

Therefore the signature is:

```text
A-U/V-A → 8-1-8
```

---

## 6. Möbius phase for IDEA

The phase rule remains:

```text
p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3
```

For the signature:

```text
8-1-8
```

we have:

```text
μ(8) = 0
μ(1) = 1
μ(8) = 0
```

Therefore:

```text
p = (0 + 1 + 0) mod 3
p = 1
```

So:

```text
phase = 1
```

Starting from:

```text
A-U/V-A
```

phase 1 gives:

```text
U/V-A-A
```

Active key:

```text
U/V-A-A
```

The phase is fixed numerically before the plaintext is evaluated.

---

## 7. IDEA ciphertext

From the Volume 3 endpoint:

```text
J(15,20)
```

continue diagonally down-left:

```text
J(15,20)
→ E(16,19)
→ D(17,18)
```

Ciphertext:

```text
J-E-D
```

The key is:

```text
U/V-A-A
```

---

## 8. Decrypting IDEA

Use the same decryption rule:

```text
P = C - K mod 29
```

Rune by rune:

| # | Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|---|
| 1 | `J(11)` | `U/V(1)` | `11 - 1 = 10` | `I` |
| 2 | `E(18)` | `A(24)` | `18 - 24 mod 29 = 23` | `D` |
| 3 | `D(23)` | `A(24)` | `23 - 24 mod 29 = 28` | `EA` |

Therefore:

```text
ciphertext: J-E-D
key:        U/V-A-A
result:     I-D-EA
```

The rune sequence:

```text
I-D-EA
```

reads as:

> **IDEA**

So the continuation becomes:

```text
NOW THE IDEA
```

---

## 9. Compact IDEA chain

```text
Volume 3 endpoint
J(15,20)
    |
    | local diagonal mirror
    v
A —3— TH —3— A
       |
       | φ(TH=2)=1=U/V
       v
A-U/V-A
    |
    | signature 8-1-8
    | Möbius phase = 1
    v
U/V-A-A
    |
    | J-E-D
    | GP subtraction mod 29
    v
I-D-EA
    |
    v
IDEA
```

---

# PART III — IDEA → OF THE

## 10. IDEA ends at D(17,18)

The final ciphertext rune of `IDEA` is:

```text
D(17,18)
```

This position is not isolated.

It is the exact center of another mirror:

```text
J(15,20) —2— D(17,18) —2— J(19,16)
```

This creates a direct structural continuation.

Notice that:

```text
J(15,20)
```

has now played two roles:

1. the endpoint of `NOW THE` and beginning of the `IDEA` ciphertext;
2. one outer node of the new `J-D-J` mirror.

The route therefore remains locally connected.

---

## 11. Transforming J-D-J

The center is:

```text
D
```

Using zero-based Gematria Primus:

```text
D = 23
```

Apply Euler's totient:

```text
φ(23) = 22
```

Value `22` corresponds to:

```text
OE
```

Therefore:

```text
J-D-J → J-OE-J
```

The transformed structure is:

```text
J-OE-J
```

---

## 12. Signature of J-OE-J

Apply Euler's totient to all three runes:

```text
J  = 11 → φ(11) = 10
OE = 22 → φ(22) = 10
J  = 11 → φ(11) = 10
```

Therefore:

```text
φ(J-OE-J) = 10-10-10
```

This uniform signature becomes important immediately.

---

## 13. The next mirror shares J(19,16)

The opposite outer node of `J-D-J` is:

```text
J(19,16)
```

That same cell is the exact center of another mirror:

```text
OE(18,16)
   |
   | 1
   |
J(19,16)
   |
   | 1
   |
OE(20,16)
```

or:

```text
OE(18,16) —1— J(19,16) —1— OE(20,16)
```

So the local geometry forms:

```text
J(15,20)
    \
     \
      D(17,18)
        \
         \
          J(19,16)
             |
             |
             OE-J-OE
```

More precisely:

```text
J-D-J
    ↓
shared J(19,16)
    ↓
OE-J-OE
```

The outer node of one mirror becomes the center of the next.

---

## 14. Exact 10-10-10 signature match

The transformed first structure is:

```text
J-OE-J
```

Its signature is:

```text
φ(J-OE-J) = 10-10-10
```

Now take the next physical mirror:

```text
OE-J-OE
```

Its signature is:

```text
φ(OE-J-OE)
=
φ(22)-φ(11)-φ(22)
=
10-10-10
```

Therefore:

```text
φ(J-OE-J) = φ(OE-J-OE)
           = 10-10-10
```

This gives two simultaneous links:

```text
GEOMETRY:
J-D-J and OE-J-OE share J(19,16)

NUMBERS:
φ(J-OE-J) = φ(OE-J-OE) = 10-10-10
```

The next mirror is therefore connected to the previous stage both spatially and numerically.

---

## 15. Möbius phase of J-OE-J

The signature is:

```text
10-10-10
```

Using the Möbius function:

```text
μ(10) = 1
μ(10) = 1
μ(10) = 1
```

So:

```text
p = (1 + 1 + 1) mod 3
p = 0
```

Therefore:

```text
phase = 0
```

and the active key remains:

```text
J-OE-J
```

---

## 16. Decrypting OF

The next two ciphertext runes are:

```text
X(18,15)
→ OE(18,16)
```

Using the phase-0 key:

```text
J-OE
```

decrypt:

| # | Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|---|
| 1 | `X(14)` | `J(11)` | `14 - 11 = 3` | `O` |
| 2 | `OE(22)` | `OE(22)` | `22 - 22 = 0` | `F` |

Therefore:

```text
X-OE
-
J-OE
=
O-F
```

Result:

> **OF**

The final ciphertext rune:

```text
OE(18,16)
```

is also an outer node of the next mirror:

```text
OE-J-OE
```

Again, the plaintext endpoint enters the next structure directly.

---

## 17. OE-J-OE generates the key for THE

The current mirror is:

```text
OE(18,16) — J(19,16) — OE(20,16)
```

Its center is:

```text
J = 11
```

Apply Euler's totient:

```text
φ(11) = 10 = I
```

Therefore:

```text
OE-J-OE → OE-I-OE
```

This is the same compiled structure already encountered earlier in the route.

Its totient signature is:

```text
10-4-10
```

because:

```text
φ(OE=22)=10
φ(I=10)=4
φ(OE=22)=10
```

---

## 18. Möbius phase for THE

For:

```text
10-4-10
```

the Möbius values are:

```text
μ(10)=1
μ(4)=0
μ(10)=1
```

Therefore:

```text
p = (1 + 0 + 1) mod 3
p = 2
```

The active cyclic key becomes:

```text
OE-I-OE → OE-OE-I
```

For the two-rune plaintext read used here, the first two active key runes are:

```text
OE-OE
```

---

## 19. Decrypting THE

The route reads inward toward:

```text
J(19,16)
```

using:

```text
A(19,17)
→ J(19,16)
```

Ciphertext:

```text
A-J
```

Using:

```text
OE-OE
```

decrypt:

| # | Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|---|
| 1 | `A(24)` | `OE(22)` | `24 - 22 = 2` | `TH` |
| 2 | `J(11)` | `OE(22)` | `11 - 22 mod 29 = 18` | `E` |

Therefore:

```text
A-J
-
OE-OE
=
TH-E
```

The rune sequence:

```text
TH-E
```

reads as:

> **THE**

So the combined continuation is:

> **OF THE**

---

## 20. Why OF THE is structurally compact

The two words are not produced from two unrelated locations.

They converge around the same local mirror:

```text
             OE(18,16)
              /     \
             /       \
        OF ends       mirror
           here         |
                        J(19,16)
                           ↑
                           |
                     THE ends here
```

The exact chain is:

```text
J-D-J
  |
  | φ(D)=OE
  v
J-OE-J
  |
  | phase 0
  v
OF
  |
  | endpoint OE(18,16)
  v
OE-J-OE
  |
  | φ(J)=I
  | phase 2
  v
THE
```

This is one of the clearest local handoffs in Volume 4.

---

# PART IV — OF THE → END

## 21. F(19,15) as a geometric pointer

Immediately beyond the `THE` endpoint:

```text
J(19,16)
```

lies:

```text
F(19,15)
```

Volume 4 does not treat this first `F` as the start of the next plaintext.

Instead, it is interpreted geometrically because it is the outer node of a radius-4 mirror:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

This gives:

```text
radius = 4
```

and identifies the opposite point:

```text
F(19,23)
```

as a natural destination.

---

## 22. Perpendicular radius-4 mirror through X(19,19)

The center:

```text
X(19,19)
```

also belongs to a perpendicular radius-4 mirror:

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

Therefore the same point is the center of two exact radius-4 structures:

```text
horizontal:
F(19,15) —4— X(19,19) —4— F(19,23)

vertical:
Y(15,19) —4— X(19,19) —4— Y(23,19)
```

The source notes the visual symmetry around:

```text
X(19,19)
```

as a supporting geometric observation.

This symmetry is not itself used as a decryption formula, but it strengthens the interpretation of the first `F` as a structural pointer.

---

## 23. J(19,16) belongs to another radius-4 structure

At the same time, the endpoint of `THE`:

```text
J(19,16)
```

is one outer node of another exact radius-4 mirror:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

So the local region contains two different roles for the same radius:

```text
F-X-F → radius 4
J-B-J → radius 4
```

The first mirror controls the geometric relocation to the second `F`.

The second mirror generates the key used at that destination.

---

## 24. Transforming J-B-J

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

Value `16` corresponds to:

```text
T
```

Therefore:

```text
J-B-J → J-T-J
```

Generated key:

```text
J-T-J
```

---

## 25. Signature and Möbius phase of J-T-J

Apply `φ`:

```text
φ(J=11) = 10
φ(T=16) = 8
φ(J=11) = 10
```

so:

```text
J-T-J → 10-8-10
```

Now:

```text
μ(10) = 1
μ(8)  = 0
μ(10) = 1
```

Therefore:

```text
p = (1 + 0 + 1) mod 3
p = 2
```

So phase 2 rotates:

```text
J-T-J
```

into:

```text
J-J-T
```

Active key:

```text
J-J-T
```

Again, the key phase is determined before judging the plaintext.

---

## 26. Moving across the F-X-F mirror

The first `F` is:

```text
F(19,15)
```

The mirror is:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

The opposite outer point is therefore:

```text
F(19,23)
```

Volume 4 uses this symmetry as the transition:

```text
F(19,15)
   |
   | across radius-4 mirror
   v
F(19,23)
```

This is where the next ciphertext begins.

---

## 27. END ciphertext

Starting from:

```text
F(19,23)
```

read downward:

```text
F(19,23)
→ L(20,23)
→ I(21,23)
```

Ciphertext:

```text
F-L-I
```

The active key is:

```text
J-J-T
```

---

## 28. Decrypting END

Using:

```text
P = C - K mod 29
```

decrypt rune by rune:

| # | Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|---|
| 1 | `F(0)` | `J(11)` | `0 - 11 mod 29 = 18` | `E` |
| 2 | `L(20)` | `J(11)` | `20 - 11 = 9` | `N` |
| 3 | `I(10)` | `T(16)` | `10 - 16 mod 29 = 23` | `D` |

Therefore:

```text
ciphertext: F-L-I
key:        J-J-T
result:     E-N-D
```

Result:

> **END**

The full new Volume 4 plaintext is now:

> **IDEA OF THE END**

and the current connected reading becomes:

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END ...**

---

## 29. Compact END chain

```text
THE ends at J(19,16)
          |
          v
      F(19,15)
          |
          | outer node of radius-4 mirror
          v
F(19,15) —4— X(19,19) —4— F(19,23)
                                  |
                                  | next ciphertext
                                  v
                             F-L-I

J(19,16) —4— B(23,12) —4— J(27,8)
                 |
                 | φ(B=17)=16=T
                 v
               J-T-J
                 |
                 | signature 10-8-10
                 | Möbius phase 2
                 v
               J-J-T
                 |
                 | F-L-I
                 | mod-29 subtraction
                 v
                END
```

---

# PART V — THE STRUCTURE AFTER END

## 30. END finishes at I(21,23)

The final ciphertext rune of `END` is:

```text
I(21,23)
```

This cell immediately enters another mirror:

```text
I(21,21) — R(21,22) — I(21,23)
```

The route therefore again ends on a rune that is already part of a new local structure.

The final `I(21,23)` is the right outer node of:

```text
I-R-I
```

---

## 31. Transforming I-R-I

The center is:

```text
R
```

Using the working Gematria Primus values:

```text
R = 4
```

Apply Euler's totient:

```text
φ(4) = 2
```

and value `2` corresponds to:

```text
TH
```

Therefore:

```text
I-R-I → I-TH-I
```

The next compiled structure is:

```text
I-TH-I
```

---

## 32. Totient signature of I-TH-I

Apply `φ`:

```text
φ(I=10)  = 4
φ(TH=2)  = 1
φ(I=10)  = 4
```

Therefore:

```text
φ(I-TH-I) = 4-1-4
```

This signature is not new.

It exactly matches an earlier key structure.

---

## 33. Return of the 4-1-4 signature

Earlier in the route, the `I MAY` branch uses:

```text
H-U/V-H
```

whose signature is:

```text
φ(H-U/V-H) = 4-1-4
```

Now, after `END`:

```text
φ(I-TH-I) = 4-1-4
```

Therefore:

```text
φ(I-TH-I)
=
φ(H-U/V-H)
=
4-1-4
```

This creates a direct numerical link between the post-`END` structure and an earlier important structure.

The match is exact at all three positions.

---

## 34. Why the 4-1-4 return matters

The route has already used totient signatures as structural fingerprints.

Volume 4 ends by producing another exact recurrence:

```text
earlier:
H-U/V-H → 4-1-4

after END:
I-TH-I → 4-1-4
```

This may indicate:

- a return to an earlier structural family;
- a clue for the next key;
- a state relation between the `I MAY` branch and the post-`END` branch;
- or another form of structural inheritance.

Volume 4 does **not** fix which of these interpretations is correct.

The important reproducible statement is only:

```text
the two structures have the same exact 4-1-4 totient signature
```

---

# PART VI — WHAT VOLUME 4 ADDS TO THE MODEL

## 35. Endpoint-to-structure continuity

One of the strongest recurring features of Volume 4 is that the route repeatedly hands one stage directly into the next.

The sequence is:

```text
NOW THE ends at J(15,20)
        ↓
J(15,20) begins IDEA
        ↓
IDEA ends at D(17,18)
        ↓
D(17,18) is center of J-D-J
        ↓
J(19,16) is outer node of J-D-J
        ↓
J(19,16) is center of OE-J-OE
        ↓
OF ends at OE(18,16)
        ↓
OE(18,16) is outer node of OE-J-OE
        ↓
THE converges on J(19,16)
        ↓
adjacent F(19,15) opens F-X-F
        ↓
opposite F(19,23) begins END
        ↓
END ends at I(21,23)
        ↓
I(21,23) is outer node of I-R-I
```

This is the main geometric continuity argument of Volume 4.

---

## 36. Center transformations used in Volume 4

Volume 4 contains a compact chain of center-to-totient transformations:

```text
TH → φ(TH) = U/V
D  → φ(D)  = OE
J  → φ(J)  = I
B  → φ(B)  = T
R  → φ(R)  = TH
```

or numerically:

```text
2  → 1
23 → 22
11 → 10
17 → 16
4  → 2
```

These are not separate ad hoc substitutions.

They all use the same operation:

```text
center rune
    ↓
Euler φ
    ↓
new key-center rune
```

---

## 37. Signature links in Volume 4

Two exact structural signature matches are especially important.

### 37.1 The 10-10-10 link

```text
φ(J-OE-J)  = 10-10-10
φ(OE-J-OE) = 10-10-10
```

These structures are also geometrically connected through:

```text
J(19,16)
```

which is an outer node in one and the center of the other.

### 37.2 The 4-1-4 return

```text
φ(I-TH-I)   = 4-1-4
φ(H-U/V-H)  = 4-1-4
```

The second equality links the new post-`END` state to an earlier important structure from the `I MAY` branch.

---

## 38. Radius structure in Volume 4

Several exact radii appear in the local geometry:

```text
A-TH-A → radius 3
J-D-J  → radius 2
OE-J-OE → radius 1
F-X-F  → radius 4
Y-X-Y  → radius 4
J-B-J  → radius 4
```

Volume 4 does **not** claim a universal numerical sequence from:

```text
3, 2, 1, 4
```

The important point is more limited:

- the radii are exact;
- the structures are local to the active route;
- radius `4` repeats across multiple connected structures around the `OF THE → END` transition.

Any larger pattern in the radii remains open.

---

## 39. Geometry and arithmetic reinforce the same handoffs

The strongest transitions are not based on plaintext readability alone.

For example:

```text
IDEA endpoint D
   ↓
center of J-D-J
   ↓
φ(D)=OE
   ↓
J-OE-J
   ↓
10-10-10
```

then:

```text
J-D-J
   ↓
shared J(19,16)
   ↓
OE-J-OE
   ↓
10-10-10
```

So the handoff from one mirror to the next is confirmed by both:

```text
shared geometry
+
matching totient signature
```

Likewise, the `END` transition combines:

```text
radius-4 pointer geometry
+
radius-4 key structure
+
fixed Möbius phase
+
exact mod-29 plaintext
```

---

## 40. Updated sequential model

The working model after Volume 4 can be represented as:

```text
current plaintext endpoint
          |
          v
local mirror / geometric relation
          |
          v
center transformation by Euler φ
          |
          v
key structure
          |
          v
totient signature
          |
          v
Möbius phase
          |
          v
active cyclic key
          |
          v
local ciphertext read
          |
          v
GP subtraction mod 29
          |
          v
plaintext
          |
          v
new endpoint
          |
          v
next local structure
          ↺
```

A second type of transition also appears:

```text
current point
    |
    v
outer node of large mirror
    |
    v
opposite outer node
    |
    v
new ciphertext location
```

The clearest Volume 4 example is:

```text
F(19,15)
    ↓
F-X-F radius-4 mirror
    ↓
F(19,23)
    ↓
END
```

---

# PART VII — FULL VOLUME 4 ROUTE

## 41. IDEA OF THE END in one chain

```text
VOLUME 3:
NOW THE
ends at J(15,20)

          ↓

A(8,13) —3— TH(11,16) —3— A(14,19)
                     |
                     | φ(TH)=U/V
                     v
                  A-U/V-A
                     |
                     | phase 1
                     v
                  U/V-A-A
                     |
                     | J(15,20)-E(16,19)-D(17,18)
                     v
                    IDEA

          ↓

D(17,18)
is center of
J(15,20) —2— D(17,18) —2— J(19,16)
                     |
                     | φ(D)=OE
                     v
                   J-OE-J
                     |
                     | phase 0
                     v
                   X-OE
                     |
                     v
                     OF

          ↓

OE(18,16)
is outer node of
OE(18,16) —1— J(19,16) —1— OE(20,16)
                     |
                     | φ(J)=I
                     v
                  OE-I-OE
                     |
                     | phase 2
                     v
                  OE-OE-I
                     |
                     | A(19,17)-J(19,16)
                     v
                    THE

          ↓

F(19,15)
is outer node of
F(19,15) —4— X(19,19) —4— F(19,23)
                                  |
                                  v
                             F(19,23)

J(19,16) —4— B(23,12) —4— J(27,8)
                 |
                 | φ(B)=T
                 v
               J-T-J
                 |
                 | phase 2
                 v
               J-J-T
                 |
                 | F(19,23)-L(20,23)-I(21,23)
                 v
                END

          ↓

I(21,23)
is outer node of
I(21,21) — R(21,22) — I(21,23)
                |
                | φ(R)=TH
                v
             I-TH-I
                |
                v
              4-1-4

MATCH:
H-U/V-H → 4-1-4
```

---

## 42. Plaintext contribution by stage

| Stage | Ciphertext | Active key | Plaintext |
|---|---|---|---|
| IDEA | `J-E-D` | `U/V-A-A` | `I-D-EA` → **IDEA** |
| OF | `X-OE` | `J-OE` | `O-F` → **OF** |
| THE | `A-J` | `OE-OE` | `TH-E` → **THE** |
| END | `F-L-I` | `J-J-T` | `E-N-D` → **END** |

So Volume 4 contributes:

> **IDEA OF THE END**

---

# PART VIII — VALIDATION STATUS

## 43. What is directly reproducible

The following claims can be checked directly against the 27×27 matrix and the stated arithmetic:

### Geometry

```text
A(8,13) —3— TH(11,16) —3— A(14,19)

J(15,20) —2— D(17,18) —2— J(19,16)

OE(18,16) —1— J(19,16) —1— OE(20,16)

F(19,15) —4— X(19,19) —4— F(19,23)

Y(15,19) —4— X(19,19) —4— Y(23,19)

J(19,16) —4— B(23,12) —4— J(27,8)

I(21,21) — R(21,22) — I(21,23)
```

### Center transforms

```text
φ(TH=2) = 1 = U/V
φ(D=23) = 22 = OE
φ(J=11) = 10 = I
φ(B=17) = 16 = T
φ(R=4) = 2 = TH
```

### Signature checks

```text
φ(J-OE-J)  = 10-10-10
φ(OE-J-OE) = 10-10-10

φ(I-TH-I)  = 4-1-4
φ(H-U/V-H) = 4-1-4
```

### Möbius phases

```text
A-U/V-A:
μ(8)+μ(1)+μ(8)
= 0+1+0
= 1 mod 3

J-OE-J:
μ(10)+μ(10)+μ(10)
= 1+1+1
= 0 mod 3

OE-I-OE:
μ(10)+μ(4)+μ(10)
= 1+0+1
= 2 mod 3

J-T-J:
μ(10)+μ(8)+μ(10)
= 1+0+1
= 2 mod 3
```

### Plaintext arithmetic

```text
J-E-D
-
U/V-A-A
=
I-D-EA
=
IDEA
```

```text
X-OE
-
J-OE
=
O-F
=
OF
```

```text
A-J
-
OE-OE
=
TH-E
=
THE
```

```text
F-L-I
-
J-J-T
=
E-N-D
=
END
```

---

## 44. What remains interpretive

The arithmetic above can be reproduced, but not every transition is yet governed by one fully formalized universal rule.

The following remain interpretive or provisional:

- why the `A-TH-A` mirror should be selected over every other local structure after `NOW THE`;
- the exact general rule that determines when an outer rune is used as a direct key source versus as a geometric pointer;
- why `F(19,15)` should be interpreted as a pointer across `F-X-F` rather than plaintext;
- whether every repeated radius must carry forward as a control value;
- whether an exact matching totient signature always indicates a valid transition;
- what the `4-1-4` return after `END` instructs the solver to do next.

These questions matter because a complete solution should eventually determine the next stage **before** the resulting English plaintext is inspected.

---

## 45. What is strongest in Volume 4

The strongest part of Volume 4 is the accumulation of independent constraints around the same local route:

```text
cell continuity
+
mirror continuity
+
Euler center transformations
+
totient signature matches
+
Möbius-fixed phases
+
mod-29 arithmetic
+
new endpoints entering new mirrors
```

In particular:

```text
J-D-J
```

and:

```text
OE-J-OE
```

are linked in two independent ways:

```text
shared J(19,16)
```

and:

```text
10-10-10 = 10-10-10
```

The route then reaches `END`, whose final cell immediately enters another mirror and recreates an earlier exact signature:

```text
4-1-4
```

This is why the proposed `IDEA OF THE END` continuation is treated as a connected structural branch rather than a set of isolated English cribs.

---

## 46. Current strongest plaintext

The current connected plaintext candidate is:

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END ...**

Volume 4 contributes:

> **IDEA OF THE END**

The punctuation and word spacing are human-readable grouping of the recovered rune stream.

The exact cryptographic output is represented in rune transliteration blocks such as:

```text
I-D-EA
O-F
TH-E
E-N-D
```

---

# PART IX — OPEN QUESTIONS

## 47. The key-selection problem remains open

The route now contains several kinds of structures:

```text
small mirrored key-generating nodes
large-radius geometric mirrors
signature-linked structures
shared-center structures
endpoint mirrors
```

The remaining central problem is to distinguish their roles deterministically.

A future rule should ideally answer:

```text
given current endpoint + local structures + inherited state
                     ↓
which structure is active?
                     ↓
is it a key source or a movement structure?
                     ↓
which direction?
                     ↓
which ciphertext?
```

without using plaintext readability to make those decisions.

---

## 48. The next test after END

The current endpoint is:

```text
I(21,23)
```

and the immediate structure is:

```text
I-R-I → I-TH-I
```

with:

```text
φ(I-TH-I) = 4-1-4
```

matching:

```text
φ(H-U/V-H) = 4-1-4
```

The next useful continuation should explain what that recurrence means **before** selecting the next plaintext.

This gives a clean prospective test for Volume 5:

> Does the `4-1-4` state identify the next structure or key without introducing a new condition after candidate plaintext is found?

---

# PART X — RESEARCH CONCLUSION

## 49. Main conclusion of Volume 4

Volume 4 extends the route from:

```text
NOW THE
```

to:

```text
IDEA OF THE END
```

The important result is not only the English phrase.

The route repeatedly preserves structural continuity:

```text
plaintext endpoint
    ↓
new mirror role
    ↓
Euler transformation
    ↓
fixed Möbius phase
    ↓
new plaintext
    ↓
new endpoint
```

The most notable new cross-checks are:

```text
φ(J-OE-J) = φ(OE-J-OE) = 10-10-10
```

and:

```text
φ(I-TH-I) = φ(H-U/V-H) = 4-1-4
```

Together with the shared nodes and exact local radii, these relations support the working hypothesis that **mirror geometry, totient arithmetic, key generation, phase selection, and movement are interacting layers of one sequential system**.

The next challenge is no longer simply to find readable plaintext.

It is to determine the next structure **predictively** from the state that Volume 4 leaves behind.

---

## 50. Minimal machine-readable chain

```text
VOLUME_3_END:
plaintext = "AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE"
endpoint = J(15,20)

IDEA_PARENT_MIRROR:
A(8,13)
TH(11,16)
A(14,19)
radius = 3

IDEA_COMPILE:
TH = 2
phi(TH) = 1 = U/V
A-TH-A -> A-U/V-A

IDEA_SIGNATURE:
phi(A=24) = 8
phi(U/V=1) = 1
phi(A=24) = 8
signature = 8-1-8

IDEA_PHASE:
mu(8)+mu(1)+mu(8)
= 0+1+0
= 1 mod 3
phase = 1

IDEA_ACTIVE_KEY:
U/V-A-A

IDEA_CIPHERTEXT:
J(15,20)
E(16,19)
D(17,18)

IDEA_DECRYPT:
J(11)-U/V(1) = 10 = I
E(18)-A(24) mod 29 = 23 = D
D(23)-A(24) mod 29 = 28 = EA

IDEA_PLAINTEXT:
I-D-EA
"IDEA"

IDEA_ENDPOINT:
D(17,18)

NEXT_MIRROR:
J(15,20)
D(17,18)
J(19,16)
radius = 2

COMPILE:
D = 23
phi(D) = 22 = OE
J-D-J -> J-OE-J

SIGNATURE_A:
phi(J-OE-J) = 10-10-10

PHASE_A:
mu(10)+mu(10)+mu(10)
= 1+1+1
= 0 mod 3
phase = 0

ACTIVE_KEY_A:
J-OE-J

OF_CIPHERTEXT:
X(18,15)
OE(18,16)

OF_DECRYPT:
X(14)-J(11) = 3 = O
OE(22)-OE(22) = 0 = F

OF_PLAINTEXT:
"O-F"
"OF"

SHARED_NODE:
J(19,16)

NEXT_PHYSICAL_MIRROR:
OE(18,16)
J(19,16)
OE(20,16)
radius = 1

SIGNATURE_B:
phi(OE-J-OE) = 10-10-10

SIGNATURE_MATCH:
phi(J-OE-J)
=
phi(OE-J-OE)
=
10-10-10

THE_COMPILE:
J = 11
phi(J) = 10 = I
OE-J-OE -> OE-I-OE

THE_SIGNATURE:
10-4-10

THE_PHASE:
mu(10)+mu(4)+mu(10)
= 1+0+1
= 2 mod 3
phase = 2

THE_ACTIVE_KEY:
OE-OE-I

THE_CIPHERTEXT:
A(19,17)
J(19,16)

THE_DECRYPT:
A(24)-OE(22) = 2 = TH
J(11)-OE(22) mod 29 = 18 = E

THE_PLAINTEXT:
TH-E
"THE"

THE_ENDPOINT:
J(19,16)

POINTER:
F(19,15)

RADIUS_4_HORIZONTAL:
F(19,15)
X(19,19)
F(19,23)
radius = 4

RADIUS_4_VERTICAL:
Y(15,19)
X(19,19)
Y(23,19)
radius = 4

END_KEY_MIRROR:
J(19,16)
B(23,12)
J(27,8)
radius = 4

END_COMPILE:
B = 17
phi(B) = 16 = T
J-B-J -> J-T-J

END_SIGNATURE:
phi(J-T-J) = 10-8-10

END_PHASE:
mu(10)+mu(8)+mu(10)
= 1+0+1
= 2 mod 3
phase = 2

END_ACTIVE_KEY:
J-J-T

POINTER_TRANSITION:
F(19,15)
across F-X-F
-> F(19,23)

END_CIPHERTEXT:
F(19,23)
L(20,23)
I(21,23)

END_DECRYPT:
F(0)-J(11) mod 29 = 18 = E
L(20)-J(11) = 9 = N
I(10)-T(16) mod 29 = 23 = D

END_PLAINTEXT:
E-N-D
"END"

END_ENDPOINT:
I(21,23)

POST_END_MIRROR:
I(21,21)
R(21,22)
I(21,23)

POST_END_COMPILE:
R = 4
phi(R) = 2 = TH
I-R-I -> I-TH-I

POST_END_SIGNATURE:
phi(I-TH-I) = 4-1-4

EARLIER_SIGNATURE:
phi(H-U/V-H) = 4-1-4

FINAL_SIGNATURE_MATCH:
phi(I-TH-I)
=
phi(H-U/V-H)
=
4-1-4

VOLUME_4_RESULT:
"IDEA OF THE END"

CURRENT_RESULT:
"AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END ..."
```

---

## Related files

- [Volume 3 technical Markdown](./0-2-volume-3.md)
- [Raw pages 0–2 rune data](../0-2-runes.txt)
- [27×27 matrix image](../../liber-primus-27x27-matrix.png)
- [Repository README](../../README.md)

---

> **Research status:** proposed and reproducible at the level of the documented coordinates, Euler-totient transformations, Möbius phases, and mod-29 arithmetic. The larger transition system remains under active investigation and is not an officially verified Cicada 3301 solution.
