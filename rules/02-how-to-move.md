# 02 — How to Move

*Distance + Direction → Next position*

The key gives more than a decryption: its **totient values** can provide distances, and its **phase** helps determine directions in the 27 × 27 matrix.

## 1. Find a distance

Euler's totient, **φ**, can be used once, twice, or on each rune of a key. The resulting numbers appear as movement distances.

| Source | Calculation | Distance |
|:---|:---|:---:|
| Center OE = 22 | φ(22) = 10 | 10 |
| Center J = 11 | φ(11) = 10; φ(10) = 4 | 10 + 4 = 14 |
| Key H–U–H | φ(8), φ(1), φ(8) | (4, 1, 4) |

For WEATHER, **φ(OE) = 10** gives a direct move:

**X(14,4) → RIGHT 10 → NG(14,14)**

A distance alone does not tell us which direction to take—or which available value to use.

## 2. Find a direction

The **coordinate selector** uses the previous key's phase, **p = 0, 1, or 2**, at a position **(r,c)**.

| Step | Formula | Meaning |
|:---|:---|:---|
| Keep the numbers | **Tₚ(r,c) = (φᵖ(r), φᵖ(c))** | Apply φ to row and column **p times** |
| Get the signs | **Vₚ(r,c) = (μ(φᵖ(r)), μ(φᵖ(c)))** | Apply Möbius μ to both numbers |

Here **φ⁰(n) = n**: phase 0 uses the original coordinates. Rows increase downward; columns increase to the right.

| Sign | Row | Column |
|:---:|:---:|:---:|
| −1 | UP | LEFT |
| +1 | DOWN | RIGHT |
| 0 | No direction | No direction |

**Example — after WEATHER: A(14,19), phase 2**

| Coordinate | Two totients | Möbius | Direction |
|:---|:---|:---|:---|
| Row 14 | 14 → 6 → 2 | μ(2) = −1 | UP |
| Column 19 | 19 → 18 → 6 | μ(6) = +1 | RIGHT |

**T₂(14,19) = (2,6) → V₂(14,19) = (−1,+1) → UP + RIGHT**

The WEATHER key contains **I = 10**, and **φ(I) = 4**. These inherited distances, together with the directions, help locate the TURNS key structure:

| Move | From | To |
|:---|:---|:---|
| RIGHT 4 | A(14,19) | NG(14,23) |
| UP 10 | NG(14,23) | H(4,23) |

The matching C(24,23), **10 below NG**, completes the vertical H–NG–C structure.

The same point can give different directions under another phase:

**V₀(14,19) = (μ(14), μ(19)) = (+1,−1) → DOWN + LEFT**

That phase is used with distance **φ(NG = 21) = 12** to reach TH(26,19) downward and G(14,7) leftward for COLD.

## 3. When a sign is zero

**Zero means the direction is unresolved—not that the distance is zero.** The number from Tₚ is still available.

At J(19,16), phase 2 gives:

| | Row | Column |
|:---|:---:|:---:|
| T₂ | φ²(19) = 6 | φ²(16) = 4 |
| V₂ | μ(6) = +1 | μ(4) = 0 |

**V₂ = (+1,0)** allows DOWN but gives no horizontal direction. The retained **4** matches the radius of two connected mirrors, F–X–F and J–B–J, in END.

In other transitions, a retained number can match a **center rune's value**, not a radius. For example, after END, the retained 4 matches **R = 4**, the center of I–R–I.

If both signs are zero, **Vₚ = (0,0)**, the selector gives no direction. The route may instead follow connected mirror geometry, as after CRY.

A selector constrains possible movement; it does not yet uniquely determine the next structure, the order of steps, or when a particular distance should be used.
