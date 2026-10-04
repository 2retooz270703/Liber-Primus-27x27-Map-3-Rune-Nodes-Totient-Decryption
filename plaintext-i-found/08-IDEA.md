# 08 — IDEA

> **Recovered plaintext:** `IDEA`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. NOW THE ends at the IDEA ciphertext start

`NOW THE` ends at:

```text
J(15,20)
```

and the same cell becomes the first ciphertext rune of `IDEA`.

Nearby, on the same diagonal, is the exact radius-3 mirror:

```text
A(8,13) —3— TH(11,16) —3— A(14,19)
```

The route has already passed through:

```text
A(14,19)
```

and reaches:

```text
J(15,20)
```

immediately beyond it on the same diagonal.

So:

```text
A-TH-A
```

is the local key-generating structure for the next block.

---

## 2. Generate the key

The center is:

```text
TH = 2
```

Apply Euler's totient:

```text
φ(2)=1=U
```

therefore:

```text
A-TH-A
→
A-U-A
```

Its totient signature is:

```text
φ(A=24)=8
φ(U=1)=1
φ(A=24)=8
```

so:

```text
8-1-8
```

The Möbius values are:

```text
μ(8)=0
μ(1)=+1
μ(8)=0
```

therefore:

```text
phase = 1
```

and:

```text
A-U-A
→ phase 1
→ U-A-A
```

So the active key is:

```text
KEY = U-A-A
```

---

## 3. IDEA ciphertext

From:

```text
J(15,20)
```

continue diagonally down-left:

```text
J(15,20)
E(16,19)
D(17,18)
```

Therefore:

```text
CIPHERTEXT = J-E-D
```

---

## 4. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: J   E   D
Key:        U   A   A
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `J=11` | `U=1` | `11-1 = 10 = I` |
| 2 | `E=18` | `A=24` | `18-24 ≡ 23 = D` |
| 3 | `D=23` | `A=24` | `23-24 ≡ 28 = EA` |

Therefore:

```text
J-E-D
-
U-A-A
=
I-D-EA
```

# **IDEA**

The plaintext becomes:

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA**

---

## 5. Strong state cross-check: 010 → CENTER

The key structure:

```text
A-U-A
```

has:

```text
signature = 8-1-8
M = (0,+1,0)
phase = 1
```

`IDEA` ends at:

```text
D(17,18)
```

and that exact cell is the center of:

```text
J(15,20) —2— D(17,18) —2— J(19,16)
```

So:

```text
A-U-A
→ M=(0,+1,0)
→ IDEA
→ endpoint becomes CENTER of J-D-J
```

This matches the same later pattern seen with `COLD` and `IS`:

```text
(0,+1,0) → CENTER-compatible
```

The decryption itself does not depend on this later interpretation.

---

## 6. Next state

The endpoint:

```text
D(17,18)
```

is already the center of:

```text
J-D-J
```

Compile the center:

```text
D=23
φ(23)=22=OE
```

therefore:

```text
J-D-J
→
J-OE-J
```

Its signature is:

```text
10-10-10
```

which exactly matches the next physical mirror:

```text
OE(18,16) — J(19,16) — OE(20,16)
```

because:

```text
φ(OE-J-OE)=10-10-10
```

This prepares the next plaintext block:

```text
OF THE
```

The later coordinate selector at the `IDEA` endpoint is:

```text
V₁(17,18)=(0,+1)
```

so the selector is partial and local mirror geometry supplies the continuation.

---

## 7. Compact route

```text
NOW THE ends at:
J(15,20)

↓
local mirror:
A(8,13) —3— TH(11,16) —3— A(14,19)

↓
TH → U

↓
A-U-A

↓
signature 8-1-8
phase 1

↓
U-A-A

ciphertext:
J-E-D

↓
I-D-EA

↓
IDEA

↓
endpoint D(17,18)
= center of J-D-J

↓
D → OE

↓
J-OE-J
→ signature 10-10-10

↓
next:
OF THE
```
