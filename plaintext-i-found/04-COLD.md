# 04 — COLD

> **Recovered plaintext:** `COLD`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

Coordinates are **1-based**.

---

## 1. TURNS leaves the value 12

`TURNS` returns to the crossroads:

```text
A(14,19)
```

The central rune of the preceding structure is:

```text
NG = 21
```

Apply Euler's totient:

```text
φ(21)=12
```

Volume 1 uses this same value in two directions from `A(14,19)`:

```text
DOWN 12
LEFT 12
```

These two branches locate the next key structure and ciphertext start.

---

## 2. Two 12-step branches

### Key branch

```text
A(14,19)
→ DOWN 12
→ TH(26,19)
```

`TH(26,19)` is the center of:

```text
H-TH-H
```

### Ciphertext branch

```text
A(14,19)
→ LEFT 12
→ G(14,7)
```

So one value:

```text
φ(NG)=12
```

selects both:

```text
key structure
and
ciphertext start
```

The later coordinate selector is consistent with these directions:

```text
V₀(14,19)=(+1,-1)
→ DOWN + LEFT
```

This selector is a later cross-check; the original route already records the two 12-step branches.

---

## 3. Generate the key

The center of:

```text
H-TH-H
```

is:

```text
TH = 2
```

Apply Euler's totient:

```text
φ(2)=1=U
```

therefore:

```text
H-TH-H
→
H-U-H
```

Its totient signature is:

```text
φ(H=8)=4
φ(U=1)=1
φ(H=8)=4
```

so:

```text
4-1-4
```

The Möbius values are:

```text
μ(4)=0
μ(1)=+1
μ(4)=0
```

therefore:

```text
phase = 1
```

and:

```text
H-U-H
→ phase 1
→ U-H-H
```

So the active repeating key is:

```text
KEY = U-H-H-U
```

---

## 4. Ciphertext

Starting from:

```text
G(14,7)
```

read upward:

```text
G(14,7)
J(13,7)
EA(12,7)
A(11,7)
```

Therefore:

```text
CIPHERTEXT = G-J-EA-A
```

---

## 5. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: G   J   EA  A
Key:        U   H   H   U
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `G=6` | `U=1` | `6-1 = 5 = C` |
| 2 | `J=11` | `H=8` | `11-8 = 3 = O` |
| 3 | `EA=28` | `H=8` | `28-8 = 20 = L` |
| 4 | `A=24` | `U=1` | `24-1 = 23 = D` |

Therefore:

```text
G-J-EA-A
-
U-H-H-U
=
C-O-L-D
```

# **COLD**

The first recovered sentence is:

# **AS I GO THE WEATHER TURNS COLD**

---

## 6. Why this branch is strong

The core transition is unusually compact:

```text
NG=21
↓
φ(NG)=12

A(14,19)
├─ DOWN 12 → H-TH-H → key
└─ LEFT 12 → G(14,7) → ciphertext
```

The same derived value controls both parts of the stage, and the key itself follows the already established center-totient rule:

```text
H-TH-H
→ H-U-H
→ phase 1
→ U-H-H
```

No new cipher mechanism is introduced.

---

## 7. Strong state cross-check: 010 → CENTER

The key structure:

```text
H-U-H
```

has:

```text
signature = 4-1-4
M = (0,+1,0)
phase = 1
```

`COLD` ends at:

```text
A(11,7)
```

and that exact cell is the center of:

```text
EA(10,7)
A(11,7)
EA(12,7)
```

or:

```text
EA-A-EA
```

So:

```text
H-U-H
→ M=(0,+1,0)
→ COLD
→ endpoint becomes CENTER of EA-A-EA
```

This later supports the working rule:

```text
(0,+1,0) → CENTER-compatible
```

The decryption itself does not depend on this later interpretation.

---

## 8. Next state

The active signature remains:

```text
4-1-4
```

and the later coordinate selector at:

```text
A(11,7)
```

gives:

```text
V₁(11,7)=(+1,+1)
```

So the next movement uses:

```text
DOWN 4
RIGHT 1
```

which leads to:

```text
B(15,8)
```

the center of:

```text
NG-B-NG
```

This begins the next plaintext:

```text
I MAY
```

---

## 9. Compact route

```text
TURNS
↓
A(14,19)

NG=21
↓
φ(NG)=12

A(14,19)
├─ DOWN 12 → H-TH-H
└─ LEFT 12 → G(14,7)

H-TH-H
↓
TH → U
↓
H-U-H
↓
signature 4-1-4
phase 1
↓
U-H-H

ciphertext:
G-J-EA-A

↓
C-O-L-D

↓
COLD
```

---

[← 03 — TURNS](./03-TURNS.md)  
[← Back to the main page](../README.md)
