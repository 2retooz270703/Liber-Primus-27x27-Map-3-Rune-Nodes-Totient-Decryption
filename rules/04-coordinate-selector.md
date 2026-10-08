# 04 — Coordinate Selector

Totient movement explains **how far** the route travels, but a distance alone cannot tell us whether to move up, down, left, or right. The **coordinate selector** supplies that missing directional information by applying Euler's totient function `φ` and the Möbius function `μ` to the current grid coordinates.

Its central idea is that **the phase already calculated for the key is reused for the coordinates**. No second phase needs to be chosen. The calculation below builds on [`02-key-phase-selection.md`](./02-key-phase-selection.md) and the movement distances in [`03-totient-movement.md`](./03-totient-movement.md).

## 1. From key phase to coordinate signs

A grid position is written as `P=(r,c)`, where `r` is the row and `c` is the column. The active key has already supplied a phase `p`, equal to **0, 1, or 2**. For either coordinate `n`, define three arithmetic layers:

```text
σ₀(n) = μ(n)
σ₁(n) = μ(φ(n))
σ₂(n) = μ(φ(φ(n))) = μ(φ²(n))
```

Here `φ⁰(n)=n`, so phase 0 applies Möbius directly; phase 1 applies one totient first; and phase 2 applies two successive totients. The Möbius function always returns **−1, 0, or +1** for these positive integer inputs.

Apply the layer selected by the key phase to **both** coordinates:

```text
Vₚ(r,c) = (σₚ(r), σₚ(c))
        = (μ(φᵖ(r)), μ(φᵖ(c)))
```

The result is a pair of signs. The first sign belongs to the **row**, the second to the **column**. The calculation uses the numerical coordinates themselves, not the rune values occupying those cells.

## 2. Reading the signs as directions

Rows increase downward and columns increase to the right. Therefore the two signs have a fixed geometric meaning:

| Component | `−1` | `+1` | `0` |
|---|---|---|---|
| Row | UP | DOWN | No vertical direction supplied |
| Column | LEFT | RIGHT | No horizontal direction supplied |

For example, `Vₚ(r,c)=(-1,+1)` selects **UP + RIGHT**, while `(+1,-1)` selects **DOWN + LEFT**. Similarly, `(+1,+1)` means **DOWN + RIGHT**, and `(-1,-1)` means **UP + LEFT**.

These signs specify **orientation, not distance or step order**. The distances must already be available from the totient chain, and the geometry determines where those distances are applied. A zero is not an instruction to move zero cells: it means this arithmetic layer has not resolved that direction.

## 3. WEATHER → TURNS: phase 2 selects UP + RIGHT

After [`02-WEATHER.md`](../plaintext-i-found/02-WEATHER.md), the route reaches the crossroads **A(14,19)**. The preceding `X-I-X` key has phase **2**, so we apply the double-totient layer to row 14 and column 19.

For the row:

```text
14 → φ(14)=6 → φ(6)=2 → μ(2)=-1
```

For the column:

```text
19 → φ(19)=18 → φ(18)=6 → μ(6)=+1
```

Combining the two signs gives:

```text
V₂(14,19) = (-1,+1)
           = UP + RIGHT
```

The movement values **10** and **4** are already active from the earlier totient chain. In [`03-TURNS.md`](../plaintext-i-found/03-TURNS.md), **RIGHT 4** takes the route from the crossroads to `NG(14,23)`. From that `NG` center, **UP 10** locates `H(4,23)`; the matching **DOWN 10** locates `C(24,23)` and completes the vertical `H-NG-C` structure:

```text
A(14,19)  → RIGHT 4 → NG(14,23)
NG(14,23) → UP 10    → H(4,23)
NG(14,23) → DOWN 10  → C(24,23)  [opposite mirror outer]
```

The selector's two signs agree with the **rightward and upward branches** used to locate this key. The downward branch is the complementary outer of the same centered structure, not a new direction selected by `V₂`.

## 4. The same crossroads changes direction for COLD

The coordinate **A(14,19)** appears again in the next transition, but the active phase is now **0**. Phase 0 applies Möbius directly to each coordinate:

```text
μ(14) = +1     (14 = 2 × 7)
μ(19) = -1     (19 is prime)

V₀(14,19) = (+1,-1)
           = DOWN + LEFT
```

The key center `NG=21` supplies the new movement value `φ(21)=12`. The two directional branches now become:

```text
A(14,19) → DOWN 12 → TH(26,19)
A(14,19) → LEFT 12 → G(14,7)
```

The first destination is the center of `H-TH-H`, which produces the **COLD** key; the second begins its ciphertext. Both are documented in [`04-COLD.md`](../plaintext-i-found/04-COLD.md).

This comparison is especially informative: **the same coordinates produce different directions under different phases**.

```text
A(14,19), p=2 → (-1,+1) → UP + RIGHT
A(14,19), p=0 → (+1,-1) → DOWN + LEFT
```

The direction is therefore not a permanent arrow attached to a cell. It depends on the key phase entering that part of the route.

## 5. COLD → I MAY: phase 1 selects DOWN + RIGHT

[`04-COLD.md`](../plaintext-i-found/04-COLD.md) ends at **A(11,7)**. The `H-U-H` key has phase **1**, so each coordinate receives one totient transformation before Möbius:

```text
Row:    11 → φ(11)=10 → μ(10)=+1
Column:  7 → φ(7)=6   → μ(6)=+1

V₁(11,7) = (+1,+1)
           = DOWN + RIGHT
```

The inherited key signature `(4,1,4)` supplies the distances **4** and **1**. Together with the selector's directions, these give the following exact route:

```text
A(11,7) → DOWN 4  → S(15,7)
S(15,7) → RIGHT 1 → B(15,8)
```

The destination `B(15,8)` is the center of `NG-B-NG`, the structure that generates the key for [`05-I-MAY.md`](../plaintext-i-found/05-I-MAY.md). Again, **the signature determines the magnitudes, while the selector determines their directions**.

## 6. When the selector is incomplete

A selector is **complete** when both components are nonzero, as in the three cases above. It is **partial** when exactly one component is zero, and **null** when both components are zero. These distinctions matter because not every coordinate produces a full direction pair.

**Partial example — after I MAY.** The ciphertext for **I MAY** ends at `E(26,16)` with phase **0**:

```text
V₀(26,16) = (μ(26), μ(16))
           = (+1,0)
```

The row component provides a **DOWN** sign, but the column component supplies nothing. This is **not** enough to specify the next move. The endpoint is already the lower outer of the `E-X-E` mirror, and that local geometry determines how the route enters [`06-CRY.md`](../plaintext-i-found/06-CRY.md). The surviving sign is directional information, not an order to move downward immediately.

**Null example — after CRY.** The final ciphertext cell for **CRY** is `S(17,16)`, where the active phase is **1**:

```text
17 → φ(17)=16 → μ(16)=0
16 → φ(16)=8  → μ(8)=0

V₁(17,16) = (0,0)
```

Neither direction is selected. Here the route continues through the existing **radius-6 mirror geometry**. The endpoint belongs to `S-IA-S`; its `IA(17,10)` center also belongs to `TH-IA-TH`. The inherited distance **6** locates the reachable `TH` outer:

```text
S(17,4)  —6— IA(17,10) —6— S(17,16)
TH(11,16) —6— IA(17,10) —6— TH(23,4)

S(17,16) → UP 6 → TH(11,16)
```

That `TH` starts the ciphertext for [`07-NOW-THE.md`](../plaintext-i-found/07-NOW-THE.md). The selector does not produce **UP** here; the paired mirror structures and inherited radius do.

## 7. What this rule contributes

The coordinate selector adds a directional layer to the same arithmetic already used for the key. **It does not choose a new phase, create movement distances, identify a key on its own, or guarantee a complete direction at every cell.**

When the selector is complete, its signs agree with three recorded transitions: `A(14,19)` under phases 2 and 0, and `A(11,7)` under phase 1. Those examples give concrete checks for **UP + RIGHT**, **DOWN + LEFT**, and **DOWN + RIGHT**. In partial and null cases, the calculation explicitly leaves information unresolved, and the route has to be continued from local geometric constraints.

The strongest conclusion is that **key phase and cell coordinates can jointly constrain orientation**, while totient inheritance supplies distance. The precise way incomplete selectors interact with geometry remains a working part of the route model. A separate question—whether a new structure should be approached through its **CENTER** or an **OUTER** rune—is treated in [`05-center-outer-states.md`](./05-center-outer-states.md).
