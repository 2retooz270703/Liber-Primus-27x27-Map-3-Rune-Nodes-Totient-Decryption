# 12 — DEATH

> **Recovered plaintext:** `DEATH`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH`  
> **Status:** proposed reconstruction; not an officially verified Cicada 3301 solution.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. From IS to the old B-centered key generator

`IS` ends at:

```text
D(21,10)
```

which is the center of the exact radius-2 mirror:

```text
E(19,12) —2— D(21,10) —2— E(23,8)
```

Using the same radius perpendicular to that diagonal gives:

```text
D(21,10) → B(23,12)
```

`B(23,12)` is already known: it is the center of the mirror that generated the key for `END`:

```text
J(19,16) —4— B(23,12) —4— J(27,8)
```

So the route returns to the existing:

```text
J-B-J
```

structure instead of introducing a new key family.

---

## 2. Regenerate the key

The center is:

```text
B = 17
```

Apply Euler's totient:

```text
φ(17)=16=T
```

Therefore:

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

This is exactly the same key used for `END`.

---

## 3. Select the unused outer J

The two outers of `J-B-J` are:

```text
J(19,16)
J(27,8)
```

At:

```text
B(23,12)
```

with phase:

```text
p=2
```

the later coordinate selector gives:

```text
V₂(23,12)=(+1,-1)
```

meaning:

```text
DOWN + LEFT
```

That selects exactly:

```text
J(27,8)
```

rather than returning to the already used `J(19,16)`.

---

## 4. Local mirror chain to the ciphertext

The selected outer:

```text
J(27,8)
```

belongs to:

```text
J(25,6) — C(26,7) — J(27,8)
```

The shared:

```text
C(26,7)
```

is itself the right outer of:

```text
C(26,3) —2— OE(26,5) —2— C(26,7)
```

Following that mirror to its opposite outer gives:

```text
C(26,3)
```

From there, reading left:

```text
C(26,3)
I(26,2)
E(26,1)
```

gives:

```text
CIPHERTEXT = C-I-E
```

The full local route is:

```text
B(23,12)
↓
J(27,8)
↓
C(26,7)
↓
C(26,3)
↓
I(26,2)
↓
E(26,1)
```

---

## 5. Decryption

Use:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: C   I   E
Key:        J   J   T
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `C=5` | `J=11` | `5-11 ≡ 23 = D` |
| 2 | `I=10` | `J=11` | `10-11 ≡ 28 = EA` |
| 3 | `E=18` | `T=16` | `18-16 = 2 = TH` |

Therefore:

```text
C-I-E
-
J-J-T
=
D-EA-TH
```

# **DEATH**

The recovered clause is:

# **THE IDEA OF THE END IS DEATH**

---

## 6. Why this branch is strong

The important checks are compact:

```text
1. IS ends at the exact center of E-D-E.
2. Its radius 2 leads to the already used B(23,12).
3. B regenerates the same J-J-T key used for END.
4. V₂(23,12)=(+1,-1) selects the unused outer J(27,8).
5. Exact local mirrors connect J(27,8) to C(26,3).
6. The resulting contiguous C-I-E decrypts directly to DEATH.
```

The strongest feature is the recursion:

```text
END
→ leave J-B-J
→ IS
→ return to B(23,12)
→ regenerate J-J-T
→ DEATH
```

No new cipher mechanism is introduced.

---

## 7. Numerical cross-checks

### 233 → φ(233) → 232

The first seven-word block has GP sum:

```text
AS I GO THE WEATHER TURNS COLD = 233
```

The later seven-word block has:

```text
THE IDEA OF THE END IS DEATH = 232
```

Since `233` is prime:

```text
φ(233)=232
```

So:

```text
233
↓ φ
232
```

links two complete plaintext blocks.

### 17 → 16 → 53

The later seven-word block contains:

```text
17 runes
```

and the key-generating center is:

```text
B=17
```

Then:

```text
φ(17)=16=T
```

The 16th prime is:

```text
53
```

and:

```text
DEATH = D(23)+EA(28)+TH(2)=53
```

So:

```text
17
→ φ(17)=16
→ 16th prime=53
→ DEATH=53
```

These are supporting checks, not required for the decryption.

---

## 8. Frozen state after DEATH

`DEATH` ends at:

```text
E(26,1)
```

The pre-rotation structure remains:

```text
J-T-J
```

with:

```text
signature = 10-8-10
M = (+1,0,+1)
phase = 2
```

The later state model treats:

```text
(+1,0,+1)
```

as **OUTER-compatible**.

The endpoint selector is:

```text
V₂(26,1)
=
(0,+1)
```

so the post-`DEATH` state is:

```text
endpoint = E(26,1)
role = OUTER-compatible
horizontal side = RIGHT-compatible
vertical direction = unresolved
```

Important:

```text
E(26,1)
```

is **not** the earlier `E(26,16)` from:

```text
E(24,16)-X(25,16)-E(26,16)
```

so the old `E-X-E` mirror does not directly contain the `DEATH` endpoint.

---

## 9. Route-level totient observation

With `DEATH`, the reconstruction now contains 12 major route blocks:

```text
AS I GO THE
WEATHER
TURNS
COLD
I MAY
CRY
NOW THE
IDEA
OF THE
END
IS
DEATH
```

The central grid rune is:

```text
NG=21
```

and:

```text
φ(21)=12
```

So:

```text
NG=21
↓ φ
12
=
12 major blocks through DEATH
```

This becomes important in the next chapter, where the proposed missing route rule continues:

```text
φ(12)=4
```

and tests `4` as the next mirror scale.

---

## 10. Next chapter

The exact frozen endpoint is:

```text
E(26,1)
```

with:

```text
M=(+1,0,+1)
V₂=(0,+1)
```

The strongest current continuation searches for:

```text
OUTER
+
RIGHT-compatible
+
radius 4
```

and leads to the candidate:

```text
SEE
```
