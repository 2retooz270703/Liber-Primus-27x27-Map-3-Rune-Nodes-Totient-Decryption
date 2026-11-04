# 28 — MAPLIFE

*One continuous ciphertext block: **MAP LIFE***

The ciphertext read with the `EO–X–I` source continues beyond MAP along the same up-right diagonal. Seven consecutive cells, with the same repeating key stream, decrypt as **M·A·P·L·I·F·E**. The block is **MAPLIFE**, read as the two English words **MAP LIFE**; the space does not reset the key.

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
| Upper outer | (15,9) | EO | 12 |
| **Center** | (16,9) | X | 14 |
| Lower outer | (17,9) | I | 10 |

This is a **vertical** source with radius **1 row**. Its outer runes are **different**, so the original node is **NON-MIRROR** under [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md). The center is `M=(16,9)`, with `n₀(M)=414`.

## 2. Derive and align the key

Use the original key **`EO–X–I`** directly. No center transformation is applied for this source.

Calculate the signature on the **unrotated derived key**:

| Derived rune | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|:---:|
| EO | 12 | 4 | 0 |
| X | 14 | 6 | +1 |
| I | 10 | 4 | 0 |

**Signature:** `(0,+1,0)`. **Phase:** `p=(1) mod 3=1`.

Rotate the key **left by 1 position**: `EO–X–I → X–I–EO`. The aligned numerical key is **`(14, 10, 12)`**.

The consumed stream is **`X–I–EO–X–I–EO–X`** across **7 ciphertext runes**.

## 3. Predict the signature from THE (27)

The preceding block has `B=(20,12)`, `E=(20,13)`, `L=(20,12)`, original center `M=(24,1)`, phase **0**, outer state **a=1**, and **S=23**. Under [Report 01](../Start-reading-here/01-next-key-signature.md), `21≤S<28` selects **Direct/+0**.

| Previous ciphertext cell | `n₀` | `μ(n₀)` |
|:---|---:|:---:|
| P(20,12) | 525 | 0 |
| L(20,13) | 526 | +1 |

`p_next=Σμ(n₀) mod 3=(1) mod 3=1`.

The outer-state selector is `n₁(L)=305`, with `μ(305)=+1`. Therefore `a_next=(1+(+1)) mod 2=0`.

**Predicted signature: `(0,+1,0)`; predicted phase: `1`.** These match the selected key. The accumulated total becomes **`S=23+1=24`**.

## 4. Predict the ciphertext axis and reading direction

Apply [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md) to the **previous** block:

`A=n₂(B)+n₀(M)=205+622=827`, with `μ(A)=−1`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(332,204)=4`, with `μ(G_axis)=0`.

`q_axis=μ(A)+μ(G_axis)=−1` → **DIAGONAL**.

For the boundary rule in [Report 02](../Start-reading-here/02-leftmost-cell-and-rotations.md), use the **original** center index `h=6`:

`τ_next=[μ(n₃(E))+φ(h)] mod 2=[+1+2] mod 2=1`.

The next leftmost cell must be the **BEGINNING**. The selected ciphertext reads **up-right**, from `R(19,11)` to `O(13,17)`, with `L=(19,11)`.

The local leftmost check gives `n₁(L)=279`, `μ(n₁(L))=0`. This is allowed in the current **Direct** class.

## 5. Check center, boundary, ray, mirror, and length constraints

| Rule | Prediction from the preceding block | Selected placement |
|:---|:---|:---|
| [Report 04](../Start-reading-here/04-predicting-next-key-center-parity.md) — center row/column | even row / odd column | `M=(16,9)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — endpoint row | odd | `E=(13,17)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — leftmost row | odd | `L=(19,11)` — **pass** |
| [Report 09](../Start-reading-here/09-predicting-next-ciphertext-column-parity.md) — leftmost column | odd | Column 11 — **pass** |
| [Report 06](../Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) — incoming ray | `Δ=(−1,-1)`, `d₈=0`, allowance `0` | `0≤0` — **pass** |
| [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md) — original node type | `d∞=11`, `d∞ mod 3=2` → NON-MIRROR | Different outer runes — **pass** |
| [Report 08](../Start-reading-here/08-minimum-ciphertext-block-length.md) — minimum block length | At least 2 runes | 7 runes — **pass** |

The center parity totals are `r(M′)≡58≡0 (mod 2)` and `c(M′)≡65≡1 (mod 2)`. The endpoint/leftmost row totals are `1→1` and `1→1`.

For Report 09, the previous ciphertext gives `Σμ(n₁(C))=1`, mirror bit `0`, and center term `0`. Thus `c(L′)≡20+(1)+0+(0)≡21≡1 (mod 2)`.

The ray is measured from the previous `L=(20,12)`. Its allowance is evaluated at the previous `E=(20,13)`: `μ(n₀(E))=+1; μ(n₃(E))=+1`. The mirror distance uses the previous lower/right outer cell `Z=(25,1)`.

## 6. Verify the four squarefree-GCD conditions

Use the **original center** `M=(16,9)` and the current block's `B`, `L`, and `E`, as defined in [Report 10](../Start-reading-here/10-squarefree-gcd-compatibility.md).

| Condition | Compared indices | GCD | `μ(GCD)` |
|:---|:---|---:|:---:|
| G1: `n₀(M), n₀(B)` | 414, 497 | 1 | +1 |
| G2: `n₀(M), n₀(L)` | 414, 497 | 1 | +1 |
| G3: `n₁(M), n₃(E)` | 228, 283 | 1 | +1 |
| G4: `n₀(M), n₂(E)` | 414, 389 | 1 | +1 |

**All four GCDs are squarefree.** A GCD greater than 1 is allowed; it must have no repeated prime factor.

## 7. Read and decrypt

| Order | Cipher cell | Ciphertext index C | Repeated key index K | `(C−K) mod 29` | Plaintext |
|---:|:---:|:---|:---|:---|:---:|
| 1 | (19,11) | R = 4 | X = 14 | `4−14=−10≡19` | **M** |
| 2 | (18,12) | C/K = 5 | I = 10 | `5−10=−5≡24` | **A** |
| 3 | (17,13) | AE = 25 | EO = 12 | `25−12=13` | **P** |
| 4 | (16,14) | C/K = 5 | X = 14 | `5−14=−9≡20` | **L** |
| 5 | (15,15) | L = 20 | I = 10 | `20−10=10` | **I** |
| 6 | (14,16) | EO = 12 | EO = 12 | `12−12=0` | **F** |
| 7 | (13,17) | O = 3 | X = 14 | `3−14=−11≡18` | **E** |

**Result: `M · A · P · L · I · F · E` → MAP LIFE. Phase `p=1`; accumulated `S=24`.**

| Counting basis | Rune-index sum | GP sum |
|:---|---:|---:|
| Ciphertext actually read | 74 | 259 |
| Key components actually consumed | 86 | 285 |
| Plaintext produced | 104 | 384 |

## 8. MAP continues into LIFE without a key reset

| Portion of the same block | Ciphertext cells | Plaintext | Runes | Index sum | GP |
|:---|:---|:---|---:|---:|---:|
| MAP | (19,11) → (17,13) | M·A·P | 3 | 56 | 211 |
| LIFE | (16,14) → (13,17) | L·I·F·E | 4 | 48 | 173 |
| **MAPLIFE** | **(19,11) → (13,17)** | **M·A·P·L·I·F·E** | **7** | **104** | **384** |

The key stream is `X–I–EO–X–I–EO–X`. LIFE starts at the fourth ciphertext cell, where the repeating stream returns to X; the space after MAP does not create another independently decrypted block or another phase update.

The MAP word ends at **(17,13)**, while the complete MAPLIFE block ends at **(13,17)**. These coordinates are transposes. Both lie on `row+column=30`, and reflection across `row=column` maps one to the other.

The previously recorded reflection involving the opening `J(13,12)`, source center `X(16,9)`, and MAP word-end `(17,13)` is retained: the two squared distances to that internal point are both 17, and the reflection axis is `row−column=4`. That observation belongs to the **MAP word-end**, not to the new endpoint `(13,17)`.

For the next transition, use the complete seven-cell ciphertext and **E=(13,17)**. Its axis calculation is `A=233+414=647`, `μ(A)=−1`, and `gcd(447,389)=1`, giving `q_axis=0` — horizontal. Truncating the block at MAP would instead give `gcd(335,285)=5` and `q_axis=−2` — diagonal. The extension into LIFE therefore changes the next-axis prediction.

## 9. Cumulative plaintext totals

| Reading boundary | English words | Runes | Rune-index sum | GP |
|:---|---:|---:|---:|---:|
| Through the MAP word, inside block 28 | 33 | 86 | 1037 | 3740 |
| Through the complete MAPLIFE block | 34 | 90 | 1085 | 3913 |

Both rows use the already selected preceding route. The earlier MAP-only totals remain valid at that internal word boundary; they are not the totals after the extended block.

The word boundary separates two sentences in the proposed reading:

> The key is to go to the east of the map.  
> Life may be the death of you.

Punctuation and word spacing are editorial. The underlying seven-rune decryption remains continuous.

## Next block

Applying Reports 01–09 to **this complete 7-rune block** predicts:

| Property | Prediction |
|:---|:---|
| Signature / phase | `(0,0,0)`, `p=0` |
| Accumulated state after the transition | `S=24`, `a=0` |
| Axis / leftmost boundary | Horizontal; leftmost = BEGINNING |
| Original key center | even row / odd column |
| Endpoint row / leftmost row / leftmost column | even / even / odd |
| Original node type | NON-MIRROR |
| Ray allowance | 0 |

The selected next block is **[MAY (29)](29-may.md)**, read `(18,11) → (18,13)` with original center `(14,13)`. Its walkthrough shows the incoming calculation explicitly.

**Status:** The specified source, exact modular subtraction, and stated incoming checks are verified for this selected placement. Numerical correspondences describe the selected route; their design intent is not established.

---

[← Previous: THE](27-the.md) · [Next: MAY →](29-may.md) · [Decryption method](../Start-reading-here/00-decryption-method.md)
