# 01 · Next Key Signature

Phase cycle and outer-state update.

This rule calculates the **phase and complete Möbius signature of the next key** from the current ciphertext coordinates and two state values.

> **17/17 phases · 17/17 complete signatures**
>
> Checked along the route from AS I GO THE → WEATHER through THEN → THE (LL).

## 1. Inputs

- **C** — all cell coordinates in the current ciphertext block.
- **K = (k₁, k₂, k₃)** — the current derived key, before its cyclic shift.
- **a** — the current outer signature state: 0 or 1.
- **S** — the accumulated sum of previously predicted phases.

Coordinates are one-based. Rows increase downward; columns increase to the right.

### Key signature

Apply Euler’s totient φ to each key value, then apply the Möbius function μ:

> **s₁ = μ(φ(k₁))**
>
> **s₂ = μ(φ(k₂))**
>
> **s₃ = μ(φ(k₃))**
>
> **σ(K) = (s₁, s₂, s₃)**

The rule uses signatures of the form **(a, b, a)**:

- **a** is 0 or +1.
- **b** is −1, 0 or +1.

The two outer signature values are equal; the outer runes themselves can differ. Use the positive rune indices of the derived key, after its center transformation and before its cyclic shift.

### Initial state

At **AS I GO THE**, the key is AE–I–EA and its signature is (0,0,0).

> **a = 0**
>
> **S = 0**

Carry the returned state forward after every block. A prime marks a next-block value: **a′, b′, p′, S′**.

## 2. Rotations and position numbers

Number the 27 × 27 grid from **1 to 729**, left to right and top to bottom.

### Original position · 0°

> **n₀(r,c) = 27(r − 1) + c**

### Clockwise quarter-turn · 90°

The coordinates become **(c, 28 − r)**.

> **n₁(r,c) = 27(c − 1) + 28 − r**

### Half-turn · 180°

The coordinates become **(28 − r, 28 − c)**.

> **n₂(r,c) = 730 − n₀(r,c)**

The constant 730 is fixed by the grid numbering:

> **n₀ + n₂ = 729 + 1 = 730**

Use these **absolute position numbers** in the Möbius calculations.

The Möbius function μ(n) is 0 when n contains a squared prime factor. Otherwise, its value is (−1)ᵏ, where k is the number of distinct prime factors. In particular, μ(1) = +1.

## 3. Phase cycle

The phase mode selects a position transform **T** and an offset **δ**.

First calculate the counter’s position within the cycle:

> **u = S mod 28**

| Counter u | Mode |
|:--|:--|
| 0–6 | Direct / +1 |
| 7–13 | Reflected / +0 |
| 14–20 | Reflected / +1 |
| 21–27 | Direct / +0 |

- **Direct:** T(n) = n.
- **Reflected:** T(n) = 730 − n.
- The number after the slash is **δ**: either 0 or 1.

Here, “Reflected” means a 180° turn about the grid center.

Read the four rows in order, then return to Direct / +1. Each mode spans **seven accumulated phase units**, rather than seven blocks.

A predicted phase of 0 leaves S unchanged. Keep the full S in the state; use only S mod 28 to select the mode.

**Coverage of the 17-transition route:** 7 transitions in Direct / +1, 5 in Reflected / +0, 5 in Reflected / +1, and 0 in Direct / +0. The fourth mode completes the cycle definition.

## 4. Next phase

For every cell in C, calculate its original position number n. Apply the selected transform T, evaluate μ, and add the results:

> **t = Σ μ(T(n))**

The sum includes **every cell in the current block**.

Add the mode offset and take the remainder modulo 3:

> **p′ = (δ + t) mod 3**

The next phase p′ is **0, 1 or 2**. Throughout this document, modulo means the least nonnegative remainder; for example, −1 mod 3 = 2.

Select the mode from the current S. Update the counter only after completing the transition.

## 5. Outer state

Calculate the 90° position number n₁ for every cell in C. Select the smallest result:

> **m = minimum n₁ over C**

The selected cell **L** is the cell in the **leftmost occupied column**. If several cells share that column, choose the **bottommost** one.

Update the outer state:

> **a′ = (a + μ(m)) mod 2**

| μ(m) | State update |
|:--:|:--|
| 0 | Preserve a |
| +1 or −1 | Toggle a: 0 ↔ 1 |

The state toggles exactly when m is **square-free**.

### Mode consistency

The same selected value supplies a mode check:

| Mode | Allowed μ(m) |
|:--|:--:|
| Direct | 0 or +1 |
| Reflected | 0 or −1 |

This check passes on **18/18 documented blocks**, including THE (LL).

## 6. Complete signature

The next signature has the form **(a′, b′, a′)**. Its phase is the sum of its components modulo 3:

> **p′ = (2a′ + b′) mod 3**

To recover b′, first calculate a residue:

> **r′ = (p′ − 2a′) mod 3**

Then convert that residue into a signature value:

| Residue r′ | Middle value b′ |
|:--:|:--:|
| 0 | 0 |
| 1 | +1 |
| 2 | −1 |

The complete prediction is:

> **σ′ = (a′, b′, a′)**

Finally, update the phase counter:

> **S′ = S + p′**

Carry **(a′, S′)** into the next block.

The block sum determines the next phase. The selected leftmost cell determines the next outer state. Those two results determine the middle component.

## 7. Example · THEN → THE (LL)

The current block THEN occupies:

- (25,25)
- (25,26)
- (25,27)

Its unshifted key is **IA–E–IA**, with signature (0,+1,0). The incoming state is **a = 0, S = 18**.

### Next phase

At S = 18, select **Reflected / +1**.

The original positions are 673, 674 and 675. Their half-turn positions give:

| Cell | n₂ | μ(n₂) |
|:--:|--:|:--:|
| (25,25) | 57 | +1 |
| (25,26) | 56 | 0 |
| (25,27) | 55 | +1 |

> **t = +1 + 0 + 1 = 2**
>
> **p′ = (1 + 2) mod 3 = 0**

### Outer state

The selected cell is **L = (25,25)**:

> **m = n₁(25,25) = 651**

Since 651 = 3 × 7 × 31, its Möbius value is −1. This sign is allowed in Reflected mode.

> **a′ = (0 − 1) mod 2 = 1**

### Complete result

With p′ = 0 and a′ = 1, the middle residue is 1, so b′ = +1.

> **Next phase: 0**
>
> **Next signature: (+1,+1,+1)**
>
> **Next state: a′ = 1, S′ = 18**

The THE (LL) key is **E–TH–E = (18,2,18)**:

| Key value | φ(value) | μ(φ(value)) |
|:--|:--:|:--:|
| E = 18 | 6 | +1 |
| TH = 2 | 1 | +1 |
| E = 18 | 6 | +1 |

Its phase and full signature match the prediction. ✅

## 8. Route verification

Start at **a = 0, S = 0** and propagate the returned state through all 17 transitions.

Each checkmark below covers **both the next phase and the complete signature**.

| Transition | Result |
|:--|:--|
| AS I GO THE<br>→ WEATHER | Phase 2 · ✅<br>(+1,0,+1) |
| WEATHER<br>→ TURNS | Phase 0 · ✅<br>(0,0,0) |
| TURNS<br>→ COLD | Phase 1 · ✅<br>(0,+1,0) |
| COLD<br>→ I MAY | Phase 0 · ✅<br>(0,0,0) |
| I MAY<br>→ CRY | Phase 1 · ✅<br>(+1,-1,+1) |
| CRY<br>→ NOW THE | Phase 2 · ✅<br>(+1,0,+1) |
| NOW THE<br>→ IDEA | Phase 1 · ✅<br>(0,+1,0) |
| IDEA<br>→ OF | Phase 0 · ✅<br>(+1,+1,+1) |
| OF<br>→ THE | Phase 2 · ✅<br>(+1,0,+1) |
| THE<br>→ END | Phase 2 · ✅<br>(+1,0,+1) |
| END<br>→ IS | Phase 1 · ✅<br>(0,+1,0) |
| IS<br>→ DEATH | Phase 2 · ✅<br>(+1,0,+1) |
| DEATH<br>→ SEE | Phase 0 · ✅<br>(0,0,0) |
| SEE<br>→ YOU | Phase 1 · ✅<br>(0,+1,0) |
| YOU<br>→ SOON | Phase 2 · ✅<br>(0,-1,0) |
| SOON<br>→ THEN | Phase 1 · ✅<br>(0,+1,0) |
| THEN<br>→ THE (LL) | Phase 0 · ✅<br>(+1,+1,+1) |

**Route convention:** OF and THE are separate blocks. SOON uses the primary X–D–W–H ciphertext route. THE (LL) is the continuation after THEN.

<details>
<summary><strong>Show the calculation details</strong></summary>

The block sum uses the mode’s position transform. Each counter and outer state is carried from one transition to the next.

**01 · AS I GO THE → WEATHER**

- Counter: 0 → 2.
- Mode: Direct / +1.
- Block sum: -2; next phase: 2.
- Selected index: 14; μ(m) = +1.
- Outer state: 0 → 1.
- Next signature: (+1,0,+1). ✅

**02 · WEATHER → TURNS**

- Counter: 2 → 2.
- Mode: Direct / +1.
- Block sum: -1; next phase: 0.
- Selected index: 365; μ(m) = +1.
- Outer state: 1 → 0.
- Next signature: (0,0,0). ✅

**03 · TURNS → COLD**

- Counter: 2 → 3.
- Mode: Direct / +1.
- Block sum: 0; next phase: 1.
- Selected index: 500; μ(m) = 0.
- Outer state: 0 → 0.
- Next signature: (0,+1,0). ✅

**04 · COLD → I MAY**

- Counter: 3 → 3.
- Mode: Direct / +1.
- Block sum: -1; next phase: 0.
- Selected index: 176; μ(m) = 0.
- Outer state: 0 → 0.
- Next signature: (0,0,0). ✅

**05 · I MAY → CRY**

- Counter: 3 → 4.
- Mode: Direct / +1.
- Block sum: 0; next phase: 1.
- Selected index: 407; μ(m) = +1.
- Outer state: 0 → 1.
- Next signature: (+1,-1,+1). ✅

**06 · CRY → NOW THE**

- Counter: 4 → 6.
- Mode: Direct / +1.
- Block sum: +1; next phase: 2.
- Selected index: 414; μ(m) = 0.
- Outer state: 1 → 1.
- Next signature: (+1,0,+1). ✅

**07 · NOW THE → IDEA**

- Counter: 6 → 7.
- Mode: Direct / +1.
- Block sum: 0; next phase: 1.
- Selected index: 422; μ(m) = +1.
- Outer state: 1 → 0.
- Next signature: (0,+1,0). ✅

**08 · IDEA → OF**

- Counter: 7 → 7.
- Mode: Reflected / +0.
- Block sum: 0; next phase: 0.
- Selected index: 470; μ(m) = -1.
- Outer state: 0 → 1.
- Next signature: (+1,+1,+1). ✅

**09 · OF → THE**

- Counter: 7 → 9.
- Mode: Reflected / +0.
- Block sum: -1; next phase: 2.
- Selected index: 388; μ(m) = 0.
- Outer state: 1 → 1.
- Next signature: (+1,0,+1). ✅

**10 · THE → END**

- Counter: 9 → 11.
- Mode: Reflected / +0.
- Block sum: -1; next phase: 2.
- Selected index: 414; μ(m) = 0.
- Outer state: 1 → 1.
- Next signature: (+1,0,+1). ✅

**11 · END → IS**

- Counter: 11 → 12.
- Mode: Reflected / +0.
- Block sum: +1; next phase: 1.
- Selected index: 601; μ(m) = -1.
- Outer state: 1 → 0.
- Next signature: (0,+1,0). ✅

**12 · IS → DEATH**

- Counter: 12 → 14.
- Mode: Reflected / +0.
- Block sum: -1; next phase: 2.
- Selected index: 223; μ(m) = -1.
- Outer state: 0 → 1.
- Next signature: (+1,0,+1). ✅

**13 · DEATH → SEE**

- Counter: 14 → 14.
- Mode: Reflected / +1.
- Block sum: -1; next phase: 0.
- Selected index: 2; μ(m) = -1.
- Outer state: 1 → 0.
- Next signature: (0,0,0). ✅

**14 · SEE → YOU**

- Counter: 14 → 15.
- Mode: Reflected / +1.
- Block sum: 0; next phase: 1.
- Selected index: 352; μ(m) = 0.
- Outer state: 0 → 0.
- Next signature: (0,+1,0). ✅

**15 · YOU → SOON**

- Counter: 15 → 17.
- Mode: Reflected / +1.
- Block sum: +1; next phase: 2.
- Selected index: 408; μ(m) = 0.
- Outer state: 0 → 0.
- Next signature: (0,-1,0). ✅

**16 · SOON → THEN**

- Counter: 17 → 18.
- Mode: Reflected / +1.
- Block sum: 0; next phase: 1.
- Selected index: 408; μ(m) = 0.
- Outer state: 0 → 0.
- Next signature: (0,+1,0). ✅

**17 · THEN → THE (LL)**

- Counter: 18 → 18.
- Mode: Reflected / +1.
- Block sum: +2; next phase: 0.
- Selected index: 651; μ(m) = -1.
- Outer state: 0 → 1.
- Next signature: (+1,+1,+1). ✅

</details>

### State after THE (LL)

The route reaches THE (LL) with **a = 1, S = 18**. Applying the same update to that block gives:

> **Next phase: 1**
>
> **Next signature: (+1,−1,+1)**
>
> **Next counter: 19**

## 9. Reference implementation

This function takes the current block coordinates and state. In the code, names such as p_next correspond to the primed values used above.

<details>
<summary><strong>Show Python implementation</strong></summary>

No external dependencies are required.

```python
def mobius(n):
    """Möbius function for a positive integer."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    sign = 1
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            sign = -sign
            if n % divisor == 0:
                return 0
        divisor += 1
    return -sign if n > 1 else sign


def predict_next_signature(cells, a, S):
    """Return the next signature and state from current coordinates."""
    cells = [tuple(cell) for cell in cells]
    if not cells or len(set(cells)) != len(cells):
        raise ValueError("provide a nonempty block of distinct cell tuples")
    if any(not (1 <= r <= 27 and 1 <= c <= 27) for r, c in cells):
        raise ValueError("coordinates must lie in the 27 x 27 grid")
    if a not in (0, 1) or not isinstance(S, int) or S < 0:
        raise ValueError("state requires a in {0, 1} and integer S >= 0")

    # Each entry is (reflected, offset), in cycle order.
    modes = ((False, 1), (True, 0), (True, 1), (False, 0))
    reflected, delta = modes[(S % 28) // 7]

    positions = [27 * (r - 1) + c for r, c in cells]
    total = sum(
        mobius(730 - n if reflected else n)
        for n in positions
    )
    p_next = (delta + total) % 3

    m = min(27 * (c - 1) + 28 - r for r, c in cells)
    mu_m = mobius(m)
    a_next = (a + mu_m) % 2
    b_next = (0, 1, -1)[(p_next - 2 * a_next) % 3]

    return {
        "phase": p_next,
        "sum_mobius": total,
        "signature": (a_next, b_next, a_next),
        "state": (a_next, S + p_next),
        "selected_index": m,
        "selected_mobius": mu_m,
        "mode": ("Reflected" if reflected else "Direct", delta),
        "sign_ok": mu_m in ((-1, 0) if reflected else (0, 1)),
    }


# Initialize once at AS I GO THE.
state = (0, 0)
first_block = [
    (13, 25), (13, 26), (13, 27),
    (14, 1), (14, 2), (14, 3), (14, 4),
]
result = predict_next_signature(first_block, *state)

assert result["phase"] == 2
assert result["signature"] == (1, 0, 1)

# Carry this state into the next current block.
state = result["state"]  # (1, 2)

```

</details>

Use the predicted signature to filter candidate keys: calculate each candidate’s signature **before its cyclic shift** and retain the matches. The predicted phase gives the candidate key’s cyclic left shift.
