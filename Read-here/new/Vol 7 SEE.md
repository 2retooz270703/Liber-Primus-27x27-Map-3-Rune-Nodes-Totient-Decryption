# SOLUTION 0–2 — Volume 7
## Post-DEATH Continuation Research: the `SEE` Candidate

**Status:** Proposed cryptanalytic research. Not an official Cicada 3301 solution.  
**Date:** 19.09.2026

> **Current strongest post-DEATH plaintext candidate**
>
> **SEE**

---

## Quick reference

| Item | Result |
| --- | --- |
| Starting plaintext | `... THE IDEA OF THE END IS DEATH.` |
| DEATH ciphertext | `C/K-I-E` |
| DEATH active key | `J-J-T` |
| Pre-rotation active structure | `J-T-J` |
| Full Möbius state | `(+1,0,+1)` |
| DEATH endpoint | `E(26,1)` |
| Coordinate selector | `V_2(26,1) = (0,+1)` |
| Directional information | horizontal component is RIGHT-compatible; vertical component unresolved |
| Nearby candidate mirror | `EA(25,2)-J(25,6)-EA(25,10)` |
| Compiled candidate key | `EA-I-EA` |
| Reused movement rule | `J -> 10 -> 4 -> 10+4=14 -> RIGHT 14` |
| Landing point | `X(25,16)` |
| Existing mirror at landing | `E(24,16)-X(25,16)-E(26,16)` |
| Candidate ciphertext | `X(25,16)-EA(26,15)-B(27,14)` |
| Decryption | `X-EA-B - EA-I-EA = S-E-E` |
| Candidate plaintext | **SEE** |
| Status of branch | strong candidate, but one transition rule remains unresolved |

---

# 1. Purpose

Volumes 1–5 recover the proposed plaintext:

```text
AS I GO, THE WEATHER TURNS COLD.
I MAY CRY NOW.
THE IDEA OF THE END IS DEATH.
```

Volumes 6 and 6.5 then analyze the route as a state machine and introduce two important tools for predicting later transitions:

1. a **coordinate direction selector** derived from the endpoint coordinates and the current phase;
2. the **full Möbius state** of the active three-rune structure, which appears to correlate with whether the endpoint becomes a CENTER or an OUTER of the next mirror.

This report freezes the state at the end of **DEATH** and investigates a continuation without starting from a guessed plaintext.

The strongest plaintext candidate found in this search is:

> **SEE**

The purpose of this file is to document exactly how that candidate is obtained, which parts reuse already established rules, which geometries are exact, and which step remains hypothetical.

---

# 2. Evidence labels

The same distinction used in Volumes 6 and 6.5 is retained here.

### [R] Recorded route fact

A fact already recorded in Volumes 1–6.5, such as a key, phase, coordinate, movement rule, mirror, or plaintext.

### [D] Derived result

A result obtained directly from the recorded data by applying the stated formulas.

### [H] Working hypothesis

A proposed interpretation or continuation that is structurally motivated but not yet proven to be a universal rule.

This distinction is especially important after DEATH.

---

# 3. Coordinate convention

Coordinates are written as:

```text
(row, column)
```

and are 1-based.

The coordinate selector behaves like a `(y,x)` sign pair:

```text
first value  = row / vertical component
second value = column / horizontal component
```

Direction convention:

```text
row:
-1 = UP
+1 = DOWN
 0 = unresolved vertical component

column:
-1 = LEFT
+1 = RIGHT
 0 = unresolved horizontal component
```

The signs select a directional branch. They are not movement distances.

---

# PART I — FROZEN STATE AT DEATH

## 4. DEATH is produced by the reused J-B-J generator

[R] Volume 5 returns to:

```text
J(19,16) - B(23,12) - J(27,8)
```

or:

```text
J-B-J
```

The center transforms by Euler's totient:

```text
B = 17
phi(17) = 16 = T
```

Therefore:

```text
J-B-J -> J-T-J
```

The totient signature of the compiled structure is:

```text
phi(J) = 10
phi(T) = 8
phi(J) = 10

signature = 10-8-10
```

The Möbius values are:

```text
mu(10) = +1
mu(8)  = 0
mu(10) = +1
```

Therefore:

```text
M = (+1,0,+1)
```

and:

```text
p = 2
```

Phase 2 rotates:

```text
J-T-J -> J-J-T
```

[R] This active key decrypts:

```text
C/K-I-E
-
J-J-T
=
D-EA-TH
```

giving:

> **DEATH**

The final ciphertext cell is:

```text
E(26,1)
```

This is the exact starting point of the post-DEATH search.

---

# PART II — TWO PREDICTIONS AVAILABLE AFTER DEATH

## 5. Prediction A: the endpoint coordinate selector

Volume 6 proposes:

```text
V_p(r,c) = ( mu(phi^p(r)), mu(phi^p(c)) )
```

using the same phase `p` already determined by the active key state.

For the DEATH endpoint:

```text
E(26,1)
p = 2
```

calculate the row component:

```text
26 -> phi(26)=12 -> phi(12)=4
mu(4)=0
```

and the column component:

```text
1 -> phi(1)=1 -> phi(1)=1
mu(1)=+1
```

Therefore:

```text
V_2(26,1) = (0,+1)
```

Interpretation:

```text
0  = vertical direction unresolved
+1 = positive horizontal / RIGHT-compatible component
```

So the endpoint of DEATH supplies a directional constraint:

> **Search the next local continuation on a RIGHT-compatible side, while geometry must resolve the missing vertical component.**

This is a **partial selector**, not a complete movement command.

Volume 6 explicitly warns that in one-zero cases the surviving sign is not yet proven to be a literal immediate arrow.

---

## 6. Why the coordinate selector is taken seriously

The selector reproduces several already recorded route directions when both components are non-zero.

Examples from Volume 6:

```text
WEATHER -> TURNS
V = (-1,+1)
-> UP + RIGHT
-> recorded move: UP 10, RIGHT 4
```

```text
TURNS -> COLD
V = (+1,-1)
-> DOWN + LEFT
-> recorded move: DOWN 12, LEFT 12
```

```text
COLD -> I MAY
V = (+1,+1)
-> DOWN + RIGHT
-> recorded move: DOWN 4, RIGHT 1
```

and before DEATH:

```text
B(23,12), p=2
V = (+1,-1)
-> DOWN + LEFT
-> selects the down-left outer J(27,8)
```

So a complete selector can reproduce the correct movement quadrant.

For DEATH:

```text
V_2(26,1)=(0,+1)
```

is weaker: only the RIGHT component survives.

---

## 7. Prediction B: the full Möbius state

Volume 6.5 observes that the full Möbius state contains more information than the phase alone.

For symmetric active structures:

```text
M = (a,b,a)
```

the phase is only one projection of the full state.

Two repeated patterns are especially important:

```text
(0,+1,0)  <-> CENTER-active
(+1,0,+1) <-> OUTER-active
```

The working interpretation is:

> The Möbius pattern of the active pre-rotation key structure predicts the structural role of the final ciphertext cell in the next mirror.

---

## 8. Repeated CENTER-active examples

Volume 6.5 records three clean `010` cases.

### COLD

```text
H-U-H
-> signature 4-1-4
-> M=(0,+1,0)
-> COLD
-> endpoint A(11,7)
-> CENTER of EA(10,7)-A(11,7)-EA(12,7)
```

### IDEA

```text
A-U/V-A
-> signature 8-1-8
-> M=(0,+1,0)
-> IDEA
-> endpoint D(17,18)
-> CENTER of J(15,20)-D(17,18)-J(19,16)
```

### IS

```text
H-TH-H
-> signature 4-1-4
-> M=(0,+1,0)
-> IS
-> endpoint D(21,10)
-> CENTER of E(19,12)-D(21,10)-E(23,8)
```

So the repeated observation is:

```text
010
-> ciphertext endpoint becomes CENTER of the next mirror
```

---

## 9. Repeated OUTER-active examples

Volume 6.5 records two clean `101` cases.

### NOW THE

```text
OE-I-OE
-> signature 10-4-10
-> M=(+1,0,+1)
-> NOW THE
-> endpoint J(15,20)
-> OUTER of J(15,20)-D(17,18)-J(19,16)
```

### END

```text
J-T-J
-> signature 10-8-10
-> M=(+1,0,+1)
-> END
-> endpoint I(21,23)
-> OUTER of I(21,21)-R(21,22)-I(21,23)
```

So the repeated observation is:

```text
101
-> ciphertext endpoint becomes OUTER of the next mirror
```

This is important for DEATH because DEATH is generated by the exact same pre-rotation structure used for END:

```text
J-T-J
-> 10-8-10
-> M=(+1,0,+1)
```

Therefore the blind Volume 6.5 prediction is:

```text
DEATH endpoint E(26,1)
-> search OUTER-role continuations first
```

---

# PART III — IMPORTANT LIMITATION OF THE STRICT OUTER PREDICTION

## 10. E(26,1) is not the E of the known E-X-E mirror

A critical coordinate correction is necessary.

The exact `E-X-E` mirror already used in Volume 2 is:

```text
E(24,16)
   |
X(25,16)
   |
E(26,16)
```

That is:

```text
E(24,16)-X(25,16)-E(26,16)
```

The DEATH endpoint is:

```text
E(26,1)
```

Therefore:

> **E(26,1) is not an outer of this E-X-E mirror.**

The two cells are on the same row but 15 columns apart:

```text
DEATH endpoint: E(26,1)
known E-X-E outer: E(26,16)
```

The post-DEATH candidate must not claim otherwise.

---

## 11. What remains unresolved

The strictest reading of the Volume 6.5 hypothesis says:

```text
101
-> the exact ciphertext endpoint itself
-> should become an OUTER of the next mirror
```

For DEATH this predicts that:

```text
E(26,1)
```

should itself participate as an outer / handoff cell.

The `SEE` candidate documented below does **not yet prove that strict condition**.

Instead, it finds a nearby right-compatible outer:

```text
EA(25,2)
```

which is one step:

```text
UP 1, RIGHT 1
```

from the DEATH endpoint.

This preserves the positive horizontal component of:

```text
V_2(26,1)=(0,+1)
```

but the exact handoff rule:

```text
E(26,1) -> EA(25,2)
```

remains a working hypothesis.

This is currently the main weakness of the `SEE` branch.

---

# PART IV — THE EA-J-EA CANDIDATE

## 12. A nearby exact mirror on the right-compatible side

One cell up and one cell right from the endpoint:

```text
E(26,1)
-> UP 1, RIGHT 1
-> EA(25,2)
```

The cell `EA(25,2)` is the left outer of the exact horizontal mirror:

```text
EA(25,2) - J(25,6) - EA(25,10)
```

with radius:

```text
4
```

An exhaustive scan of the 27x27 matrix over the standard horizontal, vertical, and 45-degree mirror axes finds this as the **only standard `EA-J-EA` occurrence**.

So the candidate geometry is not chosen from many identical `EA-J-EA` nodes.

---

## 13. EA-J-EA compiles exactly like the first node of Volume 1

The center is:

```text
J = 11
```

Apply Euler's totient:

```text
phi(11)=10=I
```

Therefore:

```text
EA-J-EA
->
EA-I-EA
```

Candidate key:

```text
EA-I-EA
```

This follows the established mirrored-node compilation rule:

```text
a-b-a -> a-phi(b)-a
```

No new key-generation rule is required.

---

## 14. Möbius state of EA-I-EA

The totient signature is:

```text
phi(EA=28)=12
phi(I=10)=4
phi(EA=28)=12
```

So:

```text
signature = 12-4-12
```

Apply Möbius:

```text
mu(12)=0
mu(4)=0
mu(12)=0
```

Therefore:

```text
M=(0,0,0)
p=0
```

So the candidate key is not rotated:

```text
EA-I-EA
```

This is a neutral Möbius state rather than a CENTER-active or OUTER-active state.

---

# PART V — THE OLD J MOVEMENT RULE REAPPEARS

## 15. RIGHT 14 is not invented for SEE

The strongest arithmetic feature of the candidate is that the center `J` reproduces a movement rule already used at the very beginning of Volume 1.

The original bootstrap rule is:

```text
J = 11
phi(J)=10=I

phi(10)=4

10+4=14

-> RIGHT 14
```

In Volume 1 this rule is used from the first `AE-J-EA` node to enter the first ciphertext stage.

Therefore using the same `J` mechanism here does not require a new distance formula.

The candidate `EA-J-EA` contains the same center:

```text
J
```

so it reproduces:

```text
J
-> 10
-> 4
-> 10+4=14
-> RIGHT 14
```

---

## 16. RIGHT 14 lands exactly on X(25,16)

Start from the left outer:

```text
EA(25,2)
```

Move:

```text
RIGHT 14
```

Then:

```text
column 2 + 14 = 16
```

so the destination is:

```text
X(25,16)
```

This landing is exact:

```text
EA(25,2)
-> R14
-> X(25,16)
```

No plaintext is needed to choose `X(25,16)`.

---

# PART VI — THE LANDING POINT IS AN ALREADY IMPORTANT NODE

## 17. X(25,16) is the center of the unique E-X-E mirror

The landing cell is not an isolated X.

It is the center of:

```text
E(24,16)
   |
X(25,16)
   |
E(26,16)
```

or:

```text
E(24,16)-X(25,16)-E(26,16)
```

This `E-X-E` mirror is already part of the recorded route in Volume 2.

Volume 2 uses it immediately after `I MAY`:

```text
I MAY
-> final ciphertext E(26,16)
-> E-X-E
-> phi(X=14)=6=G
-> E-G-E
-> CRY route
```

An exhaustive scan of the matrix over the standard mirror axes finds only **one standard E-X-E occurrence**, centered at:

```text
X(25,16)
```

So the old J-based `RIGHT 14` rule lands exactly on a unique, previously important structural center.

This is one of the strongest cross-checks in the SEE candidate.

---

# PART VII — CIPHERTEXT AT X

## 18. A direct three-rune diagonal begins at X(25,16)

From:

```text
X(25,16)
```

read one cell down-left at each step:

```text
X(25,16)
-> EA(26,15)
-> B(27,14)
```

This gives the contiguous straight ciphertext:

```text
X-EA-B
```

The direction is:

```text
DOWN + LEFT
```

An exhaustive scan of all eight adjacent straight-line directions in the 27x27 matrix finds only **one contiguous `X-EA-B` triple**:

```text
X(25,16)-EA(26,15)-B(27,14)
```

Again, the plaintext is not needed to choose between multiple identical contiguous `X-EA-B` occurrences.

---

# PART VIII — DECRYPTION

## 19. X-EA-B minus EA-I-EA

Candidate ciphertext:

```text
X-EA-B
```

Candidate key:

```text
EA-I-EA
```

Using the established rule:

```text
P = C - K mod 29
```

with 0-based Gematria Primus indices:

```text
X  = 14
EA = 28
B  = 17

EA = 28
I  = 10
EA = 28
```

Position 1:

```text
14 - 28 = -14
-14 mod 29 = 15
15 = S
```

Position 2:

```text
28 - 10 = 18
18 = E
```

Position 3:

```text
17 - 28 = -11
-11 mod 29 = 18
18 = E
```

Therefore:

```text
X-EA-B
-
EA-I-EA
=
S-E-E
```

Result:

> # **SEE**

---

# PART IX — WHY SEE IS INTERESTING

## 20. The plaintext appears only after the structure is selected

The strongest way to state the candidate is not:

```text
we wanted SEE
-> searched for runes that produce SEE
```

The candidate chain is instead:

```text
DEATH endpoint
-> coordinate selector gives a surviving RIGHT component
-> inspect nearby right-compatible geometry
-> exact EA-J-EA mirror
-> compile J -> I
-> EA-I-EA
-> reuse old J -> 10 -> 4 -> RIGHT 14 rule
-> land exactly on X(25,16)
-> X is the center of the known unique E-X-E mirror
-> direct contiguous diagonal X-EA-B
-> subtract EA-I-EA
-> SEE
```

The readable plaintext occurs at the end of the chain.

---

## 21. Reuse instead of rule creation

The candidate reuses several mechanisms that already existed before SEE was considered.

### Reused rule 1 — mirrored-center compilation

```text
a-b-a -> a-phi(b)-a
```

Applied here:

```text
EA-J-EA -> EA-I-EA
```

### Reused rule 2 — J bootstrap arithmetic

Already in Volume 1:

```text
J -> 10
10 -> 4
10+4=14
-> RIGHT 14
```

Reused here without changing the formula.

### Reused structure — E-X-E

The landing point:

```text
X(25,16)
```

is the center of the exact `E-X-E` already used in Volume 2.

### Reused decryption rule

```text
P = C - K mod 29
```

No new cipher operation is introduced.

---

## 22. Structural rarity checks

For this report, the complete 27x27 matrix was scanned for the relevant exact structures.

Using the standard horizontal, vertical, and 45-degree mirror axes:

```text
EA-J-EA
```

occurs once:

```text
EA(25,2)-J(25,6)-EA(25,10)
```

and:

```text
E-X-E
```

occurs once:

```text
E(24,16)-X(25,16)-E(26,16)
```

Scanning all eight directions for adjacent straight three-rune sequences:

```text
X-EA-B
```

occurs once:

```text
X(25,16)-EA(26,15)-B(27,14)
```

These uniqueness checks do not prove the continuation, but they reduce the possibility that the chain is selecting among many identical local patterns.

---

# PART X — WHAT THE SEE KEY SAYS AFTER SEE

## 23. The EA-I-EA state is neutral

As shown above:

```text
EA-I-EA
-> signature 12-4-12
-> M=(0,0,0)
-> p=0
```

Unlike `010` or `101`, the `000` state does not itself provide a CENTER/OUTER preference in the current Volume 6.5 model.

So after SEE, the next transition should not be forced from a CENTER/OUTER interpretation of this key state.

The endpoint geometry becomes especially important.

---

## 24. SEE ends at B(27,14)

The candidate ciphertext is:

```text
X(25,16)
EA(26,15)
B(27,14)
```

so SEE ends at:

```text
B(27,14)
```

Because the candidate phase is:

```text
p=0
```

the endpoint selector is:

```text
V_0(27,14) = (mu(27), mu(14))
```

Now:

```text
mu(27)=0
```

because `27=3^3` is not square-free, and:

```text
mu(14)=+1
```

because `14=2*7` has two distinct prime factors.

Therefore:

```text
V_0(27,14)=(0,+1)
```

So the candidate SEE endpoint again gives a partial selector with a surviving RIGHT-compatible horizontal component.

This is a useful prediction for future blind continuation tests.

It is not yet a recovered next word.

---

# PART XI — COMPARISON WITH OTHER POST-DEATH CANDIDATES

## 25. The earlier ITS branch

An earlier candidate used an arbitrary-slope central symmetry:

```text
E-B-E
```

around the DEATH region and produced a key capable of decrypting a short path to:

```text
ITS
```

The branch was interesting because it connected to an older structural endpoint.

However, it is weaker than SEE for methodology because:

1. it depends on allowing a non-standard mirror slope;
2. the partial selector `(0,+1)` was initially interpreted too strongly as a literal RIGHT command;
3. the node-selection rule is less directly inherited from earlier volumes.

Therefore `ITS` remains an interesting alternative plaintext candidate, but it is not the preferred post-DEATH branch in this report.

---

## 26. The 10,8 -> X(16,9) structural branch

Another candidate interpreted the `J-T-J` signature:

```text
10-8-10
```

as a two-dimensional movement pair:

```text
10,8
```

from the DEATH endpoint.

That route reached:

```text
X(16,9)
```

with unusually rich nested mirror structure.

It is structurally interesting, but weaker as a direct continuation rule because Volume 6 explicitly states that the first movement-distance rule is not yet universally formalized.

By contrast, the SEE branch reuses the exact old:

```text
J -> 10 -> 4 -> 14
```

bootstrap rule already recorded in Volume 1.

So the SEE branch currently requires less new arithmetic.

---

# PART XII — STRENGTHS AND WEAKNESSES

## 27. Strongest parts of the SEE candidate

The strongest observations are:

1. **DEATH has a precisely frozen state.**  
   `J-T-J -> 10-8-10 -> M=101 -> p=2 -> J-J-T -> DEATH`.

2. **The endpoint selector is derived without plaintext.**  
   `E(26,1), p=2 -> V_2=(0,+1)`.

3. **The candidate mirror is exact.**  
   `EA(25,2)-J(25,6)-EA(25,10)`.

4. **EA-J-EA is unique among standard mirrors in the matrix.**

5. **The key compilation uses the established rule.**  
   `EA-J-EA -> EA-I-EA`.

6. **The movement rule is old, not invented.**  
   The same `J -> 10 -> 4 -> 14` mechanism already appears at the beginning of Volume 1.

7. **RIGHT 14 lands exactly on X(25,16).**

8. **X(25,16) is the center of the unique E-X-E mirror already important in Volume 2.**

9. **The candidate ciphertext is a direct contiguous line.**  
   `X(25,16)-EA(26,15)-B(27,14)`.

10. **X-EA-B is unique as an adjacent straight triple in the matrix.**

11. **The standard mod-29 subtraction gives an exact readable result.**  
    `X-EA-B - EA-I-EA = SEE`.

12. **No plaintext is needed until the final subtraction.**

---

## 28. Main unresolved point

The principal weakness is the transition:

```text
E(26,1)
-> EA(25,2)
```

The coordinate selector:

```text
(0,+1)
```

supports the positive/rightward component, but does not determine the UP component.

More importantly, the strict Volume 6.5 `101 -> OUTER` hypothesis predicts that the **exact DEATH endpoint itself** should preferentially become an outer/handoff node.

The SEE branch instead uses the adjacent:

```text
EA(25,2)
```

as the outer of `EA-J-EA`.

Therefore the current status must remain:

> **SEE is a strong candidate continuation, not a completed deterministic proof.**

A stronger future result would derive the `E(26,1) -> EA(25,2)` handoff from an already established state rule, or identify a directly endpoint-anchored structure that naturally leads into the same chain.

---

# PART XIII — COMPACT CHAIN

## 29. Human-readable chain

```text
THE IDEA OF THE END IS DEATH
        |
        v
DEATH ciphertext = C/K-I-E
DEATH endpoint    = E(26,1)
active structure  = J-T-J
signature         = 10-8-10
M                 = (+1,0,+1)
phase             = 2
active key        = J-J-T
        |
        v
coordinate selector at E(26,1)
V_2(26,1) = (0,+1)
        |
        v
RIGHT-compatible local search
        |
        v
EA(25,2)-J(25,6)-EA(25,10)
        |
        | phi(J=11)=10=I
        v
EA-I-EA
        |
        | old Volume 1 J rule:
        | J -> 10 -> 4 -> 10+4=14
        v
RIGHT 14 from EA(25,2)
        |
        v
X(25,16)
        |
        | center of known E-X-E:
        | E(24,16)-X(25,16)-E(26,16)
        v
read DOWN-LEFT
        |
        v
X(25,16)-EA(26,15)-B(27,14)
        |
        v
X-EA-B - EA-I-EA
        |
        v
S-E-E
        |
        v
SEE
```

---

## 30. Minimal machine-readable chain

```text
PREVIOUS_RESULT:
plaintext = "THE IDEA OF THE END IS DEATH"

DEATH_STATE:
parent_node = J-B-J
compile = J-B-J -> J-T-J
signature = 10-8-10
mobius_state = (+1,0,+1)
phase = 2
active_key = J-J-T
ciphertext = C/K-I-E
plaintext = D-EA-TH
endpoint = E(26,1)

ENDPOINT_SELECTOR:
point = E(26,1)
phase = 2
row: 26 -> 12 -> 4 -> mu(4)=0
col: 1 -> 1 -> 1 -> mu(1)=+1
V = (0,+1)
state = PARTIAL
constraint = RIGHT-compatible; vertical unresolved

CANDIDATE_HANDOFF:
E(26,1) -> EA(25,2)
status = HYPOTHESIS

MIRROR:
EA(25,2)-J(25,6)-EA(25,10)

COMPILE:
phi(J=11)=10=I
EA-J-EA -> EA-I-EA

KEY_STATE:
signature = 12-4-12
mobius_state = (0,0,0)
phase = 0
active_key = EA-I-EA

MOVEMENT:
J -> 10
phi(10)=4
10+4=14
direction = RIGHT
EA(25,2) -> R14 -> X(25,16)

STRUCTURAL_LANDING:
E(24,16)-X(25,16)-E(26,16)
node = E-X-E
X_role = CENTER

CIPHERTEXT:
X(25,16)-EA(26,15)-B(27,14)

DECRYPT:
X-EA-B - EA-I-EA = S-E-E

CANDIDATE_PLAINTEXT:
SEE

SEE_ENDPOINT:
B(27,14)
phase = 0
V_0(27,14) = (0,+1)

STATUS:
strong post-DEATH plaintext candidate
main unresolved step = E(26,1) -> EA(25,2)
```

---

# PART XIV — VALIDATION STATUS

## 31. What is directly reproducible

The following can be reproduced directly from the current repository data and formulas:

- `J-B-J -> J-T-J`;
- `J-T-J -> 10-8-10`;
- `M=(+1,0,+1)`;
- `p=2`;
- `J-J-T` decrypts `C/K-I-E` to `DEATH`;
- DEATH ends at `E(26,1)`;
- `V_2(26,1)=(0,+1)`;
- `EA(25,2)-J(25,6)-EA(25,10)` exists exactly;
- `EA-J-EA -> EA-I-EA`;
- `EA-I-EA -> 12-4-12 -> M=(0,0,0) -> p=0`;
- the old J rule gives `10+4=14`;
- RIGHT 14 from `EA(25,2)` lands at `X(25,16)`;
- `X(25,16)` is the center of `E(24,16)-X(25,16)-E(26,16)`;
- `X(25,16)-EA(26,15)-B(27,14)` is a contiguous diagonal;
- `X-EA-B - EA-I-EA = SEE`;
- `V_0(B(27,14))=(0,+1)`.

---

## 32. What remains hypothesis

The following must remain explicitly provisional:

- that the partial selector `(0,+1)` is sufficient to choose the nearby `EA(25,2)`;
- that the route should hand off from `E(26,1)` to `EA(25,2)`;
- that `SEE` is the intended next plaintext rather than a structurally strong coincidence;
- that the neutral `000` state after `EA-I-EA` has been fully understood;
- that the next transition after `SEE` can be predicted without adding another rule.

---

# 33. Current conclusion

The strongest candidate continuation found after DEATH is:

> # **SEE**

Its strongest feature is not the English word itself.

The strongest feature is the structural chain:

```text
DEATH endpoint
-> phase-derived coordinate constraint
-> exact EA-J-EA
-> established center-totient compilation
-> old J-based RIGHT 14 rule from Volume 1
-> exact landing on the previously important E-X-E center
-> unique contiguous X-EA-B ciphertext
-> ordinary mod-29 subtraction
-> SEE
```

This gives a continuation with substantial reuse of previously documented arithmetic and geometry.

However, one transition remains insufficiently formalized:

```text
E(26,1) -> EA(25,2)
```

Therefore the correct research status is:

> **SEE is currently the strongest post-DEATH plaintext candidate found by this search, but it should remain labeled a candidate until the endpoint-to-EA handoff is derived independently of the plaintext.**

---

# 34. References inside this repository

- [Volume 1](./Volume-1.md) — bootstrap `J -> 10 -> 4 -> RIGHT 14`, original key generation, phase rule, mod-29 subtraction.
- [Volume 2](./Volume-2.md) — `I MAY`, the exact `E-X-E` node at column 16, and its role in the CRY continuation.
- [Volume 5](./Volume-5.md) — `IS`, regenerated `J-T-J / J-J-T`, ciphertext `C/K-I-E`, and `DEATH`.
- [Volume 6](./Volume-6.md) — coordinate selector `V_p(r,c)` and complete/partial/null selector states.
- [Volume 6.5](./Volume-6.5.md) — full Möbius state, CENTER/OUTER endpoint-role hypothesis, and the blind post-DEATH `101` prediction.
- `../other-stuff/data/0-2-runes.txt` — source 27x27 rune matrix used for coordinate and uniqueness checks.
