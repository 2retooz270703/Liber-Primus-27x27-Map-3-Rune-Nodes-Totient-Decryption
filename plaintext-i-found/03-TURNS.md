# 03 — TURNS

> **Recovered plaintext:** `TURNS`  
> **Current sequence:** `AS I GO THE WEATHER TURNS`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. WEATHER leads to the A crossroads

After `WEATHER`, the route continues to:

```text
A(14,19)
```

The two active control values are inherited from the previous `I`:

```text
I = 10
φ(I)=4
```

From `A(14,19)` they are reused as movement distances:

```text
UP 10
RIGHT 4
```

The later coordinate selector independently agrees with these directions:

```text
phase = 2

V₂(14,19)=(-1,+1)
→ UP + RIGHT
```

---

## 2. Locate the key structure

The rightward movement lands on:

```text
NG(14,23)
```

with:

```text
A(14,19) —4— NG(14,23) —4— A(14,27)
```

Using the other inherited value vertically from this `NG`:

```text
UP 10   → H(4,23)
DOWN 10 → C(24,23)
```

forms:

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

So the key is:

```text
KEY = H-NG-C
```

This is a non-mirrored structure, so it is used directly.

---

## 3. Signature and phase

Its totient signature is:

```text
φ(H=8)=4
φ(NG=21)=12
φ(C=5)=4
```

therefore:

```text
4-12-4
```

This exactly matches the signature of the related mirrored structure:

```text
I-NG-I
→ 4-12-4
```

For `H-NG-C`:

```text
μ(4)=0
μ(12)=0
μ(4)=0
```

so:

```text
phase = 0
```

and the key remains:

```text
H-NG-C
```

Repeated across five runes:

```text
H-NG-C-H-NG
```

---

## 4. Ciphertext

Reading upward from the crossroads gives:

```text
A(14,19)
OE(13,19)
N(12,19)
B(11,19)
W(10,19)
```

Therefore:

```text
CIPHERTEXT = A-OE-N-B-W
```

---

## 5. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: A   OE  N   B   W
Key:        H   NG  C   H   NG
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `A=24` | `H=8` | `24-8 = 16 = T` |
| 2 | `OE=22` | `NG=21` | `22-21 = 1 = U` |
| 3 | `N=9` | `C=5` | `9-5 = 4 = R` |
| 4 | `B=17` | `H=8` | `17-8 = 9 = N` |
| 5 | `W=7` | `NG=21` | `7-21 ≡ 15 = S` |

Therefore:

```text
A-OE-N-B-W
-
H-NG-C-H-NG
=
T-U-R-N-S
```

# **TURNS**

The plaintext becomes:

# **AS I GO THE WEATHER TURNS**

---

## 6. Why this branch is strong

The stage reuses the same two inherited values throughout:

```text
10 and 4
```

They first select the route:

```text
A(14,19)
→ UP 10
→ RIGHT 4
→ NG(14,23)
```

and then define the cross containing the key:

```text
A —4— NG —4— A
        |
       10
        |
        H / C
```

The resulting key also has the exact signature match:

```text
H-NG-C
→ 4-12-4
← I-NG-I
```

No new decryption rule is introduced.

---

## 7. Next state

The key center is:

```text
NG = 21
```

so:

```text
φ(NG)=12
```

This new value controls the next transition from the same crossroads:

```text
A(14,19)
→ DOWN 12
→ center of H-TH-H

A(14,19)
→ LEFT 12
→ G(14,7)
```

The later selector for the new phase agrees:

```text
V₀(14,19)=(+1,-1)
→ DOWN + LEFT
```

These two 12-step branches begin the next plaintext:

```text
COLD
```

---

## 8. Compact route

```text
WEATHER
↓
A(14,19)

inherited:
10 and 4

↓
UP 10
RIGHT 4

NG(14,23)

↓
vertical ±10

H-NG-C

↓
signature 4-12-4
phase 0

↓
ciphertext:
A-OE-N-B-W

↓
T-U-R-N-S

↓
TURNS

↓
NG=21
φ(NG)=12

↓
next:
COLD
```
