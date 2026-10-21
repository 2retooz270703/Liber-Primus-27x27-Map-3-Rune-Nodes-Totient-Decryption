# Predicting the Next Key's Center Parity

**A Coordinate Parity Prediction Report**

*27 × 27 matrix · Next-key centers · Row and column parity · Rotational Möbius correction*

---

A completed ciphertext block can provide another constraint on the **next decryption key**: whether the center of its original three-rune node lies in an **even or odd row and column**. Two compact formulas use the current ciphertext's beginning and endpoint, together with the center of its current key node, to predict these two properties.

The **column rule** uses only three row numbers and an additive constant. The **row rule** shares the same basic structure, but uses the beginning's column and adds the Möbius value of its absolute cell number after a **180° rotation**. On the selected LP2 pages 0–2 route, both rules match **all 16 recorded transitions**. They also agree with the explored **THEN → THE** continuation, giving a conditional **17/17** on that extended route.

This report adds a **location filter** to the earlier reports. [Report 01](01-next-key-signature.md) predicts the next key's numerical signature; [Report 02](02-leftmost-cell-and-rotations.md) examines leftmost-cell geometry; and [Report 03](03-predicting-axis-and-reading-direction.md) predicts the next ciphertext's axis and reading orientation. The present formulas constrain the **next key-node center**, rather than the next ciphertext's cells.

**Contents**

[01. Foundations](#foundations) · [02. Predicting the column parity](#predicting-the-column-parity) · [03. Predicting the row parity](#predicting-the-row-parity) · [04. The shared structure](#the-shared-structure) · [05. Verification across the route](#verification-across-the-route) · [06. After THEN](#after-then) · [07. Reading the result](#reading-the-result) · [Formula reference](#formula-reference)

---

## Foundations

### Three inputs from the current block

Coordinates are **one-based**: `(1,1)` is the upper-left cell of the 27 × 27 matrix. Rows increase downward, and columns increase to the right.

For the **current** ciphertext and its key node, define:

- **`B` — beginning:** the first cell in the ciphertext's actual reading order.
- **`E` — endpoint:** the last cell in that reading order.
- **`M` — original key-node center:** the coordinate of the central cell in the three-rune structure supplying the current key, before any center-totient transformation.

For any cell `X`, write its row and column as $r(X)$ and $c(X)$. These are ordinary **coordinate numbers from 1 to 27**, not the index or prime value of the rune occupying the cell.

Let the **next** original key-node center be:

$$
M'=(r',c').
$$

The prime mark identifies the **next center**. The formulas predict only the residues $r'\bmod 2$ and $c'\bmod 2$, not the complete coordinates.

### Interpreting the two outputs

Apply the same interpretation to either coordinate:

| Result modulo 2 | Row prediction | Column prediction |
|---:|---|---|
| **0** | The next center lies in an **even row**. | The next center lies in an **even column**. |
| **1** | The next center lies in an **odd row**. | The next center lies in an **odd column**. |

For example, the pair **`(0,1)`** means **even row, odd column**. It does not mean the coordinate `(0,1)`: the matrix coordinates still range from 1 to 27.

### The reflected absolute cell number

The original absolute position of a cell is:

$$
n_0(r,c)=27(r-1)+c.
$$

A **180° rotation** about the matrix center sends:

$$
(r,c)\longmapsto(28-r,28-c).
$$

The absolute position after that rotation is:

$$
\boxed{n_2(r,c)=730-n_0(r,c)}.
$$

Here **730 = 27² + 1**. The rotation changes the cell's position for the numerical calculation; it does not change which original cell is designated `B`.

The row formula applies the ordinary **Möbius function** to $n_2(B)$. Its values are $-1$, $0$, and $+1$: zero means the integer contains a squared prime factor, while a nonzero value means it is square-free.

---

## Predicting the Column Parity

### Three row numbers and one constant

Add the current ciphertext's beginning row, endpoint row, and current key-node center row, then add 1 and reduce modulo 2:

$$
\boxed{c'\equiv1+r(B)+r(E)+r(M)\pmod 2}.
$$

**Interpretation:** `0 = EVEN COLUMN`; `1 = ODD COLUMN`.

No rune values, absolute cell numbers, totients, or Möbius values enter this calculation. Its inputs are simply the **three original row coordinates**.

### Example — WEATHER → TURNS

The current block **WEATHER** has:

- **Beginning:** `NG(14,14)`.
- **Endpoint:** `E(14,18)`.
- **Original key-node center:** `OE(14,5)`.

All three row numbers are 14, so:

$$
c'\equiv1+14+14+14=43\equiv1\pmod 2.
$$

The next key center should therefore occupy an **odd column**. The recorded TURNS node is centered on **`NG(14,23)`**: column **23** satisfies the prediction.

### A geometric reading of the same expression

Modulo 2, addition and subtraction have the same effect. The column rule can therefore also be written as:

$$
c'\equiv1+r(M)+\bigl[r(E)-r(B)\bigr]\pmod 2.
$$

The ciphertext contributes the **parity of its vertical displacement** from beginning to endpoint. This is an equivalent expression of the same rule, not another independent observation.

---

## Predicting the Row Parity

### The beginning's column and a reflected Möbius correction

For the row prediction, use the beginning's **column**, the endpoint's row, the current key-node center's row, and the Möbius value of the beginning's reflected absolute position:

$$
\boxed{r'\equiv1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\pmod 2}.
$$

**Interpretation:** `0 = EVEN ROW`; `1 = ODD ROW`.

The first three variable inputs are coordinate numbers from **1 to 27**. Only the last term uses an **absolute position from 1 to 729**, obtained after the 180° rotation and then passed through $\mu$.

### What the Möbius correction does

Because the result is taken modulo 2:

- **`μ = 0`:** leave the parity of the other terms unchanged.
- **`μ = +1` or `μ = −1`:** toggle that parity.

In this calculation, **both nonzero signs have the same effect**: $-1\equiv+1\pmod 2$. The Möbius term therefore tests square-freeness; its sign is not being interpreted as a movement direction.

### Example — COLD → I MAY

The current COLD block has:

$$
B=(14,7),\qquad E=(11,7),\qquad M=(26,19).
$$

The beginning's original and reflected absolute positions are:

$$
n_0(B)=27(14-1)+7=358,
$$

$$
n_2(B)=730-358=372.
$$

Since $372=2^2\times3\times31$, its Möbius value is **0**. Substituting into the row rule gives:

$$
r'\equiv1+7+11+26+0=45\equiv1\pmod 2.
$$

The next center should lie in an **odd row**. The column rule gives:

$$
c'\equiv1+14+11+26=52\equiv0\pmod 2.
$$

Together, the rules predict **odd row, even column**. The recorded I MAY key node is centered on **`B(15,8)`**, matching both outputs.

---

## The Shared Structure

### One common term

Both formulas contain the same contribution from the endpoint and the current node center. Define:

$$
T=1+r(E)+r(M).
$$

Then the pair becomes:

$$
\boxed{c'\equiv T+r(B)\pmod 2},
$$

$$
\boxed{r'\equiv T+c(B)+\mu\bigl(n_2(B)\bigr)\pmod 2}.
$$

The **column prediction** adds the beginning's row to the common term. The **row prediction** adds its column and the reflected Möbius correction. This is a direct algebraic connection between the two expressions.

### A consequence for the next center's checkerboard class

Adding the two congruences cancels their common contribution:

$$
\boxed{r'+c'\equiv r(B)+c(B)+\mu\bigl(n_2(B)\bigr)\pmod 2}.
$$

Thus the **parity of the next center's coordinate sum** can be expressed using only the current beginning. This determines its checkerboard class, but is already implied by the two coordinate predictions; it adds no independent constraint.

The shared form is consistent with the possibility that both rules describe consequences of a common underlying process. It does not, by itself, establish that the expressions were used by the authors or derive them from a known symmetry.

---

## Verification Across the Route

### The fixed sequence and its inputs

The following table checks the **16 recorded transitions**, from **AS I GO THE → WEATHER** through **SOON → THEN**. The columns `B`, `E`, and `M` are inputs from the current block; the next center is the recorded comparison target. The last column gives the calculated **`(row parity, column parity)`**. Every pair matches the displayed next center.

As in the preceding reports, **OF and THE are separate blocks**, and **SOON uses the primary ciphertext**. Its original key node is **`L–C–EA`, centered on `C(25,7)`**. This node choice is part of the verification input: another node producing the same derived key can have different center coordinates.

| No. | Transition | Current B | Current E | Current M | Next center | Predicted (row, column) |
|---:|---|---|---|---|---|---|
| 1 | **AS I GO THE → WEATHER** | `(13,25)` | `(14,4)` | `(13,12)` | `(14,5)` | `(0,1)` |
| 2 | **WEATHER → TURNS** | `(14,14)` | `(14,18)` | `(14,5)` | `(14,23)` | `(0,1)` |
| 3 | **TURNS → COLD** | `(14,19)` | `(10,19)` | `(14,23)` | `(26,19)` | `(0,1)` |
| 4 | **COLD → I MAY** | `(14,7)` | `(11,7)` | `(26,19)` | `(15,8)` | `(1,0)` |
| 5 | **I MAY → CRY** | `(26,19)` | `(26,16)` | `(15,8)` | `(25,16)` | `(1,0)` |
| 6 | **CRY → NOW THE** | `(19,16)` | `(17,16)` | `(25,16)` | `(19,16)` | `(1,0)` |
| 7 | **NOW THE → IDEA** | `(11,16)` | `(15,20)` | `(19,16)` | `(11,16)` | `(1,0)` |
| 8 | **IDEA → OF** | `(15,20)` | `(17,18)` | `(11,16)` | `(17,18)` | `(1,0)` |
| 9 | **OF → THE** | `(18,15)` | `(18,16)` | `(17,18)` | `(19,16)` | `(1,0)` |
| 10 | **THE → END** | `(19,17)` | `(19,16)` | `(19,16)` | `(23,12)` | `(1,0)` |
| 11 | **END → IS** | `(19,23)` | `(21,23)` | `(23,12)` | `(21,22)` | `(1,0)` |
| 12 | **IS → DEATH** | `(21,9)` | `(21,10)` | `(21,22)` | `(23,12)` | `(1,0)` |
| 13 | **DEATH → SEE** | `(26,3)` | `(26,1)` | `(23,12)` | `(25,6)` | `(1,0)` |
| 14 | **SEE → YOU** | `(25,16)` | `(27,14)` | `(25,6)` | `(16,16)` | `(0,0)` |
| 15 | **YOU → SOON** | `(27,18)` | `(25,16)` | `(16,16)` | `(25,7)` | `(1,1)` |
| 16 | **SOON → THEN** | `(25,16)` | `(25,19)` | `(25,7)` | `(26,22)` | `(0,0)` |

Each formula gives **16/16 matches**, and the pair gives **16/16 joint parity matches** on this fixed route. These are two restrictions on the same next centers, so their match counts should not be treated as independent experiments.

The rules were identified by searching this recorded sequence. The table establishes the fit and makes the calculations reproducible; it does not constitute a test on previously unseen transitions.

### Selecting the SOON key center

The **YOU → SOON** transition illustrates how the two parity rules can distinguish between different centers that produce the **same numerical key**. Three documented nodes yield `L–R–EA`: **`L–C–EA` at `(25,7)`**, **`L–I–EA` at `(20,15)`**, and **`L–EO–EA` at `(25,14)`**. Their middle runes all transform to `R`, because:

$$
\varphi(5)=\varphi(10)=\varphi(12)=4=\mathrm{R}.
$$

The numerical key alone therefore does not distinguish these three possible centers. The parity rules supply an additional criterion using only the preceding **YOU** block:

$$
B=(27,18),\qquad E=(25,16),\qquad M=(16,16).
$$

The column prediction is:

$$
c'\equiv1+27+25+16=69\equiv1\pmod 2.
$$

For the row prediction, $n_0(B)=720$, so $n_2(B)=730-720=10$ and $\mu(10)=+1$. Hence:

$$
r'\equiv1+18+25+16+1=61\equiv1\pmod 2.
$$

The next key center must therefore lie in an **odd row and an odd column**:

| Original node | Center | Row parity | Column parity | Both filters |
|---|---|---|---|---|
| **L–C–EA** | **C(25,7)** | **Odd** | **Odd** | **Pass** |
| L–I–EA | I(20,15) | Even | Odd | Fails the row condition |
| L–EO–EA | EO(25,14) | Odd | Even | Fails the column condition |

**Each rule alone leaves two possibilities; together, they single out exactly `C(25,7)` among the three documented centers.** This gives a precise parity-based criterion for the recorded choice of the `L–C–EA` node, while the derived numerical key remains `L–R–EA` in all three cases. Because that center was already included when the formulas were fitted, this is a consistency check within the recorded route, not an additional independent validation.

---

## After THEN

### Calculate the two predicted parities

The THEN ciphertext runs from **`L(25,25)`** to **`W(25,27)`**. Its original `IA–IA–IA` key node has center **`IA(26,22)`**. Therefore:

$$
B=(25,25),\qquad E=(25,27),\qquad M=(26,22).
$$

For the **column**:

$$
c'\equiv1+25+25+26=77\equiv1\pmod 2.
$$

For the **row**, first reflect the beginning:

$$
n_0(B)=27(25-1)+25=673,
$$

$$
n_2(B)=730-673=57.
$$

Since $57=3\times19$, $\mu(57)=+1$. Consequently:

$$
r'\equiv1+25+25+26+1=78\equiv0\pmod 2.
$$

The prediction is:

$$
\boxed{\text{NEXT KEY CENTER: EVEN ROW, ODD COLUMN}.}
$$

### How much of the candidate space remains?

Across the full matrix, this pair of parities permits **13 even rows × 14 odd columns = 182 cells out of 729**, approximately one quarter of the grid.

Report 01 also predicts the next key's signature **`(+1,+1,+1)`**, with phase **0**. To measure the additional parity filter, enumerate mirrored three-rune nodes along the **horizontal, vertical, and both diagonal axes**, at every radius for which both outer cells lie inside the matrix. Transform the center rune through $\varphi$ to obtain the key, then retain nodes whose derived-key signature is `(+1,+1,+1)`.

This gives **44 spatial nodes at 36 distinct centers**, representing **26 distinct numerical keys** before the parity filter:

| Restriction | Spatial nodes | Distinct centers | Distinct numerical keys |
|---|---:|---:|---:|
| Signature `(+1,+1,+1)` only | 44 | 36 | 26 |
| Signature + even row | 21 | 16 | 16 |
| Signature + odd column | 25 | 18 | 18 |
| **Signature + both parity filters** | **16** | **12** | **12** |

The even-row and odd-column rows show each filter applied separately to the signature-qualified set. Their intersection is the final row.

**Both filters reduce the 44 eligible mirror nodes to 16**, removing approximately **64%**. Distinct centers decrease from **36 to 12**. A spatial node is counted by its three cell positions; different nodes can share a center or yield the same numerical key. These counts concern **mirrored nodes with the center-totient transformation**, not every possible non-mirrored key construction.

### The E–O–E candidate

The explored next key node is:

$$
\mathrm{E}(26,16)\;–\;\mathrm{O}(26,21)\;–\;\mathrm{E}(26,26).
$$

Its center **`(26,21)`** lies in an **even row and an odd column**, so it survives both filters. It is immediately **one cell left of the current THEN key center `(26,22)`**, and is the nearest remaining center to that current center by ordinary Euclidean distance.

The original center rune `O` has index **3**. Transforming it gives $\varphi(3)=2=\mathrm{TH}$, so the derived key is:

$$
\mathrm{E-O-E}\longmapsto\mathrm{E-TH-E}.
$$

Its indices are $(18,2,18)$. The signature is:

$$
\bigl(\mu(\varphi(18)),\mu(\varphi(2)),\mu(\varphi(18))\bigr)
=\bigl(\mu(6),\mu(1),\mu(6)\bigr)
=(+1,+1,+1).
$$

Its phase is **0**, so the key begins with `E–TH`. The proposed ciphertext **`L(24,27) → L(23,26)`** then gives:

| Cell | Ciphertext index | Key index | Subtraction modulo 29 | Plaintext |
|---|---:|---:|---|---|
| `(24,27)` | `L = 20` | `E = 18` | `20 − 18 = 2` | **TH** |
| `(23,26)` | `L = 20` | `TH = 2` | `20 − 2 = 18` | **E** |

This is the explored **THE** continuation. By comparison, the `D–U–D` node centered on **`(25,12)`** has an odd row and an even column, so it fails both parity conditions.

### The conditional seventeenth match

For **THEN → THE**, both formulas predict **`(0,1)`**. The candidate center `(26,21)` has exactly those parities. Including this continuation therefore gives **17/17 matches for each formula on the extended route**.

THE was already an explored candidate. This is **agreement with that candidate**, rather than independent confirmation that it is the intended next plaintext. Its surviving center is one of the **12 remaining centers**; the parity equations themselves do not instruct the reader to choose the nearest one.

---

## Reading the Result

### What the pair contributes

These formulas constrain **where the next original key node may be centered** using inputs available from the current block. They do not require a candidate word as a numerical input. After THEN, their practical contribution is the **44 → 16** reduction within the signature-qualified mirror-node set.

The predictions concern the **key-node center**, not the next ciphertext's beginning, endpoint, or leftmost cell. A candidate still needs a suitable key, ciphertext, reading geometry, and decryption result under the rules described in the earlier reports.

### What remains to be tested

The recorded fit does not establish a unique formula or a complete traversal algorithm. The source-node choices are part of the input, and other expressions can fit the same historical sequence while extrapolating differently. Future transitions with independent support are needed to test whether this particular pair continues to hold.

If the explored THE is used as the current block, its inputs are:

$$
B=(24,27),\qquad E=(23,26),\qquad M=(26,21).
$$

Here $n_2(B)=82$ and $\mu(82)=+1$. The same pair then predicts:

$$
c'\equiv1+24+23+26=74\equiv0\pmod 2,
$$

$$
r'\equiv1+27+23+26+1=78\equiv0\pmod 2.
$$

**After the candidate THE, this pair predicts an EVEN ROW and an EVEN COLUMN for the following key center.** This forecast belongs specifically to the two formulas documented here and remains unverified against a subsequent independently supported key.

---

## Formula Reference

All coordinates are **one-based**. `B` and `E` are the beginning and endpoint of the **current** ciphertext. `M` is the center coordinate of its **current original key node**. The next original center is $M'=(r',c')$.

**1 · Original absolute cell position**

$$
n_0(r,c)=27(r-1)+c
$$

**2 · Absolute position after a 180° rotation**

$$
n_2(r,c)=730-n_0(r,c)
$$

**3 · Predict the next center's column parity**

$$
\boxed{c'\equiv1+r(B)+r(E)+r(M)\pmod 2}
$$

**4 · Predict the next center's row parity**

$$
\boxed{r'\equiv1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\pmod 2}
$$

**Interpretation for either coordinate:** `0 = EVEN`; `1 = ODD`.

**5 · Shared term and derived checkerboard relation**

$$
T=1+r(E)+r(M)
$$

$$
c'\equiv T+r(B)\pmod 2,\qquad
r'\equiv T+c(B)+\mu\bigl(n_2(B)\bigr)\pmod 2
$$

$$
r'+c'\equiv r(B)+c(B)+\mu\bigl(n_2(B)\bigr)\pmod 2
$$

The last relation follows algebraically from the two parity rules; it is not an additional independent test.

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). Calculations use the supplied snapshot at commit `d5eed3f10428372c7202ceebc65cc3bdead0819d`, the selected 17-block route with `OF` and `THE` separate, the primary SOON ciphertext and its `L–C–EA` original node, and the additional explored THEN → THE continuation. The 16/16 historical fits and conditional 17/17 extended fits describe that selected route; they do not independently establish an intended or unique Cicada 3301 decryption.
