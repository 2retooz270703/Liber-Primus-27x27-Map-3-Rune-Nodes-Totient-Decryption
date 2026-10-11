# 02 — How to Move

*Distance → Direction → Next structure*

Numbers from earlier keys provide possible distances. The current coordinates and the key's phase provide possible directions.

## 1. How far?

Distances come from Euler's totient φ:

| Source | Calculation | Distance |
|:---|:---|:---:|
| OE = 22 | φ(22) = 10 | 10 |
| J = 11 | φ(11) = 10; φ(10) = 4 | 10 + 4 = 14 |
| Key H–U–H | φ(8), φ(1), φ(8) | 4 and 1 |

In WEATHER, the value **10** gives:

**X(14,4) → RIGHT 10 → NG(14,14)**

The distance alone does not determine this route.

## 2. Which way?

Take the current **(row, column)** and the previous key's phase **p**. Apply these operations to each coordinate:

| Phase | Calculation |
|:---:|:---:|
| 0 | μ(n) |
| 1 | μ(φ(n)) |
| 2 | μ(φ(φ(n))) |

Convert the results into directions:

| Result | Row | Column |
|:---:|:---:|:---:|
| −1 | UP | LEFT |
| +1 | DOWN | RIGHT |
| 0 | Not specified | Not specified |

**Example: A(14,19), phase 2**

| | Row 14 | Column 19 |
|:---|:---:|:---:|
| Apply φ twice | 14 → 6 → 2 | 19 → 18 → 6 |
| Apply μ | μ(2) = −1 | μ(6) = +1 |
| Direction | UP | RIGHT |

**V₂(14,19) = (−1,+1) → UP + RIGHT**

For TURNS, the distances **4** and **10** are used:

| Move | From → To |
|:---|:---|
| RIGHT 4 | A(14,19) → NG(14,23) |
| UP 10 | NG(14,23) → H(4,23) |

C(24,23), ten cells below NG, completes **H–NG–C**. The formula did not select DOWN.

At the **same cell**, phase 0 gives:

**V₀(14,19) = (μ(14), μ(19)) = (+1,−1) → DOWN + LEFT**

For COLD, **φ(NG = 21) = 12** leads DOWN 12 to TH(26,19) and LEFT 12 to G(14,7).

## 3. What if the result is zero?

**Zero means no direction, not zero steps.** Keep the number calculated before μ.

**Example: J(19,16), phase 2**

| | Row 19 | Column 16 |
|:---|:---:|:---:|
| Apply φ twice | 19 → 18 → 6 | 16 → 8 → 4 |
| Apply μ | +1 | 0 |

**T₂(19,16) = (6,4)** contains the numbers before μ. **V₂(19,16) = (+1,0)** contains the signs: DOWN, with no horizontal direction. The retained **4** also appears in nearby mirrors:

| Endpoint | Where the retained 4 appears |
|:---|:---|
| J(19,16) · before END | Radius of F–X–F and J–B–J |
| I(21,23) · after END | Center R = 4 of I–R–I |
| E(26,1) · after DEATH | Radius of EA–J–EA |

If both signs are zero, neither direction is selected. After CRY, connected mirrors instead provide the route.

The calculations **constrain** movement; they do not yet uniquely choose a distance, a mirror, or the order of moves.
