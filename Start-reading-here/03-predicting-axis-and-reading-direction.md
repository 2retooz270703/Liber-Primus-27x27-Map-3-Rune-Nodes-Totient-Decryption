# Predicting the Reading Axis

**Axis and reading direction · LP2 pages 0–2**

The current ciphertext’s first cell, last cell, and original key node are used to predict the next block’s **axis**. A separate boundary rule determines the order of reading along that axis.

## 1. Inputs and rotations

The matrix has **27 rows and 27 columns**, numbered from 1. Coordinates are `(row, column)`; rows increase downward and columns increase to the right.

| Symbol | Input from the current block |
| :--- | :--- |
| B | First cell read |
| E | Last cell read |
| M | Coordinate of the original key-node center, before any totient transformation |
| h | Original rune index at that center |

**M is a coordinate; h is a rune index.** They enter different formulas.

Let `n₀`, `n₁`, `n₂`, and `n₃` denote absolute positions after successive 90° clockwise turns:

| Turn | Rotated coordinates | Absolute position |
| :--- | :--- | :--- |
| 0° | (r, c) | n₀ = 27(r−1) + c |
| 90° | (c, 28−r) | n₁ = 27(c−1) + 28−r |
| 180° | (28−r, 28−c) | n₂ = 730−n₀ |
| 270° | (28−c, r) | n₃ = 27(27−c) + r |

Absolute positions run from **1 to 729**. Opposite rotations satisfy:

$$
n_0+n_2=730,\qquad n_1+n_3=730.
$$

**φ(n)** is Euler’s totient: the number of positive integers up to `n` that are coprime to `n`. **μ(n)** is the Möbius function: `0` for a number with a repeated prime factor; otherwise `+1` for an even number of distinct prime factors and `−1` for an odd number. In particular, `μ(1) = +1`.

## 2. Predict the axis

Calculate two integers from the current block:

$$
A=n_2(B)+n_0(M),
$$

$$
G=\gcd\bigl(n_1(E),n_2(E)\bigr).
$$

Here, `gcd` is the **greatest common divisor**. Apply `μ` to both integers and add:

$$
q_{\mathrm{axis}}=\mu(A)+\mu(G).
$$

| Score | Predicted next axis |
| :--- | :--- |
| q = 0 | Horizontal |
| q > 0 | Vertical |
| q < 0 | Diagonal |

Only the sign matters; the score ranges from `−2` to `+2`.

Use **ordinary integer arithmetic**. `A` may exceed 729; do not reduce it modulo 29 or 729. Fix the original node before applying the rule: different nodes can produce the same derived key but different axis predictions.

## 3. Determine the reading direction

The [boundary rule from Report 02](02-leftmost-cell-and-rotations.md) uses the current endpoint and the original center’s rune index:

$$
\tau_{\mathrm{next}}=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod 2.
$$

- **1 = BEGINNING:** the next block’s leftmost cell is read first.
- **0 = END:** the next block’s leftmost cell is read last.

The **leftmost cell** is in the smallest occupied column. If several cells share that column, choose the **bottommost** one.

Combine the predicted axis with the boundary label:

| Axis | BEGINNING | END |
| :--- | :--- | :--- |
| Horizontal | Right → | Left ← |
| Vertical | Up ↑ | Down ↓ |
| Diagonal | Up-right ↗ or down-right ↘ | Up-left ↖ or down-left ↙ |

For horizontal and vertical blocks, this fixes the direction. For diagonals, it fixes **leftward or rightward** reading; the selected cells determine the remaining up/down slope.

## 4. Worked examples

### WEATHER → TURNS: vertical, upward

WEATHER begins at **`NG(14,14)`**, ends at **`E(14,18)`**, and uses the original node centered on **`OE(14,5)`**.

$$
A=365+356=721,\qquad G=\gcd(473,361)=1.
$$

$$
q=\mu(721)+\mu(1)=1+1=2.
$$

The predicted axis is **vertical**. With original center index `OE = 22`:

$$
\tau=[\mu(257)+\varphi(22)]\bmod 2
=(-1+10)\bmod 2=1.
$$

The next leftmost cell is the **BEGINNING**. For a vertical block, the tie-break selects the bottommost cell, so the reading goes **up**. TURNS follows **`A(14,19) → W(10,19)`**.

### COLD → I MAY: horizontal, leftward

COLD begins at **`G(14,7)`**, ends at **`A(11,7)`**, and uses the original node centered on **`TH(26,19)`**.

$$
A=372+694=1066,\qquad G=\gcd(179,453)=1.
$$

$$
q=\mu(1066)+\mu(1)=-1+1=0.
$$

The predicted axis is **horizontal**. With original center index `TH = 2`:

$$
\tau=[\mu(551)+\varphi(2)]\bmod 2
=(1+1)\bmod 2=0.
$$

The next leftmost cell is the **END**, so the reading goes **left**. I MAY follows:

**`TH(26,19) → G(26,18) → T(26,17) → E(26,16)`**

## 5. Check against the recorded route

For SOON, the calculation uses **`C(25,7)`**, the center of the original **`L–C–EA`** node. This choice is part of the input; other nodes yielding the same derived key may give a different axis score.

The final column shows the recorded direction. For diagonal rows, its up/down slope comes from the selected coordinates.

| Transition | μ(A) + μ(G) = q | Predicted axis | Next boundary | Recorded direction |
| :--- | :--- | :--- | :--- | :--- |
| AS I GO THE → WEATHER | μ(717) + μ(5) = 0 | Horizontal | BEGINNING | Right → |
| WEATHER → TURNS | μ(721) + μ(1) = +2 | Vertical | BEGINNING | Up ↑ |
| TURNS → COLD | μ(734) + μ(36) = +1 | Vertical | BEGINNING | Up ↑ |
| COLD → I MAY | μ(1066) + μ(1) = 0 | Horizontal | END | Left ← |
| I MAY → CRY | μ(422) + μ(1) = +2 | Vertical | BEGINNING | Up ↑ |
| CRY → NOW THE | μ(892) + μ(2) = −1 | Diagonal | BEGINNING | Down-right ↘ |
| NOW THE → IDEA | μ(946) + μ(2) = −2 | Diagonal | END | Down-left ↙ |
| IDEA → OF | μ(618) + μ(10) = 0 | Horizontal | BEGINNING | Right → |
| OF → THE | μ(706) + μ(5) = 0 | Horizontal | END | Left ← |
| THE → END | μ(729) + μ(6) = +1 | Vertical | END | Down ↓ |
| END → IS | μ(827) + μ(1) = 0 | Horizontal | BEGINNING | Right → |
| IS → DEATH | μ(743) + μ(10) = 0 | Horizontal | END | Left ← |
| DEATH → SEE | μ(658) + μ(2) = −2 | Diagonal | END | Down-left ↙ |
| SEE → YOU | μ(720) + μ(2) = −1 | Diagonal | END | Up-left ↖ |
| YOU → SOON | μ(431) + μ(6) = 0 | Horizontal | BEGINNING | Right → |
| SOON → THEN | μ(721) + μ(3) = 0 | Horizontal | BEGINNING | Right → |

The axis rule matches **16/16 recorded transitions** with these fixed inputs. The boundary rule also matches all 16 BEGINNING/END labels. The route treats **OF and THE separately** and uses the primary **SOON** reading.

## 6. After THEN and candidate continuation

### Predict the axis and boundary

THEN begins at **`L(25,25)`**, ends at **`W(25,27)`**, and uses the original node centered on **`IA(26,22)`**, with `h = 27`.

$$
A=57+697=754,\qquad G=\gcd(705,55)=5.
$$

$$
q=\mu(754)+\mu(5)=-1-1=-2.
$$

The next axis is therefore **diagonal**. The boundary calculation gives:

$$
\tau=[\mu(25)+\varphi(27)]\bmod 2
=(0+18)\bmod 2=0.
$$

Together with the [next-key prediction from Report 01](01-next-key-signature.md), the constraints are:

| Property | Prediction after THEN |
| :--- | :--- |
| Next key | Signature (+1,+1,+1), phase 0 |
| Next axis | Diagonal |
| Next leftmost cell | END |

The next reading is constrained to **up-left ↖ or down-left ↙**.

### Candidate THE

The selected THE reads **`J(22,21) → W(21,20)`**, giving the actual **up-left** slope. Its original **`N–M–N`** node is centered on **`M(20,17)`** and produces the derived key **`N–E–N`**.

Its leftmost cell, `W(21,20)`, is the endpoint. Its 90° position is **520**, with `μ(520) = 0`, also satisfying the Reflected leftmost-cell condition from Report 02.

### Checks through THE KEY IS TO GO

Keep each selected original node fixed. The first row is the THEN → THE calculation above.

| Transition | A | G | μ(A), μ(G) → q | Predicted axis / boundary | Selected reading |
| :--- | ---: | ---: | :--- | :--- | :--- |
| THEN → THE | 754 | 5 | −1, −1 → −2 | Diagonal / END | Up-left ↖ |
| THE → KEY | 672 | 10 | 0, +1 → +1 | Vertical / BEGINNING | Up ↑ |
| KEY → IS | 499 | 30 | −1, −1 → −2 | Diagonal / END | Down-left ↙ |
| IS → TO | 705 | 2 | −1, −1 → −2 | Diagonal / BEGINNING | Up-right ↗ |
| TO → GO | 712 | 4 | 0, 0 → 0 | Horizontal / BEGINNING | Right → |

All five axes and boundary roles match the selected readings. Adding THEN → THE gives a conditional **17/17 axis fit** on that extended route; the five continuation checks are separate from the 16-transition recorded fit.

These rules constrain a candidate’s axis and reading order. They do not locate its cells, resolve a diagonal’s up/down slope, or identify a unique key or plaintext. The continuation checks remain conditional on the selected ciphertexts and original nodes.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
