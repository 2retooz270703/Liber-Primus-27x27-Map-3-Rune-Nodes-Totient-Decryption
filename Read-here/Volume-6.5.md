# Cicada 3301 Liber Primus 0-2
## 27x27 Rune Matrix Decryption - Volume 6.5

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.  
**Date:** 16.09.2026

> **Current plaintext candidate**
>
> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH.**

This document is the technical Markdown edition of the **Full Möbius State / Transition-Type Hypothesis** developed after Volumes 1-6.

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

This is a working hypothesis, not yet a universal law.

---

## Quick reference

| Item | Volume 6.5 result |
|---|---|
| Subject | Full Möbius state as a possible transition-type selector |
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

# PART VII - WORKING STATE TABLE

## 21. Observed states

| Möbius state | Phase | Support/sign structure | Current working interpretation | Evidence level |
|---|---:|---|---|---|
| `(0,0,0)` | `0` | no active component | `INHERIT / no local role selector` | hypothesis |
| `(0,+1,0)` | `1` | center only | `CENTER` | strongest repeated pattern |
| `(+1,0,+1)` | `2` | outer pair only | `OUTER` | repeated pattern |
| `(+1,-1,+1)` | `1` | outer pair positive, center inverted | `REFLECT / propagate OUTER` | provisional |
| `(+1,+1,+1)` | `0` | all equal and active | `SWAP / role equivalence` | provisional |

Compact form:

```text
000   -> INHERIT
010   -> CENTER
101   -> OUTER
(+1,-1,+1) -> REFLECT / OUTER propagation
111   -> SWAP / equivalent roles
```

The labels are mnemonic names for testable behavior, not established Cicada terminology.

---

## 22. Symmetric states not yet characterized

For:

```text
a,b in {-1,0,+1}
M = (a,b,a)
```

there are nine possible symmetric Möbius states.

The currently emphasized route examples cover five of them.

The remaining sign classes include:

```text
(-1,-1,-1)
(-1,0,-1)
(-1,+1,-1)
(0,-1,0)
```

Their phases would be:

| Möbius state | `p=(b-a) mod 3` |
|---|---:|
| `(-1,-1,-1)` | `0` |
| `(-1,0,-1)` | `1` |
| `(-1,+1,-1)` | `2` |
| `(0,-1,0)` | `2` |

No transition meaning should be assigned to these states without route evidence.

Their future appearance would provide an important test of whether the full-state interpretation is real.

---

# PART VIII - RELATION TO THE VOLUME 6 COORDINATE SELECTOR

## 23. Two different unresolved questions

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

## 24. Possible factorization of the transition

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

## 25. Why this may help the partial/null cases of Volume 6

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

# PART IX - THE MOST IMPORTANT PREDICTION AFTER DEATH

## 26. DEATH reuses the 101 state

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

# PART X - WHAT WOULD FALSIFY THE HYPOTHESIS

## 27. Required blind tests

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

# PART XI - CURRENT EVIDENCE SUMMARY

## 28. Strong observations

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

---

## 29. Hypotheses, not established facts

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
- `1-1-1`, `111`, and `000` currently have weaker behavioral evidence;
- the existence of the algebraic reduction `p=b-a mod 3` does not by itself prove a transition-state interpretation.

---

# PART XII - MINIMAL MACHINE-READABLE FORM

## 30. Core formulas

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
```

---

## 31. Current state dictionary

```text
STATE_000:
M = (0,0,0)
phase = 0
hypothesis = INHERIT / NO_LOCAL_ROLE_SELECTOR

STATE_010:
M = (0,+1,0)
phase = 1
hypothesis = CENTER
clean_examples = 3

STATE_101:
M = (+1,0,+1)
phase = 2
hypothesis = OUTER
clean_examples = 2

STATE_1N11:
M = (+1,-1,+1)
phase = 1
hypothesis = REFLECT / PROPAGATE_OUTER
evidence = provisional

STATE_111:
M = (+1,+1,+1)
phase = 0
hypothesis = SWAP / ROLE_EQUIVALENCE
evidence = provisional
```

---

## 32. Route evidence

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

## 33. Prediction state after DEATH

```text
DEATH_KEY_GENERATOR:
J-B-J -> J-T-J

DEATH_SIGNATURE:
10-8-10

DEATH_FULL_MOBIUS_STATE:
(+1,0,+1)

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
do not choose candidate by plaintext
```

---

# PART XIII - RESEARCH CONCLUSION

## 34. Main result of Volume 6.5

The existing Möbius phase rule may be preserving only part of the information generated by the arithmetic.

For symmetric key structures:

```text
M = (a,b,a)
```

the known phase rule is equivalently:

```text
p = (b-a) mod 3
```

This shows that phase is already a **relative center-vs-outer quantity**.

The full vector then retains information that the phase discards.

The strongest repeated evidence is:

```text
M=(0,+1,0)
-> COLD endpoint becomes CENTER
-> IDEA endpoint becomes CENTER
-> IS endpoint becomes CENTER
```

while the complementary state gives:

```text
M=(+1,0,+1)
-> NOW THE endpoint becomes OUTER
-> END endpoint becomes OUTER
```

The compact working hypothesis is therefore:

```text
FULL MÖBIUS STATE
        |
        +--> phase
        |    -> key rotation
        |
        +--> support/sign pattern
             -> structural role / transition type
```

or even more compactly:

```text
010 -> CENTER
101 -> OUTER
```

with the weaker provisional extensions:

```text
000   -> INHERIT
(+1,-1,+1) -> REFLECT / OUTER propagation
111   -> SWAP / role equivalence
```

This may address a gap left open by Volume 6.

The coordinate selector attempts to answer:

```text
WHICH DIRECTIONAL BRANCH?
```

The full Möbius-state hypothesis attempts to answer:

```text
WHICH STRUCTURAL ROLE / TRANSITION TYPE?
```

A possible complete transition system would therefore combine:

```text
Möbius key state
-> transition class

mirror graph
-> valid candidates

phase-coordinate selector
-> directional branch

totient value / mirror radius
-> movement scale
```

This does **not** yet establish a deterministic solution.

The decisive next test is the continuation after **DEATH**:

```text
J-T-J
-> signature 10-8-10
-> M=(+1,0,+1)
-> DEATH
-> endpoint E(26,1)
```

If `101 -> OUTER` is a real rule, the continuation should be recoverable by treating `E(26,1)` as an outer/handoff state **before any new plaintext is inspected**.

That makes the hypothesis falsifiable.

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

**`000 / (+1,-1,+1) / 111` opcode meanings:** provisional hypotheses requiring additional examples.

**Combined Volume 6 + 6.5 state machine:** promising framework, not yet proven deterministic.

**Overall solution status:** proposed, ongoing, not officially verified.
