# Predict the Next Key's Möbius Signature

The phase rule in **`Next-Key.md`** predicts the rotation of the next three-rune key from the cells of the current ciphertext. A second compact pattern predicts one additional property: **whether the next key's two outer Möbius components are both `0` or both `+1`.**

Together, these two predictions determine the complete next-key Möbius signature on the known route. The combined calculation matches **all 16 consecutive transitions, from `AS I GO THE` through `THEN`**, including the unusual signatures of `CRY`, `OF`, and `SOON`.

The new pattern has a simple interpretation: **a two-state machine switches whenever a geometrically selected cell has a square-free number under a 90° rotation of the matrix.** The same update rule applies throughout the route, without changing formulas between passages.

> **Research status:** this is a deterministic candidate selected retrospectively from the known route. The 16/16 matches are reproducible, but its prediction beyond `THEN` has not been independently tested. It is not yet established as part of Cicada's original algorithm.

### Definitions

- **`C`** — the set of `(row, column)` coordinates belonging to the current ciphertext block.
- **`r`, `c`** — a cell's row and column, both counted from **1 to 27**. Rows increase downward; columns increase to the right.
- **`K = (k₁, k₂, k₃)`** — the current derived key, expressed as rune indices modulo 29, **before its cyclic phase rotation**. For a node transformed by the center-totient rule, this is the key after that transformation.
- **`φ(n)`** — Euler's totient function.
- **`μ(n)`** — the Möbius function, whose result is `−1`, `0`, or `+1`.
- **`σ(K)`** — the key's Möbius signature: `(μ(φ(k₁)), μ(φ(k₂)), μ(φ(k₃)))`.
- **`a`** — the shared outer component of the current key's signature.
- **`m`** — the smallest position occupied by the current ciphertext after rotating the coordinates 90° clockwise and numbering the resulting matrix row by row.
- **`p_next`** — the next-key phase predicted by the existing phase rule, with value `0`, `1`, or `2`.

The inputs belong to the **current** block. The next key's runes are not needed to calculate the forecast. The current block's boundaries must already be known: this rule does not determine where its ciphertext ends.

---

## 1. One additional bit of key information

Every one of the 17 recorded keys has equal outer Möbius components, each belonging to `{0, +1}`. Its signature can therefore be written as:

$$
\sigma(K)=(a,b,a),\qquad a\in\{0,1\},\quad b\in\{-1,0,1\}.
$$

This describes the Möbius values of the derived key, not necessarily identical outer runes. It also holds for the asymmetric keys `AE–I–EA`, `H–NG–C`, and `L–R–EA`.

The signature state has two values:

| State | Meaning |
|:--:|:--|
| **0** | Both outer Möbius components are `0`. |
| **1** | Both outer Möbius components are `+1`. |

The first key, `AE–I–EA`, has signature `(0,0,0)`, so the initial state is **`a = 0`**. This follows from the key itself; it is not a freely fitted starting value.

Equal outer components and the restriction to `{0,+1}` are observations about this route. Extending this signature class to subsequent keys is part of the hypothesis. The state is a numerical property of the key; it does not by itself identify a geometric CENTER or OUTER position in the matrix.

---

## 2. Select one cell by geometry

Rotate the matrix coordinates **90° clockwise**:

$$
(r,c)\longmapsto(c,28-r).
$$

The ordinary absolute position of a cell `(r,c)` is `27(r−1)+c`. Applying that numbering to its rotated coordinates gives:

$$
n_{90}(r,c)=27(c-1)+28-r.
$$

Take the smallest rotated position among all cells of the current ciphertext:

$$
\boxed{m=\min_{(r,c)\in C}\left[27(c-1)+28-r\right]}.
$$

There is a direct way to select the same cell in the original matrix:

1. Find the **leftmost column occupied by the current ciphertext**.
2. Within that column, choose the **lowest occupied cell**.
3. Calculate its position using `27(c−1)+28−r`.

This is also equivalent to numbering the original matrix by columns from left to right, reading each column **from bottom to top**. The rotation supplies an auxiliary numbering for the calculation.

The selected cell can be the beginning, the end, or an interior cell of the ciphertext. One geometric rule chooses it in every case.

| Current ciphertext | Selected cell | Why it is selected | Rotated position |
|:--|:--:|:--|--:|
| `AS I GO THE` | `TH(14,1)` | The block crosses a row boundary; column 1 is its leftmost occupied column. | 14 |
| `WEATHER` | `NG(14,14)` | First cell of a horizontal rightward block. | 365 |
| `IDEA` | `D(17,18)` | Last cell of a diagonal down-left block. | 470 |
| `THEN` | `L(25,25)` | First cell of a horizontal rightward block. | 651 |

---

## 3. Update the two-state machine

Apply the Möbius function to the selected position and update the outer signature state:

$$
\boxed{a_{\text{next}}=\left(a+\mu(m)\right)\bmod2}.
$$

For this update, `+1` and `−1` have the same effect: both switch the state. A zero preserves it.

| Current state | `μ(m) = 0` | `μ(m) = +1` or `−1` |
|:--:|:--:|:--:|
| 0 | Stay at 0 | Switch to 1 |
| 1 | Stay at 1 | Switch to 0 |

The Möbius function explains the trigger:

- If `m` contains a squared prime factor, `μ(m) = 0`.
- If `m` is square-free, `μ(m)` is `+1` or `−1`, according to the number of distinct prime factors.

For example:

| Position | Prime factorization | Möbius value | State update |
|--:|:--|:--:|:--|
| 176 | `2⁴ × 11` | 0 | Preserve the state. |
| 407 | `11 × 37` | +1 | Switch the state. |
| 470 | `2 × 5 × 47` | −1 | Switch the state. |

Thus the candidate has a simple operating principle: **switch on a square-free selected position; otherwise retain the previous state.** It has no fixed block length or switching threshold. Several consecutive blocks can preserve the same state.

Starting with `a = 0` for `AS I GO THE`, the update reproduces all subsequent outer states recursively. Once started, the calculation can carry its own predicted state forward rather than replacing it with the observed state at each transition.

---

## 4. Recover the complete signature from the phase

For a signature `(a,b,a)`, the phase is:

$$
p=(a+b+a)\bmod3=(2a+b)\bmod3.
$$

Consequently, the next phase and the newly predicted outer state determine the central component:

$$
b_{\text{next}}\equiv p_{\text{next}}-2a_{\text{next}}\pmod3.
$$

Use the representative from `{−1,0,+1}`: remainder `0` means `0`, remainder `1` means `+1`, and remainder `2` means `−1`.

The resulting lookup table is:

| Predicted next phase | If `a_next = 0` | If `a_next = 1` |
|:--:|:--:|:--:|
| **0** | `(0,0,0)` | `(+1,+1,+1)` |
| **1** | `(0,+1,0)` | `(+1,−1,+1)` |
| **2** | `(0,−1,0)` | `(+1,0,+1)` |

**The phase rule selects a row; the new signature rule selects a column. Together they predict the complete signature.**

The independent contribution of the new rule is the outer state `a_next`. The central component is recovered algebraically using the existing phase prediction; it is not a separate independent discovery.

---

## 5. Check every known transition

`OF` and `THE` are treated as separate ciphertext blocks. The `SOON` used here is the primary `X–D–W–H` route with the rotated key `EA–L–R`.

The tables follow the same three observed phase regimes as `Next-Key.md`. These headings describe the **phase calculation**; the binary signature update remains unchanged throughout.

### Direct/+1 — AS I GO THE → IDEA

| Current ciphertext → Next key | Rotated minimum `m` | `μ(m)` | State `a → a_next` | Predicted signature | Known signature | Match |
|:--|--:|--:|:--:|:--:|:--:|:--:|
| `AS I GO THE` → `WEATHER` | 14 | +1 | 0 → 1 | `(+1, 0, +1)` | `(+1, 0, +1)` | ✅ |
| `WEATHER` → `TURNS` | 365 | +1 | 1 → 0 | `(0, 0, 0)` | `(0, 0, 0)` | ✅ |
| `TURNS` → `COLD` | 500 | 0 | 0 → 0 | `(0, +1, 0)` | `(0, +1, 0)` | ✅ |
| `COLD` → `I MAY` | 176 | 0 | 0 → 0 | `(0, 0, 0)` | `(0, 0, 0)` | ✅ |
| `I MAY` → `CRY` | 407 | +1 | 0 → 1 | `(+1, −1, +1)` | `(+1, −1, +1)` | ✅ |
| `CRY` → `NOW THE` | 414 | 0 | 1 → 1 | `(+1, 0, +1)` | `(+1, 0, +1)` | ✅ |
| `NOW THE` → `IDEA` | 422 | +1 | 1 → 0 | `(0, +1, 0)` | `(0, +1, 0)` | ✅ |

**Result: 7/7 complete-signature matches.**

### Reflected/+0 — IDEA → DEATH

| Current ciphertext → Next key | Rotated minimum `m` | `μ(m)` | State `a → a_next` | Predicted signature | Known signature | Match |
|:--|--:|--:|:--:|:--:|:--:|:--:|
| `IDEA` → `OF` | 470 | −1 | 0 → 1 | `(+1, +1, +1)` | `(+1, +1, +1)` | ✅ |
| `OF` → `THE` | 388 | 0 | 1 → 1 | `(+1, 0, +1)` | `(+1, 0, +1)` | ✅ |
| `THE` → `END` | 414 | 0 | 1 → 1 | `(+1, 0, +1)` | `(+1, 0, +1)` | ✅ |
| `END` → `IS` | 601 | −1 | 1 → 0 | `(0, +1, 0)` | `(0, +1, 0)` | ✅ |
| `IS` → `DEATH` | 223 | −1 | 0 → 1 | `(+1, 0, +1)` | `(+1, 0, +1)` | ✅ |

**Result: 5/5 complete-signature matches.**

### Reflected/+1 — DEATH → THEN

| Current ciphertext → Next key | Rotated minimum `m` | `μ(m)` | State `a → a_next` | Predicted signature | Known signature | Match |
|:--|--:|--:|:--:|:--:|:--:|:--:|
| `DEATH` → `SEE` | 2 | −1 | 1 → 0 | `(0, 0, 0)` | `(0, 0, 0)` | ✅ |
| `SEE` → `YOU` | 352 | 0 | 0 → 0 | `(0, +1, 0)` | `(0, +1, 0)` | ✅ |
| `YOU` → `SOON` | 408 | 0 | 0 → 0 | `(0, −1, 0)` | `(0, −1, 0)` | ✅ |
| `SOON` → `THEN` | 408 | 0 | 0 → 0 | `(0, +1, 0)` | `(0, +1, 0)` | ✅ |

**Result: 4/4 complete-signature matches. Overall: 16/16.**

---

## 6. Three informative examples

The phase alone does not distinguish the two signatures in its row of the lookup table. Three transitions are particularly useful because they require the less frequent signature of their respective phase.

### I MAY → CRY

The current key is `NG–T–NG`, whose outer Möbius components are both zero. Therefore `a = 0`.

The ciphertext is read leftward along row 26, ending at `E(26,16)`. This is its leftmost cell, so:

$$
m=27(16-1)+28-26=407=11\times37.
$$

There is no repeated prime factor, so `μ(407) = +1`:

$$
a_{\text{next}}=(0+1)\bmod2=1.
$$

The phase rule predicts `p_next = 1`. Hence:

$$
b_{\text{next}}\equiv1-2\times1\equiv-1\pmod3.
$$

The complete prediction is **`(+1,−1,+1)`**. The actual `CRY` key, `E–G–E`, has precisely that signature.

### IDEA → OF

The current key is `A–U–A`, with signature `(0,+1,0)`, so `a = 0`.

The selected ciphertext cell is `D(17,18)`:

$$
m=27(18-1)+28-17=470=2\times5\times47.
$$

Here `μ(470) = −1`. Modulo 2, adding `−1` switches zero to one:

$$
a_{\text{next}}=(0-1)\bmod2=1.
$$

The predicted next phase is `0`, so `b_next = +1`. The complete prediction is **`(+1,+1,+1)`**, matching the `OF` key `J–OE–J`.

### YOU → SOON

The current key is `P–TH–P`, with signature `(0,+1,0)`, so `a = 0`.

The selected ciphertext cell is `X(25,16)`:

$$
m=27(16-1)+28-25=408=2^3\times3\times17.
$$

The repeated factor 2 gives `μ(408) = 0`; the state remains zero. The next phase is `2`, so `b_next = −1`.

The complete prediction is **`(0,−1,0)`**, matching the unrotated `SOON` key `L–R–EA`.

All three cases follow the same update and the same phase-to-signature table. No special exception is added for any of them.

---

## 7. How it fits the four-state phase hypothesis

The existing phase hypothesis changes its arithmetic regime as the cumulative phase sum crosses successive multiples of 7:

*Direct/+0 → Direct/+1 → Reflected/+0 → Reflected/+1 → Direct/+0 → …*

The known route begins in *Direct/+1*. The new rule supplies a second state variable: the outer signature value `a`, with states `0` and `1`.

| Component | State information | Update principle | Output |
|:--|:--|:--|:--|
| Existing phase model | One of four arithmetic regimes, plus the accumulated phase counter. | Use current ciphertext positions; change regime at the proposed multiples-of-7 thresholds. | Next phase `p_next`. |
| Signature candidate | One binary value, `a`. | Switch when the selected rotated position is square-free. | Next outer component `a_next`. |
| Combined forecast | Predicted phase and predicted outer component. | Solve `b_next ≡ p_next − 2a_next (mod 3)`. | Complete next-key signature. |

Four phase regimes and two outer states produce **eight combinations of the main regime labels**. The phase counter must still be retained, so this does not establish a complete eight-state automaton. It is a possible combined architecture, conditional on both patterns continuing beyond the known route.

The geometry is also complementary: the phase model uses original or centrally reflected positions, while the signature candidate uses a 90° rotated numbering and one extreme ciphertext cell. Whether these operations reflect an intentional design remains an open question.

---

## 8. Prediction after THEN

The `THEN` ciphertext consists of:

| Cell | Ciphertext rune |
|:--:|:--:|
| `(25,25)` | L |
| `(25,26)` | T |
| `(25,27)` | W |

Its unrotated key is `IA–E–IA`, with signature `(0,+1,0)`. The current outer state is therefore `a = 0`.

The selected cell is `L(25,25)`:

$$
m=27(25-1)+28-25=651=3\times7\times31.
$$

The three distinct prime factors give `μ(651) = −1`, so:

$$
\boxed{a_{\text{next}}=(0-1)\bmod2=1}.
$$

In the existing phase model, the accumulated phase sum is `S = 18`. The model remains in *Reflected/+1*. The original ciphertext positions are `673,674,675`; their reflected positions are `57,56,55`, with Möbius values `+1,0,+1`.

$$
p_{\text{next}}=(1+1+0+1)\bmod3=0.
$$

Combining phase `0` with outer state `1` gives:

$$
\boxed{\sigma_{\text{next}}=(+1,+1,+1),\qquad p_{\text{next}}=0}.
$$

| Current ciphertext → Next key | Predicted phase | Predicted signature | Known signature | Status |
|:--|:--:|:--:|:--:|:--:|
| `THEN` → Unknown | 0 | `(+1,+1,+1)` | Unknown | **Untested** |

Among equally spaced symmetric mirrors in the supplied matrix for which all key-index arithmetic is defined, phase `0` leaves **155 candidate nodes**. Requiring the complete signature `(+1,+1,+1)` leaves **44 nodes representing 26 distinct three-rune keys**.

This is an additional constraint on the search. It does not yet choose a unique key, locate the next ciphertext, or determine its reading direction and length.

---

## 9. What makes the pattern interesting—and what remains unproven

The candidate has several useful properties:

- **One fixed formula** matches all 16 transitions across three observed phase regimes.
- **One fixed geometric selection** determines the cell used at every stage.
- **One initial state** follows directly from the first known key.
- **The state can be propagated recursively**, without inserting the observed next state at each step.
- **The less frequent signatures of CRY, OF, and SOON** are recovered without special cases.
- **A specific future forecast** has been fixed: outer state `+1`, and, together with the existing phase rule, signature `(+1,+1,+1)` after `THEN`.

In a comparison of **eight square symmetries × two extreme-position selectors**, only the **90° clockwise/minimum** variant matches all 16 transitions.
