# Predicting the Next Ciphertext’s Column Parity

This rule predicts whether the next block’s **leftmost cell** lies in an even or odd column. It uses only the current ciphertext and its original key node.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right. For a cell X, `r(X)` is its row and `c(X)` its column.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current block |
| C | All ciphertext cells in the current block |
| M | Center of the current original key node |
| p | Current derived key’s phase: 0, 1, or 2 |
| m | Mirror bit: 1 if the original node’s outer runes match; otherwise 0 |
| L′ | Next block’s leftmost cell |

The **leftmost cell** has the smallest column number; choose the bottommost cell in a tie.

Use the current phase from the [decryption method](00-decryption-method.md). Calculate it **modulo 3 first**, retaining 0, 1, or 2. Keep the selected original node fixed when taking M and m.

## 2. Calculate the rotated cell indices

For each orientation, number cells row by row from **1 to 729**. Use the recorded coordinates in these formulas:

| Clockwise rotation | Absolute cell index |
| :--- | :--- |
| None | n₀(r,c) = 27(r−1) + c |
| 90° | n₁(r,c) = 27(c−1) + 28−r |
| 180° | n₂(r,c) = 730−n₀(r,c) |
| 270° | n₃(r,c) = 730−n₁(r,c) |

Apply the Möbius function μ to these **absolute indices**. It is **0** if a prime factor repeats. Otherwise it is **+1** for an even number of distinct prime factors and **−1** for an odd number; **μ(1) = +1**.

## 3. Add four terms

$$
c(L')\equiv r(B)+s+m+t\pmod2.
$$

| Term | How to calculate it |
| :--- | :--- |
| r(B) | Row number of the current beginning |
| s | Sum of μ(n₁(X)) over **every current ciphertext cell** X |
| m | Original node’s mirror bit |
| t | Möbius value of the center index selected below |

All ciphertext cells use the **90° clockwise index** for s. The center’s index for t depends on the current phase:

| Current phase p | Center rotation | Center term t |
| ---: | :--- | :--- |
| 0 | 180° | μ(n₂(M)) |
| 1 | 270° clockwise | μ(n₃(M)) |
| 2 | None | μ(n₀(M)) |

Add the four terms, then take the remainder modulo 2:

**0 = even column. 1 = odd column.**

Either nonzero Möbius value toggles parity. Counting nonzero values gives the same parity as summing their signs.

## 4. Example: WEATHER → TURNS

WEATHER begins at **B = (14,14)** and uses the original center **M = (14,5)** with phase **p = 2**. Its node is **X–OE–X**, so **m = 1**.

First calculate s from all five ciphertext cells:

| Current cell X | n₁(X) | μ(n₁(X)) |
| :--- | ---: | ---: |
| (14,14) | 365 | +1 |
| (14,15) | 392 | 0 |
| (14,16) | 419 | −1 |
| (14,17) | 446 | +1 |
| (14,18) | 473 | +1 |

Thus **s = 1 + 0 − 1 + 1 + 1 = 2**.

Phase 2 selects the center’s unrotated index:

$$
n_0(M)=356=2^2\times89,\qquad t=\mu(356)=0.
$$

The total is:

$$
r(B)+s+m+t=14+2+1+0=17.
$$

**Prediction: odd column.** TURNS has leftmost cell **(14,19)**, which matches.
