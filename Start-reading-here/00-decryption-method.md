# Decryption Method

**LP2 pages 0–2 · 27 × 27 matrix**

This guide explains the proposed method for a selected ciphertext block and its three-rune key node.

## 1. Basics

- **Coordinates:** `(row, column)`, starting from 1. Rows increase downward; columns increase to the right.
- **Rune indices:** values from 0 to 28, used for subtraction modulo 29.
- **φ(n), Euler’s totient:** counts the integers from 1 to n that share no factor with n other than 1.
- **μ(n), Möbius:** zero if a prime square divides n; otherwise +1 for an even number of distinct prime factors and −1 for an odd number. `μ(1) = +1`.

## 2. Decrypt a block

### Step 1 — Build the key

For nodes using the center transformation, replace the center index with its totient and keep the outer runes:

$$
(a,b,c)\longmapsto\bigl(a,\varphi(b),c\bigr).
$$

For example, `OE = 22` and `φ(22) = 10 = I`:

**`X–OE–X` → `X–I–X`**

Some nodes supply the key unchanged and skip this transformation.

### Step 2 — Calculate the phase and align the key

For the unrotated key `K = (k₁,k₂,k₃)`, calculate:

$$
\sigma_i=\mu(\varphi(k_i)),
$$

$$
p=(\sigma_1+\sigma_2+\sigma_3)\bmod3.
$$

For `X–I–X`:

| Rune | Index | φ(index) | μ(φ(index)) |
| :--- | ---: | ---: | ---: |
| X | 14 | 6 | +1 |
| I | 10 | 4 | 0 |
| X | 14 | 6 | +1 |

The signature is `(+1,0,+1)`, so **p = 2**.

Rotate the key **left by p positions**: `X–I–X` becomes **`X–X–I`**.

### Step 3 — Subtract the repeated key

Repeat the aligned key across the ciphertext. For each rune, subtract the matching key index modulo 29:

$$
P=(C-K)\bmod29.
$$

`C` is the ciphertext index, `K` the matching key index, and `P` the plaintext index.

The block at **row 14, columns 14–18** gives:

| Ciphertext | Repeated key | Plaintext |
| :--- | :--- | :--- |
| NG (21) | X (14) | W (7) |
| P (13) | X (14) | EA (28) |
| EO (12) | I (10) | TH (2) |
| O (3) | X (14) | E (18) |
| E (18) | X (14) | R (4) |

A negative result wraps around: `13 − 14 = −1 ≡ 28 (mod 29)`.

**`W–EA–TH–E–R` → WEATHER**

## 3. Move to the next key

Use the **current key’s phase p** and a chosen anchor cell. Apply `φ` to each coordinate **p times**, then apply `μ`. At phase 0, apply `μ` directly to the original coordinates.

| Sign | Row direction | Column direction |
| :---: | :--- | :--- |
| −1 | Up | Left |
| +1 | Down | Right |
| 0 | Unspecified | Unspecified |

Zero leaves a direction unresolved; it does not necessarily mean no movement.

### Example: COLD → I MAY

COLD uses **`H–U–H`**, with indices `(8,1,8)`. Its totient values are **`(4,1,4)`**, giving phase **1**. The anchor is **`A(11,7)`**:

$$
(11,7)\xrightarrow{\varphi}(10,6)
\xrightarrow{\mu}(+1,+1).
$$

Both signs are positive: **down and right**. The recorded move uses distances **4 rows** and **1 column**:

$$
(11,7)\longrightarrow(15,7)\longrightarrow(15,8).
$$

The destination, **`B(15,8)`**, is the center of **`NG–B–NG`**, the node used for I MAY.

## 4. What remains unresolved

The decryption is reproducible once the block and key are specified. A complete route still needs rules for choosing the anchor, movement distances, and next node.

---

Source: [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption).
