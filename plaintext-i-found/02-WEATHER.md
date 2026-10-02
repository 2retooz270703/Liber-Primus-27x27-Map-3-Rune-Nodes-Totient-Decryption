# 02 — WEATHER

> **Recovered plaintext:** `WEATHER`  
> **Current sequence:** `AS I GO THE WEATHER`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

This chapter continues directly from the final point of the previous fragment:

```text
AS I GO THE
```

The previous ciphertext ended at:

```text
X(14,4)
```

That exact `X` is not an isolated endpoint. It is also the left outer rune of the next 3-rune structure, which is where the `WEATHER` stage begins.

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

---

## 1. The previous fragment ends inside the next node

The last ciphertext rune of `AS I GO THE` is:

```text
X(14,4)
```

Look immediately to the right in row 14:

```text
X(14,4) — OE(14,5) — X(14,6)
```

So the endpoint of the previous plaintext is simultaneously part of the next mirrored 3-rune node:

```text
X — OE — X
```

This gives a direct handoff:

```text
AS I GO THE
      ↓
final ciphertext rune X(14,4)
      ↓
X(14,4) — OE(14,5) — X(14,6)
```

---

## 2. X-OE-X generates the next key

The center of the new node is:

```text
OE(14,5)
```

Using the **0-based Gematria Primus index**:

```text
OE = 22
```

Apply Euler's totient function:

```text
φ(22) = 10
```

Gematria Primus index `10` is:

```text
I
```

So:

```text
X(14,4) — OE(14,5) — X(14,6)
                 ↓
              φ(22)=10
                 ↓
                 I
```

and the node becomes:

```text
X — I — X
```

Therefore the new 3-rune key is:

```text
KEY = X-I-X
```

---

## 3. The same value gives the movement

The center transformation produced:

```text
φ(OE) = 10
```

That same value is used as the movement distance.

Start again from the current route position:

```text
X(14,4)
```

Move 10 cells to the right:

```text
X(14,4) → RIGHT 10 → NG(14,14)
```

Check the column:

```text
4 + 10 = 14
```

So the destination is:

```text
NG(14,14)
```

This is especially important because a 27×27 grid has one exact center:

```text
center row    = 14
center column = 14
```

Therefore:

```text
NG(14,14)
```

is the **exact center of the entire 27×27 grid**.

The transition so far is:

```text
X(14,4) — OE(14,5) — X(14,6)
                 ↓
              OE = 22
                 ↓
              φ(22)=10=I
                 ↓
              KEY = X-I-X

X(14,4)
↓
RIGHT 10
↓
NG(14,14)
```

---

## 4. The key has three possible cyclic phases

A 3-rune key can begin in three different cyclic positions.

For:

```text
X-I-X
```

the possible phases are:

```text
phase 0: X-I-X-X-I-X...
phase 1: I-X-X-I-X-X...
phase 2: X-X-I-X-X-I...
```

So I need a rule that tells me which phase to use rather than choosing the one that gives readable English afterward.

The phase rule is:

```text
p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3
```

where:

```text
φ = Euler's totient function
μ = Möbius function
```

For the key:

```text
X-I-X
```

use the 0-based GP values:

```text
X = 14
I = 10
X = 14
```

Apply `φ`:

```text
φ(14) = 6
φ(10) = 4
φ(14) = 6
```

So the totient signature is:

```text
6-4-6
```

Now apply the Möbius function:

```text
μ(6) = +1
μ(4) = 0
μ(6) = +1
```

Therefore:

```text
p = (+1 + 0 + +1) mod 3
p = 2
```

So the active phase is:

```text
phase 2
```

and the active repeating key becomes:

```text
X-X-I
```

For a 5-rune ciphertext, that gives:

```text
KEY = X-X-I-X-X
```

---

## 5. The WEATHER ciphertext begins at the exact center

The movement landed on:

```text
NG(14,14)
```

Reading five cells to the right from that point gives:

```text
NG(14,14)
P(14,15)
EO(14,16)
O(14,17)
E(14,18)
```

So the 5-rune ciphertext is:

```text
CIPHERTEXT = NG-P-EO-O-E
```

This can be checked directly in `0-2-grid-i-used.txt`.

The plaintext word `WEATHER` is also five runes, because `EA` and `TH` are each single rune tokens:

```text
W — EA — TH — E — R
```

---

## 6. Decryption: C − K mod 29

The ciphertext is:

```text
NG-P-EO-O-E
```

The active key is:

```text
X-X-I-X-X
```

Align them:

```text
Ciphertext:  NG  P   EO  O   E
Key:         X   X   I   X   X
```

As before, decryption uses **0-based Gematria Primus values**:

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
NG = 21
P  = 13
EO = 12
O  = 3
E  = 18

X  = 14
I  = 10
```

Now decrypt each position:

| # | Ciphertext | C | Key | K | `(C - K) mod 29` | Plaintext |
|---:|---|---:|---|---:|---:|---|
| 1 | `NG(14,14)` | 21 | `X` | 14 | `21 - 14 = 7` | `W` |
| 2 | `P(14,15)` | 13 | `X` | 14 | `13 - 14 = -1 ≡ 28` | `EA` |
| 3 | `EO(14,16)` | 12 | `I` | 10 | `12 - 10 = 2` | `TH` |
| 4 | `O(14,17)` | 3 | `X` | 14 | `3 - 14 = -11 ≡ 18` | `E` |
| 5 | `E(14,18)` | 18 | `X` | 14 | `18 - 14 = 4` | `R` |

Therefore:

```text
Ciphertext:
NG-P-EO-O-E

Key:
X-X-I-X-X

(C - K) mod 29

Result:
W-EA-TH-E-R
```

which reads:

# **WEATHER**

The plaintext sequence is now:

# **AS I GO THE WEATHER**

---

## 7. The whole WEATHER route in one view

```text
previous ciphertext ends at:
X(14,4)

↓
adjacent mirrored node:
X(14,4) — OE(14,5) — X(14,6)

↓
center:
OE = 22

↓
φ(22) = 10 = I

↓
generated key:
X-I-X

↓
same value gives movement:
X(14,4) → RIGHT 10 → NG(14,14)

↓
NG(14,14) is the exact center of the 27×27 grid

↓
key phase:
φ(X-I-X) = 6-4-6
μ(6-4-6) = +1,0,+1

↓
p = 2

↓
active key:
X-X-I-X-X

↓
ciphertext:
NG(14,14)
P(14,15)
EO(14,16)
O(14,17)
E(14,18)

↓
CIPHERTEXT = NG-P-EO-O-E

↓
P = (C - K) mod 29

↓
W-EA-TH-E-R

↓
WEATHER
```

---

## 8. Strong structural cross-checks

These observations are not required to perform the decryption above, but they are useful because they independently connect this stage to the previous one.

### The first two node centers both reduce to I

The first stage used:

```text
J = 11
φ(11) = 10 = I
```

This stage uses:

```text
OE = 22
φ(22) = 10 = I
```

So the first two consecutive key-generating nodes are:

```text
AE-J-EA  →  AE-I-EA
X-OE-X   →  X-I-X
```

Among the relevant 0-based GP index values, `11` and `22` are the two values whose Euler totient is `10`.

So both stages independently converge on the same rune:

```text
I
```

---

### W-EA-TH appears directly above the ciphertext

The first three WEATHER ciphertext cells are:

```text
NG(14,14) — P(14,15) — EO(14,16)
```

Directly above them in row 13 are:

```text
W(13,14) — EA(13,15) — TH(13,16)
```

which reads:

```text
W-EA-TH
```

This is recorded as a **supporting visual clue**, not as part of the core decryption rule.

It is especially interesting because the key itself has a 3-position cyclic phase.

---

### The route lands on the exact center

The movement:

```text
X(14,4) → RIGHT 10
```

does not land on an arbitrary rune.

It lands on:

```text
NG(14,14)
```

the unique center cell of the 27×27 grid.

That gives the start of the WEATHER ciphertext a clear geometric position.

---

## 9. Where the next chapter starts

`WEATHER` ends on the ciphertext rune:

```text
E(14,18)
```

The immediately adjacent cell to the right is:

```text
A(14,19)
```

So the boundary is:

```text
E(14,18) → A(14,19)
```

That `A(14,19)` becomes the important crossroads used in the next stage.

The next chapter continues from:

```text
AS I GO THE WEATHER
```

to:

```text
AS I GO THE WEATHER TURNS
```

---

[← 01 — AS I GO THE](./01-AS-I-GO-THE.md)  
[← Back to the main page](../README.md)
