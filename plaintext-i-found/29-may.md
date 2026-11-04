# 29 — MAY

*Selected continuation: **LIFE MAY BE THE DEATH OF YOU***

This block begins the sentence **LIFE MAY BE THE DEATH OF YOU** after LIFE has already been read inside [MAPLIFE (28)](28-map.md). The vertical non-mirror source `T–OE–AE` becomes `T–I–AE`. Three cells read rightward on row 18 decrypt as **M·A·Y**.

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
| Upper outer | (11,13) | T | 16 |
| **Center** | (14,13) | OE | 22 |
| Lower outer | (17,13) | AE | 25 |

This is a **vertical** source with radius **3 rows**. Its outer runes are **different**, so the original node is **NON-MIRROR** under [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md). The center is `M=(14,13)`, with `n₀(M)=364`.

## 2. Derive and align the key

Apply the totient **only to the original center**: `OE=22 → φ(22)=10=I`. Keep both outer indices unchanged.

**`T–OE–AE → T–I–AE`**.

Calculate the signature on the **unrotated derived key**:

| Derived rune | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|:---:|
| T | 16 | 8 | 0 |
| I | 10 | 4 | 0 |
| AE | 25 | 20 | 0 |

**Signature:** `(0,0,0)`. **Phase:** `p=(0) mod 3=0`.

Phase **0** leaves the key order unchanged: **`T–I–AE`**. The aligned numerical key is **`(16, 10, 25)`**.

The consumed stream is **`T–I–AE`** across **3 ciphertext runes**.

## 3. Predict the signature from MAPLIFE (28)

The preceding block has `B=(19,11)`, `E=(13,17)`, `L=(19,11)`, original center `M=(16,9)`, phase **1**, outer state **a=0**, and **S=24**. Under [Report 01](../Start-reading-here/01-next-key-signature.md), `21≤S<28` selects **Direct/+0**.

| Previous ciphertext cell | `n₀` | `μ(n₀)` |
|:---|---:|:---:|
| R(19,11) | 497 | +1 |
| C/K(18,12) | 471 | +1 |
| AE(17,13) | 445 | +1 |
| C/K(16,14) | 419 | −1 |
| L(15,15) | 393 | +1 |
| EO(14,16) | 367 | −1 |
| O(13,17) | 341 | +1 |

`p_next=Σμ(n₀) mod 3=(3) mod 3=0`.

The outer-state selector is `n₁(L)=279`, with `μ(279)=0`. Therefore `a_next=(0+(0)) mod 2=0`.

**Predicted signature: `(0,0,0)`; predicted phase: `0`.** These match the selected key. The accumulated total becomes **`S=24+0=24`**.

## 4. Predict the ciphertext axis and reading direction

Apply [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md) to the **previous** block:

`A=n₂(B)+n₀(M)=233+414=647`, with `μ(A)=−1`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(447,389)=1`, with `μ(G_axis)=+1`.

`q_axis=μ(A)+μ(G_axis)=0` → **HORIZONTAL**.

For the boundary rule in [Report 02](../Start-reading-here/02-leftmost-cell-and-rotations.md), use the **original** center index `h=14`:

`τ_next=[μ(n₃(E))+φ(h)] mod 2=[−1+6] mod 2=1`.

The next leftmost cell must be the **BEGINNING**. The selected ciphertext reads **rightward**, from `G(18,11)` to `OE(18,13)`, with `L=(18,11)`.

The local leftmost check gives `n₁(L)=280`, `μ(n₁(L))=0`. This is allowed in the current **Direct** class.

## 5. Check center, boundary, ray, mirror, and length constraints

| Rule | Prediction from the preceding block | Selected placement |
|:---|:---|:---|
| [Report 04](../Start-reading-here/04-predicting-next-key-center-parity.md) — center row/column | even row / odd column | `M=(14,13)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — endpoint row | even | `E=(18,13)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — leftmost row | even | `L=(18,11)` — **pass** |
| [Report 09](../Start-reading-here/09-predicting-next-ciphertext-column-parity.md) — leftmost column | odd | Column 11 — **pass** |
| [Report 06](../Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) — incoming ray | `Δ=(−1,+0)`, `d₈=0`, allowance `0` | `0≤0` — **pass** |
| [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md) — original node type | `d∞=2`, `d∞ mod 3=2` → NON-MIRROR | Different outer runes — **pass** |
| [Report 08](../Start-reading-here/08-minimum-ciphertext-block-length.md) — minimum block length | At least 2 runes | 3 runes — **pass** |

The center parity totals are `r(M′)≡40≡0 (mod 2)` and `c(M′)≡49≡1 (mod 2)`. The endpoint/leftmost row totals are `2→0` and `2→0`.

For Report 09, the previous ciphertext gives `Σμ(n₁(C))=1`, mirror bit `0`, and center term `+1`. Thus `c(L′)≡19+(1)+0+(+1)≡21≡1 (mod 2)`.

The ray is measured from the previous `L=(19,11)`. Its allowance is evaluated at the previous `E=(13,17)`: `μ(n₀(E))=+1; μ(n₃(E))=−1`. The mirror distance uses the previous lower/right outer cell `Z=(17,9)`.

## 6. Verify the four squarefree-GCD conditions

Use the **original center** `M=(14,13)` and the current block's `B`, `L`, and `E`, as defined in [Report 10](../Start-reading-here/10-squarefree-gcd-compatibility.md).

| Condition | Compared indices | GCD | `μ(GCD)` |
|:---|:---|---:|:---:|
| G1: `n₀(M), n₀(B)` | 364, 470 | 2 | −1 |
| G2: `n₀(M), n₀(L)` | 364, 470 | 2 | −1 |
| G3: `n₁(M), n₃(E)` | 338, 396 | 2 | −1 |
| G4: `n₀(M), n₂(E)` | 364, 258 | 2 | −1 |

**All four GCDs are squarefree.** A GCD greater than 1 is allowed; it must have no repeated prime factor.

## 7. Read and decrypt

| Order | Cipher cell | Ciphertext index C | Repeated key index K | `(C−K) mod 29` | Plaintext |
|---:|:---:|:---|:---|:---|:---:|
| 1 | (18,11) | G = 6 | T = 16 | `6−16=−10≡19` | **M** |
| 2 | (18,12) | C/K = 5 | I = 10 | `5−10=−5≡24` | **A** |
| 3 | (18,13) | OE = 22 | AE = 25 | `22−25=−3≡26` | **Y** |

**Result: `M · A · Y` → MAY. Phase `p=0`; accumulated `S=24`.**

| Counting basis | Rune-index sum | GP sum |
|:---|---:|---:|
| Ciphertext actually read | 33 | 113 |
| Key components actually consumed | 51 | 191 |
| Plaintext produced | 69 | 271 |

## 8. Spatial links to MAPLIFE

- MAY begins at `(18,11)`, one row above the previous beginning `(19,11)` and on its exact vertical ray.
- Its middle ciphertext cell, `C/K(18,12)`, is also the second cell of MAPLIFE. Both uses subtract `I=10` and produce `A=24`.
- The lower outer cell of the MAY source, `AE(17,13)`, is the MAP word-end inside MAPLIFE.

The MAY ciphertext occupies row 18, columns 11–13. The final [YOU (34)](34-you.md) occupies row 6, the same columns and reading order. Reflection `(r,c)→(24−r,c)` exchanges these complete three-cell blocks; [OF (33)](33-of.md) lies on the fixed row 12.

The original MAY source has `GP(T–OE–AE)=59+83+101=243=3⁵`. This is a property of the shared MAY source, not a uniqueness test for the entire sentence.

## Next block

Applying Reports 01–09 to **this complete 3-rune block** predicts:

| Property | Prediction |
|:---|:---|
| Signature / phase | `(0,0,0)`, `p=0` |
| Accumulated state after the transition | `S=24`, `a=0` |
| Axis / leftmost boundary | Diagonal; leftmost = END |
| Original key center | even row / odd column |
| Endpoint row / leftmost row / leftmost column | even / even / odd |
| Original node type | NON-MIRROR |
| Ray allowance | 1 |

The selected next block is **[BE (30)](30-be.md)**, read `(25,12) → (26,11)` with original center `(20,9)`. Its walkthrough shows the incoming calculation explicitly.

**Status:** The specified source, exact modular subtraction, and stated incoming checks are verified for this selected placement. Numerical correspondences describe the selected route; their design intent is not established.

---

[← Previous: MAPLIFE](28-map.md) · [Next: BE →](30-be.md) · [Decryption method](../Start-reading-here/00-decryption-method.md)
