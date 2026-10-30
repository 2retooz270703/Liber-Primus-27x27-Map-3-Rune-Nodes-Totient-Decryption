# Predicting the Next Key’s Center Parity

**Row and column parity · LP2 pages 0–2**

Two formulas predict whether the next original key-node center lies in an **even or odd row and column**, using coordinates from the current block.

## 1. Inputs

The matrix has **27 rows and 27 columns**, numbered from 1. Coordinates are `(row, column)`; rows increase downward and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current ciphertext |
| E | Last cell read in the current ciphertext |
| M | Current original key-node center, before any center-totient transformation |
| M′ = (r′, c′) | Next original key-node center |

For a cell `X`, `r(X)` and `c(X)` are its row and column coordinates. These are **coordinate numbers**, not rune indices or prime values.

The output is a pair of parity bits, ordered **(row, column)**:

- **0 = even.**
- **1 = odd.**

For example, `(0,1)` means **even row, odd column**. It is a parity label, not a cell coordinate.

## 2. Predict the two parities

### Column parity

Add the three current row coordinates and 1, then reduce modulo 2:

$$
c'\equiv1+r(B)+r(E)+r(M)\pmod 2.
$$

This rule uses only row numbers.

### Row parity

First calculate the beginning’s absolute position and its position after a **180° turn**:

$$
n_0(B)=27\bigl(r(B)-1\bigr)+c(B),\qquad
n_2(B)=730-n_0(B).
$$

Then calculate:

$$
r'\equiv1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\pmod 2.
$$

The Möbius value is **0** when the integer has a repeated prime factor and **±1** when it is square-free. Modulo 2:

- **μ = 0:** keep the parity of the other terms.
- **μ = +1 or −1:** toggle it.

Only square-freeness matters here; both nonzero signs have the same effect.

### Shared structure

Both rules contain `1 + r(E) + r(M)`. Adding them modulo 2 cancels this common term:

$$
r'+c'\equiv r(B)+c(B)+\mu\bigl(n_2(B)\bigr)\pmod 2.
$$

This gives the next center’s checkerboard class using only the current beginning. It follows from the two rules and adds no independent constraint.

## 3. Worked example: COLD → I MAY

COLD begins at **`G(14,7)`**, ends at **`A(11,7)`**, and uses the original node centered on **`TH(26,19)`**.

The beginning’s absolute positions are:

$$
n_0(B)=358,\qquad n_2(B)=730-358=372.
$$

Since `372 = 2² × 3 × 31`, `μ(372) = 0`.

**Column:**

$$
c'\equiv1+14+11+26=52\equiv0\pmod 2.
$$

**Row:**

$$
r'\equiv1+7+11+26+0=45\equiv1\pmod 2.
$$

The prediction is **odd row, even column**. The recorded I MAY node is centered on **`B(15,8)`**, matching both bits.

## 4. Check against the recorded route

All inputs below belong to the current block. The next center is the recorded comparison target. OF and THE are separate blocks; SOON uses the primary ciphertext and the original **`L–C–EA`** node centered on **`C(25,7)`**.

| Transition | B | E | M | Next center | Predicted (row, column) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AS I GO THE → WEATHER | (13,25) | (14,4) | (13,12) | (14,5) | (0,1) |
| WEATHER → TURNS | (14,14) | (14,18) | (14,5) | (14,23) | (0,1) |
| TURNS → COLD | (14,19) | (10,19) | (14,23) | (26,19) | (0,1) |
| COLD → I MAY | (14,7) | (11,7) | (26,19) | (15,8) | (1,0) |
| I MAY → CRY | (26,19) | (26,16) | (15,8) | (25,16) | (1,0) |
| CRY → NOW THE | (19,16) | (17,16) | (25,16) | (19,16) | (1,0) |
| NOW THE → IDEA | (11,16) | (15,20) | (19,16) | (11,16) | (1,0) |
| IDEA → OF | (15,20) | (17,18) | (11,16) | (17,18) | (1,0) |
| OF → THE | (18,15) | (18,16) | (17,18) | (19,16) | (1,0) |
| THE → END | (19,17) | (19,16) | (19,16) | (23,12) | (1,0) |
| END → IS | (19,23) | (21,23) | (23,12) | (21,22) | (1,0) |
| IS → DEATH | (21,9) | (21,10) | (21,22) | (23,12) | (1,0) |
| DEATH → SEE | (26,3) | (26,1) | (23,12) | (25,6) | (1,0) |
| SEE → YOU | (25,16) | (27,14) | (25,6) | (16,16) | (0,0) |
| YOU → SOON | (27,18) | (25,16) | (16,16) | (25,7) | (1,1) |
| SOON → THEN | (25,16) | (25,19) | (25,7) | (26,22) | (0,0) |

Each formula matches **16/16 transitions**, and both bits match jointly in all 16. The rules were found by searching this sequence; unseen transitions have not yet been tested. The two match counts are not independent experiments.

### Distinguishing the SOON centers

Three documented nodes produce the same derived key **`L–R–EA`** by applying Euler’s totient function, `φ`, to the center rune’s index:

$$
\varphi(5)=\varphi(10)=\varphi(12)=4=\mathrm{R}.
$$

The preceding YOU block has `B = (27,18)`, `E = (25,16)`, and `M = (16,16)`. Its reflected beginning is `n₂(B) = 10`, with `μ(10) = +1`:

$$
c'\equiv1+27+25+16=69\equiv1\pmod 2,
$$

$$
r'\equiv1+18+25+16+1=61\equiv1\pmod 2.
$$

The prediction is **odd row, odd column**:

| Original node | Center | Parity (row, column) | Result |
| :--- | :--- | :--- | :--- |
| L–C–EA | C(25,7) | (1,1) | Pass |
| L–I–EA | I(20,15) | (0,1) | Fails row condition |
| L–EO–EA | EO(25,14) | (1,0) | Fails column condition |

Each filter alone leaves two possibilities. Together, they select **`C(25,7)` among these three centers**. That center was already part of the fitting sequence, so this is a consistency check within the recorded route.

## 5. Prediction after THEN

THEN runs from **`L(25,25)`** to **`W(25,27)`**. Its original **`IA–IA–IA`** node is centered on **`IA(26,22)`**.

For the column:

$$
c'\equiv1+25+25+26=77\equiv1\pmod 2.
$$

The beginning has `n₀(B) = 673`, so `n₂(B) = 57 = 3 × 19` and `μ(57) = +1`. For the row:

$$
r'\equiv1+25+25+26+1=78\equiv0\pmod 2.
$$

**Prediction: even row, odd column — `(0,1)`.**

### How much remains?

The full grid has **13 even rows × 14 odd columns = 182 eligible cells out of 729**.

[Report 01](01-next-key-signature.md) also predicts signature **`(+1,+1,+1)`**, phase **0**. The snapshot’s enumeration considers mirrored nodes on horizontal, vertical, and both diagonal axes, at every valid radius. Each center rune’s index is transformed through `φ` before checking the derived-key signature.

| Restriction | Spatial nodes | Distinct centers | Distinct numerical keys |
| :--- | ---: | ---: | ---: |
| Signature only | 44 | 36 | 26 |
| Signature + even row | 21 | 16 | 16 |
| Signature + odd column | 25 | 18 | 18 |
| Signature + both parities | 16 | 12 | 12 |

The middle two rows apply each parity filter separately. Their intersection reduces **44 nodes to 16**, removing about **64%**, and **36 centers to 12**.

A spatial node is identified by its three cell positions; nodes may share a center or numerical key. These counts cover mirrored nodes with center-totient derivation, excluding other key constructions.

### Candidate N–M–N

The candidate THE uses the vertical mirror:

**`N(17,17) – M(20,17) – N(23,17)`**

Its center **`M(20,17)`** has the predicted even row and odd column. The mirror radius is **3**.

Since `φ(M = 19) = 18 = E`, the derived key is **`N–E–N`**, with indices `(9,18,9)`. Their totients are `(6,6,6)`, giving signature **`(+1,+1,+1)`** and phase **0**.

The selected ciphertext decrypts as follows:

| Ciphertext cell | Key index | Plaintext modulo 29 |
| :--- | :--- | :--- |
| J(22,21), index 11 | N = 9 | 11 − 9 = 2 → TH |
| W(21,20), index 7 | E = 18 | 7 − 18 ≡ 18 → E |

**`TH–E` → THE**

This center is one of the **12 remaining centers**. Including THEN → THE gives conditional **17/17** for both parity rules, without uniquely selecting this center or plaintext.

## 6. Checks through THE KEY IS TO GO

Each row calculates both bits from the current block before comparison with the selected next center.

| Transition | Current B | Current E | Current M | Selected next center | Predicted (row, column) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| THEN → THE | (25,25) | (25,27) | (26,22) | (20,17) | (0,1) |
| THE → KEY | (22,21) | (21,20) | (20,17) | (12,16) | (0,0) |
| KEY → IS | (21,4) | (19,4) | (12,16) | (17,9) | (1,1) |
| IS → TO | (18,7) | (19,6) | (17,9) | (8,25) | (0,1) |
| TO → GO | (9,16) | (8,17) | (8,25) | (12,14) | (0,0) |

All five selected centers match both bits. For THE → KEY, `n₂(B) = 142` and `μ(142) = +1`; both coordinate sums are **64**, predicting even row and even column, as at **`H(12,16)`**.

These candidate checks are separate from the 16-transition fitting set. The candidates were found using the constraints, so their agreement is not independent validation. The formulas filter **original key-node centers**; they do not locate a unique center, select the ciphertext, or establish a complete traversal rule. Further independently supported transitions are needed to test the pair.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

Snapshot: `d5eed3f10428372c7202ceebc65cc3bdead0819d`.
