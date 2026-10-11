# 02 — How to Move

*Distance → Direction → Next structure*

Totient values from key structures can supply movement distances. After a ciphertext segment ends, its key's phase can also constrain directions at the endpoint or a nearby transition point.

## 1. Find the distance

Euler's totient φ provides numbers that can be reused as movement distances. Sometimes one value is used; sometimes two are combined.

| Source | Calculation | Distance |
|:---|:---|:---:|
| OE = 22 | φ(22) = 10 | 10 |
| J = 11 | φ(11) = 10; φ(10) = 4 | 10 + 4 = 14 |
| Key H–U–H | φ(8), φ(1), φ(8) = (4, 1, 4) | 4 and 1 |

For WEATHER, φ(OE = 22) = 10 matches the distance from the key's outer rune to the ciphertext start:

**X(14,4) → RIGHT 10 → NG(14,14)**

The number gives a distance, but does not tell us which direction to take.

## 2. Find the direction

Use the previous key's phase **p** (0, 1, or 2) at a transition point **(r,c)**, where r is the row and c is the column. Apply the corresponding calculation to each coordinate.

| Phase | Calculation for each coordinate n |
|:---:|:---:|
| 0 | μ(n) |
| 1 | μ(φ(n)) |
| 2 | μ(φ(φ(n))) |

Here μ is the Möbius function from Rule 01. Each result is −1, 0, or +1:

| Result | Row direction | Column direction |
|:---:|:---:|:---:|
| −1 | UP | LEFT |
| +1 | DOWN | RIGHT |
| 0 | Not specified | Not specified |

For example, after WEATHER, the route uses **A(14,19)** with phase 2:

| | Row 14 | Column 19 |
|:---|:---:|:---:|
| Apply φ twice | 14 → 6 → 2 | 19 → 18 → 6 |
| Apply μ | μ(2) = −1 | μ(6) = +1 |
| Direction | UP | RIGHT |

**V₂(14,19) = (−1, +1) → UP + RIGHT**

Using the inherited distances 4 and 10:

**A(14,19) → RIGHT 4 → NG(14,23) → UP 10 → H(4,23)**

The matching C(24,23) is 10 cells below NG, completing H–NG–C. That downward branch comes from the structure, not the selector.

The same point gives a different result under phase 0:

**V₀(14,19) = (μ(14), μ(19)) = (+1, −1) → DOWN + LEFT**

With φ(NG = 21) = 12, DOWN leads to TH(26,19) and LEFT to G(14,7), both used for COLD.

## 3. When the result is zero

A zero means **no direction is specified on that axis**. The number calculated before μ is still available:

**Tₚ(r,c) = (φᵖ(r), φᵖ(c))** — values before μ  
**Vₚ(r,c) = (μ(φᵖ(r)), μ(φᵖ(c)))** — direction signs

Here φᵖ means applying φ p times; phase 0 leaves the coordinate unchanged.

For example, at J(19,16) with phase 2:

| | Row 19 | Column 16 |
|:---|:---:|:---:|
| Apply φ twice | 19 → 18 → 6 | 16 → 8 → 4 |
| Before μ | 6 | 4 |
| After μ | +1 | 0 |

**T₂(19,16) = (6, 4)** retains the numbers. **V₂(19,16) = (+1, 0)** allows DOWN but gives no horizontal direction.

The retained 4 appears in several connected structures:

| Transition | Where 4 appears |
|:---|:---|
| OF THE → END | Radius of F–X–F and J–B–J |
| END → IS | Center rune R = 4 of I–R–I |
| DEATH → SEE | Radius of EA–J–EA |

These are observed matches, not a rule that every zero means a radius of 4. The calculations restrict possible movements; they do not yet determine one unique route.
