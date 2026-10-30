# Predicting the Leftmost Cell

**Rotations and reading boundaries · LP2 pages 0–2**

Two geometric checks constrain a proposed continuation: the Möbius class of its leftmost cell, and whether that cell is read first or last.

## 1. Inputs and notation

The matrix has **27 rows and 27 columns**, numbered from 1. Coordinates are `(row, column)`; rows increase downward and columns increase to the right.

| Symbol | Meaning |
| :--- | :--- |
| C | Current ciphertext block |
| L | Its leftmost cell: choose the smallest occupied column, then the bottommost cell in that column |
| E | Its endpoint: the last cell in the actual reading order |
| h | Center-rune index of the current **original key node, before any totient transformation** |

`L` and `E` may be different cells. The selection of `L` depends on position; the selection of `E` depends on reading order.

**Euler’s totient, φ(n),** counts the positive integers up to `n` that are coprime to `n`. **Möbius μ(n)** is `0` if `n` has a repeated prime factor; otherwise it is `+1` for an even number of distinct prime factors and `−1` for an odd number. In particular, `μ(1) = +1`.

## 2. Four rotations

Absolute positions are numbered row by row from **1 to 729**. All turns below are clockwise about the matrix center.

| Turn | Rotated coordinates | Absolute position | Use |
| :--- | :--- | :--- | :--- |
| 0° | (r, c) | n₀ = 27(r−1) + c | Direct phase calculation |
| 90° | (c, 28−r) | n₁ = 27(c−1) + 28−r | Leftmost-cell selection and class |
| 180° | (28−r, 28−c) | n₂ = 730−n₀ | Reflected phase calculation |
| 270° | (28−c, r) | n₃ = 27(27−c) + r | Next leftmost cell’s reading boundary |

Opposite rotations form complementary pairs:

$$
n_0+n_2=730,\qquad n_1+n_3=730.
$$

For example, **`W(25,27)`** has absolute positions **675, 705, 55, and 25** at 0°, 90°, 180°, and 270°, respectively.

The Direct/Reflected phase calculations are described in [Report 01 — Predicting the Next Key](01-next-key-signature.md).

## 3. Check the leftmost cell’s class

The smallest absolute position after a 90° turn selects the leftmost/bottommost cell:

$$
m(C)=\min_{(r,c)\in C}\bigl[27(c-1)+28-r\bigr],
\qquad \mu_L=\mu(m(C)).
$$

On the selected route, the allowed values depend on the **current block’s mode**:

| Mode | Allowed μ_L |
| :--- | :--- |
| Direct | 0 or +1 |
| Reflected | 0 or −1 |

The mode comes from the phase schedule in Report 01. A zero is allowed in both classes and cannot identify the mode by itself.

For **WEATHER**, `L = NG(14,14)` gives `m = 365 = 5 × 73`, so `μ_L = +1`: a Direct match.

For **IDEA**, `L = D(17,18)` gives `m = 470 = 2 × 5 × 47`, so `μ_L = −1`: a Reflected match. Here, `L` is also the endpoint.

### Recorded 17-block check

| Block | Mode | m = n₁(L) | μ_L |
| :--- | :--- | ---: | ---: |
| AS I GO THE | Direct/+1 | 14 | +1 |
| WEATHER | Direct/+1 | 365 | +1 |
| TURNS | Direct/+1 | 500 | 0 |
| COLD | Direct/+1 | 176 | 0 |
| I MAY | Direct/+1 | 407 | +1 |
| CRY | Direct/+1 | 414 | 0 |
| NOW THE | Direct/+1 | 422 | +1 |
| IDEA | Reflected/+0 | 470 | −1 |
| OF | Reflected/+0 | 388 | 0 |
| THE | Reflected/+0 | 414 | 0 |
| END | Reflected/+0 | 601 | −1 |
| IS | Reflected/+0 | 223 | −1 |
| DEATH | Reflected/+1 | 2 | −1 |
| SEE | Reflected/+1 | 352 | 0 |
| YOU | Reflected/+1 | 408 | 0 |
| SOON | Reflected/+1 | 408 | 0 |
| THEN | Reflected/+1 | 651 | −1 |

All **17 blocks** fit their assigned classes. The 7 Direct blocks contain **four +1 values and three zeros**; the 10 Reflected blocks contain **five −1 values and five zeros**.

## 4. Predict the next reading boundary

Use the **current endpoint E** and the **current original center index h**:

$$
\tau_{\mathrm{next}}=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod 2.
$$

- **1 = BEGINNING:** the next block’s leftmost cell is its first cell read.
- **0 = END:** the next block’s leftmost cell is its last cell read.

The center contribution is **φ(h)**. Use the original node’s center before key derivation. The boundary role applies to horizontal, vertical, and diagonal readings.

### Why the original center matters

For most recorded centers, `φ(h)` is even and leaves the result unchanged modulo 2. The two exceptions have **`h = TH = 2`**, with **`φ(2) = 1`**, which reverses the result.

**COLD → I MAY**

COLD ends at **`A(11,7)`**. Its original node is `H–TH–H`, so `φ(h) = 1`.

$$
n_3(E)=551=19\times29,\qquad\mu(551)=+1.
$$

Thus `τ_next = (1 + 1) mod 2 = 0`: **END**. The next leftmost cell, **`E(26,16)`**, is the last cell of I MAY’s right-to-left reading.

**IDEA → OF**

IDEA ends at **`D(17,18)`**. Its original node is `A–TH–A`, again giving `φ(h) = 1`.

$$
n_3(E)=260=2^2\times5\times13,\qquad\mu(260)=0.
$$

Thus `τ_next = (0 + 1) mod 2 = 1`: **BEGINNING**. The next leftmost cell, **`X(18,15)`**, is the first cell of OF.

### Recorded 16-transition check

Every row uses the current block’s endpoint and original key-node center. The predicted role matches the next block’s recorded reading order.

| Transition | n₃(E) | μ(n₃(E)) | φ(h) | Predicted next role |
| :--- | ---: | ---: | ---: | :--- |
| AS I GO THE → WEATHER | 635 | +1 | 10 | BEGINNING |
| WEATHER → TURNS | 257 | −1 | 10 | BEGINNING |
| TURNS → COLD | 226 | +1 | 12 | BEGINNING |
| COLD → I MAY | 551 | +1 | 1 | END |
| I MAY → CRY | 323 | +1 | 16 | BEGINNING |
| CRY → NOW THE | 314 | +1 | 6 | BEGINNING |
| NOW THE → IDEA | 204 | 0 | 10 | END |
| IDEA → OF | 260 | 0 | 1 | BEGINNING |
| OF → THE | 315 | 0 | 22 | END |
| THE → END | 316 | 0 | 10 | END |
| END → IS | 129 | +1 | 16 | BEGINNING |
| IS → DEATH | 480 | 0 | 2 | END |
| DEATH → SEE | 728 | 0 | 16 | END |
| SEE → YOU | 378 | 0 | 10 | END |
| YOU → SOON | 322 | −1 | 2 | BEGINNING |
| SOON → THEN | 241 | −1 | 4 | BEGINNING |

The full formula matches **16/16 transitions**. Using only the endpoint’s Möbius value gives **14/16**; the original-center correction resolves COLD → I MAY and IDEA → OF.

## 5. Prediction after THEN and candidate continuation

### The next leftmost cell should be the END

THEN occupies row 25, columns 25–27, ending at **`W(25,27)`**. Its original center is **`IA = 27`**, with `φ(27) = 18`.

$$
n_3(E)=25,\qquad\mu(25)=0,
$$

$$
\tau_{\mathrm{next}}=(0+18)\bmod 2=0.
$$

The predicted next leftmost cell is therefore the **last cell read**. This prediction follows the 16-transition record, which ends at SOON → THEN.

THEN’s own leftmost cell is **`L(25,25)`**, with `n₁ = 651 = 3 × 7 × 31` and `μ_L = −1`, matching Reflected/+1. A following candidate in the same regime must have `μ_L ∈ {−1, 0}`.

### Candidate THE

The candidate THE reads **`J(22,21) → W(21,20)`** under the derived key **`N–E–N`**, from the original node centered on **`M(20,17)`**.

Its leftmost cell is **`W(21,20)`**, the endpoint. Its 90° position is:

$$
n_1(21,20)=520=2^3\times5\times13,\qquad\mu(520)=0.
$$

It satisfies both the predicted **END** role and the Reflected sign class.

### Checks through THE KEY IS TO GO

Each row predicts the next boundary from the current block. The final column checks the selected next leftmost cell, `L′`, separately.

| Transition | n₃(E) / μ | φ(h) | Predicted role | Next L′ | n₁(L′) / μ |
| :--- | :--- | ---: | :--- | :--- | :--- |
| THEN → THE | 25 / 0 | 18 | END | (21,20) | 520 / 0 |
| THE → KEY | 210 / +1 | 18 | BEGINNING | (21,4) | 88 / 0 |
| KEY → IS | 640 / 0 | 4 | END | (19,6) | 144 / 0 |
| IS → TO | 586 / +1 | 4 | BEGINNING | (9,16) | 424 / 0 |
| TO → GO | 278 / +1 | 18 | BEGINNING | (9,20) | 532 / 0 |

All five predicted roles match the selected reading orders. KEY begins at its bottommost cell and reads upward; IS ends at its leftmost cell; TO begins at its leftmost cell.

## 6. Scope and limits

- **Route used:** the recorded checks treat OF and THE separately and use the primary SOON reading.
- **Candidate continuation:** the five checks through GO remain separate from the recorded fit. All five candidate leftmost cells give `μ = 0`, which fits both sign classes and cannot select Reflected by itself.
- **Output:** these checks constrain a continuation, but do not determine its exact coordinates, length, direction, or plaintext, or establish a unique route.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
