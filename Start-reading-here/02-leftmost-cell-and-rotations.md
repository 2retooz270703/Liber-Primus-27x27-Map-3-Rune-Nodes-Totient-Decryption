# The Leftmost Cell

**Möbius check and reading order · LP2 pages 0–2**

Two checks help evaluate a continuation: whether a block’s leftmost cell fits its mode, and whether the next block’s leftmost cell is read first or last.

## 1. Inputs

The matrix is **27 × 27**. Coordinates are `(row, column)`, starting from 1; rows increase downward and columns to the right. After rotation, cells are numbered row by row from 1 to 729.

| Symbol | Meaning |
| :--- | :--- |
| L | Current leftmost cell: smallest occupied column, bottommost cell in a tie |
| E | Current endpoint: last cell read |
| h | Rune index of the current original key-node center, **before the totient transformation** |
| L′ | Next block’s leftmost cell, selected by the same geometric rule |

L and E may be different cells. The functions `φ` and `μ` are Euler’s totient and Möbius functions, defined in the [decryption method](00-decryption-method.md).

## 2. Check the leftmost cell

For L = `(r,c)`, calculate its absolute index after a **90° clockwise turn**:

$$
n_1(r,c)=27(c-1)+28-r.
$$

Apply `μ` and compare the result with the current block’s mode from [Report 01](01-next-key-signature.md):

| Current mode | Allowed μ(n₁(L)) |
| :--- | :--- |
| Direct | 0 or +1 |
| Reflected | 0 or −1 |

**Zero is allowed in both modes**, so it cannot identify the mode by itself.

## 3. Predict the next reading boundary

Use the **current endpoint E** and the **original center’s rune index h**. The endpoint’s absolute index after a **270° clockwise turn** is:

$$
n_3(r,c)=27(27-c)+r.
$$

Calculate:

$$
\tau_{\mathrm{next}}=\bigl[\mu(n_3(E))+\varphi(h)\bigr]\bmod2.
$$

| Result | Prediction for L′ |
| :---: | :--- |
| 1 | BEGINNING — first cell read |
| 0 | END — last cell read |

This describes the reading order, whether the block is horizontal, vertical, or diagonal.

## 4. Example: after THEN

THEN is in **Reflected/+1**. Its leftmost cell is **`L(25,25)`**, its endpoint is **`W(25,27)`**, and its original center rune is **`IA = 27`**.

### Current leftmost cell

$$
n_1(25,25)=651=3\times7\times31,\qquad\mu(651)=-1.
$$

The value −1 fits the Reflected mode.

### Next reading boundary

For the endpoint, `n₃(25,27) = 25` and `μ(25) = 0`. The original center gives `φ(27) = 18`:

$$
\tau_{\mathrm{next}}=(0+18)\bmod2=0.
$$

**The next block’s leftmost cell should be its END.**

The candidate THE reads **`J(22,21) → W(21,20)`**, ending at its leftmost cell as predicted. That cell’s 90° index is **520**, with `μ(520) = 0`, also allowed in the Reflected class.

## 5. What the result establishes

On the selected route, the class check matches **17/17 blocks** and the boundary rule matches **16/16 transitions**. The candidate THE is a separate conditional check. These conditions constrain candidates but do not determine exact coordinates or a unique plaintext.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
