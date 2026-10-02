# 03 — TURNS

> **Recovered plaintext:** `TURNS`  
> **Current sequence:** `AS I GO THE WEATHER TURNS`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

This chapter continues directly from the end of `WEATHER`.

The previous ciphertext ended at:

```text
E(14,18)
```

The very next cell is:

```text
A(14,19)
```

That `A(14,19)` becomes the crossroads for the `TURNS` stage.

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

---

## 1. WEATHER leads directly to A(14,19)

The `WEATHER` ciphertext was:

```text
NG(14,14)
P(14,15)
EO(14,16)
O(14,17)
E(14,18)
```

So `WEATHER` ends at:

```text
E(14,18)
```

The next cell to the right is:

```text
A(14,19)
```

Therefore the handoff is immediate:

```text
WEATHER
   ↓
E(14,18) → A(14,19)
```

I treat:

```text
A(14,19)
```

as the next crossroads.

The two numerical values carried forward from the previous stage are:

```text
I = 10
```

and:

```text
φ(I) = φ(10) = 4
```

So the active movement values are:

```text
10 and 4
```

---

## 2. A(14,19) uses both inherited values

Starting from:

```text
A(14,19)
```

use the value `10` vertically:

```text
A(14,19) → UP 10 → NG(4,19)
```

because:

```text
14 - 10 = 4
```

Now use the value `4` horizontally from the same crossroads:

```text
A(14,19) → RIGHT 4 → NG(14,23)
```

because:

```text
19 + 4 = 23
```

So the two inherited values point to two `NG` cells:

```text
                 NG(4,19)
                    ↑
                   10
                    |
                A(14,19) ---- 4 ----> NG(14,23)
```

This is already a strong geometric structure: the same crossroads is connected to two `NG` runes by exactly the two values inherited from the previous stage.

---

## 3. The first NG is the center of I-NG-I

The point reached by moving `UP 10` is:

```text
NG(4,19)
```

In the grid, that rune is the center of:

```text
I(4,18) — NG(4,19) — I(4,20)
```

So the first branch reveals the mirrored node:

```text
I-NG-I
```

Its totient signature is:

```text
φ(I)  = φ(10) = 4
φ(NG) = φ(21) = 12
φ(I)  = φ(10) = 4
```

Therefore:

```text
I-NG-I → 4-12-4
```

Keep this numerical fingerprint:

```text
4-12-4
```

It appears again immediately.

---

## 4. The second NG reveals H-NG-C

The second movement from the crossroads was:

```text
A(14,19) → RIGHT 4 → NG(14,23)
```

This `NG(14,23)` is itself the center of a larger vertical structure.

Use the already active distance `10` above and below it:

```text
NG(14,23) → UP 10   → H(4,23)
NG(14,23) → DOWN 10 → C(24,23)
```

because:

```text
14 - 10 = 4
14 + 10 = 24
```

So the vertical structure is:

```text
H(4,23)
   |
  10
   |
NG(14,23)
   |
  10
   |
C(24,23)
```

This gives the 3-rune key:

```text
KEY = H-NG-C
```

There is also a horizontal symmetry around the same center:

```text
A(14,19) — 4 — NG(14,23) — 4 — A(14,27)
```

So `NG(14,23)` is not an arbitrary point. It is simultaneously the center of:

```text
A(14,19) — NG(14,23) — A(14,27)
```

and:

```text
H(4,23)
   |
NG(14,23)
   |
C(24,23)
```

---

## 5. H-NG-C has the same 4-12-4 fingerprint

Now take the totients of the new key:

```text
H  = 8
NG = 21
C  = 5
```

Apply Euler's totient:

```text
φ(H)  = φ(8)  = 4
φ(NG) = φ(21) = 12
φ(C)  = φ(5)  = 4
```

Therefore:

```text
H-NG-C → 4-12-4
```

This is exactly the same signature as the mirrored node found by the other branch:

```text
I(4,18)-NG(4,19)-I(4,20)
        ↓
      4-12-4
```

and:

```text
H(4,23)-NG(14,23)-C(24,23)
        ↓
      4-12-4
```

So the two different movements from `A(14,19)` lead to two different 3-rune structures with the same totient fingerprint:

```text
I-NG-I  → 4-12-4
H-NG-C  → 4-12-4
```

This is one of the strongest structural checks in this stage.

---

## 6. Möbius phase of H-NG-C

The key is:

```text
H-NG-C
```

Its totient signature is:

```text
4-12-4
```

Apply the Möbius function:

```text
μ(4)  = 0
μ(12) = 0
μ(4)  = 0
```

Therefore:

```text
p = (0 + 0 + 0) mod 3
p = 0
```

So the key is used **without rotation**:

```text
ACTIVE KEY = H-NG-C
```

For a 5-rune ciphertext, repeat it as:

```text
H-NG-C-H-NG
```

---

## 7. The TURNS ciphertext

Return to the crossroads:

```text
A(14,19)
```

Now read **upward in column 19**.

The five ciphertext cells are:

```text
A(14,19)
OE(13,19)
N(12,19)
B(11,19)
W(10,19)
```

So:

```text
CIPHERTEXT = A-OE-N-B-W
```

The active repeating key is:

```text
KEY = H-NG-C-H-NG
```

Align them:

```text
Ciphertext:  A   OE  N   B   W
Key:         H   NG  C   H   NG
```

---

## 8. Decryption: C − K mod 29

As before, decryption uses the **0-based Gematria Primus indices**:

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
A  = 24
OE = 22
N  = 9
B  = 17
W  = 7

H  = 8
NG = 21
C  = 5
```

Now decrypt each position:

| # | Ciphertext | C | Key | K | `(C - K) mod 29` | Plaintext |
|---:|---|---:|---|---:|---:|---|
| 1 | `A(14,19)` | 24 | `H` | 8 | `24 - 8 = 16` | `T` |
| 2 | `OE(13,19)` | 22 | `NG` | 21 | `22 - 21 = 1` | `U` |
| 3 | `N(12,19)` | 9 | `C` | 5 | `9 - 5 = 4` | `R` |
| 4 | `B(11,19)` | 17 | `H` | 8 | `17 - 8 = 9` | `N` |
| 5 | `W(10,19)` | 7 | `NG` | 21 | `7 - 21 = -14 ≡ 15` | `S` |

Therefore:

```text
Ciphertext:
A-OE-N-B-W

Key:
H-NG-C-H-NG

(C - K) mod 29

Result:
T-U-R-N-S
```

which reads:

# **TURNS**

The plaintext sequence is now:

# **AS I GO THE WEATHER TURNS**

---

## 9. The whole TURNS route in one view

```text
WEATHER ends at:
E(14,18)

↓
next cell:
A(14,19)

↓
inherited values:
I = 10
φ(I) = 4

↓
two movements from A(14,19):

UP 10
↓
NG(4,19)
↓
I(4,18)-NG(4,19)-I(4,20)
↓
signature 4-12-4


RIGHT 4
↓
NG(14,23)
↓
UP 10   → H(4,23)
DOWN 10 → C(24,23)
↓
H(4,23)-NG(14,23)-C(24,23)
↓
signature 4-12-4

↓
key:
H-NG-C

↓
Möbius phase:
μ(4), μ(12), μ(4)
= 0,0,0
↓
p = 0

↓
active 5-rune key:
H-NG-C-H-NG

↓
read upward from A(14,19):

A(14,19)
OE(13,19)
N(12,19)
B(11,19)
W(10,19)

↓
CIPHERTEXT = A-OE-N-B-W

↓
P = (C - K) mod 29

↓
T-U-R-N-S

↓
TURNS
```

---

## 10. Later cross-check: the coordinates predict UP + RIGHT

A later part of the research introduced a coordinate-direction selector.

This rule was **not needed to first obtain `TURNS`**, so I keep it separate from the core derivation above.

The incoming `WEATHER` key had:

```text
phase p = 2
```

Apply that same phase to the coordinates of the crossroads:

```text
A(14,19)
```

The later rule defines:

```text
V₂(14,19)
=
( μ(φ²(14)), μ(φ²(19)) )
```

For the row:

```text
14 → φ(14)=6 → φ(6)=2 → μ(2)=-1
```

For the column:

```text
19 → φ(19)=18 → φ(18)=6 → μ(6)=+1
```

Therefore:

```text
V₂(14,19) = (-1,+1)
```

with the direction convention:

```text
-1 row    = UP
+1 column = RIGHT
```

So the coordinate calculation independently gives:

```text
UP + RIGHT
```

which is exactly the direction pair used above:

```text
A(14,19) → UP 10
A(14,19) → RIGHT 4
```

The coordinate selector does **not** generate the distances `10` and `4`; those already come from the inherited totient state. It independently selects their directions.

---

## 11. Later interpretation: H-NG-C is a hidden non-mirrored key

A later volume distinguishes two kinds of discovered keys.

For a mirrored structure such as:

```text
X-OE-X
```

the center is transformed with `φ` before the key is used.

But:

```text
H(4,23)-NG(14,23)-C(24,23)
```

is **not mirrored**.

The later working rule therefore classifies it as a hidden non-mirrored key:

```text
H-NG-C → use directly
```

This matches what happens here: the key is not changed into another 3-rune sequence before decryption.

---

## 12. Original supporting observation

The older Volume 1 also recorded an `EA-G-EA` visual clue around the `WEATHER → TURNS` transition and explicitly treated the `G` branch as a false path.

That observation is not needed to reproduce `TURNS`, so I keep it outside the core route.

The reproducible handoff used in this chapter is simply:

```text
E(14,18) → A(14,19)
```

---

## 13. Where the next chapter starts

The final ciphertext rune of `TURNS` is:

```text
W(10,19)
```

The key used for `TURNS` contains:

```text
NG = 21
```

and:

```text
φ(21) = 12
```

That value `12` becomes the main movement value in the next stage.

The next chapter continues from:

```text
AS I GO THE WEATHER TURNS
```

to:

```text
AS I GO THE WEATHER TURNS COLD
```

---

[← 02 — WEATHER](./02-WEATHER.md)  
[← Back to the main page](../README.md)
