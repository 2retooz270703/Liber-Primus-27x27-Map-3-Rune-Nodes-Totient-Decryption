# Predicting the Next Key

**Möbius signatures · LP2 pages 0–2**

The current ciphertext’s coordinates are used to predict the **next key’s phase and Möbius signature**. The calculation fits 16 transitions on the selected route and gives a constraint for continuing after THEN.

## 1. Target and inputs

For a derived three-rune key in its **unrotated order**, the signature and phase are:

$$
\sigma_i=\mu(\varphi(k_i)),\qquad
p=(\sigma_1+\sigma_2+\sigma_3)\bmod 3.
$$

Here, `φ(n)` is Euler’s totient: the number of positive integers up to `n` that are coprime to `n`. The Möbius function `μ(n)` is `0` if `n` has a repeated prime factor; otherwise it is `+1` for an even number of distinct prime factors and `−1` for an odd number. In particular, `μ(1) = +1`.

The 17 recorded keys share the form:

$$
\sigma=(a,b,a),\qquad a\in\{0,1\},\quad b\in\{-1,0,+1\}.
$$

Equal outer signature values do not require identical outer runes: `AE–I–EA` and `H–NG–C` both fit this family.

The prediction needs:

- **Current ciphertext cells:** their coordinates and block boundaries.
- **Current outer state, a:** the first and third components of the current key’s signature.
- **Running phase total, S:** the sum of the next-key phases predicted so far.

Start with **`S = 0`** and **`a = 0`**, from the initial key `AE–I–EA`, whose signature is `(0,0,0)`.

Coordinates are `(row, column)`, numbered from 1. Rows increase downward; columns increase to the right.

## 2. Prediction steps

### Step 1 — Number the ciphertext cells

Convert every current ciphertext cell to an absolute position:

$$
n(r,c)=27(r-1)+c.
$$

Positions run from **1 to 729**. Write the current block’s positions as `n₁, n₂, …`.

### Step 2 — Predict the next phase

Select the mode using **S before the transition**:

| S before | Mode | U(n) | Offset δ |
| :--- | :--- | :--- | ---: |
| 0 ≤ S < 7 | Direct/+1 | n | 1 |
| 7 ≤ S < 14 | Reflected/+0 | 730 − n | 0 |
| 14 ≤ S < 21 | Reflected/+1 | 730 − n | 1 |
| 21 ≤ S < 28 | Direct/+0 — untested | n | 0 |

The Reflected modes use a **180° turn**: `(r,c)` becomes `(28−r,28−c)`, taking position `n` to `730−n`.

Apply `μ` to every position in the active mode, add the offset, and reduce modulo 3:

$$
p_{\mathrm{next}}=\left(\delta+\sum_i\mu(U(n_i))\right)\bmod 3.
$$

### Step 3 — Predict the outer state

A **90° clockwise turn** maps `(r,c)` to `(c,28−r)`. The rotated absolute position is:

$$
n_{90}(r,c)=27(c-1)+28-r.
$$

Select the smallest rotated position among all current ciphertext cells:

$$
m=\min_i n_{90}(r_i,c_i).
$$

On the original grid, this means: choose the **leftmost occupied column**, then the **bottommost cell** in that column.

Update the outer state:

$$
a_{\mathrm{next}}=(a+\mu(m))\bmod 2.
$$

- **μ(m) = 0:** keep the current state.
- **μ(m) = +1 or −1:** switch `0 ↔ 1`.

### Step 4 — Complete the signature and carry the state forward

The middle component follows from the phase:

$$
b_{\mathrm{next}}\equiv p_{\mathrm{next}}-2a_{\mathrm{next}}\pmod 3.
$$

Convert the residue to a Möbius value: **`0 → 0`, `1 → +1`, `2 → −1`**.

| Next phase | Signature if a_next = 0 | Signature if a_next = 1 |
| :---: | :--- | :--- |
| 0 | (0, 0, 0) | (+1, +1, +1) |
| 1 | (0, +1, 0) | (+1, −1, +1) |
| 2 | (0, −1, 0) | (+1, 0, +1) |

Finally, update the running total:

$$
S_{\mathrm{next}}=S+p_{\mathrm{next}}.
$$

Use the predicted `a_next` and updated `S` for the following transition. The outer state is propagated recursively; it is not reset from each recorded next key.

## 3. Check against the recorded route

In the table, **Σμ** is the sum in the active mode, **p** is the predicted next phase, and **S after** includes that prediction. Every calculation uses the **current block’s cells**.

| Transition | Σμ | p | m / μ(m) | Predicted next signature | S after |
| :--- | ---: | ---: | :--- | :--- | ---: |
| AS I GO THE → WEATHER | −2 | 2 | 14 / +1 | (+1, 0, +1) | 2 |
| WEATHER → TURNS | −1 | 0 | 365 / +1 | (0, 0, 0) | 2 |
| TURNS → COLD | 0 | 1 | 500 / 0 | (0, +1, 0) | 3 |
| COLD → I MAY | −1 | 0 | 176 / 0 | (0, 0, 0) | 3 |
| I MAY → CRY | 0 | 1 | 407 / +1 | (+1, −1, +1) | 4 |
| CRY → NOW THE | +1 | 2 | 414 / 0 | (+1, 0, +1) | 6 |
| NOW THE → IDEA | 0 | 1 | 422 / +1 | (0, +1, 0) | 7 |
| IDEA → OF | 0 | 0 | 470 / −1 | (+1, +1, +1) | 7 |
| OF → THE | −1 | 2 | 388 / 0 | (+1, 0, +1) | 9 |
| THE → END | −1 | 2 | 414 / 0 | (+1, 0, +1) | 11 |
| END → IS | +1 | 1 | 601 / −1 | (0, +1, 0) | 12 |
| IS → DEATH | −1 | 2 | 223 / −1 | (+1, 0, +1) | 14 |
| DEATH → SEE | −1 | 0 | 2 / −1 | (0, 0, 0) | 14 |
| SEE → YOU | 0 | 1 | 352 / 0 | (0, +1, 0) | 15 |
| YOU → SOON | +1 | 2 | 408 / 0 | (0, −1, 0) | 17 |
| SOON → THEN | 0 | 1 | 408 / 0 | (0, +1, 0) | 18 |

The first **7 transitions** use Direct/+1; the next **5** use Reflected/+0; the final **4** use Reflected/+1. Their phase sums are **7, 7, and 4**, bringing `S` to **18**.

All **16 predicted phases and complete signatures** match the recorded next keys. This selected route treats **OF and THE as separate blocks** and uses the project’s primary **SOON** reading.

### Sign check for the selected cell

The same `μ(m)` values also follow a mode-dependent pattern:

| Recorded mode | Nonzero values | Zero values |
| :--- | :--- | ---: |
| Direct/+1 | Four +1 values | 3 |
| Reflected/+0 and Reflected/+1 | Four −1 values | 5 |

THEN also gives `μ(m) = −1` in Reflected/+1, extending this sign check to **17/17 known blocks**. It reuses the outer-state calculation, so it is not an independent test.

## 4. Worked prediction after THEN

The current key is **`IA–E–IA`**, with signature `(0,+1,0)`. Thus **`a = 0`**. The running total is **`S = 18`**, selecting **Reflected/+1**.

The THEN ciphertext occupies three cells:

| Cell | Position n | 730 − n | μ(730 − n) |
| :--- | ---: | ---: | ---: |
| L(25,25) | 673 | 57 | +1 |
| T(25,26) | 674 | 56 | 0 |
| W(25,27) | 675 | 55 | +1 |

**Next phase:** the reflected sum is 2, so:

$$
p_{\mathrm{next}}=(1+2)\bmod 3=0.
$$

**Outer state:** the selector chooses `L(25,25)`, giving:

$$
m=27(25-1)+28-25=651.
$$

Since `651 = 3 × 7 × 31`, `μ(651) = −1`. Therefore:

$$
a_{\mathrm{next}}=(0-1)\bmod 2=1.
$$

**Complete signature:** phase 0 and outer state 1 give middle value `+1`:

$$
\boxed{p_{\mathrm{next}}=0,\qquad\sigma_{\mathrm{next}}=(+1,+1,+1).}
$$

The running total stays at **`S = 18`**.

## 5. Candidate continuation: THE KEY IS TO GO

### The first THE

The candidate ciphertext is **`J(22,21) → W(21,20)`**. Its original key node is the vertical mirror:

**`N(17,17) – M(20,17) – N(23,17)`**

The center transforms as `φ(M = 19) = 18 = E`, giving **`N–E–N`**, with indices `(9,18,9)`. Its signature is **`(+1,+1,+1)`** and its phase is **0**, matching the prediction after THEN.

Subtracting the first two key indices from `J–W` modulo 29 gives **`TH–E` → THE**.

### Five candidate transitions

The same rules give the following results. All five use **Reflected/+1**. The `S` column shows the total before and after each transition.

| Transition | S before → after | Σμ | m / μ(m) | Next phase | Next signature | Selected next key |
| :--- | :--- | ---: | :--- | ---: | :--- | :--- |
| THEN → THE | 18 → 18 | +2 | 651 / −1 | 0 | (+1, +1, +1) | N–E–N |
| THE → KEY | 18 → 19 | 0 | 520 / 0 | 1 | (+1, −1, +1) | TH–R–TH |
| KEY → IS | 19 → 20 | 0 | 88 / 0 | 1 | (+1, −1, +1) | W–R–W |
| IS → TO | 20 → 20 | −1 | 144 / 0 | 0 | (+1, +1, +1) | X–E–X |
| TO → GO | 20 → 20 | −1 | 424 / 0 | 0 | (+1, +1, +1) | TH–TH–TH |

Each selected key matches the predicted signature. The outer state switches to 1 after THEN and remains 1 throughout this continuation.

## 6. Scope and limits

- **Recorded fit:** 16/16 next-key signatures on the selected route. The middle component is derived from the phase and outer state, so these are not three independent predictions.
- **Candidate continuation:** the five checks through GO fit the selected keys, but the candidate was found using these constraints. They remain separate from the 16-transition recorded fit.
- **Mode schedule:** thresholds 7 and 14 were fitted to the recorded route. Direct/+0 at `21 ≤ S < 28` and any repeating cycle remain untested.
- **Output:** the rule predicts a signature within the observed family. It does not uniquely identify the next key’s runes, ciphertext location, or plaintext.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
