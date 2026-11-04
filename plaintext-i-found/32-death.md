# 32 — DEATH

*Selected continuation: **LIFE MAY BE THE DEATH OF YOU***

This DEATH follows THE in the new sentence. A direct, non-mirror `TH–G–OE` source is rotated once to `G–OE–TH`. Three cells read diagonally down-left decrypt as **D·EA·TH**. It is distinct from the earlier [DEATH (13)](13-death.md).

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
| Left outer | (14,1) | TH | 2 |
| **Center** | (14,7) | G | 6 |
| Right outer | (14,13) | OE | 22 |

This is a **horizontal** source with radius **6 columns**. Its outer runes are **different**, so the original node is **NON-MIRROR** under [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md). The center is `M=(14,7)`, with `n₀(M)=358`.

## 2. Derive and align the key

Use the original key **`TH–G–OE`** directly. No center transformation is applied for this source.

Calculate the signature on the **unrotated derived key**:

| Derived rune | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|:---:|
| TH | 2 | 1 | +1 |
| G | 6 | 2 | −1 |
| OE | 22 | 10 | +1 |

**Signature:** `(+1,−1,+1)`. **Phase:** `p=(1) mod 3=1`.

Rotate the key **left by 1 position**: `TH–G–OE → G–OE–TH`. The aligned numerical key is **`(6, 22, 2)`**.

The consumed stream is **`G–OE–TH`** across **3 ciphertext runes**.

## 3. Predict the signature from THE (31)

The preceding block has `B=(11,11)`, `E=(11,12)`, `L=(11,11)`, original center `M=(10,20)`, phase **0**, outer state **a=0**, and **S=24**. Under [Report 01](../Start-reading-here/01-next-key-signature.md), `21≤S<28` selects **Direct/+0**.

| Previous ciphertext cell | `n₀` | `μ(n₀)` |
|:---|---:|:---:|
| D(11,11) | 281 | −1 |
| P(11,12) | 282 | −1 |

`p_next=Σμ(n₀) mod 3=(−2) mod 3=1`.

The outer-state selector is `n₁(L)=287`, with `μ(287)=+1`. Therefore `a_next=(0+(+1)) mod 2=1`.

**Predicted signature: `(+1,−1,+1)`; predicted phase: `1`.** These match the selected key. The accumulated total becomes **`S=24+1=25`**.

## 4. Predict the ciphertext axis and reading direction

Apply [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md) to the **previous** block:

`A=n₂(B)+n₀(M)=449+263=712`, with `μ(A)=0`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(314,448)=2`, with `μ(G_axis)=−1`.

`q_axis=μ(A)+μ(G_axis)=−1` → **DIAGONAL**.

For the boundary rule in [Report 02](../Start-reading-here/02-leftmost-cell-and-rotations.md), use the **original** center index `h=24`:

`τ_next=[μ(n₃(E))+φ(h)] mod 2=[0+8] mod 2=0`.

The next leftmost cell must be the **END**. The selected ciphertext reads **down-left**, from `F(10,10)` to `R(12,8)`, with `L=(12,8)`.

The local leftmost check gives `n₁(L)=205`, `μ(n₁(L))=+1`. This is allowed in the current **Direct** class.

## 5. Check center, boundary, ray, mirror, and length constraints

| Rule | Prediction from the preceding block | Selected placement |
|:---|:---|:---|
| [Report 04](../Start-reading-here/04-predicting-next-key-center-parity.md) — center row/column | even row / odd column | `M=(14,7)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — endpoint row | even | `E=(12,8)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — leftmost row | even | `L=(12,8)` — **pass** |
| [Report 09](../Start-reading-here/09-predicting-next-ciphertext-column-parity.md) — leftmost column | even | Column 8 — **pass** |
| [Report 06](../Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) — incoming ray | `Δ=(−1,-1)`, `d₈=0`, allowance `0` | `0≤0` — **pass** |
| [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md) — original node type | `d∞=5`, `d∞ mod 3=2` → NON-MIRROR | Different outer runes — **pass** |
| [Report 08](../Start-reading-here/08-minimum-ciphertext-block-length.md) — minimum block length | At least 2 runes | 3 runes — **pass** |

The center parity totals are `r(M′)≡32≡0 (mod 2)` and `c(M′)≡33≡1 (mod 2)`. The endpoint/leftmost row totals are `0→0` and `2→0`.

For Report 09, the previous ciphertext gives `Σμ(n₁(C))=2`, mirror bit `0`, and center term `−1`. Thus `c(L′)≡11+(2)+0+(−1)≡12≡0 (mod 2)`.

The ray is measured from the previous `L=(11,11)`. Its allowance is evaluated at the previous `E=(11,12)`: `μ(n₀(E))=−1; μ(n₃(E))=0`. The mirror distance uses the previous lower/right outer cell `Z=(14,16)`.

## 6. Verify the four squarefree-GCD conditions

Use the **original center** `M=(14,7)` and the current block's `B`, `L`, and `E`, as defined in [Report 10](../Start-reading-here/10-squarefree-gcd-compatibility.md).

| Condition | Compared indices | GCD | `μ(GCD)` |
|:---|:---|---:|:---:|
| G1: `n₀(M), n₀(B)` | 358, 253 | 1 | +1 |
| G2: `n₀(M), n₀(L)` | 358, 305 | 1 | +1 |
| G3: `n₁(M), n₃(E)` | 176, 525 | 1 | +1 |
| G4: `n₀(M), n₂(E)` | 358, 425 | 1 | +1 |

**All four GCDs are squarefree.** A GCD greater than 1 is allowed; it must have no repeated prime factor.

## 7. Read and decrypt

| Order | Cipher cell | Ciphertext index C | Repeated key index K | `(C−K) mod 29` | Plaintext |
|---:|:---:|:---|:---|:---|:---:|
| 1 | (10,10) | F = 0 | G = 6 | `0−6=−6≡23` | **D** |
| 2 | (11,9) | NG = 21 | OE = 22 | `21−22=−1≡28` | **EA** |
| 3 | (12,8) | R = 4 | TH = 2 | `4−2=2` | **TH** |

**Result: `D · EA · TH` → DEATH. Phase `p=1`; accumulated `S=25`.**

| Counting basis | Rune-index sum | GP sum |
|:---|---:|---:|
| Ciphertext actually read | 25 | 92 |
| Key components actually consumed | 30 | 105 |
| Plaintext produced | 53 | 203 |

## 8. Source and ciphertext details

The first ciphertext rune is **F=0**. Subtracting the consumed `G=6` gives `0−6≡23=D`; this does not require applying φ or μ to zero. The source key itself contains no F=0 component.

This source uses `TH–G–OE` **without transforming its center**. Applying φ to that center would produce a different key, phase, and decryption; it is not the operation documented here.

The source center `G(14,7)` is also the first ciphertext cell of the earlier [COLD (04)](04-cold.md). Its right outer cell `OE(14,13)` is the original center of the [MAY (29)](29-may.md) source. The left outer `TH(14,1)` belongs to the opening ciphertext block.

## Next block

Applying Reports 01–09 to **this complete 3-rune block** predicts:

| Property | Prediction |
|:---|:---|
| Signature / phase | `(0,−1,0)`, `p=2` |
| Accumulated state after the transition | `S=27`, `a=0` |
| Axis / leftmost boundary | Horizontal; leftmost = END |
| Original key center | odd row / odd column |
| Endpoint row / leftmost row / leftmost column | even / even / odd |
| Original node type | NON-MIRROR |
| Ray allowance | 0 |

The selected next block is **[OF (33)](33-of.md)**, read `(12,18) → (12,17)` with original center `(9,17)`. Its walkthrough shows the incoming calculation explicitly.

**Status:** The specified source, exact modular subtraction, and stated incoming checks are verified for this selected placement. Numerical correspondences describe the selected route; their design intent is not established.

---

[← Previous: THE](31-the.md) · [Next: OF →](33-of.md) · [Decryption method](../Start-reading-here/00-decryption-method.md)
