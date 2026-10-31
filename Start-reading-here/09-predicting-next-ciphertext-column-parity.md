# Predicting the Next Ciphertext’s Column Parity

**Leftmost cell · LP2 pages 0–2**

This rule uses the current ciphertext and its original key node to predict whether the next block’s **leftmost cell** lies in an even or odd column.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Meaning |
| :--- | :--- |
| B | First cell read in the current ciphertext block |
| C | All cells of the current ciphertext block |
| M | Center of the current original key node |
| p | Current derived key’s phase: 0, 1, or 2 |
| m | 1 if the original node’s two outer runes are identical; otherwise 0 |
| L′ | Next block’s leftmost cell |

For any cell `X`, `r(X)` is its row and `c(X)` its column. The leftmost cell is in the **smallest column**, with the **bottommost cell** chosen in a tie.

Take `p` from the [decryption method](00-decryption-method.md). Calculate it modulo 3 first, retaining **0, 1, or 2**. Use the selected original node’s coordinates for `M` and its outer rune symbols for `m`.

**All inputs on the right-hand side belong to the current block.** The prime mark identifies the next block.

## 2. Number cells after rotation

Number the original matrix row by row from 1 to 729:

$$
n_0(r,c)=27(r-1)+c.
$$

A **90° clockwise rotation** sends `(r,c)` to `(c,28−r)`. Let `n_j(X)` be the absolute cell number after `j` such rotations, with `j` reduced modulo 4:

$$
\begin{aligned}
n_1(r,c)&=27(c-1)+28-r,\\
n_2(r,c)&=730-n_0(r,c),\\
n_3(r,c)&=730-n_1(r,c).
\end{aligned}
$$

The center’s rotation depends on the current phase:

| Current p | (p + 2) mod 4 | Center rotation | Index used |
| ---: | ---: | :--- | :--- |
| 0 | 2 | 180° | n₂(M) |
| 1 | 3 | 270° clockwise | n₃(M) |
| 2 | 0 | No rotation | n₀(M) |

These rotations determine numerical inputs to the rule. The ciphertext and key remain in their recorded positions.

## 3. Predict the column parity

$$
\boxed{
c(L')\equiv
r(B)+\sum_{X\in C}\mu\bigl(n_1(X)\bigr)+m+
\mu\!\left(n_{(p+2)\bmod4}(M)\right)
\pmod2.
}
$$

**0 = even column; 1 = odd column.**

To apply the rule:

1. Take the row number of the current beginning `B`.
2. Add the Möbius values of the absolute indices of **all current ciphertext cells after a 90° clockwise rotation**.
3. Add `m`, the current original node’s mirror bit.
4. Add the Möbius value of the center’s phase-dependent rotated index, then reduce the total modulo 2.

The Möbius function `μ(n)` is **0** when `n` has a repeated prime factor; otherwise it is **+1 or −1**. Modulo 2, either nonzero value toggles parity. Equivalently, `μ(n) mod 2 = μ(n)²`, the indicator that `n` is squarefree. Apply it here to **absolute cell indices**.

## 4. Example: WEATHER → TURNS

WEATHER has **`B = (14,14), M = (14,5), p = 2`**. Its original node is **X–OE–X**, so **`m = 1`**.

| Current ciphertext cell | n₁(X) | μ(n₁(X)) |
| :--- | ---: | ---: |
| (14,14) | 365 | +1 |
| (14,15) | 392 | 0 |
| (14,16) | 419 | −1 |
| (14,17) | 446 | +1 |
| (14,18) | 473 | +1 |

The sum is **2**. With `p = 2`, the center is evaluated without rotation:

$$
n_0(M)=356=2^2\times89,\qquad\mu(356)=0.
$$

Therefore:

$$
c(L')\equiv14+2+1+0=17\equiv1\pmod2.
$$

The predicted column is **odd**. TURNS has leftmost cell **`(14,19)`**, which matches.

## 5. Verification across the selected route

The formula matches **27/27 transitions** between the 28 selected blocks, from **AS I GO, THE** through **MAP**. The total is the complete right-hand side before reduction modulo 2.

| No. | Transition | Total | Predicted bit | Recorded L′ |
| ---: | :--- | ---: | ---: | :--- |
| 1 | AS I GO, THE → WEATHER | 16 | 0 | (14,14) |
| 2 | WEATHER → TURNS | 17 | 1 | (14,19) |
| 3 | TURNS → COLD | 15 | 1 | (14,7) |
| 4 | COLD → I MAY | 16 | 0 | (26,16) |
| 5 | I MAY → CRY | 26 | 0 | (19,16) |
| 6 | CRY → NOW THE | 20 | 0 | (11,16) |
| 7 | NOW THE → IDEA | 14 | 0 | (17,18) |
| 8 | IDEA → OF | 15 | 1 | (18,15) |
| 9 | OF → THE | 20 | 0 | (19,16) |
| 10 | THE → END | 21 | 1 | (21,23) |
| 11 | END → IS | 17 | 1 | (21,9) |
| 12 | IS → DEATH | 21 | 1 | (26,1) |
| 13 | DEATH → SEE | 24 | 0 | (27,14) |
| 14 | SEE → YOU | 26 | 0 | (25,16) |
| 15 | YOU → SOON | 26 | 0 | (25,16) |
| 16 | SOON → THEN | 27 | 1 | (25,25) |
| 17 | THEN → THE | 24 | 0 | (21,20) |
| 18 | THE → KEY | 24 | 0 | (21,4) |
| 19 | KEY → IS | 22 | 0 | (19,6) |
| 20 | IS → TO | 18 | 0 | (9,16) |
| 21 | TO → GO | 10 | 0 | (9,20) |
| 22 | GO → TO | 10 | 0 | (12,22) |
| 23 | TO → THE | 14 | 0 | (9,18) |
| 24 | THE → EAST | 12 | 0 | (16,22) |
| 25 | EAST → OF | 14 | 0 | (6,12) |
| 26 | OF → THE | 8 | 0 | (20,12) |
| 27 | THE → MAP | 21 | 1 | (19,11) |

These checks retain the selected original nodes, including SOON’s **L–C–EA** node centered at **C/K(25,7)**. A different spatial source for the same numerical key can change the forecast.

## 6. Forecasts after MAP and MAPLIFE

For MAP, **`B = (19,11), M = (16,9), p = 1, m = 0`**. The center term is:

$$
n_3(M)=502=2\times251,\qquad\mu(502)=+1.
$$

Continuing the same key stream along the same diagonal produces **MAPLIFE as one seven-rune block**. Its phase remains 1; the sum over the current ciphertext changes as the block extends.

| Current block | Ciphertext beginning → endpoint | Σμ(n₁(X)) | Total | Predicted next L′ column |
| :--- | :--- | ---: | ---: | :--- |
| MAP | (19,11) → (17,13) | 0 | 19 + 0 + 0 + 1 = 20 | Even |
| MAPLIFE, one block | (19,11) → (13,17) | 1 | 19 + 1 + 0 + 1 = 21 | Odd |

These are conditional forecasts for two choices of the current block’s boundary.

## 7. Status and use

**Status: an empirical candidate found using all 27 selected transitions.** The sample includes the 16 transitions of the initial 17-block reconstruction and 11 transitions of the candidate continuation. Both parts were used during the search; independent validation is still needed.

Apply this column condition alongside the row-parity rules in [Report 05](05-predicting-next-ciphertext-row-parity.md) and the existing geometry and key constraints. It supplies one parity condition on `L′`; it does not identify an exact cell, key, or plaintext.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
