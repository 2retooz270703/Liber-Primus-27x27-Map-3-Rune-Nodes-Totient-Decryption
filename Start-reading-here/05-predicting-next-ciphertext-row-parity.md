# Predicting the Next Ciphertext's Row Parity

**A Phase and Coordinate Parity Prediction Report**

*27 × 27 matrix · Ciphertext endpoints · Leftmost cells · Current phase · 180° Möbius correction*

---

The earlier reports predict the next key's signature, the next ciphertext's reading geometry, and the parity of the next original key-node center. A closely related pair of formulas adds another constraint: **whether the next ciphertext's endpoint and leftmost cell lie in even or odd rows**.

Both formulas share the term **1 + p**, where p is the **current key's phase**, and use the same current original node center **M**. The endpoint rule applies the Möbius function to M's absolute cell number after a **180° rotation**. The leftmost-cell rule applies it to M's ordinary row number and reuses the next-center row-parity prediction from [Report 04](04-predicting-next-key-center-parity.md).

Each formula matches **all 16 recorded transitions** on the selected LP2 pages 0–2 route. Both also agree with the **THEN → THE** realization used in the candidate continuation **THE KEY IS TO GO**, giving a conditional **17/17** on that extended route. These are empirical fits, rather than a derivation of the intended traversal.

**Contents**

[01. Foundations](#foundations) · [02. Predicting the endpoint row](#predicting-the-endpoint-row) · [03. Predicting the leftmost-cell row](#predicting-the-leftmost-cell-row) · [04. The shared structure](#the-shared-structure) · [05. Verification across the route](#verification-across-the-route) · [06. After THEN](#after-then) · [07. Reading the result](#reading-the-result) · [Formula reference](#formula-reference)

---

## Foundations

### Current inputs and next-block targets

Coordinates are **one-based**: `(1,1)` is the upper-left cell. Rows increase downward and columns increase to the right.

| Symbol | Meaning |
|---|---|
| **B** | Beginning of the **current** ciphertext: its first cell in reading order. |
| **E** | Endpoint of the **current** ciphertext: its last cell in reading order. |
| **M** | Center of the **current original key node**, before any center-totient transformation. |
| **p** | Phase of the **current derived key**, expressed as 0, 1, or 2. |
| **E′** | Endpoint of the **next** ciphertext. |
| **L′** | Leftmost cell of the **next** ciphertext. |
| **M′** | Center of the **next original key node**. |
| **r(X), c(X)** | Ordinary row and column numbers of cell X, from 1 to 27. |
| **μ** | The ordinary Möbius function, with values −1, 0, and +1. |
| **φ** | Euler's totient function, used in the existing key-phase definition. |

The **leftmost cell** is selected geometrically: take the smallest occupied column; if several cells share it, take the **bottommost** one. It can be the beginning or endpoint of a straight ciphertext, depending on its reading direction.

The prime mark means **next block**. The two outputs are row-parity bits, not full row numbers:

| Result modulo 2 | Interpretation |
|---:|---|
| **0** | The target cell lies in an **even row**. |
| **1** | The target cell lies in an **odd row**. |

### The current phase

For the current derived key `K = (k₁,k₂,k₃)`, in its unaligned order, [Report 00](00-decryption-method.md) defines:

$$
\sigma_i=\mu\bigl(\varphi(k_i)\bigr),\qquad
p=(\sigma_1+\sigma_2+\sigma_3)\bmod3.
$$

Calculate p modulo **3 first**, retaining its representative **0, 1, or 2**. Then use that number in the formulas below and reduce their final results modulo **2**. This is the current key's phase, not the predicted phase of the next key or the cumulative phase total S.

### The 180° cell number

The absolute number of a cell in the original matrix is:

$$
n_0(r,c)=27(r-1)+c.
$$

A 180° rotation sends `(r,c)` to `(28−r,28−c)`. Its absolute number becomes:

$$
\boxed{n_2(r,c)=730-n_0(r,c)}.
$$

Thus **μ(n₂(M))** uses an absolute position from **1 to 729**, while **μ(r(M))** uses an ordinary row number from **1 to 27**. Neither input is the rune index occupying M.

Modulo 2, both nonzero Möbius signs have the same effect: **μ = +1 and μ = −1 toggle parity; μ = 0 leaves it unchanged**. These binary formulas use square-freeness, not the distinction between the two nonzero signs.

---

## Predicting the Endpoint Row

### Current phase and the reflected center

Add 1, the current phase, and the Möbius value of the current center's 180° cell number:

$$
\boxed{r(E')\equiv1+p+\mu\bigl(n_2(M)\bigr)\pmod2}.
$$

**Interpretation:** `0 = EVEN ROW`; `1 = ODD ROW`.

This first prediction needs only the **current phase p** and **current center M**. It does not require a proposed next word, a selected next key, or the next endpoint's coordinates.

### Example — TURNS → COLD

For the current TURNS block, `p = 0` and `M = (14,23)`. Therefore:

$$
n_0(M)=27(14-1)+23=374,
$$

$$
n_2(M)=730-374=356=2^2\times89.
$$

Since μ(356) = 0:

$$
r(E')\equiv1+0+0=1\pmod2.
$$

The next endpoint should lie in an **odd row**. The recorded COLD endpoint is **`(11,7)`**, which satisfies the prediction.

---

## Predicting the Leftmost-Cell Row

### Reuse the earlier center prediction

Write the next-center row-parity prediction from Report 04 as:

$$
\boxed{
\widehat r(M')=
\bigl[1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\bigr]\bmod2
}.
$$

The hat identifies a **calculated parity bit**, either 0 or 1. It is not the full future row coordinate and is not a value taken from an already selected next node.

The new leftmost-cell formula is:

$$
\boxed{
r(L')\equiv\widehat r(M')+1+p+\mu\bigl(r(M)\bigr)\pmod2
}.
$$

**Interpretation:** `0 = EVEN ROW`; `1 = ODD ROW`.

Only **current-block information** is needed. The next-center bit is computed from B, E, and M using the earlier rule.

### An expression containing only current inputs

Substituting the earlier prediction makes the dependency explicit. The two additive constants 1 cancel modulo 2:

$$
\boxed{
r(L')\equiv c(B)+r(E)+r(M)+p+
\mu\bigl(n_2(B)\bigr)+\mu\bigl(r(M)\bigr)\pmod2
}.
$$

This is the same rule in expanded form, not an additional independently discovered formula.

### Example — the leftmost cell differs from the endpoint

For **TURNS → COLD**, the earlier center rule gives **`r̂(M′) = 0`**. Since the current phase is 0 and μ(r(M)) = μ(14) = +1:

$$
r(L')\equiv0+1+0+1=2\equiv0\pmod2.
$$

COLD's leftmost cell is **`(14,7)`**, in an **even row**. Its endpoint is **`(11,7)`**, in an **odd row**, as the first formula predicts. The two targets can therefore differ even within one ciphertext.

---

## The Shared Structure

### One phase term, two views of M

Define:

$$
U=(1+p)\bmod2.
$$

Then the pair becomes:

$$
r(E')\equiv U+\mu\bigl(n_2(M)\bigr)\pmod2,
$$

$$
r(L')\equiv\widehat r(M')+U+\mu\bigl(r(M)\bigr)\pmod2.
$$

The first uses M's **full reflected cell number**. The second uses the **ordinary row number of the same M**, relative to the predicted next-center parity. This common structure is the main connection between the two expressions.

Adding the predictions cancels the shared phase term:

$$
\boxed{
r(E')+r(L')+\widehat r(M')
\equiv\mu\bigl(n_2(M)\bigr)+\mu\bigl(r(M)\bigr)\pmod2
}.
$$

This relation follows algebraically from the pair. It supplies no additional independent filter.

### Connections to the earlier reports

- **Report 00** supplies the current derived key and phase p.
- **Report 02** defines the leftmost cell and predicts whether L′ is the next beginning or endpoint.
- **Report 03** constrains the next ciphertext's axis and reading direction.
- **Report 04** supplies the predicted row parity of the next original key-node center.

The 180° operation also appears in the earlier center-row rule as **μ(n₂(B))**. The new endpoint rule uses **μ(n₂(M))** instead: the same numerical transformation applied to a different current anchor.

The exact identity `n₂ = 730 − n₀` expresses central symmetry of the grid. Its recurrence is a structural feature of these fitted expressions; it does not establish that central symmetry was the authors' traversal mechanism.

---

## Verification Across the Route

The table checks the two new predictions against the recorded next endpoint and leftmost cell. **Rows 1–16 are the historical fitting set. Row 17 uses the N–M–N source node for THE in the candidate continuation THE KEY IS TO GO.**

OF and the earlier THE remain separate blocks. SOON uses the primary ciphertext and the original **L–C–EA node centered on C(25,7)**, as in Report 04. Changing original nodes can change the current M and subsequent predictions.

The final column gives **(endpoint row parity, leftmost-cell row parity)**. Each pair agrees with the displayed next coordinates. The next-center bit is calculated by the earlier formula before evaluating the leftmost-cell rule.

| No. | Transition | Current p | Current M | Predicted next-center row bit | Next E′ | Next L′ | Predicted (E′ row, L′ row) |
|---:|---|---:|---|---:|---|---|---|
| 1 | **AS I GO THE → WEATHER** | 0 | `(13,12)` | 0 | `(14,18)` | `(14,14)` | `(0,0)` |
| 2 | **WEATHER → TURNS** | 2 | `(14,5)` | 0 | `(10,19)` | `(14,19)` | `(0,0)` |
| 3 | **TURNS → COLD** | 0 | `(14,23)` | 0 | `(11,7)` | `(14,7)` | `(1,0)` |
| 4 | **COLD → I MAY** | 1 | `(26,19)` | 1 | `(26,16)` | `(26,16)` | `(0,0)` |
| 5 | **I MAY → CRY** | 0 | `(15,8)` | 1 | `(17,16)` | `(19,16)` | `(1,1)` |
| 6 | **CRY → NOW THE** | 1 | `(25,16)` | 1 | `(15,20)` | `(11,16)` | `(1,1)` |
| 7 | **NOW THE → IDEA** | 2 | `(19,16)` | 1 | `(17,18)` | `(17,18)` | `(1,1)` |
| 8 | **IDEA → OF** | 1 | `(11,16)` | 1 | `(18,16)` | `(18,15)` | `(0,0)` |
| 9 | **OF → THE (earlier)** | 0 | `(17,18)` | 1 | `(19,16)` | `(19,16)` | `(1,1)` |
| 10 | **THE (earlier) → END** | 2 | `(19,16)` | 1 | `(21,23)` | `(21,23)` | `(1,1)` |
| 11 | **END → IS** | 2 | `(23,12)` | 1 | `(21,10)` | `(21,9)` | `(1,1)` |
| 12 | **IS → DEATH** | 1 | `(21,22)` | 1 | `(26,1)` | `(26,1)` | `(0,0)` |
| 13 | **DEATH → SEE** | 2 | `(23,12)` | 1 | `(27,14)` | `(27,14)` | `(1,1)` |
| 14 | **SEE → YOU** | 0 | `(25,6)` | 0 | `(25,16)` | `(25,16)` | `(1,1)` |
| 15 | **YOU → SOON** | 1 | `(16,16)` | 1 | `(25,19)` | `(25,16)` | `(1,1)` |
| 16 | **SOON → THEN** | 2 | `(25,7)` | 0 | `(25,27)` | `(25,25)` | `(1,1)` |
| 17 | **THEN → THE (N–M–N candidate)** | 1 | `(26,22)` | 0 | `(21,20)` | `(21,20)` | `(1,1)` |

Each rule gives **16/16 historical matches**, and both agree with the candidate THE, giving conditional **17/17** on the extended route. The pair's matches are correlated and should not be counted as independent experiments. The candidate continuation was selected using the same constraints, so this agreement is not a blind seventeenth test.

---

## After THEN

### Calculate the predicted rows

The current THEN block has:

$$
B=(25,25),\qquad E=(25,27),\qquad M=(26,22),\qquad p=1.
$$

For the earlier center-row prediction:

$$
n_2(B)=730-673=57,\qquad\mu(57)=+1,
$$

$$
\widehat r(M')=[1+25+25+26+1]\bmod2=0.
$$

For the new endpoint prediction:

$$
n_0(M)=697,\qquad n_2(M)=33,\qquad\mu(33)=+1,
$$

$$
r(E')\equiv1+1+1=3\equiv1\pmod2.
$$

For the new leftmost-cell prediction, μ(r(M)) = μ(26) = +1:

$$
r(L')\equiv0+1+1+1=3\equiv1\pmod2.
$$

The pair therefore predicts:

$$
\boxed{\text{NEXT ENDPOINT AND LEFTMOST CELL: ODD ROW}.}
$$

Report 02 also predicts **END** after THEN, meaning **L′ = E′**. On this transition, the two formulas constrain the **same physical cell** and supply one shared odd-row filter, rather than two independent reductions. Neither formula in this report predicts a column.

### The THE realization in the candidate continuation

The selected THE ciphertext is **J(22,21) → W(21,20)**, with the original **N–M–N** key node centered on **M(20,17)**. Transforming the center gives φ(M = 19) = 18 = E, producing the derived key **N–E–N** with phase 0.

Its endpoint and leftmost cell are both **W(21,20)**. Row **21** is odd, matching both predictions above. This is the THE realization used in **THE KEY IS TO GO**.

---

## Reading the Result

### What the pair contributes

The formulas connect the current phase and two numerical views of the current node center to the **rows of the next ciphertext's boundaries**. The second extends the previous key-center prediction into a constraint on ciphertext location.

The result is a useful additional filter on the selected route. It does not specify exact coordinates, choose a numerical key, determine a word, or by itself locate the whole next ciphertext.

### What remains to be tested

These expressions were found by searching the recorded transitions. Their shared structure is interesting, but a perfect historical fit does not prove an intended Cicada mechanism. Other short expressions can fit the same labels and produce different future forecasts. The current node choices and the older formula reused by the second rule are also part of the model.

The useful next test is to retain these expressions unchanged and compare their forecasts with a further transition supported independently of them.

### A fixed forecast after the candidate THE

For the N–M–N realization of THE used above:

$$
B=(22,21),\qquad E=(21,20),\qquad M=(20,17),\qquad p=0.
$$

The beginning has n₂(B) = 142 and μ(142) = +1. Report 04 therefore predicts the next center's row bit as:

$$
\widehat r(M')=[1+21+21+20+1]\bmod2=0.
$$

Here **n₀(M) = 530**, **n₂(M) = 200**, **μ(200) = 0**, and **μ(20) = 0**. Thus:

$$
r(E')\equiv1+0+0=1\pmod2,
$$

$$
r(L')\equiv0+1+0+0=1\pmod2.
$$

**After this THE, the pair predicts ODD ROWS for both the following endpoint and leftmost cell.** The candidate KEY has endpoint **EA(19,4)** and leftmost cell **N(21,4)**, matching both predictions. This is a conditional consistency check within the candidate continuation, not an independent validation.

---

## Formula Reference

All coordinates are **one-based**. B, E, M, and p belong to the **current** block. Prime marks identify the **next** block. Every output below is a parity bit: **0 = EVEN ROW; 1 = ODD ROW**.

**1 · Absolute cell numbers**

$$
n_0(r,c)=27(r-1)+c,\qquad n_2(r,c)=730-n_0(r,c)
$$

**2 · Current derived-key phase**

$$
p=\left[\sum_{i=1}^{3}\mu\bigl(\varphi(k_i)\bigr)\right]\bmod3
$$

**3 · Earlier next-center row-parity prediction — Report 04**

$$
\widehat r(M')=
\bigl[1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\bigr]\bmod2
$$

**4 · New endpoint row-parity rule**

$$
\boxed{r(E')\equiv1+p+\mu\bigl(n_2(M)\bigr)\pmod2}
$$

**5 · New leftmost-cell row-parity rule**

$$
\boxed{r(L')\equiv\widehat r(M')+1+p+\mu\bigl(r(M)\bigr)\pmod2}
$$

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). Calculations use the supplied snapshot at commit `d5eed3f10428372c7202ceebc65cc3bdead0819d`, the selected 17-block route with OF and THE separate, the primary SOON ciphertext and its L–C–EA original node, and the candidate THEN → THE continuation using the N–M–N node centered on M(20,17). The 16/16 historical fits and conditional 17/17 extended fits describe that selected route; they do not independently establish an intended or unique Cicada 3301 decryption.
