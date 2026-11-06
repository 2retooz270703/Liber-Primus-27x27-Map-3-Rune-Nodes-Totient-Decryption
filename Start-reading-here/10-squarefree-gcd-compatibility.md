# Squarefree-GCD Compatibility of the Next Key and Ciphertext

This proposed filter links the **original center of the next key node** to the **beginning, leftmost cell, and endpoint of the next ciphertext**. Four comparisons must avoid a zero Möbius value.

## 1. Inputs and cell indices

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

| Symbol | Meaning |
| :--- | :--- |
| M′ | Center of the **next original three-rune key node**, before any totient transformation or key rotation |
| B′ | First ciphertext cell read in the next block |
| L′ | Next ciphertext's leftmost cell: smallest column, bottommost cell in a tie |
| E′ | Last ciphertext cell read in the next block |

Number the 729 cells row by row after each clockwise rotation:

| Rotation | Absolute index of cell `(r,c)` |
| :--- | :--- |
| 0° | `n₀(r,c) = 27(r − 1) + c` |
| 90° | `n₁(r,c) = 27(c − 1) + 28 − r` |
| 180° | `n₂(r,c) = 730 − n₀(r,c)` |
| 270° | `n₃(r,c) = 730 − n₁(r,c)` |

The rotations change the **numerical indices** used in the test; they do not change which original cells were selected.

## 2. The four conditions

A proposed next block passes only when **all four** are satisfied:

$$
G_1:\quad \mu\\left(\gcd(n_0(M'),n_0(B'))\right)\ne 0
$$

$$
G_2:\quad \mu\\left(\gcd(n_0(M'),n_0(L'))\right)\ne 0
$$

$$
G_3:\quad \mu\\left(\gcd(n_1(M'),n_3(E'))\right)\ne 0
$$

$$
G_4:\quad \mu\\left(\gcd(n_0(M'),n_2(E'))\right)\ne 0
$$

Here, `gcd` is the greatest common divisor. The Möbius function `μ(n)` equals **0** when `n` is divisible by a prime square (4, 9, 25, 49, ...); otherwise it is **+1 or −1**.

**Meaning:** The two cell indices **do not need to be coprime**. They may share prime factors, but no **square of the same prime** may divide both. Equivalently, their GCD must be **squarefree**.

- **12 and 18:** `12 = 2 × 2 × 3`, `18 = 2 × 3 × 3`. Their `gcd = 6 = 2 × 3`, so `μ(6) = +1` — **pass**.
- **12 and 20:** `12 = 2 × 2 × 3`, `20 = 2 × 2 × 5`. Their `gcd = 4 = 2 × 2`, so `μ(4) = 0` — **fail**.

The filter does **not** forbid repeated factors inside an individual cell index; it forbids a **repeated prime factor in the common divisor**.

**The filter can reject alternatives.** For example, SOON has three documented original nodes that derive the same key. With the SOON ciphertext fixed, the center at **(20,15)** gives `gcd(n₀(M′), n₀(B′)) = 8`, so G₁ and G₂ fail. The alternative centers **(25,7)** and **(25,14)** pass all four conditions. This makes the choice of original center important.
