# 04 — COLD

> **Recovered plaintext:** `COLD`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

This chapter continues directly from `TURNS`.

The previous stage was built from the crossroads:

```text
A(14,19)
```

and the key:

```text
H-NG-C
```

The important value carried forward from that key is the value of its center rune:

```text
NG = 21
φ(21) = 12
```

That single value `12` controls both branches of the `COLD` stage.

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

---

## 1. TURNS gives the next control value: 12

The key used for `TURNS` was:

```text
H-NG-C
```

Its center rune is:

```text
NG = 21
```

Apply Euler's totient function:

```text
φ(21) = 12
```

So the next control value is:

```text
12
```

The same crossroads is reused:

```text
A(14,19)
```

but now the movement is:

```text
DOWN 12
LEFT 12
```

These two movements do two different jobs:

```text
DOWN 12 → finds the next key-generating structure
LEFT 12 → finds the next ciphertext start
```

That dual use of the same value is one of the strongest structural features of this stage.

---

## 2. DOWN 12 finds H-TH-H

Start from:

```text
A(14,19)
```

Move down 12 cells:

```text
A(14,19) → DOWN 12 → TH(26,19)
```

because:

```text
14 + 12 = 26
```

The landing cell is not isolated. It is the center of this vertical mirrored node:

```text
H(25,19)
   |
TH(26,19)
   |
H(27,19)
```

So the discovered structure is:

```text
H-TH-H
```

This is a proper mirrored 3-rune node:

```text
outer — center — outer
H     — TH     — H
```

---

## 3. LEFT 12 finds the COLD ciphertext start

Return to the same crossroads:

```text
A(14,19)
```

Move left 12 cells:

```text
A(14,19) → LEFT 12 → G(14,7)
```

because:

```text
19 - 12 = 7
```

So the same value:

```text
12 = φ(NG)
```

has now identified both:

```text
TH(26,19)  → center of the next key node
G(14,7)    → start of the next ciphertext
```

In one view:

```text
                     A(14,19)
                    /        \
             DOWN 12          LEFT 12
                ↓                 ↓
          TH(26,19)            G(14,7)
              ↓                   ↓
          H-TH-H              ciphertext
          key node              start
```

---

## 4. Compile H-TH-H into the key

The same node-compilation rule used earlier is:

```text
K = (a, φ(b), c)
```

For:

```text
H-TH-H
```

the center rune is:

```text
TH = 2
```

Apply Euler's totient:

```text
φ(2) = 1
```

Gematria Primus index `1` is:

```text
U
```

Therefore:

```text
H-TH-H
   ↓
φ(TH=2)=1=U
   ↓
H-U-H
```

So the generated key is:

```text
KEY = H-U-H
```

---

## 5. Möbius phase of H-U-H

The 3-rune key is:

```text
H-U-H
```

Using the 0-based Gematria Primus indices:

```text
H = 8
U = 1
H = 8
```

Apply Euler's totient:

```text
φ(8) = 4
φ(1) = 1
φ(8) = 4
```

So the key signature is:

```text
4-1-4
```

Now apply the Möbius function:

```text
μ(4) = 0
μ(1) = +1
μ(4) = 0
```

The phase is:

```text
p = (0 + 1 + 0) mod 3
p = 1
```

Therefore the key rotates from:

```text
H-U-H
```

to:

```text
U-H-H
```

For a 4-rune ciphertext, repeat the cycle:

```text
ACTIVE KEY = U-H-H-U
```

---

## 6. The COLD ciphertext

The ciphertext starts at:

```text
G(14,7)
```

Read upward in column 7:

```text
G(14,7)
J(13,7)
EA(12,7)
A(11,7)
```

So:

```text
CIPHERTEXT = G-J-EA-A
```

The active key is:

```text
KEY = U-H-H-U
```

Align them:

```text
Ciphertext:  G   J   EA  A
Key:         U   H   H   U
```

---

## 7. Decryption: C − K mod 29

As before:

```text
P = (C - K) mod 29
```

where:

```text
C = ciphertext rune value
K = key rune value
P = plaintext rune value
```

The values needed here are:

```text
G  = 6
J  = 11
EA = 28
A  = 24

U  = 1
H  = 8
```

Now decrypt each position:

| # | Ciphertext | C | Key | K | `(C - K) mod 29` | Plaintext |
|---:|---|---:|---|---:|---:|---|
| 1 | `G(14,7)` | 6 | `U` | 1 | `6 - 1 = 5` | `C` |
| 2 | `J(13,7)` | 11 | `H` | 8 | `11 - 8 = 3` | `O` |
| 3 | `EA(12,7)` | 28 | `H` | 8 | `28 - 8 = 20` | `L` |
| 4 | `A(11,7)` | 24 | `U` | 1 | `24 - 1 = 23` | `D` |

Therefore:

```text
Ciphertext:
G-J-EA-A

Key:
U-H-H-U

(C - K) mod 29

Result:
C-O-L-D
```

which reads:

# **COLD**

The first recovered block is now:

# **AS I GO THE WEATHER TURNS COLD**

---

## 8. The whole COLD route in one view

```text
TURNS key:
H-NG-C

↓
center rune:
NG = 21

↓
φ(21) = 12

↓
return to:
A(14,19)

↓
use 12 in two directions:


A(14,19)
│
├── DOWN 12
│      ↓
│   TH(26,19)
│      ↓
│   H(25,19)-TH(26,19)-H(27,19)
│      ↓
│   H-TH-H
│      ↓
│   φ(TH=2)=1=U
│      ↓
│   H-U-H
│      ↓
│   signature 4-1-4
│      ↓
│   μ = 0,+1,0
│      ↓
│   phase p=1
│      ↓
│   active key U-H-H-U
│
└── LEFT 12
       ↓
    G(14,7)
       ↓
    read upward:
    G(14,7)
    J(13,7)
    EA(12,7)
    A(11,7)
       ↓
    CIPHERTEXT = G-J-EA-A

↓
P = (C - K) mod 29

↓
C-O-L-D

↓
COLD
```

---

## 9. Strong cross-check: the same A crossroads changes direction with phase

A later part of the research introduced a coordinate-direction selector.

This rule was **not required to first obtain `COLD`**, so it is kept as a later independent cross-check.

The same physical cell:

```text
A(14,19)
```

was already used for the `TURNS` stage.

There, the incoming phase was:

```text
p = 2
```

and the later coordinate rule produced:

```text
UP + RIGHT
```

For the transition from `TURNS` to `COLD`, the active `H-NG-C` key has:

```text
p = 0
```

Apply phase 0 directly to the coordinates:

```text
V₀(14,19)
=
( μ(14), μ(19) )
```

Now:

```text
μ(14) = +1
μ(19) = -1
```

Using the direction convention:

```text
+1 row    = DOWN
-1 column = LEFT
```

gives:

```text
V₀(14,19) = (+1,-1)
```

therefore:

```text
DOWN + LEFT
```

which is exactly the direction pair used in the core route:

```text
DOWN 12
LEFT 12
```

This is particularly interesting because the **same coordinate** changes its branch when the incoming phase changes:

```text
A(14,19), p=2 → UP + RIGHT   → TURNS
A(14,19), p=0 → DOWN + LEFT  → COLD
```

So the direction does not behave like a fixed arrow attached to the cell itself.

---

## 10. Strong cross-check: column 19 → column 7

The `TURNS` ciphertext ends at:

```text
W(10,19)
```

So it ends in:

```text
column 19
```

The `COLD` ciphertext begins at:

```text
G(14,7)
```

So it begins in:

```text
column 7
```

The difference is:

```text
19 - 7 = 12
```

and the controlling value for this transition is exactly:

```text
φ(NG) = 12
```

Therefore the geometric transition is:

```text
column 19
   ↓
minus 12
   ↓
column 7
```

This is the same `12` already used to find the H-TH-H key node.

The older Volume 1 also noted that `W` has 0-based GP index `7` and prime value `19`, creating another `19 ↔ 7` association. I treat that numerical coincidence as supporting evidence rather than as part of the decryption rule.

---

## 11. Strong cross-check at the COLD endpoint

`COLD` ends at:

```text
A(11,7)
```

That exact rune is the center of another mirrored structure:

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

So the endpoint is not just an arbitrary final ciphertext cell.

Now compare this with the Möbius state of the `COLD` key:

```text
H-U-H
```

Its signature was:

```text
4-1-4
```

and:

```text
μ(4), μ(1), μ(4)
=
0,+1,0
```

So the full Möbius state is:

```text
(0,+1,0)
```

A later volume observed that this state repeatedly behaves like a **CENTER-active** state.

Here, that later interpretation matches the geometry exactly:

```text
H-U-H
↓
M = (0,+1,0)
↓
COLD
↓
A(11,7)
↓
CENTER of EA-A-EA
```

This is a later structural cross-check, not a rule that was needed to force the plaintext.

---

## 12. The endpoint already carries the next structural fingerprint

The new endpoint structure is:

```text
EA-A-EA
```

Its totient signature is:

```text
φ(EA=28) = 12
φ(A=24)  = 8
φ(EA=28) = 12
```

therefore:

```text
EA-A-EA → 12-8-12
```

This matters in the next chapter because the key later found for `I MAY` has the **same signature**:

```text
12-8-12
```

So the end of `COLD` already contains a numerical fingerprint that reappears in the next decryption stage.

---

## 13. Numerical checkpoint after the first seven words

`COLD` completes the first seven-word plaintext block:

```text
AS I GO THE WEATHER TURNS COLD
```

Using rune tokens, this contains:

```text
7 words
21 runes
```

The full 0-based Gematria Primus index sum is:

```text
233
```

The word:

```text
COLD
```

has index sum:

```text
C + O + L + D
= 5 + 3 + 20 + 23
= 51
```

And:

```text
233 is the 51st prime
```

So the observed relation is:

```text
COLD sum = 51
51st prime = 233
full 7-word block sum = 233
```

There is also a Fibonacci observation recorded in the earlier research:

```text
F₇  = 13
F₁₃ = 233
```

giving:

```text
7 → 13 → 233
```

These numerical relations are **supporting checks only**. They are not needed to derive the route or decrypt `COLD`.

---

## 14. A smaller transition hint

The last ciphertext rune is:

```text
A(11,7)
```

and:

```text
φ(A=24) = 8
```

Gematria Primus index `8` is:

```text
H
```

So:

```text
A → φ(A)=H
```

The older research recorded this as another possible hint toward the `H`-based structures used around this transition.

I treat it as secondary evidence, not as a route-selection rule.

---

## 15. Where the next chapter starts

The post-`COLD` state is now:

```text
endpoint:
A(11,7)

endpoint node:
EA(10,7)-A(11,7)-EA(12,7)

COLD key:
H-U-H

inherited signature:
4-1-4
```

The next stage reuses that inherited:

```text
4-1-4
```

as movement information beginning from:

```text
A(11,7)
```

The next chapter continues from:

```text
AS I GO THE WEATHER TURNS COLD
```

to:

```text
AS I GO THE WEATHER TURNS COLD I MAY
```

---

[← 03 — TURNS](./03-TURNS.md)  
[← Back to the main page](../README.md)
