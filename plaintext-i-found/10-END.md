# 10 — END

> **Recovered plaintext:** `END`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. THE ends beside a radius-4 pointer

`THE` ends at:

```text
J(19,16)
```

Immediately left is:

```text
F(19,15)
```

which is the left outer of:

```text
F(19,15) —4— X(19,19) —4— F(19,23)
```

So the opposite outer:

```text
F(19,23)
```

becomes the next ciphertext start.

The same center `X(19,19)` also belongs to the perpendicular mirror:

```text
Y(15,19)
    |
    4
    |
X(19,19)
    |
    4
    |
Y(23,19)
```

This reinforces the local radius-4 geometry.

---

## 2. Generate the key from J-B-J

The `THE` endpoint:

```text
J(19,16)
```

is also an outer of:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
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
J-B-J
→
J-T-J
```

Its totient signature is:

```text
φ(J=11)=10
φ(T=16)=8
φ(J=11)=10
```

so:

```text
10-8-10
```

The Möbius values are:

```text
μ(10)=+1
μ(8)=0
μ(10)=+1
```

therefore:

```text
phase = 2
```

and:

```text
J-T-J
→ phase 2
→ J-J-T
```

So the active key is:

```text
KEY = J-J-T
```

---

## 3. END ciphertext

From the opposite outer of `F-X-F`:

```text
F(19,23)
```

read downward:

```text
F(19,23)
L(20,23)
I(21,23)
```

Therefore:

```text
CIPHERTEXT = F-L-I
```

---

## 4. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: F   L   I
Key:        J   J   T
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `F=0` | `J=11` | `0-11 ≡ 18 = E` |
| 2 | `L=20` | `J=11` | `20-11 = 9 = N` |
| 3 | `I=10` | `T=16` | `10-16 ≡ 23 = D` |

Therefore:

```text
F-L-I
-
J-J-T
=
E-N-D
```

# **END**

The plaintext becomes:

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END**

---

## 5. Why this branch is strong

The transition uses two exact radius-4 structures in the same local region:

```text
F-X-F
→ selects the ciphertext start F(19,23)

J-B-J
→ generates the key J-J-T
```

So the same scale:

```text
4
```

controls both route relocation and key generation.

No new cipher rule is introduced.

---

## 6. Strong state cross-check: 101 → OUTER

The pre-rotation structure:

```text
J-T-J
```

has:

```text
signature = 10-8-10
M = (+1,0,+1)
phase = 2
```

`END` finishes at:

```text
I(21,23)
```

and that exact cell is the right outer of:

```text
I(21,21) — R(21,22) — I(21,23)
```

So:

```text
J-T-J
→ M=(+1,0,+1)
→ END
→ endpoint becomes OUTER of I-R-I
```

This matches the earlier `NOW THE` case and supports the later working rule:

```text
(+1,0,+1) → OUTER-compatible
```

The plaintext decryption itself does not depend on this later state interpretation.

---

## 7. Next state

The endpoint:

```text
I(21,23)
```

is already part of:

```text
I-R-I
```

with:

```text
R=4
φ(4)=2=TH
```

therefore:

```text
I-R-I
→
I-TH-I
```

Its totient signature is:

```text
4-1-4
```

The same center `R(21,22)` also opens:

```text
H(21,17) — R(21,22) — H(21,27)
```

which compiles to:

```text
H-TH-H
```

with the same signature:

```text
4-1-4
```

This prepares the next plaintext:

```text
IS
```

The later coordinate selector at the `END` endpoint is:

```text
V₂(21,23)=(0,+1)
```

so the selector is partial and local mirror geometry supplies the continuation.

---

## 8. Compact route

```text
THE ends at J(19,16)

↓
adjacent pointer:
F(19,15)

↓
F(19,15) —4— X(19,19) —4— F(19,23)

↓
ciphertext start:
F(19,23)

meanwhile:

J(19,16) —4— B(23,12) —4— J(27,8)

↓
B → T

↓
J-T-J

↓
phase 2

↓
J-J-T

ciphertext:
F-L-I

↓
E-N-D

↓
END
```
