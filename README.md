# Cicada 3301 Liber Primus 0–2 — 27×27 Rune Matrix Decryption

This repository documents a **proposed cryptanalytic framework for Cicada 3301's Liber Primus, pages 0–2**.

The central observation is:

> **Liber Primus pages 0–2 contain exactly 729 rune tokens, and 729 = 27 × 27.**

The complete rune sequence can therefore be written **left-to-right, row-by-row** as a **27×27 matrix** without adding or removing runes.

![Liber Primus 27x27 rune matrix](./liber-primus-27x27-matrix.png)

The working hypothesis is that this square is not only a visual rearrangement of a linear ciphertext. It may also function as a **spatial map** in which mirrored or structured three-rune patterns act as nodes, key sources, and navigation points.

The proposed framework is:

> **729 runes → 27×27 matrix → three-rune structures → Euler totient φ → local movement → Möbius μ key phase → Gematria Primus subtraction mod 29 → plaintext → next structure**

Current Volume 1 result:

> ## **AS I GO, THE WEATHER TURNS COLD**

**Status:** proposed, reproducible research; **not an officially verified Cicada 3301 solution**.

---

## Quick start / reproducibility

If you want to inspect or test the proposal without reading the full PDF first, start here:

| File | Purpose |
| --- | --- |
| [`SOLUTION-0-2-volume-1.md`](./SOLUTION-0-2-volume-1.md) | Full technical, machine-readable explanation of Volume 1 |
| [`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt) | Raw 729-rune dataset arranged as 27 rows × 27 tokens |
| [`verify-volume-1.py`](./verify-volume-1.py) | Standard-library Python verifier for the encoded core checks |
| [`SOLUTION 0-2 volume 1.pdf`](./SOLUTION%200-2%20volume%201.pdf) | Original visual research document with highlighted routes and matrix diagrams |

Run the verifier from the repository root:

```bash
python3 verify-volume-1.py
```

No third-party Python packages are required.

The verifier checks the **encoded, reproducible core** of Volume 1: dataset shape, matrix coordinates, node locations, Euler-totient transforms, Möbius phases, key streams, mod-29 subtraction, proposed plaintext segments, and several numerical consistency checks.

A successful run means that the stated operations reproduce the stated results from the repository dataset. It **does not** by itself prove that the proposed plaintext is the intended Cicada 3301 solution.

---

## Repository map

### Technical research

- [`SOLUTION-0-2-volume-1.md`](./SOLUTION-0-2-volume-1.md) — technical Markdown edition
- [`SOLUTION 0-2 volume 1.pdf`](./SOLUTION%200-2%20volume%201.pdf) — original visual Volume 1
- [`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt) — machine-readable source data
- [`verify-volume-1.py`](./verify-volume-1.py) — reproducibility verifier

### Conceptual interpretation

- [`WHAT-IS-LIBER-PRIMUS.md`](./WHAT-IS-LIBER-PRIMUS.md) — conceptual Markdown version

### Visual reference

- [`liber-primus-27x27-matrix.png`](./liber-primus-27x27-matrix.png) — 27×27 matrix visualization

---

## Evidence levels used in this repository

To avoid mixing arithmetic with interpretation, the project separates claims into three levels.

### 1. Reproducible core

These claims can be checked directly from the 729-rune dataset and the explicit formulas or coordinates in Volume 1.

Examples:

- 729 rune tokens form a 27×27 matrix.
- The geometric center is `(14,14)`.
- The center rune is `NG`.
- The stated structures occur at the stated coordinates.
- `φ(J=11)=10=I`.
- `φ(OE=22)=10=I`.
- The Möbius phase rule produces the stated key rotations.
- The listed ciphertext/key pairs reproduce:
  - **AS I GO THE**
  - **WEATHER**
  - **TURNS**
  - **COLD**
- The full proposed phrase contains 7 words and 21 rune tokens.
- Its 0-based Gematria Primus index sum is 233.

These are the main targets of [`verify-volume-1.py`](./verify-volume-1.py).

### 2. Supporting observations

These are exact or checkable relationships that may support the construction but do not independently prove the plaintext.

Examples include:

- `COLD` has a 0-based GP index sum of `51`.
- `233` is the 51st prime.
- `F₇ = 13` and `F₁₃ = 233`.
- `19 − 7 = 12 = φ(NG)`.
- `NG = 21` and occupies the center of the 27×27 matrix.

These are treated as **consistency checks**, not as standalone decryption rules.

### 3. Interpretive / exploratory hypotheses

These include broader architectural or thematic ideas, such as:

- the matrix behaving like a labyrinth or state-transition system;
- a possible connection to a **Recursive Transition Network (RTN)**;
- separators or visual features acting as instructions;
- thematic wordplay and numerical references.

These ideas are deliberately kept separate from the deterministic arithmetic checks.

---

# Core method

## 1. Build the 27×27 matrix

Pages 0–2 contain exactly:

```text
729 rune tokens
```

and:

```text
729 = 27 × 27
```

The rune sequence is placed in original order:

```text
left to right
→ next row
→ left to right
→ next row
...
```

This creates a coordinate system with rows and columns numbered `1..27`.

The raw matrix data used by this repository is available in:

[`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt)

Each line contains exactly 27 rune tokens.

Multi-character forms such as `AE`, `OE`, `NG`, `TH`, `U/V`, `C/K`, `S/Z`, and `IA/O` represent **single rune tokens**.

---

## 2. Three-rune structures

Important structures encountered in Volume 1 include:

```text
AE-J-EA
X-OE-X
I-NG-I
H-NG-C/K
H-TH-H
```

The proposal treats these structures as functional nodes rather than merely visual coincidences.

A recurring node transformation is:

```text
K = (a, φ(b), c)
```

where the center rune value `b` is transformed by Euler's totient function.

---

## 3. Stage 1 — AS I GO THE

First node:

```text
AE-J-EA
```

Using 0-based Gematria Primus values:

```text
J = 11
φ(11) = 10
10 = I
```

Therefore:

```text
AE-J-EA
→ AE-I-EA
```

This gives the three-rune key:

```text
AE-I-EA
```

The next derived value is:

```text
φ(I=10) = 4
10 + 4 = 14
```

Volume 1 uses:

```text
RIGHT 14
```

The ciphertext is:

```text
L-AE-N-TH-P-U/V-X
```

Repeated key:

```text
AE-I-EA-AE-I-EA-AE
```

Decryption rule:

```text
P = C - K mod 29
```

Result:

> **AS I GO THE**

---

## 4. Stage 2 — WEATHER

The final `X` of the previous ciphertext opens the adjacent structure:

```text
X-OE-X
```

Its center transforms as:

```text
φ(OE=22) = 10 = I
```

giving:

```text
X-OE-X
→ X-I-X
```

The proposed phase rule is:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

For:

```text
X-I-X
```

the result is:

```text
p = 2
```

so the active cycle becomes:

```text
X-X-I
```

A movement of:

```text
RIGHT 10
```

from the stated starting cell reaches:

```text
(14,14) = NG
```

the exact center of the 27×27 matrix.

The five matrix tokens used at this stage are:

```text
NG-P-EO-O-E
```

with active key stream:

```text
X-X-I-X-X
```

and mod-29 subtraction gives:

> **WEATHER**

---

## 5. Stage 3 — TURNS

After WEATHER, the route reaches:

```text
A(14,19)
```

which functions as a crossroads in Volume 1.

The previously derived values are reused locally:

```text
I = 10
φ(I) = 4
```

From `A(14,19)`:

```text
UP 10    → NG(4,19)
RIGHT 4  → NG(14,23)
```

Around the right-hand NG:

```text
UP 10   → H(4,23)
DOWN 10 → C/K(24,23)
```

forming:

```text
H-NG-C/K
```

Its totient signature is:

```text
4-12-4
```

matching the signature of:

```text
I-NG-I
```

Reading upward from `A(14,19)` gives:

```text
A-OE-N-B-W
```

Using:

```text
H-NG-C/K-H-NG
```

as the repeating key gives:

> **TURNS**

---

## 6. Stage 4 — COLD

The next control value comes from:

```text
NG = 21
φ(21) = 12
```

From `A(14,19)`, the same value points in two directions:

```text
DOWN 12 → center of H-TH-H
LEFT 12 → G(14,7)
```

The first branch identifies the next key-generating structure.

The second branch identifies the next ciphertext start.

For:

```text
H-TH-H
```

the center transforms as:

```text
TH = 2
φ(2) = 1
1 = U/V
```

therefore:

```text
H-TH-H
→ H-U/V-H
```

The Möbius phase formula gives:

```text
p = 1
```

so the active cycle becomes:

```text
U/V-H-H
```

The ciphertext read upward from `G(14,7)` is:

```text
G-J-EA-A
```

Active key stream:

```text
U/V-H-H-U/V
```

Therefore:

```text
G-J-EA-A
-
U/V-H-H-U/V
=
C/K-O-L-D
```

with the intended English reading:

> **COLD**

---

# Current route

The current Volume 1 chain can be summarized as:

```text
729 rune tokens
↓
27×27 matrix
↓
AE-J-EA
↓
φ(J)=10=I
↓
AE-I-EA
↓
RIGHT 14
↓
AS I GO THE
↓
X-OE-X
↓
φ(OE)=10=I
↓
X-I-X
↓
Möbius phase 2
↓
RIGHT 10
↓
central NG
↓
WEATHER
↓
A(14,19) crossroads
↓
10 / 4 local movements
↓
H-NG-C/K
↓
TURNS
↓
φ(NG)=12
↓
H-TH-H + G(14,7)
↓
H-U/V-H
↓
Möbius phase 1
↓
COLD
```

Current proposed plaintext:

> # **AS I GO, THE WEATHER TURNS COLD**

---

## Numerical consistency checks

The proposed phrase contains:

```text
7 words
21 rune tokens
```

so:

```text
21 = 3 × 7
```

Using 0-based Gematria Primus indices:

```text
full plaintext sum = 233
COLD sum = 51
```

and:

```text
51st prime = 233
```

Fibonacci:

```text
F₇  = 13
F₁₃ = 233
```

Another geometric/numerical relation in Volume 1 is:

```text
TURNS ends in column 19
COLD begins in column 7

19 - 7 = 12
φ(NG=21) = 12
```

These relationships are documented as **supporting checks**, not as independent proof of the plaintext.

---

## Raw data and provenance

The repository includes the exact 729-token transcription used to construct the matrix:

[`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt)

The verifier normalizes this file as 27 lines of 27 space-separated tokens and checks its expected SHA-256 fingerprint before executing route-level verification.

The repository transcription was also cross-checked during preparation against the public LiberPrayground `p0-2.txt` transcription:

https://github.com/relikd/LiberPrayground/blob/main/pages/p0-2.txt

This external transcription is a reproducibility reference, not an official Cicada 3301 endorsement of this research.

---

## What the verifier proves — and what it does not

[`verify-volume-1.py`](./verify-volume-1.py) is designed to answer a narrow question:

> **Given the repository's fixed 729-rune dataset and the explicit Volume 1 operations, do the stated coordinates, arithmetic, keys, phases, and plaintext outputs reproduce correctly?**

It checks that question automatically.

It does **not** claim to prove:

- that the initial node selection is uniquely forced;
- that every local movement rule is generated by one universal equation;
- that the plaintext has been authenticated by Cicada 3301;
- that post-hoc numerical observations independently prove the plaintext;
- that the RTN interpretation is cryptographically necessary;
- that exploratory probability estimates constitute a complete statistical model.

This distinction is intentional.

---

## Main open question

The most important unresolved issue is not whether the encoded arithmetic reproduces — it does under the stated route.

The stronger question is:

> **Can the same framework determine a new step or plaintext segment prospectively, before the result is known, without adding an arbitrary rule after seeing the output?**

A successful out-of-sample continuation would provide much stronger evidence for the framework.

Conversely, if continuation consistently requires unconstrained new choices, that would weaken the hypothesis.

---

## Recursive Transition Network hypothesis

A broader conceptual interpretation is that the 27×27 map may behave somewhat like a **Recursive Transition Network (RTN)**:

```text
node
→ transition
→ operation
→ new state
→ continuation
```

The proposed matrix route behaves similarly:

```text
structure
→ mathematical operation
→ movement
→ decryption
→ next structure
```

This is an **architectural hypothesis**, not a required step in the Volume 1 arithmetic.

For the broader interpretation, see:

[`WHAT-IS-LIBER-PRIMUS.md`](./WHAT-IS-LIBER-PRIMUS.md)

---

## Research status

This repository contains **ongoing, proposed cryptanalytic research**.

The goal of publishing it publicly is to make the method:

> **readable, reproducible, testable, criticizable, falsifiable, improvable, and continuable by other researchers.**

If you find:

- a transcription error;
- a coordinate error;
- an arithmetic error;
- a hidden degree of freedom;
- a stronger alternative explanation;
- a statistical problem;
- or an independently reproducible continuation,

please open a GitHub Issue.

---

## Related terminology

Cicada 3301 · Liber Primus · Liber Primus 0–2 · cryptanalysis · Gematria Primus · 729 runes · 27×27 rune matrix · three-rune nodes · mirrored rune structures · Euler's totient function · Euler totient · totient navigation · Möbius function · Möbius key phase · modular arithmetic · mod 29 · Recursive Transition Network · RTN · Fibonacci 233 · AS I GO THE WEATHER TURNS COLD
