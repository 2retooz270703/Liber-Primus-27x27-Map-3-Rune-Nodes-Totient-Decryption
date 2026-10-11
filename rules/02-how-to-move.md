# 02 — How to Move

*Distance → Direction → Next position*

The key's totient values can provide movement distances. Its phase determines how the current coordinates are read.

## 1. Find the distance

Euler's totient φ(n) can supply a distance in several ways:

| Source | Calculation | Distance |
|:---|:---|:---:|
| Center OE = 22 | φ(22) = 10 | 10 |
| Center J = 11 | φ(11) + φ²(11) = 10 + 4 | 14 |
| Key H–U–H | φ(8), φ(1), φ(8) | (4, 1, 4) |

For WEATHER, the center OE gives **φ(22) = 10**:

**X(14,4) → RIGHT 10 → NG(14,14)**

These calculations provide possible distances. They do not, by themselves, choose which distance or direction to use.

## 2. Find the direction

Use the previous key's phase **p = 0, 1, or 2** at the current position **(r,c)**. Apply φ to each coordinate *p* times, then apply the Möbius function μ.

| Layer | Formula | What it gives |
|:---|:---|:---|
| Numbers | Tₚ(r,c) = (φᵖ(r), φᵖ(c)) | The values before μ |
| Signs | Vₚ(r,c) = (μ(φᵖ(r)), μ(φᵖ(c))) | The directions |

Here φ⁰(n) = n, so phase 0 uses the coordinates unchanged.

| Sign | Row | Column |
|:---:|:---:|:---:|
| −1 | UP | LEFT |
| +1 | DOWN | RIGHT |
| 0 | Unresolved | Unresolved |

**Example — A(14,19), phase 2 (after WEATHER)**

| | Row 14 | Column 19 |
|:---|:---:|:---:|
| Apply φ twice | 14 → 6 → 2 | 19 → 18 → 6 |
| Apply μ | μ(2) = −1 | μ(6) = +1 |
| Direction | UP | RIGHT |

**V₂(14,19) = (−1,+1) → UP + RIGHT**

The inherited distances **4** and **10** help locate the TURNS key structure:

| Move | Result |
|:---|:---|
| RIGHT 4 | A(14,19) → NG(14,23) |
| UP 10 | NG(14,23) → H(4,23) |

C(24,23), ten cells below NG, completes **H–NG–C**. That downward branch completes the structure; it is not selected by V₂.

The same point gives a different result under phase 0:

**V₀(14,19) = (μ(14), μ(19)) = (+1,−1) → DOWN + LEFT**

With **φ(NG = 21) = 12**, these directions reach TH(26,19) and G(14,7) for COLD.

## 3. When a sign is zero

A zero means **no direction is given on that axis**. The number before μ is still available.

**Example — J(19,16), phase 2 (before END)**

| | Row 19 | Column 16 |
|:---|:---:|:---:|
| Apply φ twice | 19 → 18 → 6 | 16 → 8 → 4 |
| Apply μ | μ(6) = +1 | μ(4) = 0 |

**T₂(19,16) = (6,4) → V₂(19,16) = (+1,0)**

The selector allows DOWN but gives no horizontal direction. The retained **4** matches the radius of two connected mirrors, **F–X–F** and **J–B–J**.

A retained value need not be a radius. After END, **φ²(21) = 4** matches **R = 4**, the center of **I–R–I**.

If both signs are zero, **Vₚ = (0,0)**, neither direction is selected. After CRY, the route instead follows connected mirror geometry.

The selector constrains possible movement. It does not yet uniquely choose the next structure, the order of moves, or which available distance becomes active.
