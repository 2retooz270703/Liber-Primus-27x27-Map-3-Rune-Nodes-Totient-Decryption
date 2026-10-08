# 16 — THEN

> **Recovered plaintext candidate:** `THEN` (`TH-E-N`: **three runes**, four Latin letters)  
> **Current proposed sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON THEN`  
> **Status:** strongest currently identified **direct continuation** after the primary `SOON` route. The coordinates, cipher arithmetic, mirror geometry, and Möbius rotations below are reproducible; the proposed handoff and selection of the key-generating mirror are **not yet uniquely forced by a universal route rule**. This is a research candidate, not a verified Cicada 3301 plaintext.

Everything below uses the original 27×27 map:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

Coordinates are **1-based** `(row,column)`. Rune arithmetic uses the repository's **0-based Gematria Primus indices**, modulo `29`. `TH`, `IA`, `EA`, and other multi-letter transliterations each denote **one rune**.

---

## 1. Frozen starting point: the primary SOON endpoint

The previous chapter, [`15-SOON.md`](./15-SOON.md), gives the preferred local reconstruction:

```text
CIPHERTEXT: X(25,16) D(25,17) W(25,18) H(25,19)
KEY:        EA       L        R        EA
PLAINTEXT:  S        O        O        N
```

The `SOON` key is generated as:

```text
L-R-EA
↓
signature = 8-2-12
M         = (0,-1,0)
phase     = 2
↓
active key = EA-L-R
```

So the fixed state with which chapter 16 begins is:

```text
LAST CELL = H(25,19)
PHASE     = 2
```

This chapter does **not** silently switch to the secondary `SOON` route. Its alternate endpoint `W(27,27)` will be used only as a later geometric cross-check.

---

## 2. Reuse phase 2 on the endpoint coordinates

Apply the existing coordinate selector; do not introduce a new phase:

```text
T₂(r,c) = (φ²(r), φ²(c))
V₂(r,c) = (μ(φ²(r)), μ(φ²(c)))
```

At `H(25,19)`:

```text
ROW 25:
25 → φ(25)=20 → φ(20)=8 → μ(8)=0

COLUMN 19:
19 → φ(19)=18 → φ(18)=6 → μ(6)=+1
```

Therefore:

```text
T₂(25,19) = (8,6)
V₂(25,19) = (0,+1)
```

The second component gives an unambiguous **RIGHT-compatible direction**. The first component has a zero Möbius sign, but its pre-Möbius value `8` is retained by the existing **hidden-value rule**.

```text
DIRECTION: RIGHT
RETAINED NUMERIC PAIR: (8,6)
```

**Important distinction:** `V₂` determines orientation, not step length. The use of `6` as one step length and `8` as another is a proposed, geometry-supported application of the retained `T₂` values—not a theorem of the coordinate-selector rule alone.

---

## 3. Both retained values land on the SAME prospective ciphertext

Read the exact original row 25 beginning at the `SOON` endpoint:

| Column | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
|---|---|---|---|---|---|---|---|---|---|
| Rune | **H** | EA | TH | **IA** | AE | C | **L** | **T** | **W** |
| Offset from H | **0** | +1 | +2 | **+3** | +4 | +5 | **+6** | +7 | **+8** |

So the selector's numeric pair is reflected in two exact positions:

```text
H(25,19) → RIGHT 6 → L(25,25)
H(25,19) → RIGHT 8 → W(25,27)
```

The uninterrupted segment from the first landing point to the second is:

```text
L(25,25) → T(25,26) → W(25,27)
```

Therefore the **proposed** contiguous ciphertext is:

```text
CIPHERTEXT = L-T-W
```

This uses **both** numbers already exposed after `SOON`:

```text
                    +6                 +2
H(25,19) ───────────────────→ L(25,25) ───→ W(25,27)
└─────────────────────────────── +8 ────────────────┘
```

`L-T-W` occurs **once** as a directed, consecutive, straight three-rune sequence in the entire 27×27 map (all eight reading directions checked). Its occurrence is exactly:

```text
(25,25) → (25,26) → (25,27)
```

**Selection caveat:** this does not prove that `6` must be the ciphertext entry point. It documents the tight geometry once the `(6,8)` interpretation is adopted.

---

## 4. The exact midpoint hides a globally unique key mirror

The distance from `H(25,19)` to the prospective starting cell `L(25,25)` is `6`.

The midpoint is therefore **forced geometrically**:

```text
(19+25)/2 = 22

MIDPOINT = (25,22)
```

The rune at that exact position is:

```text
IA(25,22)
```

Look down its column:

```text
IA(25,22)  ← midpoint between H and L
    |
    | 1
    |
IA(26,22)  ← mirror center
    |
    | 1
    |
IA(27,22)  ← outer node
```

This is an exact equal-radius, vertical, three-rune mirror:

```text
IA-IA-IA
radius = 1
```

A scan of **all 729 grid positions**, all four standard unoriented axes (horizontal, vertical, and both 45° diagonals), and every possible integral arm length finds **exactly one** standard `IA-IA-IA` mirror: the one above.

This is the principal reason to investigate this mirror as the key generator: **one of its outer runes is exactly halfway along the proposed post-`SOON` move**.

```text
SOON END            KEY-MIRROR OUTER            CIPHERTEXT START
H(25,19) ─── 3 ─── IA(25,22) ─── 3 ─── L(25,25)
                         |
                      IA(26,22)
                         |
                      IA(27,22)
```

The midpoint position itself is fixed by the two proposed anchors. The further step **“use the mirror passing through this midpoint as the key generator”** remains a proposed structural-selection rule and needs testing on other transitions.

---

## 5. Generate the key by the existing center-totient rule

The mirror is:

```text
IA-IA-IA
```

The **center** is `IA(26,22)` and its rune index is:

```text
IA = 27
φ(27) = 18
18 = E
```

Compile the central rune, leaving the outers unchanged:

```text
IA-IA-IA
   ↓ φ
IA-E-IA
```

This gives the three-rune **unrotated key**:

```text
K = IA-E-IA
```

There is no need to choose a key by reading the desired English word backward. This key follows from a concrete mirror and the repository's existing center-transformation mechanism.

---

## 6. Möbius independently fixes the active phase

Compute the totient signature of the generated key:

```text
K = IA-E-IA

φ(IA=27) = 18
φ(E=18)  =  6
φ(IA=27) = 18

signature = 18-6-18
```

Apply Möbius:

```text
μ(18) =  0
μ(6)  = +1
μ(18) =  0

M = (0,+1,0)
```

The key phase is:

```text
p = (0+1+0) mod 3 = 1
```

Under the repository's rotation convention:

```text
phase 0 → IA-E-IA
phase 1 → E-IA-IA   ← selected mathematically
phase 2 → IA-IA-E
```

Therefore the active key is:

```text
ACTIVE KEY = E-IA-IA
PHASE      = 1
```

The rotation is **not chosen manually** to produce `THEN`; it is generated by the same `φ → μ → phase mod 3` procedure as in stages `01–15`.

---

## 7. Full modular decryption: L-T-W → TH-E-N

Apply the established decryption formula:

```text
P = (C - K) mod 29
```

For the three consecutive ciphertext runes:

| # | Position | Ciphertext `C` | Active key `K` | Subtraction mod 29 | Plaintext |
|---:|---|---|---|---|---|
| 1 | `(25,25)` | `L = 20` | `E = 18` | `(20−18) mod 29 = 2` | **TH** |
| 2 | `(25,26)` | `T = 16` | `IA = 27` | `(16−27) mod 29 = 18` | **E** |
| 3 | `(25,27)` | `W = 7` | `IA = 27` | `(7−27) mod 29 = 9` | **N** |

Thus:

```text
CIPHERTEXT: L   T    W
VALUES:     20  16   7

ACTIVE KEY: E   IA   IA
VALUES:     18  27   27

RESULT:      2  18    9
RUNES:      TH   E    N
```

# **THEN**

This is a **three-rune** plaintext: `TH` is one Gematria Primus rune.

The proposed growing English sequence is:

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON THEN**

`SEE YOU SOON, THEN` is natural English, although punctuation and sentence boundaries cannot be deduced from this operation.

---

## 8. The entire primary handoff in one diagram

```text
15 — SOON

X-D-W-H
-
EA-L-R-EA
=
S-O-O-N

             final H(25,19)
                    |
          inherited phase p=2
                    |
     T₂(25,19) = (8,6)
     V₂(25,19) = (0,+1)
                    |
               RIGHT
                    |
           +6 ────┼────→ L(25,25) ─ T(25,26) ─ W(25,27)
                    |            \_______________________/
           +3 ────┼────→ IA(25,22)   ciphertext L-T-W
                    |       |
                    |    IA(26,22)
                    |       |
                    |    IA(27,22)
                    |       |
                    |  IA-IA-IA (unique mirror)
                    |       |
                    |  φ(center IA=27)=18=E
                    |       |
                    |  IA-E-IA
                    |       |
                    |  signature 18-6-18
                    |       |
                    |  M=(0,+1,0)
                    |       |
                    |  phase 1
                    |       |
                    |  KEY E-IA-IA
                    |       |
                    +-------+-------------------+
                                                |
                                         L-T-W
                                       - E-IA-IA
                                                |
                                           TH-E-N
                                                |
                                              THEN
```

The anchored facts are the coordinates, the value pair, the midpoint mirror, and the arithmetic. The **interpretive choices** are precisely the use of `+6` for ciphertext entry and the midpoint mirror as the key source.

---

## 9. The end of THEN touches the secondary SOON endpoint

`THEN` ends at:

```text
W(25,27)
```

In chapter `15-SOON.md`, the **secondary** reconstruction of `SOON` ends at:

```text
W(27,27)
```

These are not isolated locations. The intermediate cell is:

```text
NG(26,27)
```

Together they form an exact radius-1 vertical mirror:

```text
W (25,27)  ← END OF THEN
|
NG(26,27)  ← CENTER
|
W (27,27)  ← END OF SECONDARY SOON
```

That is:

```text
W-NG-W
```

**Verified geometric link:** the proposed primary post-`SOON` continuation ends at one outer, and the earlier secondary `SOON` route ends at the other outer of the same local mirror.

**Important uniqueness correction:** `W-NG-W` is **not globally unique**; it occurs in two standard equal-radius arrangements in the matrix. The specific instance connecting these two endpoints is directly verifiable and is the one relevant here.

---

## 10. The W-NG-W mirror can regenerate phase 2

Treat the local endpoint mirror as the **candidate next key generator**.

Transform its center:

```text
NG = 21
φ(21) = 12 = EO

W-NG-W
↓
W-EO-W
```

Now derive its signature:

```text
φ(W=7)  = 6
φ(EO=12)= 4
φ(W=7)  = 6

signature = 6-4-6
```

Möbius:

```text
μ(6)=+1
μ(4)= 0
μ(6)=+1

M = (+1,0,+1)
phase = (1+0+1) mod 3 = 2
```

So the candidate next active key is:

```text
W-EO-W
phase 2
→ W-W-EO
```

**If** this local mirror is chosen for the next key, the route enters phase `2` again.

This is a **possible next-state bridge**, not an established continuation or a proof of any word following `THEN`.

---

## 11. Exact coordinate-state return: (8,6) → (8,6)

The starting `SOON` endpoint has already given:

```text
H(25,19), p=2

T₂(25,19)=(8,6)
V₂(25,19)=(0,+1)
```

Now conditionally use the phase `2` generated by `W-NG-W` at the `THEN` endpoint `W(25,27)`:

```text
ROW 25:
φ²(25)=φ(20)=8
μ(8)=0

COLUMN 27:
27 → φ(27)=18 → φ(18)=6
μ(6)=+1
```

This produces:

```text
T₂(25,27)=(8,6)
V₂(25,27)=(0,+1)
```

Compare both states:

| Feature | After primary SOON | After THEN, **if** W-NG-W sets p=2 |
|---|---|---|
| Cell | `H(25,19)` | `W(25,27)` |
| Phase | `2` | `2` |
| Totient pair | `(8,6)` | `(8,6)` |
| Möbius pair | `(0,+1)` | `(0,+1)` |
| Direction | RIGHT-compatible | RIGHT-compatible |

The equality is exact, including **both** pre-Möbius components.

There is a further check specific to the 1–27 column domain:

```text
φ²(19)=6
φ²(27)=6
```

Among column numbers `1…27`, **19 and 27 are the only two** with `φ²(c)=6`.

Their separation is:

```text
27 − 19 = 8 = φ²(25)
```

Hence the retained `8` at the initial state is also the exact horizontal displacement between the two equal-state endpoints:

```text
H(25,19) ───── RIGHT 8 ─────→ W(25,27)
```

This is a precise and unusual internal **consistency relation**. It does **not** establish that the algorithm is supposed to loop, nor does it specify where to go after the rightmost column `27`.

---

## 12. A critical phase ambiguity at the final W

There is another exact mirror containing the final cell:

```text
W(25,9) —9— W(25,18) —9— W(25,27)
```

This `W-W-W` mirror is globally unique among standard axes and integral radii. It generates:

```text
φ(W=7)=6=G
W-W-W → W-G-W
```

Its signature and phase are:

```text
signature = 6-2-6
M = (+1,-1,+1)
phase = 1
```

This **competes** with the local `W-NG-W` mirror, which gives phase `2`.

Moreover, the active phase of `THEN` itself is `1`. If this phase is simply carried forward before choosing another mirror, the direct coordinate selector at `W(25,27)` is:

```text
T₁(25,27)=(φ(25),φ(27))=(20,18)
V₁(25,27)=(μ(20),μ(18))=(0,0)
```

Therefore:

```text
UNCONDITIONAL END STATE AFTER THEN:
    W(25,27), inherited phase 1
    T₁=(20,18)
    V₁=(0,0)

CONDITIONAL BRIDGE:
    choose W-NG-W
    new phase 2
    T₂=(8,6)
    V₂=(0,+1)
```

The returned `(8,6)` state is **not automatic**. Any claim that `THEN` has proven a mandatory phase-2 cycle would overstate the current findings.

---

## 13. A numeric connection to the previously recovered phrase

Calculate the 0-based rune-index sum of the preceding three words:

```text
SEE  = S(15) + E(18) + E(18) = 51
YOU  = Y(26) + O(3)  + U(1)  = 30
SOON = S(15) + O(3)  + O(3) + N(9) = 30

GP(SEE YOU SOON) = 51+30+30 = 111
```

Apply Euler totient:

```text
111 = 3×37
φ(111)=72
```

The generated **active key** of `THEN` sums to:

```text
E-IA-IA

E(18)+IA(27)+IA(27)=72
```

So:

```text
φ(GP(SEE YOU SOON))
=
φ(111)
=
72
=
Σ(active key for THEN)
```

Among the **212 distinct active keys** produced by standard symmetric mirror generators in the full grid, only **two** have sum `72`:

```text
E-IA-IA
Y-L-Y
```

A second exact arithmetic property is:

```text
GP(THEN) = TH(2)+E(18)+N(9) = 29
```

That is equal to the cipher modulus `29`.

For completeness:

```text
Σ(ciphertext L-T-W)=20+16+7=43
Σ(active key E-IA-IA)=18+27+27=72
43−72=-29
```

Two of the three individual subtractions wrap around modulus `29`, so their corrected plaintext sum is:

```text
−29 + 2×29 = 29
```

**Evidence discipline:** the final sum identity follows from modular subtraction once the ciphertext and key are fixed; it is not an additional independent proof. The `φ(111)=72` relation was recognized *after* finding the candidate and likewise cannot be counted as an independent, pre-registered prediction.

---

## 14. Global search and negative controls

The arithmetic result is **not** globally unique just because the output spells an English word.

A reproducible full-grid enumeration used:

```text
standard mirror axes:
    horizontal
    vertical
    diagonal ↘
    diagonal ↙

all integer mirror radii
all 27×27 positions
same center φ and Möbius phase rules
all directed straight three-rune ciphertext paths
```

Observed totals:

| Search class | Count |
|---|---:|
| All standard equal-radius symmetric rune mirrors | **507** |
| Mirrors with admissible nonzero key-base values | **442** |
| Distinct active keys produced by those mirrors | **212** |
| Directed contiguous paths of exactly 3 rune cells | **5,200** |
| Key/path combinations decrypting to `TH-E-N` | **47** |
| Occurrences of directed `L-T-W` | **1** |
| Standard `IA-IA-IA` mirrors | **1** |

Thus:

```text
THEN IS NOT GLOBALLY UNIQUE AS A POSSIBLE DECRYPTION.
```

What distinguishes the **proposed local route** is not the output alone but the conjunction:

```text
frozen endpoint H(25,19)
+
phase-2 selector RIGHT-compatible
+
pre-Möbius pair (8,6)
+
RIGHT 6 → start L
+
RIGHT 8 → end W
+
midpoint (25,22) → outer IA
+
unique IA-IA-IA mirror
+
fixed φ/μ key E-IA-IA
+
exact TH-E-N result
```

As another local control, consider all admissible mirrors having at least one node within Chebyshev distance `6` of `L(25,25)`. There are **84**, producing **68** different plaintext sequences when used on this **same** `L-T-W` ciphertext. Only the `IA-IA-IA` structure in this set gives `THEN`, and its relevant outer lies at the exact halfway position between `H` and `L`.

This local specificity supports ranking the candidate for further work. It **does not** eliminate the post-selection / multiple-testing problem; the radius-6 neighborhood and midpoint criterion were not fixed independently before inspecting the result.

---

## 15. Alternatives were checked rather than silently discarded

### 15.1. Another path can also spell THEN

For example, a route reversing leftward from the same `L(25,25)` reads:

```text
L(25,25) → C(25,24) → AE(25,23)
```

Under the active key `E-T-T`:

```text
L-C-AE
-
E-T-T
=
TH-E-N
```

This key can itself be generated from a real mirror:

```text
T(7,26) —1— M(8,25) —1— T(9,24)

M=19
φ(19)=18=E
T-M-T → T-E-T
Möbius phase = 1
active key = E-T-T
```

So this is a legitimate **alternative arithmetic decoding**, not fabricated cipher material. It is weaker as the immediate handoff because it reads **LEFT** despite the endpoint selector's RIGHT-compatible sign, and its key mirror is much farther away rather than anchored at the H→L midpoint.

Other global `THEN` matches also exist; this is why the complete search count matters.

### 15.2. Why this is stronger as the next stage than DEEP

The earlier candidate `DEEP` is a mathematically valid alternative construction and should remain in exploratory notes, not be rewritten as an established stage.

Its initial chain is:

```text
H(25,19)
→ diagonal N-H-N
→ N(27,21)
→ IA(27,22)
→ read UP IA-IA-IA-B
→ DEEP
```

Its missing rule is the forced transition into `IA(27,22)` and the UP reading direction.

In contrast, the present `THEN` route uses the actual RIGHT-compatible branch and **both** coordinate values `(8,6)` to mark its ciphertext boundaries directly on the same row as the `SOON` endpoint.

It also uses the unique `IA-IA-IA` arrangement as a **key source** precisely at the halfway point, rather than as the beginning of a different ciphertext.

**The shared `IA-IA-IA` is one piece of matrix geometry with two candidate roles—not two independent confirmations.** `THEN` is preferred here for a clearer local handoff, not because `DEEP` is arithmetically wrong.

---

## 16. Why THEN is the preferred stage-16 research candidate

After locking the chapter-15 endpoint, the strongest internally coherent reconstruction is:

```text
SOON ends at H(25,19)
        |
        | phase 2
        v
T₂=(8,6), V₂=(0,+1)
        |
        | RIGHT 6, RIGHT 8 (proposed length assignment)
        v
L(25,25) - T(25,26) - W(25,27)
        |
        +--- midpoint of H→L = IA(25,22)
                              |
                              v
                        IA-IA-IA
                              |
                          φ(center)
                              v
                         IA-E-IA
                              |
                         M=(0,+1,0)
                              |
                           phase 1
                              |
                              v
                         E-IA-IA
                              |
                              v
                       L-T-W − E-IA-IA
                              |
                              v
                           TH-E-N
                              |
                              v
                            THEN
```

Three especially useful **structural** checks accompany this:

1. The directed ciphertext and the key-generating `IA-IA-IA` are both unique in the matrix under the stated scan conventions.
2. The `THEN` endpoint shares `W-NG-W` with the independently documented secondary endpoint of `SOON`.
3. **If** `W-NG-W` is selected next, its Möbius phase recovers the complete `(8,6)/(0,+1)` selector state with which this chapter began.

The **arithmetically verified** conclusion is:

```text
L-T-W − E-IA-IA (mod 29) = TH-E-N
```

The **research hypothesis** is:

```text
AS I GO THE WEATHER TURNS COLD
I MAY CRY
NOW THE IDEA OF THE END IS DEATH
SEE YOU SOON THEN
```

Line breaks are for readability, not verified original punctuation.

---

## 17. Remaining open questions

The distinction between exact observations and an established decoding algorithm is essential:

1. **Distance rule:** the coordinate selector supplies RIGHT, while `T₂=(8,6)` supplies two numbers. Why must `+6` mark ciphertext entry and `+8` its endpoint, rather than other route uses?
2. **Key-mirror choice:** does a general rule select the mirror whose outer is the exact halfway cell of the `H→L` move, *before* seeing what word its key produces?
3. **Ciphertext length:** is the number of read runes always determined by the two selected anchors, and can that be verified prospectively at other stages?
4. **Endpoint branch:** does `W(25,27)` select the local `W-NG-W` (phase 2), the larger `W-W-W` (phase 1), or neither? The state-cycle claim requires the first selection.
5. **Right boundary:** a repeated RIGHT-compatible selector at column `27` cannot by itself prescribe another ordinary rightward grid step; a boundary/turn/reflection rule remains to be justified.
6. **Statistics:** the full search produces 47 `THEN` decodings under unconstrained key/path pairing. Further evidence must reduce the candidate set using **predefined selection rules**, rather than add retrospective coincidences.

**Working evidence hierarchy:**

```text
exact grid coordinates and mirror geometry    = VERIFIED
φ, μ, active key, mod-29 decryption         = VERIFIED
same-row +6/+8 geometric alignment         = VERIFIED
interpretation of 6 and 8 as anchors        = PROPOSED
midpoint mirror as mandatory key source     = PROPOSED
THEN as intended Cicada plaintext          = UNVERIFIED
next-state return via W-NG-W                = CONDITIONAL
```

---

## 18. Reproducibility checklist

All core results are independently testable against [`../0-2-live-map.html`](../0-2-live-map.html) and the existing [`../rules/`](../rules/) files:

```text
[ ] Confirm 15-SOON ends at H(25,19), phase 2.
[ ] Compute φ²(25)=8, φ²(19)=6 and μ=(0,+1).
[ ] Confirm H(25,19), IA(25,22), L(25,25), T(25,26), W(25,27).
[ ] Scan 27×27 grid and verify the unique L-T-W run.
[ ] Scan all standard mirrors and verify unique IA-IA-IA at (25–27,22).
[ ] Compute φ(IA=27)=18=E to obtain IA-E-IA.
[ ] Compute signature (18,6,18), μ=(0,+1,0), phase 1.
[ ] Subtract E-IA-IA from L-T-W mod 29 to recover TH-E-N.
[ ] Confirm W(25,27)–NG(26,27)–W(27,27).
[ ] Compute the conditional W-NG-W phase 2 and T₂=(8,6) at W(25,27).
[ ] Check the competing W-W-W mirror and its phase 1.
[ ] Preserve the caveat that THEN is not globally unique in free key/path searches.
```

**Result:** `THEN` is currently the **preferred, reproducibly supported candidate for stage 16**, while a unique, predictive end-to-end route-selection algorithm remains unfinished.
