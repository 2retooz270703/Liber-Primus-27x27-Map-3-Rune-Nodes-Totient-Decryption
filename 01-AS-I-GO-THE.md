# 01 — AS I GO THE

> **Recovered plaintext:** `AS I GO THE`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

This chapter shows exactly how I obtained the first readable fragment:

# **AS I GO THE**

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Keep that file open while reading.  
Every coordinate in this chapter refers to that grid and is written as:

```text
(row, column)
```

The coordinates are **1-based**.

---

## 1. Why there is a 27×27 grid

Liber Primus pages 0–2 contain exactly:

```text
729 runes
```

and:

```text
729 = 27 × 27
```

So I arranged the 729 runes in their original order into a square:

```text
27 rows × 27 columns
```

I wrote the runes left to right. After 27 runes, the sequence continues at the beginning of the next row.

The resulting grid is the file:

```text
0-2-grid-i-used.txt
```

From this point onward, I treat the rune text not only as a linear ciphertext, but also as a **map with exact coordinates**.

---

## 2. The first 3×3 structure I noticed

Near the center-left of the grid, I noticed this exact 3×3 block:

```text
M(12,11)    H(12,12)    M(12,13)

AE(13,11)   J(13,12)    EA(13,13)

EO(14,11)   AE(14,12)   OE(14,13)
```

The part that immediately interested me was the middle row:

```text
AE(13,11) — J(13,12) — EA(13,13)
```

It has a simple 3-rune structure:

```text
AE — J — EA
```

The center rune is:

```text
J(13,12)
```

Using the **0-based Gematria Primus index**:

```text
J = 11
```

Now apply Euler's totient function:

```text
φ(11) = 10
```

Gematria Primus index `10` is:

```text
I
```

So the middle row transforms as:

```text
AE(13,11) — J(13,12) — EA(13,13)
                 ↓
              φ(11)=10
                 ↓
                 I
```

which gives the 3-rune key:

```text
AE — I — EA
```

or:

```text
KEY = AE-I-EA
```

---

## 3. The same center rune gives the movement distance

The center rune `J(13,12)` also gives the numerical values that lead to the first ciphertext.

Start with:

```text
J = 11
```

First totient:

```text
φ(11) = 10
```

Second totient:

```text
φ(10) = 4
```

Then:

```text
10 + 4 = 14
```

So I get the movement distance:

```text
14
```

For this first step, I use the **left outer rune of the 3-rune row** as the departure point:

```text
AE(13,11)
```

Move 14 cells to the right:

```text
AE(13,11) → RIGHT 14 → L(13,25)
```

Check the columns:

```text
11 + 14 = 25
```

So the movement lands exactly on:

```text
L(13,25)
```

That is the beginning of the first ciphertext segment.

The complete derivation is:

```text
center: J(13,12)

J = 11
↓
φ(11) = 10
↓
φ(10) = 4
↓
10 + 4 = 14

departure point: AE(13,11)
↓
RIGHT 14
↓
L(13,25)
```

---

## 4. The first ciphertext

Starting at:

```text
L(13,25)
```

I read to the right until the end of row 13:

```text
L(13,25) — AE(13,26) — N(13,27)
```

Then the sequence continues at the beginning of row 14:

```text
TH(14,1) — P(14,2) — U/V(14,3) — X(14,4)
```

So the complete 7-rune ciphertext is:

```text
L(13,25)
AE(13,26)
N(13,27)
TH(14,1)
P(14,2)
U/V(14,3)
X(14,4)
```

or, compactly:

```text
CIPHERTEXT = L-AE-N-TH-P-U/V-X
```

---

## 5. The key used to decrypt it

The key generated from the 3-rune node was:

```text
AE-I-EA
```

The ciphertext has 7 runes, so I repeat the key until it also has 7 positions:

```text
KEY = AE-I-EA-AE-I-EA-AE
```

Now align ciphertext and key:

```text
Ciphertext:  L   AE  N   TH  P   U/V X
Key:         AE  I   EA  AE  I   EA  AE
```

---

## 6. The decryption rule: C − K mod 29

I use **0-based Gematria Primus values** and subtraction modulo 29.

The rule is:

```text
P = (C - K) mod 29
```

where:

```text
C = ciphertext rune value
K = key rune value
P = plaintext rune value
```

So at every position:

```text
ciphertext value
− key value
mod 29
= plaintext value
```

The relevant 0-based values are:

```text
L   = 20
AE  = 25
N   = 9
TH  = 2
P   = 13
U/V = 1
X   = 14

I   = 10
EA  = 28
```

Now decrypt each rune.

| # | Ciphertext | C | Key | K | `(C - K) mod 29` | Plaintext |
|---:|---|---:|---|---:|---:|---|
| 1 | `L(13,25)` | 20 | `AE` | 25 | `20 - 25 = -5 ≡ 24` | `A` |
| 2 | `AE(13,26)` | 25 | `I` | 10 | `25 - 10 = 15` | `S` |
| 3 | `N(13,27)` | 9 | `EA` | 28 | `9 - 28 = -19 ≡ 10` | `I` |
| 4 | `TH(14,1)` | 2 | `AE` | 25 | `2 - 25 = -23 ≡ 6` | `G` |
| 5 | `P(14,2)` | 13 | `I` | 10 | `13 - 10 = 3` | `O` |
| 6 | `U/V(14,3)` | 1 | `EA` | 28 | `1 - 28 = -27 ≡ 2` | `TH` |
| 7 | `X(14,4)` | 14 | `AE` | 25 | `14 - 25 = -11 ≡ 18` | `E` |

Therefore:

```text
Ciphertext:
L-AE-N-TH-P-U/V-X

Key:
AE-I-EA-AE-I-EA-AE

(C - K) mod 29

Result:
A-S-I-G-O-TH-E
```

The plaintext runes read:

# **AS I GO THE**

---

## 7. The whole first route in one view

```text
729 runes
↓
27×27 grid
↓
3×3 structure:

M(12,11)    H(12,12)    M(12,13)
AE(13,11)   J(13,12)    EA(13,13)
EO(14,11)   AE(14,12)   OE(14,13)

↓
middle row:
AE(13,11) — J(13,12) — EA(13,13)

↓
J = 11
φ(11) = 10 = I

↓
key:
AE-I-EA

↓
movement values:
11 → φ → 10 → φ → 4
10 + 4 = 14

↓
AE(13,11) → RIGHT 14 → L(13,25)

↓
ciphertext:
L(13,25)
AE(13,26)
N(13,27)
TH(14,1)
P(14,2)
U/V(14,3)
X(14,4)

↓
repeating key:
AE-I-EA-AE-I-EA-AE

↓
P = (C - K) mod 29

↓
A-S-I-G-O-TH-E

↓
AS I GO THE
```

---

## 8. Later cross-check: the key phase

This was not needed to first discover `AS I GO THE`, but a later rule gives an independent check of the key orientation.

For the generated key:

```text
AE-I-EA
```

the totient signature is:

```text
φ(AE) = 20
φ(I)  = 4
φ(EA) = 12
```

so:

```text
20-4-12
```

Apply the Möbius function:

```text
μ(20) = 0
μ(4)  = 0
μ(12) = 0
```

Therefore:

```text
p = (0 + 0 + 0) mod 3
p = 0
```

Phase `0` means:

```text
do not rotate the key
```

so the active key remains:

```text
AE-I-EA
```

That is exactly the orientation used above.

---

## 9. Where the next chapter starts

The first ciphertext ends at:

```text
X(14,4)
```

That exact grid point becomes part of the next structural transition.

So the next stage begins from:

```text
X(14,4)
```

and continues the plaintext from:

```text
AS I GO THE
```

to:

```text
AS I GO THE WEATHER
```

---

[← Back to the main page](../README.md)
