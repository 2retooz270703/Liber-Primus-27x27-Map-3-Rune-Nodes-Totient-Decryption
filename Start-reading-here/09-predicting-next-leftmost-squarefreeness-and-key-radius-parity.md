# Predicting the Next Leftmost Cell's Squarefreeness and Key-Node Radius Parity

**Two New Binary Prediction Rules for the 27 × 27 Matrix**

*LP2 pages 0–2 · Original key-node centers · Ciphertext boundaries · Möbius squarefreeness · Key-node radius parity · Post-THEN candidate reduction*

---

The preceding reports predict the next decryption key's Möbius signature, the next ciphertext's axis and boundary role, coordinate parities, an incoming geometric ray, and whether the next original key node is mirrored. Two further binary relations constrain properties that those reports leave open:

1. **The squarefreeness of the next ciphertext's leftmost cell number in the original matrix.**
2. **The parity of the radius of the next original three-rune key node.**

Both rules reproduce **all 16 transitions** in the selected initial LP2 pages 0–2 reconstruction, from `AS I GO THE → WEATHER` through `SOON → THEN`. Both also match the **five candidate transitions** from `THEN → THE` through `TO → GO`, giving **21/21 on the selected extended route**.

These are concrete, forward-computable constraints. After `THEN`, the squarefreeness rule reduces **115 admissible leftmost cells to 44** for two-rune ciphertexts. The radius rule reduces **16 admissible mirrored key nodes to 9**. Together, they also reduce the placements and key-node realizations of the two-rune plaintext `THE` from **13 to 4** under the stated candidate enumeration.

**Research status:** the equalities and candidate counts are exact for the specified route and search definitions. Both rules were identified retrospectively, and the five-block continuation is a selected hypothesis rather than independently authenticated plaintext. The **21/21 fit is not a statistical proof of a Cicada 3301 traversal algorithm**. This report separates verified arithmetic from interpretation so the formulas can be frozen and tested prospectively.

**Contents**

[01. Foundations](#foundations) · [02. Predicting next-cell squarefreeness](#predicting-the-next-leftmost-cells-squarefreeness) · [03. Predicting next-node radius parity](#predicting-the-next-key-nodes-radius-parity) · [04. Complete 21-transition verification](#complete-21-transition-verification) · [05. The search after THEN](#the-search-after-then) · [06. Selectivity and limits](#selectivity-and-limits) · [Formula reference](#formula-reference)

---

## Foundations

### Coordinates and current-versus-next notation

The matrix has **27 rows and 27 columns**, indexed from `(1,1)` at the upper left. Rows increase downward and columns increase rightward. All coordinates in this report are **one-based**.

| Symbol | Meaning |
|---|---|
| `B` | Beginning of the **current** ciphertext: first cell in reading order. |
| `E` | Endpoint of the **current** ciphertext: last cell in reading order. |
| `L` | **Current** leftmost ciphertext cell: minimum column, bottommost row if tied. |
| `M` | Center of the **current original three-rune key node**, before center-totient transformation. |
| `p` | Phase of the **current derived key**, one of `0`, `1`, or `2`. |
| `L′` | Leftmost cell of the **next** ciphertext. |
| `M′` | Center of the **next original key node**. |
| `R′` | Radius of the **next original key node**, in grid steps. |
| `r(X), c(X)` | Row and column of cell `X`. |
| `φ, μ` | Euler's totient function and the ordinary Möbius function. |

The original row-major cell number is

$$
\boxed{n_0(r,c)=27(r-1)+c},\qquad 1\leq n_0\leq729.
$$

**The cell number is not the rune index.** `μ(n₀(L′))` measures the arithmetic class of a matrix position, while the derived key's own Möbius signature uses `μ(φ(kᵢ))` on rune indices. Those operations must not be conflated.

### Two binary outputs

The Möbius function satisfies `μ(n) ∈ {−1,0,+1}`. Its square is the **squarefree indicator**:

$$
\mu^2(n)=\begin{cases}
1,&n\text{ is squarefree},\\
0,&n\text{ has a squared prime divisor}.
\end{cases}
$$

Thus a predicted `0` means **exactly `μ(n) = 0`**; a predicted `1` permits `μ(n) = +1` or `−1`.

For a key-node radius, reduction modulo 2 has its ordinary geometric meaning: `0 = EVEN RADIUS`, `1 = ODD RADIUS`. In both rules, negative Möbius values are reduced modulo 2 in the usual way, so `−1 ≡ +1 (mod 2)`.

### Current-key phase and original-node radius

As in Reports 00–01, the current **derived**, unaligned key `K=(k₁,k₂,k₃)` has

$$
\sigma_i=\mu(\varphi(k_i)),\qquad
\boxed{p=(\sigma_1+\sigma_2+\sigma_3)\bmod3}.
$$

Compute the phase modulo **3 first**, then use its representative `0`, `1`, or `2` in the parity formula. The predicted radius applies to the **next original spatial node**, not to the cyclically rotated decryption key.

If the outer cells of that original node are `O₁′` and `O₂′`, they lie at equal integer-grid distance from its center `M′`. Its radius is

$$
R'=\max\!\left(|r(O'_1)-r(M')|,\ |c(O'_1)-c(M')|\right).
$$

This definition works for horizontal, vertical, and 45° diagonal nodes, including nodes whose **outer rune symbols differ**. It is a geometric distance, not a rune value or a totient.

---

## Predicting the Next Leftmost Cell's Squarefreeness

### The current ciphertext's endpoint span

Measure the eight-direction (Chebyshev) distance between the current ciphertext's beginning and endpoint:

$$
\boxed{D=\max\!\left(|r(B)-r(E)|,\ |c(B)-c(E)|\right)}.
$$

This uses **the two actual reading boundaries**, not the current leftmost cell. The first composite block `AS I GO THE` has a large endpoint span even though its ciphertext contains only seven runes; replacing `D` with its rune count would change the result for that block.

### The squarefreeness predictor

The next leftmost cell's original absolute position obeys the following empirical binary relation on the selected route:

$$
\boxed{
\mu^2\!\left(n_0(L')\right)
=\bigl[1+r(M)+p+D\bigr]\bmod2
}.
$$

| Calculated bit | Prediction for the next leftmost cell |
|:---:|---|
| **0** | `μ(n₀(L′)) = 0`: its original cell number is **not squarefree**. |
| **1** | `μ(n₀(L′)) ∈ {−1,+1}`: its original cell number **is squarefree**. |

**The calculation uses only current-block information.** It does not require the proposed next plaintext, its key, or its leftmost coordinate to compute the bit. The prospective cell is tested only afterward.

### A compact form for straight ciphertexts

For a straight, contiguous ciphertext of `N` cells, its beginning and endpoint are `N−1` king-like steps apart, so `D=N−1`. The same relation simplifies to

$$
\boxed{
\mu^2(n_0(L'))\equiv r(M)+p+N\pmod2
}\qquad\text{(straight contiguous current block)}.
$$

The simplified expression matches all **20 transitions whose current ciphertext is straight**. The complete `D` formulation also covers the composite starting block and gives **21/21** on the selected extended route. These are equivalent forms where `D=N−1`; they are not independent discoveries.

### Worked example — THEN → THE

The known `THEN` block has

$$
B=(25,25),\quad E=(25,27),\quad M=(26,22),\quad p=1.
$$

Its ciphertext boundary span is `D = 2`. Therefore

$$
\mu^2(n_0(L'))=[1+26+1+2]\bmod2=30\bmod2=0.
$$

**Prediction: the next leftmost cell must have `μ(n₀) = 0`.**

In the selected `THE` realization, the ciphertext is `J(22,21) → W(21,20)` and its leftmost cell is `L′=(21,20)`. Its original cell number is

$$
n_0(21,20)=27\cdot20+20=560=2^4\cdot5\cdot7.
$$

Hence `μ(560)=0`, exactly matching the prediction. This is a **conditional** test of the candidate THE, not an independently decrypted seventeenth observation.

---

## Predicting the Next Key Node's Radius Parity

### The current leftmost column and beginning checkerboard class

This second relation uses the **current ciphertext's leftmost cell `L`** and its **beginning `B`**. It combines two Möbius evaluations of the same current column with the ordinary coordinate sum at the beginning.

The next original key-node radius satisfies the following empirical relation:

$$
\boxed{
R'\equiv
c(L)+\mu(c(L))+\mu(\varphi(c(L)))+r(B)+c(B)
\pmod2
}.
$$

| Calculated bit | Prediction for the next original key node |
|:---:|---|
| **0** | The original node has an **even** radius. |
| **1** | The original node has an **odd** radius. |

This condition is different from Report 07's mirror-status predictor. Report 07 uses `d∞(Z,L) mod 3` to predict whether the **next original outer rune symbols match**. The present expression predicts the **integer parity of the next node's radius**, regardless of whether those symbols match. A mirrored node may have either even or odd radius.

### Worked example — THEN → THE

For `THEN`, the leftmost cell and beginning coincide:

$$
L=(25,25),\qquad B=(25,25).
$$

Since `μ(25)=0`, `φ(25)=20`, and `μ(20)=0`, the radius prediction is

$$
R'\equiv25+0+0+25+25=75\equiv1\pmod2.
$$

**Prediction: the next original key node has an ODD radius.**

The selected source of `THE` is the vertical mirror

$$
\mathrm{N}(17,17)\;–\;\mathrm{M}(20,17)\;–\;\mathrm{N}(23,17).
$$

The two outer cells are three rows from the center, so `R′=3`: **odd**, as predicted.

### A non-mirror check — YOU → SOON

For `YOU`, `L=(25,16)` and `B=(27,18)`. Here `μ(16)=0`, `φ(16)=8`, and `μ(8)=0`:

$$
R'\equiv16+0+0+27+18=61\equiv1\pmod2.
$$

The source node selected for the following `SOON` is **`L–C–EA`**, centered on `C(25,7)`, with outer cells `(25,4)` and `(25,10)`. Its radius is **3**, again odd. The outer rune symbols **L and EA are different**, confirming that the radius rule applies to the documented non-mirror class as well.

---

## Complete 21-Transition Verification

### Squarefreeness: 16 recorded + 5 conditional matches

The input triple is `(r(M), p, D)`. `b` is the predicted squarefreeness bit; the last column shows the actual Möbius value at the selected next leftmost cell's **original** absolute number. For `b=1`, either sign `+1` or `−1` is correct.

| # | Current → next block | `(r(M),p,D)` | Predicted `b` | Next `L′` | `n₀(L′)` | Actual `μ(n₀)` |
|---:|---|:---:|:---:|:---:|---:|:---:|
| 1 | AS I GO THE → WEATHER | `(13,0,21)` | **1** | `(14,14)` | 365 | `+1` ✓ |
| 2 | WEATHER → TURNS | `(14,2,4)` | **1** | `(14,19)` | 370 | `−1` ✓ |
| 3 | TURNS → COLD | `(14,0,4)` | **1** | `(14,7)` | 358 | `+1` ✓ |
| 4 | COLD → I MAY | `(26,1,3)` | **1** | `(26,16)` | 691 | `−1` ✓ |
| 5 | I MAY → CRY | `(15,0,3)` | **1** | `(19,16)` | 502 | `+1` ✓ |
| 6 | CRY → NOW THE | `(25,1,2)` | **1** | `(11,16)` | 286 | `−1` ✓ |
| 7 | NOW THE → IDEA | `(19,2,4)` | **0** | `(17,18)` | 450 | `0` ✓ |
| 8 | IDEA → OF | `(11,1,2)` | **1** | `(18,15)` | 474 | `−1` ✓ |
| 9 | OF → THE | `(17,0,1)` | **1** | `(19,16)` | 502 | `+1` ✓ |
| 10 | THE → END | `(19,2,1)` | **1** | `(21,23)` | 563 | `−1` ✓ |
| 11 | END → IS | `(23,2,2)` | **0** | `(21,9)` | 549 | `0` ✓ |
| 12 | IS → DEATH | `(21,1,1)` | **0** | `(26,1)` | 676 | `0` ✓ |
| 13 | DEATH → SEE | `(23,2,2)` | **0** | `(27,14)` | 716 | `0` ✓ |
| 14 | SEE → YOU | `(25,0,2)` | **0** | `(25,16)` | 664 | `0` ✓ |
| 15 | YOU → SOON | `(16,1,2)` | **0** | `(25,16)` | 664 | `0` ✓ |
| 16 | SOON → THEN | `(25,2,3)` | **1** | `(25,25)` | 673 | `−1` ✓ |
| **17** | **THEN → THE*** | `(26,1,2)` | **0** | `(21,20)` | 560 | `0` ✓ |
| 18 | THE* → KEY* | `(20,0,1)` | **0** | `(21,4)` | 544 | `0` ✓ |
| 19 | KEY* → IS* | `(12,1,2)` | **0** | `(19,6)` | 492 | `0` ✓ |
| 20 | IS* → TO* | `(17,1,1)` | **0** | `(9,16)` | 232 | `0` ✓ |
| 21 | TO* → GO* | `(8,0,1)` | **0** | `(9,20)` | 236 | `0` ✓ |

**Result: 16/16 on the initial recorded sequence; 5/5 on the candidate continuation; 21/21 combined.** The 21 predictions classify ten next-cell positions as squarefree and eleven as non-squarefree. The five starred blocks are **selected candidate plaintext**, not independently authenticated LP2 readings.

### Radius parity: 16 recorded + 5 conditional matches

Here `R′` is measured **in the next original key-generating node**, before its center rune is transformed with `φ`. The prediction uses only the **current** `L` and `B`.

| # | Current → next block | Current `L` | Current `B` | Predicted radius parity | Actual next radius |
|---:|---|:---:|:---:|:---:|---:|
| 1 | AS I GO THE → WEATHER | `(14,1)` | `(13,25)` | **Odd** | 1 ✓ |
| 2 | WEATHER → TURNS | `(14,14)` | `(14,14)` | **Even** | 10 ✓ |
| 3 | TURNS → COLD | `(14,19)` | `(14,19)` | **Odd** | 1 ✓ |
| 4 | COLD → I MAY | `(14,7)` | `(14,7)` | **Even** | 2 ✓ |
| 5 | I MAY → CRY | `(26,16)` | `(26,19)` | **Odd** | 1 ✓ |
| 6 | CRY → NOW THE | `(19,16)` | `(19,16)` | **Odd** | 1 ✓ |
| 7 | NOW THE → IDEA | `(11,16)` | `(11,16)` | **Odd** | 3 ✓ |
| 8 | IDEA → OF | `(17,18)` | `(15,20)` | **Even** | 2 ✓ |
| 9 | OF → THE | `(18,15)` | `(18,15)` | **Odd** | 1 ✓ |
| 10 | THE → END | `(19,16)` | `(19,17)` | **Even** | 4 ✓ |
| 11 | END → IS | `(21,23)` | `(19,23)` | **Odd** | 5 ✓ |
| 12 | IS → DEATH | `(21,9)` | `(21,9)` | **Even** | 4 ✓ |
| 13 | DEATH → SEE | `(26,1)` | `(26,3)` | **Even** | 4 ✓ |
| 14 | SEE → YOU | `(27,14)` | `(25,16)` | **Odd** | 11 ✓ |
| 15 | YOU → SOON | `(25,16)` | `(27,18)` | **Odd** | 3 ✓ |
| 16 | SOON → THEN | `(25,16)` | `(25,16)` | **Odd** | 1 ✓ |
| **17** | **THEN → THE*** | `(25,25)` | `(25,25)` | **Odd** | 3 ✓ |
| 18 | THE* → KEY* | `(21,20)` | `(22,21)` | **Odd** | 1 ✓ |
| 19 | KEY* → IS* | `(21,4)` | `(21,4)` | **Even** | 6 ✓ |
| 20 | IS* → TO* | `(19,6)` | `(18,7)` | **Odd** | 3 ✓ |
| 21 | TO* → GO* | `(9,16)` | `(9,16)` | **Odd** | 7 ✓ |

**Result: 16/16 on the initial recorded sequence; 5/5 on the candidate continuation; 21/21 combined.** Fourteen predicted radii are odd and seven are even.

**Source-node consistency:** the primary `SOON` choice throughout this report is `L–C–EA` with center `(25,7)` and radius `3`, matching Reports 04–05. Report 07 displays the later arm `(25,20)` from a different documented `SOON` source-node alternative in its summary table. That alternative must not be combined with the `(25,7)` center when measuring an original node's radius. Report 07's mirror-status result remains unchanged for the documented alternatives.

---

## The Search After THEN

### Reconstructing the 115 leftmost cells

This report uses the same **two-rune ciphertext** search baseline established by the preceding rules. After `THEN`:

- Report 03 requires a **DIAGONAL** next ciphertext.
- Report 02 requires the next leftmost cell to be the **END**, so the two-rune ciphertext starts one row above or below and one column to the right of its leftmost cell.
- Report 05 predicts an **ODD ROW** for that next endpoint and leftmost cell.
- Report 02 permits `μ(n₁(L′)) ∈ {0,−1}` in the active Reflected mode.
- Report 06 allows an incoming eight-direction ray deviation of **at most one cell** from `L_THEN=(25,25)` to the next beginning, because `q(THEN)=1`.

Enumeration of the 27 × 27 matrix under exactly these conditions gives **115 distinct leftmost cells**, represented by **170 oriented two-cell ciphertext placements**. Some leftmost cells permit both diagonal slopes, which is why the placement count exceeds the cell count.

### Apply the new squarefreeness condition

The predicted value from `THEN` is `μ(n₀(L′))=0`. Rechecking the 115 admissible cells produces:

| Test | Distinct leftmost cells | Oriented two-rune placements |
|---|---:|---:|
| Reports 02, 03, 05, 06 baseline | **115** | **170** |
| Plus next-cell squarefreeness rule | **44** | **69** |
| Excluded by the new squarefreeness rule | **71** | **101** |

The **115 → 44** reduction removes approximately **61.7%** of previously admissible leftmost cells. These are direct enumeration counts, not estimates. The criterion is compatible with the selected `THE` endpoint `W(21,20)`.

### Apply the new key-node radius condition

Report 01 predicts the following key's Möbius signature as `(+1,+1,+1)`. Report 04 predicts an original key-center **EVEN ROW and ODD COLUMN**; Report 07 predicts a **MIRRORED** original node.

Enumerating equally spaced, same-outer-rune key triples on horizontal, vertical, and 45° diagonal axes gives:

| Current restriction | Spatial nodes | Distinct centers | Distinct derived keys |
|---|---:|---:|---:|
| Predicted signature only | 44 | 36 | 26 |
| Signature + center row/column parity | **16** | **12** | **12** |
| Plus **odd original radius** | **9** | **7** | **8** |

The radius prediction after `THEN` is `R′ mod 2 = 1`, so **seven of the sixteen** already qualified spatial nodes are eliminated. The selected `N–M–N` node at center `(20,17)` has radius `3` and remains.

The two new restrictions act on different search dimensions. For two-rune diagonal placements, the resulting Cartesian search set has **69 eligible oriented placements × 9 eligible original nodes = 621 placement–node combinations**, compared with **170 × 16 = 2,720** before the two new filters. These raw combinations do not yet impose a chosen English plaintext.

### An exact two-rune plaintext control: THE

For `THE`, the target plaintext indices are **`TH · E = (2,18)`**. Because the next predicted signature is `(+1,+1,+1)`, its derived-key phase is `0`. Each candidate's first two aligned key elements can therefore be subtracted from its two ciphertext runes modulo `29` without a phase offset.

| Search state | `THE` key–ciphertext realizations |
|---|---:|
| Previous baseline (16 qualified key nodes and 170 placements) | **13** |
| Add squarefreeness of next leftmost cell | **10** |
| Also require an odd-radius key node | **4** |

The four surviving `THE` realizations are:

| Ciphertext beginning → endpoint | Derived key | Original key center | Radius |
|---|---|:---:|---:|
| `(10,9) → (9,8)` | `E–TH–E` | `(26,21)` | 5 |
| **`(22,21) → (21,20)`** | **`N–E–N`** | **`(20,17)`** | **3** |
| `(24,27) → (23,26)` | `E–TH–E` | `(26,21)` | 5 |
| `(24,5) → (25,4)` | `U–TH–U` | `(26,11)` | 1 |

The selected `N–M–N → N–E–N` source and its `J–W → TH–E` ciphertext **survive both rules**. The other three realizations are important controls: these binary constraints do **not** yet uniquely select the intended next word placement or key.

---

## Selectivity and Limits

### What the exact checks establish

1. The squarefreeness rule computes a binary property of the **next leftmost cell** using the **current original center row, current phase, and current ciphertext endpoint span**.
2. The radius rule computes the **next original key-node radius parity** using the **current leftmost column and current ciphertext beginning**.
3. Both relations give **16/16 historical fits and 5/5 conditional candidate fits**, without changing coefficients between the initial and extended routes.
4. After `THEN`, the conditions give **115 → 44 distinct next leftmost cells** and **16 → 9 spatial key nodes**, respectively.
5. When the desired next plaintext is separately fixed as the two-rune `THE`, the full enumeration gives **13 → 4** viable key–ciphertext realizations under these two additional conditions.

### The unavoidable multiple-testing qualification

These formulas were discovered by comparing many numerical features against the recorded route. In the examined family of short XOR-style parity expressions, **14 distinct four-term formulas** matched the original 16 transitions for the next-cell squarefreeness target, and **17 distinct four-term formulas** matched the original 16 transitions for the next-radius target. In each family, **one** formula also matched all five selected continuation transitions.

This selection result is useful for identifying compact candidates; it is **not** evidence that the chosen formula is mathematically unique or statistically surprising after the broader search. The five post-THEN blocks were themselves selected using other project constraints. Their agreement must not be reported as five independent blind tests.

Two further cautions are material:

- **Source-node choices matter.** The radius rule measures an actual original spatial triple. Different source triples producing the same derived key can have different radii. The verification fixes the primary `SOON` original node consistently with Reports 04–05.
- **The binary classifiers do not generate a coordinate.** Squarefreeness leaves 44 possible leftmost cells. Radius parity leaves nine source nodes. Neither rule predicts the next ray direction, movement distance, complete key, or plaintext by itself.

### A fixed next-transition forecast

If the selected `GO` block is accepted as current, its recorded inputs are:

$$
B=(9,20),\quad E=(9,21),\quad M=(12,14),\quad p=0,\quad L=(9,20).
$$

The squarefreeness relation gives `D=1`, hence

$$
\mu^2(n_0(L'))=[1+12+0+1]\bmod2=0.
$$

The radius relation uses `c(L)=20`, `μ(20)=0`, `φ(20)=8`, `μ(8)=0`:

$$
R'\equiv20+0+0+9+20=49\equiv1\pmod2.
$$

**Frozen conditional forecast after GO:** the following leftmost cell has **`μ(n₀)=0`**, and the following original key node has an **ODD radius**. This forecast has not been tested against an independently determined subsequent block; it is stated here to make prospective falsification possible without altering either formula.

### Research conclusion

The two formulas add **distinct, reproducible binary constraints** to the project's existing search framework. Their strongest immediate contribution is not an additional English coincidence but the ability to remove inadmissible future **cell positions and source-node radii** before decrypting a candidate plaintext.

The next decisive step is to hold both formulas fixed while testing **alternative admissible branches and independently supported future ciphertexts**. Successful agreement across those controls would strengthen the hypothesis that the relations reflect a common traversal process rather than retrospective arithmetic selection.

---

## Formula Reference

All coordinates are **one-based**. `B`, `E`, `L`, `M`, and `p` are **current-block** inputs. Prime marks designate the **next block**.

**1 · Original absolute cell number**

$$
n_0(r,c)=27(r-1)+c.
$$

**2 · Current endpoint span**

$$
D=\max(|r(B)-r(E)|,\ |c(B)-c(E)|).
$$

**3 · Next leftmost cell's squarefreeness**

$$
\boxed{\mu^2(n_0(L'))=[1+r(M)+p+D]\bmod2}.
$$

`0` means `μ(n₀(L′))=0`; `1` means `μ(n₀(L′))=±1`.

**4 · Equivalent form for a straight contiguous current ciphertext of N runes**

$$
\boxed{\mu^2(n_0(L'))\equiv r(M)+p+N\pmod2}.
$$

**5 · Next original key-node radius parity**

$$
\boxed{R'\equiv c(L)+\mu(c(L))+\mu(\varphi(c(L)))+r(B)+c(B)\pmod2}.
$$

`0 = EVEN RADIUS`; `1 = ODD RADIUS`.

**6 · Original source-node radius**

$$
R'=\max(|r(O'_1)-r(M')|,\ |c(O'_1)-c(M')|).
$$

**7 · Selected-route fit and post-THEN selectivity**

| New predictor | Recorded transitions | Conditional continuation | Combined selected route | Post-THEN reduction |
|---|:---:|:---:|:---:|---|
| Next-leftmost squarefreeness | 16/16 | 5/5 | **21/21** | **115 → 44 leftmost cells** |
| Next-original-node radius parity | 16/16 | 5/5 | **21/21** | **16 → 9 mirrored source nodes** |

---

### Related project reports

- [00 — The 27 × 27 Matrix / Decryption Method](00-decryption-method.md)
- [01 — Predicting the Next Key](01-next-key-signature.md)
- [02 — Predicting the Leftmost Cell](02-leftmost-cell-and-rotations.md)
- [03 — Predicting the Reading Axis](03-predicting-axis-and-reading-direction.md)
- [04 — Predicting the Next Key's Center Parity](04-predicting-next-key-center-parity.md)
- [05 — Predicting the Next Ciphertext's Row Parity](05-predicting-next-ciphertext-row-parity.md)
- [06 — Predicting the Next Ciphertext's Ray and Möbius-Gated Deviation](06-predicting-next-ciphertext-ray-and-mobius-deviation.md)
- [07 — Predicting the Next Key's Mirror Status](07-predicting-next-key-mirror-status.md)
- [08 — Minimum Ciphertext Block Length](08-minimum-ciphertext-block-length.md)

*Data provenance:* the supplied snapshot of [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption), its `0-2-live-map.html` matrix, the selected primary `plaintext-i-found/01`–`17` blocks, and the selected candidate `18`–`22` continuation. Both mathematical fits and all search-space counts were recalculated for this particular snapshot. The proposed continuation is a research hypothesis; no claim of independent Cicada 3301 authentication is made.
