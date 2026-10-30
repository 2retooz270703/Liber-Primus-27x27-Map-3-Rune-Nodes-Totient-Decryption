# Predicting the Next Key’s Center Parity

**Row and column parity · LP2 pages 0–2**

Two formulas use the current block’s coordinates to predict whether the next original key-node center lies in an **even or odd row and column**.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current block |
| E | Last cell read in the current block |
| M | Current original key-node center, before the totient transformation |
| (r′, c′) | Next original key-node center |

For any cell `X`, `r(X)` is its row and `c(X)` its column. All inputs are **coordinate numbers**.

Read each formula modulo 2: **0 = even, 1 = odd**.

## 2. Predict the column parity

Add the three current row numbers and 1:

$$
c'\equiv1+r(B)+r(E)+r(M)\pmod2.
$$

## 3. Predict the row parity

First calculate the beginning’s absolute index after a **180° turn**, numbering cells row by row from 1 to 729:

$$
n_2(B)=730-\bigl[27(r(B)-1)+c(B)\bigr].
$$

Then calculate:

$$
r'\equiv1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\pmod2.
$$

The Möbius value `μ(n)` is **0** if `n` has a repeated prime factor; otherwise it is **+1 or −1**. Modulo 2, zero leaves the sum’s parity unchanged, while either nonzero value toggles it.

## 4. Example: after THEN

THEN has:

- **B = (25,25)** — first cell.
- **E = (25,27)** — last cell.
- **M = (26,22)** — original key-node center.

### Column

$$
c'\equiv1+25+25+26=77\equiv1\pmod2.
$$

The next center’s column should be **odd**.

### Row

The reflected beginning has index:

$$
n_2(B)=730-673=57=3\times19,\qquad\mu(57)=+1.
$$

Therefore:

$$
r'\equiv1+25+25+26+1=78\equiv0\pmod2.
$$

The next center’s row should be **even**.

**Prediction: (row parity, column parity) = (0,1) — even row, odd column.**

This leaves **13 even rows × 14 odd columns = 182 eligible cells** out of 729. The candidate THE uses an original center at **(20,17)**, which passes both conditions.

## 5. What the result establishes

Both formulas match **16/16 recorded transitions** used to find them. Unseen transitions have not yet been tested, and the candidate THE is a conditional check.

The formulas narrow the search for the next original center. They do not identify its exact coordinates, a unique key, or plaintext.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

