# 01 — Predicting the Next Key Signature

**A coordinate-based rule for the next key's phase and Möbius signature.**

The rule reads the **current ciphertext cells** in the 27 × 27 grid and returns two properties of the **next three-rune key**: its cyclic phase and its full Möbius signature.

> **Recorded result: 17/17 matching transitions** — from `AS I GO THE → WEATHER` to `THEN → THE (LL)` — on the selected plaintext route.

The calculation needs only the current cell coordinates and a running state `(a, S)`. It does **not** require the next key or its coordinates as input.

---

## 1. What the rule uses

The grid is numbered **1–729**, row by row, starting at the top left. Coordinates `(r, c)` start at 1.

| Symbol | Meaning |
|:--|:--|
| `C` | Coordinates of all cells in the **current** ciphertext block |
| `μ(n)` | Möbius function: `−1`, `0`, or `+1` |
| `a` | Current key's outer signature value: `0` or `1` |
| `S` | Sum of all previously predicted phases |

For a cell `(r, c)`, three index formulas are enough:

```text
Original (0°):     n   = 27(r − 1) + c
Clockwise (90°):   n90 = 27(c − 1) + 28 − r
Half-turn (180°):  n180 = 730 − n
```

Here, **180° is a rotation about the center**, not a mirror flip over one axis. The constant `730` is `27² + 1`.

The Möbius function returns `0` when a number has a repeated prime factor. Otherwise it is `+1` for an even number of distinct prime factors, or `−1` for an odd number; `μ(1) = +1`.

### What is a key signature?

For a derived three-rune key `K = (k1, k2, k3)`, apply Euler's totient function `φ`, then Möbius, to each **positive rune index**:

```text
signature(K) = ( μ(φ(k1)), μ(φ(k2)), μ(φ(k3)) )
             = ( a, b, a )
```

All recorded keys in this route have **equal outer signature values**. This does not mean their outer runes must be the same. Always calculate the signature **after the key's center transformation, but before its cyclic shift**.

**Initial state:** the `AS I GO THE` key `AE–I–EA` has signature `(0,0,0)`, so start with **`a = 0` and `S = 0`**.

---

## 2. The four-mode phase cycle

First select a mode from the running phase total:

```text
u = S mod 28
```

| `u` | Position used | Offset `δ` |
|:--:|:--|:--:|
| **0–6** | Original `n` | **+1** |
| **7–13** | Rotated 180°: `730 − n` | **0** |
| **14–20** | Rotated 180°: `730 − n` | **+1** |
| **21–27** | Original `n` | **0** |

The modes repeat in that order. Each covers **seven units of accumulated phase**, *not* seven ciphertext blocks. A predicted phase of `0` leaves `S` unchanged.

On the documented route, the first three modes are used for **7, 5, and 5 transitions** respectively. The fourth mode is part of the proposed cycle but has **no recorded test yet**.

---

## 3. Predict the next signature

### Step 1 — Find the next phase

Use **every cell** of the current ciphertext. Choose each cell's original or 180° index according to the table above, and sum the Möbius values:

```text
t = sum( μ(chosen position of x) for x in C )
p = (δ + t) mod 3
```

The predicted phase `p` is `0`, `1`, or `2`. It specifies the next key's **cyclic left shift**.

### Step 2 — Find the next outer value

This time use **one cell**, selected by a 90° clockwise rotation:

```text
m = minimum n90 among cells in C
a_next = (a + μ(m)) mod 2
```

You can select this cell directly on the original grid:

1. Find the **leftmost column** occupied by the ciphertext.
2. If several ciphertext cells lie in it, take the **bottommost** one.

The update is simple: **`μ(m) = 0` keeps `a` unchanged; `μ(m) = ±1` switches `a` between 0 and 1.**

The selected cell also supplies a consistency check:

| Current mode | Allowed `μ(m)` |
|:--|:--:|
| Original position | `0` or `+1` |
| 180° position | `0` or `−1` |

This sign check matches **18/18 documented ciphertext blocks**, including `THE (LL)`.

### Step 3 — Read the complete signature

The predicted phase `p` and outer value `a_next` uniquely specify the next signature:

| Phase `p` | `a_next = 0` | `a_next = 1` |
|:--:|:--:|:--:|
| **0** | `(0,0,0)` | `(+1,+1,+1)` |
| **1** | `(0,+1,0)` | `(+1,−1,+1)` |
| **2** | `(0,−1,0)` | `(+1,0,+1)` |

The middle value follows from `b_next = (p − 2a_next) mod 3`, interpreting residue `2` as `−1`.

Finally update the running state:

```text
S_next = S + p
Next state = (a_next, S_next)
```

**Use the returned state for the following ciphertext block.** Do not reset it between transitions.

---

## 4. Example: `THEN → THE (LL)`

The ciphertext `THEN` occupies `(25,25)`, `(25,26)`, `(25,27)`. Its unshifted key has signature `(0,+1,0)`, and the incoming state is **`a = 0, S = 18`**.

**1 · Phase**

Since `S = 18`, use the **180° / +1** mode:

| Current cell | 180° index | Möbius |
|:--|--:|:--:|
| `(25,25)` | 57 | `+1` |
| `(25,26)` | 56 | `0` |
| `(25,27)` | 55 | `+1` |

So `t = 1 + 0 + 1 = 2`, and **`p = (1 + 2) mod 3 = 0`**.

**2 · Outer value**

The leftmost/bottommost selection is `L(25,25)`. Its 90° index is **`m = 651 = 3 × 7 × 31`**, so `μ(651) = −1`.

The sign is allowed in the 180° mode, and **`a_next = (0 − 1) mod 2 = 1`**.

**3 · Complete signature**

Look up `p = 0` and `a_next = 1` in the table above:

```text
Predicted phase:      0
Predicted signature:  (+1,+1,+1)
Next state:           (a = 1, S = 18)
```

The next recorded key is **`E–TH–E = (18,2,18)`**. Its signature is indeed `(+1,+1,+1)`, because `μ(φ(18)) = μ(6) = +1` and `μ(φ(2)) = μ(1) = +1`.

---

## 5. Verification across the route

Starting from `(a, S) = (0, 0)`, the rule reproduces the **phase and full signature at every one of the 17 recorded transitions**. Entries are grouped by the mode selected **before** each transition.

### Original / +1

| Transition | Phase | Next signature |
|:--|:--:|:--:|
| AS I GO THE → WEATHER | 2 | `(+1,0,+1)` |
| WEATHER → TURNS | 0 | `(0,0,0)` |
| TURNS → COLD | 1 | `(0,+1,0)` |
| COLD → I MAY | 0 | `(0,0,0)` |
| I MAY → CRY | 1 | `(+1,−1,+1)` |
| CRY → NOW THE | 2 | `(+1,0,+1)` |
| NOW THE → IDEA | 1 | `(0,+1,0)` |

### 180° / +0

| Transition | Phase | Next signature |
|:--|:--:|:--:|
| IDEA → OF | 0 | `(+1,+1,+1)` |
| OF → THE | 2 | `(+1,0,+1)` |
| THE → END | 2 | `(+1,0,+1)` |
| END → IS | 1 | `(0,+1,0)` |
| IS → DEATH | 2 | `(+1,0,+1)` |

### 180° / +1

| Transition | Phase | Next signature |
|:--|:--:|:--:|
| DEATH → SEE | 0 | `(0,0,0)` |
| SEE → YOU | 1 | `(0,+1,0)` |
| YOU → SOON | 2 | `(0,−1,0)` |
| SOON → THEN | 1 | `(0,+1,0)` |
| THEN → THE (LL) | 0 | `(+1,+1,+1)` |

**Route convention:** `OF` and `THE` are separate blocks; `SOON` uses the primary `X–D–W–H` ciphertext route. The last comparison uses the `THE (LL)` continuation after `THEN`.

<details>
<summary><strong>Full arithmetic log — 17 transitions</strong></summary>

The entries show the incoming and outgoing phase total, Möbius block sum, selected 90° index, and outer-state change. All signatures in the tables above follow from these values.

| Current ciphertext | `S → S_next` | `t` | `m; μ(m)` | `a → a_next` |
|:--|:--:|--:|:--:|:--:|
| AS I GO THE | 0 → 2 | −2 | 14; +1 | 0 → 1 |
| WEATHER | 2 → 2 | −1 | 365; +1 | 1 → 0 |
| TURNS | 2 → 3 | 0 | 500; 0 | 0 → 0 |
| COLD | 3 → 3 | −1 | 176; 0 | 0 → 0 |
| I MAY | 3 → 4 | 0 | 407; +1 | 0 → 1 |
| CRY | 4 → 6 | +1 | 414; 0 | 1 → 1 |
| NOW THE | 6 → 7 | 0 | 422; +1 | 1 → 0 |
| IDEA | 7 → 7 | 0 | 470; −1 | 0 → 1 |
| OF | 7 → 9 | −1 | 388; 0 | 1 → 1 |
| THE | 9 → 11 | −1 | 414; 0 | 1 → 1 |
| END | 11 → 12 | +1 | 601; −1 | 1 → 0 |
| IS | 12 → 14 | −1 | 223; −1 | 0 → 1 |
| DEATH | 14 → 14 | −1 | 2; −1 | 1 → 0 |
| SEE | 14 → 15 | 0 | 352; 0 | 0 → 0 |
| YOU | 15 → 17 | +1 | 408; 0 | 0 → 0 |
| SOON | 17 → 18 | 0 | 408; 0 | 0 → 0 |
| THEN | 18 → 18 | +2 | 651; −1 | 0 → 1 |

</details>

### Current prediction beyond the recorded transitions

At `THE (LL)`, the state is **`(a, S) = (1, 18)`**. Applying the same rule to that block gives **phase `1`**, signature **`(+1,−1,+1)`**, and updated counter **`S = 19`**. This is the next prediction; no following key is compared in the 17-transition table.

---

## 6. Python reference

The function takes **only current ciphertext coordinates and the current state**. It returns the next phase, signature, state, and selected-cell sign check.

<details>
<summary><strong>Show standalone Python implementation</strong></summary>

No external packages are needed.

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
    """Predict the next key's phase, signature and running state."""
    cells = [tuple(cell) for cell in cells]
    if not cells or len(cells) != len(set(cells)):
        raise ValueError("provide distinct ciphertext cells")
    if any(not (1 <= r <= 27 and 1 <= c <= 27) for r, c in cells):
        raise ValueError("coordinates must be between 1 and 27")
    if a not in (0, 1) or not isinstance(S, int) or S < 0:
        raise ValueError("state must have a in {0,1} and S >= 0")

    # The four modes: (use_180_degree_rotation, offset).
    modes = ((False, 1), (True, 0), (True, 1), (False, 0))
    rotated, delta = modes[(S % 28) // 7]

    positions = [27 * (r - 1) + c for r, c in cells]
    t = sum(mobius(730 - n if rotated else n) for n in positions)
    phase = (delta + t) % 3

    m = min(27 * (c - 1) + 28 - r for r, c in cells)
    mu_m = mobius(m)
    a_next = (a + mu_m) % 2
    b_next = (0, 1, -1)[(phase - 2 * a_next) % 3]

    return {
        "phase": phase,
        "signature": (a_next, b_next, a_next),
        "state": (a_next, S + phase),
        "sum_mobius": t,
        "selected_index": m,
        "selected_mobius": mu_m,
        "sign_ok": mu_m in ((-1, 0) if rotated else (0, 1)),
    }


# First recorded transition: AS I GO THE -> WEATHER.
state = (0, 0)
first_block = [
    (13, 25), (13, 26), (13, 27),
    (14, 1), (14, 2), (14, 3), (14, 4),
]
result = predict_next_signature(first_block, *state)
assert result["phase"] == 2
assert result["signature"] == (1, 0, 1)
state = result["state"]  # (1, 2), for the next block
```

</details>

**Using the prediction:** compute candidate keys' Möbius signatures **before cyclic shifting**, retain those matching the predicted three values, and apply the predicted phase as the cyclic left shift. The signature narrows the candidate keys; it does not by itself determine the next ciphertext's location or plaintext.
