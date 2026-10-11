# 02 — How to Move

*Totient values → Distance → Direction*

After a ciphertext segment ends, numbers from its key can help locate the next structure. **Distance** tells us how many cells to move; **direction** tells us which way to look.

## 1. Find the distance

Euler's totient φ, introduced in Rule 01, can also supply movement distances.

For example, the **COLD** key is H–U–H. Apply φ to its three rune values:

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Key | H = 8 | U = 1 | H = 8 |
| φ | 4 | 1 | 4 |

The next recorded move uses **4** and **1** as distances. Neither number tells us which way to travel.

Other stages use a center's φ value, such as φ(OE = 22) = 10, or add successive values: φ(J = 11) = 10 and φ(10) = 4, giving 14. There is not yet one rule for choosing which distance to use.

## 2. Find the direction

Use the **phase of the previous ciphertext's key**. Apply it to the coordinates of the endpoint or a nearby transition point. For instance, WEATHER ends at E(14,18), but its next coordinate check uses A(14,19).

The phase tells us how many times to apply φ to each coordinate *before* applying the Möbius function μ:

| Phase | Calculation for a coordinate n |
|:---:|:---:|
| 0 | μ(n) |
| 1 | μ(φ(n)) |
| 2 | μ(φ(φ(n))) |

The result is a sign for each coordinate. Rows increase downward; columns increase to the right.

| μ result | Row | Column |
|:---:|:---:|:---:|
| −1 | UP | LEFT |
| +1 | DOWN | RIGHT |
| 0 | No direction | No direction |

For **COLD → I MAY**, the ciphertext ends at **A(11,7)**. The COLD key has phase **1**, so apply φ once, then μ:

| | Row 11 | Column 7 |
|:---|:---:|:---:|
| φ | φ(11) = 10 | φ(7) = 6 |
| μ | μ(10) = +1 | μ(6) = +1 |
| Direction | DOWN | RIGHT |

**DOWN + RIGHT**, using the distances **4** and **1** from Section 1:

**A(11,7) → DOWN 4 → S(15,7) → RIGHT 1 → B(15,8)**

B(15,8) is the center of the next structure, NG–B–NG. The signs select possible directions, but do not specify the order of the moves or uniquely select a destination.

In short, for coordinates (r,c) and phase p:

**Vₚ(r,c) = (μ(φᵖ(r)), μ(φᵖ(c)))**

Here φᵖ means applying φ exactly p times. The formula uses the *coordinate numbers*, not the rune values at those cells.

## 3. When μ gives zero

A zero means **no direction on that axis**. It does not erase the number calculated just before μ.

For example, **END** ends at **I(21,23)** with phase **2**:

| | Row 21 | Column 23 |
|:---|:---:|:---:|
| Apply φ twice | 21 → 12 → 4 | 23 → 22 → 10 |
| Apply μ | μ(4) = 0 | μ(10) = +1 |
| Direction | Not specified | RIGHT |

Keep both the numbers *before* μ and the signs *after* μ:

| Values before μ | Direction signs after μ |
|:---:|:---:|
| T₂(21,23) = (4, 10) | V₂(21,23) = (0, +1) |

The retained **4** matches the center rune **R = 4** in the nearby **I–R–I** mirror. In other transitions, a retained value matches a mirror's radius instead.

The general form for retaining these values is:

**Tₚ(r,c) = (φᵖ(r), φᵖ(c))**

A retained value is a possible clue, not an automatic movement command. The calculations constrain the route; they do not yet determine a unique next structure.
