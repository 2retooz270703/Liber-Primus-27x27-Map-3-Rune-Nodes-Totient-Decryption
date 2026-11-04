# 34 — YOU

*Selected continuation: **LIFE MAY BE THE DEATH OF YOU***

The mirror `H–R–H` has its center transformed to produce `H–TH–H`. Phase 1 aligns it as `TH–H–H`. Three ciphertext cells read rightward on row 6 decrypt as **Y·O·U**, completing **LIFE MAY BE THE DEATH OF YOU**.

**Conventions:** Coordinates are 1-based `(row, column)` in the 27 × 27 matrix. Rune indices are 0–28; GP values are the corresponding prime weights. `B`, `E`, `L`, and `M` denote the beginning, endpoint, leftmost ciphertext cell, and original key-node center. The leftmost tie-break is the bottommost cell. Method and rotation conventions follow [Report 00](../Start-reading-here/00-decryption-method.md).

| Position index | Formula |
|:---|:---|
| `n₀(r,c)` | `27(r−1)+c` |
| `n₁(r,c)` | `27(c−1)+28−r` |
| `n₂(r,c)` | `730−n₀(r,c)` |
| `n₃(r,c)` | `27(27−c)+r` |

## 1. Locate the original source node

| Role | Coordinate | Matrix rune | Index |
|:---|:---:|:---:|---:|
| Left outer | (21,17) | H | 8 |
| **Center** | (21,22) | R | 4 |
| Right outer | (21,27) | H | 8 |

This is a **horizontal** source with radius **5 columns**. Its outer runes are **equal**, so the original node is **MIRROR** under [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md). The center is `M=(21,22)`, with `n₀(M)=562`.

## 2. Derive and align the key

Apply the totient **only to the original center**: `R=4 → φ(4)=2=TH`. Keep both outer indices unchanged.

**`H–R–H → H–TH–H`**.

Calculate the signature on the **unrotated derived key**:

| Derived rune | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|:---:|
| H | 8 | 4 | 0 |
| TH | 2 | 1 | +1 |
| H | 8 | 4 | 0 |

**Signature:** `(0,+1,0)`. **Phase:** `p=(1) mod 3=1`.

Rotate the key **left by 1 position**: `H–TH–H → TH–H–H`. The aligned numerical key is **`(2, 8, 8)`**.

The consumed stream is **`TH–H–H`** across **3 ciphertext runes**.

## 3. Predict the signature from OF (33)

The preceding block has `B=(12,18)`, `E=(12,17)`, `L=(12,17)`, original center `M=(9,17)`, phase **2**, outer state **a=0**, and **S=27**. Under [Report 01](../Start-reading-here/01-next-key-signature.md), `21≤S<28` selects **Direct/+0**.

| Previous ciphertext cell | `n₀` | `μ(n₀)` |
|:---|---:|:---:|
| H(12,18) | 315 | 0 |
| AE(12,17) | 314 | +1 |

`p_next=Σμ(n₀) mod 3=(1) mod 3=1`.

The outer-state selector is `n₁(L)=448`, with `μ(448)=0`. Therefore `a_next=(0+(0)) mod 2=0`.

**Predicted signature: `(0,+1,0)`; predicted phase: `1`.** These match the selected key. The accumulated total becomes **`S=27+1=28`**.

## 4. Predict the ciphertext axis and reading direction

Apply [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md) to the **previous** block:

`A=n₂(B)+n₀(M)=415+233=648`, with `μ(A)=0`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(448,416)=32`, with `μ(G_axis)=0`.

`q_axis=μ(A)+μ(G_axis)=0` → **HORIZONTAL**.

For the boundary rule in [Report 02](../Start-reading-here/02-leftmost-cell-and-rotations.md), use the **original** center index `h=8`:

`τ_next=[μ(n₃(E))+φ(h)] mod 2=[−1+4] mod 2=1`.

The next leftmost cell must be the **BEGINNING**. The selected ciphertext reads **rightward**, from `EA(6,11)` to `N(6,13)`, with `L=(6,11)`.

The incoming calculation is defined at **S=27**. At the resulting **S=28**, the local selector is `n₁(L)=292`, `μ(292)=0`. Zero is allowed in **both** documented classes, so this terminal check does not require an invented phase mode at S=28.

## 5. Check center, boundary, ray, mirror, and length constraints

| Rule | Prediction from the preceding block | Selected placement |
|:---|:---|:---|
| [Report 04](../Start-reading-here/04-predicting-next-key-center-parity.md) — center row/column | odd row / even column | `M=(21,22)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — endpoint row | even | `E=(6,13)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — leftmost row | even | `L=(6,11)` — **pass** |
| [Report 09](../Start-reading-here/09-predicting-next-ciphertext-column-parity.md) — leftmost column | odd | Column 11 — **pass** |
| [Report 06](../Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) — incoming ray | `Δ=(−6,-6)`, `d₈=0`, allowance `0` | `0≤0` — **pass** |
| [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md) — original node type | `d∞=4`, `d∞ mod 3=1` → MIRROR | Equal outer runes — **pass** |
| [Report 08](../Start-reading-here/08-minimum-ciphertext-block-length.md) — minimum block length | At least 2 runes | 3 runes — **pass** |

The center parity totals are `r(M′)≡41≡1 (mod 2)` and `c(M′)≡34≡0 (mod 2)`. The endpoint/leftmost row totals are `4→0` and `4→0`.

For Report 09, the previous ciphertext gives `Σμ(n₁(C))=0`, mirror bit `0`, and center term `−1`. Thus `c(L′)≡12+(0)+0+(−1)≡11≡1 (mod 2)`.

The ray is measured from the previous `L=(12,17)`. Its allowance is evaluated at the previous `E=(12,17)`: `μ(n₀(E))=+1; μ(n₃(E))=−1`. The mirror distance uses the previous lower/right outer cell `Z=(9,21)`.

## 6. Verify the four squarefree-GCD conditions

Use the **original center** `M=(21,22)` and the current block's `B`, `L`, and `E`, as defined in [Report 10](../Start-reading-here/10-squarefree-gcd-compatibility.md).

| Condition | Compared indices | GCD | `μ(GCD)` |
|:---|:---|---:|:---:|
| G1: `n₀(M), n₀(B)` | 562, 146 | 2 | −1 |
| G2: `n₀(M), n₀(L)` | 562, 146 | 2 | −1 |
| G3: `n₁(M), n₃(E)` | 574, 384 | 2 | −1 |
| G4: `n₀(M), n₂(E)` | 562, 582 | 2 | −1 |

**All four GCDs are squarefree.** A GCD greater than 1 is allowed; it must have no repeated prime factor.

## 7. Read and decrypt

| Order | Cipher cell | Ciphertext index C | Repeated key index K | `(C−K) mod 29` | Plaintext |
|---:|:---:|:---|:---|:---|:---:|
| 1 | (6,11) | EA = 28 | TH = 2 | `28−2=26` | **Y** |
| 2 | (6,12) | J = 11 | H = 8 | `11−8=3` | **O** |
| 3 | (6,13) | N = 9 | H = 8 | `9−8=1` | **U** |

**Result: `Y · O · U` → YOU. Phase `p=1`; accumulated `S=28`.**

| Counting basis | Rune-index sum | GP sum |
|:---|---:|---:|
| Ciphertext actually read | 48 | 175 |
| Key components actually consumed | 18 | 51 |
| Plaintext produced | 30 | 113 |

## 8. The final node and the reflected ciphertext

The original `H–R–H` node at `(21,17)–(21,22)–(21,27)` is also used in the earlier [IS (12)](12-is.md). The source and aligned `TH–H–H` key recur; the present ciphertext is different.

MAY reads `(18,11)→(18,13)`, while YOU reads `(6,11)→(6,13)`. The exact reflection `(r,c)→(24−r,c)` maps the ordered MAY cells to the ordered YOU cells. Its fixed line is **row 12**, which contains the entire intervening OF block `(12,18)→(12,17)`.

Among MAY, BE, THE, DEATH, OF, and YOU, no ciphertext cell is repeated. The middle MAY cell `(18,12)` was already used inside MAPLIFE; the middle YOU cell `(6,12)` was used by the earlier OF (26). Those are overlaps with the preceding route, not repetitions between the six new blocks.

## 9. Plaintext totals and the last key

| Plaintext unit | Words | Runes | Rune-index sum | GP |
|:---|---:|---:|---:|---:|
| LIFE | 1 | 4 | 48 | 173 |
| MAY BE THE DEATH OF YOU | 6 | 15 | 210 | 796 |
| **LIFE MAY BE THE DEATH OF YOU** | **7** | **19** | **258** | **969** |

The rune sequence is `L·I·F·E · M·A·Y · B·E · TH·E · D·EA·TH · O·F · Y·O·U`. TH and EA each count as one rune.

Several exact correspondences use these fixed counting conventions:

- `210=2×3×5×7`, and **`φ(210)=48=Σindices(LIFE)`**. The YOU ciphertext indices `(28,11,9)` also sum to **48**.
- The consumed YOU key is `TH–H–H`, with **GP=5+23+23=51**. Thus **`969=19×51`**: the GP of the complete sentence equals its rune count times the GP of its final three-rune key.
- **`969=C(19,3)=19×18×17/6`**, the number of three-position choices from 19 positions. This is an additional description of the same GP total, not an independent new sum.
- **`φ(969)=576`**. The preceding selected segment TO THE EAST OF THE MAP uses consumed key GP **106+100+163+46+42+119=576**. Here MAP means the first three cells inside MAPLIFE; the extra LIFE cells are not counted in that earlier segment.
- The original last key has index sum `8+4+8=20`, the index of **L**, the first rune of LIFE. Its transformed key has sum `8+2+8=18`, the index of **E**, the last rune of LIFE. The original key's GP is `23+11+23=57=3×19`.
- Plaintext YOU has index sum **30** and GP **113**, the **30th prime**. The first MAY ciphertext has GP `17+13+83=113` as well.

The observations above share some of the same totals and are not statistically independent.

## 10. Coordinate sums and the 729-cell matrix

For this section, count the **15 ciphertext cells after LIFE**, from MAY through YOU. The rows and columns are the original 1-based coordinates; the consumed key stream has one value per ciphertext cell.

| Block | Sum of rows | Sum of columns | Cipher index sum | Consumed key index sum | Cipher GP | Consumed key GP |
|:---|---:|---:|---:|---:|---:|---:|
| MAY | 54 | 36 | 33 | 51 | 113 | 191 |
| BE | 51 | 23 | 5 | 28 | 14 | 96 |
| THE | 22 | 23 | 36 | 45 | 132 | 176 |
| DEATH | 33 | 27 | 25 | 30 | 92 | 105 |
| OF | 24 | 35 | 33 | 30 | 124 | 114 |
| YOU | 18 | 36 | 48 | 18 | 175 | 51 |
| **Total** | **202** | **180** | **180** | **202** | **650** | **733** |

The selected route therefore satisfies the exact integer equalities:

**`Σcolumns=Σcipher indices=180`** and **`Σrows=Σconsumed key indices=202`**.

The GP totals also give:

**`733−4=729=27²`**, where 4 is the rune count of LIFE.

**`969−φ(650)=969−240=729=27²`**, where 969 is the GP of the complete 19-rune sentence, and 650 is the GP of the 15 ciphertext cells after LIFE.

These relations use consumed key components and survive the three validated BE-source configurations. In contrast, the full-key sum 223 and the identity `φ(798)=216=6³` depend on an unused third component of BE and are not used as source-independent evidence.

### Retrospective endpoint check without a dictionary

After all **13** canonical placements of MAY BE THE DEATH OF, every admissible next straight block of **2–27 runes** was enumerated under Reports 01–10. Neither YOU nor a three-rune length was supplied:

| Accumulated constraints | Ciphertext/source assignments retained |
|:---|---:|
| Reports 01–10 | 80,341 |
| + the two coordinate-sum equalities | 3 |
| + consumed key GP = 729 + rune count of LIFE | **1** |
| + complete sentence GP − φ(ciphertext GP) = 729 | **1** |

The unique retained block is **Y·O·U**, at `(6,11)→(6,13)`, with original center `(21,22)`. An independent node-and-coordinate enumerator reproduced these counts.

With reversed source orders allowed, **75** prefix configurations and **466,437** endpoint assignments produce **3** retained source configurations, all with the same YOU ciphertext and plaintext. The two GP=729 relations alone retain two literal endings; the coordinate constraints are also needed for the combined selection.

These endpoint constraints were identified after YOU was found. The experiment is a retrospective consistency/selection check, not a prediction on unseen plaintext or proof of authorial intent. Its search domain excludes F=0 key components and does not extrapolate a phase mode beyond S=28.

## 11. Does the reading continue after YOU?

The incoming phase is computed from OF at **S=27** and gives the present **S=28**. Report 01 does not define an outgoing phase mode at S=28. The current selector `μ(n₁(6,11))=μ(292)=0` passes both documented orientation classes, but it does not define a new phase regime.

The geometry formulas that do not depend on S still yield a partial forecast:

| Next-block property | Prediction from YOU |
|:---|:---|
| Axis | Diagonal: `A=1146`, `G_axis=2`, `μ(A)+μ(G_axis)=−2` |
| Reading boundary | `τ=0`: leftmost is the END; up-left or down-left |
| Original key center | Odd row / even column |
| Endpoint and leftmost rows | Both even |
| Leftmost column | Odd |
| Original node type | MIRROR |
| Incoming anchor and allowance | From `(6,11)`, with `d₈≤1` |
| Signature and phase | Not specified without extending Report 01 |

Thus **S=28 does not establish that the plaintext has ended**. No following word or outgoing phase is claimed here.

## 12. Complete selected reading

> As I go, the weather turns cold.  
> I may cry now.  
> The idea of the end is death.  
> See you soon, then.  
> The key is to go to the east of the map.  
> Life may be the death of you.

Under this word segmentation, the complete reading contains **40 words**, **105 runes**, rune-index sum **1295**, and GP **4709**. Word boundaries, spelling choices for shared rune labels, and punctuation are editorial.

**Status:** The specified source, exact modular subtraction, and stated incoming checks are verified for this selected placement. Numerical correspondences describe the selected route; their design intent is not established.

---

[← Previous: OF](33-of.md) · [Decryption method](../Start-reading-here/00-decryption-method.md)
