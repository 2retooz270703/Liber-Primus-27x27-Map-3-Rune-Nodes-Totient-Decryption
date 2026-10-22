# 19 — KEY

*Candidate continuation after THEN: **THE KEY IS TO GO …***

This is **candidate block 19**, following the proposed **THE** at block 18. It is **not** part of the original 17-block reconstruction, which ends at **THEN**; **DEATH** occurs at block 13. That initial reconstruction supplies 16 recorded transitions used to develop and evaluate Reports 01–06.

The proposed ciphertext is `N–L–EA`, read **upward** and decrypted with `R–TH–TH` to obtain the rune sequence **`C/K · E · Y`**, read here as **KEY**.

The calculation retains the basic operations from Report 00: **center-totient key derivation, Möbius rotation, and subtraction modulo 29**. The early **coordinate selector** and **CENTER/OUTER endpoint heuristic** from Report 00 are **not mandatory tests after THEN**. The proposed transition is checked instead against **Reports 01–06**, as in block 18. Agreement with these reports demonstrates consistency with the selected model, **not proof that the plaintext is unique or authentic**.

**Notation:** Coordinates are **1-based** `(row, column)` in the 27 × 27 matrix. Rune values are indices in the **29-rune alphabet**, not Gematria Primus prime values. `φ` is Euler's totient function and `μ` is the Möbius function. For rotations of cell coordinates, we use:

- `n₀(r,c) = 27(r − 1) + c` — original row-major index.
- `n₁(r,c) = 27(c − 1) + 28 − r` — index after a 90° clockwise rotation.
- `n₂(r,c) = 730 − n₀(r,c)` — index after a 180° rotation.
- `n₃(r,c) = 27(27 − c) + r` — index after a 270° clockwise rotation.

## 1. Locate the original key node

The selected source is a **vertical `TH–H–TH` mirror** centered on **`H (12,16)`**:

| Mirror | Upper outer | Center | Lower outer | Radius |
|:---|:---:|:---:|:---:|:---:|
| `TH–H–TH` | TH (11,16) | **H (12,16)** | TH (13,16) | **1 row** |

Both outer runes are in column **16**, one row from the center. Their midpoint is `(11 + 13) / 2 = 12`, so the mirror geometry is exact.

This is the **chosen original node**, before the center rune is transformed. The mathematical rules will test its derived signature and center parity. They do **not** uniquely identify this node without additional constraints; an alternative source node is discussed in Section 6.

## 2. Derive and align the decryption key

### Transform the center rune

Keep the two outer `TH` runes. Replace the center `H` by the rune indexed by its totient:

`H = 8 → φ(8) = 4 → R`

The unrotated key is:

`TH–H–TH → TH–R–TH`

### Calculate the Möbius signature

Apply `φ` and then `μ` to each **derived key** index:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| TH | 2 | φ(2) = 1 | μ(1) = **+1** |
| R | 4 | φ(4) = 2 | μ(2) = **−1** |
| TH | 2 | φ(2) = 1 | μ(1) = **+1** |

**Totient signature:** `(1, 2, 1)`  
**Möbius signature:** `(+1, −1, +1)`

The cyclic left-rotation phase is:

`p = (1 − 1 + 1) mod 3 = 1`

Rotate the key **one position to the left**:

`TH–R–TH → R–TH–TH`

**Final repeating decryption key: `R–TH–TH`.**

## 3. Predict the next key from the preceding THE

Report 01 predicts the next key's **signature and phase before the next original node is chosen**. For this test, the preceding proposed **THE** must be treated as the current block:

| Current THE component | Coordinate | Role |
|:---|:---:|:---|
| J | (22,21) | Ciphertext **beginning** |
| W | (21,20) | Ciphertext **endpoint** and **leftmost cell** |
| M | (20,17) | **Original key-node center** (`N–M–N`) |

The current **THE** key has signature `(+1,+1,+1)`, outer state `a = 1`, and phase **0**. The cumulative phase total after the proposed `THEN → THE` transition is **`S = 18`**, so the next prediction still uses the **Reflected/+1** mode from Report 01.

### Predict the next phase

Reflect the current ciphertext cells through 180°:

| Current cell | `n₀` | `n₂ = 730 − n₀` | Möbius value |
|:---|---:|---:|:---:|
| J (22,21) | 588 | 142 | μ(142) = **+1** |
| W (21,20) | 560 | 170 | μ(170) = **−1** |

The Reflected/+1 formula gives:

`p_next = [1 + μ(142) + μ(170)] mod 3 = (1 + 1 − 1) mod 3 = 1`

Thus the **predicted next phase is 1**, before selecting the `TH–H–TH` mirror. The cumulative total would become **`S = 19`**.

### Predict the outer signature

THE's leftmost cell is `W (21,20)`. Its 90°-rotated index is:

`n₁(21,20) = 27(20 − 1) + 28 − 21 = 520`

Since `520` contains a squared prime factor, `μ(520) = 0`. The outer state therefore stays unchanged:

`a_next = (1 + 0) mod 2 = 1`

The middle component is fixed by the phase:

`b_next ≡ p_next − 2a_next = 1 − 2 ≡ 2 (mod 3) → −1`

**Report 01 prediction: `(+1, −1, +1)`, phase 1.** This matches the key `TH–R–TH` derived independently from the selected mirror in Section 2. The prediction fixes a numerical signature, **not a unique key or a unique mirror**.

## 4. Predict the ciphertext axis and locate the candidate

### Determine the reading direction (Reports 02–03)

The current THE ciphertext has beginning `B = (22,21)`, endpoint `E = (21,20)`, and original node center `M = (20,17)`.

For Report 03's **axis rule**:

`A = n₂(B) + n₀(M) = 142 + 530 = 672`

`G = gcd(n₁(E), n₂(E)) = gcd(520,170) = 10`

Because `μ(672) = 0` and `μ(10) = +1`:

`q_axis = μ(A) + μ(G) = 0 + 1 = +1 → VERTICAL`

Report 02's **leftmost-boundary rule** uses the preceding endpoint and the **original** THE center index `M = 19`, not the transformed key center:

`n₃(E) = n₃(21,20) = 210`, with `μ(210) = +1`.

`τ_next = [μ(210) + φ(19)] mod 2 = (1 + 18) mod 2 = 1 → BEGINNING`

For a **vertical** segment, the tie-break definition of *leftmost cell* selects the **bottommost** cell. When that cell is the **BEGINNING**, the ciphertext must be read **upward**.

**Predicted reading geometry: VERTICAL, UPWARD, leftmost cell at the BEGINNING.** These formulas constrain the axis and ordering; they do not predict a particular column or length.

### Select and test the proposed three-rune segment

The selected segment occupies **column 4**:

| Reading order | Cell | Rune | Role |
|:---:|:---:|:---:|:---|
| 1 | **(21,4)** | **N** | Beginning and leftmost cell |
| 2 | (20,4) | L | Middle cell |
| 3 | **(19,4)** | **EA** | Endpoint |

It is read:

`N (21,4) → L (20,4) → EA (19,4)` **(UPWARD)**

This follows the predicted direction. All three cells share column 4, so the bottommost one, **`N (21,4)`**, is the geometrically defined leftmost cell for a vertical ciphertext.

### Check the incoming Möbius-gated ray (Report 06)

Report 06 compares the **previous leftmost cell** `W (21,20)` with the **new beginning** `N (21,4)`. These two cells are on the same row, separated by **16 columns**:

`Δ = (21,4) − (21,20) = (0, −16)`

The distance from this displacement to the nearest of the eight compass rays is:

`d₈ = min(|0|, |−16|, ||0| − |−16||) = 0`

The allowance comes from the **previous endpoint**, also `W (21,20)`:

- `n₀(21,20) = 560`, so `μ(560) = 0`.
- `n₃(21,20) = 210`, so `μ(210) = +1`.

Both values are **not** zero, so Report 06 gives **`q = 0`**: no off-ray deviation is permitted.

**`d₈ = 0 ≤ q = 0` — pass.** This is an **exact horizontal incoming ray**, even though the **new ciphertext itself is read vertically upward**. Those are two different geometric directions: the first connects successive blocks; the second is the reading axis *within* KEY.

## 5. Read and decrypt

Repeat `R–TH–TH` along the selected upward ciphertext. Subtract each key-rune index **modulo 29**:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (21,4) | N = 9 | R = 4 | 9 − 4 ≡ 5 | **C/K** |
| (20,4) | L = 20 | TH = 2 | 20 − 2 ≡ 18 | **E** |
| (19,4) | EA = 28 | TH = 2 | 28 − 2 ≡ 26 | **Y** |

## Result

**Decrypted rune sequence:** `C/K · E · Y`  
**Proposed English reading: KEY**

The first output is **rune index 5**, represented by a **shared C/K rune** in this alphabet. Interpreting it as the English letter **K** yields **KEY**; the modular calculation alone returns the rune, **not a unique Latin spelling**. This distinction is important when evaluating whether the plaintext was predicted or recognized after decryption.

All three modular subtractions are exact for the selected source node and ciphertext.

## 6. Verification against Reports 01–06

The checks below are conditional on accepting **block 18 — THE** as the preceding ciphertext. They are **outside** the original 16-transition fitting set.

| Report | Predicted constraint after THE | Check on this KEY candidate | Result |
|:---|:---|:---|:---:|
| **01 — Next key signature** | `(+1,−1,+1)`, phase **1** | `TH–R–TH` has `(1,2,1) → (+1,−1,+1)`; phase 1 | **Pass** |
| **02 — Leftmost cell and rotations** | Leftmost = **BEGINNING**; reflected-mode `μ(n₁(L′)) ∈ {0,−1}` | Beginning `N (21,4)`; `n₁ = 88`, `μ(88) = 0` | **Pass** |
| **03 — Reading axis and direction** | **VERTICAL**, with leftmost = BEGINNING → **UP** | `N (21,4) → EA (19,4)` is vertical upward | **Pass** |
| **04 — Next center parity** | **Even row / even column** | `H (12,16)` is even/even | **Pass** |
| **05 — Next ciphertext row parity** | Endpoint **odd**, leftmost **odd** | Endpoint `EA (19,4)` and leftmost `N (21,4)` are both in odd rows | **Pass** |
| **06 — Incoming ray** | `d₈ ≤ q`, with `q = 0` | `d₈ = 0` from `W (21,20)` to `N (21,4)` | **Pass** |

The parity checks can be reproduced directly from the previous THE block:

- **Report 04 — column:** `c′ ≡ 1 + r(B) + r(E) + r(M) = 1 + 22 + 21 + 20 = 64 ≡ 0 (mod 2)`.
- **Report 04 — row:** `r′ ≡ 1 + c(B) + r(E) + r(M) + μ(n₂(B)) = 1 + 21 + 21 + 20 + 1 = 64 ≡ 0 (mod 2)`.
- **Report 05 — endpoint row:** `r(E′) ≡ 1 + p + μ(n₂(M)) = 1 + 0 + μ(200) = 1 (mod 2)`.
- **Report 05 — leftmost row:** `r(L′) ≡ r̂(M′) + 1 + p + μ(r(M)) = 0 + 1 + 0 + μ(20) = 1 (mod 2)`.

**Interpretation:** The selected candidate satisfies all six stated reports. Some checks reuse inputs or derived values—for example, Report 03's boundary orientation uses Report 02, and Report 05 uses Report 04's center-row prediction. These are **not six independent statistical tests**. Passing them does not establish that the chosen key node, ciphertext cells, or English word are unique.

## 7. Additional geometric connections

### The KEY start shares a diagonal with candidate IS and TO

For an anti-diagonal of this matrix, the coordinate sum `r + c` is constant. The proposed KEY beginning, together with the coordinates associated with subsequent **IS** and **TO** candidates, all satisfy **`r + c = 25`**:

| Proposed use | Cell | Coordinate | `r + c` |
|:---|:---:|:---:|---:|
| **KEY** beginning | N | (21,4) | **25** |
| **IS** candidate | OE | (19,6) | **25** |
| **IS** candidate | X | (18,7) | **25** |
| **TO** candidate | U | (9,16) | **25** |
| **TO** candidate | NG | (8,17) | **25** |

The shared diagonal is a **verifiable coordinate relationship**. It is not an independent decryption of **IS** or **TO** in this file, nor proof that Cicada intended the placement.

### A second original mirror produces the same key

Another vertical node can also generate `TH–R–TH`:

| Original mirror | First outer | Center | Second outer | Radius |
|:---|:---:|:---:|:---:|:---:|
| `TH–I–TH` | TH (4,2) | **I (12,2)** | TH (20,2) | **8 rows** |

Since `I = 10` and `φ(10) = 4 = R`, its derived key is also **`TH–R–TH`**, with the same signature and rotation. Its center **`(12,2)`** is likewise **even/even**. Thus **Reports 01 and 04 alone do not distinguish these two original nodes**.

The source notes report that, when the following **IS** candidate and the full 01–06 transition checks are included in a mirror-node enumeration, **only `H (12,16)` permits that continuation**. The enumeration and its candidate count are **not reproduced here**; this is a conditional claim about the wider proposed branch, not a uniqueness proof supplied by the KEY decryption itself.

## 8. Status of the continuation

**Established within this candidate:** the selected `TH–H–TH` mirror, key derivation `TH–R–TH → R–TH–TH`, upward ciphertext `N–L–EA`, exact modulo-29 output `C/K · E · Y`, and the reported 01–06 constraints are mutually consistent.

**Still open:** whether this source node and ciphertext are singled out *without knowing the desired English phrase*, whether the common C/K rune is intended to be read as **K** here, and whether subsequent blocks **IS TO GO** can be generated with the same fixed constraints and no discretionary additions.
