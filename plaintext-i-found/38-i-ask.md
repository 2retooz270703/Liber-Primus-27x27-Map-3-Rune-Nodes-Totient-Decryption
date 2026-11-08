# 38 — I ASK

*Candidate continuation: **GO DO AS I ASK***

The non-mirror source `T–M–EA` is used directly at phase 0. Four consecutive ciphertext cells read downward and decrypt as **I·A·S·C/K**, read as **I ASK**. The two words share one continuous four-rune block and one repeating key stream.

**Conventions:** Coordinates are 1-based `(row, column)` in the 27 × 27 matrix. Rune indices are 0–28; GP values are the corresponding prime weights. `B`, `E`, `L`, and `M` denote the ciphertext beginning, endpoint, leftmost cell, and original source center. Ties for `L` select the bottommost cell. `Z` is the lower outer source cell, or the right outer cell for a horizontal source, **regardless of source reading order**. Key alignment follows [Report 00](../Start-reading-here/00-decryption-method.md); phase forecasting beyond `S=28` uses the cyclic extension in [Report 11](../Start-reading-here/11-seven-thresholds-and-cyclic-phase-modes.md).

| Position index | Formula |
| --- | --- |
| `n₀(r,c)` | `27(r−1)+c` |
| `n₁(r,c)` | `27(c−1)+28−r` |
| `n₂(r,c)` | `730−n₀(r,c)` |
| `n₃(r,c)` | `27(27−c)+r` |

The indices `n₁`, `n₂`, and `n₃` number the same physical cell after 90°, 180°, and 270° clockwise rotations. These positional rotations do not reorder a source key or change the ciphertext reading direction.

## 1. Locate the original source node

| Role in key order | Coordinate | Matrix rune | Index |
| --- | :---: | :---: | ---: |
| Upper outer | (11,13) | T | 16 |
| **Center** | (12,13) | M | 19 |
| Lower outer | (13,13) | EA | 28 |

The source lies on the **vertical (N–S)** axis and has radius **1 grid step**. Its outer indices are different, so its original type is **NON-MIRROR**. The center is **`M=(12,13)`**, with **`n₀(M)=310`**. The source is read **downward**.

## 2. Derive and align the key

Use **`T–M–EA`** directly. No center transformation is applied in the main walkthrough.

Calculate the signature on the **unrotated derived key**:

| Derived rune | Index | φ(index) | μ(φ(index)) |
| :---: | ---: | ---: | ---: |
| T | 16 | 8 | 0 |
| M | 19 | 18 | 0 |
| EA | 28 | 12 | 0 |

**Signature:** `(0, 0, 0)`. **Phase:** `p=(0) mod 3=0`.

Phase **0** leaves the derived order unchanged. The aligned key is **`T–M–EA = (16, 19, 28)`**.

Across this 4-rune block, the actually consumed stream is **`T–M–EA–T = (16, 19, 28, 16)`**.

The three-rune key is repeated to cover the fourth ciphertext cell. Thus the full key `T–M–EA` has **index sum 63, GP 239**, whereas the consumed stream `T–M–EA–T` has **index sum 79, GP 298**. These are distinct counting scopes.

## 3. Predict the signature from AS (37)

The preceding block has `B=(22,2)`, `E=(22,1)`, `L=(22,1)`, original source center `M=(6,16)`, phase **2**, outer state **`a=1`**, and accumulated state **`S=32`**.

[Report 01](../Start-reading-here/01-next-key-signature.md) supplies the signature selector. [Report 11](../Start-reading-here/11-seven-thresholds-and-cyclic-phase-modes.md) extends the phase schedule using the cycle index `q_cycle=floor(S/7) mod 4`. At `S=32`, **`q_cycle=0`**, selecting **Direct/+1** for this incoming forecast.

| Previous ciphertext cell | n₀ | μ(n₀) |
| --- | ---: | ---: |
| N(22,2) | 569 | −1 |
| Y(22,1) | 568 | 0 |

`p_next=(1+Σμ(n₀)) mod 3=(1+(-1)) mod 3=0`.

The outer-state selector is `n₁(L)=6`, with `μ(6)=+1`. Therefore `a_next=(1+(1)) mod 2=0`.

**Predicted signature: `(0, 0, 0)`; predicted phase: `0`.** Both match the selected derived key. Update S only after this forecast: **`S=32+0=32`**.

The no-skipping condition from Report 11 also passes: `32 mod 7=4`; this transition does not jump strictly across a multiple of seven. The resulting local mode at `S=32` remains **Direct/+1**.

## 4. Predict the ciphertext axis and reading direction

Using the previous block in [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md):

`A=n₂(B)+n₀(M)=161+151=312`, with `μ(A)=0`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(6,162)=6`, with `μ(G_axis)=+1`.

`μ(A)+μ(G_axis)=1` → **VERTICAL**.

For the boundary rule in [Report 02](../Start-reading-here/02-leftmost-cell-and-rotations.md), the previous **original** center index is `h=17`:

`τ_next=[μ(n₃(E))+φ(h)] mod 2=[0+16] mod 2=0`.

The next leftmost cell must be the **END**. The selected ciphertext reads **downward**, `(5,17) → (6,17) → (7,17) → (8,17)`, with **`L=(8,17)`**.

For a vertical ciphertext, all cells share the same column. The bottommost tie-break makes L the lower endpoint `(8,17)`. Therefore `τ=0` means reading **from top to bottom**, not reading leftward.

The local leftmost-mode check is `n₁(L)=452`, `μ(452)=0`. This passes the Direct class, which allows `μ(n₁(L))∈{0,+1}`.

## 5. Check parities, ray offset, node type, and length

| Rule | Incoming prediction | Selected placement |
| --- | --- | --- |
| [Report 04](../Start-reading-here/04-predicting-next-key-center-parity.md) — source center | even row / odd column | `M=(12,13)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — endpoint row | even | `E=(8,17)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — leftmost row | even | `L=(8,17)` — **pass** |
| [Report 09](../Start-reading-here/09-predicting-next-ciphertext-column-parity.md) — leftmost column | odd | Column 17 — **pass** |
| [Report 06](../Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) — ray allowance | `d₈≤1` | `d₈=1` — **pass** |
| [Report 12](../Start-reading-here/12-predicting-exact-ray-deviation.md) — exact ray offset | `d₈=1` | `d₈=1` — **pass** |
| [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md) — original node type | NON-MIRROR | Outer indices `16`, `28` — **pass** |
| [Report 08](../Start-reading-here/08-minimum-ciphertext-block-length.md) — minimum block length | At least 2 runes | 4 runes — **pass** |

The ray anchor is the previous **`L=(22,1)`**, with displacement `Δ=(-17,+16)`. The geometric score is `d₈=min(|Δr|,|Δc|,||Δr|−|Δc||)=1`.

Report 06 gives the ray allowance `q_ray=1` from `μ(n₀(E_prev))=0` and `μ(n₃(E_prev))=0`. Report 12 gives the beginning-derived zero indicator `z=0`, so its required exact offset is `q_ray and not z=1`. This ray allowance is separate from the phase-cycle index in Section 3.

For Report 07, the previous geometrically defined `Z=(8,18)` is at Chebyshev distance **17** from the previous L. Since `17 mod 3=2`, the forecast is **NON-MIRROR**, matching this source.

## 6. Verify the four squarefree-GCD conditions

Apply [Report 10](../Start-reading-here/10-squarefree-gcd-compatibility.md) to the selected **original** source center and the selected ciphertext.

| Condition | Compared indices | GCD | μ(GCD) |
| --- | --- | ---: | ---: |
| G1: n₀(M), n₀(B) | `310, 125` | 5 | −1 |
| G2: n₀(M), n₀(L) | `310, 206` | 2 | −1 |
| G3: n₁(M), n₃(E) | `340, 278` | 2 | −1 |
| G4: n₀(M), n₂(E) | `310, 524` | 2 | −1 |

**All four GCDs are squarefree.** A GCD greater than 1 is allowed; it must have no repeated prime factor.

## 7. Check the exact source axis and radius parity

For [Report 13](../Start-reading-here/13-predicting-next-key-axis-group.md), calculate the group bit from the previous source and ciphertext:

`X=n₁(M_prev)+n₂(Z_prev)=950`, `μ(X)=0`; `Y=n₁(L_prev)+n₂(Z_prev)=529`, `μ(Y)=0`.

The negativity indicators agree, so **`b=1`**. Zero is nonnegative in this comparison.

[Report 14](../Start-reading-here/14-predicting-exact-next-key-axis.md) supplies the diagonal bit:

| Argument | Value | μ(value) | Bit test |
| --- | ---: | ---: | --- |
| `G=gcd(n₁(M_prev),n₃(Z_prev))` | 1 | +1 | `[μ(G)<0]=0` |
| `T=GP(previous original source)` | 145 | +1 | `[μ(T)>0]=1` |
| `A=n₀(M_prev)+n₃(Z_prev)` | 402 | −1 | `[μ(A)≠0]=1` |

`d=0 XOR 1 XOR 1=0`. Therefore **`axis_next=2b+d=2`**, the **vertical (N–S)** source axis. The selected source passes.

For [Report 15](../Start-reading-here/15-predicting-next-key-radius-parity.md), the three radius-parity bits are:

| Term | Calculation | Bit |
| --- | --- | ---: |
| Checkerboard difference | `(6+16+22+2) mod 2` | 0 |
| Negative Möbius GCD | `gcd(n₂(Z_prev),n₂(L_prev))=1`; `μ(1)=+1` | 0 |
| Positive Möbius sum | `n₁(B_prev)+n₁(E_prev)=39`; `μ(39)=+1` | 1 |

`R_next mod 2=0 XOR 0 XOR 1=1` → **odd radius**. The selected radius **1** passes.

## 8. Read and decrypt

| Order | Cipher cell | Ciphertext index C | Consumed key index K | (C−K) mod 29 | Plaintext |
| ---: | :---: | --- | --- | --- | :---: |
| 1 | (5,17) | Y = 26 | T = 16 | `26−16=10` | **I** |
| 2 | (6,17) | X = 14 | M = 19 | `14−19=-5≡24` | **A** |
| 3 | (7,17) | X = 14 | EA = 28 | `14−28=-14≡15` | **S** |
| 4 | (8,17) | NG = 21 | T = 16 | `21−16=5` | **K (C/K rune)** |

**Result: `I · A · S · K` → I ASK. Phase `p=0`; accumulated `S=32`.**

The final rune is the standard C/K rune, read as K in ASK. The space between I and ASK is an internal word boundary in one continuous ciphertext block. The key does not restart at that space. No English word is split between independently decrypted blocks.

| Counting basis | Rune-index sum | GP sum |
| --- | ---: | ---: |
| Ciphertext actually read | 75 | 276 |
| Key stream actually consumed | 79 | 298 |
| Plaintext produced | 54 | 194 |
| Full original source — three runes | 63 | 239 |
| Full derived key — three runes | 63 | 239 |

## 9. Reflection of the opening source

The last source is the exact reflection of the opening ordered source across the main diagonal:

| Source order | Opening source, block 01 | Last source, block 38 |
|---|---|---|
| 1 | AE(13,11) | T(11,13) |
| 2 | J(13,12) | M(12,13) |
| 3 | EA(13,13) | EA(13,13) |

The coordinate map is **`(r,c) → (c,r)`**. It preserves the order of the three source positions, exchanges the centers `(13,12)` and `(12,13)`, and fixes the shared EA cell `(13,13)`. The geometry is reflected; the rune values are not asserted to be identical.

| Key counted once as a triple | Index sum | GP |
| --- | ---: | ---: |
| Opening original AE–J–EA = (25,11,28) | 64 | 247 |
| Opening derived/aligned AE–I–EA = (25,10,28) | 63 | 241 |
| Last original/derived/aligned T–M–EA = (16,19,28) | 63 | 239 |

The opening and last **derived** triples both have index sum **63**. Their GP totals **239 and 241** are twin primes. These arithmetic properties concern the same reflected pair and should not be counted as independent experiments.

The opening center `(13,12)`, last center `(12,13)`, and last ciphertext cell `(8,17)` all lie on the anti-diagonal **`r+c=25`**.

## 10. Branch totals and accumulated totals

The continuation has **five English words in four decryption blocks**, and **ten runes**:

**`GO | DO | AS | I ASK`**

Here `|` denotes an actual block boundary. In particular, I is not a one-rune decryption block.

| Block | Runes | ΣP | ΣC | ΣK consumed | GP(P) | GP(C) | GP(K consumed) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 35 — GO | 2 | 9 | 3 | 52 | 24 | 9 | 206 |
| 36 — DO | 2 | 26 | 51 | 25 | 96 | 198 | 86 |
| 37 — AS | 2 | 39 | 35 | 25 | 150 | 132 | 84 |
| 38 — I ASK | 4 | 54 | 75 | 79 | 194 | 276 | 298 |
| **Total** | **10** | **128** | **164** | **181** | **464** | **615** | **674** |

All key-stream totals count only components actually subtracted, including repeated components. For I ASK, **298** enters the consumed GP total; **239** is the GP of its three-rune key counted once. Those quantities are never substituted for one another. Reused ciphertext cells elsewhere in the route are counted once per reading use.

| Accumulated quantity | Through YOU (34) | Through I ASK (38) |
| --- | --- | --- |
| English words | 40 | 45 |
| Runes | 105 | 115 |
| Phase state S | 28 | 32 |
| Plaintext index sum | 1295 | 1423 |
| Ciphertext index sum | 1437 | 1601 |
| Consumed-key index sum | 1476 | 1657 |
| Plaintext GP | 4709 | 5173 |
| Ciphertext GP | 5177 | 5792 |
| Consumed-key GP | 5327 | 6001 |
| Negative modular differences requiring +29 | 46 | 51 |

## 11. Arithmetic correspondences

The following are exact, **retrospectively identified** correspondences for the selected placement. They are not additional rules in Reports 00–15. All survive the two AS operations because they use invariant consumed streams, fixed original sources, or the unchanged last key. Several reuse the same totals and are not statistically independent.

### 11.1. The new beginning and the original beginning

The ten new ciphertext indices sum to **164**, the position of the first new ciphertext cell:

**`ΣC_new=164=n₀(7,2)=n₀(B_GO)`**.

The consumed key stream has **GP 674 = 2×337**. Its totient equals the position of the original opening key center:

**`φ(GP(K_new))=φ(674)=336=n₀(13,12)`**.

The two Y components consumed by GO have **GP 206**, equal to `n₀(8,17)`, the final I ASK ciphertext position.

### 11.2. A second positional return through the previous instruction

The new ciphertext has **GP 615 = 3×5×41**:

**`φ(615)=320=n₀(12,23)`**.

Cell `(12,23)` begins [TO (23)](23-to.md), the first block of **TO THE EAST OF THE MAP**. Thus φ of the new key GP matches the opening center, while φ of the new ciphertext GP matches the beginning of that earlier directional instruction.

### 11.3. The last consumed T in two numerical representations

The last consumed key rune is **T**, index **16**, GP **59**:

**`GP(K_new)−GP(C_new)=674−615=59=GP(T)`**.

**`φ(GP(K_new))−φ(GP(C_new))=336−320=16=index(T)`**.

Equivalently, the first nine new key uses have GP 615, matching all ten new ciphertext uses; the tenth key use adds T=59. The two comparisons share the same GP totals and are dependent observations.

### 11.4. Three accumulated prime sums

With `p_n` denoting the nth prime:

| Entire route through I ASK | Index sum | Prime index |
| --- | ---: | ---: |
| Plaintext | 1423 = p₂₂₄ | 224 |
| Ciphertext | 1601 = p₂₅₂ | 252 |
| Consumed key | 1657 = p₂₆₀ | 260 |

The prime-index gaps give **`252−224=28`**, the state after YOU, and **`260−252=8`**, the row of the final ciphertext endpoint `(8,17)`. Also **`φ(464)=224`**, so:

**`p_{φ(GP(P_new))}=p₂₂₄=1423=ΣP_entire_route`**.

### 11.5. Accumulated ciphertext GP and phase state

The entire ciphertext GP and final state satisfy:

**`5177+615=5792=32×181=S_final×ΣK_new`**.

There are 51 negative C−K differences on the whole route, each requiring one addition of 29. Their count also gives **`φ(51)=32=S_final`**. This state equality is an endpoint observation, not an invariant established at every earlier block.

### 11.6. Plaintext GP, matrix size, and new length

The complete candidate plaintext has GP **5173**:

**`4709+464=5173=7×739=7×(729+10)`**.

Here 729 is the matrix cell count, 10 is the number of new runes, and 7 is the phase interval used by the model.

### 11.7. Rotated positions and the earlier MAP boundary

The ten new ciphertext cells have `Σn₀=3560`. At 180° rotation, `n₂=730−n₀`, giving:

**`Σn₂=10×730−3560=3740`**.

The selected plaintext **from the opening through MAP inclusive** also has **GP 3740**. That scope ends after the first three runes of MAP LIFE, at the end of the previous map instruction; the following LIFE is excluded. It is a word boundary inside block 28, not a separate decryption block.

### 11.8. A composite correspondence to 3301

Count each of the three physical cells of each new **original source node** once:

| Source | Absolute positions n₀ in key order | Sum |
| --- | --- | ---: |
| GO | 70, 182, 294 | 546 |
| DO | 345, 335, 325 | 1005 |
| AS | 95, 151, 207 | 453 |
| I ASK | 283, 310, 337 | 930 |
| **All four sources** | **12 cells** | **2934** |

Use the last key **once as the triple T–M–EA**, with GP **239**, and the new plaintext index sum **128**:

**`Σn₀(original sources)+GP(last three-rune key)+ΣP_new`**

**`=2934+239+128=3301`**.

This expression intentionally combines three different measurements. The 239 term counts the last key once, whereas the consumed I ASK stream has GP 298. The choice of these measurements was found after the phrase and is not prescribed by the transition rules.

### 11.9. Block number and original-source measurements

The last word ASK has **`GP=97+53+13=163=p₃₈`**, matching the number **38** of its decryption block. The four new source-center rows sum to the same number: **`7+13+6+12=38`**. The word GP itself is intrinsic to ASK; the match to block number belongs to this placement.

The four full **original**, pre-transformation triples have index sums **58, 55, 42, 63**:

**`58+55+42+63=218`**, and **`φ(218)=108=4×27`**.

The 12 original source cells have column sum **180**, also **`φ(ΣK_new)=φ(181)=180`**. These original-source measurements are separate from the ten actually consumed key components.

### 11.10. Prefix comparisons with explicit boundaries

| Scope | Exact correspondence |
| --- | --- |
| Ciphertext GP of GO, DO, AS — first three new blocks | `9+198+132=339=3×113`; 113 is GP of the preceding plaintext YOU |
| Plaintext GP of GO DO AS — first three new words | `24+96+150=270=27×10`; 10 is the new phrase rune count |
| Consumed-key GP of GO and DO — first two new blocks | `206+86=292=n₁(6,11)`; (6,11) begins the preceding YOU ciphertext |

The earlier MAY…YOU coordinate equalities do **not** repeat for this continuation: the new row sum is **139**, versus consumed-key index sum **181**; the new column sum is **77**, versus ciphertext index sum **164**. The value **139=p₃₄** matches the block number of the preceding YOU, but it is a different observation from those earlier equalities.

## 12. Retrospective endpoint check without a dictionary

Fix only **GO (35), DO (36), and AS (37)** in the specified placements, using the direct AS operation. Enumerate every admissible next straight ciphertext block of **2–27 runes** under Reports 00–15, including the cyclic extension in 11. Do not supply the word I, the word ASK, a four-rune length, or a number of following English words.

| Successive conditions | Remaining endpoint assignments |
| --- | ---: |
| Reports 00–15 | 21342 |
| + total new ciphertext index sum = n₀(B_GO) = 164 | 178 |
| + φ(total new consumed-key GP) = opening center position 336 | 3 |
| + complete plaintext GP = 7×(729 + number of new runes) | 1 |

The unique survivor is the four-rune segment **`(5,17)→(8,17)`**, with the source **T–M–EA**, giving **`I·A·S·C/K` → I ASK**. The preceding three-survivor stage already fixes these ciphertext cells; its other two plaintext outputs are G·U·S·U and TH·D·R·Y, using other source keys.

A second enumeration, looping over sources first and applying the reference report checks, reproduced **21,342 → 178 → 3 → 1**. It considered 350 source/operation choices and 196 geometrically eligible segments before their joint GCD filter. These are counts conditional on the fixed prefix, not an exhaustive search of every possible English continuation.

A separate ordered-geometry check retains 119 endpoints whose source is the main-diagonal reflection of the opening ordered source; adding `ΣC_new=164` leaves one, again I ASK. The order of the three reflected elements is part of that condition.

In the saved bounded grammar search, **7,059 assignments** represent **2,977 candidate strings** before final language assessment; this catalogue includes grammatical and semantic rejects. A matched subset has **307 strings** with five words and ten new runes. Within the full saved catalogue, the two T comparisons in 11.3 hold together for one string, and the ordered-source reflection holds for one string: GO DO AS I ASK. The two AS operations account for two assignments of the same physical branch.

All endpoint criteria and numerical comparisons above were investigated after the candidate was found. Their selectivity is retrospective; it is not a probability of chance occurrence, an independent prediction of unseen plaintext, or proof of Cicada authorship.

## 13. Outgoing forecast

The continuation ends at the complete four-rune I ASK block, with **S=32**. A further transition is defined by Report 11, but no following plaintext is selected here. The current block predicts:

| Next-block property | Forecast from the complete current block |
| --- | --- |
| Signature / phase | `(0, +1, 0)`, `p=1` |
| State after acceptance | `S=33`, `a=0` |
| Ciphertext axis / leftmost boundary | Diagonal; leftmost = BEGINNING |
| Original source center | even row / even column |
| Endpoint row / leftmost row / leftmost column | odd / odd / even |
| Original source type | NON-MIRROR |
| Exact original source axis | horizontal (W–E) |
| Original source radius | even |
| Ray allowance / exact offset | 0 / 0 |

The numerical coincidences do not establish that I ASK is the intended endpoint of pages 0–2. Further source and ciphertext coordinates remain unresolved.

## 14. Complete candidate reading

> As I go, the weather turns cold.  
> I may cry now.  
> The idea of the end is death.  
> See you soon, then.  
> The key is to go to the east of the map.  
> Life may be the death of you.  
> **Go, do as I ask.**

This segmentation gives **45 English words**, **115 runes**, plaintext-index sum **1423**, and plaintext GP **5173**. Word boundaries, punctuation, and the K reading of the C/K rune in ASK are editorial choices consistent with the specified rune sequence.

**Status:** Exact modular subtraction and the incoming checks of Reports 00–15 pass for the specified placement, using Report 11’s cyclic phase extension. Source order is recorded explicitly. The candidate plaintext and the design intent of its numerical correspondences remain unconfirmed.

---

[← Previous: AS](37-as.md) · [Decryption method](../Start-reading-here/00-decryption-method.md) · [Cyclic phase schedule](../Start-reading-here/11-seven-thresholds-and-cyclic-phase-modes.md)
