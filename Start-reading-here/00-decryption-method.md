# Decryption Method

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

### Direct implementation

The inputs here are **integer rune indices** read from the selected matrix cells. Supply the ciphertext in reading order and the original node's three indices in **outer–center–outer** order. Set `transform_center=True` to apply φ to the center, or `False` for an unchanged key. The original input sequences are preserved.

Ciphertext and plaintext indices range from 0 to 28. This implementation requires **positive key indices, 1…28**, because the signature calculation uses φ and μ on positive integers; a zero key component is rejected explicitly. The functions `mu` and `phi` below can also be passed to the other reports' implementations.

The result contains the unrotated derived key, its signature and phase, the aligned key, and the plaintext rune indices. Call the function once per independently decrypted block, including all its words. Block-length and continuation filters are applied separately.

```python
from operator import index as integer_index


def phi(n):
    """Euler's totient for a positive integer; phi(1) = 1."""
    n = integer_index(n)
    if n < 1:
        raise ValueError("phi requires a positive integer.")

    result = n
    remaining = n
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result -= result // factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        result -= result // remaining
    return result


def mu(n):
    """Mobius function for a positive integer; mu(1) = 1."""
    n = integer_index(n)
    if n < 1:
        raise ValueError("mu requires a positive integer.")

    sign = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            sign = -sign
            if n % factor == 0:
                return 0
        factor += 1
    return -sign if n > 1 else sign


def decrypt_block(ciphertext_indices, original_node_runes, transform_center):
    """Derive, align and repeat a three-rune key; subtract modulo 29."""
    ciphertext = [integer_index(v) for v in ciphertext_indices]
    key = [integer_index(v) for v in original_node_runes]

    if len(key) != 3:
        raise ValueError("The original node must contain three rune indices.")
    if any(not 1 <= k <= 28 for k in key):
        raise ValueError("This signature calculation requires key indices 1..28.")
    if any(not 0 <= c <= 28 for c in ciphertext):
        raise ValueError("Ciphertext rune indices must be in 0..28.")

    if transform_center:
        key[1] = phi(key[1])

    signature = tuple(mu(phi(k)) for k in key)
    phase = int(sum(signature) % 3)
    aligned_key = key[phase:] + key[:phase]
    plaintext = tuple(
        (c - aligned_key[j % 3]) % 29 for j, c in enumerate(ciphertext)
    )

    return {
        "unrotated_key": tuple(key),
        "signature": signature,
        "phase": phase,
        "aligned_key": tuple(aligned_key),
        "plaintext": plaintext,
    }


# WEATHER example:
# result = decrypt_block(
#     [21, 13, 12, 3, 18], [14, 22, 14], transform_center=True
# )
# result["unrotated_key"] == (14, 10, 14)
# result["signature"] == (1, 0, 1)
# result["phase"] == 2
# result["aligned_key"] == (14, 14, 10)
# result["plaintext"] == (7, 28, 2, 18, 4)  # W-EA-TH-E-R
```
