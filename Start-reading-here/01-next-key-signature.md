# Predicting the Next Key

## 1. Inputs

For the **derived key in unrotated order**, the signature contains one value `μ(φ(rune index))` per rune. Its phase is the sum of those values modulo 3, as defined in the [decryption method](00-decryption-method.md).

The recorded keys have equal first and third signature values, either **0 or +1**. Call this shared value **a**.

Keep two values as you follow the route:

| Value | Meaning |
| :--- | :--- |
| S | Running sum of the next-key phases predicted so far |
| a | Current key’s shared outer signature value |

Start with **`S = 0, a = 0`**, from the initial key `AE–I–EA`, whose signature is `(0,0,0)`.

Coordinates are `(row, column)`, numbered from 1. Rows increase downward; columns increase to the right.

## 2. Prediction steps

### Step 1 — Predict the next phase

Convert every current ciphertext cell to an absolute position:

$$
n(r,c)=27(r-1)+c.
$$

Use **S before the transition** to choose the calculation. Each sum includes **all cells of the current block**.

| S before | Mode | Next-phase calculation |
| :--- | :--- | :--- |
| 0 ≤ S < 7 | Direct/+1 | (1 + Σμ(n)) mod 3 |
| 7 ≤ S < 14 | Reflected/+0 | Σμ(730−n) mod 3 |
| 14 ≤ S < 21 | Reflected/+1 | (1 + Σμ(730−n)) mod 3 |
| 21 ≤ S < 28 | Direct/+0 | Σμ(n) mod 3 |

`730−n` is the cell’s absolute position after a **180° turn**. The result is the predicted next phase: **0, 1, or 2**.

### Step 2 — Predict the outer values

In the current ciphertext, choose the **leftmost occupied column**, then the **bottommost cell** in that column.

For this cell `(r,c)`, calculate its absolute position after a **90° clockwise turn**:

$$
m=27(c-1)+28-r.
$$

Update the outer value:

$$
a_{\mathrm{next}}=(a+\mu(m))\bmod2.
$$

- **μ(m) = 0:** keep a unchanged.
- **μ(m) = +1 or −1:** switch `0 ↔ 1`.

### Step 3 — Read the complete signature

The next phase and updated outer value determine all three components:

| Next phase | a_next = 0 | a_next = 1 |
| :---: | :--- | :--- |
| 0 | (0,0,0) | (+1,+1,+1) |
| 1 | (0,+1,0) | (+1,−1,+1) |
| 2 | (0,−1,0) | (+1,0,+1) |

For the following transition, **add the predicted phase to S** and **replace a with a_next**. Carry both values forward.

### Direct implementation

Supply `current_cipher_cells` as a nonempty list of all current ciphertext coordinates **in reading order**, using 1-based `(row, column)` pairs. `S` is the integer accumulated sum through the current block, before predicting the outgoing transition. `a` is the shared outer signature value of the current **derived key in unrotated order**, either 0 or 1.

The code implements this report's finite phase schedule for **0 ≤ S < 28**. The proposed cyclic extension and no-skipping filter are defined separately in [Report 11](11-seven-thresholds-and-cyclic-phase-modes.md). A forecast here can reach `S_next = 28`; the current sum remains unchanged while the forecast is calculated.

The supplied `mu` and `phi` functions evaluate Möbius and Euler's totient on positive integers. `next_unrotated_key` contains the candidate's three positive derived rune indices **after any center transformation and before cyclic alignment**. The acceptance function compares its complete signature with the forecast.

```python
def predict_next_key(current_cipher_cells, S, a, mu):
    """Forecast the next phase, signature, and carried state under Report 01."""
    if not 0 <= S < 28:
        raise ValueError("Report 01 defines its phase schedule for 0 <= S < 28.")
    if a not in (0, 1):
        raise ValueError("The current outer signature value a must be 0 or 1.")

    mode = S // 7
    reflected = mode in (1, 2)
    offset = 1 if mode in (0, 2) else 0
    mobius_sum = 0

    for r, c in current_cipher_cells:
        n = 27 * (r - 1) + c
        if reflected:
            n = 730 - n
        mobius_sum += mu(n)

    next_phase = int((offset + mobius_sum) % 3)

    L = min(current_cipher_cells, key=lambda cell: (cell[1], -cell[0]))
    r, c = L
    n90 = 27 * (c - 1) + 28 - r
    next_outer = int((a + mu(n90)) % 2)

    signature_table = {
        0: ((0, 0, 0), (1, 1, 1)),
        1: ((0, 1, 0), (1, -1, 1)),
        2: ((0, -1, 0), (1, 0, 1)),
    }
    signature = signature_table[next_phase][next_outer]

    return {
        "phase": next_phase,
        "signature": signature,
        "S_next": int(S + next_phase),
        "a_next": next_outer,
    }


def derived_key_signature(unrotated_key, mu, phi):
    """Calculate mu(phi(k)) for each of the three positive derived indices."""
    return tuple(int(mu(phi(k))) for k in unrotated_key)


def accepts_next_key_prediction(
    current_cipher_cells, S, a, next_unrotated_key, mu, phi
):
    """Check the candidate's unrotated derived-key signature."""
    predicted = predict_next_key(current_cipher_cells, S, a, mu)
    actual = derived_key_signature(next_unrotated_key, mu, phi)
    return actual == predicted["signature"]


# Initial state for the recorded route:
# S, a = 0, 0
#
# prediction = predict_next_key(current_cipher_cells, S, a, mu)
# Check a proposed next derived key:
# accepts_next_key_prediction(
#     current_cipher_cells, S, a, next_unrotated_key, mu, phi
# )
#
# After the candidate passes all applicable filters, carry the state forward:
# S, a = prediction["S_next"], prediction["a_next"]
```
