# Predicting the Exact Next-Ciphertext Ray Deviation

This report refines [Report 06](06-predicting-next-ciphertext-ray-and-mobius-deviation.md). 

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

## 4. Three worked transitions

### A. OF (09) → THE (10): an offset is required

The selected **OF** ciphertext reads `B=(18,15) → E=(18,16)`, with `L=(18,15)`. Its endpoint indices are:

- `n₀(E) = 475 = 5² × 19`, so `μ(n₀(E)) = 0`.
- `n₃(E) = 315 = 3² × 5 × 7`, so `μ(n₃(E)) = 0`.

Therefore **`q = 1`**. At the beginning, `n₀(B) = 474` has `μ(474) = −1`, while `n₁(B) = 388` has `μ(388) = 0`. Consequently **`z = 0`**, and the proposed rule requires **`d₈ = 1`**.

The recorded next beginning is `B′=(19,17)`. Relative to `L=(18,15)`, `Δr=1` and `Δc=2`, giving

$$
d_8=\min(1,2,1)=\boxed{1}.
$$

The selected transition meets the **exact** requirement, not merely Report 06's allowance.

### B. SEE (14) → YOU (15): the apparent exception is on-ray

For **SEE**, `B=(25,16)`, `E=(27,14)`, and `L=(27,14)`.

- At `E`: `n₀(E)=716`, `n₃(E)=378`; both have Möbius value **0**. Thus **`q=1`**.
- At `B`: `n₀(B)=664`, `n₁(B)=408`; both have Möbius value **0**. Thus **`z=1`**.

The new prediction is **`d₈=q(1-z)=0`**. The selected next ciphertext begins at `B′=(27,18)`, on the same row as `L=(27,14)`, so **`d₈=0`**, as required.

### C. KEY (19) → IS (20): a second on-ray exception

For **KEY**, `B=(21,4)`, `E=(19,4)`, and `L=(21,4)`.

- At `E`: `n₀(E)=490`, `n₃(E)=640`; both have Möbius value **0**. Thus **`q=1`**.
- At `B`: `n₀(B)=544`, `n₁(B)=88`; both have Möbius value **0**. Thus **`z=1`**.

The new prediction is **`d₈=0`**. The selected **IS** begins at `B′=(18,7)`, giving `Δr=−3`, `Δc=+3`: a perfect 45° diagonal from `L`, and hence **`d₈=0`**.

These two on-ray cases are particularly informative: Report 06 allowed both `0` and `1`, while the new beginning-based test specifically predicts `0`.

## 5. Audit of the selected 33 transitions

There are **34 selected ciphertext blocks** and therefore **33 recorded transitions**. All 33 agree with the proposed exact-deviation rule.

Of these:

- **24** have `q=0`; both the old and new rules already require `d₈=0`. These cases provide **no additional discrimination**.
- **9** have `q=1`; these are the **informative cases**. Seven have `z=0` and observed `d₈=1`; two have `z=1` and observed `d₈=0`.

| Transition | Current → next | `q` | `z` | Predicted `d₈` | Observed `d₈` | Match |
| ---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 08→09 | IDEA → OF | 1 | 0 | **1** | 1 | Yes |
| 09→10 | OF → THE | 1 | 0 | **1** | 1 | Yes |
| 12→13 | IS → DEATH | 1 | 0 | **1** | 1 | Yes |
| 13→14 | DEATH → SEE | 1 | 0 | **1** | 1 | Yes |
| 14→15 | SEE → YOU | 1 | 1 | **0** | 0 | Yes |
| 17→18 | THEN → THE | 1 | 0 | **1** | 1 | Yes |
| 19→20 | KEY → IS | 1 | 1 | **0** | 0 | Yes |
| 24→25 | THE → EAST | 1 | 0 | **1** | 1 | Yes |
| 29→30 | MAY → BE | 1 | 0 | **1** | 1 | Yes |

The nine rows above are the **entire subset where Report 06 permits two outcomes**. In the remaining 24 transitions, `q=0` and the observed offset is `0` throughout. Thus the headline **33/33** should be read alongside the more diagnostic **9/9 within the ambiguous subset**.

## 6. Exploratory branch-pruning result

An exploratory candidate enumeration for the **existing selected route and its fixed test setup** produced the following counts. Here “old” means satisfying the previously applied conditions including `d₈ ≤ q`; “new” adds the exact equality `d₈=q(1-z)`.

| Current → next | Old candidates | New candidates | Eliminated |
| :--- | ---: | ---: | ---: |
| IDEA → OF | 58 | 40 | 18 |
| OF → THE | 66 | 54 | 12 |
| IS → DEATH | 67 | 54 | 13 |
| DEATH → SEE | 59 | 36 | 23 |
| SEE → YOU | 59 | 59 | 0 |
| THEN → THE | 59 | 46 | 13 |
| KEY → IS | 88 | 21 | 67 |
| THE → EAST | 128 | 104 | 24 |
| MAY → BE | 43 | 28 | 15 |
| **Nine informative transitions** | **627** | **442** | **185** |
| **Other 24 transitions** | **801** | **801** | **0** |
| **All 33 transitions** | **1,428** | **1,243** | **185** |

For the nine informative transitions, this is **185/627 ≈ 29.5%** fewer candidates. Across all 33, it is **185/1,428 ≈ 13.0%** fewer candidates.

## 7. A falsifiable prediction beyond the recorded route

The selected last block **YOU (34)** has:

- Current beginning `B=(6,11)`.
- Current endpoint `E=(6,13)`.
- Current leftmost cell `L=(6,11)`.

At the endpoint:

$$
n_0(E)=148,\quad n_3(E)=384,\quad \mu(148)=\mu(384)=0.
$$

Hence **`q=1`**. At the beginning:

$$
n_0(B)=146,\quad n_1(B)=292,\quad \mu(146)=+1,\quad \mu(292)=0.
$$

Hence **`z=0`**, and the new rule gives the prospective constraint

$$
\boxed{\ d_8\bigl((6,11),B_{35}\bigr)=1\ }.
$$

**If the same rule continues beyond block 34, the next ciphertext must begin exactly one ray-offset unit away from the eight lines through `(6,11)`**, rather than directly on a line.

## 8. Interpretation and limits

The proposed linkage is arithmetically specific: **square factors in rotated indices at the endpoint enable an offset; square factors at the beginning decide whether the enabled offset must be zero instead.** This fits the project's recurring use of Möbius zeroes and squarefree restrictions, especially [Report 10](10-squarefree-gcd-compatibility.md).
