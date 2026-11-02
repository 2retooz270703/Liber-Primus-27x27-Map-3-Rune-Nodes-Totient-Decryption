# 10 — Squarefree-GCD Compatibility of the Next Key and Ciphertext

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
G_1:\quad \mu\!\left(\gcd(n_0(M'),n_0(B'))\right)\ne 0
$$

$$
G_2:\quad \mu\!\left(\gcd(n_0(M'),n_0(L'))\right)\ne 0
$$

$$
G_3:\quad \mu\!\left(\gcd(n_1(M'),n_3(E'))\right)\ne 0
$$

$$
G_4:\quad \mu\!\left(\gcd(n_0(M'),n_2(E'))\right)\ne 0
$$

Here, `gcd` is the greatest common divisor. The Möbius function `μ(n)` equals **0** when `n` is divisible by a prime square (4, 9, 25, 49, ...); otherwise it is **+1 or −1**.

**Meaning:** The two cell indices **do not need to be coprime**. They may share prime factors, but no **square of the same prime** may divide both. Equivalently, their GCD must be **squarefree**.

- **12 and 18:** `12 = 2 × 2 × 3`, `18 = 2 × 3 × 3`. Their `gcd = 6 = 2 × 3`, so `μ(6) = +1` — **pass**.
- **12 and 20:** `12 = 2 × 2 × 3`, `20 = 2 × 2 × 5`. Their `gcd = 4 = 2 × 2`, so `μ(4) = 0` — **fail**.

The filter does **not** forbid repeated factors inside an individual cell index; it forbids a **repeated prime factor in the common divisor**.

## 3. Worked example: WEATHER → TURNS

The recorded **TURNS** block uses:

| Selected cell | Coordinate |
| :--- | :--- |
| Original key center `NG` (M′) | **(14,23)** |
| Ciphertext beginning `A` (B′) | **(14,19)** |
| Ciphertext leftmost cell (L′) | **(14,19)** |
| Ciphertext endpoint `W` (E′) | **(10,19)** |

Its ciphertext is read **upward** in column 19. Therefore B′ and L′ coincide.

| Rule | Indices compared | GCD | Möbius value | Result |
| :--- | :--- | ---: | ---: | :--- |
| G₁ | `n₀(M′)=374`, `n₀(B′)=370` | 2 | −1 | Pass |
| G₂ | `n₀(M′)=374`, `n₀(L′)=370` | 2 | −1 | Pass |
| G₃ | `n₁(M′)=608`, `n₃(E′)=226` | 2 | −1 | Pass |
| G₄ | `n₀(M′)=374`, `n₂(E′)=468` | 2 | −1 | Pass |

**All four pass.** In every comparison the GCD is 2, not 1. Even though some individual indices contain squared prime factors, the **shared** factor appears only once.

## 4. Checks against the recorded route

Using the selected original key centers and ciphertext cells in [`01–28`](../plaintext-i-found/), the four conditions each pass **27/27 next blocks** (blocks 02–28). These comprise **16** next-block transitions in the initial AS I GO ... THEN sequence and **11** blocks in the proposed continuation through MAP.

The tested family consists of **48 comparisons**: four center rotations × four ciphertext rotations × three target positions (B′, L′, E′). **Exactly these four comparisons** reach 27/27 on the selected route; the other 44 do not. The opening block (01) is the starting point, not a predicted next block, and is excluded from this count.

As a separate check, **2,000,000 random permutations** reassigning the same 27 key centers to the fixed 27 ciphertext blocks produced **1,422** permutations satisfying all four *fixed* conditions (**0.0711%**, random seed 3301). This tests sensitivity to the chosen center–ciphertext pairings, not the probability that Cicada deliberately designed the rule.

**The filter can reject alternatives.** For example, SOON has three documented original nodes that derive the same key. With the SOON ciphertext fixed, the center at **(20,15)** gives `gcd(n₀(M′), n₀(B′)) = 8`, so G₁ and G₂ fail. The alternative centers **(25,7)** and **(25,14)** pass all four conditions. This makes the choice of original center important.

## 5. Interpretation

The recurring property is **avoidance of `μ(gcd) = 0`** across specific relationships between the next key center and ciphertext cells, including rotated positions. It is a **candidate positional filter**, not a plaintext decryption formula.

The 27/27 result is exact for the **selected** route, but the rules were identified from these same data and some key placements have alternatives. The result therefore supports further testing of non-random structure; by itself it does **not** establish a unique continuation or prove Cicada's intent.
