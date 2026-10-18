*LIBER PRIMUS II · PAGES 0–2*

# The 27 × 27 Matrix

**A Geometric Decryption Report**

*Three-rune keys · Möbius phases · Coordinate movement · Mirror geometry*

---

The proposed reading of the 27 × 27 matrix begins with a simple distinction: a rune provides a **cipher value**, while the cell containing it provides a **geometric position**. The two types of information can be used together. A three-rune structure supplies a decryption key; number-theoretic functions determine how that key is aligned; and positions in the grid help connect one recovered passage to another.

This report develops that idea as one continuous method rather than as three separate sets of instructions. Each operation is introduced through a concrete example, with the relevant calculation shown alongside its meaning.

> **The central idea:** the proposed plaintext is read through three complementary layers: **decryption** establishes what a selected group of runes says; **movement** investigates where the reading may continue; and **mirror geometry** checks how the chosen cells fit into the larger matrix.

**Contents**

[01. Foundations](#foundations) · [02. Decrypting a passage](#decrypting-a-passage) · [03. Finding the next position](#finding-the-next-position) · [04. Mirror geometry](#mirror-geometry) · [05. Reading the evidence together](#reading-the-evidence-together) · [Formula reference](#formula-reference)

---

## Foundations

### A rune and its coordinate are different inputs

The matrix contains 27 rows and 27 columns. Throughout this report, coordinates are **one-based**: `(1, 1)` is the upper-left cell, rows increase **downward**, and columns increase **to the right**. A label such as `E(14,18)` means that the rune `E` occupies row 14, column 18.

The cipher itself uses a **29-rune alphabet**. Every rune therefore has an index used in modular subtraction. A cell coordinate, by contrast, supplies two numbers that can be processed to suggest movement through the grid.

The same functions appear in different parts of the method, but they act on **three distinct kinds of inputs**:

- **Rune index** — the numerical value used to derive keys and decrypt ciphertext; for example, `OE = 22`.
- **Grid coordinate** — the row and column used to calculate direction and geometric relationships; for example, `A(11,7)`.
- **Three-cell structure** — a spatial arrangement used as a key or a supporting mirror; for example, `X–OE–X`.

### The two arithmetic tools

**Euler's totient function**, $\varphi(n)$, counts the positive integers up to $n$ that are coprime to $n$. In the recorded examples, it transforms rune indices and coordinates into other useful values:

$$
\varphi(22)=10,\qquad \varphi(14)=6.
$$

**The Möbius function**, $\mu(n)$, reduces a positive integer to one of three possible values:

$$
\mu(n)\in\{-1,0,+1\}.
$$

Its meaning is precise: **0** indicates a repeated prime factor; for a square-free integer, **+1** indicates an even number of distinct prime factors and **−1** indicates an odd number.

For example:

$$
\mu(6)=+1,\qquad \mu(4)=0,\qquad \mu(10)=+1.
$$

In this model, $\varphi$ performs a numerical transformation; $\mu$ turns a transformed number into a compact sign. We will use that distinction repeatedly.

---

## Decrypting a Passage

### Step 1 — Derive a three-rune key

A recurring pattern in the selected matrix is a three-rune structure. In many recorded examples, its outer runes remain unchanged while the **center rune is replaced by the rune indexed by its totient**.

Take the structure **`X–OE–X`**. The center rune `OE` has index `22`, and $\varphi(22)=10$ corresponds to `I`. The resulting key is therefore:

$$
\mathrm{X-OE-X}
\quad\xrightarrow{\;\varphi(22)=10\;}\quad
\mathrm{X-I-X}.
$$

In this example, the **left** and **right** runes remain `X`. Only the **center** changes: `OE (22)` becomes `I (10)` through the totient function. Thus the original structure `X–OE–X` yields the key **`X–I–X`**.

For structures that use this center transformation, the numerical form is:

$$
(a,b,c)\longmapsto\bigl(a,\varphi(b),c\bigr).
$$

**Not every three-rune key requires this transformation.** The recorded route also contains non-mirrored structures, such as `H–NG–C`, whose key is used directly. It is important to distinguish a *structure in the matrix* from the *key ultimately used for subtraction*.

### Step 2 — Calculate the key's Möbius signature

A key of three runes has three possible cyclic alignments. The recorded procedure does not choose the starting rune arbitrarily: it calculates a **phase** from the derived key itself.

Let $K=(k_1,k_2,k_3)$ denote the three **rune indices in their unrotated order**. Apply $\varphi$ to each index, then $\mu$ to obtain each component of the **Möbius signature**:

$$
\sigma_i=\mu(\varphi(k_i)),\quad i=1,2,3.
$$

Together, these form the ordered signature **`(σ₁, σ₂, σ₃)`**.

For **`X–I–X`**, the three calculations are:

- **Left:** `X = 14` → φ(14) = 6 → μ(6) = **+1**.
- **Center:** `I = 10` → φ(10) = 4 → μ(4) = **0**.
- **Right:** `X = 14` → φ(14) = 6 → μ(6) = **+1**.

Thus:

$$
\sigma(\mathrm{X-I-X})=(+1,0,+1).
$$

### Step 3 — Turn the signature into a phase

Add the three signature components, then reduce the sum modulo three:

$$
\boxed{p=(\sigma_1+\sigma_2+\sigma_3)\bmod 3}
$$

In the running example:

$$
p=(1+0+1)\bmod 3=2.
$$

The phase tells us how many positions to rotate the **key to the left**, cyclically. The possible alignments are **phase 0:** `X–I–X`; **phase 1:** `I–X–X`; and **phase 2:** **`X–X–I`**. The computed phase is 2, so the third arrangement is used.

The key is therefore read as **`X–X–I`**. This is a *cyclic rotation of the three key elements*, not a physical rotation of the matrix.

The phase specifies the alignment, while the complete signature retains additional information about the numerical structure of the key. Both should be recorded.

### Step 4 — Subtract the aligned key modulo 29

The ciphertext for the recorded **WEATHER** passage occupies **row 14, columns 14–18**:

```text
Ciphertext    NG    P    EO    O    E
Key stream    X     X    I     X    X
```

The phase-aligned key `X–X–I` repeats until it covers all five ciphertext runes. Each rune is then decrypted by subtracting the corresponding key index **modulo 29**:

$$
\boxed{\displaystyle P_j=(C_j-K_j)\bmod 29}
$$

Here $C_j$ is a ciphertext index, $K_j$ is the repeated, aligned key index, and $P_j$ is the resulting plaintext index.

**Rune-by-rune decryption** (all differences are interpreted modulo 29):

1. `NG (21)` − `X (14)` = `7` → **W**
2. `P (13)` − `X (14)` ≡ `28` → **EA**
3. `EO (12)` − `I (10)` = `2` → **TH**
4. `O (3)` − `X (14)` ≡ `18` → **E**
5. `E (18)` − `X (14)` = `4` → **R**

The negative differences wrap around within the 29-rune alphabet. The resulting sequence is:

$$
\mathrm{W\;\cdot\;EA\;\cdot\;TH\;\cdot\;E\;\cdot\;R}
$$

> **Recovered reading — WEATHER**
>
> Five ciphertext runes produce five plaintext runes under the derived key, the calculated phase, and modular subtraction.

The key point is that the English word is obtained only **after** the rune-index calculations. The phase calculation selects an alignment from the key's own arithmetic rather than from the appearance of the resulting English word.

This completes the **decryption** operation for an already selected ciphertext block. It does not yet determine which ciphertext block should be read next.

---

## Finding the Next Position

### Two separate questions: direction and distance

Once a ciphertext block has been read, the recorded route uses the current key and a selected grid cell to investigate the next location. These calculations separate naturally into two parts:

- **Direction:** how the current phase transforms the anchor cell's row and column into signs.
- **Distance:** which totient-derived values are used as movement lengths.

The direction operation has one compact formula. The examples show several ways to obtain distances, but do **not yet specify one universal rule** for selecting them in every case.

### Step 1 — Convert a coordinate into direction signs

Let $(r,c)$ be a chosen anchor cell and let $p\in\{0,1,2\}$ be the phase of the **current** key. Define $\varphi^p$ to mean *apply the totient function exactly $p$ times*; $\varphi^0(n)=n$.

First retain the transformed coordinates:

$$
T_p(r,c)=\bigl(\varphi^p(r),\ \varphi^p(c)\bigr).
$$

Apply $\mu$ to each transformed coordinate to obtain its directional sign:

$$
v_r=\mu(\varphi^p(r)),\qquad v_c=\mu(\varphi^p(c)).
$$

Combine them into the direction vector:

$$
\boxed{V_p(r,c)=(v_r,v_c)}
$$

The coordinate convention translates these signs into directions:

- **−1** means **up** along the row axis and **left** along the column axis.
- **+1** means **down** along the row axis and **right** along the column axis.
- **0** leaves that axis's direction **unspecified**.

A zero is **not necessarily a command to stay still**. It means the sign rule does not determine a direction for that axis. The corresponding pre-Möbius value in $T_p$ can still matter.

**Choosing the anchor:** several recorded checks use the ciphertext endpoint, but not all. For example, `WEATHER` ends at `E(14,18)`, while its following coordinate check uses the neighboring `A(14,19)`. The anchor is therefore part of each recorded transition, not yet a universally fixed choice.

### Step 2 — A complete move: COLD → I MAY

The recorded **COLD** key is `H–U–H`, with indices $(8,1,8)$. Its totient values are:

$$
(\varphi(8),\varphi(1),\varphi(8))=(4,1,4).
$$

Its Möbius signature is $(0,+1,0)$, giving phase $p=1$. In this transition, the values **4** and **1** are used as the movement distances.

The ciphertext ends at **`A(11,7)`**. With phase 1, apply $\varphi$ once to each coordinate and then $\mu$:

$$
\mu(\varphi(11))=\mu(10)=+1
$$

$$
\mu(\varphi(7))=\mu(6)=+1
$$

Both signs are positive: the move goes **down** and **right**. Using distances 4 and 1, respectively:

**Move down four rows:**

$$
(11,7)\longrightarrow(15,7)
$$

**Then move right one column:**

$$
(15,7)\longrightarrow(15,8)
$$

The destination, **`B(15,8)`**, is the center of the next recorded structure: **`NG–B–NG`**.

This is where the arithmetic and the map meet. The phase supplies a direction pair, the current key provides distances for this transition, and the resulting cell is the center of a meaningful three-rune structure.

### Why the distance calculation is kept separate

The recorded route contains other totient-based distance constructions. For the rune `OE = 22`:

$$
\varphi(22)=10
$$

For `J`, the sum of two successive totients is calculated as:

$$
\varphi(\mathrm{J})=10,\qquad\varphi(10)=4
$$

$$
10+4=14
$$

These provide concrete numerical distances in the respective examples. However, the current movement notes do not determine **when to use a single totient value, a pair of values, or a sum** without reference to the recorded route. A correct report should keep that distinction visible.

### Step 3 — Preserve the values when Möbius returns zero

The **END** ciphertext ends at **`I(21,23)`** and has phase $p=2$. Applying $\varphi$ twice gives:

$$
21\xrightarrow{\varphi}12\xrightarrow{\varphi}4
$$

$$
23\xrightarrow{\varphi}22\xrightarrow{\varphi}10
$$

So the two outputs of the coordinate procedure are:

$$
\boxed{T_2(21,23)=(4,10)}
$$

$$
\boxed{V_2(21,23)=(0,+1)}
$$

The column receives a **right** sign. The row receives `0` and thus has no specified direction from this rule. Yet the retained value **4** is the index of the central rune **`R`** in the nearby `I–R–I` mirror.

This explains why the two outputs should not be collapsed into one. $V_p$ contains the directional signs; $T_p$ preserves the numbers from which those signs were produced. Elsewhere in the recorded examples, such a retained number can also match a mirror's radius.

---

## Mirror Geometry

### Recognizing a three-cell mirror

A *mirror* consists of **two identical outer runes** at equal distances on opposite sides of a center. The cells may lie on a row, a column, or a diagonal. The defining feature is spatial symmetry, not a particular reading direction.

Consider the diagonal mirror **`J–D–J`**. Its three cells lie along a diagonal: the **first outer** `J` is at `(15,20)`, the **center** `D` is at `(17,18)`, and the **second outer** `J` is at `(19,16)`.

The coordinate midpoint of the two outer cells is exactly the central cell:

$$
\frac{(15,20)+(19,16)}{2}=(17,18).
$$

Equivalently, the offsets from `D(17,18)` are $(-2,+2)$ and $(+2,-2)$: equal distances in opposite directions.

### Shared cells connect different structures

The mirror system is not made of isolated triples. The **same physical cell** can be the center of one structure and an outer element of another:

- **`J(19,16)`** is the **center** of `OE–J–OE`, but an **outer** cell in both `J–D–J` and `J–B–J`.
- **`R(21,22)`** is the **center** of both `I–R–I` and `H–R–H`.

Such overlaps are geometric connections: the structures share an exact grid position. They are not, by themselves, instructions to follow one branch rather than another, but they provide a concrete way to compare candidate continuations.

### Endpoint role and the current key's signature

The recovered passages **NOW THE** and **IDEA** end at different positions in the *same* `J–D–J` mirror. Their endpoint roles also correspond to different Möbius signatures:

**NOW THE** ends at **`J(15,20)`**, an **outer cell** of `J–D–J`. Its key is `OE–I–OE`; its totient values are `(10,4,10)` and its Möbius signature is **`(+1,0,+1)`**.

**IDEA** ends at **`D(17,18)`**, the **center** of the same `J–D–J` mirror. Its key is `A–U–A`; its totient values are `(8,1,8)` and its Möbius signature is **`(0,+1,0)`**.

The same endpoint-role association occurs in four other recorded passages:

- **COLD** — `(0,+1,0)`; endpoint `A(11,7)` is the **center** of `EA–A–EA`.
- **IS** — `(0,+1,0)`; endpoint `D(21,10)` is the **center** of `E–D–E`.
- **WEATHER** — `(+1,0,+1)`; endpoint `E(14,18)` is an **outer** cell of `E–NG–E`.
- **END** — `(+1,0,+1)`; endpoint `I(21,23)` is an **outer** cell of `I–R–I`.

On this route, the recurring association is:

- **`(0,+1,0)` → center**
- **`(+1,0,+1)` → outer**

This is a useful **cross-check** because the key's numerical signature and the ciphertext endpoint's spatial role are determined by different aspects of the recorded candidate. It does not independently prove that a passage or a mirror was intentionally encoded.

---

## Reading the Evidence Together

The purpose of the three layers is not to make every mathematical coincidence count as a solution. Each layer has a **different job**, and the strongest recorded examples are those in which the layers reinforce one another.

**Decryption — What does this group of runes say?**

The chosen ciphertext and derived key yield a numerical plaintext through a calculated phase and subtraction modulo 29. For example, `NG–P–EO–O–E` becomes **WEATHER** under the aligned `X–X–I` key stream.

**Movement — Where might the reading continue?**

For **COLD → I MAY**, the phase and coordinate signs provide down/right directions. The recorded distances 4 and 1 lead from `A(11,7)` to `B(15,8)`, the center of `NG–B–NG`.

**Mirror geometry — How does that location fit into the map?**

The endings of **NOW THE** and **IDEA** occupy the outer and center positions of the same `J–D–J` mirror, respectively; their key signatures follow the corresponding recorded pattern.

### What the method presently determines

Once a ciphertext block and its derived key are specified, the **key-alignment and modulo-29 decryption arithmetic are reproducible**. The three-rune structures, endpoint coordinates, and their geometric overlaps can likewise be checked directly against the selected map.

The navigation examples do not yet define a single **automatic procedure** for choosing every anchor cell and movement distance. A matching mirror role is additional structural evidence, not a unique selection rule. These boundaries are important because a repeatable decryption operation and a fully specified traversal algorithm are not the same thing.

The broader working hypothesis is that the matrix's plaintext, keys, and geometry form one navigable system. The examples in this report explain how that hypothesis is implemented on the **selected LP2 pages 0–2 route**; they do not independently establish an intended or unique Cicada 3301 solution.

---

## Formula Reference

The following expressions summarize the operations used in the report. **Rune indices** are inputs to the first three rules; **cell coordinates** are inputs to the last two.

**1 · Derive a key** — transform the center *where applicable*.

$$
(a,b,c)\longmapsto\bigl(a,\varphi(b),c\bigr)
$$

**2 · Calculate the signature and phase** — use the derived, unrotated key $K$.

$$
\sigma_i=\mu(\varphi(k_i))
$$

$$
p=(\sigma_1+\sigma_2+\sigma_3)\bmod 3
$$

**3 · Decrypt a ciphertext rune** — repeat the cyclically aligned key.

$$
P_j=(C_j-K_j)\bmod 29
$$

**4 · Preserve the transformed coordinate values.**

$$
T_p(r,c)=\bigl(\varphi^p(r),\varphi^p(c)\bigr)
$$

**5 · Obtain the direction signs.**

$$
v_r=\mu(\varphi^p(r)),\quad v_c=\mu(\varphi^p(c))
$$

$$
V_p(r,c)=(v_r,v_c)
$$

Here $\varphi^p$ denotes **iteration**, not exponentiation, and phase $p$ belongs to the **current block's key** when used for movement.

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). This document consolidates the recorded decryption, coordinate-movement, and mirror observations for the selected LP2 pages 0–2 reading. The separate next-key signature-prediction model is not part of this guide.
