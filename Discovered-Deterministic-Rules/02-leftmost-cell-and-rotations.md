# Predicting the Leftmost Cell

**A Rotational Möbius Boundary Report**

*27 × 27 matrix · Leftmost-cell selection · 270° boundary prediction · Four rotations*

---

The next-key signature is not the only property that can be anticipated from a completed ciphertext. The **geometry of the current block** also provides information about the **leftmost cell of the next block**: which numerical class that cell belongs to, and whether it appears at the **beginning or the end** of the next reading.

Two observations connect these questions. First, the leftmost cell of each recorded ciphertext has its **own Möbius value**, calculated from its position after a 90° clockwise turn. That value follows the current **Direct** or **Reflected** geometric mode. Second, a 270° clockwise turn of the **current ciphertext's endpoint**, combined with the totient of its **original key-node center**, predicts whether the next ciphertext's leftmost cell is its first or last cell.

These rules describe distinct properties. The 90° calculation checks the **numerical class of the cell itself**; the 270° calculation predicts its **role in the reading order**. The selected LP2 pages 0–2 route contains **17 ciphertext blocks and 16 recorded transitions**, allowing both properties to be examined directly.

This report focuses only on **leftmost-cell geometry, Möbius membership, and the beginning/end rule**. The separate procedure for predicting the next key's full signature is documented in [Report 01 — Predicting the Next Key](01-next-key-signature.md).

**Contents**

[01. Foundations](#foundations) · [02. The four rotations](#the-four-rotations) · [03. The cell's own Möbius state](#the-cells-own-möbius-state) · [04. Predicting beginning or end](#predicting-beginning-or-end) · [05. Verification across the route](#verification-across-the-route) · [06. The prediction after THEN](#the-prediction-after-then) · [Formula reference](#formula-reference)

---

## Foundations

### The leftmost cell is a geometric object

The matrix is indexed by **one-based coordinates** `(r,c)`: rows increase from top to bottom, and columns increase from left to right. An absolute position is obtained by reading its 27 × 27 cells row by row:

$$
n(r,c)=27(r-1)+c
$$

Thus every cell has a position from **1 to 729**. The function $\mu(n)$ is the ordinary **Möbius function**, whose possible values are `−1`, `0`, and `+1`. A value of zero means the number contains a squared prime factor; a nonzero sign records the parity of its distinct prime factors.

For a ciphertext block $C$, define its **leftmost cell** $L$ as follows:

1. Find the **smallest occupied column** in the block.
2. If several cells occupy that column, choose the **bottommost** one.

This is an unambiguous geometric selection: it does **not** depend on which cell was read first. In the recorded route, this selected leftmost cell also lies at a **reading boundary** — it is either the beginning or the end of its ciphertext.

### Two cells must not be confused

This report repeatedly refers to two different positions:

- **`L` — leftmost cell:** chosen from the entire current ciphertext by the geometric rule above. Its own Möbius state is evaluated after a **90° clockwise** rotation.
- **`E` — endpoint:** the **last cell in the current ciphertext's actual reading order**. It is the input to the **270° clockwise** beginning/end predictor.

Sometimes `L` and `E` are the same physical cell; sometimes they are not. The distinction is essential to reproducing the calculations.

We also use **`h`**, the index of the center rune in the **current original key node, before any totient transformation**. This is not necessarily the center index of the already transformed decryption key.

---

## The Four Rotations

### One operator, four orientations

Let $R$ mean **90° clockwise** about the center of the 27 × 27 matrix. Applying it repeatedly produces a complete cycle:

`R⁰ (0°) → R¹ (90°) → R² (180°) → R³ (270°) → R⁴ = R⁰`

The four coordinate transformations are:

**0° — original orientation**

$$
R^0(r,c)=(r,c)
$$

**90° clockwise — quarter-turn**

$$
R(r,c)=(c,28-r)
$$

**180° — half-turn about the center**

$$
R^2(r,c)=(28-r,28-c)
$$

**270° clockwise — three-quarter-turn**

$$
R^3(r,c)=(28-c,r)
$$

The number **28** follows from the one-based grid width: `27 + 1 = 28`.

### The same rotations as absolute positions

It is not necessary to rotate the physical matrix in order to evaluate a cell. Insert each transformed coordinate into $n(r,c)$.

**Original position:**

$$
n_0(r,c)=27(r-1)+c
$$

**90° position:**

$$
n_1(r,c)=27(c-1)+28-r
$$

**180° position:**

$$
n_2(r,c)=730-n_0(r,c)
$$

**270° position:**

$$
n_3(r,c)=27(27-c)+r
$$

The opposite orientations are paired by an exact numerical relationship:

$$
\boxed{n_0+n_2=730}
$$

$$
\boxed{n_1+n_3=730}
$$

Consequently, the 180° calculation is the **complement of the original position**, while the 270° calculation is the **complement of the 90° position** of the same cell. These are mathematical identities of the 27 × 27 grid, not additional fitted rules.

### One cell seen in all four orientations

Take `W(25,27)`, the final ciphertext cell of **THEN**. The four orientations place it at:

- **0°:** `(25,27)` → absolute position **675**.
- **90°:** `(27,3)` → absolute position **705**.
- **180°:** `(3,1)` → absolute position **55**.
- **270°:** `(1,25)` → absolute position **25**.

The complementary pairs are immediately visible: **675 + 55 = 730** and **705 + 25 = 730**.

### What each orientation contributes

The same four rotations appear in different parts of the proposed reading system, but they do **different jobs**:

- **`R⁰` (0°)** — supplies original absolute positions for the **Direct** next-key phase calculation.
- **`R¹` (90°)** — identifies the leftmost cell through the minimum rotated position; its Möbius value also updates the next key's outer-signature state.
- **`R²` (180°)** — supplies centrally reflected absolute positions for the **Reflected** next-key phase calculation.
- **`R³` (270°)** — acts on the **current endpoint** to predict whether the **next** ciphertext's leftmost cell is the beginning or the end.

This is the common geometry connecting Reports 01 and 02. The quarter-turn and three-quarter-turn are complementary; so are the original and half-turned orientations. Their roles, however, must remain separate.

---

## The Cell's Own Möbius State

### Belonging to its own geometric mode

The leftmost cell of a ciphertext has an individual Möbius state determined **from that cell's own rotated absolute position**. For a block $C$, let:

$$
\boxed{m(C)=\min_{(r,c)\in C}n_1(r,c)}
$$

The corresponding cell is exactly the leftmost/bottommost cell $L$ defined earlier. Its Möbius value is:

$$
\boxed{\mu_L=\mu(m(C))}
$$

In the selected route, **the permitted sign depends on the block's current geometric mode**:

**Direct mode:**

$$
\mu_L\in\{0,+1\}
$$

**Reflected mode:**

$$
\mu_L\in\{0,-1\}
$$

This is the **leftmost cell's own Möbius-class check**. The class belongs to the **current ciphertext's mode**, not to an arbitrary neighboring word or to the next key's rune values. A value of **0** is acceptable in both modes; a positive or negative value distinguishes the classes.

The Direct/Reflected label comes from the phase-cycle regime established in Report 01. It is **not** inferred from the sign when the sign is zero. In the recorded sequence, Direct applies through **NOW THE**; Reflected starts at **IDEA** and continues through **THEN**.

### Worked example — a Direct leftmost cell

For **WEATHER**, the ciphertext occupies row 14, columns 14–18. Its leftmost cell is `NG(14,14)`. After 90° clockwise:

$$
m=27(14-1)+28-14=365
$$

Since `365 = 5 × 73` contains two distinct prime factors:

$$
\mu(365)=+1
$$

The value **+1** belongs to the **Direct** sign class.

### Worked example — a Reflected leftmost cell

For **IDEA**, the cells are read from `J(15,20)` to `D(17,18)`. The leftmost cell is `D(17,18)`:

$$
m=27(18-1)+28-17=470
$$

Because `470 = 2 × 5 × 47` contains three distinct prime factors:

$$
\mu(470)=-1
$$

The value **−1** belongs to the **Reflected** sign class. Here, the leftmost cell also happens to be the **ciphertext endpoint**.

### The full 17-block sign check

Each item below gives the leftmost cell's **90° absolute position** and its own Möbius value. The mode belongs to that **same ciphertext**.

**Direct/+1 — 7 blocks**

- `AS I GO THE` — `m = 14`, **μ = +1**.
- `WEATHER` — `m = 365`, **μ = +1**.
- `TURNS` — `m = 500`, **μ = 0**.
- `COLD` — `m = 176`, **μ = 0**.
- `I MAY` — `m = 407`, **μ = +1**.
- `CRY` — `m = 414`, **μ = 0**.
- `NOW THE` — `m = 422`, **μ = +1**.

**Reflected/+0 — 5 blocks**

- `IDEA` — `m = 470`, **μ = −1**.
- `OF` — `m = 388`, **μ = 0**.
- `THE` — `m = 414`, **μ = 0**.
- `END` — `m = 601`, **μ = −1**.
- `IS` — `m = 223`, **μ = −1**.

**Reflected/+1 — 5 blocks, including THEN**

- `DEATH` — `m = 2`, **μ = −1**.
- `SEE` — `m = 352`, **μ = 0**.
- `YOU` — `m = 408`, **μ = 0**.
- `SOON` — `m = 408`, **μ = 0**.
- `THEN` — `m = 651`, **μ = −1**.

The result is **17/17 blocks within their assigned sign classes**: the 7 Direct blocks contain **four +1 values and three zeros**; the 10 Reflected blocks contain **five −1 values and five zeros**. This is a check on the recorded route. It does not, by itself, identify the next ciphertext's coordinates.

---

## Predicting Beginning or End

### Why the 270° rotation matters

The 90° test examines the **leftmost cell of a block that has already been selected**. The next question is more predictive: **before choosing the following ciphertext, can the current block tell us whether its leftmost cell will be read first or last?**

The recorded beginning/end rule acts on the **current ciphertext's final cell** $E$, using a **270° clockwise** rotation. The second input is the center rune index $h$ of the **current original key node** — the rune at the center *before* any $\varphi$ transformation used to derive the key.

Let $E=(r_E,c_E)$. Its 270°-rotated absolute position is:

$$
n_3(E)=27(27-c_E)+r_E
$$

Then define the predicted next boundary role as:

$$
\boxed{\tau_{\mathrm{next}}=\bigl(\mu(n_3(E))+\varphi(h)\bigr)\bmod 2}
$$

The interpretation is binary:

- **`τ_next = 1` — BEGINNING.** The next block's leftmost cell is its **first ciphertext cell**.
- **`τ_next = 0` — END.** The next block's leftmost cell is its **last ciphertext cell**.

Modulo 2 gives a result of **0 or 1 even when the Möbius value is −1**. The center contribution is $\varphi(h)$, **not** $\mu(\varphi(h))$, and $h$ is taken **before** center-totient key derivation.

### Why the center correction is necessary

In most recorded transitions, $\varphi(h)$ is even. Then it does not change the result modulo 2: a nonzero Möbius value predicts **BEGINNING**, and zero predicts **END**.

Two recorded transitions have **`h = TH = 2`**, for which $\varphi(2)=1$ is odd. In precisely those cases, the center contribution **reverses** the binary result. These cases make the distinction between the full formula and the Möbius-only shortcut visible.

**COLD → I MAY — a predicted END**

`COLD` ends at `A(11,7)`. Its original key node is `H–TH–H`, so `h = 2` and $\varphi(h)=1$. Rotate the endpoint 270°:

$$
n_3(11,7)=27(27-7)+11=551
$$

The number `551 = 19 × 29` is square-free, so $\mu(551)=+1$. Therefore:

$$
\tau_{\mathrm{next}}=(1+1)\bmod 2=0
$$

The leftmost cell of **I MAY** is `E(26,16)`, and it is indeed the **last** cell in the recorded right-to-left reading.

**IDEA → OF — a predicted BEGINNING**

`IDEA` ends at `D(17,18)`. Its original node is `A–TH–A`; again `h = 2`, with $\varphi(h)=1$. The 270° endpoint index is:

$$
n_3(17,18)=27(27-18)+17=260
$$

Because `260 = 2² × 5 × 13`, its Möbius value is **0**. Thus:

$$
\tau_{\mathrm{next}}=(0+1)\bmod 2=1
$$

The leftmost cell of **OF** is `X(18,15)`, which is its **first** ciphertext cell. Without the original-center correction, both this case and `COLD → I MAY` would be predicted incorrectly.

### What the rule predicts — and what it does not

The output **BEGINNING/END** constrains the next block's **reading orientation relative to its leftmost cell**. It does not specify the next block's exact location, direction, length, or plaintext. Those require separate constraints. In particular, a leftmost cell being an **END** does not automatically imply a horizontal right-to-left reading: the recorded route also contains vertical and diagonal examples.

---

## Verification Across the Route

### All 16 beginning/end predictions

The records below use the **last cell of the current ciphertext**, apply its **270° clockwise absolute position**, add the totient of the **original source-node center**, and compare the predicted role with the leftmost cell in the following recorded block.

The compact notation is **`n₃(E) / μ / φ(h) → role`**. The result matches the observed boundary in every listed transition.

**Direct/+1 transitions — 7/7**

1. `AS I GO THE → WEATHER` — `635 / +1 / 10` → **BEGINNING**.
2. `WEATHER → TURNS` — `257 / −1 / 10` → **BEGINNING**.
3. `TURNS → COLD` — `226 / +1 / 12` → **BEGINNING**.
4. `COLD → I MAY` — `551 / +1 / 1` → **END**.
5. `I MAY → CRY` — `323 / +1 / 16` → **BEGINNING**.
6. `CRY → NOW THE` — `314 / +1 / 6` → **BEGINNING**.
7. `NOW THE → IDEA` — `204 / 0 / 10` → **END**.

**Reflected/+0 transitions — 5/5**

8. `IDEA → OF` — `260 / 0 / 1` → **BEGINNING**.
9. `OF → THE` — `315 / 0 / 22` → **END**.
10. `THE → END` — `316 / 0 / 10` → **END**.
11. `END → IS` — `129 / +1 / 16` → **BEGINNING**.
12. `IS → DEATH` — `480 / 0 / 2` → **END**.

**Reflected/+1 transitions — 4/4**

13. `DEATH → SEE` — `728 / 0 / 16` → **END**.
14. `SEE → YOU` — `378 / 0 / 10` → **END**.
15. `YOU → SOON` — `322 / −1 / 2` → **BEGINNING**.
16. `SOON → THEN` — `241 / −1 / 4` → **BEGINNING**.

Across the selected route, the **full 270° formula gives 16/16 beginning/end matches**. Its Möbius-only component gives **14/16**; the two remaining cases are the two original nodes whose center index is `TH = 2`, with odd totient. The result is an exact fit to the recorded transitions, not a claim that every possible alternative reading has been eliminated.

### Why the two checks reinforce each other

The checks constrain **different aspects** of a proposed continuation:

- The **90° rule** asks whether the next candidate's **own leftmost cell** has a Möbius value allowed by the next block's Direct/Reflected mode.
- The **270° rule** asks whether that same leftmost cell occupies the predicted **reading boundary**, using information from the *previous* block's endpoint and original key-node center.

One is a **cell-class condition**; the other is a **boundary-position condition**. Passing both is more informative than passing either alone, although neither check independently determines a unique ciphertext.

---

## The Prediction After THEN

### The 270° boundary calculation

The last recorded ciphertext is **THEN**, occupying row 25, columns 25–27. Its final cell is **`W(25,27)`**. The original key structure has center rune **`IA = 27`**, before the transformation that gives `E = 18`.

The endpoint's 270° coordinate is `(1,25)`; its absolute position is therefore:

$$
n_3(E)=27(27-27)+25=25
$$

Since `25 = 5²`, the Möbius value is **0**. The original center contributes $\varphi(27)=18$, giving:

$$
\tau_{\mathrm{next}}=(0+18)\bmod 2=0
$$

**Prediction: the leftmost cell of the ciphertext after THEN should be its END, not its beginning.** This is a prospective boundary prediction; the 16/16 verification above ends at `SOON → THEN`.

### The companion 90° Möbius condition

`THEN` itself is in **Reflected/+1**. Its own leftmost cell is `L(25,25)`, whose 90° position is **651**:

$$
\mu(651)=\mu(3\times7\times31)=-1
$$

Thus **THEN passes its own Reflected sign check**. For a proposed following ciphertext still in that geometric regime, its new leftmost cell must have a 90° Möbius value in **`{−1, 0}`**.

One explored continuation, **THE**, uses `L(24,27) → L(23,26)`. Its leftmost cell is **`L(23,26)`**, the **last** cell in that reading. For this cell:

$$
n_1(23,26)=680
$$

Since `680 = 2³ × 5 × 17`, $\mu(680)=0$. This candidate therefore satisfies **both** the predicted END role and the Reflected leftmost-cell class. These constraints describe a compatible candidate, not a unique selection among possible continuations.

---

## Formula Reference

The following expressions collect the operations used in this report. All coordinates are **one-based**, $E$ denotes the **current ciphertext's last read cell**, and $h$ is the **original, pre-totient center-rune index**.

**1 · Absolute cell position**

$$
n(r,c)=27(r-1)+c
$$

**2 · Four rotations**

$$
R^0(r,c)=(r,c),\qquad R(r,c)=(c,28-r)
$$

$$
R^2(r,c)=(28-r,28-c),\qquad R^3(r,c)=(28-c,r)
$$

**3 · Opposite-rotation complements**

$$
n_0+n_2=730,\qquad n_1+n_3=730
$$

**4 · Leftmost cell's own Möbius value**

$$
m(C)=\min_{(r,c)\in C}\bigl[27(c-1)+28-r\bigr]
$$

$$
\mu_L=\mu(m(C))
$$

**5 · Mode membership**

**Direct:** $\mu_L\in\{0,+1\}$; **Reflected:** $\mu_L\in\{0,-1\}$.

**6 · Next leftmost cell's beginning/end role**

$$
\boxed{\tau_{\mathrm{next}}=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod 2}
$$

**Interpretation:** `1 = BEGINNING`; `0 = END`.

The essential geometric distinction is simple: **R¹ evaluates the leftmost cell's own Möbius class; R³ evaluates the current endpoint to predict the next leftmost cell's reading boundary.** R⁰ and R² provide the paired Direct/Reflected position systems used in Report 01.

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). Calculations use the selected 17-block plaintext route, treating `OF` and `THE` as separate blocks and using the primary `SOON` reading. The 17/17 sign-class check and 16/16 boundary fit describe that route; they do not independently establish an intended or unique Cicada 3301 decryption.
