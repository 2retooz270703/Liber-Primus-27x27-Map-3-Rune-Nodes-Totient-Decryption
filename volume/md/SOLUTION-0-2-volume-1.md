# SOLUTION 0–2 — Volume 1

## Technical Markdown Edition

This document is a structured technical transcription of **SOLUTION 0-2 volume 1** for **Cicada 3301's Liber Primus, pages 0–2**.

Its purpose is to make the proposed method easy to read, search, reproduce, criticize, and parse by humans, GitHub search, web search engines, and AI systems.

This file does **not** claim that the method is an officially verified solution to Liber Primus. It records the proposed derivation in Volume 1 and separates the core technical chain from secondary observations and interpretive hypotheses.

## Quick reference

| Item | Volume 1 result |
| --- | --- |
| Subject | Cicada 3301 — Liber Primus pages 0–2 |
| Input size | 729 runes |
| Spatial representation | 27×27 rune matrix |
| Main node type | mirrored / structured three-rune nodes |
| Main arithmetic | Gematria Primus indices, Euler's totient φ, Möbius μ, mod 29 |
| Phase rule | `p = Σ μ(φ(Kᵢ)) mod 3` |
| Current proposed plaintext | **AS I GO, THE WEATHER TURNS COLD** |
| Status | proposed, ongoing, not officially verified |

### Source-page map

This Markdown edition follows the accompanying PDF in this order:

- PDF pp. 5–8: 729-rune matrix, AE-J-EA, RIGHT 14, **AS I GO THE**
- PDF pp. 9–11 and 18: X-OE-X, central NG, Möbius phase, **WEATHER**
- PDF pp. 12–18: A crossroads, values 10 and 4, H-NG-C, **TURNS**
- PDF pp. 19–21: `φ(NG)=12`, H-TH-H → H-U-H, **COLD**
- PDF pp. 21–24: 233 / Fibonacci / column structure / thematic observations
- PDF pp. 1–4: GEB / RTN context and the broader methodological interpretation

---


## 1. Scope

The Volume 1 proposal is based on the following central idea:

**729 runes → 27×27 matrix → mirrored three-rune structures → Euler totient transformations → movement through the matrix → three-rune keys → Möbius key phase → Gematria Primus subtraction mod 29 → plaintext → next structural node**

Current proposed plaintext:

> **AS I GO, THE WEATHER TURNS COLD**

The core technical derivation begins with the exact rune count of pages 0–2.

---

## 2. Notation and conventions

### 2.1 Rune transliteration tokens

Names such as `AE`, `OE`, `NG`, and `TH` are **single rune transliteration tokens**, not sequences of ordinary Latin letters.

This matters when counting runes.

For example:

- `AS I GO THE` = `A-S-I-G-O-TH-E` = **7 runes**
- `WEATHER` = `W-EA-TH-E-R` = **5 runes**
- `TURNS` = `T-U-R-N-S` = **5 runes**
- `COLD` = `C-O-L-D` = **4 runes**

Total:

`7 + 5 + 5 + 4 = 21 runes`

The spaces and punctuation in the English plaintext are human-readable grouping; the cryptographic operations are performed on rune tokens.

### 2.2 Numeric systems

The core decryption and totient steps use the **0-based Gematria Primus index values used in Volume 1**.

Examples:

- `J = 11`
- `I = 10`
- `NG = 21`
- `TH = 2`
- `U = 1`

Volume 1 also mentions a separate **prime-value assignment** in later supporting observations, for example the statement that W has zero-based GP index 7 and prime value 19.

These two numeric systems should not be conflated:

- **0-based GP index** → used in the core mod-29 / totient derivation and the 233 sum;
- **prime value** → used only in secondary numerical observations.

### 2.3 Euler's totient function

Euler's totient function is written:

`φ(n)`

It is used in the proposal for:

1. transforming the center rune of a three-rune node;
2. generating or reusing movement values;
3. connecting one structural stage to the next.

### 2.4 Möbius function

The Möbius function is written:

`μ(n)`

It is used to determine the starting phase of a repeating three-rune key.

### 2.5 Modular decryption

The decryption rule is:

`P = C - K mod 29`

where:

- `P` = plaintext rune index;
- `C` = ciphertext rune index;
- `K` = active key rune index.

After subtraction modulo 29, the resulting index is mapped back to its Gematria Primus rune.

### 2.6 Coordinates

Coordinates in Volume 1 are written as:

`(row, column)`

The 27×27 matrix is labeled from 1 to 27 on both axes, so the coordinates used here are **1-based**.

### 2.7 Core rule versus local transition

Volume 1 does **not** present one universal movement equation that automatically generates every future step.

Instead, it proposes a recurring framework:

`node → mathematical value → local movement/key instruction → plaintext → next structural clue`

The totient, three-rune key structure, phase rule, and mod-29 subtraction recur, while the exact way a locally derived value is used can depend on the structure reached at that stage.

This distinction is important for accurately representing the Volume 1 hypothesis.

---

# Part I — Construction of the map

## 3. Exact rune count: 729 = 27 × 27

Liber Primus pages 0–2 contain exactly:

**729 runes**

and:

**729 = 27 × 27**

The proposed construction is therefore to write the complete rune sequence into a square matrix:

1. begin with the first rune;
2. write runes from left to right;
3. after 27 runes, continue at the beginning of the next row;
4. repeat until all 729 runes are placed.

This creates a:

**27×27 rune matrix**

No runes are added or removed.

In Volume 1, the matrix is treated as more than a convenient layout. Its geometry is part of the proposed cryptanalytic mechanism.

The source notes visible symmetry and reflection around the central region and treats mirrored three-rune structures as possible functional nodes.

---

## 4. Core node model

A recurring structural pattern is a three-rune node:

`a - b - c`

The central rune can be transformed with Euler's totient function.

The later node-compilation rule is stated as:

`K = (a, φ(b), c)`

So a node:

`a - b - c`

can generate the key:

`a - φ(b) - c`

when `φ(b)` corresponds to a Gematria Primus rune value.

In the proposed route, three-rune structures are used for both:

- **key generation**, and
- **navigation through the 27×27 matrix**.

---

# Part II — Stage 1: AS I GO THE

## 5. First node: AE-J-EA

The first important three-rune structure is:

**AE-J-EA**

The center rune is:

`J = 11`

Apply Euler's totient:

`φ(11) = 10`

and Gematria Primus value 10 is:

`I`

Therefore:

`AE-J-EA → AE-I-EA`

The generated repeating key is:

**AE-I-EA**

---

## 6. Movement from the first node

The same transformed value is also used to derive movement.

From:

`J → φ(J) = 10 = I`

apply the totient once more:

`φ(10) = 4`

Then:

`10 + 4 = 14`

Volume 1 interprets this as:

**RIGHT 14**

So the proposed route is:

```text
AE-J-EA
→ J
→ φ(J)=10=I
→ φ(I)=4
→ 10+4=14
→ RIGHT 14
```

---

## 7. First ciphertext and decryption

At the resulting location, Volume 1 gives the encrypted runes:

**L-AE-N-TH-P-U-X**

The three-rune key is repeated across seven runes:

**AE-I-EA-AE-I-EA-AE**

Using Gematria Primus subtraction modulo 29:

`P = C - K mod 29`

Volume 1 gives:

```text
ciphertext: L-AE-N-TH-P-U-X
key:        AE-I-EA-AE-I-EA-AE
operation:  P = C - K mod 29
result:     A-S-I-G-O-TH-E
```

Result:

> **AS I GO THE**

The source treats this as especially important because:

- the key is generated directly from the node;
- the movement value is generated from the same totient chain;
- the key spans exactly seven ciphertext runes;
- the decrypted segment ends at the next structural feature.

---

# Part III — Stage 2: WEATHER

## 8. Transition from the final X

The plaintext segment:

**AS I GO THE**

ends on a final ciphertext rune:

**X**

Volume 1 identifies an adjacent mirrored structure:

**X-OE-X**

The center rune is:

`OE`

and:

`φ(OE) = 10 = I`

Therefore:

`X-OE-X → X-I-X`

The new three-rune key is:

**X-I-X**

The same value `10 = I` is used as the next movement:

**RIGHT 10**

This movement lands on:

**NG**

at the exact center of the 27×27 matrix.

The proposed chain is therefore:

```text
AS I GO THE
→ final X
→ adjacent X-OE-X
→ φ(OE)=10=I
→ compiled key X-I-X
→ RIGHT 10
→ exact center NG
→ 5-rune segment
→ active phase pattern X-X-I-X-X
→ WEATHER
```

Volume 1 explicitly states that the next segment contains **5 runes** and gives the active five-position key pattern `X-X-I-X-X`.

The PDF body text does **not** print those five ciphertext runes as a standalone textual sequence; their position is shown visually in the matrix. For strict source fidelity, this Markdown edition therefore does not invent or import a ciphertext transcription from later research.

The proposed plaintext for this stage is:

> **WEATHER**

---

## 9. Why the J → OE sequence matters in the proposal

Volume 1 emphasizes that the first two consecutive mirrored nodes have center runes:

`J`

and:

`OE`

and states that, in the Gematria Primus values being used, these are the only two values whose totient equals:

`10 = I`

So the sequence is:

`J → φ(J)=10=I`

followed by:

`OE → φ(OE)=10=I`

This repeated reduction to `I` is treated as a structural connection between the first two stages.

Volume 1 also notes that the next key begins at the exact center `NG` of the entire 27×27 matrix.

---

# Part IV — Möbius key-phase rule

## 10. The phase problem

A three-rune key can be repeated in three cyclic phases.

For a key:

`k1-k2-k3`

the possible starts are:

- phase 0: `k1-k2-k3...`
- phase 1: `k2-k3-k1...`
- phase 2: `k3-k1-k2...`

Volume 1 proposes a direct rule for selecting the phase.

---

## 11. Phase formula

The proposed rule is:

`p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3`

Equivalent compact form:

**Phase = Σ μ(φ(Kᵢ)) mod 3**

Interpretation:

- `p = 0` → start from rune 1;
- `p = 1` → start from rune 2;
- `p = 2` → start from rune 3.

This rule is intended to make key rotation deterministic rather than manually selected.

---

## 12. Phase of AE-I-EA

For:

**AE-I-EA**

Volume 1 gives:

`φ(K) = 20, 4, 12`

Then:

`μ = 0, 0, 0`

Therefore:

`Σμ = 0`

and:

`p = 0`

So the active key remains:

**AE-I-EA**

This matches the phase used for:

> **AS I GO THE**

---

## 13. Phase of X-I-X

For:

**X-I-X**

Volume 1 gives:

`φ(K) = 6, 4, 6`

Then:

`μ = +1, 0, +1`

Therefore:

`Σμ = 2`

and:

`p = 2`

So the active cyclic key begins from the third rune:

`X-I-X → X-X-I`

The active repeating key is therefore:

**X-X-I**

This is the phase used in the proposed decryption of:

> **WEATHER**

Volume 1 also notes a visual clue: directly above the WEATHER ciphertext are the three runes:

**W-EA-TH**

and interprets those three runes as a possible hint toward a three-position phase-selection rule.

---

# Part V — Stage 3: TURNS

## 14. Transition after WEATHER

Volume 1 states that WEATHER ends on `E` and visually enters a structure described as:

**EA-G-AE**

However, the source explicitly treats the `G` route as a false path and instead continues from:

**A**

This next point is:

**A(14,19)**

and is treated as a crossroads.

The two previously derived control values are:

`I = 10`

and:

`φ(I) = 4`

These are reused as movement values.

---

## 15. A(14,19) as a crossroads

From:

**A(14,19)**

Volume 1 gives two movements:

`UP 10 → NG`

and:

`RIGHT 4 → NG`

This defines the route:

**UP → RIGHT**

The right-hand NG is:

**NG(14,23)**

Volume 1 notes that this NG has A exactly four cells away on both its left and right:

`A(14,19) --4-- NG(14,23) --4-- A(14,27)`

This is presented as a structural reason to treat that NG as important.

---

## 16. Deriving H-NG-C

From the right-hand:

**NG(14,23)**

move vertically by the already established value `10`.

Volume 1 gives:

`UP 10 → H(4,23)`

and:

`DOWN 10 → C(24,23)`

This forms the vertical three-rune structure:

**H-NG-C**

In Volume 1, H-NG-C is not presented as an independently chosen key. It is the **vertical axis of the same cross** whose horizontal axis contains:

`A(14,19) --4-- NG(14,23) --4-- A(14,27)`

The vertical axis is:

```text
H(4,23)
   |
  10
   |
NG(14,23)
   |
  10
   |
C(24,23)
```

Its totient signature is:

`4-12-4`

because:

- `φ(H) = 4`
- `φ(NG) = 12`
- `φ(C) = 4`

Volume 1 compares this with the mirrored structure:

**I-NG-I**

which has the same totient signature:

**4-12-4**

The key H-NG-C is therefore treated as part of the same structural family.

---

## 17. Ciphertext for TURNS

Reading upward from A gives:

**A-OE-N-B-W**

The repeated key is:

**H-NG-C-H-NG**

Using modular subtraction, Volume 1 gives:

```text
ciphertext: A-OE-N-B-W
key:        H-NG-C-H-NG
operation:  P = C - K mod 29
result:     T-U-R-N-S
```

Result:

> **TURNS**

So the third stage is:

`A(14,19)`
`→ UP 10`
`→ NG`
`→ RIGHT 4`
`→ NG(14,23)`
`→ vertical H-NG-C`
`→ read upward from A`
`→ A-OE-N-B-W`
`→ subtract H-NG-C-H-NG`
`→ TURNS`

### Derived consistency note

Using the phase rule already stated in Volume 1:

`φ(H-NG-C) = 4,12,4`

and:

`μ(4)=0, μ(12)=0, μ(4)=0`

so:

`p = 0`

This is consistent with using H-NG-C without rotation.

This phase calculation is a direct consequence of the stated phase rule; Volume 1 itself presents the H-NG-C subtraction directly.

---

# Part VI — Stage 4: COLD

## 18. The next value: φ(NG)=12

The important central value of the H-NG-C structure is:

`NG = 21`

Therefore:

**φ(NG) = φ(21) = 12**

Volume 1 uses this single value in two directions from the A crossroads.

From:

**A(14,19)**

move:

**DOWN 12**

and:

**LEFT 12**

These two branches point to two different parts of the next decryption stage.

---

## 19. Two 12-step branches

### Branch A — key structure

Exactly 12 cells down from A lands on the center of:

**H-TH-H**

Because the origin is `A(14,19)`, the center reached by `DOWN 12` is **(26,19)**. This coordinate is a direct arithmetic consequence of the stated move; Volume 1 describes the destination structurally as the center of H-TH-H.

Volume 1 describes H-TH-H as the natural next mirrored key point in the lower region and notes that its vertical occurrence lies entirely within A's column.

### Branch B — ciphertext start

Exactly 12 cells left from A lands on:

**G(14,7)**

This is the starting point of the ciphertext for the next word.

So:

`φ(NG)=12`

simultaneously identifies:

1. the structure that generates the next key;
2. the starting point of the next ciphertext.

This dual use of the same value is one of the strongest structural features claimed in Volume 1.

---

## 20. Compiling H-TH-H

Volume 1 states the node compilation rule:

`K = (a, φ(b), c)`

Apply it to:

**H-TH-H**

The center rune is:

`TH = 2`

and:

`φ(2) = 1`

Gematria Primus value 1 is:

`U`

Therefore:

`H-TH-H → H-U-H`

The generated three-rune key is:

**H-U-H**

---

## 21. Möbius phase of H-U-H

Apply the phase formula:

`p = [μ(φ(k1)) + μ(φ(k2)) + μ(φ(k3))] mod 3`

For:

**H-U-H**

Volume 1 gives:

`p = [μ(4) + μ(1) + μ(4)] mod 3`

Then:

`= [0 + 1 + 0] mod 3`

Therefore:

`p = 1`

So the active cyclic key begins from rune 2:

`H-U-H → U-H-H`

The active repeating key is:

**U-H-H**

---

## 22. Ciphertext for COLD

Volume 1 gives the ciphertext:

**G-J-EA-A**

The active repeating key is:

**U-H-H-U**

Apply:

`P = C - K mod 29`

So:

```text
ciphertext: G-J-EA-A
key:        U-H-H-U
operation:  P = C - K mod 29
result:     C-O-L-D
```


Result:

> **COLD**

---

# Part VII — Current recovered sequence

## 23. Full Volume 1 plaintext

The proposed plaintext recovered in this Volume is:

> **AS I GO, THE WEATHER TURNS COLD**

The route can be summarized as:

```text
AE-J-EA
→ AE-I-EA
→ RIGHT 14
→ AS I GO THE
→ X-OE-X
→ X-I-X
→ phase 2 = X-X-I
→ RIGHT 10
→ central NG
→ WEATHER
→ A(14,19) crossroads
→ reuse 10 and 4
→ H-NG-C
→ TURNS
→ φ(NG)=12
→ two 12-step branches
   ├─ DOWN 12 → H-TH-H → H-U-H → phase 1 = U-H-H
   └─ LEFT 12 → G(14,7), ciphertext start
→ COLD
```

---

# Part VIII — Structured stage summary

## 24. Human-readable stage table

| Stage | Structural source | Transform / control | Movement | Key / phase | Ciphertext explicitly transcribed in Volume 1 | Proposed plaintext |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | AE-J-EA | `φ(J=11)=10=I`; `φ(I)=4`; `10+4=14` | RIGHT 14 | AE-I-EA; phase 0 | L-AE-N-TH-P-U-X | **AS I GO THE** |
| 2 | X-OE-X | `φ(OE)=10=I` | RIGHT 10 → central NG | X-I-X; phase 2 → X-X-I | Not printed as a standalone sequence in the PDF body text | **WEATHER** |
| 3 | A crossroads → H-NG-C | reuse `10` and `4`; H-NG-C signature `4-12-4` | UP 10, RIGHT 4; read upward | H-NG-C; phase 0 is consistent with the stated rule | A-OE-N-B-W | **TURNS** |
| 4 | `φ(NG=21)=12` → H-TH-H | H-TH-H → H-U-H | DOWN 12 to key node; LEFT 12 to G(14,7) | H-U-H; phase 1 → U-H-H | G-J-EA-A | **COLD** |

## 25. Machine-readable compact trace

```text
STAGE 1
node: AE-J-EA
center: J=11
transform: phi(11)=10=I
compiled_key: AE-I-EA
phase: 0
movement_basis: 10 + phi(10)=10+4=14
movement: RIGHT 14
ciphertext: L-AE-N-TH-P-U-X
active_key: AE-I-EA-AE-I-EA-AE
operation: P=C-K mod 29
plaintext: AS I GO THE
next_structure: X-OE-X

STAGE 2
node: X-OE-X
center: OE
transform: phi(OE)=10=I
compiled_key: X-I-X
phase_formula: sum(mu(phi(K_i))) mod 3
phase: 2
active_key_cycle: X-X-I
movement: RIGHT 10
destination: exact center NG of 27x27 matrix
ciphertext_length: 5 runes
plaintext: WEATHER
next_point: A(14,19) via the E/A boundary and visual EA-G-AE connection

STAGE 3
origin: A(14,19)
control_values: 10 and 4
movement_1: UP 10 -> NG
movement_2: RIGHT 4 -> NG(14,23)
derived_vertical_node: H(4,23)-NG(14,23)-C(24,23)
key: H-NG-C
totient_signature: 4-12-4
phase: 0 [derived from stated phase rule]
ciphertext_direction: upward from A
ciphertext: A-OE-N-B-W
active_key: H-NG-C-H-NG
operation: P=C-K mod 29
plaintext: TURNS

STAGE 4
control_value: phi(NG=21)=12
branch_1: DOWN 12 from A -> center of H-TH-H
branch_2: LEFT 12 from A -> G(14,7), next ciphertext start
node: H-TH-H
node_compilation: K=(a,phi(b),c)
transform: phi(TH=2)=1=U
compiled_key: H-U-H
phase: 1
active_key_cycle: U-H-H
ciphertext: G-J-EA-A
active_key: U-H-H-U
operation: P=C-K mod 29
plaintext: COLD

CURRENT_RESULT
plaintext: AS I GO, THE WEATHER TURNS COLD
words: 7
runes: 21
zero_based_GP_index_sum: 233
COLD_index_sum: 51
233_prime_index: 51
matrix_center_rune: NG
NG_value: 21
fibonacci_links: F7=13; F13=233
```

---

# Part IX — Numerical structure and proposed checks

## 26. Seven words and twenty-one runes

The phrase:

**AS I GO THE WEATHER TURNS COLD**

contains:

- **7 words**
- **21 runes**

Therefore:

`21 = 3 × 7`

Volume 1 notes that:

`NG = 21`

and NG occupies the center of the 27×27 matrix.

---

## 27. Gematria Primus sum: 233

Using the 0-based Gematria Primus indices used in Volume 1, the total plaintext sum is:

**233**

The source gives the complete index sum as:

`A(24) + S(15) + I(10) + G(6) + O(3) + TH(2) + E(18) + W(7) + EA(28) + TH(2) + E(18) + R(4) + T(16) + U(1) + R(4) + N(9) + S(15) + C(5) + O(3) + L(20) + D(23) = 233`

The word:

**COLD**

has an index sum of:

**51**

Volume 1 notes:

**233 is the 51st prime number**

So the proposed numerical relation is:

`COLD sum = 51`
`→ 51st prime = 233`
`→ full plaintext index sum = 233`

---

## 28. Fibonacci relation

Volume 1 also notes:

`F₇ = 13`

and:

`F₁₃ = 233`

giving:

**7 → 13 → 233**

The source treats the repeated appearance of 7, 21, 51, and 233 as a possible consistency pattern connecting:

- word count;
- rune count;
- Gematria Primus indices;
- the central NG;
- prime numbers;
- Fibonacci numbers.

These relationships are **supporting observations**, not independent proof of the plaintext.

---

# Part X — Column structure

## 29. Columns 19 and 7

Volume 1 identifies column 19 as structurally important because several features are anchored to it, including:

- the A crossroads;
- I-NG-I;
- H-TH-H.

It also notes:

- `W` has zero-based GP index `7`;
- `W` has prime value `19`;
- the difference is:

`19 - 7 = 12`

and:

`12 = φ(NG)`

So:

**19 − 7 = 12 = φ(NG)**

Geometrically:

- **TURNS** ends on W in column 19;
- **COLD** begins in column 7.

Volume 1 therefore interprets `φ(NG)=12` as linking the transition:

**19 → 7**

both numerically and geometrically.

---

# Part XI — Transition-cell observations

## 30. Final cells as possible hints

Volume 1 proposes that the final ciphertext cell of a stage may hint at the next step.

### After AS I GO THE

The segment ends on:

`X`

which opens the adjacent mirror:

**X-OE-X**

### After WEATHER

WEATHER ends at the E/A boundary, visually leading toward:

**A(14,19)**

the crossroads used for the next stage.

### After TURNS

TURNS ends on:

`W`

in column 19.

This is linked to the proposed:

**19 → 7**

transition through:

`φ(NG)=12`

### After COLD

COLD ends on:

`A(11,7)`

and Volume 1 notes:

`φ(A)=8=H`

as an additional hint toward `H`, reinforcing the continuation through the H-TH-H structure.

These are interpretive transition cues in Volume 1 rather than independent decryption rules.

---

# Part XII — Additional observations in Volume 1

## 31. Initial ROAD / PATH / WAY construction

Before the main 27×27 derivation, Volume 1 records:

`ROAD = R(4) + O(3) + A(24) + D(23) = 54 → 54 mod 29 = 25 → AE`

`PATH = P(13) + A(24) + TH(2) = 39 → 39 mod 29 = 10 → I`

`WAY = W(7) + A(24) + Y(26) = 57 → 57 mod 29 = 28 → EA`

This gives:

**AE-I-EA**

Volume 1 notes that the same key appears in the 3×3 matrix.

This material is presented in the source before the technical reconstruction beginning with the 729-rune matrix.

---

## 32. GEB / Recursive Transition Network context

Volume 1 opens with pages from *Gödel, Escher, Bach* discussing **Recursive Transition Networks (RTNs)** and later compares the map-like route to a system in which one state leads to another through structured transitions.

In Volume 1, this functions as conceptual context rather than as a required mathematical step in the decryption chain.

The core Volume 1 plaintext derivation described above does not require an RTN formalism to execute.

---

## 33. Separators and dots

Volume 1 considers the possibility that apparent separators between words are not ordinary linguistic divisions but may act as:

- markers;
- movement clues;
- structural hints;
- or a checksum-like layer.

The source also notes visual patterns in the dots, including diagonals and vertical lines.

These ideas are exploratory and are not required to reproduce the core four-stage plaintext derivation above.

---

## 34. H-TH-H uniqueness observation

Below the A crossroads, Volume 1 identifies:

**H-TH-H**

and describes it as the only mirrored structure in that lower area both vertically and horizontally.

The vertical instance is treated as especially significant because it lies entirely within A's column.

This is used as a structural argument for choosing H-TH-H as the next key-generating node.

---

## 35. WAY through A

Volume 1 also notes that:

**WAY**

passes through the highly connected A intersection with A at its center.

This is treated as a possible thematic hint that the A position functions as a crossroads or path-selection point.

It is not required for the modular decryption itself.

---

# Part XIII — Statistical and thematic claims

## 36. Random-window estimate

Volume 1 reports a test in which random shuffling produced the relevant type of window next to the central NG with an estimated probability of:

**0.0041%**

or approximately:

**1 in 24,000**

This is an author-reported estimate from Volume 1 and should not be treated as an independently validated statistical result without reproducing the exact randomization test and selection criteria.

---

## 37. J → OE estimate

Volume 1 gives a simple estimate for observing the consecutive centers J then OE:

`1 / 29² = 1 / 841`

or approximately:

**0.119%**

The source explicitly presents this as only a simple estimate before accounting for other observed constraints.

Because the structures were discovered within a larger search process, this number should be read as a heuristic observation rather than a complete multiple-comparisons analysis.

---

## 38. DIVINITY WITHIN / A CROSSROADS

Near the end of Volume 1, the source records:

**DIVINITY WITHIN = 491**

and:

**"A" CROSSROADS = 491**

and interprets the equality as possible wordplay connected to:

**FIND THE DIVINITY WITHIN AND EMERGE**

This is a secondary thematic observation and is not required for the core decryption chain.

---

## 39. Prime 19 observation

Volume 1 states that a 2014 `message.txt.asc` hidden-space sequence encoded primes from 2 to 37 except:

**19**

and connects this observation to the proposed importance of column 19 and the:

**19 → 7**

transition.

This is presented as a possible external thematic connection, not as a required decryption step.

---

## 40. Additional numerical observations

Volume 1 also records:

- the prime-value sum associated with **AS I GO THE** as `301`, noted for its resemblance to `3301`;
- separator counts across the seven words summing to `14`.

These are exploratory observations in the source and are not part of the core deterministic chain used to produce the current plaintext.

---

# Part XIV — Reproducible core versus supporting observations

## 41. Core derivation

The technically central chain in Volume 1 is:

1. count 729 runes;
2. form the 27×27 matrix;
3. identify AE-J-EA;
4. compile AE-I-EA through `φ(J)=10=I`;
5. derive RIGHT 14 from `10 + φ(10)`;
6. decrypt `L-AE-N-TH-P-U-X` to **AS I GO THE**;
7. use final X to enter X-OE-X;
8. compile X-I-X through `φ(OE)=10=I`;
9. calculate Möbius phase 2 → X-X-I;
10. move RIGHT 10 to central NG;
11. obtain **WEATHER**;
12. continue to A(14,19);
13. reuse 10 and 4 as UP and RIGHT movements;
14. derive H-NG-C;
15. decrypt upward ciphertext to **TURNS**;
16. calculate `φ(NG)=12`;
17. use 12 in two branches: key node and ciphertext start;
18. compile H-TH-H → H-U-H;
19. calculate Möbius phase 1 → U-H-H;
20. decrypt G-J-EA-A to **COLD**.

Result:

> **AS I GO, THE WEATHER TURNS COLD**

---

## 42. Supporting observations

The following observations support or motivate the proposal but are not individually necessary to execute the core chain:

- symmetry of the matrix;
- separator alignment;
- W-EA-TH as a phase hint;
- EA-G-AE as a visual continuation clue;
- uniqueness claims about specific mirrored structures;
- 233 / 51 / Fibonacci relationships;
- column 19 and column 7 relationship;
- final-cell transition hints;
- ROAD / PATH / WAY → AE-I-EA;
- RTN / GEB context;
- DIVINITY WITHIN = 491 and "A" CROSSROADS = 491;
- prime 19 observations;
- 301 and separator-sum 14 observations;
- author-reported probability estimates.

Keeping these separate from the core derivation makes it easier to test which parts of the proposal are reproducible and which parts are interpretive or confirmatory.

---

# Part XV — Reproduction aids

## 43. Minimal pseudocode derived from the stated formulas

The following pseudocode does **not** add a new cryptographic rule. It only expresses the formulas already stated in Volume 1 in machine-readable form.

```text
compile_node(a, b, c):
    return (a, rune_for_index(phi(index(b))), c)

phase(key):
    s = 0
    for rune in key:
        s += mobius(phi(index(rune)))
    return s mod 3

rotate_key(key, p):
    # p=0 -> rune 1, p=1 -> rune 2, p=2 -> rune 3
    return cyclic_rotation_left(key, p)

decrypt_mod29(ciphertext, active_key):
    for each position i:
        plaintext_index[i] = (index(ciphertext[i]) - index(active_key[i])) mod 29
    return runes_for_indices(plaintext_index)
```

Movement is intentionally **not** reduced to one universal pseudocode function here, because Volume 1 uses locally derived values and structural clues rather than stating one global movement equation.

## 44. Independent reproduction checklist

A reader attempting to reproduce Volume 1 should verify these claims separately:

1. The source transcription of Liber Primus pages 0–2 contains exactly **729 rune tokens**.
2. Row-wise placement creates a **27×27** matrix with the same coordinates as the PDF.
3. The stated nodes and coordinates exist in that matrix.
4. `AE-J-EA → AE-I-EA` follows from `φ(11)=10`.
5. RIGHT 14 reaches the stated seven-rune ciphertext.
6. Mod-29 subtraction gives `A-S-I-G-O-TH-E`.
7. The final X is adjacent to X-OE-X.
8. `φ(OE)=10` and RIGHT 10 reaches central NG.
9. The Möbius phase calculations for AE-I-EA, X-I-X, and H-U-H reproduce phases 0, 2, and 1.
10. A(14,19), NG(14,23), H(4,23), and C(24,23) match the matrix.
11. Reading upward from A gives `A-OE-N-B-W`, and subtraction by H-NG-C-H-NG gives TURNS.
12. `φ(NG=21)=12` produces the two stated 12-step branches.
13. H-TH-H compiles to H-U-H through `φ(TH=2)=1=U`.
14. G-J-EA-A minus U-H-H-U gives COLD.
15. The 21 plaintext rune indices sum to **233** and COLD sums to **51**.
16. Any probability or uniqueness claim should be reproduced with its exact search space and selection criteria before being treated as statistical evidence.

### Source-data limitation

The PDF contains the 27×27 matrix primarily as images rather than as a complete plain-text 729-token transcription. Therefore, this Markdown edition describes the route and coordinates but does not by itself provide the complete raw matrix dataset.

For maximum reproducibility in a future repository revision, the strongest additional artifact would be a separate machine-readable file containing the exact 729-rune transcription and/or the full 27×27 matrix, for example:

`liber-primus-0-2-729-runes.txt`

or:

`liber-primus-0-2-27x27-matrix.tsv`

That would allow an independent script or AI system to verify coordinates directly rather than relying on the PDF image.

---

# Part XVI — Current status

## 45. Status of the proposal

This document records the state of **SOLUTION 0-2 — Volume 1**.

Current proposed plaintext:

> **AS I GO, THE WEATHER TURNS COLD**

This result should be treated as:

- a proposed cryptanalytic construction;
- an ongoing research hypothesis;
- a reproducible sequence of stated operations that can be independently checked;
- **not** an officially verified Cicada 3301 solution.

The most important next test is whether the same structural framework can continue beyond COLD without introducing arbitrary rules.

---

## 46. Terminology and aliases

Relevant terms for this Volume include:

**Cicada 3301, Liber Primus, Liber Primus pages 0–2, Liber Primus decryption, Liber Primus solution, 729 runes, 27×27 rune matrix, 27x27 grid, three-rune nodes, mirrored rune structures, Gematria Primus, Euler's totient function, Euler totient, totient navigation, Möbius function, Möbius key phase, mod 29, modular subtraction, AE-J-EA, AE-I-EA, X-OE-X, X-I-X, I-NG-I, H-NG-C, H-TH-H, H-U-H, A crossroads, AS I GO THE WEATHER TURNS COLD, Fibonacci 233, Recursive Transition Network, RTN.**

---

## 47. Companion source

This Markdown document is a structured technical edition of the accompanying PDF:

**SOLUTION 0-2 volume 1**

The PDF contains the original visual matrices, highlighted routes, screenshots, and diagrams. This Markdown edition focuses on searchable text, formulas, coordinates, transition logic, source fidelity, reproducibility, and explicit separation between core derivation and secondary observations.

## Machine-readable source data

The exact 729-rune transcription used for the 27×27 matrix is included in this repository:

[liber-primus-0-2-729-runes.txt](./liber-primus-0-2-729-runes.txt)

It contains exactly 27 rows × 27 rune tokens = 729 runes.
