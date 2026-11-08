# Seven-Phase Thresholds and Cyclic Mode Transitions

## 1. State and terminology

Let `p_i ∈ {0,1,2}` be the Möbius phase of the **i-th derived key**, as defined in the [decryption method](00-decryption-method.md). Let `S_i` be the running sum **after** that block:

$$
S_0=0,\qquad S_i=S_{i-1}+p_i.
$$

For a transition from block `i−1` to block `i`, [Report 01](01-next-key-signature.md) predicts `p_i` from the **previous ciphertext** using the mode selected by `S_{i-1}`. Only then is the running sum updated.

A **seven-phase threshold** is a positive multiple of seven:

$$
T_k=7k\qquad(k=1,2,3,\ldots).
$$

Use **multiple of 7**, not *divisor of 7*, for the values `7, 14, 21, 28, ...`.

## 2. Proposed rule A — Never skip a multiple of seven

A valid transition must **not jump strictly across** a seven-phase threshold. If a threshold is reached, the sum must **land on it exactly**.

Formally, reject a proposed transition if there is an integer `k ≥ 1` such that

$$
S_{\mathrm{before}}<7k<S_{\mathrm{after}},
\qquad S_{\mathrm{after}}=S_{\mathrm{before}}+p_{\mathrm{next}}.
$$

Because the phase is only `0`, `1`, or `2`, the rule has one simple operational form:

$$
\boxed{\text{If }p_{\mathrm{next}}=2,\ \text{reject if }S_{\mathrm{before}}\bmod7=6.}
$$

Otherwise the transition satisfies this particular filter. A phase of `2` is **not forbidden in general**: it is forbidden only when it would skip over the next multiple of seven.

| S before | Next phase | S after | Result | Reason |
| ---: | ---: | ---: | :--- | :--- |
| 6 | 2 | 8 | **Reject** | Skips 7 |
| 6 | 1 | 7 | Keep | Lands on 7 |
| 12 | 2 | 14 | Keep | Lands on 14 |
| 20 | 2 | 22 | **Reject** | Skips 21 |
| 25 | 2 | 27 | Keep | No threshold crossed |
| 27 | 2 | 29 | **Reject** | Skips 28 |
| 27 | 1 | 28 | Keep | Lands on 28 |

## 3. Proposed rule B — The four modes repeat cyclically

Report 01 specifies four consecutive intervals, each seven phase-units wide. The proposed extension treats those four intervals as **one repeating cycle of length 28**.

For any nonnegative accumulated sum `S`, choose

$$
q=\left\lfloor\frac{S}{7}\right\rfloor\bmod4.
$$

The mode for **predicting the next phase** is then:

| q | S in first cycle | Mode | Next-phase formula |
| :---: | :--- | :--- | :--- |
| 0 | 0–6 | **Direct/+1** | `(1 + Σμ(n)) mod 3` |
| 1 | 7–13 | **Reflected/+0** | `Σμ(730−n) mod 3` |
| 2 | 14–20 | **Reflected/+1** | `(1 + Σμ(730−n)) mod 3` |
| 3 | 21–27 | **Direct/+0** | `Σμ(n) mod 3` |
| **0** | **28–34** | **Direct/+1** | **`(1 + Σμ(n)) mod 3`** |

Here `n = 27(r−1)+c` is the 1-based absolute index of each occupied **current ciphertext** cell `(r,c)` in the 27×27 matrix. The sum covers every cell of that block; `730−n` is the index reflected by a 180° rotation. This extends the formulas in [Report 01](01-next-key-signature.md), without changing their calculations for `0 ≤ S < 28`.

The proposed cycle is:

**Direct/+1 → Reflected/+0 → Reflected/+1 → Direct/+0 → Direct/+1 → ...**

**Timing matters:** When a block's phase makes `S` reach a threshold, the **new mode applies to the outgoing transition from that block**, not retroactively to the transition that produced it.

### Direct implementation

Supply every cell of the current ciphertext block as a nonempty list of 1-based `(row, column)` coordinates. The supplied `mu` function must evaluate the Möbius function on positive integers. `MAP LIFE`, for example, is supplied as one continuous block.

`S_current` is a nonnegative integer: the accumulated phase sum **after the current block**, hence **before the transition being checked**. The candidate's `next_phase` is its derived-key phase, either 0, 1, or 2.

The acceptance function checks both the deterministic phase forecast under Rule B and the no-skipping condition under Rule A. It leaves the predicted phase unchanged.

```python
def cyclic_phase_mode(S_current):
    """Return (use_180_degree_indices, additive_offset) for the next forecast."""
    q = (S_current // 7) % 4
    reflected = q in (1, 2)
    offset = 1 if q in (0, 2) else 0
    return reflected, offset


def expected_next_phase(current_cipher_cells, S_current, mu):
    """Predict the next phase from all current ciphertext cells and current S."""
    reflected, offset = cyclic_phase_mode(S_current)
    mobius_sum = 0

    for r, c in current_cipher_cells:
        n = 27 * (r - 1) + c
        if reflected:
            n = 730 - n
        mobius_sum += mu(n)

    return int((offset + mobius_sum) % 3)


def skips_seven_threshold(S_before, next_phase):
    """Test Rule A; S_before >= 0 and next_phase is 0, 1, or 2."""
    return next_phase == 2 and S_before % 7 == 6


def accepts_next_phase(current_cipher_cells, S_current, next_phase, mu):
    """Apply the cyclic phase forecast and no-skipping filter together."""
    predicted = expected_next_phase(current_cipher_cells, S_current, mu)
    return (
        next_phase == predicted
        and not skips_seven_threshold(S_current, next_phase)
    )


# Keep a candidate next key only if:
# accepts_next_phase(current_cipher_cells, S_current, next_phase, mu)
#
# Only after acceptance, update the accumulated sum once:
# S_next = S_current + next_phase
```
