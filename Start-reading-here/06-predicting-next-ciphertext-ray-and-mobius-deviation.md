# Filtering the Next Ciphertext’s Beginning

**Ray alignment and allowed offset · LP2 pages 0–2**

The next beginning is checked against eight rays from the current block’s leftmost cell. A condition at the current endpoint determines whether a one-cell offset is allowed.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right.

In the formulas, `r(X)` and `c(X)` denote a cell’s row and column.

| Symbol | Meaning |
| :--- | :--- |
| L | Current leftmost cell: smallest occupied column, bottommost cell in a tie |
| E | Current endpoint: last cell read |
| B′ | Proposed beginning of the next block: first cell read |

**Measure the displacement from L. Evaluate the Möbius condition at E.** These may be different cells.

## 2. Calculate the allowed offset

For the endpoint `E = (r,c)`, calculate its absolute indices in the original orientation and after a **270° clockwise turn**:

$$
n_0(r,c)=27(r-1)+c,\qquad n_3(r,c)=27(27-c)+r.
$$

The Möbius value `μ(n)` is **0** if `n` has a repeated prime factor; otherwise it is **+1 or −1**.

Set the allowance:

- **q = 1** if both `μ(n₀(E)) = 0` and `μ(n₃(E)) = 0`.
- **q = 0** otherwise.

## 3. Check the next beginning

The eight rays run horizontally, vertically, and diagonally at 45°, with unrestricted length. For a proposed B′, calculate:

$$
\Delta r=r(B')-r(L),\qquad\Delta c=c(B')-c(L),
$$

$$
d_8=\min\left(|\Delta r|,|\Delta c|,\bigl||\Delta r|-|\Delta c|\bigr|\right).
$$

This **grid-offset score** is zero when B′ shares a row, column, or 45° diagonal with L. The anchor L itself also qualifies.

Accept the candidate only if:

$$
d_8\le q.
$$

| Allowance | Required position |
| :--- | :--- |
| q = 0 | Exactly on a ray: d₈ = 0 |
| q = 1 | On a ray or one cell off: d₈ = 0 or 1 |

**An allowance of 1 permits an offset; it does not require one.**

## 4. Example: OF → THE

For OF, **L = (18,15)** and **E = (18,16)**. The following THE begins at **B′ = (19,17)**.

At E:

- `n₀(E) = 475 = 5² × 19`.
- `n₃(E) = 315 = 3² × 5 × 7`.

Both indices contain a squared prime factor, so both Möbius values are zero and **q = 1**.

Measure from L:

$$
(\Delta r,\Delta c)=(1,2),\qquad d_8=\min(1,2,1)=1.
$$

The candidate passes because **1 ≤ 1**.

## 5. What the result establishes

All **16 transitions** in the selected research reconstruction pass: **12 exact alignments** and **4 one-cell offsets**. Independent validation is still needed.

The rule filters candidate positions. It does not choose the ray, travel distance, side of an offset, key, or plaintext.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).

