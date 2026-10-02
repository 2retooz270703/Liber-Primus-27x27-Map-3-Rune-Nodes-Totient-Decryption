# 02 — Key Phase Selection

> **Purpose:** define how the active cyclic phase of a 3-rune key is selected.  
> This rule determines **which rune the repeated key starts from** before decryption.

---

## 1. The phase problem

A 3-rune key can start in three cyclic positions.

For:

```text
k1-k2-k3
```

the three possible phases are:

```text
phase 0 → k1-k2-k3
phase 1 → k2-k3-k1
phase 2 → k3-k1-k2
```

Example:

```text
H-U-H
```

can be used as:

```text
phase 0 → H-U-H
phase 1 → U-H-H
phase 2 → H-H-U
```

So the route needs a rule that fixes the active starting position.

---

## 2. The Möbius phase rule

Let the key be:

```text
K = k1-k2-k3
```

First compute its totient signature:

```text
φ(k1)-φ(k2)-φ(k3)
```

Then apply the Möbius function `μ` to each signature value and sum the result:

```text
p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3
```

This gives the phase:

```text
p = 0 → phase 0
p = 1 → phase 1
p = 2 → phase 2
```

So the pipeline is:

```text
3-rune key
↓
totient signature
↓
Möbius values
↓
sum mod 3
↓
active phase
```

---

## 3. How the phase is used

Once `p` is known, the key is rotated before being repeated across the ciphertext.

For:

```text
k1-k2-k3
```

the active key becomes:

```text
p=0 → k1-k2-k3
p=1 → k2-k3-k1
p=2 → k3-k1-k2
```

Then that rotated 3-rune key is repeated to match the ciphertext length.

---

## 4. Example: AE-I-EA

Start with:

```text
AE-I-EA
```

Compute the signature:

```text
φ(AE=25)=20
φ(I=10)=4
φ(EA=28)=12
```

so:

```text
20-4-12
```

Apply Möbius:

```text
μ(20)=0
μ(4)=0
μ(12)=0
```

Sum:

```text
0+0+0 = 0
```

Therefore:

```text
p = 0
```

So the key remains:

```text
AE-I-EA
```

This is the phase used in:

```text
AS I GO THE
```

---

## 5. Example: X-I-X

Start with:

```text
X-I-X
```

Compute the signature:

```text
φ(X=14)=6
φ(I=10)=4
φ(X=14)=6
```

so:

```text
6-4-6
```

Apply Möbius:

```text
μ(6)=+1
μ(4)=0
μ(6)=+1
```

Sum:

```text
1+0+1 = 2
```

Therefore:

```text
p = 2
```

So the active key is:

```text
X-I-X
→
X-X-I
```

This is the phase used in:

```text
WEATHER
```

---

## 6. Example: H-U-H

Start with:

```text
H-U-H
```

Compute the signature:

```text
φ(H=8)=4
φ(U=1)=1
φ(H=8)=4
```

so:

```text
4-1-4
```

Apply Möbius:

```text
μ(4)=0
μ(1)=+1
μ(4)=0
```

Sum:

```text
0+1+0 = 1
```

Therefore:

```text
p = 1
```

So the active key is:

```text
H-U-H
→
U-H-H
```

This is the phase used in:

```text
COLD
```

---

## 7. Example: J-T-J

Start with:

```text
J-T-J
```

Compute the signature:

```text
φ(J=11)=10
φ(T=16)=8
φ(J=11)=10
```

so:

```text
10-8-10
```

Apply Möbius:

```text
μ(10)=+1
μ(8)=0
μ(10)=+1
```

Sum:

```text
1+0+1 = 2
```

Therefore:

```text
p = 2
```

So the active key is:

```text
J-T-J
→
J-J-T
```

This is the phase used in:

```text
END
and
DEATH
```

---

## 8. Why this rule matters

Without a phase rule, every 3-rune key would have three possible cyclic starts, and the plaintext could be chosen by trial and error.

The Möbius phase rule removes that freedom:

```text
key
→ signature
→ Möbius sum
→ fixed phase
→ active repeated key
```

So the route does not need to guess which cyclic rotation to use.

---

## 9. Evidence status

The rule is strongly supported because it works consistently across the recovered route.

Clean examples include:

```text
AE-I-EA → p=0
X-I-X   → p=2
H-U-H   → p=1
J-T-J   → p=2
```

This file defines only the phase rule itself.

Later files explain how the same totient and Möbius machinery is used for:

```text
movement values
coordinate selectors
CENTER / OUTER state roles
inheritance
route selection
```
