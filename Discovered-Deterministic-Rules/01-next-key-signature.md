# 01 · Predicting the Next Key Signature

*Phase cycle · Outer-state update · Complete signature*

This rule calculates the **phase and full Möbius signature of the next key** from the current ciphertext coordinates and two state values.

> **17/17 phase matches · 17/17 complete signature matches**
>
> From AS I GO THE → WEATHER through THEN → THE (LL).

## 1. Inputs and state

The grid contains **27 × 27 cells**. Coordinates are one-based: rows increase downward and columns increase to the right.

| Symbol | Meaning |
|:--|:--|
| C | All ciphertext cell coordinates in the current block |
| K | The current derived three-rune key, before its cyclic shift |
| a | Current outer signature state: 0 or 1 |
| S | Sum of previously predicted phases |
| φ | Euler’s totient function |
| μ | Möbius function: −1, 0 or +1 |

### Key signature

Apply φ to each of the three key values, then apply μ:

```math
s_i=\mu(\varphi(k_i)),\qquad i=1,2,3
```

```math
\sigma(K)=(s_1,s_2,s_3)=(a,b,a)
```

The rule uses the signature class **(a, b, a)**, where a is 0 or +1 and b is −1, 0 or +1.

Equal outer signature values do not require identical outer runes. Use the positive indices of the derived key, after its center transformation and **before its cyclic shift**.

### Initial state

At **AS I GO THE**, the key AE–I–EA has signature (0,0,0):

```math
a=0,\qquad S=0
```

A prime marks a value for the next block: a′, b′, p′ or S′. Carry the returned state forward after each transition.

## 2. Shared geometry

Number the grid from **1 to 729**, left to right and top to bottom.

A clockwise quarter-turn is

```math
R(r,c)=(c,28-r)
```

The three position functions are:

**Original position · 0°**

```math
n_0(r,c)=27(r-1)+c
```

**Quarter-turn · 90°**

```math
n_1(r,c)=27(c-1)+28-r
```

**Half-turn · 180°**

```math
n_2(r,c)=730-n_0(r,c)
```

The constant 730 comes directly from the grid:

```math
n_0(x)+n_2(x)=27^2+1=730
```

All Möbius evaluations below use **absolute position indices**, rather than rune values. The matrix does not need to be physically rotated.

The Möbius function is zero when its argument contains a squared prime factor. Otherwise, its sign is determined by the parity of the number of distinct prime factors; μ(1) = +1.

## 3. Phase cycle

The current counter selects a position transform T and an offset δ. Its position within the four-mode cycle is

```math
u=S\bmod28
```

| Counter u | Mode |
|:--|:--|
| 0–6 | Direct / +1 |
| 7–13 | Reflected / +0 |
| 14–20 | Reflected / +1 |
| 21–27 | Direct / +0 |

- **Direct:** T(n) = n.
- **Reflected:** T(n) = 730 − n.
- The number after the slash gives **δ**.

“Reflected” means a **180° turn about the grid center**.

The cycle follows the table from top to bottom, then returns to Direct / +1. Each mode spans **seven accumulated phase units**, rather than seven blocks.

Keep the full S in the state and use S mod 28 to select a mode. A predicted phase of 0 leaves S unchanged.

**Route coverage:** 7 transitions in Direct / +1, 5 in Reflected / +0, 5 in Reflected / +1, and 0 in Direct / +0. The fourth mode completes the cycle definition.

## 4. Predict the next phase

Evaluate Möbius at the mode’s position index for **every cell in the current block**, then add the values:

```math
t=\sum_{x\in C}\mu(T(n_0(x)))
```

Add the offset and reduce modulo 3:

```math
p'=(\delta+t)\bmod3
```

The result p′ is **0, 1 or 2**.

Select the mode from the current S. Use the least nonnegative remainder throughout: for example, −1 mod 3 = 2.

## 5. Update the outer state

Select the smallest absolute index after a 90° clockwise rotation:

```math
m=\min_{x\in C}n_1(x)
```

In the original grid, the selected cell L is in the **leftmost occupied column**. If several cells share that column, choose the **bottommost** one.

Update the outer state:

```math
a'=(a+\mu(m))\bmod2
```

| μ(m) | Effect |
|:--:|:--|
| 0 | Preserve a |
| +1 or −1 | Toggle a: 0 ↔ 1 |

The outer state toggles exactly when m is **square-free**. Both nonzero Möbius values have the same effect modulo 2.

### Mode consistency

The same selected cell supplies a sign check:

| Mode | Allowed μ(m) |
|:--|:--:|
| Direct | 0 or +1 |
| Reflected | 0 or −1 |

This check passes on **18/18 documented blocks**, including THE (LL).

## 6. Recover the full signature

The next signature has the form (a′, b′, a′). Its phase is the sum of its components modulo 3:

```math
p'=(2a'+b')\bmod3
```

Recover the middle component by first calculating a residue:

```math
z=(p'-2a')\bmod3
```

Convert z into the middle signature value:

| Residue z | Middle value b′ |
|:--:|:--:|
| 0 | 0 |
| 1 | +1 |
| 2 | −1 |

The complete next signature is

```math
\sigma'=(a',b',a')
```

Finish the transition by updating the counter:

```math
S'=S+p'
```

Carry **(a′, S′)** into the next block.

The block sum determines the phase. The selected leftmost cell determines the outer state. Together, they determine the complete signature.

## 7. Worked example · THEN → THE (LL)

THEN occupies **(25,25), (25,26), (25,27)**. Its unshifted key is IA–E–IA with signature (0,+1,0), so the incoming state is **a = 0, S = 18**.

### Next phase

At S = 18, the mode is **Reflected / +1**. The original indices are 673, 674 and 675:

| Cell | Half-turn index | μ |
|:--:|--:|:--:|
| (25,25) | 57 | +1 |
| (25,26) | 56 | 0 |
| (25,27) | 55 | +1 |

```math
t=1+0+1=2
```

```math
p'=(1+2)\bmod3=0
```

### Outer state

The selected cell is **L = (25,25)**:

```math
m=n_1(25,25)=651
```

Since 651 = 3 × 7 × 31, μ(651) = −1. The sign passes the Reflected-mode check and toggles the outer state:

```math
a'=(0-1)\bmod2=1
```

### Complete result

Phase 0 and outer state 1 give middle residue z = 1, hence b′ = +1:

```math
\sigma'=(+1,+1,+1)
```

The returned state is **a′ = 1, S′ = 18**.

This matches the THE (LL) key **E–TH–E = (18,2,18)**:

| Key value | φ(value) | μ(φ(value)) |
|:--|:--:|:--:|
| E = 18 | 6 | +1 |
| TH = 2 | 1 | +1 |
| E = 18 | 6 | +1 |

**Next phase: 0 · Complete signature: (+1,+1,+1)** ✅

## 8. Verification

Start at **a = 0, S = 0** and propagate the returned state through all 17 transitions.

Each checkmark covers **both the phase and the complete next-key signature**.

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

### State at THE (LL)

The route reaches THE (LL) with **a = 1, S = 18**. Applying the same update to that block gives phase **1**, signature **(+1,−1,+1)**, and counter **19**.

## 9. Reference implementation

The implementation accepts the current block coordinates and state. Names such as p_next correspond to the primed values above.

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

Use the predicted signature to filter candidate keys: calculate each candidate’s signature **before its cyclic shift** and retain the matches. The predicted phase gives the key’s cyclic left shift.
