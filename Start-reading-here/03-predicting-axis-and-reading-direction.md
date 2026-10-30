# Predicting the Reading Axis

**Axis and reading direction · LP2 pages 0–2**

Use the current block’s first cell, last cell, and original key node to predict the next block’s axis and reading order.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Input from the current block |
| :--- | :--- |
| B | First cell read |
| E | Last cell read |
| M | Coordinate of the original key-node center |
| h | Original rune index at that center, before the totient transformation |

**M is a coordinate; h is a rune index.** Fix the original node before calculating: nodes that produce the same derived key can give different predictions.

Use Euler’s totient `φ` and the Möbius function `μ`, defined in the [decryption method](00-decryption-method.md).

After each rotation, number cells row by row from 1 to 729:

| Clockwise turn | Absolute index of cell (r, c) |
| :--- | :--- |
| 0° | n₀ = 27(r−1) + c |
| 90° | n₁ = 27(c−1) + 28−r |
| 180° | n₂ = 730−n₀ |
| 270° | n₃ = 27(27−c) + r |

## 2. Predict the axis

Calculate:

$$
A=n_2(B)+n_0(M),\qquad G=\gcd\bigl(n_1(E),n_2(E)\bigr).
$$

Here, `gcd` means greatest common divisor. Keep `A` as an ordinary integer, even when it exceeds 729.

Then calculate the score:

$$
q=\mu(A)+\mu(G).
$$

| Score | Next axis |
| :--- | :--- |
| q = 0 | Horizontal |
| q > 0 | Vertical |
| q < 0 | Diagonal |

## 3. Determine the reading direction

Apply the [boundary rule](02-leftmost-cell-and-rotations.md):

$$
\tau=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod2.
$$

The next block’s **leftmost cell** is the one in the smallest column; choose the bottommost cell in a tie.

| Axis | τ = 1: leftmost read first | τ = 0: leftmost read last |
| :--- | :--- | :--- |
| Horizontal | Right → | Left ← |
| Vertical | Up ↑ | Down ↓ |
| Diagonal | Up-right ↗ or down-right ↘ | Up-left ↖ or down-left ↙ |

For diagonals, the selected coordinates determine the remaining up/down slope.

## 4. Example: after THEN

THEN begins at **`L(25,25)`**, ends at **`W(25,27)`**, and uses the original center **`IA(26,22)`**, with rune index `h = 27`.

### Axis

$$
A=57+697=754,\qquad G=\gcd(705,55)=5.
$$

$$
q=\mu(754)+\mu(5)=-1-1=-2.
$$

The next axis is **diagonal**.

### Reading direction

$$
\tau=[\mu(25)+\varphi(27)]\bmod2=(0+18)\bmod2=0.
$$

The next leftmost cell is read **last**. The predicted direction is therefore **up-left or down-left**.

The candidate THE reads **`J(22,21) → W(21,20)`**, matching the up-left option.

## 5. What the result establishes

Both rules match **16/16 recorded transitions** with the selected original nodes. This is a fit to that route. The rules constrain a candidate’s axis and reading order; they do not determine its exact cells, a unique key, or plaintext.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

