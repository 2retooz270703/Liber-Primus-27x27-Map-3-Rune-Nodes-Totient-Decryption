# Predicting the Next Ciphertext’s Row Parity

Two rules predict whether the next block’s endpoint and leftmost cell lie in **even or odd rows**.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current block |
| E | Last cell read in the current block |
| M | Current original key-node center, before the totient transformation |
| p | Current derived key’s phase: 0, 1, or 2 |
| E′ | Next block’s endpoint: last cell read |
| L′ | Next block’s leftmost cell |

For any cell `X`, `r(X)` is its row and `c(X)` its column. The leftmost cell is in the **smallest column**, with the **bottommost cell** chosen in a tie.

Calculate the current phase `p` modulo 3, as defined in the [decryption method](00-decryption-method.md), before applying these rules.

## 2. Predict the two row parities

All results are reduced modulo 2: **0 = even, 1 = odd**.

For a cell `(r,c)`, its absolute index after a **180° turn** is:

$$
n_2(r,c)=730-\bigl[27(r-1)+c\bigr].
$$

The Möbius value `μ(n)` is **0** if `n` has a repeated prime factor; otherwise it is **+1 or −1**. Either nonzero value toggles parity.

### Endpoint

$$
r(E')\equiv1+p+\mu\bigl(n_2(M)\bigr)\pmod2.
$$

This uses the current phase and the center’s reflected **absolute index**.

### Leftmost cell

First calculate the predicted next-center row bit `b`, using [Report 04](04-predicting-next-key-center-parity.md):

$$
b=\bigl[1+c(B)+r(E)+r(M)+\mu\bigl(n_2(B)\bigr)\bigr]\bmod2.
$$

Calculate `b` from the current block before selecting the next node. Then:

$$
r(L')\equiv b+1+p+\mu\bigl(r(M)\bigr)\pmod2.
$$

Here, the Möbius input is the center’s **row number** `r(M)`.

## 3. Example: TURNS → COLD

For TURNS, the current inputs are:

**`B = (14,19), E = (10,19), M = (14,23), p = 0`.**

The required values are:

| Input | Value | Möbius value |
| :--- | ---: | ---: |
| n₂(M) | 356 = 2² × 89 | 0 |
| n₂(B) | 360 = 2³ × 3² × 5 | 0 |
| r(M) | 14 = 2 × 7 | +1 |

The predicted next-center row bit is:

$$
b=[1+19+10+14+0]\bmod2=0.
$$

| Target | Calculation modulo 2 | Predicted row | Recorded cell |
| :--- | :--- | :--- | :--- |
| Endpoint E′ | 1 + 0 + 0 ≡ 1 | Odd | (11,7) |
| Leftmost cell L′ | 0 + 1 + 0 + 1 ≡ 0 | Even | (14,7) |

Both predictions match. The endpoint and leftmost cell are different cells here.
