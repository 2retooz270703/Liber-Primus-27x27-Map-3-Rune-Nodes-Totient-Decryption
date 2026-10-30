# Predicting the Next Ciphertext’s Row Parity

**Endpoint and leftmost cell · LP2 pages 0–2**

Two rules predict whether the next ciphertext’s **endpoint** and **leftmost cell** lie in even or odd rows. They use the current key’s phase and original node center, together with the center-row prediction from Report 04.

## 1. Inputs and current phase

The matrix has **27 rows and 27 columns**, numbered from 1. Coordinates are `(row, column)`; rows increase downward and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current ciphertext |
| E | Last cell read in the current ciphertext |
| M | Current original key-node center, before any center-totient transformation |
| p | Current derived key’s phase: 0, 1, or 2 |
| E′ | Next ciphertext’s endpoint |
| L′ | Next ciphertext’s leftmost cell |
| M′ | Next original key-node center |

`r(X)` and `c(X)` are a cell’s row and column coordinates. The leftmost cell is in the **smallest occupied column**; if several cells share that column, choose the **bottommost** one.

All predicted row bits use **`0 = even`** and **`1 = odd`**. They are parity labels, not full row numbers.

For the current derived key `K = (k₁,k₂,k₃)` in its unrotated order, [Report 00](00-decryption-method.md) defines:

$$
p=\left[\sum_{i=1}^{3}\mu\bigl(\varphi(k_i)\bigr)\right]\bmod3.
$$

Here, `φ` is Euler’s totient function. The Möbius function `μ(n)` is `0` if `n` has a repeated prime factor; otherwise it is `+1` for an even number of distinct prime factors and `−1` for an odd number, with `μ(1) = +1`.

**Calculate p modulo 3 first**, keeping its value as 0, 1, or 2. Use that current phase in the rules below, whose final results are reduced modulo 2. The next key’s phase and the running phase total `S` are separate quantities.

## 2. Predict the two rows

The original and 180°-rotated absolute cell numbers are:

$$
n_0(r,c)=27(r-1)+c,\qquad n_2(r,c)=730-n_0(r,c).
$$

### Endpoint row

Use the current phase and the reflected absolute position of the current center:

$$
r(E')\equiv1+p+\mu\bigl(n_2(M)\bigr)\pmod2.
$$

This rule needs only **p and M**.

### Leftmost-cell row

First calculate the next-center row bit using [Report 04](04-predicting-next-key-center-parity.md):

$$
\widehat r(M')=
\bigl[1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\bigr]\bmod2.
$$

Then use:

$$
r(L')\equiv\widehat r(M')+1+p+\mu\bigl(r(M)\bigr)\pmod2.
$$

The hat marks a **predicted parity bit calculated from current inputs**. Do not take it from an already selected next node.

Both rules share `1 + p`, but use different Möbius inputs:

- **Endpoint:** `n₂(M)`, an absolute position from 1 to 729.
- **Leftmost cell:** `r(M)`, a row coordinate from 1 to 27.

Neither is a rune index. In these modulo-2 rules, `μ = 0` keeps parity unchanged; either nonzero sign toggles it.

## 3. Worked example: TURNS → COLD

For TURNS:

**`B = (14,19), E = (10,19), M = (14,23), p = 0`.**

The center has `n₀(M) = 374` and `n₂(M) = 356 = 2² × 89`, so `μ(n₂(M)) = 0`. Its row gives `μ(14) = +1`.

The beginning has `n₂(B) = 360` and `μ(360) = 0`. The earlier center rule therefore gives:

$$
\widehat r(M')=[1+19+10+14+0]\bmod2=0.
$$

| Target | Calculation modulo 2 | Predicted row | Recorded cell |
| :--- | :--- | :--- | :--- |
| Endpoint E′ | 1 + 0 + 0 ≡ 1 | Odd | (11,7) |
| Leftmost cell L′ | 0 + 1 + 0 + 1 ≡ 0 | Even | (14,7) |

This example shows why the endpoint and leftmost cell must be checked separately.

## 4. Check against the recorded route

The next-center bit is calculated before applying the leftmost-cell rule. The final column lists **(endpoint row parity, leftmost-cell row parity)**.

| Transition | Current p | Current M | Predicted center-row bit | Next E′ | Next L′ | Predicted (E′, L′) |
| :--- | ---: | :--- | ---: | :--- | :--- | :--- |
| AS I GO THE → WEATHER | 0 | (13,12) | 0 | (14,18) | (14,14) | (0,0) |
| WEATHER → TURNS | 2 | (14,5) | 0 | (10,19) | (14,19) | (0,0) |
| TURNS → COLD | 0 | (14,23) | 0 | (11,7) | (14,7) | (1,0) |
| COLD → I MAY | 1 | (26,19) | 1 | (26,16) | (26,16) | (0,0) |
| I MAY → CRY | 0 | (15,8) | 1 | (17,16) | (19,16) | (1,1) |
| CRY → NOW THE | 1 | (25,16) | 1 | (15,20) | (11,16) | (1,1) |
| NOW THE → IDEA | 2 | (19,16) | 1 | (17,18) | (17,18) | (1,1) |
| IDEA → OF | 1 | (11,16) | 1 | (18,16) | (18,15) | (0,0) |
| OF → THE (earlier) | 0 | (17,18) | 1 | (19,16) | (19,16) | (1,1) |
| THE (earlier) → END | 2 | (19,16) | 1 | (21,23) | (21,23) | (1,1) |
| END → IS | 2 | (23,12) | 1 | (21,10) | (21,9) | (1,1) |
| IS → DEATH | 1 | (21,22) | 1 | (26,1) | (26,1) | (0,0) |
| DEATH → SEE | 2 | (23,12) | 1 | (27,14) | (27,14) | (1,1) |
| SEE → YOU | 0 | (25,6) | 0 | (25,16) | (25,16) | (1,1) |
| YOU → SOON | 1 | (16,16) | 1 | (25,19) | (25,16) | (1,1) |
| SOON → THEN | 2 | (25,7) | 0 | (25,27) | (25,25) | (1,1) |

Each rule matches **16/16 recorded transitions**. The formulas were found by searching this fitting set, and their match counts are correlated.

The route treats OF and the earlier THE separately. SOON uses the primary ciphertext and the original **`L–C–EA`** node centered on **`C(25,7)`**. Changing the original node can change the predictions.

## 5. Prediction after THEN

The current inputs are:

**`B = (25,25), E = (25,27), M = (26,22), p = 1`.**

The reflected beginning is `n₂(B) = 57`, with `μ(57) = +1`. Hence:

$$
\widehat r(M')=[1+25+25+26+1]\bmod2=0.
$$

For the center, `n₀(M) = 697`, `n₂(M) = 33`, and `μ(33) = +1`. Its row gives `μ(26) = +1`:

$$
r(E')\equiv1+1+1=3\equiv1\pmod2,
$$

$$
r(L')\equiv0+1+1+1=3\equiv1\pmod2.
$$

**Prediction: both the next endpoint and leftmost cell lie in odd rows.**

[Report 02](02-leftmost-cell-and-rotations.md) predicts **END** after THEN, so **L′ = E′**. Here the pair supplies **one shared odd-row filter on the same cell**. These formulas do not predict its column.

### Candidate THE

The selected THE reads **`J(22,21) → W(21,20)`**. Its original **`N–M–N`** node is centered on **`M(20,17)`**; `φ(19) = 18 = E` gives the derived key **`N–E–N`**, with phase **0**.

Its endpoint and leftmost cell are both **`W(21,20)`**, in odd row **21**. This matches both predictions, giving conditional **17/17** for each rule on the extended route.

## 6. Forecast after the candidate THE

Using that THE as the current block:

**`B = (22,21), E = (21,20), M = (20,17), p = 0`.**

The reflected beginning is `n₂(B) = 142`, with `μ(142) = +1`:

$$
\widehat r(M')=[1+21+21+20+1]\bmod2=0.
$$

The center has `n₀(M) = 530`, `n₂(M) = 200`, and `μ(200) = 0`. Its row gives `μ(20) = 0`:

$$
r(E')\equiv1+0+0=1\pmod2,
$$

$$
r(L')\equiv0+1+0+0=1\pmod2.
$$

Both following rows are predicted to be **odd**. The candidate KEY has endpoint **`EA(19,4)`** and leftmost cell **`N(21,4)`**, matching both bits.

These candidate checks are conditional: the continuation was selected using the constraints. They remain separate from the 16-transition fitting set. The rules filter row parity; they do not determine exact coordinates, a unique key, or plaintext. Further independently supported transitions are needed to test them.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

Snapshot: `d5eed3f10428372c7202ceebc65cc3bdead0819d`.
