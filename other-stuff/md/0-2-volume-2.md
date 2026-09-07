# Cicada 3301 Liber Primus 0-2
## 27x27 Rune Matrix Decryption - Volume 2

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.  
**Date:** 06.09.2026

> **Strongest plaintext candidate**
>
> **AS I GO, THE WEATHER TURNS COLD.**  
> **I MAY CRY...**

---

## 1. Purpose of Volume 2

Volume 1 ends at:

**AS I GO, THE WEATHER TURNS COLD.**

Volume 2 continues from the final state of **COLD**.

The main new observation is that totient values appear to persist across stages of the route. In some cases, values already derived from a key or node are reused as movement distances and lead to the location of another key.

The exact rule that decides **when this mechanism is activated** is still unknown. However, the mechanism is visible in multiple strong examples.

---

## 2. Core rules used in this volume

### 2.1 Mirrored 3-rune node compilation

For a mirrored node:

`a-b-a`

apply Euler's totient to the center:

`a-b-a -> a-phi(b)-a`

Example:

`H-TH-H -> H-U-H`

because:

`phi(TH=2)=1=U`

### 2.2 Totient signature

For a key `K=(k1,k2,k3)`:

`signature(K) = (phi(k1), phi(k2), phi(k3))`

### 2.3 Mobius phase

The cyclic key phase is:

`p = sum(mu(phi(ki))) mod 3`

The phase is therefore determined numerically, before judging the plaintext.

### 2.4 Gematria subtraction

Decryption uses:

`plaintext = ciphertext - key mod 29`

with Gematria Primus values from Volume 1.

---

## 3. Two observed types of keys

### Type A - directly generated keys

A mirrored 3-rune node directly generates a key by transforming its center with `phi`.

Example:

`H-TH-H -> H-U-H`

### Type B - hidden keys

Some keys are not generated at the current node.

Instead, specific totient values derived earlier in the route are reused as movement distances. Those movements lead to the location of another key in the 27x27 grid.

Observed pattern:

`earlier totient values -> movement -> hidden key location`

The activation rule is not yet fully known.

---

## 4. Mirrored vs non-mirrored hidden keys

A second distinction appears in the current model.

If a discovered key is **non-mirrored**, it is used directly.

Example:

`H-NG-C -> H-NG-C`

If a discovered structure is **mirrored**, its center is transformed by `phi` before the final key is used.

Example:

`NG-B-NG -> phi(B)=T -> NG-T-NG`

This suggests a close relationship between **mirror symmetry** and **totient transformation**.

---

# PART I - COLD -> I MAY

## 5. Frozen state at the end of COLD

Volume 1 derives the COLD key from:

`H-TH-H -> H-U-H`

because:

`phi(TH=2)=1=U`

The totient signature of `H-U-H` is:

`4-1-4`

The ciphertext for **COLD** ends at:

`A(11,7)`

So the post-COLD state contains:

- parent structure: `H-TH-H`
- active/generated key: `H-U-H`
- inherited totient signal: `4-1-4`
- COLD endpoint: `A(11,7)`

---

## 6. A structural fingerprint at the COLD endpoint

The final A of COLD is immediately inside:

`EA(10,7) - A(11,7) - EA(12,7)`

So:

`EA-A-EA`

Its totient signature is:

`phi(EA=28)=12`
`phi(A=24)=8`
`phi(EA=28)=12`

Therefore:

`EA-A-EA -> 12-8-12`

This becomes important because the later I MAY key has the exact same signature.

---

## 7. The inherited 4-1-4 signal locates B

Starting from the final A of COLD:

`A(11,7)`

reuse the inherited values from `H-U-H -> 4-1-4`.

Movement:

`D4: A(11,7) -> S(15,7)`

then:

`R1: S(15,7) -> B(15,8)`

So:

`A(11,7) -> D4 -> S(15,7) -> R1 -> B(15,8)`

---

## 8. B reveals the hidden mirrored structure

B is the center of:

`NG(13,8) - B(15,8) - NG(17,8)`

Therefore the discovered structure is:

`NG-B-NG`

Because it is mirrored, transform the center:

`phi(B=17)=16=T`

So:

`NG-B-NG -> NG-T-NG`

The actual key is:

`NG-T-NG`

Its totient signature is:

`phi(NG=21)=12`
`phi(T=16)=8`
`phi(NG=21)=12`

Therefore:

`NG-T-NG -> 12-8-12`

This gives the exact structural match:

`EA-A-EA -> 12-8-12 <- NG-T-NG`

The endpoint of COLD already contains the numerical fingerprint of the key later used for I MAY.

---

## 9. Mobius phase of NG-T-NG

For:

`NG-T-NG -> 12-8-12`

the Mobius values are:

`mu(12)=0`
`mu(8)=0`
`mu(12)=0`

Therefore:

`p = 0`

The key is not rotated.

The three cyclic phases produce:

| Phase | Result |
|---|---|
| 0 | `I M A Y` |
| 1 | `S X A TH` |
| 2 | `I X F Y` |

The Mobius rule independently selects **phase 0**.

---

## 10. Return to the preserved H-TH-H structure

The newly found key is applied back to the same preserved parent structure:

`H-TH-H`

This is the structure that previously generated `H-U-H` for COLD.

Its center is:

`TH(26,19)`

Reading left gives:

`TH(26,19) - G(26,18) - T(26,17) - E(26,16)`

Ciphertext:

`TH-G-T-E`

Repeating key:

`NG-T-NG-NG`

Decryption:

`TH(2) - NG(21) mod 29 = 10 = I`
`G(6) - T(16) mod 29 = 19 = M`
`T(16) - NG(21) mod 29 = 24 = A`
`E(18) - NG(21) mod 29 = 26 = Y`

Therefore:

`TH-G-T-E - NG-T-NG-NG = I-M-A-Y`

Result:

> **I MAY**

---

## 11. Compact I MAY chain

```text
H-TH-H
  |
  | phi(TH)=U
  v
H-U-H
  |
  | totient signature
  v
4-1-4
  |
  | after COLD: D4, R1
  v
B(15,8)
  |
  v
NG-B-NG
  |
  | phi(B)=T
  v
NG-T-NG
  |
  | signature 12-8-12
  | Mobius phase 0
  v
return to H-TH-H
  |
  | read TH-G-T-E
  v
I MAY
```

Strong structural cross-check:

`EA-A-EA -> 12-8-12 <- NG-T-NG`

---

# PART II - I MAY -> CRY

## 12. The final E of I MAY opens the next node

The ciphertext for I MAY ends at:

`E(26,16)`

That same rune is immediately part of:

`E(24,16) - X(25,16) - E(26,16)`

So the next mirrored structure is:

`E-X-E`

This repeats an important behavior of the model: the end of one read can become part of the next structural node.

---

## 13. E-X-E generates E-G-E

Because the node is mirrored:

`phi(X=14)=6=G`

Therefore:

`E-X-E -> E-G-E`

Its totient signature is:

`phi(E=18)=6`
`phi(G=6)=2`
`phi(E=18)=6`

So:

`E-G-E -> 6-2-6`

---

## 14. Mobius phase of E-G-E

For:

`6-2-6`

the Mobius values are:

`mu(6)=+1`
`mu(2)=-1`
`mu(6)=+1`

Therefore:

`p = (+1 - 1 + 1) mod 3 = 1`

The active key becomes:

`G-E-E`

The three possible phases produce:

| Phase | Result |
|---|---|
| 0 | `OE T Y` |
| 1 | `C R Y` |
| 2 | `OE R N` |

Again, the Mobius rule independently selects the phase that produces the readable plaintext.

---

## 15. The inherited value 6 leads to J

Using the outer totient value:

`6`

move upward from the center X:

`X(25,16) -> U6 -> J(19,16)`

J is exactly the center of:

`OE(18,16) - J(19,16) - OE(20,16)`

Reading upward from J gives:

`J(19,16) - OE(18,16) - S(17,16)`

Ciphertext:

`J-OE-S`

---

## 16. Decrypting CRY

Active key:

`G-E-E`

Decryption:

`J(11) - G(6) = 5 = C`
`OE(22) - E(18) = 4 = R`
`S(15) - E(18) mod 29 = 26 = Y`

Therefore:

`J-OE-S - G-E-E = C-R-Y`

Result:

> **CRY**

---

## 17. Compact CRY chain

```text
I MAY
  |
  | final ciphertext rune E
  v
E-X-E
  |
  | phi(X)=G
  v
E-G-E
  |
  | totient signature
  v
6-2-6
  |
  | Mobius phase 1
  v
G-E-E
  |
  | U6 from X
  v
J(19,16)
  |
  | read J-OE-S upward
  v
CRY
```

---

# PART III - TOTIENT CHAIN / STRUCTURAL INHERITANCE

## 18. Main structural idea

The strongest broader observation of Volume 2 is that a totient result may remain relevant after its first use.

A value can appear first as part of a key signature and later reappear as a distance or structural relation elsewhere in the grid.

In the current model, totients can participate in several roles:

1. transforming the center of a mirrored node;
2. defining a key signature;
3. determining Mobius phase;
4. acting as movement distances;
5. leading to hidden key locations.

This behavior is referred to here as **totient inheritance** or a **totient chain**.

This does **not** mean that every earlier totient value is always reused.

The exact activation rule is still unknown.

What is currently observable is that specific derived values recur at structurally important transitions.

---

## 19. Hidden-key comparison

### H-NG-C

This structure is an example of a non-mirrored hidden key.

Previously derived values are reused as distances in the grid:

- one value locates NG;
- another defines the vertical distance to H and C.

The resulting key:

`H-NG-C`

is non-mirrored and is therefore used directly.

### NG-B-NG

After COLD:

`H-U-H -> 4-1-4`

Those values lead to B:

`A -> D4 -> R1 -> B`

B is the center of:

`NG-B-NG`

Because this structure is mirrored:

`phi(B)=T`

Therefore:

`NG-B-NG -> NG-T-NG`

The new key is then applied back to the preserved `H-TH-H` structure and produces:

`I MAY`

---

## 20. Current rule summary

The current working model can be summarized as:

```text
mirrored 3-rune node
        |
        v
apply phi to center
        |
        v
key
        |
        +--> totient signature
        |        |
        |        +--> Mobius phase
        |        |
        |        +--> possible inherited movement values
        |
        v
decrypt ciphertext
        |
        v
next structural location
```

A second mechanism can occur:

```text
earlier derived totient values
        |
        v
movement through 27x27 grid
        |
        v
hidden key / hidden node
```

If the discovered structure is mirrored:

`transform center with phi`

If it is non-mirrored:

`use directly`

---

# PART IV - VALIDATION STATUS

## 21. What is strongly supported

The following parts are currently the strongest elements of Volume 2:

- `H-U-H -> 4-1-4` is inherited from the COLD stage.
- `D4 -> R1` reaches B at the center of `NG-B-NG`.
- `NG-B-NG -> NG-T-NG` follows the same center-totient rule used elsewhere.
- `EA-A-EA` and `NG-T-NG` share the exact signature `12-8-12`.
- Mobius fixes `NG-T-NG` to phase 0 before plaintext inspection.
- `TH-G-T-E` decrypts exactly to `I MAY`.
- The final E of I MAY immediately opens `E-X-E`.
- `E-X-E -> E-G-E` follows the same mirrored-center rule.
- Mobius fixes `E-G-E` to phase 1 before plaintext inspection.
- `U6` lands exactly on J, another mirrored center.
- `J-OE-S` decrypts exactly to `CRY`.

---

## 22. What remains unresolved

The arithmetic and geometry above are reproducible, but the complete state machine is not yet fully formalized.

Open questions include:

- What exact condition activates hidden-key search?
- Why are particular inherited totient values used at a given transition?
- What fully deterministic rule selects movement direction?
- How is parent-state return represented formally?
- Can the same rules predict the continuation after CRY without adding a new rule?

These questions are important because a true solution should predict the next stage before the plaintext is known.

---

## 23. Current strongest plaintext

After repeated testing and attempts to break the structure, the strongest continuation found so far remains:

> **AS I GO, THE WEATHER TURNS COLD.**  
> **I MAY CRY...**

`I MAY` is currently the strongest post-COLD result.

`CRY` is the strongest continuation found after `I MAY`.

Later candidate branches remain experimental and are not included as fixed plaintext in this volume.

---

# 24. Research conclusion

Volume 2 suggests that Euler totients are doing more than transforming individual rune nodes.

They appear to connect:

- mirror symmetry,
- key generation,
- numerical signatures,
- Mobius phases,
- grid movement,
- hidden-key locations,
- and structural inheritance between stages.

The system appears strongly centered on mirrored geometry: when a mirrored structure is encountered, the center repeatedly becomes the point where the totient transformation acts.

The most important new result of this volume is therefore not only the plaintext candidate **I MAY CRY**, but the possibility that **totient values form a persistent control layer governing both cryptographic and spatial behavior in the 27x27 grid**.

---

## 25. Minimal machine-readable chain

```text
VOLUME_1_END:
plaintext = "AS I GO, THE WEATHER TURNS COLD"
endpoint = A(11,7)
parent_node = H-TH-H
cold_key = H-U-H
cold_signature = 4-1-4

POST_COLD:
A(11,7)
D4 -> S(15,7)
R1 -> B(15,8)

NODE:
NG(13,8)-B(15,8)-NG(17,8)

COMPILE:
phi(B=17)=16=T
NG-B-NG -> NG-T-NG

SIGNATURE:
NG-T-NG -> 12-8-12

CROSS_CHECK:
EA-A-EA -> 12-8-12

PHASE:
mu(12)+mu(8)+mu(12)=0
phase=0

CIPHERTEXT:
TH-G-T-E

KEY:
NG-T-NG-NG

PLAINTEXT:
I-M-A-Y

NEXT_NODE:
E-X-E

COMPILE:
phi(X=14)=6=G
E-X-E -> E-G-E

SIGNATURE:
E-G-E -> 6-2-6

PHASE:
mu(6)+mu(2)+mu(6)=1
phase=1
active_key=G-E-E

MOVE:
X(25,16)
U6 -> J(19,16)

CIPHERTEXT:
J-OE-S

PLAINTEXT:
C-R-Y

CURRENT_RESULT:
"AS I GO, THE WEATHER TURNS COLD. I MAY CRY..."
```
