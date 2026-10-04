# 01 — AS I GO THE

> **Recovered plaintext:** `AS I GO THE`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. Build the grid

Liber Primus pages 0–2 contain:

```text
729 runes
```

and:

```text
729 = 27 × 27
```

So the rune stream is placed row-by-row into a:

```text
27×27 grid
```

This makes exact coordinates and geometric structures available.

---

## 2. First key-generating structure

The first important local structure is:

```text
M(12,11)    H(12,12)    M(12,13)

AE(13,11)   J(13,12)    EA(13,13)

EO(14,11)   AE(14,12)   OE(14,13)
```

The middle row is:

```text
AE(13,11) — J(13,12) — EA(13,13)
```

with center:

```text
J = 11
```

Apply Euler's totient:

```text
φ(11)=10=I
```

therefore:

```text
AE-J-EA
→
AE-I-EA
```

So the key is:

```text
KEY = AE-I-EA
```

Its later Möbius phase check gives:

```text
phase = 0
```

so the key is used without rotation.

---

## 3. Derive the movement

The same center gives:

```text
J = 11
φ(11)=10
φ(10)=4
```

Then:

```text
10+4=14
```

Using the left outer rune as the departure point:

```text
AE(13,11)
→ RIGHT 14
→ L(13,25)
```

This lands exactly at the start of the first ciphertext.

---

## 4. Ciphertext

Read forward from:

```text
L(13,25)
```

across the row boundary:

```text
L(13,25)
AE(13,26)
N(13,27)
TH(14,1)
P(14,2)
U(14,3)
X(14,4)
```

Therefore:

```text
CIPHERTEXT = L-AE-N-TH-P-U-X
```

Repeat the key across seven runes:

```text
KEY = AE-I-EA-AE-I-EA-AE
```

---

## 5. Decryption

Use:

```text
P = (C - K) mod 29
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `L=20` | `AE=25` | `20-25 ≡ 24 = A` |
| 2 | `AE=25` | `I=10` | `25-10 = 15 = S` |
| 3 | `N=9` | `EA=28` | `9-28 ≡ 10 = I` |
| 4 | `TH=2` | `AE=25` | `2-25 ≡ 6 = G` |
| 5 | `P=13` | `I=10` | `13-10 = 3 = O` |
| 6 | `U=1` | `EA=28` | `1-28 ≡ 2 = TH` |
| 7 | `X=14` | `AE=25` | `14-25 ≡ 18 = E` |

Therefore:

```text
L-AE-N-TH-P-U-X
-
AE-I-EA-AE-I-EA-AE
=
A-S-I-G-O-TH-E
```

# **AS I GO THE**

---

## 6. Why this branch is strong

The same `J` center generates both the key and movement:

```text
J
├─ φ(11)=10=I → AE-I-EA
└─ 10 + φ(10)=10+4=14 → RIGHT 14
```

That movement lands exactly on a seven-rune segment which decrypts cleanly under the generated repeating key.

No separate movement value or manually chosen key is introduced.

---

## 7. Next state

The final ciphertext rune is:

```text
X(14,4)
```

and the same cell is the left outer of the adjacent mirror:

```text
X(14,4) — OE(14,5) — X(14,6)
```

So the route continues directly into:

```text
X-OE-X
```

which generates the next plaintext:

```text
WEATHER
```

---

## 8. Compact route

```text
729 runes
↓
27×27 grid

↓
AE-J-EA

↓
J → I

↓
AE-I-EA
phase 0

↓
J=11
φ(J)=10
φ(10)=4
10+4=14

↓
RIGHT 14

↓
L-AE-N-TH-P-U-X

↓
AE-I-EA-AE-I-EA-AE

↓
A-S-I-G-O-TH-E

↓
AS I GO THE

↓
X-OE-X
→ WEATHER
```
