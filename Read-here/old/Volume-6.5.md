# Cicada 3301 Liber Primus 0-2
## 27x27 Rune Matrix Decryption - Volume 6.5

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.  
**Date:** 16.09.2026

> **Current plaintext candidate**
>
> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH.**

This document is the technical Markdown edition of the **Full Möbius State / Signed Transition-Type Hypothesis** developed after Volumes 1-6.

Volume 6.5 does **not** introduce a new plaintext segment. Its purpose is to preserve information that is currently discarded by the phase calculation and test whether that information can explain the **type of structural transition** used by the route.

The central observation is:

```text
the Möbius vector may carry more information than the phase alone
```

For the symmetric 3-rune key structures used repeatedly in the route, the Möbius state has the form:

```text
M = (a,b,a)
```

where:

```text
a = Möbius value of the two outer positions
b = Möbius value of the center position
```

The existing phase rule reduces this full state to one number:

```text
p = (a+b+a) mod 3
```

but because:

```text
2a == -a  (mod 3)
```

the phase can also be written as:

```text
p = (b-a) mod 3
```

This suggests a possible separation of functions:

```text
FULL MÖBIUS STATE (a,b,a)
        |
        +--> phase p = (b-a) mod 3
        |      -> cyclic key rotation
        |
        +--> support/sign pattern
               -> possible structural transition type
```

The strongest currently observed distinction is:

```text
(0,+1,0) -> CENTER-like behavior
(+1,0,+1) -> OUTER-like behavior
```

A second, more global observation changes the interpretation of the entire state space.

For symmetric states there are exactly nine theoretical possibilities:

```text
M = (a,b,a),    a,b in {-1,0,+1}
```

but, except for `000`, they occur naturally in global sign-inverted pairs:

```text
(0,+1,0)     <-> (0,-1,0)
(+1,0,+1)    <-> (-1,0,-1)
(+1,-1,+1)   <-> (-1,+1,-1)
(+1,+1,+1)   <-> (-1,-1,-1)

(0,0,0)      <-> itself
```

The states already used by the recovered route occupy only one canonical side of these pairs:

```text
000
010
101
1,-1,1
111
```

while their four exact negative partners have not yet been required by the current first `1+3+9 = 13`-stage presentation.

This suggests a more compact possibility:

```text
9 raw symmetric states
=
4 signed transition classes
+
1 neutral state
```

The **equivalence class `{M,-M}`** may encode the structural operation, while the **global sign** may encode polarity / traversal orientation.

This is a working hypothesis, not yet a universal law.

---

## Quick reference

| Item | Volume 6.5 result |
|---|---|
| Subject | Full Möbius state, signed state symmetry, and a possible transition-type selector |
| New plaintext | None |
| Existing phase rule | `p = [mu(phi(k1)) + mu(phi(k2)) + mu(phi(k3))] mod 3` |
| Symmetric state | `M = (a,b,a)` |
| Equivalent phase form | `p = (b-a) mod 3` |
| Strongest repeated state | `(0,+1,0)` |
| Repeated behavior | endpoint becomes the center of the next mirror |
| Complementary state | `(+1,0,+1)` |
| Observed behavior | endpoint becomes an outer node of the next mirror in two clean cases |
| Other observed states | `(0,0,0)`, `(+1,-1,+1)`, `(+1,+1,+1)` |
| Main hypothesis | full Möbius state may encode transition topology while `p` encodes key rotation |
| Complete symmetric state space | `9 = 4 signed pairs + 000` |
| Global sign symmetry | every non-zero state has an exact partner `M <-> -M` |
| Current route polarity | the observed first `1+3+9 = 13`-stage presentation uses only the canonical positive representatives |
| Exact sign effect on phase | `M -> -M` implies `p -> -p mod 3`, therefore `1 <-> 2` and `0 -> 0` |
| Refined state model | transition class = `{M,-M}`; polarity = global sign; `000` = neutral |
| Relation to Volume 6 | key-state pattern may select **what structural role to use**; coordinate selector may help select **which directional branch** |
| Status | promising state-machine hypothesis; requires blind route-wide testing |

---

# PART I - SCOPE AND EVIDENCE LEVELS

## 1. What Volume 6.5 is trying to solve

Volumes 1-6 already establish or investigate several recurring layers:

- the 27x27 rune matrix;
- mirrored or structured 3-rune nodes;
- Euler-totient center transformation;
- 3-rune key generation;
- Möbius phase selection;
- Gematria Primus subtraction modulo 29;
- inherited totient values;
- mirror radii and shared nodes;
- local geometric handoffs;
- the phase-coordinate selector of Volume 6.

The unresolved problem is not only:

```text
Which direction should the route move?
```

There is an earlier structural question:

```text
What kind of transition should happen next?
```

Examples include:

```text
Should the endpoint be treated as a CENTER?
Should it be treated as an OUTER node?
Should an inherited state be reused?
Should a symmetric role swap be allowed?
Should the outer numerical value propagate?
```

Volume 6 tests a possible directional selector.

Volume 6.5 asks whether the **full Möbius state of the active key** may provide the missing **transition-type selector**.

---

## 2. Evidence labels

As in Volume 6, three evidence levels are used.

### [R] Recorded route fact

A key, signature, phase, coordinate, mirror, endpoint role, movement, or plaintext already documented in Volumes 1-6.

### [D] Derived result

A result obtained directly from the recorded values by applying the stated arithmetic.

Example:

```text
signature = 4-1-4
M = (mu(4),mu(1),mu(4))
  = (0,+1,0)

p = 0+1+0
  = 1 mod 3
```

### [H] Working hypothesis

An interpretation suggested by repeated behavior but not yet proven universal.

Examples:

```text
(0,+1,0) means CENTER-active
(+1,0,+1) means OUTER-active
(+1,-1,+1) means REFLECT / outer propagation
(+1,+1,+1) permits role equivalence or SWAP
(0,0,0) means no local Möbius selector / INHERIT
the pair {M,-M} may represent one transition class with opposite polarity
the currently unused negative states may be reverse-orientation partners rather than new opcodes
```

The distinction between [R], [D], and [H] is essential.

---

# PART II - THE FULL MÖBIUS STATE

## 3. Existing phase rule

For an active 3-rune key:

```text
K = (k1,k2,k3)
```

define its totient signature:

```text
S(K) = (phi(k1),phi(k2),phi(k3))
```

and its Möbius state:

```text
M(K) = (
  mu(phi(k1)),
  mu(phi(k2)),
  mu(phi(k3))
)
```

The existing phase rule is:

```text
p = sum(M(K)) mod 3
```

or explicitly:

```text
p = [mu(phi(k1)) + mu(phi(k2)) + mu(phi(k3))] mod 3
```

The value `p` determines the cyclic key rotation.

---

## 4. Symmetric keys reduce to M = (a,b,a)

The key structures repeatedly used by the route are symmetric:

```text
outer - center - outer
```

After compilation, their totient signatures also have the symmetric form:

```text
x-y-x
```

Therefore their Möbius vectors have the form:

```text
M = (a,b,a)
```

The phase becomes:

```text
p = (a+b+a) mod 3
  = (2a+b) mod 3
```

Since:

```text
2a == -a (mod 3)
```

we obtain:

```text
p = (b-a) mod 3
```

So for symmetric states:

> **The phase is the center Möbius value relative to the outer Möbius value.**

This is algebraically equivalent to the existing phase formula. No new phase rule is introduced.

---

## 5. Why the full vector matters

Reducing:

```text
M = (a,b,a)
```

to:

```text
p = (b-a) mod 3
```

is many-to-one.

Different full states can produce the same phase.

For example:

```text
(0,+1,0)   -> p=1
(+1,-1,+1) -> p=1
(-1,0,-1)  -> p=1
```

Similarly:

```text
(+1,0,+1)  -> p=2
(0,-1,0)   -> p=2
(-1,+1,-1) -> p=2
```

and:

```text
(0,0,0)      -> p=0
(+1,+1,+1)   -> p=0
(-1,-1,-1)   -> p=0
```

Therefore:

```text
phase p
```

cannot reconstruct the full Möbius state.

If the different full states behave differently in the route, then the phase rule is only one projection of a larger state.

---

## 6. Two possible outputs from one calculation

A useful working factorization is:

```text
M(K) = full Möbius state
```

with two separate derived quantities:

```text
P(M) = (b-a) mod 3
```

and:

```text
T(M) = pattern/sign/support of (a,b,a)
```

Possible interpretation:

```text
P(M) -> cyclic key phase
T(M) -> structural transition type
```

This is the central hypothesis of Volume 6.5.

---

# PART III - THE STRONGEST REPEATED STATE: (0,+1,0)

## 7. Meaning of the pattern

The state:

```text
M = (0,+1,0)
```

has one immediately visible property:

```text
outer = 0
center = +1
outer = 0
```

Only the center is non-zero.

A natural structural reading is therefore:

```text
CENTER-active
```

The route contains three especially clear examples in which this state is followed by an endpoint that becomes the **center of the next exact mirror**.

---

## 8. Example 1 - COLD

[R] The preserved mirror:

```text
H-TH-H
```

compiles through:

```text
phi(TH=2) = 1 = U
```

to:

```text
H-U-H
```

Its totient signature is:

```text
4-1-4
```

[D] Therefore:

```text
M = (
  mu(4),
  mu(1),
  mu(4)
)

M = (0,+1,0)
```

and:

```text
p = 1
```

[R] This key family decrypts the block ending in:

```text
COLD
```

whose final ciphertext position is:

```text
A(11,7)
```

[R] That exact endpoint is the center of:

```text
EA(10,7) - A(11,7) - EA(12,7)
```

or:

```text
EA-A-EA
```

So the observed chain is:

```text
H-U-H
  |
  | signature 4-1-4
  v
M = (0,+1,0)
  |
  | phase 1
  v
COLD
  |
  v
A(11,7)
  |
  | endpoint role
  v
CENTER of EA-A-EA
```

[H] This is consistent with:

```text
(0,+1,0) -> CENTER
```

---

## 9. Example 2 - IDEA

[R] Volume 4 uses:

```text
A-U/V-A
```

with signature:

```text
8-1-8
```

[D] Its Möbius state is:

```text
mu(8) = 0
mu(1) = +1
mu(8) = 0

M = (0,+1,0)
```

and:

```text
p = 1
```

[R] Phase 1 gives:

```text
U/V-A-A
```

which decrypts:

```text
J-E-D
```

to:

```text
I-D-EA
```

or:

> **IDEA**

[R] IDEA ends at:

```text
D(17,18)
```

and that exact cell is the center of:

```text
J(15,20) - D(17,18) - J(19,16)
```

or:

```text
J-D-J
```

Therefore:

```text
A-U/V-A
  |
  | signature 8-1-8
  v
M = (0,+1,0)
  |
  | phase 1
  v
IDEA
  |
  v
D(17,18)
  |
  v
CENTER of J-D-J
```

Again:

```text
(0,+1,0) -> CENTER
```

---

## 10. Example 3 - IS

[R] After END, Volume 5 returns to the `4-1-4` family through:

```text
H-R-H -> H-TH-H
```

with:

```text
signature = 4-1-4
```

[D] Therefore:

```text
M = (0,+1,0)
p = 1
```

and the active key ordering is:

```text
TH-H-H
```

[R] The first two key runes decrypt:

```text
EO-D
```

to:

```text
I-S
```

or:

> **IS**

[R] IS ends at:

```text
D(21,10)
```

and this exact cell is the center of:

```text
E(19,12) - D(21,10) - E(23,8)
```

or:

```text
E-D-E
```

Therefore:

```text
H-TH-H
  |
  | signature 4-1-4
  v
M = (0,+1,0)
  |
  | phase 1
  v
IS
  |
  v
D(21,10)
  |
  v
CENTER of E-D-E
```

Again:

```text
(0,+1,0) -> CENTER
```

---

## 11. Three-case summary

The currently documented clean cases are:

| Active structure | Signature | Möbius state | Plaintext block | Endpoint | Next structural role |
|---|---|---|---|---|---|
| `H-U-H` | `4-1-4` | `(0,+1,0)` | `COLD` | `A(11,7)` | center of `EA-A-EA` |
| `A-U/V-A` | `8-1-8` | `(0,+1,0)` | `IDEA` | `D(17,18)` | center of `J-D-J` |
| `H-TH-H` | `4-1-4` | `(0,+1,0)` | `IS` | `D(21,10)` | center of `E-D-E` |

The repeated observation is:

```text
3 tested clean occurrences of (0,+1,0)
-> 3 endpoints that become mirror centers
```

[H] The strongest current state interpretation is therefore:

```text
(0,+1,0) = CENTER-active
```

This is the strongest new observation in Volume 6.5.

---

# PART IV - THE COMPLEMENTARY STATE: (+1,0,+1)

## 12. Meaning of the complementary pattern

Now consider:

```text
M = (+1,0,+1)
```

Its support is the complement of `010`:

```text
outer = +1
center = 0
outer = +1
```

The two outer positions are non-zero while the center is zero.

A natural structural reading is:

```text
OUTER-active
```

Its phase is:

```text
p = 0-(+1)
  = -1
  = 2 mod 3
```

So the two complementary states give:

```text
(0,+1,0) -> p=1
(+1,0,+1) -> p=2
```

This creates a simple center/outer duality.

---

## 13. Example 1 - NOW THE

[R] Volume 3 compiles:

```text
OE-J-OE -> OE-I-OE
```

with signature:

```text
10-4-10
```

[D] The Möbius state is:

```text
mu(10) = +1
mu(4)  = 0
mu(10) = +1

M = (+1,0,+1)
```

and:

```text
p = 2
```

[R] Phase 2 gives:

```text
OE-OE-I
```

and the repeated key decrypts:

```text
TH-AE-B-A-J
```

to:

```text
N-O-W-TH-E
```

or:

> **NOW THE**

[R] The ciphertext endpoint is:

```text
J(15,20)
```

Volume 4 then records that this same J becomes one **outer node** of:

```text
J(15,20) - D(17,18) - J(19,16)
```

or:

```text
J-D-J
```

So:

```text
OE-I-OE
  |
  | signature 10-4-10
  v
M = (+1,0,+1)
  |
  | phase 2
  v
NOW THE
  |
  v
J(15,20)
  |
  v
OUTER of J-D-J
```

[H] This is consistent with:

```text
(+1,0,+1) -> OUTER
```

---

## 14. Example 2 - END

[R] Volume 4 uses:

```text
J-T-J
```

with signature:

```text
10-8-10
```

[D] Therefore:

```text
mu(10) = +1
mu(8)  = 0
mu(10) = +1

M = (+1,0,+1)
```

and:

```text
p = 2
```

Phase 2 gives:

```text
J-J-T
```

which decrypts:

```text
F-L-I
```

to:

```text
E-N-D
```

or:

> **END**

[R] END finishes at:

```text
I(21,23)
```

Volume 4 / Volume 5 record that this cell is the right outer node of:

```text
I(21,21) - R(21,22) - I(21,23)
```

or:

```text
I-R-I
```

Therefore:

```text
J-T-J
  |
  | signature 10-8-10
  v
M = (+1,0,+1)
  |
  | phase 2
  v
END
  |
  v
I(21,23)
  |
  v
OUTER of I-R-I
```

Again:

```text
(+1,0,+1) -> OUTER
```

---

## 15. Two-case summary

The two clearest endpoint-role examples are:

| Active structure | Signature | Möbius state | Plaintext block | Endpoint | Next structural role |
|---|---|---|---|---|---|
| `OE-I-OE` | `10-4-10` | `(+1,0,+1)` | `NOW THE` | `J(15,20)` | outer of `J-D-J` |
| `J-T-J` | `10-8-10` | `(+1,0,+1)` | `END` | `I(21,23)` | outer of `I-R-I` |

So the current clean observation is:

```text
2 tested clean occurrences of (+1,0,+1)
-> 2 endpoints that become mirror outers
```

[H] The corresponding state interpretation is:

```text
(+1,0,+1) = OUTER-active
```

The evidence set is smaller than for `010`, but the complementary behavior is notable.

---

# PART V - THE CENTER / OUTER DUALITY

## 16. Phase as a relative center/outer state

For:

```text
M = (a,b,a)
```

the phase is:

```text
p = (b-a) mod 3
```

For the two strongest states:

```text
CENTER-active:
M = (0,+1,0)
p = +1-0
p = 1
```

and:

```text
OUTER-active:
M = (+1,0,+1)
p = 0-(+1)
p = -1
p = 2 mod 3
```

So the phase values `1` and `2` are naturally opposite:

```text
p=1 -> center is one state ahead of outer
p=2 -> center is one state behind outer
```

The cyclic key rotation mirrors this relation.

For a center-active example:

```text
A-U/V-A
phase 1
-> U/V-A-A
```

The transformed center moves to the first key position.

For an outer-active example:

```text
OE-I-OE
phase 2
-> OE-OE-I
```

The transformed center moves to the last key position.

This suggests that the arithmetic and the structural role may be two views of the same center/outer relation.

---

## 17. Compact duality

The strongest current working rule can be written:

```text
010
CENTER is the only non-zero Möbius component
-> CENTER-like continuation

101
OUTERS are the non-zero Möbius components
-> OUTER-like continuation
```

or:

```text
(0,+1,0)  <-> CENTER
(+1,0,+1) <-> OUTER
```

This is more informative than storing only:

```text
p=1
p=2
```

because the full vector explicitly retains **which structural positions are active**.

---

# PART VI - OTHER OBSERVED STATES

## 18. State (+1,-1,+1)

[R] Volume 2 compiles:

```text
E-X-E -> E-G-E
```

with signature:

```text
6-2-6
```

[D] Its Möbius state is:

```text
mu(6) = +1
mu(2) = -1
mu(6) = +1

M = (+1,-1,+1)
```

and:

```text
p = (+1-1+1) mod 3
p = 1
```

[R] The notable behavior after this state is the repeated propagation of the **outer value 6**.

The documented chain includes:

```text
E-G-E signature -> 6-2-6
                  |
                  v
outer value = 6
                  |
                  v
movement by 6
                  |
                  v
radius-6 S mirror
                  |
                  v
phi^2(shared center) = 6
                  |
                  v
radius-6 TH mirror
                  |
                  v
U6 transition
```

The center Möbius value has the opposite sign from the outer pair:

```text
outer  = +1
center = -1
outer  = +1
```

[H] A possible interpretation is:

```text
(+1,-1,+1)
-> REFLECT / reject center / propagate OUTER state
```

This is currently supported by only one strong family, so it must remain provisional.

---

## 19. State (+1,+1,+1)

[R] Volume 4 records:

```text
J-OE-J
```

with:

```text
phi(J-OE-J) = 10-10-10
```

and:

```text
M = (+1,+1,+1)
```

Therefore:

```text
p = 0
```

The next physical mirror:

```text
OE-J-OE
```

has the same totient signature:

```text
phi(OE-J-OE) = 10-10-10
```

So:

```text
phi(J-OE-J)
=
phi(OE-J-OE)
=
10-10-10
```

The rune roles have exchanged while the arithmetic signature remains unchanged.

[H] A possible interpretation is:

```text
(+1,+1,+1)
-> role equivalence / SWAP-compatible state
```

The important observation is not that `111` proves a swap operation, but that a completely homogeneous Möbius state contains **no center-vs-outer arithmetic distinction**.

This makes role exchange structurally plausible without changing the numerical signature.

---

## 20. State (0,0,0)

[R] Volume 2 uses:

```text
NG-T-NG
```

with signature:

```text
12-8-12
```

[D]:

```text
mu(12) = 0
mu(8)  = 0
mu(12) = 0

M = (0,0,0)
```

so:

```text
p = 0
```

The phase supplies no internal distinction between outer and center.

The route at this stage relies on additional information already present in the system:

- the inherited `4-1-4` movement signal;
- the `EA-A-EA -> 12-8-12 <- NG-T-NG` signature match;
- the preserved `H-TH-H` parent structure.

[H] A conservative interpretation is therefore:

```text
(0,0,0)
-> no local Möbius role selector
-> use inherited / matched structural state
```

A short label is:

```text
000 -> INHERIT
```

This does not mean the state performs no operation. It means the full Möbius vector itself does not distinguish a center or outer role.

---


# PART VII - GLOBAL SIGN SYMMETRY OF THE NINE-STATE SPACE

## 21. The complete symmetric Möbius state space

For a symmetric mirror/key state:

```text
M = (a,b,a)
```

with:

```text
a,b in {-1,0,+1}
```

there are exactly:

```text
3 x 3 = 9
```

possible full Möbius states.

They are:

| State | Phase `p=(b-a) mod 3` |
|---|---:|
| `(-1,-1,-1)` | `0` |
| `(-1,0,-1)` | `1` |
| `(-1,+1,-1)` | `2` |
| `(0,-1,0)` | `2` |
| `(0,0,0)` | `0` |
| `(0,+1,0)` | `1` |
| `(+1,-1,+1)` | `1` |
| `(+1,0,+1)` | `2` |
| `(+1,+1,+1)` | `0` |

This table is exhaustive for all symmetric phase-admissible states whose Möbius values are defined.

A mirror containing an element for which the required totient/Möbius pipeline is undefined belongs outside this nine-state table and should be treated separately.

---

## 22. The nine states are organized as four sign pairs plus one neutral state

The nine states are not structurally unrelated.

Apply a global sign inversion:

```text
I(M) = -M
```

For:

```text
M = (a,b,a)
```

this gives:

```text
-M = (-a,-b,-a)
```

The nine-state set decomposes exactly into the following orbits:

```text
PAIR A:
(0,+1,0) <-> (0,-1,0)

PAIR B:
(+1,0,+1) <-> (-1,0,-1)

PAIR C:
(+1,-1,+1) <-> (-1,+1,-1)

PAIR D:
(+1,+1,+1) <-> (-1,-1,-1)

NEUTRAL:
(0,0,0) <-> (0,0,0)
```

Therefore the raw state space can be rewritten as:

```text
9 states
=
4 two-element sign orbits
+
1 fixed point
```

or:

```text
9
=
(4 x 2) + 1
```

This is the first reason to suspect that the four currently unused states may not represent four completely new operations.

They may be the opposite-polarity versions of already observed transition classes.

---

## 23. Canonical positive representatives

For every non-zero symmetric state, define its polarity by the sign of the **first non-zero component**:

```text
s(M) = +1  if the first non-zero component of M is +1
s(M) = -1  if the first non-zero component of M is -1
```

For:

```text
M = (0,0,0)
```

define:

```text
s(M) = 0
```

Now define a canonical representative:

```text
C(M) = s(M) * M
```

for every non-zero state.

This forces the first non-zero component of the canonical state to be positive.

The four canonical non-zero representatives are therefore:

```text
C1 = (0,+1,0)
C2 = (+1,0,+1)
C3 = (+1,-1,+1)
C4 = (+1,+1,+1)
```

and the neutral state is:

```text
C0 = (0,0,0)
```

Every possible non-zero symmetric state can now be written uniquely as:

```text
M = s * C
```

where:

```text
s in {-1,+1}
```

and:

```text
C in {
  (0,+1,0),
  (+1,0,+1),
  (+1,-1,+1),
  (+1,+1,+1)
}
```

This gives a compact factorization:

```text
FULL STATE
=
STRUCTURAL CLASS
x
POLARITY
```

with `000` as the neutral fixed state.

### Important precision

The structural class should **not** be defined by element-wise absolute value.

For example:

```text
abs(+1,-1,+1) = (1,1,1)
abs(+1,+1,+1) = (1,1,1)
```

which would incorrectly collapse two different sign-orbits.

The correct object is:

```text
the equivalence class {M,-M}
```

or, equivalently:

```text
the canonical sign-normalized state C(M)
```

This distinction is important.

---

## 24. Global sign inversion reverses the phase exactly

For symmetric states:

```text
M = (a,b,a)
```

the phase is:

```text
p(M) = (b-a) mod 3
```

Now invert the full state:

```text
M -> -M
```

Then:

```text
p(-M)
=
(-b)-(-a)
=
a-b
=
-(b-a)
=
-p(M) mod 3
```

Therefore:

```text
p(-M) = -p(M) mod 3
```

This gives the exact phase transformation:

```text
p=0 -> p=0
p=1 -> p=2
p=2 -> p=1
```

or:

```text
1 <-> 2
0  -> 0
```

This is not interpretive; it follows directly from the arithmetic.

The four sign pairs behave as follows:

| Canonical state | Canonical phase | Negative partner | Negative phase |
|---|---:|---|---:|
| `(0,+1,0)` | `1` | `(0,-1,0)` | `2` |
| `(+1,0,+1)` | `2` | `(-1,0,-1)` | `1` |
| `(+1,-1,+1)` | `1` | `(-1,+1,-1)` | `2` |
| `(+1,+1,+1)` | `0` | `(-1,-1,-1)` | `0` |

So the negative partner is literally a **phase-reversed version** of the positive representative whenever the canonical phase is non-zero.

---

## 25. The first 13-stage presentation occupies only one polarity

[R] Volume 6 proposes a `3^0 -> 3^1 -> 3^2` presentation:

```text
1 + 3 + 9 = 13
```

with:

```text
3^0 = initialization
3^1 = three clear selector demonstrations
3^2 = nine later geometry-heavy pieces
```

The exact segmentation remains interpretive, as already stated in Volume 6.

However, when the full symmetric Möbius states used by the recovered route are classified by global sign, the observed state vocabulary is:

```text
000
010
101
1,-1,1
111
```

These are exactly:

```text
the neutral state
+
the four canonical positive representatives
```

The unused states are exactly:

```text
0,-1,0
-1,0,-1
-1,+1,-1
-1,-1,-1
```

which are:

```text
-010
-101
-(1,-1,1)
-111
```

No additional asymmetric leftover state is required.

That is the unusual observation:

> **The currently recovered first 13-stage route uses one complete canonical half of the signed state space, plus the neutral state, while the other half consists exactly of the four global negatives.**

This is much more structured than merely observing that "four states have not appeared."

The missing four are not arbitrary omissions.

They are the complete negative image of the four non-neutral states already used.

### Caution

This is not yet proof of intentional polarity.

The route contains repeated key families, and the signs of Möbius values are not expected to be statistically uniform in an unconstrained way.

Therefore a naive probability such as `1/16` should not be treated as a significance estimate without a proper null model.

The correct next test is structural:

```text
Do negative partners appear later?
If they appear, do they preserve transition class
while reversing orientation / phase behavior?
```

---

## 26. A smaller state machine: class plus polarity

The new symmetry suggests replacing the earlier idea of nine unrelated opcodes with a smaller machine.

Instead of:

```text
9 raw states -> 9 independent meanings
```

use:

```text
4 transition classes
x
2 polarities
+
1 neutral state
```

The working class table becomes:

```text
CLASS 0:
000
-> NEUTRAL / INHERIT

CLASS 1:
±(0,1,0)
-> CENTER class

CLASS 2:
±(1,0,1)
-> OUTER class

CLASS 3:
±(1,-1,1)
-> REFLECT / OUTER-PROPAGATION class

CLASS 4:
±(1,1,1)
-> SWAP / ROLE-EQUIVALENCE class
```

The positive representatives already have route evidence:

```text
+010
+101
+(1,-1,1)
+111
```

The negative representatives have not yet been behaviorally characterized.

Therefore the safest interpretation is:

```text
class = observed/provisional transition type
sign  = unknown polarity variable
```

The sign could encode one of several closely related things:

```text
forward vs reverse traversal
enter vs leave a structural role
clockwise vs counter-clockwise orientation
outward vs inward use of the same graph relation
positive vs negative branch of the same transition
```

The current data are not sufficient to choose among these interpretations.

The important point is more limited:

```text
the negative partner should be tested as the inverse-polarity
version of the SAME transition class before inventing a new opcode
```

---

## 27. Why the `111 <-> -1,-1,-1` pair is especially important

The pair:

```text
(+1,+1,+1)
<->
(-1,-1,-1)
```

is a uniquely strong future test.

Both states have:

```text
p = 0
```

because:

```text
b-a = 0
```

for both.

Therefore the ordinary phase rule cannot distinguish them at all.

The phase sees:

```text
111      -> p=0
-1,-1,-1 -> p=0
```

If the two states later produce systematically opposite structural behavior, then that difference **cannot** be explained by phase.

It would directly demonstrate that the full signed Möbius vector carries an additional state variable beyond `p`.

This makes the negative homogeneous state:

```text
(-1,-1,-1)
```

one of the most valuable possible future observations.

The same idea applies more generally, but this pair provides the cleanest separation because the phase remains exactly unchanged under sign inversion.

---

## 28. Signed-state architecture and a possible movement rule

Combining the observations gives a more explicit candidate machine.

For a non-zero symmetric Möbius state:

```text
M = (a,b,a)
```

compute:

```text
1. polarity:
   s = sign(first non-zero component)

2. canonical transition class:
   C = s * M

3. phase:
   p = (b-a) mod 3
```

Then use the outputs separately:

```text
C -> WHAT structural relation is active
s -> WHICH polarity / orientation of that relation
p -> WHICH cyclic key phase is used
```

The known route currently suggests:

```text
C=010 -> CENTER class
C=101 -> OUTER class
C=1,-1,1 -> REFLECT / OUTER-PROPAGATION class
C=111 -> SWAP / ROLE-EQUIVALENCE class
C=000 -> neutral / inherited state
```

A possible full transition pipeline is:

```text
mirror / key generator
        |
        v
totient signature
        |
        v
full Möbius state M
        |
        +-----------------------------+
        |                             |
        v                             v
canonical class C                polarity s
        |                             |
        v                             v
transition type                 orientation
        |                             |
        +-------------+---------------+
                      |
                      v
              phase p = b-a mod 3
                      |
          +-----------+-----------+
          |                       |
          v                       v
     key rotation          coordinate layer
                                  |
                                  v
                         local mirror graph
                                  |
                                  v
                        unique movement candidate?
```

This architecture is attractive because the sign inversion is automatically propagated into the known phase mechanism:

```text
M -> -M
implies
p -> -p mod 3
```

So a polarity flip does not require a second arbitrary phase rule.

It automatically changes:

```text
phase 1 <-> phase 2
```

and therefore also changes which phase layer Volume 6 applies to the coordinates.

This creates a concrete route by which the sign of the full Möbius state could influence physical movement through the maze.

### Critical future prediction

If a negative partner appears later, the first test should be:

```text
same canonical class
+
opposite polarity
+
phase reversed when p != 0
```

rather than:

```text
completely new transition rule
```

For example:

```text
+010 -> CENTER class, phase 1

-010 -> should remain CENTER class,
        but with opposite polarity,
        phase 2
```

and:

```text
+101 -> OUTER class, phase 2

-101 -> should remain OUTER class,
        but with opposite polarity,
        phase 1
```

The exact geometric meaning of "opposite polarity" is still unknown.

Finding the first negative state may therefore reveal the actual forward/reverse movement rule.

---


# PART VIII - WORKING STATE TABLE

## 29. Signed working state table

The state table is now better written in terms of **canonical transition class + signed partner**.

| Canonical class | Positive state | Negative partner | `p(+)` | `p(-)` | Current working meaning |
|---|---|---|---:|---:|---|
| neutral | `(0,0,0)` | itself | `0` | `0` | `INHERIT / no local role selector` |
| center class | `(0,+1,0)` | `(0,-1,0)` | `1` | `2` | `CENTER`, polarity unknown |
| outer class | `(+1,0,+1)` | `(-1,0,-1)` | `2` | `1` | `OUTER`, polarity unknown |
| reflect class | `(+1,-1,+1)` | `(-1,+1,-1)` | `1` | `2` | `REFLECT / propagate OUTER`, provisional |
| homogeneous class | `(+1,+1,+1)` | `(-1,-1,-1)` | `0` | `0` | `SWAP / role equivalence`, provisional |

Compact form:

```text
000              -> INHERIT / NEUTRAL

±010             -> CENTER class
±101             -> OUTER class
±(1,-1,1)        -> REFLECT / OUTER-PROPAGATION class
±111             -> SWAP / ROLE-EQUIVALENCE class
```

with:

```text
sign = polarity / orientation candidate
```

The currently observed route uses:

```text
000
+010
+101
+(1,-1,1)
+111
```

and has not yet required:

```text
-010
-101
-(1,-1,1)
-111
```

The labels remain mnemonic hypotheses, not established Cicada terminology.

---

## 30. The four unused states are not arbitrary

The four symmetric states not yet used by the current route are:

```text
(0,-1,0)
(-1,0,-1)
(-1,+1,-1)
(-1,-1,-1)
```

Earlier they could be described simply as "uncharacterized states."

The signed-state observation gives a stronger classification:

```text
(0,-1,0)    = -(0,+1,0)
(-1,0,-1)   = -(+1,0,+1)
(-1,+1,-1)  = -(+1,-1,+1)
(-1,-1,-1)  = -(+1,+1,+1)
```

So every unused state is the exact global negative of one already represented in the recovered route.

Their phase values are:

| Unused state | Positive partner | Positive phase | Negative phase |
|---|---|---:|---:|
| `(0,-1,0)` | `(0,+1,0)` | `1` | `2` |
| `(-1,0,-1)` | `(+1,0,+1)` | `2` | `1` |
| `(-1,+1,-1)` | `(+1,-1,+1)` | `1` | `2` |
| `(-1,-1,-1)` | `(+1,+1,+1)` | `0` | `0` |

The revised prediction is therefore not:

```text
four unknown states
-> four unknown operations
```

but:

```text
four missing negative states
-> test first as reverse-polarity forms
   of the four existing non-neutral classes
```

No exact movement semantics should be assigned until one of these states appears in a blind continuation.

---

# PART IX - RELATION TO THE VOLUME 6 COORDINATE SELECTOR

## 31. Two different unresolved questions

Volume 6 asks:

```text
Given the current point and phase,
which directional branch is compatible?
```

Its working coordinate selector is:

```text
V_p(r,c) = (
  mu(phi^p(r)),
  mu(phi^p(c))
)
```

Volume 6.5 asks an earlier question:

```text
Given the current active key state,
what kind of structural relation should be followed?
```

The two rules therefore need not compete.

They may operate at different levels.

---

## 32. Possible factorization of the transition

A combined deterministic architecture could be:

```text
CURRENT MIRROR / KEY GENERATOR
        |
        v
compile center with phi
        |
        v
ACTIVE 3-RUNE STRUCTURE
        |
        v
totient signature
        |
        v
FULL MÖBIUS STATE M=(a,b,a)
        |
        +-----------------------------+
        |                             |
        v                             v
p=(b-a) mod 3                 state pattern T(M)
        |                             |
        v                             v
key rotation                  transition type
        |                    CENTER / OUTER /
        |                    INHERIT / REFLECT /
        |                    SWAP ...
        v                             |
decrypt ciphertext                   |
        |                             |
        +--------------+--------------+
                       |
                       v
              endpoint / branch point
                       |
                       v
              Volume 6 coordinate
                  selector V_p
                       |
                       v
        choose among compatible geometry
                       |
                       v
            radius / totient scale
                       |
                       v
                 next structure
```

This factorization would explain why a directional rule alone may be insufficient.

The missing variable may be:

```text
transition type
```

not merely:

```text
direction
```

---

## 33. Why this may help the partial/null cases of Volume 6

Volume 6 observes that many later transitions give:

```text
partial coordinate signal
```

or:

```text
null coordinate signal
```

and therefore require geometry.

The full-key Möbius state could potentially tell the route **which geometric role to inspect** before the coordinate selector chooses among candidates.

For example:

```text
010 -> search endpoint as CENTER
101 -> search endpoint as OUTER
```

This would reduce the geometric candidate space before directional selection.

A possible hierarchy is therefore:

```text
1. full key Möbius state -> structural role/class
2. local mirror graph     -> candidates of that class
3. coordinate selector    -> branch preference when available
4. active totient/radius  -> scale
```

This is a testable architecture.

---

# PART X - THE MOST IMPORTANT PREDICTION AFTER DEATH

## 34. DEATH reuses the 101 state

[R] Volume 5 returns to the already established key generator:

```text
J-B-J -> J-T-J
```

with signature:

```text
10-8-10
```

and therefore:

```text
M = (+1,0,+1)
p = 2
```

The active key:

```text
J-J-T
```

decrypts:

```text
C/K-I-E
```

to:

```text
D-EA-TH
```

or:

> **DEATH**

The ciphertext ends at:

```text
E(26,1)
```

This creates a direct falsifiable test of the Volume 6.5 hypothesis.

If:

```text
(+1,0,+1) = OUTER-active
```

is a real transition rule, then the first structures investigated after:

```text
E(26,1)
```

should preferentially treat that endpoint as an **outer / handoff node**, not arbitrarily as any nearby center.

The prediction is:

```text
DEATH
  |
  | active full state = (+1,0,+1)
  v
E(26,1)
  |
  v
search OUTER-role continuations first
```

This prediction must be tested against the complete precomputed mirror graph, without selecting a structure because it produces readable plaintext.

---

# PART XI - WHAT WOULD FALSIFY THE HYPOTHESIS

## 35. Required blind tests

A genuine transition rule must work before the next plaintext is known.

The following tests are therefore required.

### Test A - exhaustive endpoint-role classification

For every active key in the documented route:

```text
1. compute full M
2. record endpoint
3. enumerate every exact mirror containing that endpoint
4. classify endpoint role:
   CENTER
   OUTER
   BOTH
   NONE
5. compare role with M
```

The result should not be selected manually.

### Test B - all occurrences, not only successful examples

If the matrix contains additional active or candidate structures with:

```text
M=(0,+1,0)
```

or:

```text
M=(+1,0,+1)
```

they must also be tested.

A rule cannot be supported only by the examples that already fit it.

### Test C - blind continuation after DEATH

Freeze the state at:

```text
DEATH endpoint = E(26,1)
M = (+1,0,+1)
```

Then generate candidate continuations using only:

- precomputed grid geometry;
- the full Möbius state;
- previously established arithmetic rules;
- the Volume 6 coordinate selector if applicable.

Do not use candidate plaintext to decide the branch.

### Test D - unseen state prediction

If one of the currently uncharacterized states appears:

```text
(-1,-1,-1)
(-1,0,-1)
(-1,+1,-1)
(0,-1,0)
```

record its behavior before assigning it an opcode.

### Test E - state collisions at equal phase

The strongest test is to compare states with the **same phase but different full vectors**.

For example:

```text
p=1:
(0,+1,0)
(+1,-1,+1)
```

If they consistently produce different structural behavior, then the full vector contains information that phase alone cannot represent.

---


### Test F - global sign-pair test

For every future occurrence of a negative state:

```text
-M
```

identify its positive canonical partner:

```text
+M
```

and test whether:

```text
1. both belong to the same structural transition class;
2. their phases satisfy p(-M) = -p(M) mod 3;
3. the route behavior differs by a consistent polarity/orientation relation.
```

A negative state that behaves as a completely unrelated operation would weaken the signed-class model.

### Test G - homogeneous pair test

The strongest discriminating case is:

```text
(+1,+1,+1)
vs
(-1,-1,-1)
```

because both have:

```text
p=0
```

If they later produce opposite or systematically different behavior while phase remains unchanged, the extra behavior must come from the full signed state rather than the phase alone.

### Test H - positive-half continuation test

Under the current `1+3+9` presentation, the recovered route uses only:

```text
000
+010
+101
+(1,-1,1)
+111
```

A continuation should record, before plaintext inspection, whether the next genuinely new state remains in this positive set or crosses into:

```text
-010
-101
-(1,-1,1)
-111
```

The first such crossing would be a natural candidate for a polarity-regime change.


# PART XII - CURRENT EVIDENCE SUMMARY

## 36. Strong observations

The following are direct and reproducible from the existing route:

### Observation A

```text
4-1-4 -> (0,+1,0)
8-1-8 -> (0,+1,0)
```

### Observation B

Three clean `010` cases end on mirror centers:

```text
COLD -> A(11,7) -> center of EA-A-EA
IDEA -> D(17,18) -> center of J-D-J
IS   -> D(21,10) -> center of E-D-E
```

### Observation C

Two clean `101` cases end on mirror outers:

```text
NOW THE -> J(15,20) -> outer of J-D-J
END     -> I(21,23) -> outer of I-R-I
```

### Observation D

`101` is the complement of `010` at the support level:

```text
010 -> center only
101 -> outer pair only
```

### Observation E

For symmetric states:

```text
p = (b-a) mod 3
```

so phase itself is a relative center/outer quantity.

### Observation F

The complete nine-state space decomposes exactly into:

```text
4 global sign pairs + 000
```

There are no additional leftover symmetric states.

### Observation G

The currently used non-neutral states are exactly the four canonical positive representatives:

```text
010
101
1,-1,1
111
```

while the unused states are exactly their negatives.

### Observation H

Global sign inversion has an exact arithmetic effect:

```text
M -> -M
```

implies:

```text
p -> -p mod 3
```

therefore:

```text
phase 1 <-> phase 2
phase 0 -> phase 0
```

### Observation I

The pair:

```text
111 <-> -1,-1,-1
```

is invisible to the ordinary phase rule because both states have `p=0`.

If their future behavior differs, the full signed vector necessarily contains information not present in the phase.

---

## 37. Hypotheses, not established facts

The following interpretations remain hypotheses:

```text
010 -> CENTER opcode
101 -> OUTER opcode
000 -> INHERIT opcode
1-1-1 -> REFLECT / propagate OUTER opcode
111 -> SWAP / role-equivalence opcode
```

In particular:

- three `010` examples are suggestive but still a small sample;
- two clean `101` examples are an even smaller sample;
- `1,-1,1`, `111`, and `000` currently have weaker behavioral evidence;
- the existence of the algebraic reduction `p=b-a mod 3` does not by itself prove a transition-state interpretation;
- the fact that the currently used states lie in one canonical sign half does not by itself prove that sign means forward/reverse movement;
- repeated key families mean state occurrences are not statistically independent;
- the negative partners must be observed and tested before their polarity semantics can be assigned.

---

# PART XIII - MINIMAL MACHINE-READABLE FORM

## 38. Core formulas

```text
KEY_SIGNATURE:
S(K) = (
  phi(k1),
  phi(k2),
  phi(k3)
)

FULL_MOBIUS_STATE:
M(K) = (
  mu(phi(k1)),
  mu(phi(k2)),
  mu(phi(k3))
)

FOR_SYMMETRIC_KEY:
M = (a,b,a)

PHASE:
p = (a+b+a) mod 3
p = (b-a) mod 3

GLOBAL_SIGN_INVERSION:
I(M) = -M

PHASE_UNDER_SIGN_INVERSION:
p(-M) = -p(M) mod 3

POLARITY_FOR_NONZERO_STATE:
s(M) = sign(first non-zero component)

CANONICAL_STATE:
C(M) = s(M) * M

STATE_FACTORIZATION:
M = s * C
```

---

## 39. Signed state dictionary

```text
STATE_NEUTRAL:
M = (0,0,0)
phase = 0
polarity = 0
canonical_class = NEUTRAL
hypothesis = INHERIT / NO_LOCAL_ROLE_SELECTOR

CLASS_CENTER_POSITIVE:
M = (0,+1,0)
canonical = (0,+1,0)
polarity = +1
phase = 1
hypothesis = CENTER
clean_examples = 3

CLASS_CENTER_NEGATIVE:
M = (0,-1,0)
canonical = (0,+1,0)
polarity = -1
phase = 2
hypothesis = SAME_CENTER_CLASS / OPPOSITE_POLARITY
evidence = unobserved

CLASS_OUTER_POSITIVE:
M = (+1,0,+1)
canonical = (+1,0,+1)
polarity = +1
phase = 2
hypothesis = OUTER
clean_examples = 2

CLASS_OUTER_NEGATIVE:
M = (-1,0,-1)
canonical = (+1,0,+1)
polarity = -1
phase = 1
hypothesis = SAME_OUTER_CLASS / OPPOSITE_POLARITY
evidence = unobserved

CLASS_REFLECT_POSITIVE:
M = (+1,-1,+1)
canonical = (+1,-1,+1)
polarity = +1
phase = 1
hypothesis = REFLECT / PROPAGATE_OUTER
evidence = provisional

CLASS_REFLECT_NEGATIVE:
M = (-1,+1,-1)
canonical = (+1,-1,+1)
polarity = -1
phase = 2
hypothesis = SAME_REFLECT_CLASS / OPPOSITE_POLARITY
evidence = unobserved

CLASS_HOMOGENEOUS_POSITIVE:
M = (+1,+1,+1)
canonical = (+1,+1,+1)
polarity = +1
phase = 0
hypothesis = SWAP / ROLE_EQUIVALENCE
evidence = provisional

CLASS_HOMOGENEOUS_NEGATIVE:
M = (-1,-1,-1)
canonical = (+1,+1,+1)
polarity = -1
phase = 0
hypothesis = SAME_HOMOGENEOUS_CLASS / OPPOSITE_POLARITY
evidence = unobserved
```

The signed dictionary encodes the revised hypothesis:

```text
transition class = canonical state C(M)
polarity         = s(M)
phase            = (b-a) mod 3
```

---

## 40. Route evidence

```text
CENTER_CASE_1:
structure = H-U-H
signature = 4-1-4
M = (0,+1,0)
phase = 1
plaintext = COLD
endpoint = A(11,7)
next_role = CENTER
next_mirror = EA-A-EA

CENTER_CASE_2:
structure = A-U/V-A
signature = 8-1-8
M = (0,+1,0)
phase = 1
plaintext = IDEA
endpoint = D(17,18)
next_role = CENTER
next_mirror = J-D-J

CENTER_CASE_3:
structure = H-TH-H
signature = 4-1-4
M = (0,+1,0)
phase = 1
plaintext = IS
endpoint = D(21,10)
next_role = CENTER
next_mirror = E-D-E

OUTER_CASE_1:
structure = OE-I-OE
signature = 10-4-10
M = (+1,0,+1)
phase = 2
plaintext = NOW THE
endpoint = J(15,20)
next_role = OUTER
next_mirror = J-D-J

OUTER_CASE_2:
structure = J-T-J
signature = 10-8-10
M = (+1,0,+1)
phase = 2
plaintext = END
endpoint = I(21,23)
next_role = OUTER
next_mirror = I-R-I

REFLECT_CANDIDATE:
structure = E-G-E
signature = 6-2-6
M = (+1,-1,+1)
phase = 1
observed = outer value 6 propagates through later movement/radius relations

SWAP_CANDIDATE:
structure_A = J-OE-J
structure_B = OE-J-OE
signature_A = 10-10-10
signature_B = 10-10-10
M = (+1,+1,+1)
phase = 0
observed = center/outer rune roles exchange while signature is preserved
```

---

## 41. Prediction state after DEATH

```text
DEATH_KEY_GENERATOR:
J-B-J -> J-T-J

DEATH_SIGNATURE:
10-8-10

DEATH_FULL_MOBIUS_STATE:
(+1,0,+1)

DEATH_CANONICAL_CLASS:
(+1,0,+1) = OUTER class

DEATH_POLARITY:
+1

DEATH_PHASE:
2

DEATH_ACTIVE_KEY:
J-J-T

DEATH_CIPHERTEXT:
C/K-I-E

DEATH_PLAINTEXT:
D-EA-TH

DEATH_ENDPOINT:
E(26,1)

VOLUME_6_5_PREDICTION:
search endpoint first as OUTER / structural handoff
preserve positive polarity unless a new state forces a sign change
if a negative partner appears, test it as the same class with opposite polarity
do not choose candidate by plaintext
```

---

# PART XIV - RESEARCH CONCLUSION

## 42. Main result of Volume 6.5

The existing Möbius phase rule appears to preserve only part of the information generated by the arithmetic.

For symmetric key structures:

```text
M = (a,b,a)
```

the known phase rule is exactly:

```text
p = (b-a) mod 3
```

This already shows that phase is a **relative center-vs-outer quantity**.

The full vector retains additional information that the phase discards.

The strongest repeated behavioral evidence remains:

```text
M=(0,+1,0)
-> COLD endpoint becomes CENTER
-> IDEA endpoint becomes CENTER
-> IS endpoint becomes CENTER
```

while the complementary support pattern gives:

```text
M=(+1,0,+1)
-> NOW THE endpoint becomes OUTER
-> END endpoint becomes OUTER
```

The new observation extends this into the complete symmetric state space.

There are exactly nine possible states:

```text
M=(a,b,a),    a,b in {-1,0,+1}
```

and they decompose exactly as:

```text
4 global sign pairs
+
000
```

The currently recovered route uses:

```text
000
010
101
1,-1,1
111
```

while the four unused states are exactly:

```text
-010
-101
-(1,-1,1)
-111
```

This motivates a substantially smaller state machine.

Instead of interpreting nine raw states as nine unrelated operations, define:

```text
transition class = equivalence class {M,-M}
polarity         = global sign
```

or, computationally:

```text
s = sign(first non-zero component)
C = s*M
```

Then every non-zero state factors as:

```text
M = s*C
```

where `C` belongs to one of four canonical classes.

The current working model is:

```text
000
-> NEUTRAL / INHERIT

±010
-> CENTER class

±101
-> OUTER class

±(1,-1,1)
-> REFLECT / OUTER-PROPAGATION class

±111
-> SWAP / ROLE-EQUIVALENCE class
```

The exact meaning of negative polarity is not yet known.

It may represent:

```text
reverse traversal
inverse use of the same structural relation
enter/leave reversal
inward/outward reversal
another binary orientation of the same graph transition
```

The mathematics provides one exact constraint:

```text
M -> -M
```

forces:

```text
p -> -p mod 3
```

therefore:

```text
phase 1 <-> phase 2
phase 0 -> phase 0
```

So if the global sign is a movement-polarity bit, it is already coupled to the established phase rule automatically.

No additional phase mechanism is required.

This suggests a refined transition architecture:

```text
FULL MÖBIUS STATE M
        |
        +--> canonical class C
        |      -> WHAT structural transition is active
        |
        +--> polarity s
        |      -> WHICH orientation of that transition
        |
        +--> phase p
               -> key rotation
               -> Volume 6 coordinate layer
```

followed by:

```text
local mirror graph
-> candidate structures

coordinate selector
-> branch information when available

totient/radius state
-> movement scale
```

This may explain why a pure directional rule has been difficult to find.

The missing deterministic information may be split across three related outputs of the same arithmetic state:

```text
CLASS
POLARITY
PHASE
```

rather than being encoded in one coordinate arrow.

The observation that the current `1+3+9 = 13`-stage presentation uses only the canonical positive half of the non-neutral state space is especially unusual.

It raises a concrete possibility:

```text
the recovered route is currently operating in one polarity regime
```

and the four unused negative states may be reserved for:

```text
the same structural transitions in the opposite orientation
```

This remains a hypothesis.

The strongest future evidence would be the first appearance of one of:

```text
0,-1,0
-1,0,-1
-1,+1,-1
-1,-1,-1
```

If such a state preserves the transition class of its positive partner while reversing a consistent aspect of traversal, the signed-state interpretation would gain strong support.

The most decisive case would be:

```text
111
vs
-1,-1,-1
```

because both have:

```text
p=0
```

Any systematic behavioral difference between them would necessarily come from the full signed state and not from phase.

Finally, the continuation after **DEATH** remains a blind test.

The regenerated key uses:

```text
J-T-J
-> signature 10-8-10
-> M=(+1,0,+1)
-> canonical class = OUTER
-> polarity = +1
-> phase = 2
-> DEATH
-> endpoint E(26,1)
```

Therefore the immediate continuation should first be searched as:

```text
OUTER-class
positive-polarity
structural handoff
```

without reading candidate plaintext.

If the continuation instead produces one of the four negative states, that event should be treated as a possible **polarity flip** and tested against the exact signed-pair rules above.

The resulting core hypothesis of Volume 6.5 is therefore:

```text
RAW MÖBIUS STATE
=
TRANSITION CLASS
+
POLARITY
+
PHASE INFORMATION
```

with:

```text
transition class = M modulo global sign
polarity         = sign of the canonical orientation
phase            = b-a mod 3
```

This is not yet a deterministic solution to the maze.

But it reduces the apparently irregular nine-state space to a highly constrained signed system and creates several precise falsifiable predictions for any continuation beyond **DEATH**.

---

# References inside this repository

- [Volume 1](./Volume-1.md) - map construction, first key families, original phase rule, `AS I GO THE WEATHER TURNS COLD`.
- [Volume 2](./Volume-2.md) - `H-U-H -> 4-1-4`, COLD endpoint `EA-A-EA`, `E-G-E -> 6-2-6`, `I MAY CRY`.
- [Volume 3](./Volume-3.md) - `OE-I-OE -> 10-4-10`, `NOW THE`, radius-6 propagation.
- [Volume 4](./Volume-4.md) - `A-U/V-A -> 8-1-8`, IDEA endpoint `J-D-J`, `10-10-10`, `J-T-J`, `END`, endpoint `I-R-I`.
- [Volume 5](./Volume-5.md) - return to `4-1-4`, `IS`, endpoint `E-D-E`, reused `J-T-J`, `DEATH`.
- [Volume 6](./Volume-6.md) - phase-coordinate selector and complete/partial/null directional states.

---

## Final status

**Algebraic reduction `p=(b-a) mod 3`:** exact for symmetric Möbius states `M=(a,b,a)`.

**`(0,+1,0) -> CENTER`:** strongest new behavioral pattern; observed in three clean documented cases.

**`(+1,0,+1) -> OUTER`:** complementary repeated pattern; observed in two clean documented cases.

**Nine-state decomposition:** exact: `9 = 4 global sign pairs + 000`.

**Global sign effect on phase:** exact: `p(-M) = -p(M) mod 3`.

**Positive-half observation:** current route uses the four canonical positive non-neutral representatives; their four negatives remain unused under the present route interpretation.

**Negative-state meanings:** unobserved; opposite-polarity interpretation is a falsifiable hypothesis, not an established rule.

**`000 / (+1,-1,+1) / 111` transition meanings:** provisional hypotheses requiring additional examples.

**Combined Volume 6 + 6.5 signed state machine:** promising framework, not yet proven deterministic.

**Overall solution status:** proposed, ongoing, not officially verified.
