# Predicting the Next Key

**A Geometric Signature Prediction Report**

*27 × 27 matrix · Möbius signatures · Phase cycles · Rotational geometry*

---

The central question of this report is whether a completed ciphertext block can tell us something about the **next decryption key before that key is selected**. In the recorded reading of *Liber Primus* LP2, pages 0–2, the answer takes the form of a numerical prediction: the current ciphertext's **cell positions** determine the next key's phase and its three-component Möbius signature.

Two geometric operations work together. A calculation across **all cells of the current ciphertext** predicts the next key's phase. A separate calculation using **one cell selected after a 90° rotation** predicts the state of its outer signature components. Those two results determine the entire signature. Across the selected route, this procedure reproduces **16 consecutive recorded next-key signatures**.

This report concerns **only the prediction of the next key's signature**. It does not attempt to select the next ciphertext, derive the exact three runes of the key, or describe the separate movement and mirror-navigation rules.

**Contents**

[01. Foundations](#foundations) · [02. The geometry](#the-geometry) · [03. Predicting the phase](#predicting-the-phase) · [04. Predicting the outer state](#predicting-the-outer-state) · [05. Reconstructing the signature](#reconstructing-the-signature) · [06. Verification across the route](#verification-across-the-route) · [07. Prediction after THEN](#prediction-after-then) · [Formula reference](#formula-reference)

---

## Foundations

### What is being predicted?

Every decryption key in this model is an ordered sequence of **three rune indices**. Before any cyclic alignment is applied, write the derived key as:

$$
K=(k_1,k_2,k_3)
$$

Its **Möbius signature** is obtained by applying Euler's totient function, then the Möbius function, to each rune index:

$$
\sigma_i=\mu(\varphi(k_i)),\qquad i=1,2,3
$$

The three values form the ordered signature **`(σ₁, σ₂, σ₃)`**. Here, $\varphi(n)$ is Euler's totient function. The Möbius function $\mu(n)$ returns **−1**, **0**, or **+1**. It is zero when $n$ has a squared prime factor; otherwise its sign depends on the parity of the number of distinct prime factors.

The **phase** of a key is the sum of its three signature components modulo 3:

$$
p=(\sigma_1+\sigma_2+\sigma_3)\bmod 3
$$

A phase is therefore one of **0, 1, or 2**. In decryption, it describes the key's cyclic alignment. In this report, it is the **first quantity predicted for the next key**.

### The observed signature family

The 17 recorded keys, including the starting key, share a useful numerical property: their first and third signature components are equal and are either 0 or +1. Thus each signature has the form:

$$
\sigma(K)=(a,b,a)
$$

The outer state $a$ can be **0 or 1**, and the middle value $b$ can be **−1, 0, or +1**. Importantly, equal *signature components* do not mean that the outer **runes** have to be identical. The keys `AE–I–EA` and `H–NG–C`, for example, need not have matching outer letters to fit the same numerical family.

The initial derived key, **`AE–I–EA`**, has signature **`(0,0,0)`**. Consequently, the starting outer state is:

$$
a_0=0
$$

This observed initial state lets the prediction proceed **recursively**, without replacing a computed outer state with the observed next one at each step.

### Ciphertext cells and the running phase total

The grid has **27 rows and 27 columns**, numbered from 1. Rows increase downward, and columns increase to the right. A cell at row $r$, column $c$ has an absolute position:

$$
n(r,c)=27(r-1)+c
$$

Absolute positions run from **1 to 729**. Let $C$ denote the set of positions belonging to the **current ciphertext block**. The block's boundaries must be specified before the prediction is applied.

We also retain a cumulative phase total, **`S`**. It begins at **0** and is increased by each predicted next-key phase:

$$
S_{\mathrm{next}}=S+p_{\mathrm{next}}
$$

This total controls which **phase-calculation mode** is active. It is not the key's phase itself: $p$ is always 0, 1, or 2, whereas $S$ accumulates across transitions.

---

## The Geometry

### One rotation, two roles

A **90° clockwise** rotation of a 27 × 27 cell coordinate is:

$$
R(r,c)=(c,28-r)
$$

After two such rotations, the cell has undergone a **180° turn about the matrix center**:

$$
R^2(r,c)=(28-r,28-c)
$$

Under absolute numbering, that half-turn takes position $n$ to:

$$
n\bigl(R^2(r,c)\bigr)=730-n(r,c)
$$

The constant **730** comes directly from the matrix's **729 cells plus one**. For example, absolute position `673` becomes `57` after a half-turn, because `730 − 673 = 57`.

This reveals the model's central geometric relationship:

- **Original positions, $R^0$:** used by the **Direct** phase calculation.
- **Half-turned positions, $R^2$:** used by the **Reflected** phase calculation.
- **Quarter-turned positions, $R^1$:** used to select one cell for the **outer-state update**.

In other words, the calculations for phase and outer state are different, but both are expressed through powers of the **same 90° clockwise rotation**. The proposed next-key prediction does not require $R^3$.

### Why the two geometric operations are kept distinct

The phase operation adds Möbius values from **every ciphertext cell**. The outer-state operation uses only the cell with the **smallest absolute position after a quarter-turn**. Neither operation depends on already knowing the exact next key.

The two operations will now be derived separately and then combined.

---

## Predicting the Phase

### The rule for all ciphertext cells

Start with the absolute positions of the current ciphertext. Depending on the active mode, use either their original positions or their **180°-rotated** positions. Apply $\mu$ to each, add the results, include a mode-specific offset, and reduce modulo 3.

Let $U(n)$ mean either $n$ or $730-n$. Let $\delta$ be either 0 or 1. Then:

$$
\boxed{p_{\mathrm{next}}=\left(\delta+\sum_{n\in C}\mu(U(n))\right)\bmod 3}
$$

What changes from one mode to another is **not** this general calculation, but the pair of choices **`U`** and **`δ`**.

### The phase-cycle modes

The accumulated total $S$, evaluated **before each transition**, selects one of four proposed modes.

**Mode I — Direct/+1 · `0 ≤ S < 7`**

Use original positions and add 1:

$$
p_{\mathrm{next}}=\left(1+\sum_{n\in C}\mu(n)\right)\bmod 3
$$

This is the observed starting mode. It matches the first **7 consecutive transitions**, ending when the cumulative total reaches `S = 7`.

**Mode II — Reflected/+0 · `7 ≤ S < 14`**

Use the half-turned positions, with no additive offset:

$$
p_{\mathrm{next}}=\left(\sum_{n\in C}\mu(730-n)\right)\bmod 3
$$

This matches the next **5 transitions**. Their predicted phases increase the total from `S = 7` to `S = 14`.

**Mode III — Reflected/+1 · `14 ≤ S < 21`**

Keep the half-turned positions, but restore the offset of 1:

$$
p_{\mathrm{next}}=\left(1+\sum_{n\in C}\mu(730-n)\right)\bmod 3
$$

This matches the following **4 recorded transitions**. At the end of the primary 17-block route, the cumulative total is `S = 18`, so this mode is still active.

**Mode IV — Direct/+0 · `21 ≤ S < 28`**

The proposed fourth state returns to original positions without the offset:

$$
p_{\mathrm{next}}=\left(\sum_{n\in C}\mu(n)\right)\bmod 3
$$

**This fourth mode has not yet been tested against a recorded next key.** It completes the proposed four-state pattern, but it is not part of the observed 16-transition fit.

### How the cycle is organized

The four proposed modes form a sequence:

**Direct/+0 → Direct/+1 → Reflected/+0 → Reflected/+1 → Direct/+0**

The known route starts in **Direct/+1**, not Direct/+0. Each transition adds its predicted phase (0, 1, or 2) to $S$. Crossing the thresholds **7**, **14**, and — prospectively — **21** changes the active calculation.

The first seven predictions are:

`2 · 0 · 1 · 0 · 1 · 2 · 1`

They sum to **7**. The following five predictions are:

`0 · 2 · 2 · 1 · 2`

They also sum to **7**. The next four are:

`0 · 1 · 2 · 1`

They add **4**, bringing the total to **18**.

The step at `S = 7` changes **both** the geometric orientation and the additive offset. The step at `S = 14` changes **only** the offset. The anticipated step at `S = 21` would return to the Direct orientation.

The thresholds at 7 and 14 were identified from this recorded route. The unobserved fourth mode and any repeating cycle beyond it are **extensions of the model**, not additional verified transitions.

---

## Predicting the Outer State

### Select one cell after a quarter-turn

The second part of the prediction uses a **90° clockwise rotation**, not the half-turn used in the Reflected phase calculation.

The absolute position of a rotated cell is:

$$
n_{90}(r,c)=27(c-1)+28-r
$$

Among **all cells of the current ciphertext**, select the minimum of these rotated positions:

$$
\boxed{m=\min_{(r,c)\in C}n_{90}(r,c)}
$$

There is a simple way to identify this cell **without rotating the grid visually**: first find the ciphertext's **leftmost occupied column**; if several cells share that column, take the **bottommost** one. That is precisely the cell whose rotated absolute position is smallest.

The chosen cell may be the start, end, or an interior point of the ciphertext. The selection rule remains the same.

### Update the outer components

Let $a$ be the outer state of the **current key**, already known from the starting key or the previous prediction. The next outer state is:

$$
\boxed{a_{\mathrm{next}}=(a+\mu(m))\bmod 2}
$$

This gives a particularly clear interpretation:

- **`μ(m) = 0`:** preserve the existing outer state.
- **`μ(m) = +1` or `−1`:** switch the outer state from 0 to 1, or from 1 to 0.

Because the update is taken modulo 2, **both nonzero signs toggle the same state**. Equivalently, a **square-free** selected position toggles the outer state; a position with a repeated prime factor preserves it.

For example, at the transition **`IDEA → OF`**, the selected current-ciphertext cell is `D(17,18)`. Its rotated position is:

$$
m=27(18-1)+28-17=470
$$

Because `470 = 2 × 5 × 47`, its Möbius value is **−1**. The incoming outer state is 0, so:

$$
a_{\mathrm{next}}=(0-1)\bmod 2=1
$$

The next key must therefore have outer signature components **`(+1, …, +1)`**. The middle component is determined by the phase, as shown next.

### A second check: the sign follows the geometric mode

The same selected position $m$ shows a consistent **mode-dependent sign restriction** on the recorded route:

**Direct modes** permit:

$$
\mu(m)\in\{0,+1\}
$$

**Reflected modes** permit:

$$
\mu(m)\in\{0,-1\}
$$

Among the first seven Direct/+1 transitions, the selected positions yield **four `+1` values and three zeros**. Across the following nine Reflected transitions, they yield **four `−1` values and five zeros**. The known `THEN` ciphertext also yields `−1`, making **17/17 known ciphertext blocks** consistent with the mode-specific sign restriction.

The restriction concerns the **sign of the same Möbius value** used by the outer-state update. It is a useful geometric consistency check, not a third independent source of the next signature.

A square-free integer has $\mu(m)=+1$ when it has an **even** number of distinct prime factors, and $\mu(m)=-1$ when the number is **odd**. The nonzero selected positions in this route reflect exactly that distinction: `14`, `365`, `407`, and `422` in the Direct part; `470`, `601`, `223`, `2`, and `651` in the Reflected part (the last is from `THEN`).

---

## Reconstructing the Signature

### From two predictions to three components

By this point, the calculation has produced two pieces of information:

1. **`p_next`**, the next key's phase, computed from **all ciphertext cells** and the active phase-cycle mode.
2. **`a_next`**, the shared outer state of the next signature, computed from **one 90°-selected cell**.

Within the observed signature family, the next signature must have the form:

$$
\sigma_{\mathrm{next}}=(a_{\mathrm{next}},b_{\mathrm{next}},a_{\mathrm{next}})
$$

Its phase is the sum of those three values modulo 3:

$$
p_{\mathrm{next}}\equiv 2a_{\mathrm{next}}+b_{\mathrm{next}}\pmod 3
$$

Therefore the middle component is fixed algebraically:

$$
\boxed{b_{\mathrm{next}}\equiv p_{\mathrm{next}}-2a_{\mathrm{next}}\pmod 3}
$$

To convert the residue into a Möbius value, interpret **0 as 0**, **1 as +1**, and **2 as −1**.

### All six possible signatures

The two outer-state possibilities and the three phase values give precisely **six** signatures in the observed family:

- **Phase 0:** outer state `0` gives **`(0,0,0)`**; outer state `1` gives **`(+1,+1,+1)`**.
- **Phase 1:** outer state `0` gives **`(0,+1,0)`**; outer state `1` gives **`(+1,−1,+1)`**.
- **Phase 2:** outer state `0` gives **`(0,−1,0)`**; outer state `1` gives **`(+1,0,+1)`**.

There is **no separate middle-rune rule** here. Once the phase and outer state are known, the central signature component follows necessarily.

### A complete example: IDEA → OF

The current block is `IDEA`; the running phase total is **`S = 7`**. This selects **Reflected/+0**. The reflected Möbius sum across the current ciphertext is **0**, so:

$$
p_{\mathrm{next}}=(0+0)\bmod 3=0
$$

As calculated above, the selected 90° cell gives `m = 470`, `μ(m) = −1`, and therefore **`a_next = 1`**. For phase 0:

$$
b_{\mathrm{next}}=(0-2)\bmod 3=1
$$

The prediction is consequently:

$$
\boxed{\sigma_{\mathrm{next}}=(+1,+1,+1)}
$$

That matches the recorded **`OF`** key's complete Möbius signature. The example illustrates the division of labor: the **whole ciphertext** predicts the phase, the **selected rotated cell** predicts the outer state, and the **signature equation** supplies the middle value.

---

## Verification Across the Route

The following is the complete **16-transition record** used in the combined check. Each entry gives the current-to-next passage, the Möbius sum in the active phase mode (`Σμ`), the predicted phase (`p`), the 90°-selected position (`m`) and its Möbius value, the updated cumulative total (`S`), and the **predicted next-key signature**. The recorded next key has the same signature in each of these entries.

The entries are grouped by the active phase-cycle mode. All position and sign calculations refer to the **current** ciphertext block, not to the next one.

### Mode I · Direct/+1 — 7 matches

1. **`AS I GO THE` → `WEATHER`** — `Σμ = −2`, `p = 2`, `m = 14`, `μ(m) = +1`, `S = 2` → **`(+1,0,+1)`**.
2. **`WEATHER` → `TURNS`** — `Σμ = −1`, `p = 0`, `m = 365`, `μ(m) = +1`, `S = 2` → **`(0,0,0)`**.
3. **`TURNS` → `COLD`** — `Σμ = 0`, `p = 1`, `m = 500`, `μ(m) = 0`, `S = 3` → **`(0,+1,0)`**.
4. **`COLD` → `I MAY`** — `Σμ = −1`, `p = 0`, `m = 176`, `μ(m) = 0`, `S = 3` → **`(0,0,0)`**.
5. **`I MAY` → `CRY`** — `Σμ = 0`, `p = 1`, `m = 407`, `μ(m) = +1`, `S = 4` → **`(+1,−1,+1)`**.
6. **`CRY` → `NOW THE`** — `Σμ = +1`, `p = 2`, `m = 414`, `μ(m) = 0`, `S = 6` → **`(+1,0,+1)`**.
7. **`NOW THE` → `IDEA`** — `Σμ = 0`, `p = 1`, `m = 422`, `μ(m) = +1`, `S = 7` → **`(0,+1,0)`**.

The **seventh prediction** raises $S$ to 7 and moves the calculation into Reflected/+0 for the next transition.

### Mode II · Reflected/+0 — 5 matches

8. **`IDEA` → `OF`** — `Σμ = 0`, `p = 0`, `m = 470`, `μ(m) = −1`, `S = 7` → **`(+1,+1,+1)`**.
9. **`OF` → `THE`** — `Σμ = −1`, `p = 2`, `m = 388`, `μ(m) = 0`, `S = 9` → **`(+1,0,+1)`**.
10. **`THE` → `END`** — `Σμ = −1`, `p = 2`, `m = 414`, `μ(m) = 0`, `S = 11` → **`(+1,0,+1)`**.
11. **`END` → `IS`** — `Σμ = +1`, `p = 1`, `m = 601`, `μ(m) = −1`, `S = 12` → **`(0,+1,0)`**.
12. **`IS` → `DEATH`** — `Σμ = −1`, `p = 2`, `m = 223`, `μ(m) = −1`, `S = 14` → **`(+1,0,+1)`**.

Here the **twelfth prediction** raises $S$ to 14. The geometric orientation stays Reflected, while the offset changes from +0 to +1.

### Mode III · Reflected/+1 — 4 matches

13. **`DEATH` → `SEE`** — `Σμ = −1`, `p = 0`, `m = 2`, `μ(m) = −1`, `S = 14` → **`(0,0,0)`**.
14. **`SEE` → `YOU`** — `Σμ = 0`, `p = 1`, `m = 352`, `μ(m) = 0`, `S = 15` → **`(0,+1,0)`**.
15. **`YOU` → `SOON`** — `Σμ = +1`, `p = 2`, `m = 408`, `μ(m) = 0`, `S = 17` → **`(0,−1,0)`**.
16. **`SOON` → `THEN`** — `Σμ = 0`, `p = 1`, `m = 408`, `μ(m) = 0`, `S = 18` → **`(0,+1,0)`**.

At the end of these 16 transitions, **`S = 18`**. The proposed threshold of 21 has not yet been reached.

### Reading the result correctly

On this **fixed, selected route**, the phase rule matches **16/16 recorded next-key phases**, and the recursively propagated outer-state rule reconstructs **16/16 complete next-key signatures**. The sign restriction on the selected rotated cell holds for the **same 16 blocks**, plus the known ciphertext `THEN` — hence **17/17** for that separate check.

These counts are **not three independent experiments**. The middle signature component is derived from the phase and outer state, while the sign check reuses the same selected Möbius value as the outer-state rule. The selected route treats **`OF` and `THE` as separate ciphertext blocks** and uses the primary `SOON` reading recorded in the project.

---

## Prediction After THEN

### The current state

The last recorded block is **`THEN`**. Its ciphertext occupies three cells on row 25:

- **`L(25,25)`** — absolute position **673**.
- **`T(25,26)`** — absolute position **674**.
- **`W(25,27)`** — absolute position **675**.

The current derived key is **`IA–E–IA`**, with signature **`(0,+1,0)`**, so the current outer state is **`a = 0`**. The phase total is **`S = 18`**; the active calculation therefore remains **Reflected/+1**.

### Step 1 — Predict the next phase

Reflect the three absolute positions through the center of the matrix:

- `673` becomes **57**, with `μ(57) = +1`.
- `674` becomes **56**, with `μ(56) = 0`.
- `675` becomes **55**, with `μ(55) = +1`.

The transformed Möbius sum is **2**. With the Reflected/+1 offset:

$$
p_{\mathrm{next}}=(1+2)\bmod 3=0
$$

The next phase is **0**. Because this predicted phase adds zero, the cumulative total stays at **`S = 18`**.

### Step 2 — Predict the outer state

The leftmost ciphertext column is 25, so the 90° selector chooses **`L(25,25)`**. Its rotated absolute position is:

$$
m=27(25-1)+28-25=651
$$

The factorization is **`651 = 3 × 7 × 31`**, giving **`μ(651) = −1`**. This also satisfies the Reflected-mode sign restriction.

Starting from `a = 0`, the outer-state update yields:

$$
a_{\mathrm{next}}=(0-1)\bmod 2=1
$$

### Step 3 — Recover the complete signature

The phase is 0 and the outer state is 1. Therefore the central component is also +1:

$$
b_{\mathrm{next}}=(0-2)\bmod 3=1
$$

The full prediction is:

$$
\boxed{\sigma(K_{\mathrm{next}})=(+1,+1,+1)}
$$

**Next-key phase: 0. Next-key Möbius signature: `(+1,+1,+1)`.**

The arithmetic for the current `THEN` ciphertext is directly checkable. The **next-key signature** is a prediction to apply to the continuation, not an independently established next key. In particular, this signature alone does **not** uniquely specify the three rune indices or a plaintext word.


### The THE realization used in the candidate continuation

The candidate **THE KEY IS TO GO** begins with ciphertext **J(22,21) → W(21,20)**. Its original key node is the vertical mirror:

$$
\mathrm{N}(17,17)\;–\;\mathrm{M}(20,17)\;–\;\mathrm{N}(23,17).
$$

The center transforms by φ(M = 19) = 18 = E, giving **N–E–N**, with indices **(9,18,9)**. Its signature is **(+1,+1,+1)** and its phase is **0**, matching the prediction from THEN. Subtracting N–E from J–W modulo 29 gives **TH–E**.

### Signature checks through THE KEY IS TO GO

The same rules are kept fixed for all five candidate transitions. Every row uses the current block's ciphertext and the incoming cumulative total S.

| Candidate transition | S before | Reflected Σμ | Current selected m / μ(m) | Predicted next phase | Predicted next signature | S after |
|---|---:|---:|---|---:|---|---:|
| THEN → THE | 18 | 2 | 651 / −1 | 0 | (+1,+1,+1) | 18 |
| THE → KEY | 18 | 0 | 520 / 0 | 1 | (+1,−1,+1) | 19 |
| KEY → IS | 19 | 0 | 88 / 0 | 1 | (+1,−1,+1) | 20 |
| IS → TO | 20 | -1 | 144 / 0 | 0 | (+1,+1,+1) | 20 |
| TO → GO | 20 | -1 | 424 / 0 | 0 | (+1,+1,+1) | 20 |

Each predicted signature matches its selected derived key: **N–E–N, TH–R–TH, W–R–W, X–E–X, TH–TH–TH**. After THEN changes the outer state from 0 to 1, it remains 1 through these five keys. All five candidate blocks use **Reflected/+1**, with S between **18 and 20**.

These are five conditional consistency checks of a candidate found using the constraints. They are separate from the 16-transition historical fit and do not establish a unique key, route, or plaintext.
---

## Formula Reference

These are the complete operations needed to reproduce the signature prediction, given the **current ciphertext coordinates**, the current outer state, and the running total $S$.

**1 · Convert a grid cell to its absolute position.**

$$
n(r,c)=27(r-1)+c
$$

**2 · Select the phase mode.** Use the running total **before** the transition:

- `0 ≤ S < 7` → **Direct/+1**, with `U(n) = n` and `δ = 1`.
- `7 ≤ S < 14` → **Reflected/+0**, with `U(n) = 730 − n` and `δ = 0`.
- `14 ≤ S < 21` → **Reflected/+1**, with `U(n) = 730 − n` and `δ = 1`.
- `21 ≤ S < 28` → **Direct/+0**, with `U(n) = n` and `δ = 0` (**untested**).

**3 · Predict the phase from all current ciphertext positions.**

$$
p_{\mathrm{next}}=\left(\delta+\sum_{n\in C}\mu(U(n))\right)\bmod 3
$$

**4 · Select the smallest position after a 90° clockwise rotation.**

$$
m=\min_{(r,c)\in C}\bigl(27(c-1)+28-r\bigr)
$$

**5 · Update the outer signature state.**

$$
a_{\mathrm{next}}=(a+\mu(m))\bmod 2
$$

**6 · Obtain the center and complete signature.** Convert the center's residue `0 → 0`, `1 → +1`, `2 → −1`.

$$
b_{\mathrm{next}}\equiv p_{\mathrm{next}}-2a_{\mathrm{next}}\pmod 3
$$

$$
\sigma_{\mathrm{next}}=(a_{\mathrm{next}},b_{\mathrm{next}},a_{\mathrm{next}})
$$

**7 · Carry the phase total forward.**

$$
S_{\mathrm{next}}=S+p_{\mathrm{next}}
$$

The recursion starts at **`S = 0`** and **`a = 0`**, determined by the first recorded key. The three observed modes reproduce 16 signatures on the selected route. The proposed fourth mode and a complete repeating cycle remain outside the tested interval.

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). This report consolidates the project's phase-cycle, rotated-cell selector, and complete next-key signature calculations for the selected LP2 pages 0–2 reading.
