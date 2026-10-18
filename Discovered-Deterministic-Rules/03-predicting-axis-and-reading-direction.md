# Predicting the Reading Axis

**A Geometric Axis and Direction Report**

*27 × 27 matrix · Four rotations · Möbius axis rule · 270° boundary orientation*

---

Recovering a key does not tell us where the next ciphertext lies or how its runes should be read. The next step is to predict the **shape of the next reading** before using a candidate plaintext to choose between possible paths. In the selected LP2 pages 0–2 route, a calculation involving the current ciphertext's beginning and end, together with the center of its original key node, predicts whether the following ciphertext runs **horizontally, vertically, or diagonally**.

A second calculation supplies the missing sense of travel. The **270° boundary rule** from Report 02 predicts whether the following ciphertext's leftmost cell will be its **beginning or end**. Combining these results greatly narrows the reading direction: the axis identifies the line; the boundary fixes the order along that line, with one remaining distinction for diagonal slopes.

This is the third report in the `deterministic-rules` series. [Report 01](01-next-key-signature.md) predicts the next key's signature. [Report 02](02-leftmost-cell-and-rotations.md) explains the leftmost cell's own Möbius class and its beginning/end role. **This report focuses exclusively on the next ciphertext's axis and reading direction.**

**Contents**

[01. Foundations](#foundations) · [02. Predicting the axis](#predicting-the-axis) · [03. The 270° direction rule](#the-270-direction-rule) · [04. Verification across the route](#verification-across-the-route) · [05. Three worked transitions](#three-worked-transitions) · [06. How the four rotations connect](#how-the-four-rotations-connect) · [07. After THEN](#after-then) · [Formula reference](#formula-reference)

---

## Foundations

### Three inputs from the current ciphertext

The matrix has 27 rows and 27 columns. Coordinates are **one-based**: `(1,1)` is the upper-left cell, rows increase **downward**, and columns increase **to the right**. The absolute position of a cell is:

$$
n(r,c)=27(r-1)+c
$$

For each *current* ciphertext block, keep three distinct geometric inputs:

- **`B` — beginning:** the **first cell read** in the current ciphertext.
- **`E` — endpoint:** the **last cell read** in the current ciphertext.
- **`M` — original node center:** the coordinate of the center cell of the **original three-rune structure supplying the current key**, before its center rune is transformed by Euler's totient function.

The **coordinate** of `M`, rather than its rune index, enters the axis formula. The rune index of the original center is a separate input, called **`h`**, for the 270° boundary formula. Keeping `M` and `h` separate prevents two different types of information from being mixed.

### The four rotations

Let `R` mean a **90° clockwise** turn about the center of the matrix. Its four orientations are:

**0° — original coordinates**

$$
R^0(r,c)=(r,c)
$$

**90° clockwise**

$$
R(r,c)=(c,28-r)
$$

**180° clockwise**

$$
R^2(r,c)=(28-r,28-c)
$$

**270° clockwise**

$$
R^3(r,c)=(28-c,r)
$$

Their absolute positions are denoted by $n_0$, $n_1$, $n_2$, and $n_3$, respectively:

$$
n_0(r,c)=27(r-1)+c
$$

$$
n_1(r,c)=27(c-1)+28-r
$$

$$
n_2(r,c)=730-n_0(r,c)
$$

$$
n_3(r,c)=27(27-c)+r
$$

Two exact identities tie the opposite orientations together:

$$
n_0+n_2=730
$$

$$
n_1+n_3=730
$$

The constant **730** is `27² + 1`. Each rotation therefore acts on the same underlying cell, but supplies a different numerical view of it.

---

## Predicting the Axis

### Two Möbius terms, one output

The next-axis rule combines **the reflected beginning**, **the original node center**, and **two rotated views of the endpoint**. First calculate:

$$
A=n_2(B)+n_0(M)
$$

The first term reflects the beginning of the ciphertext through the matrix center (180°); the second adds the original absolute position of its key-node center.

Next calculate:

$$
G=\gcd\bigl(n_1(E),n_2(E)\bigr)
$$

Here `gcd` means **greatest common divisor**. The endpoint is examined after **90°** and **180°** rotations, and the shared divisor of those two absolute positions is retained.

Finally, apply the Möbius function separately to both integers and add the signs:

$$
\boxed{q_{\mathrm{axis}}=\mu(A)+\mu(G)}
$$

**Interpret the sign of the result:**

- **`q = 0` — HORIZONTAL.** The next block follows a row.
- **`q > 0` — VERTICAL.** The next block follows a column.
- **`q < 0` — DIAGONAL.** The next block follows a diagonal.

Each Möbius value is `−1`, `0`, or `+1`, so the combined result can only be `−2`, `−1`, `0`, `+1`, or `+2`. It is the **sign of the sum**, not its magnitude, that determines the predicted axis.

### What the calculation does not change

The addition producing `A` is **ordinary integer addition**. Its result may be larger than 729, because it is an arithmetic input to $\mu$ rather than another matrix coordinate. There is **no reduction modulo 29 or 729**. Similarly, `G` is an ordinary greatest common divisor of two rotated absolute positions, not a distance measured along a row or column.

The formula uses the **current block's** beginning, endpoint, and original key node. It does not require the following block's coordinates to predict its axis. Selecting which original node counts as `M` must, however, be fixed consistently: different nodes can produce the same derived key but different axis predictions.

---

## The 270° Direction Rule

### Predict which boundary the leftmost cell occupies

The axis calculation answers **which line** the next ciphertext follows, but not yet **which way along that line** its runes are read. Report 02 supplies a second prediction using the current endpoint `E` and the **rune index** `h` of its original node center:

$$
\boxed{\tau_{\mathrm{next}}=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod 2}
$$

Here $n_3(E)$ is the absolute position after **270° clockwise**, and $\varphi$ is Euler's totient function. The output is a binary reading-boundary label:

- **`τ = 1` — BEGINNING.** The next ciphertext's leftmost cell is read **first**.
- **`τ = 0` — END.** The next ciphertext's leftmost cell is read **last**.

The **leftmost cell** means the cell with the smallest occupied column; if several cells share that column, use the **bottommost** one. This convention is geometric and does not depend on the reading order. For the straight-line target blocks tested here, the selected cell is at a reading boundary.

### Turn an axis into an oriented reading

Once the next axis and boundary label have been predicted, the direction is constrained as follows.

**Horizontal axis**

- **BEGINNING** → read **right** (`→`).
- **END** → read **left** (`←`).

**Vertical axis**

Because the bottommost cell is chosen when the column is tied:

- **BEGINNING** → read **up** (`↑`).
- **END** → read **down** (`↓`).

**Diagonal axis**

- **BEGINNING** → read toward the **right**: either **up-right** (`↗`) or **down-right** (`↘`).
- **END** → read toward the **left**: either **up-left** (`↖`) or **down-left** (`↙`).

The distinction matters. **Axis + leftmost boundary fixes a unique direction for horizontal and vertical paths.** For a diagonal it fixes the **left/right component**, but the **up/down slope** still depends on the actual diagonal geometry. After candidate cells are located, that final distinction is immediate from their coordinates; it is not a separate result of the 270° formula.

### Why the two predictions complement each other

The **axis rule** relies on `B`, `E`, and the spatial coordinate `M`. The **boundary rule** relies on `E` and the original center rune's index `h`. They constrain different questions about the same next block: first, the orientation of its line; second, its ordering along that line. Neither needs a proposed plaintext word as a numerical input.

---

## Verification Across the Route

### Reading the checks

The following checks cover the **16 recorded transitions from `AS I GO THE → WEATHER` through `SOON → THEN`**, plus the explored **`THEN → THE`** continuation. Each item records the two Möbius terms that give the axis score, followed by the boundary role from the 270° rule and the observed direction of the following block.

The numerical inputs come from the selected ciphertext endpoints and original key-node centers. **For `SOON`, the axis calculation uses `C(25,7)` as the center of the original `L–C–EA` node.** Other documented nodes yield the same derived key but not necessarily the same value of $q_{\mathrm{axis}}$; this choice is therefore part of the verification input.

### Direct/+1 — seven recorded transitions

1. **`AS I GO THE → WEATHER`** — `μ(717) + μ(5) = +1 − 1 = 0` → **horizontal**; leftmost **BEGINNING** → **right**.
2. **`WEATHER → TURNS`** — `μ(721) + μ(1) = +1 + 1 = +2` → **vertical**; **BEGINNING** → **up**.
3. **`TURNS → COLD`** — `μ(734) + μ(36) = +1 + 0 = +1` → **vertical**; **BEGINNING** → **up**.
4. **`COLD → I MAY`** — `μ(1066) + μ(1) = −1 + 1 = 0` → **horizontal**; **END** → **left**.
5. **`I MAY → CRY`** — `μ(422) + μ(1) = +1 + 1 = +2` → **vertical**; **BEGINNING** → **up**.
6. **`CRY → NOW THE`** — `μ(892) + μ(2) = 0 − 1 = −1` → **diagonal**; **BEGINNING** → **down-right** on the recorded slope.
7. **`NOW THE → IDEA`** — `μ(946) + μ(2) = −1 − 1 = −2` → **diagonal**; **END** → **down-left** on the recorded slope.

### Reflected/+0 — five recorded transitions

8. **`IDEA → OF`** — `μ(618) + μ(10) = −1 + 1 = 0` → **horizontal**; **BEGINNING** → **right**.
9. **`OF → THE`** — `μ(706) + μ(5) = +1 − 1 = 0` → **horizontal**; **END** → **left**.
10. **`THE → END`** — `μ(729) + μ(6) = 0 + 1 = +1` → **vertical**; **END** → **down**.
11. **`END → IS`** — `μ(827) + μ(1) = −1 + 1 = 0` → **horizontal**; **BEGINNING** → **right**.
12. **`IS → DEATH`** — `μ(743) + μ(10) = −1 + 1 = 0` → **horizontal**; **END** → **left**.

### Reflected/+1 — four recorded transitions

13. **`DEATH → SEE`** — `μ(658) + μ(2) = −1 − 1 = −2` → **diagonal**; **END** → **down-left** on the recorded slope.
14. **`SEE → YOU`** — `μ(720) + μ(2) = 0 − 1 = −1` → **diagonal**; **END** → **up-left** on the recorded slope.
15. **`YOU → SOON`** — `μ(431) + μ(6) = −1 + 1 = 0` → **horizontal**; **BEGINNING** → **right**.
16. **`SOON → THEN`** — `μ(721) + μ(3) = +1 − 1 = 0` → **horizontal**; **BEGINNING** → **right**, using the selected `C(25,7)` node.

### Explored continuation — THEN → THE

17. **`THEN → THE`** — `μ(754) + μ(5) = −1 − 1 = −2` → **diagonal**; **END** → **leftward**, specifically **up-left** on the selected `L–L` candidate.

The axis result matches **all 16 recorded transitions on the fixed primary route**. Including the explored `THEN → THE` candidate gives **17/17 axis matches on that extended route**. The preceding 270° rule independently reproduces the **BEGINNING/END** label on the 16 recorded transitions; the proposed `THE` also matches its subsequent END prediction. These figures refer to a chosen reading route with specified original nodes, not to a unique selection of every ciphertext from the full matrix.

---

## Three Worked Transitions

### 1. WEATHER → TURNS — vertical, upward

The current ciphertext **WEATHER** begins at `NG(14,14)` and ends at `E(14,18)`. Its original key node is centered on `OE(14,5)`.

For the reflected beginning and original center:

$$
A=n_2(14,14)+n_0(14,5)=365+356=721
$$

For the two rotated endpoint positions:

$$
G=\gcd(473,361)=1
$$

Both Möbius values are +1:

$$
q_{\mathrm{axis}}=\mu(721)+\mu(1)=2
$$

The following ciphertext therefore has a **vertical** axis. The 270° calculation for the current endpoint and original center rune `OE = 22` predicts **BEGINNING**:

$$
\tau_{\mathrm{next}}=[\mu(257)+\varphi(22)]\bmod 2=1
$$

For a vertical block, the leftmost tie-break selects the bottommost cell. When that cell is the beginning, the reading goes **up**. The recorded TURNS ciphertext begins at `A(14,19)` and ends at `W(10,19)`, following precisely this direction.

### 2. COLD → I MAY — horizontal, leftward

The current block **COLD** begins at `G(14,7)` and ends at `A(11,7)`. Its original node is centered on `TH(26,19)`.

The two axis inputs are:

$$
A=n_2(14,7)+n_0(26,19)=372+694=1066
$$

$$
G=\gcd(179,453)=1
$$

Consequently:

$$
q_{\mathrm{axis}}=\mu(1066)+\mu(1)=-1+1=0
$$

The following ciphertext is **horizontal**. The original center rune is `TH = 2`, so $\varphi(2)=1$ contributes an odd correction to the 270° boundary formula:

$$
\tau_{\mathrm{next}}=[\mu(551)+1]\bmod 2=0
$$

The leftmost cell must be the **END**, so a horizontal ciphertext is read **leftward**. The recorded I MAY block follows `TH(26,19) → G(26,18) → T(26,17) → E(26,16)`, ending at its leftmost cell.

### 3. THEN → THE — diagonal, leftward

The current ciphertext **THEN** begins at `L(25,25)` and ends at `W(25,27)`. Its original key node is centered on `IA(26,22)`.

The reflected beginning and original center give:

$$
A=n_2(25,25)+n_0(26,22)=57+697=754
$$

The rotated endpoint positions give:

$$
G=\gcd(705,55)=5
$$

Both terms are negative:

$$
q_{\mathrm{axis}}=\mu(754)+\mu(5)=-1-1=-2
$$

**The predicted next axis is diagonal.** The 270° rule uses `n₃(W(25,27)) = 25` and original center rune `IA = 27`:

$$
\tau_{\mathrm{next}}=[\mu(25)+\varphi(27)]\bmod 2=0
$$

The following ciphertext's **leftmost cell should be its END**. Together, the two predictions constrain the continuation to a **leftward-reading diagonal** (`↖` or `↙`). The explored THE candidate runs from `L(24,27)` to `L(23,26)`, making its leftmost cell the endpoint and selecting **up-left** (`↖`) through its actual coordinates.

---

## How the Four Rotations Connect

The axis formula and boundary formula do not introduce four unrelated coordinate tricks. They use four orientations of the **same 27 × 27 cell numbering**.

- **`R⁰` (0°)** contributes the original absolute position of the key-node center, $n_0(M)$, to the axis calculation.
- **`R¹` (90°)** contributes the endpoint position $n_1(E)$ to the greatest-common-divisor term. Separately, in Reports 01 and 02, the minimum 90° position identifies the leftmost cell.
- **`R²` (180°)** contributes the reflected beginning $n_2(B)$ and endpoint $n_2(E)$ to the axis formula. In Report 01, reflected positions also drive the Reflected next-key phase mode.
- **`R³` (270°)** contributes $n_3(E)$ to the next **BEGINNING/END** prediction.

The complementary identities $n_0+n_2=730$ and $n_1+n_3=730$ show why these positions form a closed rotational system. The connections between the coordinates are exact; the assignment of the Möbius score's signs to the three axes is the empirical rule examined on the recorded route.

**Putting the reports together:** Report 01 predicts a numerical **next-key signature**; Report 02 predicts the **leftmost cell's boundary role** and its allowed Möbius class; Report 03 predicts the **next ciphertext's axis** and uses the boundary role to orient its reading. These are successive constraints on a candidate, not a substitute for locating its cells and deriving its key.

---

## After THEN

The calculations now provide three concrete properties of the explored continuation following `THEN`:

1. **Next-key signature:** `(+1,+1,+1)` with phase **0** (Report 01).
2. **Next ciphertext axis:** **DIAGONAL**, since the axis score is **−2** (this report).
3. **Next leftmost-cell boundary:** **END**, since the 270° boundary result is **0** (Report 02).

These fix a **diagonal reading toward the left**. In the selected candidate **THE**, the two ciphertext cells are `L(24,27) → L(23,26)`, giving the actual **up-left** slope. Its leftmost cell, `L(23,26)`, is the endpoint, as predicted; its 90°-rotated Möbius value is **0**, which also satisfies the Reflected-mode leftmost-cell condition from Report 02.

The result is a coherent set of constraints on this candidate. **The axis and boundary equations alone do not distinguish up-left from down-left diagonals or locate the unique next plaintext.** Their value is that they reject incompatible axes and boundary orientations before further geometric and decryption checks.

---

## Formula Reference

All cell coordinates are **one-based**. `B` and `E` are the current ciphertext's **first and last read cells**; `M` is its original key-node center **coordinate**; `h` is that center's original **rune index**.

**1 · Absolute cell position**

$$
n_0(r,c)=27(r-1)+c
$$

**2 · Rotated absolute positions**

$$
n_1(r,c)=27(c-1)+28-r
$$

$$
n_2(r,c)=730-n_0(r,c)
$$

$$
n_3(r,c)=27(27-c)+r
$$

**3 · Predict the next ciphertext axis**

$$
A=n_2(B)+n_0(M)
$$

$$
G=\gcd\bigl(n_1(E),n_2(E)\bigr)
$$

$$
\boxed{q_{\mathrm{axis}}=\mu(A)+\mu(G)}
$$

**Interpretation:** `0 = HORIZONTAL`, `positive = VERTICAL`, `negative = DIAGONAL`.

**4 · Predict the next leftmost-cell boundary**

$$
\boxed{\tau_{\mathrm{next}}=[\mu(n_3(E))+\varphi(h)]\bmod 2}
$$

**Interpretation:** `1 = BEGINNING`, `0 = END`.

**5 · Convert boundary into reading direction**

- **Horizontal:** BEGINNING → `→`; END → `←`.
- **Vertical:** BEGINNING → `↑`; END → `↓`.
- **Diagonal:** BEGINNING → `↗ / ↘`; END → `↖ / ↙`. The slope is resolved using the selected cells.

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). The checks use the selected LP2 pages 0–2 reading, with `OF` and `THE` treated as separate blocks, the primary `SOON` ciphertext and its `L–C–EA` original node, and an additional examined `THEN → THE` continuation.
