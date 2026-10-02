# 01 — AS I GO THE

> **Recovered fragment:** `AS I GO THE`  
> **Status:** proposed research; not an officially verified Cicada 3301 solution.

This is the first readable fragment I recovered from **Liber Primus pages 0–2**.

The purpose of this chapter is simple: show the path from the original runes to **AS I GO THE** without mixing in the later parts of the route.

---

## 1. The starting observation: 729 = 27 × 27

Pages 0–2 contain exactly **729 runes**.

```text
729 = 27 × 27
```

So I placed the runes in their original order into a **27×27 grid**, reading left to right and continuing on the next row after every 27 runes.

This was the first important change in how I looked at the text: the runes were no longer only a one-dimensional ciphertext. They could also be treated as a **map**.

![Liber Primus 27×27 rune grid](../other-stuff/data/grid.png)

---

## 2. The first structure that stood out

Near the center-left of the grid I noticed an unusual 3×3 area:

```text
M    H    M
AE   J    EA
EO   AE   OE
```

I first noticed and highlighted this region manually. I then used AI-assisted analysis to test whether its internal structure could produce a useful key.

The middle row became the important part:

```text
AE — J — EA
```

Using the **0-based Gematria Primus indices**:

```text
J = 11
```

Apply Euler's totient function:

```text
φ(11) = 10
```

and Gematria Primus index `10` is:

```text
I
```

So the three-rune structure changes from:

```text
AE — J — EA
```

to:

```text
AE — I — EA
```

This gives the first repeating key:

```text
AE-I-EA
```

---

## 3. The same totient chain gives the movement

The center rune does more than generate the key.

Starting again from:

```text
J = 11
```

the first totient gives:

```text
φ(11) = 10 = I
```

Apply the totient once more:

```text
φ(10) = 4
```

Now combine the two derived values:

```text
10 + 4 = 14
```

This gives the first movement used in the route:

```text
RIGHT 14
```

The left rune of the original structure is:

```text
AE(13,11)
```

Moving 14 cells to the right lands exactly on:

```text
L(13,25)
```

So the chain is:

```text
AE-J-EA
   ↓
J = 11
   ↓ φ
10 = I
   ↓ φ
4

10 + 4 = 14
   ↓
RIGHT 14

AE(13,11) → L(13,25)
```

---

## 4. The first ciphertext segment

From `L(13,25)`, I continued to the end of row 13 and then into row 14.

That gives exactly seven ciphertext runes:

```text
L — AE — N — TH — P — U/V — X
```

The route ends this first read at:

```text
X(14,4)
```

This endpoint is useful later because the same `X` becomes part of the next structural handoff. In other words, the first plaintext block does not simply stop at an arbitrary cell.

---

## 5. Decryption

Repeat the three-rune key across the seven ciphertext runes:

```text
Ciphertext:  L   AE   N   TH   P   U/V   X
Key:         AE  I    EA  AE   I   EA    AE
```

Decryption uses Gematria Primus subtraction modulo 29:

```text
P = (C - K) mod 29
```

| # | Cipher | Key | Calculation | Plain |
|---:|---|---|---|---|
| 1 | `L = 20` | `AE = 25` | `20 - 25 ≡ 24` | `A` |
| 2 | `AE = 25` | `I = 10` | `25 - 10 = 15` | `S` |
| 3 | `N = 9` | `EA = 28` | `9 - 28 ≡ 10` | `I` |
| 4 | `TH = 2` | `AE = 25` | `2 - 25 ≡ 6` | `G` |
| 5 | `P = 13` | `I = 10` | `13 - 10 = 3` | `O` |
| 6 | `U/V = 1` | `EA = 28` | `1 - 28 ≡ 2` | `TH` |
| 7 | `X = 14` | `AE = 25` | `14 - 25 ≡ 18` | `E` |

Therefore:

```text
A — S — I — G — O — TH — E
```

which reads:

# **AS I GO THE**

---

## 6. A later cross-check: the key phase

The first fragment was found before the full phase rule was formalized. Later, the Möbius phase rule provided an independent check that the key should begin in exactly this orientation.

For:

```text
AE-I-EA
```

the totient signature is:

```text
φ(AE), φ(I), φ(EA)
= 20, 4, 12
```

and:

```text
μ(20), μ(4), μ(12)
= 0, 0, 0
```

So:

```text
p = (0 + 0 + 0) mod 3
  = 0
```

Phase `0` means the key is used without rotation:

```text
AE-I-EA
```

That is the same phase used in the original decryption.

---

## Why this first result matters

The fragment is not based only on finding an English phrase. The same local structure produces the **key**, produces the values used for the **movement**, the movement lands on the exact start of the seven-rune ciphertext, and the decryption works by the same modulo-29 subtraction later used throughout the route.

The final `X` also becomes the handoff into the next stage.

So the first route can be compressed to:

```text
729 runes
   ↓
27×27 grid
   ↓
AE-J-EA
   ↓ φ(center)
AE-I-EA
   ↓
J: 11 → 10 → 4
   ↓
10 + 4 = RIGHT 14
   ↓
L-AE-N-TH-P-U/V-X
   ↓
subtract AE-I-EA mod 29
   ↓
AS I GO THE
```

---

[← Back to the main page](../README.md)
