# 31 — THE

*Selected continuation: **LIFE MAY BE THE DEATH OF YOU***

This is THE in **LIFE MAY BE THE DEATH OF YOU**. A direct, non-mirror `NG–A–EO` source decrypts two cells read rightward on row 11 as **TH·E**. It is a different placement and source from [THE (27)](27-the.md).

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
| Upper-right outer | (6,24) | NG | 21 |
| **Center** | (10,20) | A | 24 |
| Lower-left outer | (14,16) | EO | 12 |

This is a **diagonal** source with radius **4 diagonal grid steps**. Its outer runes are **different**, so the original node is **NON-MIRROR** under [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md). The center is `M=(10,20)`, with `n₀(M)=263`.

## 2. Derive and align the key

Use the original key **`NG–A–EO`** directly. No center transformation is applied for this source.

Calculate the signature on the **unrotated derived key**:

| Derived rune | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|:---:|
| NG | 21 | 12 | 0 |
| A | 24 | 8 | 0 |
| EO | 12 | 4 | 0 |

**Signature:** `(0,0,0)`. **Phase:** `p=(0) mod 3=0`.

Phase **0** leaves the key order unchanged: **`NG–A–EO`**. The aligned numerical key is **`(21, 24, 12)`**.

The consumed stream is **`NG–A`** across **2 ciphertext runes**.

The third aligned component, **`EO=12`**, is not consumed by this two-rune block.

## 3. Predict the signature from BE (30)

The preceding block has `B=(25,12)`, `E=(26,11)`, `L=(26,11)`, original center `M=(20,9)`, phase **0**, outer state **a=0**, and **S=24**. Under [Report 01](../Start-reading-here/01-next-key-signature.md), `21≤S<28` selects **Direct/+0**.

| Previous ciphertext cell | `n₀` | `μ(n₀)` |
|:---|---:|:---:|
| U/V(25,12) | 660 | 0 |
| R(26,11) | 686 | 0 |

`p_next=Σμ(n₀) mod 3=(0) mod 3=0`.

The outer-state selector is `n₁(L)=272`, with `μ(272)=0`. Therefore `a_next=(0+(0)) mod 2=0`.

**Predicted signature: `(0,0,0)`; predicted phase: `0`.** These match the selected key. The accumulated total becomes **`S=24+0=24`**.

## 4. Predict the ciphertext axis and reading direction

Apply [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md) to the **previous** block:

`A=n₂(B)+n₀(M)=70+522=592`, with `μ(A)=0`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(272,44)=4`, with `μ(G_axis)=0`.

`q_axis=μ(A)+μ(G_axis)=0` → **HORIZONTAL**.

For the boundary rule in [Report 02](../Start-reading-here/02-leftmost-cell-and-rotations.md), use the **original** center index `h=15`:

`τ_next=[μ(n₃(E))+φ(h)] mod 2=[+1+8] mod 2=1`.

The next leftmost cell must be the **BEGINNING**. The selected ciphertext reads **rightward**, from `D(11,11)` to `P(11,12)`, with `L=(11,11)`.

The local leftmost check gives `n₁(L)=287`, `μ(n₁(L))=+1`. This is allowed in the current **Direct** class.

## 5. Check center, boundary, ray, mirror, and length constraints

| Rule | Prediction from the preceding block | Selected placement |
|:---|:---|:---|
| [Report 04](../Start-reading-here/04-predicting-next-key-center-parity.md) — center row/column | even row / even column | `M=(10,20)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — endpoint row | odd | `E=(11,12)` — **pass** |
| [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md) — leftmost row | odd | `L=(11,11)` — **pass** |
| [Report 09](../Start-reading-here/09-predicting-next-ciphertext-column-parity.md) — leftmost column | odd | Column 11 — **pass** |
| [Report 06](../Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) — incoming ray | `Δ=(−15,+0)`, `d₈=0`, allowance `0` | `0≤0` — **pass** |
| [Report 07](../Start-reading-here/07-predicting-next-key-mirror-status.md) — original node type | `d∞=8`, `d∞ mod 3=2` → NON-MIRROR | Different outer runes — **pass** |
| [Report 08](../Start-reading-here/08-minimum-ciphertext-block-length.md) — minimum block length | At least 2 runes | 2 runes — **pass** |

The center parity totals are `r(M′)≡58≡0 (mod 2)` and `c(M′)≡72≡0 (mod 2)`. The endpoint/leftmost row totals are `1→1` and `1→1`.

For Report 09, the previous ciphertext gives `Σμ(n₁(C))=0`, mirror bit `0`, and center term `0`. Thus `c(L′)≡25+(0)+0+(0)≡25≡1 (mod 2)`.

The ray is measured from the previous `L=(26,11)`. Its allowance is evaluated at the previous `E=(26,11)`: `μ(n₀(E))=0; μ(n₃(E))=+1`. The mirror distance uses the previous lower/right outer cell `Z=(26,3)`.

## 6. Verify the four squarefree-GCD conditions

Use the **original center** `M=(10,20)` and the current block's `B`, `L`, and `E`, as defined in [Report 10](../Start-reading-here/10-squarefree-gcd-compatibility.md).

| Condition | Compared indices | GCD | `μ(GCD)` |
|:---|:---|---:|:---:|
| G1: `n₀(M), n₀(B)` | 263, 281 | 1 | +1 |
| G2: `n₀(M), n₀(L)` | 263, 281 | 1 | +1 |
| G3: `n₁(M), n₃(E)` | 531, 416 | 1 | +1 |
| G4: `n₀(M), n₂(E)` | 263, 448 | 1 | +1 |

**All four GCDs are squarefree.** A GCD greater than 1 is allowed; it must have no repeated prime factor.

## 7. Read and decrypt

| Order | Cipher cell | Ciphertext index C | Repeated key index K | `(C−K) mod 29` | Plaintext |
|---:|:---:|:---|:---|:---|:---:|
| 1 | (11,11) | D = 23 | NG = 21 | `23−21=2` | **TH** |
| 2 | (11,12) | P = 13 | A = 24 | `13−24=−11≡18` | **E** |

**Result: `TH · E` → THE. Phase `p=0`; accumulated `S=24`.**

| Counting basis | Rune-index sum | GP sum |
|:---|---:|---:|
| Ciphertext actually read | 36 | 132 |
| Key components actually consumed | 45 | 176 |
| Plaintext produced | 20 | 72 |

## 8. Keep this THE separate from earlier occurrences

This block uses **NG–A–EO directly**, with `M=(10,20)`. The preceding [THE (27)](27-the.md), before MAPLIFE, instead uses the transformed `J–G–U → J–TH–U` source at `(24,1)`. The plaintext is the same, but the nodes, cells, and key indices differ.

The lower outer source cell `EO(14,16)` is the sixth ciphertext cell of MAPLIFE, where subtraction with `EO=12` produces F. Only NG and A are consumed in the present two-rune THE.

## Next block

Applying Reports 01–09 to **this complete 2-rune block** predicts:

| Property | Prediction |
|:---|:---|
| Signature / phase | `(+1,−1,+1)`, `p=1` |
| Accumulated state after the transition | `S=25`, `a=1` |
| Axis / leftmost boundary | Diagonal; leftmost = END |
| Original key center | even row / odd column |
| Endpoint row / leftmost row / leftmost column | even / even / even |
| Original node type | NON-MIRROR |
| Ray allowance | 0 |

The selected next block is **[DEATH (32)](32-death.md)**, read `(10,10) → (12,8)` with original center `(14,7)`. Its walkthrough shows the incoming calculation explicitly.

**Status:** The specified source, exact modular subtraction, and stated incoming checks are verified for this selected placement. Numerical correspondences describe the selected route; their design intent is not established.

---

[← Previous: BE](30-be.md) · [Next: DEATH →](32-death.md) · [Decryption method](../Start-reading-here/00-decryption-method.md)
