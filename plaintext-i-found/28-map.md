# 28 — MAP

*Candidate completion: **THE KEY IS TO GO TO THE EAST OF THE MAP***

This is **candidate block 28**, completing the six new words after `GO`: **TO → THE → EAST → OF → THE → MAP**. The selected three-cell ciphertext reads **diagonally up-right**, from `R(19,11)` to `AE(17,13)`, and an original **non-mirror `EO–X–I` key node** is used **without** transforming its center. Phase 1 aligns the key to `X–I–EO`, which decrypts the ciphertext as **`M · A · P` → MAP**.

The original independently recorded route ends at `THEN` (17). This extended reading remains a **candidate**. Arithmetic correctness for the chosen nodes and ciphertext cells must be distinguished from a proof that they are the only valid placements or the intended Cicada 3301 message. All matrix coordinates are 1-based, rune indices 0–28, and `φ`, `μ`, and GP retain their meanings from Reports 00–08. Rotations are `n₀(r,c)=27(r−1)+c`, `n₁(r,c)=27(c−1)+28−r`, `n₂=730−n₀`, and `n₃(r,c)=27(27−c)+r`.

## 1. Locate the original source node

| Role | Coordinate | Matrix rune | Index |
|:---|:---:|:---:|---:|
| Upper outer | (15,9) | EO | 12 |
| **Center** | **(16,9)** | **X** | **14** |
| Lower outer | (17,9) | I | 10 |

This is a **vertical, equally spaced node of radius one row**. The distinct outer runes `EO≠I` make it **NON-MIRROR** under Report 07. Its original center has absolute position `n₀(16,9)=414`.

## 2. Use the direct key and compute the rotation

For this selected non-mirror source **no center transformation is applied**. Use the original key `EO–X–I = (12,14,10)` directly.

| Key rune | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|:---:|
| EO | 12 | 4 | 0 |
| X | 14 | 6 | +1 |
| I | 10 | 4 | 0 |

**Möbius signature:** `(0,+1,0)`; **phase:** `p=(0+1+0) mod 3=1`.

Rotate once to the left: `EO–X–I → X–I–EO`; aligned indices **`(14,10,12)`**. All three key runes are used.

## 3. Predict the next signature from THE (Report 01)

The immediately preceding block is **the second THE (27)**: ciphertext `P(20,12) → L(20,13)`, original center `G(24,1)`, leftmost cell `P(20,12)`, current phase **0**, outer state **1**, and **`S=23`**. The phase mode remains **Direct/+0**.

- Original ciphertext positions `n₀(20,12)=525`, `n₀(20,13)=526`.
- `μ(525)=0`, `μ(526)=+1`, giving `p_next=(0+1) mod 3=1`.
- The 90° selector is `n₁(20,12)=305`; `μ(305)=+1` toggles the outer state from 1 to 0.
- Phase 1 with outer state 0 predicts signature **`(0,+1,0)`**, matching untransformed `EO–X–I`.

The accumulated total becomes **`S=23+1=24`**.

## 4. Axis, direction, and leftmost cell (Reports 02–03)

For the current second THE, use `B=(20,12)`, `E=(20,13)`, and original node center `M=(24,1)`:

`A=n₂(B)+n₀(M)=205+622=827`; `μ(827)=−1`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(332,204)=4`; `μ(4)=0`.

Therefore **`q_axis=−1+0=−1` → DIAGONAL**.

The current original center rune is `G=6` with `φ(6)=2`. Since `n₃(E)=398` and `μ(398)=+1`, the predicted boundary is:

`τ_next=[1+2] mod 2=1` → **leftmost = BEGINNING**.

| Order | Cell | Cipher rune | Role |
|:---:|:---:|:---:|:---|
| 1 | (19,11) | R | **Beginning and leftmost** |
| 2 | (18,12) | C/K | Interior |
| 3 | (17,13) | AE | Endpoint |

The selected direction is **up-right**. The leftmost cell `(19,11)` has rotated position `n₁(19,11)=279` and `μ(279)=0`, which is allowed by the proposed Direct mode.

## 5. Center, row, ray, mirror, and length checks (Reports 04–08)

| Report | Prediction from THE (27) | Selected MAP |
|:---|:---|:---|
| **04 — Center parity** | Even row, odd column | X(16,9): **even/odd** |
| **05 — Endpoint row** | Odd | AE(17,13), **row 17** |
| **05 — Leftmost row** | Odd | R(19,11), **row 19** |
| **06 — Incoming ray** | From `L_THE=(20,12)` to `B_MAP=(19,11)`: `Δ=(−1,−1)`, `d₈=0`, permitted `q=0` | **Pass** |
| **07 — Next mirror status** | Later THE arm `(25,1)` to leftmost `(20,12)`: `d∞=11`, `11 mod 3=2` → **NON-MIRROR** | `EO≠I` — **pass** |
| **08 — Minimum length** | At least two runes | **Three** |

The parity bits for Report 04 are `(0,1)` and for Report 05 `(1,1)`. Report 06 gives `q=0` because the previous endpoint `(20,13)` has `μ(n₀)=μ(526)=+1` and `μ(n₃)=μ(398)=+1`, so the one-cell exception is not available.

## 6. Read and decrypt

| Cipher cell | Ciphertext | Aligned key | `(C−K) mod 29` | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (19,11) | R = 4 | X = 14 | `4−14≡19` | **M** |
| (18,12) | C/K = 5 | I = 10 | `5−10≡24` | **A** |
| (17,13) | AE = 25 | EO = 12 | `25−12=13` | **P** |

## Result

**`M · A · P` → MAP**. **Phase `p=1`; cumulative `S=24`.** The first two differences wrap modulo 29. The selected three-rune source and full three-rune ciphertext fit the project's proposed minimum-length condition.

## 7. Exact spatial relation to the original J center

The opening of this research route identifies **`J(13,12)`** as the original center. Let:

- `J=(13,12)` — original opening cell;
- `M=(16,9)` — center of the proposed MAP key;
- `E=(17,13)` — endpoint of the MAP ciphertext.

Their displacements from the two centers to the endpoint are:

`J → E = (+4,+1)` and `M → E = (+1,+4)`.

Both have **squared Euclidean length 17**:

`|J−E|²=4²+1²=17`, and `|M−E|²=1²+4²=17`.

Furthermore, reflection across the diagonal line **`row − column = 4`** sends `J(13,12)` to `M(16,9)` and leaves endpoint `E(17,13)` on that line. This is an exact **isosceles/reflection symmetry** involving the opening cell and the selected MAP realization. It does not select MAP uniquely, but it is geometrically notable.

## 8. GP and index totals at the endpoint

| New word | Plaintext runes | Rune-index sum | GP |
|:---|:---|---:|---:|
| TO | T · O | 19 | 66 |
| THE | TH · E | 20 | 72 |
| EAST | EA · S · T | 59 | 221 |
| OF | O · F | 3 | 9 |
| THE | TH · E | 20 | 72 |
| MAP | M · A · P | 56 | 211 |
| **New six-word total** | **14 runes** | **177** | **651** |

The first **seven** runes `TO THE EAST` yield **GP 359**, the **72nd prime**, while the previously proposed text through `GO` contains **72 runes**. The eastern/western seven-rune split uses ciphertext columns **18–24** and **11–13** respectively.

The new GP total is **651**. That equals the previously documented 90°-rotated index of the **THEN** leftmost cell `L(25,25)`: `n₁(25,25)=651`. This is a post-selection numerical correspondence, not a derivation of the six words.

For all six new blocks, the sum of GP values of **consumed aligned key runes** is **576**, while `GP(GO)=24`; thus **`576=24²`**. Separately, the MAP word has `GP(MAP)=71+97+43=211`, the **47th prime**, and its original center rune is `X` with `GP(X)=47`.

Adding the earlier proposed five words `THE KEY IS TO GO` (index sum **122**, GP **429**) gives:

| Complete proposed continuation after THEN | Words | Runes | Rune-index sum | GP |
|:---|---:|---:|---:|---:|
| THE KEY IS TO GO TO THE EAST OF THE MAP | **11** | **25** | **299** | **1080** |

Here **`1080=27×40`**, and the plaintext-index sum **299** matches the **ciphertext-index sum** of the initial recorded seven-word passage `AS I GO, THE WEATHER TURNS COLD`. Crucially, that earlier passage's **plaintext** index sum was **233**, not 299.

Across the complete selected reading, from `AS I GO` through `MAP`, the totals are **33 English words**, **86 runes**, index sum **1037**, and GP **3740**. The earlier special endpoint equalities at GO — `φ(860)=336` and the prime ordinal of GP 3089 — do **not** automatically extend to MAP.

## 9. Status and next research test

**Verified conditionally:** the original `EO–X–I` node, direct (untransformed) key, phase-1 rotation, exact three-rune output, and all selected-route predictions under the documented Reports **01–08**. The reflected geometric relation among `J`, the MAP center, and the MAP endpoint is also exactly reproducible.

**Not established:** unique ciphertext coordinates, a unique admissible key, authenticity of the proposed English sentence, or predictive validity of the Direct/+0 mode beyond the historical sample. The supplied repository documents Reports 00–08 only. An additional experimental constraint sometimes called **Report 09** is not claimed to pass; the selected extension requires separate scrutiny under any such rule.

The key open problem remains a **predictive generator for the exact next ciphertext location**, rather than a further numerical equality discovered after choosing a readable branch. A proper comparison should test this whole six-word path against *other* Report 01–08-admissible continuations with the same arithmetic, geometry, and key flexibility.
