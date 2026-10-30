# Predicting the Next Key

This method predicts the next key’s **phase and signature** from the current ciphertext’s coordinates.

## 1. Inputs

For the **derived key in unrotated order**, the signature contains one value `μ(φ(rune index))` per rune. Its phase is the sum of those values modulo 3, as defined in the [decryption method](00-decryption-method.md).

The recorded keys have equal first and third signature values, either **0 or +1**. Call this shared value **a**.

Keep two values as you follow the route:

| Value | Meaning |
| :--- | :--- |
| S | Running sum of the next-key phases predicted so far |
| a | Current key’s shared outer signature value |

Start with **`S = 0, a = 0`**, from the initial key `AE–I–EA`, whose signature is `(0,0,0)`.

Coordinates are `(row, column)`, numbered from 1. Rows increase downward; columns increase to the right.

## 2. Prediction steps

### Step 1 — Predict the next phase

Convert every current ciphertext cell to an absolute position:

$$
n(r,c)=27(r-1)+c.
$$

Use **S before the transition** to choose the calculation. Each sum includes **all cells of the current block**.

| S before | Mode | Next-phase calculation |
| :--- | :--- | :--- |
| 0 ≤ S < 7 | Direct/+1 | (1 + Σμ(n)) mod 3 |
| 7 ≤ S < 14 | Reflected/+0 | Σμ(730−n) mod 3 |
| 14 ≤ S < 21 | Reflected/+1 | (1 + Σμ(730−n)) mod 3 |
| 21 ≤ S < 28 | Direct/+0 — untested | Σμ(n) mod 3 |

`730−n` is the cell’s absolute position after a **180° turn**. The result is the predicted next phase: **0, 1, or 2**.

### Step 2 — Predict the outer values

In the current ciphertext, choose the **leftmost occupied column**, then the **bottommost cell** in that column.

For this cell `(r,c)`, calculate its absolute position after a **90° clockwise turn**:

$$
m=27(c-1)+28-r.
$$

Update the outer value:

$$
a_{\mathrm{next}}=(a+\mu(m))\bmod2.
$$

- **μ(m) = 0:** keep a unchanged.
- **μ(m) = +1 or −1:** switch `0 ↔ 1`.

### Step 3 — Read the complete signature

The next phase and updated outer value determine all three components:

| Next phase | a_next = 0 | a_next = 1 |
| :---: | :--- | :--- |
| 0 | (0,0,0) | (+1,+1,+1) |
| 1 | (0,+1,0) | (+1,−1,+1) |
| 2 | (0,−1,0) | (+1,0,+1) |

For the following transition, **add the predicted phase to S** and **replace a with a_next**. Carry both values forward.

## 3. Example: the prediction after THEN

At THEN, **`S = 18`** and **`a = 0`**, so the active mode is **Reflected/+1**.

### Next phase

| Current cell | Position n | 730−n | μ(730−n) |
| :--- | ---: | ---: | ---: |
| L(25,25) | 673 | 57 | +1 |
| T(25,26) | 674 | 56 | 0 |
| W(25,27) | 675 | 55 | +1 |

The sum is 2. Adding the mode’s offset gives:

$$
p_{\mathrm{next}}=(1+2)\bmod3=0.
$$

### Outer values

The selected cell is **`L(25,25)`**:

$$
m=27(25-1)+28-25=651.
$$

Since `651 = 3 × 7 × 31`, `μ(651) = −1`. Therefore:

$$
a_{\mathrm{next}}=(0-1)\bmod2=1.
$$

Phase **0** and outer value **1** give:

**Next signature: `(+1,+1,+1)`. Next phase: `0`.**

The running total stays at **18**; carry forward **a = 1**.
