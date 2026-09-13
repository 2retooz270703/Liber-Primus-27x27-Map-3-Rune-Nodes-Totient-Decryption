# Cicada 3301 Liber Primus 0–2
## 27×27 Rune Matrix Decryption — Volume 3

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.  
**Date:** 08.09.2026

> **Strongest plaintext candidate**
>
> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

This document is the technical Markdown edition of Volume 3.

It continues directly from the `CRY` endpoint established in Volume 2 and records the proposed geometric continuation to `NOW THE`. The goal is to keep the route explicit, searchable, reproducible, and easy to inspect by humans, scripts, and AI systems.

The central new idea of Volume 3 is that **mirror geometry may determine direction**, while a previously derived totient value can reappear as an exact geometric radius.

---

## Quick reference

| Item | Volume 3 result |
|---|---|
| Subject | Cicada 3301 — Liber Primus pages 0–2 |
| Spatial representation | 27×27 rune matrix |
| Previous plaintext | `AS I GO, THE WEATHER TURNS COLD. I MAY CRY` |
| Entry endpoint | `S(17,16)` |
| Main inherited value | `6` |
| Main new geometric rule | outer rune of a mirror → move toward its center |
| Radius structure | `S —6— IA/O —6— S` |
| Companion structure | `TH —6— IA/O —6— TH` |
| Transition | `S(17,16) → U6 → TH(11,16)` |
| Key-generating node | `OE-J-OE` |
| Compiled key | `OE-I-OE` |
| Möbius phase | `2` |
| Active cyclic key | `OE-OE-I` |
| Ciphertext | `TH-AE-B-A-J` |
| New plaintext | `NOW THE` |
| Current result | `AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...` |
| Status | proposed, ongoing, not officially verified |

---

# PART I — THE GEOMETRIC RULE

## 1. Purpose of Volume 3

Volume 2 ends with:

> **CRY**

at the ciphertext endpoint:

```text
S(17,16)
```

Volume 2 also leaves an important unresolved question:

> How is movement direction selected without choosing a direction after seeing the plaintext?

Volume 3 tests a simple answer:

**the mirror itself may encode direction.**

The proposed rule is:

```text
outer rune of mirror
        ↓
move toward center
```

If the route instead lands exactly on the center, the mirror is symmetric in both directions and cannot select one side by geometry alone. In the current model, this is where a related-structure or hidden-key search can become relevant.

The second major proposal is that a value already produced by a previous stage can reappear as an **exact radius in the grid**.

For the continuation after `CRY`, that value is:

```text
6
```

---

## 2. Notation and conventions

### 2.1 Coordinates

Coordinates are written as:

```text
(row, column)
```

and use the 1-based 27×27 matrix convention used in Volumes 1 and 2.

Example:

```text
S(17,16)
```

means row 17, column 16.

### 2.2 Rune transliteration tokens

Names such as:

```text
AE
OE
TH
NG
IA/O
```

represent single rune transliteration tokens in the working notation.

They must not be counted as multiple Latin letters when counting rune positions.

### 2.3 Movement notation

Examples:

```text
U6 = move UP 6 cells
D4 = move DOWN 4 cells
R1 = move RIGHT 1 cell
```

### 2.4 Radius notation

A structure such as:

```text
A —6— B —6— A
```

means that each outer rune lies exactly six grid steps from the center along the axis of that mirrored structure.

### 2.5 Double totient

Volume 3 uses:

```text
φ²(n)
```

to mean:

```text
φ(φ(n))
```

For example:

```text
IA/O = 27
φ(27) = 18
φ(18) = 6

φ²(IA/O) = 6
```

---

## 3. Proposed mirror-direction rule

### 3.1 Horizontal mirror

For:

```text
A — B — A
```

the proposed direction rule is:

```text
left outer A  → move right toward B
right outer A → move left toward B
```

The destination is the center.

### 3.2 Vertical mirror

For:

```text
A
│
B
│
A
```

the rule is:

```text
top outer A    → move down toward B
bottom outer A → move up toward B
```

Again, the destination is the center.

### 3.3 General interpretation

The broader rule is not limited to the literal letters `A-B-A`.

It applies to a mirrored structure:

```text
x — y — x
```

when the route reaches one of the two outer runes.

The proposed instruction is:

> follow the mirror axis toward its center.

This reduces the directional ambiguity that remained open at the end of Volume 2.

---

## 4. What happens when the route reaches a center

If the route reaches the center rune rather than an outer rune, both mirror directions are geometrically equal.

Volume 3 therefore proposes a different behavior:

```text
land on outer rune
        ↓
follow mirror toward center

land on center
        ↓
related / hidden-key search may activate
```

The source notes a more specific geometric pattern during hidden-key search:

1. movement reaches the **center** of the hidden key;
2. the key itself lies on the **perpendicular axis**;
3. the route turns approximately 90° to identify the two outer runes.

This proposal is consistent with the hidden-key behavior already described in Volume 2, but it is not yet a fully formalized universal state rule.

---

## 5. Totient signatures as structural fingerprints

Volume 3 retains the signature concept from Volume 2.

For a three-rune structure:

```text
K = (k1, k2, k3)
```

the totient signature is:

```text
signature(K) = (φ(k1), φ(k2), φ(k3))
```

Different rune structures can therefore belong to the same numerical family.

### 5.1 The 12-8-12 family

```text
EA-A-EA → 12-8-12
NG-T-NG → 12-8-12
```

This link is used in the `COLD → I MAY` transition.

### 5.2 The 4-12-4 family

```text
I-NG-I → 4-12-4
H-NG-C → 4-12-4
```

This is another example of a mirrored structure and a hidden key sharing the same numerical fingerprint.

Volume 3 treats these matches as support for the idea that a signature can identify a **related structure**, not only serve as an intermediate arithmetic result.

---

## 6. Supporting observation: 77 mirrored structures

Volume 3 notes that the 27×27 matrix contains exactly:

```text
77
```

mirrored structures of the general form:

```text
A-B-A
```

This is recorded as a **supporting observation only**.

It is not required to derive `NOW THE`, and Volume 3 does not use `77` as a movement value, key, or phase input.

The source also discusses possible symbolic interpretations of repeated numbers. Those interpretations are kept separate from the core geometric and arithmetic route.

---

# PART II — THE STATE AFTER CRY

## 7. Frozen state at the end of Volume 2

The transition into Volume 3 begins from the exact final state of `CRY`.

Volume 2 reaches the mirrored node:

```text
E-X-E
```

and transforms its center:

```text
X = 14
φ(14) = 6 = G
```

Therefore:

```text
E-X-E → E-G-E
```

The totient signature is:

```text
φ(E=18) = 6
φ(G=6)  = 2
φ(E=18) = 6
```

so:

```text
E-G-E → 6-2-6
```

The Möbius phase is:

```text
μ(6) + μ(2) + μ(6)
= +1 - 1 + 1
= 1 mod 3
```

so the active key is:

```text
G-E-E
```

The outer value:

```text
6
```

is then reused as movement:

```text
X(25,16) → U6 → J(19,16)
```

Reading upward gives:

```text
J-OE-S
```

and:

```text
J-OE-S - G-E-E = C-R-Y
```

Therefore:

> **CRY**

The final ciphertext rune is:

```text
S(17,16)
```

This is the entry point for Volume 3.

---

## 8. Why the value 6 is already active

The value `6` is not introduced after `CRY`.

It has already appeared in the immediately preceding structure:

```text
E-G-E → 6-2-6
```

and has already been used as movement:

```text
X(25,16) → U6 → J(19,16)
```

So the post-CRY state contains both:

```text
endpoint = S(17,16)
active inherited value = 6
```

The next question is therefore:

> Does the new endpoint itself contain geometry that confirms the same value?

Volume 3 answers yes.

---

# PART III — THE RADIUS-6 GEOMETRY

## 9. Radius-6 mirror at S(17,16)

The endpoint:

```text
S(17,16)
```

is one outer rune of an exact mirrored structure:

```text
S(17,4) —6— IA/O(17,10) —6— S(17,16)
```

This gives:

```text
radius = 6
```

So the same `6` already present in the preceding totient chain now reappears as a literal geometric radius.

This is important because the movement value is not being introduced independently at the new endpoint.

The endpoint itself belongs to a structure with exactly that radius.

---

## 10. The center independently encodes the same 6

The center of the radius-6 mirror is:

```text
IA/O(17,10)
```

Its working Gematria Primus value is:

```text
IA/O = 27
```

Apply Euler's totient twice:

```text
φ(27) = 18
φ(18) = 6
```

Therefore:

```text
φ²(IA/O) = 6
```

The same number is now present in three distinct roles:

```text
previous totient signature → 6
previous movement          → 6
current mirror radius      → 6
```

and the center of the current mirror independently reduces to:

```text
φ²(center) = 6
```

This is the main numerical-geometric cross-check of Volume 3.

---

## 11. Companion radius-6 mirror

The same center:

```text
IA/O(17,10)
```

also belongs to another exact mirror with the same radius:

```text
TH(11,16) —6— IA/O(17,10) —6— TH(23,4)
```

So two different mirrors share exactly the same center and radius:

```text
S(17,4)   —6— IA/O(17,10) —6— S(17,16)
TH(11,16) —6— IA/O(17,10) —6— TH(23,4)
```

This creates a relationship between the current `S` mirror and a companion `TH` mirror.

The shared center identifies the related structure.

---

## 12. Selecting the next endpoint

The current position is:

```text
S(17,16)
```

The inherited value is:

```text
6
```

The companion mirror has two outer endpoints:

```text
TH(11,16)
TH(23,4)
```

Volume 3 observes that only one of these companion endpoints is reachable from the current `S(17,16)` by a single straight movement of exactly six cells:

```text
S(17,16) → UP 6 → TH(11,16)
```

So the proposed transition is:

```text
S(17,16)
    |
    | U6
    v
TH(11,16)
```

This is the point from which the next ciphertext is read.

---

# PART IV — CRY → NOW THE

## 13. Ciphertext beginning at TH(11,16)

From:

```text
TH(11,16)
```

Volume 3 reads diagonally down-right:

```text
TH(11,16)
→ AE(12,17)
→ B(13,18)
→ A(14,19)
→ J(15,20)
```

Ciphertext:

```text
TH-AE-B-A-J
```

The source describes this read as following the axis of an `A-TH-A` mirror.

The important point for the technical chain is the exact five-rune sequence and its coordinates.

---

## 14. The key already exists: OE-J-OE

The key-generating structure immediately preceding this continuation is:

```text
OE-J-OE
```

Its center is:

```text
J = 11
```

Apply Euler's totient:

```text
φ(11) = 10
```

and Gematria Primus value `10` is:

```text
I
```

Therefore the mirrored node compiles as:

```text
OE-J-OE → OE-I-OE
```

The generated three-rune key is:

```text
OE-I-OE
```

This uses the same center-transformation rule already established in the earlier Volumes:

```text
a-b-a → a-φ(b)-a
```

---

## 15. Totient signature of OE-I-OE

For:

```text
OE-I-OE
```

the totient values are:

```text
φ(OE=22) = 10
φ(I=10)  = 4
φ(OE=22) = 10
```

Therefore:

```text
OE-I-OE → 10-4-10
```

This signature is then used for the Möbius phase calculation.

---

## 16. Möbius phase of OE-I-OE

The phase rule remains:

```text
p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3
```

For:

```text
10-4-10
```

the Möbius values are:

```text
μ(10) = +1
μ(4)  = 0
μ(10) = +1
```

Therefore:

```text
p = (1 + 0 + 1) mod 3
p = 2
```

So the key is rotated to phase 2:

```text
OE-I-OE → OE-OE-I
```

Active cyclic key:

```text
OE-OE-I
```

Repeated across the five ciphertext runes:

```text
OE-OE-I-OE-OE
```

The phase is fixed numerically **before** evaluating the plaintext.

---

## 17. Decrypting NOW THE

The decryption rule is the same as in Volumes 1 and 2:

```text
P = C - K mod 29
```

Using zero-based Gematria Primus values:

| # | Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|---|
| 1 | `TH(2)` | `OE(22)` | `2 - 22 mod 29 = 9` | `N` |
| 2 | `AE(25)` | `OE(22)` | `25 - 22 = 3` | `O` |
| 3 | `B(17)` | `I(10)` | `17 - 10 = 7` | `W` |
| 4 | `A(24)` | `OE(22)` | `24 - 22 = 2` | `TH` |
| 5 | `J(11)` | `OE(22)` | `11 - 22 mod 29 = 18` | `E` |

Therefore:

```text
ciphertext: TH-AE-B-A-J
key:        OE-OE-I-OE-OE
result:     N-O-W-TH-E
```

Result:

> **NOW THE**

The plaintext rune sequence is:

```text
N-O-W-TH-E
```

which corresponds to the English grouping:

```text
NOW THE
```

---

## 18. Compact NOW THE chain

```text
CRY
 |
 | endpoint
 v
S(17,16)
 |
 | inherited value = 6
 | exact local radius = 6
 v
S —6— IA/O —6— S
        |
        | φ²(IA/O)=6
        | same center
        v
TH —6— IA/O —6— TH
 |
 | S(17,16) → U6
 v
TH(11,16)
 |
 | read diagonal down-right
 v
TH-AE-B-A-J

OE-J-OE
 |
 | φ(J)=10=I
 v
OE-I-OE
 |
 | signature 10-4-10
 | Möbius phase 2
 v
OE-OE-I
 |
 | GP subtraction mod 29
 v
NOW THE
```

---

# PART V — WHAT VOLUME 3 ADDS TO THE MODEL

## 19. The value 6 across the transition

The strongest structural feature of Volume 3 is the repeated appearance of the same value without an independent reintroduction.

The value `6` appears as:

1. the outer totient value in:

   ```text
   E-G-E → 6-2-6
   ```

2. the movement used in Volume 2:

   ```text
   X(25,16) → U6 → J(19,16)
   ```

3. the exact radius of the mirror containing the final `CRY` endpoint:

   ```text
   S —6— IA/O —6— S
   ```

4. the double-totient value of that mirror's center:

   ```text
   φ²(IA/O) = 6
   ```

5. the exact radius of a second mirror with the same center:

   ```text
   TH —6— IA/O —6— TH
   ```

6. the straight movement from the current endpoint to the relevant companion endpoint:

   ```text
   S(17,16) → U6 → TH(11,16)
   ```

This is the central arithmetic-geometric chain of Volume 3.

---

## 20. Geometry as a control layer

Volumes 1 and 2 already suggest that totient values can control:

- key generation;
- key signatures;
- Möbius phase;
- movement;
- hidden-key discovery.

Volume 3 adds a stronger geometric role.

A value may also describe the **shape of the map itself**.

The current proposal is therefore:

```text
number derived cryptographically
        ↓
same number appears geometrically
        ↓
geometry constrains the next movement
        ↓
next key / ciphertext becomes available
```

This is a stronger claim than simply noticing a matching number after the fact.

For the rule to remain useful, the same kind of constraint should continue to predict unseen transitions.

---

## 21. Sequential model

The current working model can be summarized as:

```text
current endpoint / structure
          |
          v
inherited totient information
          |
          v
local mirror geometry
          |
          v
direction / related structure
          |
          v
key-generating node
          |
          v
Euler φ transformation
          |
          v
totient signature
          |
          v
Möbius phase
          |
          v
active cyclic key
          |
          v
ciphertext read
          |
          v
GP subtraction mod 29
          |
          v
plaintext
          |
          v
new endpoint
          ↺
```

A second branch remains possible when the route reaches a center:

```text
movement
   |
   v
center of structure
   |
   v
mirror cannot choose side
   |
   v
signature / related-structure search
   |
   v
hidden-key center
   |
   v
perpendicular axis
   |
   v
hidden key
```

This branch remains less formalized than the direct outer-rune rule.

---

## 22. The recurring center behavior

Volume 3 emphasizes a recurring property of the route:

> important transitions repeatedly lead into the center of another mirrored structure.

Examples across the project include:

- landing at the central `NG` of the 27×27 matrix;
- reaching the center `B` of `NG-B-NG`;
- moving to the center `J` of `OE-J-OE`;
- using the shared center `IA/O` to identify paired radius-6 mirrors.

After `NOW THE`, the source also notes another mirror:

```text
A-TH-A
```

as part of the continuing structure.

The exact continuation after `THE` is not fixed in this volume.

---

## 23. Boundary observation: AS I GO THE / NOW THE

Volume 3 notes a repeated textual behavior:

```text
AS I GO THE
```

and later:

```text
NOW THE
```

In both cases, the decryption route appears to generate `THE` together with the preceding block even though normal English punctuation may place a semantic boundary before it.

This is an **interpretive observation**, not a required cryptographic rule.

The current human-readable grouping is therefore written as:

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

The punctuation is editorial grouping of the recovered rune plaintext, not an additional encrypted operation.

---

# PART VI — MAP NOTATION FROM VOLUME 3 ONWARD

## 24. Color legend

Volume 3 defines the map colors used for the continuing research:

- **Purple** — ciphertext that decrypts into proposed plaintext.
- **Blue** — hidden-key points used for geometry or clue structure.
- **Green** — selected geometric confirmation points or transition clues.
- **Thin purple outline** — mirrors directly involved in forming or confirming plaintext, including possible return structures.

The source explicitly states that green should be used selectively rather than marking every geometric relation.

---

# PART VII — VALIDATION STATUS

## 25. What is strongest in Volume 3

The strongest directly checkable elements of the Volume 3 continuation are:

- Volume 2 ends `CRY` at `S(17,16)`.
- The immediately preceding transformed node is `E-G-E → 6-2-6`.
- The value `6` was already used as a movement value before the `CRY` endpoint.
- `S(17,16)` lies on the exact radius-6 mirror:

  ```text
  S(17,4) —6— IA/O(17,10) —6— S(17,16)
  ```

- The center gives:

  ```text
  IA/O = 27
  φ(27) = 18
  φ(18) = 6
  ```

- The same center belongs to a second radius-6 mirror:

  ```text
  TH(11,16) —6— IA/O(17,10) —6— TH(23,4)
  ```

- The recorded transition is:

  ```text
  S(17,16) → U6 → TH(11,16)
  ```

- From `TH(11,16)`, the exact ciphertext is:

  ```text
  TH-AE-B-A-J
  ```

- The key is generated by the already established mirrored-center rule:

  ```text
  OE-J-OE → OE-I-OE
  ```

- Möbius fixes phase 2 before plaintext inspection:

  ```text
  OE-I-OE → OE-OE-I
  ```

- Standard mod-29 subtraction gives exactly:

  ```text
  NOW THE
  ```

These are the core reproducible claims of Volume 3.

---

## 26. What remains unresolved

Volume 3 reduces the earlier direction ambiguity, but the full algorithm is still not complete.

Open questions include:

1. Is the rule:

   ```text
   outer rune → toward center
   ```

   universal for all active mirror structures?

2. What exact condition activates hidden-key search when a route reaches a center?

3. When a hidden-key search begins, what formally selects the related structure if more than one signature match exists?

4. When an inherited number reappears, what determines whether it should be read as:
   - movement distance,
   - key signature,
   - mirror radius,
   - or another structural relation?

5. Can the next continuation after:

   ```text
   NOW THE
   ```

   be predicted from the current state without adding a new rule after seeing candidate plaintext?

6. How should the newly observed `A-TH-A` structure participate in the next transition?

A true deterministic solution should answer these questions using information available **before** the next plaintext is inspected.

---

## 27. Verification-script status

The repository currently contains dedicated verification scripts for Volumes 1 and 2.

Volume 3 does not yet have a dedicated verifier.

This Markdown edition therefore keeps the key coordinates, transforms, phase arithmetic, and mod-29 subtraction explicit so that a future `verify_volume_3.py` can test the same claims directly.

---

## 28. Current strongest plaintext

The current connected plaintext candidate is:

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

The new Volume 3 contribution is:

> **NOW THE**

This continuation is strongest when treated as part of the same sequential route rather than as an isolated crib.

---

# 29. Research conclusion

Volume 3 adds a geometric layer to the model developed in Volumes 1 and 2.

The key new proposal is not only that mirror structures are symmetric, but that their symmetry can carry **directional information**:

```text
outer rune → toward center
```

At the `CRY` endpoint, the inherited value `6` is unusually constrained:

```text
E-G-E signature
      ↓
      6
      ↓
previous movement
      ↓
radius of S mirror
      ↓
φ² of IA/O center
      ↓
radius of TH mirror
      ↓
U6 transition
      ↓
TH(11,16)
```

The subsequent key is generated by an already established rule, its phase is fixed numerically, and the five-rune ciphertext decrypts to:

> **NOW THE**

The broader working hypothesis is therefore that **totient arithmetic and mirror geometry are not separate observations but interacting layers of the same transition system**.

The next major test is predictive:

> Can the state after `NOW THE` determine the next movement, structure, key, and plaintext before the continuation is known?

---

## 30. Minimal machine-readable chain

```text
VOLUME_2_END:
plaintext = "AS I GO, THE WEATHER TURNS COLD. I MAY CRY"
cry_ciphertext = J-OE-S
cry_key = G-E-E
cry_endpoint = S(17,16)

PREVIOUS_NODE:
E-X-E

COMPILE:
phi(X=14)=6=G
E-X-E -> E-G-E

SIGNATURE:
E-G-E -> 6-2-6
inherited_value = 6

CRY_ENDPOINT_MIRROR:
S(17,4)
IA/O(17,10)
S(17,16)
radius = 6

CENTER_CHECK:
IA/O = 27
phi(27) = 18
phi(18) = 6
phi2(IA/O) = 6

COMPANION_MIRROR:
TH(11,16)
IA/O(17,10)
TH(23,4)
radius = 6

MOVE:
S(17,16)
U6 -> TH(11,16)

CIPHERTEXT_COORDINATES:
TH(11,16)
AE(12,17)
B(13,18)
A(14,19)
J(15,20)

CIPHERTEXT:
TH-AE-B-A-J

KEY_NODE:
OE-J-OE

KEY_COMPILE:
J=11
phi(11)=10=I
OE-J-OE -> OE-I-OE

KEY_SIGNATURE:
OE-I-OE -> 10-4-10

PHASE:
mu(10)+mu(4)+mu(10)
= 1+0+1
= 2 mod 3
phase = 2

ACTIVE_KEY:
OE-OE-I
repeated = OE-OE-I-OE-OE

DECRYPT:
TH(2)-OE(22) mod 29 = 9=N
AE(25)-OE(22) = 3=O
B(17)-I(10) = 7=W
A(24)-OE(22) = 2=TH
J(11)-OE(22) mod 29 = 18=E

PLAINTEXT:
N-O-W-TH-E
"NOW THE"

CURRENT_RESULT:
"AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ..."
```

---

> **Research status:** proposed, reproducible in the documented arithmetic and coordinates, and still under active analysis.  
> This document does not claim an officially verified Cicada 3301 solution.
