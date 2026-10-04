# 05 — I MAY

> **Recovered plaintext:** `I MAY`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. COLD leaves the signal 4-1-4

`COLD` ends at:

```text
A(11,7)
```

The key used for `COLD` came from:

```text
H-TH-H
→
H-U-H
```

with signature:

```text
4-1-4
```

The later coordinate selector at the `COLD` endpoint gives:

```text
V₁(11,7)=(+1,+1)
```

so the inherited values are used as:

```text
DOWN 4
RIGHT 1
```

Starting from:

```text
A(11,7)
```

gives:

```text
A(11,7)
→ DOWN 4
→ S(15,7)
→ RIGHT 1
→ B(15,8)
```

---

## 2. B reveals the hidden key structure

`B(15,8)` is the center of:

```text
NG(13,8) —2— B(15,8) —2— NG(17,8)
```

So the hidden mirror is:

```text
NG-B-NG
```

The center is:

```text
B = 17
```

Apply Euler's totient:

```text
φ(17)=16=T
```

therefore:

```text
NG-B-NG
→
NG-T-NG
```

So the key structure is:

```text
NG-T-NG
```

---

## 3. Exact signature match at the COLD endpoint

The final `A(11,7)` of `COLD` is itself the center of:

```text
EA(10,7)
A(11,7)
EA(12,7)
```

or:

```text
EA-A-EA
```

Its signature is:

```text
φ(EA=28)=12
φ(A=24)=8
φ(EA=28)=12
```

so:

```text
EA-A-EA
→
12-8-12
```

The newly found key has exactly the same signature:

```text
NG-T-NG
→
12-8-12
```

Therefore:

```text
EA-A-EA
→ 12-8-12
← NG-T-NG
```

This is a strong structural cross-check linking the `COLD` endpoint to the `I MAY` key.

---

## 4. Möbius phase

For:

```text
12-8-12
```

the Möbius values are:

```text
μ(12)=0
μ(8)=0
μ(12)=0
```

so:

```text
M=(0,0,0)
phase=0
```

The key is not rotated:

```text
KEY = NG-T-NG
```

For four ciphertext runes it repeats as:

```text
NG-T-NG-NG
```

---

## 5. Return to H-TH-H

The new key is applied back to the preserved parent structure:

```text
H-TH-H
```

Its center is:

```text
TH(26,19)
```

Reading left gives:

```text
TH(26,19)
G(26,18)
T(26,17)
E(26,16)
```

Therefore:

```text
CIPHERTEXT = TH-G-T-E
```

---

## 6. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: TH  G   T   E
Key:        NG  T   NG  NG
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `TH=2` | `NG=21` | `2-21 ≡ 10 = I` |
| 2 | `G=6` | `T=16` | `6-16 ≡ 19 = M` |
| 3 | `T=16` | `NG=21` | `16-21 ≡ 24 = A` |
| 4 | `E=18` | `NG=21` | `18-21 ≡ 26 = Y` |

Therefore:

```text
TH-G-T-E
-
NG-T-NG-NG
=
I-M-A-Y
```

# **I MAY**

---

## 7. Why this branch is strong

The transition uses one connected chain:

```text
COLD endpoint A(11,7)
→ inherited 4-1 movement
→ B(15,8)
→ NG-B-NG
→ B transforms to T
→ NG-T-NG
→ exact signature match 12-8-12
→ phase 0
→ TH-G-T-E
→ I MAY
```

No new decryption rule is introduced.

The especially strong check is:

```text
EA-A-EA
→ 12-8-12
← NG-T-NG
```

because the endpoint structure and the hidden key independently produce the same numerical fingerprint.

---

## 8. Next state

`I MAY` ends at:

```text
E(26,16)
```

which is already the lower outer of:

```text
E(24,16)
X(25,16)
E(26,16)
```

So the route immediately enters:

```text
E-X-E
```

The later coordinate selector gives:

```text
V₀(26,16)=(+1,0)
```

which is only partial, so local mirror geometry supplies the next transition.

The center transforms as:

```text
X=14
φ(14)=6=G
```

therefore:

```text
E-X-E
→
E-G-E
```

which begins the next plaintext:

```text
CRY
```

---

## 9. Compact route

```text
COLD ends at:
A(11,7)

↓
signature inherited:
4-1-4

↓
DOWN 4, RIGHT 1

B(15,8)

↓
NG-B-NG

↓
B → T

↓
NG-T-NG

↓
signature 12-8-12
phase 0

↓
return to H-TH-H

↓
ciphertext:
TH-G-T-E

↓
I-M-A-Y

↓
I MAY
```
