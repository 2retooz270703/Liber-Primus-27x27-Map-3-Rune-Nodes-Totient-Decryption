# The Red Heading of Liber Primus: `SEQUENDI RATIO`

**A combined investigation of two candidate keys in the 27×27 rune matrix**  
*Liber Primus, LP2, pages 0–2 · Research consolidated 30 October 2026*

> [!IMPORTANT]
> **Reproducible candidate, not a confirmed Cicada 3301 solution.**  
> The two red-heading words decrypt exactly, under two different geometrically sourced keys, to the **literal rune sequence `SECUENDI RATIO`**. Reading its third rune, `C/K`, as the Latin letter **Q** gives the proposed title **`SEQUENDI RATIO`**, meaning approximately **“a method of following.”** The arithmetic and the specified matrix geometry are verifiable; the choice of keys, reading directions, and Latin spelling are not yet consequences of one proven cipher rule.

## 1. Result at a glance

The complete red heading, including its original word division, is:

```text
Runes:           ᛋᚻᛖᚩᚷᛗᛡᚠ  •  ᛋᚣᛖᛝᚳ
Transliteration: S H E O G M IA F   •  S Y E NG C
Length:                  8         +       5        = 13 runes
```

The 13 runes occupy **row 1, columns 1–13** of the project's 27×27 matrix. The separator is not counted as a cell. Neither word is altered or replaced before decryption.

| | First word | Second word |
|---|---|---|
| Original ciphertext | `S–H–E–O–G–M–IA–F` | `S–Y–E–NG–C` |
| Ciphertext reading | **Right → left** (rune reversal) | **Left → right** |
| Original key source | Four corners of a rectangle | Three equally spaced diagonal cells |
| Source runes | `X–N–X–C` | `J–R–TH` |
| Derived repeating key | `X–N–X–C` | `J–TH–TH` (totient on the center) |
| Literal decryption | **`SECUENDI`** | **`RATIO`** |
| Proposed Latin reading | **`SEQUENDI`** (`C/K` read as `Q`) | **`RATIO`** |

**Combined candidate:**

```text
Exact rune output:  S–E–C–U–E–N–D–I   R–A–T–I–O
Literal spelling:   SECUENDI RATIO
Latin hypothesis:   SEQUENDI RATIO
Suggested meaning:  A METHOD OF FOLLOWING
```

The important proposed connection is **not just a pair of English-looking words**. Both keys can be located at specific cells of the same matrix, and both proposed source constructions reuse two earlier anchors: the route's opening **`J(13,12)`** and its candidate **`MAP`** stage. These are the strongest structural aspects of the observation, subject to the methodological cautions below.

## 2. Conventions and established project anchors

### Rune arithmetic

The project's Gematria Primus **rune indices** run from 0 to 28:

```text
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Rune:   F  U TH  O  R  C  G  W  H  N  I  J EO  P  X  S  T  B  E  M  L NG OE  D  A AE  Y IA EA
```

The repeated-key subtraction used in both candidate readings is

$$
P_i = (C_i-K_i)\bmod 29.
$$

**Rune indices are not GP prime weights.** Prime weights are used only in the separate numerical observations in Section 7. Coordinates are **1-based `(row, column)`**: rows increase downward, columns rightward. `φ` denotes Euler's totient; `μ` denotes the Möbius function. An `IA`, `EO`, or `TH` transliteration is **one rune**, even though it contains two Latin letters.

### Two anchors from the proposed plaintext route

**Opening anchor — `J(13,12)`.** The project's first reconstructed source is `AE–J–EA`, centered at `J(13,12)`. In the earlier analysis, the 13-rune heading and `φ(13)=12` provided an additional motivation for examining that coordinate. Here it is treated as a **previously selected anchor**, not as a newly inferred certainty.

**MAP anchor — the candidate stage 28.** Its original three-rune source and the selected ciphertext are:

| Component | Coordinates and runes |
|---|---|
| Original MAP source | `EO(15,9) – X(16,9) – I(17,9)` |
| Original source center | **`M = X(16,9)`** |
| Selected MAP ciphertext | `R(19,11) → C/K(18,12) → AE(17,13)` |
| Ciphertext endpoint | **`E = AE(17,13)`** |

The project's selected MAP decryption uses a center-preserving key variant, rotated by its reported phase. **MAP is in stages 18–28, which are candidate route extensions; their status is not equivalent to an independently authenticated Cicada decryption.** Any heading construction depending on MAP inherits that condition.

## 3. First word: the rectangle that gives `SECUENDI`

### 3.1 Four real matrix cells

The candidate four-rune key is read **clockwise, starting at the upper-left corner** of an axis-aligned rectangle:

| Order | Corner | Coordinate | Cell rune | Index |
|---:|---|:---:|:---:|---:|
| 1 | Upper left | **(6,3)** | **X** | 14 |
| 2 | Upper right | **(6,9)** | **N** | 9 |
| 3 | Lower right | **(24,9)** | **X** | 14 |
| 4 | Lower left | **(24,3)** | **C/K** | 5 |

```text
       column 3                    column 9
row 6      X ──────────────────────── N
           │                          │
           │   MAP source is on       │
           │   the right-hand side:   EO (15,9)
           │                          X  (16,9)
           │                          I  (17,9)
           │                          │
row 24     C ──────────────────────── X

Clockwise corner key: X – N – X – C
Index key:           14 – 9 – 14 – 5
```

No totient transformation is applied to these four source runes. The key is **period four**, not a three-rune key with an extra symbol.

### 3.2 Why this rectangle is geometrically interesting

The two **opposite `X` corners** have exactly the same *squared* distance from the pre-existing opening `J = (13,12)`:

$$
\begin{aligned}
d^2\bigl(J,(6,3)\bigr)&=(13-6)^2+(12-3)^2=\boxed{130},\\
d^2\bigl(J,(24,9)\bigr)&=(24-13)^2+(9-12)^2=\boxed{130}.
\end{aligned}
$$

Consequently, `J` lies on the perpendicular bisector of the segment joining those opposite `X` corners. The rectangle's **center** is `Q=(15,6)` — **not** `J`. The bisector through `J` and `Q` has equation

$$
\boxed{3r+c=51},\qquad 3(13)+12=51.
$$

An additional independent-looking *spatial* alignment involves the original MAP source:

- All three original MAP source cells, `EO(15,9)`, `X(16,9)`, and `I(17,9)`, lie on the rectangle's **right side**, between rows 6 and 24 at column 9.
- The **midpoint of that side** is `(15,9)`, precisely the MAP source's upper arm, `EO`; it is **not** the MAP center `X(16,9)`.
- The rectangle's width in **coordinate steps** is `9−3=6=φ(14)`, where 14 is the MAP-center rune `X`'s index. Its height is `24−6=18`, making its height-to-width ratio **3:1**. Including boundary cells, the region spans **19×7 cells**.

These are exact observations, but the width and aspect ratio were **not prerequisites** of the selection procedure. They must not be retrospectively presented as independent predictions.

The repository also contains an optional [annotated diagram](../assets/02-sequendi-rectangle.png) illustrating these points. All coordinates and equations needed to understand the result are included here without the image.

### 3.3 A finite selector: 123,201 rectangles → one

It is possible to specify a geometric search that identifies these four corners **without checking the desired word, or looking for `N` and `C/K`**:

1. Fix the already recorded opening cell `J(13,12)` and the original MAP source `EO(15,9)–X(16,9)–I(17,9)`.
2. Find every cell containing the **MAP-center rune `X`**. Pair `X` cells whose squared distances from `J` are equal.
3. Discard pairs in the same row or column; each remaining pair specifies opposite corners of a non-degenerate, axis-aligned rectangle.
4. Require the **entire original three-cell MAP source** to lie along a single rectangle side.
5. Only after the rectangle has been selected, read the other two corner symbols and test the heading.

| Selection filter | Remaining candidates |
|---|---:|
| `X` cells in the matrix | 28 |
| Unordered `X`-cell pairs | 378 |
| Pairs at equal squared distance from `J` | 6 |
| Pairs defining non-degenerate rectangles | 5 |
| Rectangles whose side contains the entire MAP source | **1** |

The one selected rectangle is `((6,3), (6,9), (24,9), (24,3))`. The other four non-degenerate equal-distance rectangles fail the MAP-side test; the sixth pair shares a row and cannot define a non-degenerate rectangle.

For a separate exhaustive check, a 27×27 grid has

$$
\binom{27}{2}^{\!2}=\boxed{123{,}201}
$$

axis-aligned, non-degenerate rectangles with corners at cell centers. Of these, **4,290** have the entire MAP source on one side. Counting both diagonals of those rectangles gives **8,580 diagonal records**; **16** have `X` at both endpoints, **50** have endpoints equidistant from `J`, and **one** meets both criteria. The two enumeration orders agree.

**Meaning of “unique”:** exactly one rectangle satisfies this *specific, retrospectively formulated combination* of anchors, symbols, distance equality, and side incidence. This is **not** a global claim about every possible geometric selection rule.

### 3.4 The eight-rune decryption

Reverse the **rune order** of the first red word, without reversing the letters within `IA`:

```text
Original word:     S   H   E   O   G   M  IA   F
Reversed runes:    F  IA   M   G   O   E   H   S
Repeated key:      X   N   X   C   X   N   X   C
```

With original ciphertext indices `C_0,...,C_7` and period-four key `K=(14,9,14,5)`, the exact operation is

$$
P_j=\bigl(C_{7-j}-K_{j\bmod4}\bigr)\bmod29,\qquad j=0,\ldots,7.
$$

| # | Original cell | Reversed ciphertext | Key | Difference mod 29 | Plain rune |
|---:|:---:|---|---|---|:---:|
| 1 | (1,8) | F = 0 | X = 14 | `0−14 ≡ 15` | **S** |
| 2 | (1,7) | IA = 27 | N = 9 | `27−9 = 18` | **E** |
| 3 | (1,6) | M = 19 | X = 14 | `19−14 = 5` | **C/K** |
| 4 | (1,5) | G = 6 | C = 5 | `6−5 = 1` | **U/V** |
| 5 | (1,4) | O = 3 | X = 14 | `3−14 ≡ 18` | **E** |
| 6 | (1,3) | E = 18 | N = 9 | `18−9 = 9` | **N** |
| 7 | (1,2) | H = 8 | X = 14 | `8−14 ≡ 23` | **D** |
| 8 | (1,1) | S = 15 | C = 5 | `15−5 = 10` | **I** |

**Exact output:** `S–E–C–U–E–N–D–I`, i.e. **`SECUENDI`**. All eight ciphertext runes are used. There are three modular wraparounds, and the index-sum checksum is

$$
96-2(14+9+14+5)+3\times29=\boxed{99}.
$$

This arithmetic does **not** by itself produce a `Q`. The Q interpretation is discussed in Section 6.

## 4. Second word: a `MAP` extension that gives `RATIO`

### 4.1 Extend a known displacement

Consider the original MAP key center and its selected ciphertext endpoint:

$$
M=(16,9),\qquad E=(17,13),\qquad E-M=(+1,+4).
$$

Extend the exact same displacement *once more* beyond `E`:

$$
\boxed{R'=2E-M=(18,17)}.
$$

The real matrix rune at `(18,17)` is **`R`**. Thus `AE(17,13)` is exactly the midpoint between the MAP source center `(16,9)` and this new `R` cell. The operation uses coordinates only; no symbols are substituted to force the result.

Now use the **existing opening `J(13,12)`** as one arm of an equally spaced diagonal source. Reflect it through the new center `(18,17)`:

$$
Z=2(18,17)-(13,12)=\boxed{(23,22)}.
$$

The matrix rune at `(23,22)` is **`TH`**. The source is therefore

```text
J (13,12)  ── (+5,+5) ──  R (18,17)  ── (+5,+5) ──  TH (23,22)
                  original three-cell node: J – R – TH
```

It is an **equally spaced 45° diagonal**, and a **non-mirror node** because its two outer rune symbols differ (`J ≠ TH`). The coordinates of the arms are symmetric even though the rune symbols are not.

### 4.2 Transform the center, then determine the phase

The source has rune indices `J=11`, `R=4`, `TH=2`. Apply the project's **center-only totient** operation:

$$
\varphi(4)=2=\mathrm{TH},\qquad
\mathrm{J-R-TH}\longrightarrow\boxed{\mathrm{J-TH-TH}}.
$$

For the resulting three-rune key, the project uses the Möbius values of the totients of its indices:

| Key rune | Index | Totient | Möbius of totient |
|:---:|---:|---:|---:|
| J | 11 | `φ(11)=10` | `μ(10)=+1` |
| TH | 2 | `φ(2)=1` | `μ(1)=+1` |
| TH | 2 | `φ(2)=1` | `μ(1)=+1` |

The key signature is `(+1,+1,+1)`; hence the existing three-rune phase formula gives

$$
p=(1+1+1)\bmod3=\boxed{0}.
$$

**No rotation is required.** Repeat the key as `J–TH–TH–J–TH` over the five red runes, read in the **original left-to-right direction**.

### 4.3 The five-rune decryption

| # | Red ciphertext | Cipher index | Key | Key index | Difference | Plain rune |
|---:|:---:|---:|:---:|---:|---|:---:|
| 1 | S | 15 | J | 11 | `15−11 = 4` | **R** |
| 2 | Y | 26 | TH | 2 | `26−2 = 24` | **A** |
| 3 | E | 18 | TH | 2 | `18−2 = 16` | **T** |
| 4 | NG | 21 | J | 11 | `21−11 = 10` | **I** |
| 5 | C/K | 5 | TH | 2 | `5−2 = 3` | **O** |

```text
Ciphertext: S   Y   E   NG   C
Key:        J  TH  TH    J  TH
Plaintext:  R   A   T    I   O
```

**Exact output:** **`RATIO`**, with plaintext index sequence `(4,24,16,10,3)`. No modulo wraparound is needed. The checksum is

$$
85-(11+2+2+11+2)=85-28=\boxed{57}.
$$

### 4.4 A second, separate source for the same key

The matrix has a second equally spaced **horizontal** source in row 1, beyond the red heading:

```text
J(1,19) ── O(1,21) ── TH(1,23)
```

Here `φ(index(O))=φ(3)=2`, so the center transformation again gives `J–TH–TH`. This confirms that the derived key has **two specific geometric realizations** in the matrix. It is **not a second independent decryption**: the key stream and the five-rune arithmetic are identical.

Across all **14,976** equally spaced three-cell horizontal, vertical, and 45° diagonal placements in the 27×27 matrix, the original investigation found **exactly two** center-totient sources yielding this exact key. Given the matrix's rune frequencies, roughly **1.98** such sources would be expected under a simple random-permutation approximation for this *already specified* key. The rarity of the shape alone therefore does **not** establish statistical significance. The particular connection to the chosen MAP center, endpoint, and opening `J` is the more interesting feature.

### 4.5 An algebraic equivalence with the earlier `THEN` key

The project's stage 17, `THEN`, used the aligned key `E–IA–IA = (18,27,27)`. Element by element, this is the **additive inverse mod 29** of `J–TH–TH = (11,2,2)`:

$$
(18,27,27)+(11,2,2)\equiv(0,0,0)\pmod{29}.
$$

Thus subtracting `J–TH–TH` is equivalent to **adding** `E–IA–IA`. If restarted at the second word's boundary, that complementary addition yields the same `RATIO`. It is an **equivalence**, not a new independent match or proof that the previous THEN key was intended for the heading.

## 5. How the two constructions fit together

Both candidate source keys use the **same opening and MAP anchors**, but the mechanisms are genuinely different:

| Property | `SECUENDI` | `RATIO` |
|---|---|---|
| Matrix feature | Rectangle, four corners | Equally spaced diagonal, three cells |
| Role of `J(13,12)` | Circle center: two `X` corners are equidistant | One outer arm of source triple |
| Role of MAP | Entire original source lies on one side | Source-center → ciphertext-endpoint vector is extended |
| Key construction | Read direct corner runes | Totient-transform the center rune |
| Key length | 4 | 3 |
| Order of ciphertext | Reverse all 8 runes | Keep all 5 runes in printed order |
| Rotation | Selected upper-left start, clockwise; **not derived from a general phase law** | Existing three-rune phase gives 0 |
| Literal output | `SECUENDI` | `RATIO` |

The two words are effectively decrypted **away from their printed separator**: the left-hand group is read right-to-left, and the right-hand group left-to-right. This is a useful description of the successful setup, **not** an independently established instruction to read every heading outward.

Most importantly, the observed relationship does **not** yet provide one deterministic algorithm that tells a solver, *before looking at possible outputs*, when to select a rectangle instead of a three-cell node, when to reverse a word, or how to restart keys at a word boundary.

## 6. From literal runes to the proposed Latin title

The first calculation yields these **actual** rune indices:

```text
S   E  C/K U/V E   N   D   I
15 18   5   1 18   9  23  10
```

In the project's transliteration, the third rune is `C/K` (index 5). There is **no distinct Q rune** among the 29 symbols. A proposed Latin reading treats that rune as **Q** in the sequence `...CU...`, giving:

```text
Numerical output:  SECUENDI RATIO
Latin reading:     SEQUENDI RATIO
```

This is a **spelling hypothesis**, not a modification of the arithmetic. The recovered rune always remains index 5, and neither its index nor its prime weight is changed. The absence of a Q rune makes a transliteration convention necessary, but **does not prove that this convention is the one Cicada used**.

In Latin, *sequendi* is the genitive of the gerund from *sequor* (“to follow, pursue”). *Ratio* can mean “method,” “procedure,” “system,” or “reasoning.” Therefore *sequendi ratio* can reasonably be rendered **“a method of following”** or **“a method of pursuit,”** depending on context. It is not, by itself, an explicit instruction about *which* line or route to follow.

Lexical references: Lewis and Short, *A Latin Dictionary*, entries [*sequor*](https://alatius.com/ls/index.php?l=sequor) and [*ratio*](https://alatius.com/ls/index.php?l=ratio). These support the **Latin interpretation only**; they do not authenticate the cipher hypothesis.

## 7. Numerical cross-checks and secondary observations

### 7.1 Original ciphertext sums

The first red group has index sum **96**, the second **85**, and the full heading **181**:

$$
96-85=\boxed{11}=\operatorname{index}(J).
$$

This reuses a numerical value associated with the opening `J` cell. It is exact, but subtracting the two word sums is **not independently known to be part of the intended cipher**.

### 7.2 Prime-weight sums of the recovered words

The **Gematria Primus prime weight** assigned to a rune is the prime at its index: `F(0)=2`, `U(1)=3`, …, `EA(28)=109`. These weights are distinct from the indices used in decryption.

| Word, using the actual rune encoding | Rune-index sum | GP prime-weight sum | Euler totient of GP sum |
|---|---:|---:|---:|
| `SECUENDI` | 99 | **352** | **160** |
| `RATIO` | 57 | **205** | **160** |
| **Combined** | **156** | **557** | — |

The individual GP calculations are:

$$
\begin{aligned}
\mathrm{GP}(\mathrm{SECUENDI})&=53+67+13+3+67+29+89+31=\boxed{352},\\
\mathrm{GP}(\mathrm{RATIO})&=11+97+59+31+7=\boxed{205}.
\end{aligned}
$$

Their totients are equal despite different factorizations:

$$
\begin{aligned}
352&=2^5\cdot11,& \varphi(352)&=\boxed{160},\\
205&=5\cdot41,& \varphi(205)&=\boxed{160}.
\end{aligned}
$$

And their combined GP sum is **prime**:

$$
\mathrm{GP}(\mathrm{SECUENDI\ RATIO})=352+205=\boxed{557},\quad 557\text{ is prime}.
$$

The checksum over both words is consistent with three total wraparounds:

$$
\underbrace{181}_{\text{cipher indices}}-
\underbrace{112}_{\text{aligned key indices}}+
3\cdot29=\underbrace{156}_{\text{plaintext indices}}.
$$

These relationships are **additional exact observations**, not evidence that can be multiplied into an independent statistical significance calculation. They also apply to the literal `C/K` rune encoding, whether or not `SECUENDI` is read as *sequendi*.

## 8. Checks against alternative explanations

### 8.1 The MAP extension is selective within one fixed 28-stage test

The first research note applied a fixed construction to each of the project's **28 recorded stages**: take that stage's original key-node center `M` and selected ciphertext endpoint `E`; set `R'=2E−M`; reflect the fixed opening `J(13,12)` across `R'` to obtain `Z=2R'−J`; keep the triple only if the cells lie in the matrix and form a horizontal, vertical, or 45° equally spaced node. Test its direct and center-totient key variants and their indicated phases against the unchanged five-rune second heading word.

Only **two of the 28 stages** gave eligible triples under that precise recipe:

| Stage | Derived triple | Tested output | Interpretation |
|---|---|---|---|
| 06 — `CRY` | `J–U–Y`, centered at `(9,16)` | `ESBAD` (phase 2) | No recognizable word |
| **28 — `MAP`** | **`J–R–TH`, centered at `(18,17)`** | **`RATIO`** (center totient, phase 0) | Candidate word |

This **1-of-28 word outcome** is meaningful only **within the stated search family**. Because the construction arose during exploration of the heading, it must **not** be translated into a probability of Cicada's intention.

### 8.2 The rectangle selector was developed after the word was found

The first-word candidate and its period-four key originated in exploratory key/lexical searching. The rectangular source was identified, and the particular `J`/MAP selector was formalized **afterward**. It is still valuable as a compact, reproducible geometric characterization, but it was **not a blind prediction** of `SECUENDI`.

Further controls reported in the original rectangle note found that:

- Of **729 possible matrix cells** substituted as the circle center while keeping the MAP source fixed, **705** selected no rectangle and **24** selected one.
- Of the **24 cells containing `J`**, only the originally used **`J(13,12)`** selected a rectangle under this specific test.
- Substituting the RATIO center or its far arm, the MAP source center, the MAP ciphertext endpoint/start, or the geometric matrix center did not select one.
- Testing both ciphertext directions, both perimeter directions, and four starting corners (16 configurations) yielded `SECUENDI` in **two equivalent orientations of the identical four-number key**: upper-left `X` clockwise or lower-right `X` counterclockwise. These count as **one**, not two, successful key streams.

Again, these are **controls of a retrospectively chosen rule**, not a calibrated p-value.

### 8.3 A single key does not decrypt both words

Applying the three-rune `J–TH–TH` key to the first eight red runes, without the word-specific reverse reading and rectangular construction, gives an **unrecognizable** sequence (`R–G–T–NG–R–B–T–IA`). The successful first-word reading requires a different key and direction. That asymmetry is a genuine unresolved feature, not something the combined phrase makes disappear.

### 8.4 The heading keys are not validated as the next sequential post-MAP stage

The project's conditional **Reports 01–08** predict the next normal route block after MAP. In the selected MAP state, its immediate next **key signature** is reported to be `(0,0,0)`; the RATIO key instead has **`(+1,+1,+1)`**. Both sum to phase 0 modulo 3, but **equal phase is not equal signature**.

Moreover, the ordinary next ciphertext is predicted to have a constrained right-going **diagonal** geometry, whereas the second red heading word is printed **horizontally** at row 1, columns 9–13. The candidate title therefore **does not satisfy the existing rules as the next ordinary sequential ciphertext block**. It must remain a **separate word-level title/heading hypothesis**, or a future general theory must explicitly explain the exception.

The first-word rectangle adds a second unresolved mismatch: the existing phase mechanism was defined for **three-rune nodes**, not four-corner keys. Applying the old modulo 3 to its signature sum or switching to modulo 4 leads to different phase conventions; neither extension is independently justified here. The successful first-word computation uses **a specifically chosen starting corner and no rotation**.

### 8.5 The danger of many possible keys

The original audit of 28 route stages checked **888** sliding key-stream alignments over the heading. The longest exact overlap with the previously proposed route plaintext was four runes, and **278 out of 500** random permutations of the heading reached an overlap of at least four in the same test. A separate permissive search for eastern-half, parity-compatible post-MAP three-rune source nodes with the predicted `(0,0,0)` signature found **614 eligible node realizations** and **555 distinct derived keys**, without identifying a convincing full-heading plaintext.

These background searches show that **short lexical matches are common when enough key choices are tried**. The present case should be judged primarily on whether one consistent rule can predict *both* heading readings and later unseen data, rather than on the attractiveness of the proposed title or individual numerical coincidences.

## 9. What is established, and what remains open

**Reproducible facts within the project's matrix and chosen candidate route:**

- The two source shapes are present at the specified coordinates.
- The **rectangle selection** yields one result within its exactly defined geometric family.
- The **MAP extension** produces `J–R–TH`, whose center totient gives `J–TH–TH`.
- The arithmetic gives the literal **`SECUENDI RATIO`** exactly, preserving all 13 ciphertext runes.
- The reported GP sums, equal totients, and prime combined sum are correct.

**Unresolved inferences:**

- Whether the two heading keys were **intended by Cicada**, rather than found through flexible retrospective searches.
- Whether there is a principled **four-corner vs. three-cell selection rule**.
- Whether **ciphertext reversal, key starting corner, key phase, and word-boundary reset** can be predicted rather than selected for the desired phrase.
- Whether a **`C/K → Q`** transliteration convention is independently supported.
- Whether this scheme generalizes to **other heading words or unseen LP2 ciphertext**, and how it relates to the existing sequential Reports 00–08.

The most decisive next step is to **freeze** the full source-selection, orientation, transformation, and phase procedure *before* evaluating a new target. Then test it on additional predetermined text and controlled shuffled matrices, recording negative results and the number of admissible choices. Without that predictive step, the proposal remains a **structured, falsifiable candidate**, not a demonstrated decryption method.

## 10. Verification script

The script below requires only standard Python. It reads the **actual 27×27 matrix** from the repository archive, checks its SHA-256 fingerprint, recomputes both plaintext words, verifies the geometric rectangle search in two enumeration orders, tests the secondary RATIO source, and checks the prime/totient relationships.

Save the code as `verify_red_heading.py`, then run:

```bash
python verify_red_heading.py /path/to/Liber-Primus-project.zip
```

<details>
<summary><strong>Python verification source (click to expand)</strong></summary>

```python
from itertools import combinations, product
from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import re
import sys
import zipfile

ALPHABET = "F U TH O R C G W H N I J EO P X S T B E M L NG OE D A AE Y IA EA".split()
IDX = {rune: i for i, rune in enumerate(ALPHABET)}


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def d2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def corners(a, b):
    r1, r2 = sorted((a[0], b[0]))
    c1, c2 = sorted((a[1], b[1]))
    return ((r1, c1), (r1, c2), (r2, c2), (r2, c1))


def on_one_side(rect, points):
    r1, c1 = rect[0]
    r2, c2 = rect[2]
    edges = ((0, r1, c1, c2), (0, r2, c1, c2),
             (1, c1, r1, r2), (1, c2, r1, r2))
    return any(
        all(p[axis] == fixed and lo <= p[1 - axis] <= hi for p in points)
        for axis, fixed, lo, hi in edges
    )


archive_path = Path(sys.argv[1])
with zipfile.ZipFile(archive_path) as zf:
    name = next(n for n in zf.namelist() if n.endswith("/0-2-live-map.html"))
    html = zf.read(name).decode("utf-8")

table = re.search(r'<table class="rune-grid">(.*?)</table>', html, re.S).group(1)
matrix = []
for tr in re.findall(r"<tr>(.*?)</tr>", table, re.S):
    row = re.findall(r'<span class="rune">(.*?)</span>', tr)
    if row:
        matrix.append([IDX[s.split("/")[0]] for s in row])

assert len(matrix) == 27 and all(len(row) == 27 for row in matrix)
fingerprint = hashlib.sha256(bytes(v for row in matrix for v in row)).hexdigest()
assert fingerprint == "7878349fef98939f6c816d657547e7e80f1b875d83b28e239c328e67b26159c7"


def at(p):
    return matrix[p[0] - 1][p[1] - 1]


J = (13, 12)
M = (16, 9)
E = (17, 13)
map_source = ((15, 9), M, (17, 9))
assert at(J) == IDX["J"]
assert [at(p) for p in map_source] == [IDX[x] for x in ("EO", "X", "I")]
assert [at(p) for p in ((19, 11), (18, 12), E)] == [IDX[x] for x in ("R", "C", "AE")]
assert [at((1, c)) for c in range(1, 14)] == [IDX[x] for x in
    "S H E O G M IA F S Y E NG C".split()]

# ----- First word: rectangle selector -----
xs = [p for p in product(range(1, 28), repeat=2) if at(p) == IDX["X"]]
equal_pairs = [(a, b) for a, b in combinations(xs, 2) if d2(a, J) == d2(b, J)]
rectangles = [corners(a, b) for a, b in equal_pairs if a[0] != b[0] and a[1] != b[1]]
selected = [rect for rect in rectangles if on_one_side(rect, map_source)]
assert (len(xs), len(equal_pairs), len(rectangles), len(selected)) == (28, 6, 5, 1)
rect = selected[0]
assert rect == ((6, 3), (6, 9), (24, 9), (24, 3))
assert [at(p) for p in rect] == [IDX[x] for x in ("X", "N", "X", "C")]
assert d2(rect[0], J) == d2(rect[2], J) == 130
assert (rect[1][0] + rect[2][0]) // 2 == 15
assert phi(at(M)) == 6 == rect[1][1] - rect[0][1]
assert rect[2][0] - rect[1][0] == 18

# Cross-check using every possible axis-aligned rectangle and both diagonals.
counts = dict(all=0, side=0, x_diagonals=0, equal_diagonals=0, both=0)
for r1, r2 in combinations(range(1, 28), 2):
    for c1, c2 in combinations(range(1, 28), 2):
        rec = ((r1, c1), (r1, c2), (r2, c2), (r2, c1))
        counts["all"] += 1
        if not on_one_side(rec, map_source):
            continue
        counts["side"] += 1
        for i, j in ((0, 2), (1, 3)):
            a, b = rec[i], rec[j]
            x_pair = at(a) == at(b) == IDX["X"]
            equal = d2(a, J) == d2(b, J)
            counts["x_diagonals"] += x_pair
            counts["equal_diagonals"] += equal
            counts["both"] += x_pair and equal
assert counts == dict(all=123201, side=4290, x_diagonals=16,
                      equal_diagonals=50, both=1)

key1 = [at(p) for p in rect]
cipher1 = matrix[0][:8][::-1]  # reversal by rune, not by Latin letter
plain1 = [(c - key1[i % 4]) % 29 for i, c in enumerate(cipher1)]
assert "".join(ALPHABET[n] for n in plain1) == "SECUENDI"
assert sum(plain1) == 99

# ----- Second word: extended MAP geometry -----
step = (E[0] - M[0], E[1] - M[1])
assert step == (1, 4)
r_center = (E[0] + step[0], E[1] + step[1])
far_arm = (2 * r_center[0] - J[0], 2 * r_center[1] - J[1])
assert (r_center, far_arm) == ((18, 17), (23, 22))
source2 = (J, r_center, far_arm)
assert [at(p) for p in source2] == [IDX[x] for x in ("J", "R", "TH")]
key2 = [at(J), phi(at(r_center)), at(far_arm)]
assert key2 == [11, 2, 2]

cipher2 = matrix[0][8:13]
plain2 = [(c - key2[i % 3]) % 29 for i, c in enumerate(cipher2)]
assert "".join(ALPHABET[n] for n in plain2) == "RATIO"
assert sum(plain2) == 57

# Independent horizontal source for the same transformed three-rune key.
other_source = ((1, 19), (1, 21), (1, 23))
assert [at(p) for p in other_source] == [IDX[x] for x in ("J", "O", "TH")]
assert [at(other_source[0]), phi(at(other_source[1])), at(other_source[2])] == key2
assert [(29 - k) % 29 for k in key2] == [IDX[x] for x in ("E", "IA", "IA")]

# Enumerate equally spaced triples in four undirected axis families.
triple_count, source_matches = 0, []
for center in product(range(1, 28), repeat=2):
    for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
        for radius in range(1, 27):
            a = (center[0] - radius * dr, center[1] - radius * dc)
            b = (center[0] + radius * dr, center[1] + radius * dc)
            if not all(1 <= v <= 27 for p in (a, b) for v in p):
                continue
            triple_count += 1
            if [at(a), phi(at(center)), at(b)] == key2:
                source_matches.append((a, center, b))
assert triple_count == 14976
assert len(source_matches) == 2

# ----- GP prime-weight totals -----
primes = [n for n in range(2, 110) if prime(n)]
assert len(primes) == 29
s1, s2 = (sum(primes[n] for n in seq) for seq in (plain1, plain2))
assert (s1, s2) == (352, 205)
assert phi(s1) == phi(s2) == 160
assert s1 + s2 == 557 and prime(557)
assert sum(matrix[0][:8]) == 96 and sum(matrix[0][8:13]) == 85
assert sum(plain1) + sum(plain2) == 156

print("Literal output: SECUENDI RATIO")
print("Latin hypothesis: SEQUENDI RATIO")
print("Rectangle:", rect, "| Exhaustive check:", counts)
print("RATIO source:", source2, "| Equivalent sources:", len(source_matches))
print("GP:", s1, "+", s2, "= 557 (prime) | phi sums: 160, 160")
print("Matrix SHA-256:", fingerprint)
```

</details>

The script establishes the stated **matrix, geometry, arithmetic, and finite search counts**. It does **not** automatically verify the exploratory 28-stage comparisons, prove the Q transliteration, or test whether the constructions predict a new Cicada ciphertext.

---

## Project references and provenance

This document consolidates the two original research notes, preserving their substantive claims and explicit limitations:

1. *The Red Heading: A Geometric `J–TH–TH` Key and the Candidate Plaintext `RATIO`* (28 October 2026).
2. *The Red Heading: A Rectangular `X–N–X–C` Key and the Candidate Reading `SEQUENDI`* (29 October 2026).

Within the repository, the principal supporting files are:

- [`0-2-live-map.html`](../0-2-live-map.html) — the complete 729-rune matrix.
- [`plaintext-i-found/01-as-i-go-the.md`](../plaintext-i-found/01-as-i-go-the.md) — opening `AE–J–EA` source.
- [`plaintext-i-found/17-then.md`](../plaintext-i-found/17-then.md) — the complementary `E–IA–IA` key.
- [`plaintext-i-found/28-map.md`](../plaintext-i-found/28-map.md) — the selected MAP source and ciphertext.
- [`Start-reading-here/00-decryption-method.md`](../Start-reading-here/00-decryption-method.md) — rune arithmetic, key transformations, signatures, and phases.
- [`Start-reading-here/01-next-key-signature.md`](../Start-reading-here/01-next-key-signature.md) and [Reports 02–08](../Start-reading-here/) — conditional predictions for the next sequential block.

**Matrix fingerprint:** SHA-256 of the 729 rune indices, row-major, encoded as one byte per index:

```text
7878349fef98939f6c816d657547e7e80f1b875d83b28e239c328e67b26159c7
```

**Repository placement:** this Markdown file is designed to live in `Really cool discoveries!/` alongside the previous notes, so the relative repository links above resolve. The main text and verification code remain usable without the optional image.

---

**Conclusion.** `SEQUENDI RATIO` is a coherent **candidate Latin reading** of two exact modular outputs, each associated with a precisely specified matrix construction that reconnects to `J` and MAP. The combined result is worth investigating because it yields *testable procedures and identifiable failures*, **not** because a Latin phrase or a few numerical coincidences suffice to establish what Cicada 3301 intended.
