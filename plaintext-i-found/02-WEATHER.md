# 02 — WEATHER

> **Recovered plaintext:** `WEATHER`  
> **Current sequence:** `AS I GO THE WEATHER`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. The previous endpoint opens X-OE-X

`AS I GO THE` ends at:

```text
X(14,4)
```

That same cell is the left outer of:

```text
X(14,4) — OE(14,5) — X(14,6)
```

So the next key-generating structure is:

```text
X-OE-X
```

The center is:

```text
OE = 22
```

and:

```text
φ(22)=10=I
```

therefore:

```text
X-OE-X
→
X-I-X
```

So the new key structure is:

```text
X-I-X
```

---

## 2. The same value gives the movement

The center transformation produced:

```text
10
```

Reuse it as movement from the current route position:

```text
X(14,4)
→ RIGHT 10
→ NG(14,14)
```

This lands exactly on the unique center of the 27×27 grid:

```text
NG(14,14)
```

So the same `φ(OE)=10` both:

```text
generates I in the key
and
moves the route to the grid center
```

---

## 3. Möbius phase

For:

```text
X-I-X
```

the totient signature is:

```text
φ(X=14)=6
φ(I=10)=4
φ(X=14)=6
```

so:

```text
6-4-6
```

The Möbius values are:

```text
μ(6)=+1
μ(4)=0
μ(6)=+1
```

therefore:

```text
phase = 2
```

and:

```text
X-I-X
→ phase 2
→ X-X-I
```

For five runes:

```text
KEY = X-X-I-X-X
```

---

## 4. Ciphertext

Starting at the grid center and reading right:

```text
NG(14,14)
P(14,15)
EO(14,16)
O(14,17)
E(14,18)
```

gives:

```text
CIPHERTEXT = NG-P-EO-O-E
```

This sequence is directly checkable in the 27×27 grid.

---

## 5. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: NG  P   EO  O   E
Key:        X   X   I   X   X
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `NG=21` | `X=14` | `21-14 = 7 = W` |
| 2 | `P=13` | `X=14` | `13-14 ≡ 28 = EA` |
| 3 | `EO=12` | `I=10` | `12-10 = 2 = TH` |
| 4 | `O=3` | `X=14` | `3-14 ≡ 18 = E` |
| 5 | `E=18` | `X=14` | `18-14 = 4 = R` |

Therefore:

```text
NG-P-EO-O-E
-
X-X-I-X-X
=
W-EA-TH-E-R
```

# **WEATHER**

The plaintext becomes:

# **AS I GO THE WEATHER**

---

## 6. Why this branch is strong

The stage reuses one arithmetic value consistently:

```text
OE=22
↓
φ(OE)=10=I
```

which gives both:

```text
X-OE-X → X-I-X
```

and:

```text
RIGHT 10 → NG(14,14)
```

The route lands on the exact center of the entire grid, not an arbitrary cell.

There are also two useful cross-checks:

```text
J=11  → φ(J)=10=I
OE=22 → φ(OE)=10=I
```

so the first two key-generating centers independently reduce to the same rune `I`.

And directly above the first three ciphertext cells:

```text
NG-P-EO
```

the grid contains:

```text
W-EA-TH
```

This is a visual supporting clue, not part of the decryption rule.

---

## 7. Next state

`WEATHER` ends at:

```text
E(14,18)
```

Immediately to the right is:

```text
A(14,19)
```

which becomes the next crossroads.

The two active values carried forward are:

```text
I = 10
φ(I)=4
```

and the later coordinate selector at:

```text
A(14,19)
```

with phase `2` gives:

```text
V₂(14,19)=(-1,+1)
→ UP + RIGHT
```

These values drive the next stage:

```text
TURNS
```

---

## 8. Compact route

```text
AS I GO THE
↓
X(14,4)

↓
X-OE-X

↓
OE → I

↓
X-I-X

↓
signature 6-4-6
phase 2

↓
X-X-I

↓
RIGHT 10

NG(14,14)
= exact grid center

↓
ciphertext:
NG-P-EO-O-E

↓
W-EA-TH-E-R

↓
WEATHER
```
