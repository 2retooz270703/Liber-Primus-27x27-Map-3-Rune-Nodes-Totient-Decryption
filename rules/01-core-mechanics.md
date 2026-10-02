# 01 — Core Mechanics

> **Purpose:** define the basic objects and arithmetic used throughout the 27×27 route.  
> More advanced rules — phase selection, coordinate selectors, state roles, inheritance, and route selection — are explained separately.

---

## 1. The 27×27 grid

Liber Primus pages 0–2 contain:

```text
729 rune positions
```

Since:

```text
729 = 27 × 27
```

the rune stream is placed row-by-row into a:

```text
27×27 grid
```

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

Example:

```text
J(13,12)
```

means row 13, column 12.

The grid is not only a layout: its rows, columns, diagonals, centers, and mirrored structures are used by the route.

---

## 2. Rune values

The arithmetic uses the **0-based Gematria Primus indices**.

Examples:

```text
U  = 1
TH = 2
J  = 11
I  = 10
NG = 21
EA = 28
```

Transliterations such as:

```text
AE
EA
OE
EO
NG
TH
```

are single rune tokens, not multiple Latin letters.

Unless stated otherwise, all numeric operations in the route use these 0-based rune values.

---

## 3. Three-rune structures

A recurring structural unit is:

```text
a-b-c
```

where the middle rune is the **center**.

Mirrored structures have the form:

```text
a-b-a
```

Examples:

```text
X-OE-X
H-TH-H
OE-J-OE
```

Non-mirrored structures can also act as keys:

```text
H-NG-C
```

The important point is that the route repeatedly treats three-rune structures as functional units for key generation, matching, and navigation.

---

## 4. Center totient transformation

When a three-rune structure is compiled, Euler's totient is applied to its center:

```text
a-b-c
→
a-φ(b)-c
```

The transformed number is mapped back to the rune with that Gematria Primus index.

### Example 1

```text
AE-J-EA

J = 11
φ(11)=10
10 = I
```

therefore:

```text
AE-J-EA
→
AE-I-EA
```

### Example 2

```text
H-TH-H

TH = 2
φ(2)=1
1 = U
```

therefore:

```text
H-TH-H
→
H-U-H
```

This is the basic key-generation operation used repeatedly in the route.

---

## 5. Totient signature

After a key is generated, apply `φ` to each of its three runes:

```text
K = k1-k2-k3
```

then:

```text
signature(K)
=
φ(k1)-φ(k2)-φ(k3)
```

Example:

```text
H-U-H
```

gives:

```text
φ(H=8)=4
φ(U=1)=1
φ(H=8)=4
```

so:

```text
signature = 4-1-4
```

These signatures are later used for:

```text
phase selection
structural matching
movement / inheritance
state analysis
```

The rules for those uses are defined separately.

---

## 6. Repeating keys

A three-rune key is repeated to match the ciphertext length.

Example:

```text
key:
AE-I-EA

7-rune repetition:
AE-I-EA-AE-I-EA-AE
```

The starting position of the cyclic key can change.

That rotation is determined by the **Möbius phase rule**, explained separately.

---

## 7. Modular decryption

Plaintext is recovered with:

```text
P = (C - K) mod 29
```

where:

```text
C = ciphertext rune value
K = active key rune value
P = plaintext rune value
```

Example:

```text
C = L  = 20
K = AE = 25

20 - 25 = -5
-5 mod 29 = 24

24 = A
```

So:

```text
L - AE
→ A
```

The same subtraction is applied rune by rune across the full ciphertext.

---

## 8. Core pipeline

The basic mechanism can be reduced to:

```text
729 runes
↓
27×27 grid
↓
three-rune structure
↓
transform center with φ
↓
3-rune key
↓
totient signature
↓
select active key phase
↓
repeat key across ciphertext
↓
P = (C - K) mod 29
↓
plaintext
↓
next structural location
```

This file defines only the foundation.

The later rules explain how the system chooses:

```text
which key phase is active
which direction to move
which values are inherited
whether the next role is CENTER or OUTER
how partial / null selectors are resolved
how the next route structure is selected
```
