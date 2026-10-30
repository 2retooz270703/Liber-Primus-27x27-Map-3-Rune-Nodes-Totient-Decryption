# The 27 × 27 Matrix

**Decryption method · LP2 pages 0–2**

This proposed method combines three-rune keys, a calculated key phase, and movement through the matrix. The examples below show how each part works and where the route remains unresolved.

## 1. Conventions

- **Coordinates:** `(row, column)`, numbered from 1. Rows increase downward; columns increase to the right.
- **Rune indices:** values in the 29-rune alphabet, used for decryption modulo 29. They are separate from cell coordinates.
- **Euler’s totient, φ(n):** the number of positive integers up to `n` that are coprime to `n`.
- **Möbius function, μ(n):** `0` if `n` has a repeated prime factor; otherwise `+1` for an even number of distinct prime factors and `−1` for an odd number. In particular, `μ(1) = +1`.

## 2. Decrypt a ciphertext block

### Build the key

For structures that use the center transformation, keep the outer runes and replace the center index with its totient:

$$
(a,b,c)\longmapsto\bigl(a,\varphi(b),c\bigr).
$$

For example, `OE = 22` and `φ(22) = 10 = I`, so:

**`X–OE–X` → `X–I–X`**

Some keys, including the non-mirrored `H–NG–C`, are used directly. The transformation is not applied to every structure.

### Calculate the phase and align the key

For the derived key in its **unrotated order**, calculate a three-value signature:

$$
\sigma_i=\mu(\varphi(k_i)),\qquad i=1,2,3.
$$

Add the signature values and reduce modulo 3:

$$
p=(\sigma_1+\sigma_2+\sigma_3)\bmod 3.
$$

For `X–I–X`:

| Key rune | Index | φ(index) | μ(φ(index)) |
| :--- | ---: | ---: | ---: |
| X | 14 | 6 | +1 |
| I | 10 | 4 | 0 |
| X | 14 | 6 | +1 |

The signature is `(+1, 0, +1)`, giving `p = 2`.

Rotate the key **left by p positions**. Here, `X–I–X` becomes **`X–X–I`**. This changes the order of the key elements; it does not rotate the matrix.

### Subtract the repeated key

Repeat the aligned key across the ciphertext and subtract rune indices modulo 29:

$$
P_j=(C_j-K_j)\bmod 29.
$$

Here, `C` is the ciphertext, `K` is the repeated aligned key, and `P` is the plaintext.

The **WEATHER** example uses row 14, columns 14–18:

| Ciphertext | Key | Result modulo 29 | Plaintext |
| :--- | :--- | ---: | :--- |
| NG (21) | X (14) | 7 | W |
| P (13) | X (14) | 28 | EA |
| EO (12) | I (10) | 2 | TH |
| O (3) | X (14) | 18 | E |
| E (18) | X (14) | 4 | R |

**`W–EA–TH–E–R` → WEATHER**

## 3. Find the next position

Movement uses the **current key’s phase** and a chosen anchor cell `(r, c)`. Direction and distance are calculated separately.

### Calculate direction signs

Apply the totient function to each coordinate `p` times, then apply the Möbius function:

$$
T_p(r,c)=\bigl(\varphi^p(r),\varphi^p(c)\bigr)
$$

$$
V_p(r,c)=\bigl(\mu(\varphi^p(r)),\mu(\varphi^p(c))\bigr).
$$

`φᵖ` means **repeated application**, not exponentiation. At phase 0, the coordinates stay unchanged before applying `μ`.

| Sign | Row direction | Column direction |
| :---: | :--- | :--- |
| −1 | Up | Left |
| +1 | Down | Right |
| 0 | Unspecified | Unspecified |

A zero leaves that direction unresolved. It does not necessarily mean “do not move.” Keep the transformed values in `Tₚ` as well as the signs in `Vₚ`.

### Example: COLD → I MAY

The **COLD** key is `H–U–H`, with indices `(8, 1, 8)`:

- Totient values: `(4, 1, 4)`.
- Möbius signature: `(0, +1, 0)`.
- Phase: `p = 1`.

The anchor is the ciphertext endpoint, **`A(11,7)`**. Applying `φ` once gives:

$$
T_1(11,7)=(10,6),\qquad V_1(11,7)=(+1,+1).
$$

The signs indicate **down and right**. This transition uses the key’s totient values **4** and **1** as the row and column distances:

$$
(11,7)\xrightarrow{\text{down 4}}(15,7)
\xrightarrow{\text{right 1}}(15,8).
$$

The destination is **`B(15,8)`**, the center of `NG–B–NG`, the next recorded structure for **I MAY**.

### Other distance calculations

The route also includes:

- A single totient: `OE = 22`, so `φ(22) = 10`.
- A sum of successive totients: `J = 11`, so `φ(11) + φ(10) = 10 + 4 = 14`.

These calculations produce the recorded distances, but there is no universal rule yet for choosing between them.

### Example: retain a value when its sign is zero

The **END** ciphertext ends at **`I(21,23)`**, with phase `p = 2`:

$$
21\xrightarrow{\varphi}12\xrightarrow{\varphi}4,
\qquad
23\xrightarrow{\varphi}22\xrightarrow{\varphi}10.
$$

Therefore:

$$
T_2(21,23)=(4,10),\qquad V_2(21,23)=(0,+1).
$$

The column sign points right; the row direction is unspecified. The retained value **4** matches the index of **R**, the center rune of the nearby `I–R–I` mirror.

## 4. Check mirror geometry

A **mirror** has two identical outer runes at equal, opposite offsets from a center. It may be horizontal, vertical, or diagonal.

For example, `J–D–J` occupies **`J(15,20)`**, **`D(17,18)`**, and **`J(19,16)`**. The outer cells have the center as their midpoint:

$$
\frac{(15,20)+(19,16)}{2}=(17,18).
$$

### Endpoint roles and key signatures

For **NOW THE**, the key `OE–I–OE` has totient values `(10, 4, 10)` and signature `(+1, 0, +1)`. For **IDEA**, `A–U–A` gives `(8, 1, 8)` and signature `(0, +1, 0)`.

Their endpoints occupy the outer and center positions of the same `J–D–J` mirror. Four other passages follow the same pattern:

| Passage | Key signature | Endpoint | Role | Mirror |
| :--- | :--- | :--- | :--- | :--- |
| NOW THE | (+1, 0, +1) | J(15,20) | Outer | J–D–J |
| IDEA | (0, +1, 0) | D(17,18) | Center | J–D–J |
| COLD | (0, +1, 0) | A(11,7) | Center | EA–A–EA |
| IS | (0, +1, 0) | D(21,10) | Center | E–D–E |
| WEATHER | (+1, 0, +1) | E(14,18) | Outer | E–NG–E |
| END | (+1, 0, +1) | I(21,23) | Outer | I–R–I |

In these examples, **`(0, +1, 0)` corresponds to a center**, while **`(+1, 0, +1)` corresponds to an outer cell**. This provides a consistency check for a candidate passage.

### Shared cells

One cell can belong to several structures:

| Cell | Roles |
| :--- | :--- |
| J(19,16) | Center of `OE–J–OE`; outer cell of `J–D–J` and `J–B–J` |
| R(21,22) | Center of both `I–R–I` and `H–R–H` |

These overlaps connect structures at exact coordinates, but do not by themselves select the next branch.

## 5. What remains unresolved

For a specified ciphertext block and derived key, the phase and modulo-29 plaintext calculation are reproducible. A complete traversal still needs rules for:

- **Choosing the anchor.** It is often the ciphertext endpoint, but the check after WEATHER uses `A(14,19)`, next to the endpoint `E(14,18)`.
- **Choosing distances.** Different transitions use individual totient values, paired values, or sums.
- **Choosing the continuation.** Mirror roles and shared cells help compare candidates, but do not yet determine a unique route.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
