# 27 — THE

*Candidate continuation: **THE KEY IS TO GO TO THE EAST OF THE MAP***

This is **candidate block 27**, the second `THE` in the new six-word continuation. It is different from candidate THE (24), which uses `L–X–S` and a direct non-mirror key. Here the proposed horizontal ciphertext `P–L` reads **rightward**, and a **non-mirror** original `J–G–U` node has **only its middle rune transformed**. The resulting key `J–TH–U` decrypts the two cells as **`TH · E` → THE**.

All coordinates are 1-based in the 27 × 27 matrix; key and ciphertext arithmetic uses indices modulo 29. GP values are prime weights, not those indices. The position functions are `n₀(r,c)=27(r−1)+c`, `n₁(r,c)=27(c−1)+28−r`, `n₂=730−n₀`, and `n₃(r,c)=27(27−c)+r`.

## 1. Original vertical key node

| Role | Coordinate | Rune | Index |
|:---|:---:|:---:|---:|
| Upper outer | (23,1) | J | 11 |
| **Center** | **(24,1)** | **G** | **6** |
| Lower outer | (25,1) | U/V | 1 |

The radius is **one row**, and all three cells are in column 1. Because **`J≠U/V`**, this is a **NON-MIRROR** source node (even though its cells are geometrically symmetric about the center). The original center's absolute position is `n₀(24,1)=622`.

## 2. Transform only the center, then derive the phase

For this selected non-mirror node the recorded operation is **center-only totient transformation**:

`J(11) – G(6) – U/V(1) → J(11) – TH(2) – U/V(1)` because **`φ(6)=2`**.

| Derived rune | Index | Totient | Möbius |
|:---:|---:|---:|:---:|
| J | 11 | `φ(11)=10` | `μ(10)=+1` |
| TH | 2 | `φ(2)=1` | `μ(1)=+1` |
| U/V | 1 | `φ(1)=1` | `μ(1)=+1` |

The signature is **`(+1,+1,+1)`** and the cyclic phase is `p=(1+1+1) mod 3=0`. No rotation follows: **`J–TH–U`**, aligned key indices **`(11,2,1)`**. This block uses only **`J–TH`**.

## 3. Report 01 prediction from OF

Current OF: ciphertext `J(6,12) → H(7,13)`, original node center `T(19,26)`, leftmost `J(6,12)`, current phase 0, outer state 0, cumulative `S=23`. The Direct/+0 extension uses the current unrotated ciphertext positions:

- `n₀(6,12)=147`, `μ(147)=0`.
- `n₀(7,13)=175`, `μ(175)=0`.
- `p_next=(0+0) mod 3=0`.
- Selected `n₁(6,12)=319`, `μ(319)=+1`; the outer state becomes `(0+1) mod 2=1`.

The predicted next signature is **`(+1,+1,+1)`**, matching derived `J–TH–U`. The phase is zero, so **`S=23` remains unchanged**.

## 4. Reading geometry from OF (Reports 02–03)

From OF's beginning `B=(6,12)`, endpoint `E=(7,13)`, and original center `M=(19,26)`:

`A=n₂(B)+n₀(M)=583+512=1095` and `μ(1095)=−1`.

`G_axis=gcd(n₁(E),n₂(E))=gcd(345,555)=15`, with `μ(15)=+1`.

Hence **`q_axis=−1+1=0` → HORIZONTAL**.

The original center rune of OF is `T=16`, for which `φ(16)=8`. With `n₃(E)=385` and `μ(385)=−1`:

`τ_next=[−1+8] mod 2=1` → leftmost must be the **BEGINNING**, so the horizontal block reads **rightward**.

The selected ciphertext **`P(20,12) → L(20,13)`** reads right on row 20, with leftmost `P(20,12)`. Its rotated position `n₁(20,12)=305` has `μ(305)=+1`, permitted by Direct mode.

## 5. Check reports 04–08

| Report | Prediction from OF | Selected second THE |
|:---|:---|:---|
| **04 — Center parity** | Even row / odd column | G(24,1) **even/odd** |
| **05 — Endpoint row** | Even | L(20,13) is in row 20 |
| **05 — Leftmost row** | Even | P(20,12) is in row 20 |
| **06 — Incoming ray** | From `L_OF=(6,12)` to `B_THE=(20,12)`: `Δ=(+14,0)`, `d₈=0`, permitted `q=0` | **Pass** |
| **07 — Next mirror status** | OF later outer `(20,25)` to `(6,12)` gives `d∞=14`, `14 mod 3=2` → **NON-MIRROR** | `J≠U/V` — **pass** |
| **08 — Minimum length** | Two or more ciphertext runes | **Two** |

Report 06's gate is 0 because `μ(n₀(E_OF))=μ(175)=0` but `μ(n₃(E_OF))=μ(385)=−1`: the one-cell deviation allowance requires **both** values to be zero. Report 04 predicts parity `(0,1)` and Report 05 predicts `(0,0)` for the two boundary rows.

## 6. Read and decrypt

| Cell | Ciphertext | Aligned key | Modular difference | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (20,12) | P = 13 | J = 11 | `13−11=2` | **TH** |
| (20,13) | L = 20 | TH = 2 | `20−2=18` | **E** |

## Result

**`TH · E` → THE**. **Phase `p=0`, accumulated `S=23`.** The third `U/V` key element is not consumed. Both subtractions are direct, without modulo wraparound.

## 7. Distinguishing the two new THE keys

| Property | THE (24) | THE (27) |
|:---|:---|:---|
| Ciphertext | T(9,19) → R(9,18) | P(20,12) → L(20,13) |
| Original source | L–X–S | J–G–U |
| Center handling | **Direct** (no φ) | **Center-only φ** |
| Final key | X–S–L, phase 1 | J–TH–U, phase 0 |
| Output | TH · E | TH · E |

Both plaintexts have `GP(THE)=72`, but they are obtained from **different original nodes and different operations**. This illustrates the branch's flexibility: matching a word twice with different key constructions does not by itself identify a unique cipher mechanism.

**Status:** The specified second THE passes modular arithmetic and conditional Reports 01–08. It belongs to a selected route using several non-mirror nodes and a proposed Direct/+0 phase extension. No unique-position selector or passing claim for an undocumented experimental Report 09 is established.
