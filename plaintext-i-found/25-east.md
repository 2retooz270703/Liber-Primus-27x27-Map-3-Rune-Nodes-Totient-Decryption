# 25 — EAST

*Candidate continuation: **THE KEY IS TO GO TO THE EAST OF THE MAP***

This is **candidate block 25**, following TO (23) and THE (24). Its three-cell ciphertext `TH–N–C/K` is read **down-left** and yields **`EA · S · T` → EAST**. Here **`EA` is one rune**, not the separate runes `E` and `A`: the block therefore has **three** plaintext runes, despite spelling four English letters.

The source key is a **non-mirror** diagonal `E–O–D`. No center totient transformation is used for this particular node; its original indices are cyclically rotated by phase 1. This is still a *candidate* continuation after the original 17-block reconstruction, not an authenticated LP2 reading. Coordinates `(r,c)` are one-based. Rune-index arithmetic is modulo 29, while GP uses prime values. Rotations use `n₀=27(r−1)+c`, `n₁=27(c−1)+28−r`, `n₂=730−n₀`, `n₃=27(27−c)+r`.

## 1. Locate the original node

| Role | Coordinate | Matrix rune | Index |
|:---|:---:|:---:|---:|
| First outer | (6,10) | E | 18 |
| **Center** | **(13,17)** | **O** | **3** |
| Second outer | (20,24) | D | 23 |

This is a **down-right diagonal** with radius **seven cells** in each coordinate. The midpoint is `(13,17)` and the arms `E` and `D` differ, making the original triple **NON-MIRROR** under Report 07. The center's absolute position is `n₀(13,17)=341`.

## 2. Derive the untransformed key and align it

The selected original source is used **directly**, without replacing center `O=3` by `φ(3)=2`. The unrotated key is `E–O–D = (18,3,23)`.

| Key rune | Index | Totient | Möbius value |
|:---:|---:|---:|:---:|
| E | 18 | 6 | +1 |
| O | 3 | 2 | −1 |
| D | 23 | 22 | +1 |

The signature is **`(+1,−1,+1)`** and the phase is `p=(1−1+1) mod 3=1`. One cyclic left shift gives **`O–D–E`**, aligned indices **`(3,23,18)`**. All three elements are used.

## 3. Predict the next key from THE (Report 01)

Current THE ciphertext: `T(9,19) → R(9,18)`; original center `X(14,4)`; leftmost `R(9,18)`; phase 1; outer state 0; accumulated **`S=22`**. Report 01 uses the proposed **Direct/+0** mode.

- Current original absolute positions: `n₀(T)=235`, `n₀(R)=234`.
- `μ(235)=+1`, `μ(234)=0`, so `p_next=(1+0) mod 3=1`.
- The selected leftmost rotated position is `n₁(9,18)=478`, with `μ(478)=+1`.
- Updated outer state `(0+1) mod 2=1`; required signature **`(+1,−1,+1)`**.

The selected direct `E–O–D` key realizes this prediction. **`S` increases from 22 to 23.**

## 4. Axis, boundary, and placement (Reports 02–03)

From current THE beginning `B=(9,19)`, endpoint `E=(9,18)`, original center `M=(14,4)`:

- `A=n₂(B)+n₀(M)=495+355=850`, giving `μ(A)=0`.
- `G_axis=gcd(n₁(E),n₂(E))=gcd(478,496)=2`, giving `μ(G_axis)=−1`.
- `q_axis=0−1=−1`: predicted **DIAGONAL**.
- With original center rune `X=14`, `τ_next=[μ(n₃(E))+φ(14)] mod 2=[μ(252)+6] mod 2=0`: leftmost is the **END**.

The selected ciphertext is:

| Order | Coordinate | Cipher rune | Role |
|:---:|:---:|:---:|:---|
| 1 | (14,24) | TH | Beginning |
| 2 | (15,23) | N | Interior |
| 3 | (16,22) | C/K | **Endpoint and leftmost** |

It follows a **down-left 45° diagonal**. The leftmost cell's quarter-turn index is `n₁(16,22)=579`, whose Möbius value is **+1**, allowed by Direct mode.

## 5. Parities, gated ray, and mirror status (Reports 04–08)

| Report | Prediction from THE | Selected EAST |
|:---|:---|:---|
| **04 — Center parity** | Odd row / odd column | O(13,17): **odd/odd** |
| **05 — Endpoint / leftmost row** | Even / even | Both are the endpoint in **row 16** |
| **06 — Incoming eight-ray** | From THE's `L=(9,18)` to EAST's `B=(14,24)`: `Δ=(+5,+6)`, `d₈=1`; permitted `q=1` | **Pass at the one-cell limit** |
| **07 — Next mirror status** | THE later outer `(17,4)` to `L=(9,18)`: `d∞=14`, `14 mod 3=2` → **NON-MIRROR** | `E≠D` — **pass** |
| **08 — Minimum block length** | Two or more ciphertext runes | **Three** |

For Report 06, the current THE endpoint `R(9,18)` has `n₀=234` and `n₃=252`. Both `μ(234)=0` and `μ(252)=0`, so exactly **one cell of deviation** is allowed. Report 04 gives parity bits `(1,1)` and Report 05 `(0,0)` without consulting EAST's chosen coordinates.

## 6. Rune-by-rune decryption

| Cipher cell | Cipher rune/index | Aligned key/index | Calculation | Plaintext rune |
|:---:|:---:|:---:|:---:|:---:|
| (14,24) | TH = 2 | O = 3 | `2−3≡28 (mod 29)` | **EA** |
| (15,23) | N = 9 | D = 23 | `9−23≡15 (mod 29)` | **S** |
| (16,22) | C/K = 5 | E = 18 | `5−18≡16 (mod 29)` | **T** |

## Result

**`EA · S · T` → EAST**. **Phase `p=1`; accumulated `S=23`.** All three key elements are consumed and all three differences wrap modulo 29.

## 7. Numerical and geographic observations

| Portion of the new continuation | Number of plaintext runes | GP sum |
|:---|---:|---:|
| TO | 2 | 66 |
| THE | 2 | 72 |
| EAST | 3 | 221 |
| **TO THE EAST** | **7** | **359** |

**359 is the 72nd prime**, while the proposed full reading up through preceding `GO` contains **72 runes**. The three selected EAST ciphertext positions have columns **24, 23, 22**, all on the **east side** of the matrix's central column 14. The GP of the EAST **ciphertext** is `5+29+13=47`, matching `GP(X)=47`, the original center rune of the preceding THE node and, later, the selected MAP node.

**Conditional status:** Reports 01–08 and exact modular subtraction agree for the chosen placements. The one-cell ray allowance permits this beginning but does not select it uniquely. The direct use of a non-mirror key and the unobserved Direct/+0 phase mode are explicit model assumptions, and no authenticity claim or Report 09 pass claim is made.
