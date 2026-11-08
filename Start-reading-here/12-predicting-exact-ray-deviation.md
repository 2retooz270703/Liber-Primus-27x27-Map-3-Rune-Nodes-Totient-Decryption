# Predicting the Exact Next-Ciphertext Ray Deviation

## 1. What is new?

[Report 06](06-predicting-next-ciphertext-ray-and-mobius-deviation.md) evaluates the next ciphertext's **beginning** against eight horizontal, vertical, and 45° diagonal rays through the current ciphertext's **leftmost cell**. Its endpoint-based Möbius condition sets an allowance `q`:

- `q = 0`: the next beginning must lie **on** one of the rays (`d₈ = 0`).
- `q = 1`: the next beginning may lie **on** a ray or **one grid-offset unit off** it (`d₈ ∈ {0, 1}`).

The unresolved choice in the second case is now addressed by an additional test at the **current ciphertext beginning**. For the 33 selected transitions, that test correctly distinguishes all seven observed `d₈ = 1` cases from the two observed `d₈ = 0` cases when `q = 1`.

**The proposal changes an upper bound, `d₈ ≤ q`, into an exact prediction, `d₈ = 0` or `d₈ = 1`.** It does not choose a unique ray, a distance along that ray, a key node, a ciphertext length, or a plaintext word.

## 2. Definitions and coordinate conventions

Use the project's **27 × 27** matrix, with 1-based `(row, column)` coordinates: rows increase downward; columns increase rightward.

| Symbol | Meaning |
| :--- | :--- |
| `B` | Current ciphertext's **first** cell in reading order |
| `E` | Current ciphertext's **last** cell in reading order |
| `L` | Current ciphertext's geometrically **leftmost** cell: smallest column, bottommost on ties |
| `B′` | Proposed **first** cell of the next ciphertext |
| `μ(n)` | Möbius function; `μ(n) = 0` exactly when a squared prime divides `n` |
| `n₀, n₁, n₃` | Absolute cell indices at 0°, 90°, and 270° clockwise rotation |

The rotated positions are **indices of the same original cell**, not new locations from which a ciphertext is read:

$$
n_0(r,c)=27(r-1)+c,
$$

$$
n_1(r,c)=27(c-1)+28-r,
$$

$$
n_3(r,c)=27(27-c)+r.
$$

For the displacement from `L` to `B′`, set

$$
\Delta r=r(B')-r(L),\qquad \Delta c=c(B')-c(L),
$$

$$
d_8(L,B')=\min\left(
|\Delta r|,\ |\Delta c|,\ \bigl||\Delta r|-|\Delta c|\bigr|
\right).
$$

This is the **ray-offset score** used in Report 06, **not** the ordinary Chebyshev distance between two cells. It equals zero at any distance along a horizontal, vertical, or 45° diagonal line through `L` (including `L` itself).

## 3. Proposed exact-deviation rule

**Step A — Determine whether an offset is possible (unchanged from Report 06).** Evaluate the *current endpoint* `E`:

$$
q=\mathbf1\left[
\mu\left(n_0(E)\right)=0
\ \land\ 
\mu\left(n_3(E)\right)=0
\right].
$$

**Step B — Resolve the allowance using the current beginning.** Evaluate the *current beginning* `B`:

$$
z=\mathbf1\left[
\mu\left(n_0(B)\right)=0
\ \land\ 
\mu\left(n_1(B)\right)=0
\right].
$$

**Step C — Require the exact offset:**

$$
\boxed{\ d_8(L,B')=q(1-z)\ }.
$$

| Endpoint test `q` | Beginning test `z` | Required `d₈(L,B′)` | Meaning |
| :---: | :---: | :---: | :--- |
| 0 | 0 | **0** | Exactly on a ray |
| 0 | 1 | **0** | Exactly on a ray |
| 1 | 0 | **1** | Exactly one grid-offset unit off the rays |
| 1 | 1 | **0** | Exactly on a ray despite the original allowance |

The only new constraint is the distinction between the last two rows. **Do not replace `B` by `L`:** the test is performed on the first cell *read*, while the geometric ray remains anchored at `L`.

### Direct implementation

Supply the current ciphertext cells **in reading order**, using 1-based `(row, column)` coordinates. The supplied `mu` function must evaluate the Möbius function on positive integers.

The required offset is calculated from the current beginning B and endpoint E. The acceptance check separately locates L using the stated leftmost-cell convention, then compares the candidate next beginning with the required offset.

```python
def expected_next_ray_offset(current_cipher_cells, mu):
    """Return the required offset, 0 or 1, from the current block only."""
    B = current_cipher_cells[0]
    E = current_cipher_cells[-1]

    def n0(cell):
        r, c = cell
        return 27 * (r - 1) + c

    def n90(cell):
        r, c = cell
        return 27 * (c - 1) + 28 - r

    def n270(cell):
        r, c = cell
        return 27 * (27 - c) + r

    q = (mu(n0(E)) == 0 and mu(n270(E)) == 0)
    z = (mu(n0(B)) == 0 and mu(n90(B)) == 0)
    return int(q and not z)


def ray_offset(leftmost_cell, next_beginning):
    """Return the report's d8 score relative to the current leftmost cell."""
    dr = abs(next_beginning[0] - leftmost_cell[0])
    dc = abs(next_beginning[1] - leftmost_cell[1])
    return min(dr, dc, abs(dr - dc))


def accepts_next_beginning(current_cipher_cells, next_beginning, mu):
    """Apply the exact-offset filter to a candidate next first cell."""
    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    required = expected_next_ray_offset(current_cipher_cells, mu)
    return ray_offset(L, next_beginning) == required


# Keep a candidate next beginning B_next only if:
# accepts_next_beginning(current_cipher_cells, B_next, mu)
```
