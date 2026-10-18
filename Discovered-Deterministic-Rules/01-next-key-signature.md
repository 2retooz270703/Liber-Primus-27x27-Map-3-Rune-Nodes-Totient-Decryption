# 01 · Predicting the Next Key Signature

**Phase cycle · Leftmost-cell update · Complete Möbius signature**

Given the current ciphertext block and the current state, this rule calculates the **phase and full Möbius signature of the next key**. It combines a sum over the block with a state update controlled by one selected cell.

> **Route check:** 17/17 next-key phases and 17/17 complete signatures match the documented route, from **AS I GO THE → WEATHER** through **THEN → THE (LL)**.

## 1. Inputs and state

The grid contains **27 × 27 cells**. Coordinates are one-based: rows increase downward and columns increase to the right.

| Symbol | Meaning |
|:--|:--|
| $C$ | Coordinates of every ciphertext cell in the current block. |
| $K=(k_1,k_2,k_3)$ | Current derived key, **before its cyclic shift**. |
| $\varphi$ | Euler’s totient function. |
| $\mu$ | Möbius function, with values $-1,0,+1$. |
| $a$ | Current outer signature state, either $0$ or $1$. |
| $S$ | Accumulated sum of the phases predicted at previous transitions. |

The key signature is

$$
\sigma(K)=
\bigl(\mu(\varphi(k_1)),\ \mu(\varphi(k_2)),\ \mu(\varphi(k_3))\bigr).
$$

The rule operates on the signature class

$$
\sigma(K)=(a,b,a),
\qquad a\in\{0,1\},\quad b\in\{-1,0,+1\}.
$$

Equal outer **signature values** do not require identical outer runes. The signature is calculated from the positive rune indices of the derived key, after its center transformation and before its cyclic shift.

For the first block, **AS I GO THE**, the key is AE–I–EA, its signature is $(0,0,0)$, and the initial state is

$$
\boxed{a=0,\qquad S=0.}
$$

After initialization, each transition uses only the current block coordinates and the state $(a,S)$.

## 2. Position indices and rotations

Number the grid cells from **1 to 729**, left to right and top to bottom:

$$
n_0(r,c)=27(r-1)+c.
$$

Let $R$ be a clockwise quarter-turn:

$$
R(r,c)=(c,28-r),
\qquad n_j(x)=n_0(R^j x).
$$

| Rotation | Coordinates | Absolute position index |
|:--|:--|:--|
| $0^\circ$ | $(r,c)$ | $n_0=27(r-1)+c$ |
| $90^\circ$ | $(c,28-r)$ | $n_1=27(c-1)+28-r$ |
| $180^\circ$ | $(28-r,28-c)$ | $n_2=730-n_0$ |

The constant **730** follows directly from the numbering:

$$
n_0(x)+n_2(x)=27^2+1=730.
$$

All Möbius evaluations below use these **absolute position numbers**, rather than the rune values stored in those positions.

The Möbius function is zero when its argument contains a squared prime factor. Otherwise, it is $(-1)^k$, where $k$ is the number of distinct prime factors; $\mu(1)=+1$.

## 3. Select the phase mode

The phase mode selects the position transform and an additive offset. The four-mode cycle is specified by

$$
u=S\bmod28.
$$

| Counter position $u$ | Mode | $\rho$ | Offset $\delta$ | Index used in the sum | Route transitions |
|:--|:--|:--:|:--:|:--|--:|
| $0\le u<7$ | Direct / +1 | 0 | 1 | $n_0(x)$ | 7 |
| $7\le u<14$ | Reflected / +0 | 1 | 0 | $n_2(x)=730-n_0(x)$ | 5 |
| $14\le u<21$ | Reflected / +1 | 1 | 1 | $n_2(x)=730-n_0(x)$ | 5 |
| $21\le u<28$ | Direct / +0 | 0 | 0 | $n_0(x)$ | 0 |

The cycle starts at **Direct / +1**:

**Direct / +1 → Reflected / +0 → Reflected / +1 → Direct / +0 → Direct / +1**

Each mode spans **seven units of accumulated phase**. The counter measures phase values, not the number of blocks: a predicted phase of 0 leaves $S$ unchanged.

The route table in Section 8 contains transitions in the first three modes. The fourth row completes the cycle definition. Keep the full accumulated $S$ in the state; use $S\bmod28$ to select a mode.

## 4. Calculate the next phase

Evaluate Möbius at the selected index of **every cell in the current block**, add the mode offset, and reduce modulo 3:

$$
\boxed{
p_{\mathrm{next}}
=
\left[
\delta+\sum_{x\in C}\mu\bigl(n_{2\rho}(x)\bigr)
\right]_3.
}
$$

Here $[z]_m$ means the least nonnegative residue modulo $m$, so $p_{\mathrm{next}}\in\{0,1,2\}$.

- **Direct:** sum $\mu(n_0(x))$.
- **Reflected:** sum $\mu(730-n_0(x))$.

Here **Reflected** means a $180^\circ$ turn about the grid center.

Select the mode from the **current** $S$ and calculate the entire sum before updating the state.

## 5. Update the outer signature state

Select the cell with the smallest index after a $90^\circ$ clockwise rotation:

$$
L=\operatorname*{arg\,min}_{x\in C}n_1(x),
\qquad m=n_1(L).
$$

In the original grid, this is the cell in the **leftmost occupied column**; if several cells share that column, choose the **bottommost** one.

Update the outer state:

$$
\boxed{a_{\mathrm{next}}=[a+\mu(m)]_2.}
$$

| Value at the selected cell | Effect |
|:--:|:--|
| $\mu(m)=0$ | Preserve $a$. |
| $\mu(m)=+1$ or $-1$ | Toggle $a$: $0\leftrightarrow1$. |

Equivalently, the outer state toggles exactly when $m$ is **square-free**. Both nonzero Möbius values have the same effect modulo 2.

### Mode consistency check

The same selected cell also supplies a sign check:

$$
\begin{aligned}
\text{Direct:}\quad &\mu(m)\in\{0,+1\},\\
\text{Reflected:}\quad &\mu(m)\in\{0,-1\}.
\end{aligned}
$$

This check passes on **18/18 documented blocks**, including THE (LL). It uses the same $\mu(m)$ as the outer-state update.

## 6. Reconstruct the complete signature

The next phase and outer state determine the middle component:

$$
p_{\mathrm{next}}
\equiv
2a_{\mathrm{next}}+b_{\mathrm{next}}
\pmod3.
$$

Define the balanced residue map

$$
\operatorname{bal}_3(0)=0,\qquad
\operatorname{bal}_3(1)=+1,\qquad
\operatorname{bal}_3(2)=-1.
$$

Then

$$
\boxed{
b_{\mathrm{next}}
=
\operatorname{bal}_3
\left([p_{\mathrm{next}}-2a_{\mathrm{next}}]_3\right),
\qquad
\sigma_{\mathrm{next}}
=
(a_{\mathrm{next}},b_{\mathrm{next}},a_{\mathrm{next}}).
}
$$

| Next phase | Outer state 0 | Outer state 1 |
|:--:|:--:|:--:|
| 0 | $(0,0,0)$ | $(+1,+1,+1)$ |
| 1 | $(0,+1,0)$ | $(+1,-1,+1)$ |
| 2 | $(0,-1,0)$ | $(+1,0,+1)$ |

**The block sum selects the row; the leftmost-cell update selects the column.**

Finish the transition by updating the counter:

$$
\boxed{S_{\mathrm{next}}=S+p_{\mathrm{next}}.}
$$

Carry $(a_{\mathrm{next}},S_{\mathrm{next}})$ into the next block. Do not reset the state between blocks.

## 7. Worked example: THEN → THE (LL)

The current block **THEN** occupies $(25,25),(25,26),(25,27)$. Its derived, unshifted key is IA–E–IA with signature $(0,+1,0)$, so $a=0$. The incoming counter is $S=18$.

**Phase.** At $S=18$, select **Reflected / +1**.

| Cell | $n_0$ | $n_2=730-n_0$ | $\mu(n_2)$ |
|:--:|--:|--:|:--:|
| $(25,25)$ | 673 | 57 | +1 |
| $(25,26)$ | 674 | 56 | 0 |
| $(25,27)$ | 675 | 55 | +1 |

$$
p_{\mathrm{next}}=[1+1+0+1]_3=0.
$$

**Outer state.** The selected cell is $L=(25,25)$:

$$
m=27(25-1)+28-25=651=3\cdot7\cdot31,
\qquad \mu(m)=-1.
$$

The sign is allowed in Reflected mode, and the outer state toggles:

$$
a_{\mathrm{next}}=[0-1]_2=1.
$$

**Complete signature.** Phase 0 and outer state 1 give

$$
\boxed{
\sigma_{\mathrm{next}}=(+1,+1,+1),\qquad
p_{\mathrm{next}}=0,\qquad
S_{\mathrm{next}}=18.
}
$$

This matches the THE (LL) key **E–TH–E = (18,2,18)**:

$$
\sigma(18,2,18)
=
\bigl(\mu(6),\mu(1),\mu(6)\bigr)
=
(+1,+1,+1).
$$

## 8. Route verification

The state is propagated from **$a=0,S=0$** at AS I GO THE. Every row uses the preceding row’s returned state.

In the table, **D1** means Direct / +1, **R0** Reflected / +0, and **R1** Reflected / +1. The sum column is evaluated in that row’s mode. Each checkmark means that **both the predicted phase and complete signature match the next key**.

| Transition | $S$ before | Mode | $\Sigma\mu$ | $p_{\mathrm{next}}$ | $\mu(m)$ | Predicted = actual signature | Match |
|:--|--:|:--:|--:|:--:|:--:|:--:|:--:|
| AS I GO THE → WEATHER | 0 | D1 | -2 | 2 | +1 | `(+1,0,+1)` | ✅ |
| WEATHER → TURNS | 2 | D1 | -1 | 0 | +1 | `(0,0,0)` | ✅ |
| TURNS → COLD | 2 | D1 | 0 | 1 | 0 | `(0,+1,0)` | ✅ |
| COLD → I MAY | 3 | D1 | -1 | 0 | 0 | `(0,0,0)` | ✅ |
| I MAY → CRY | 3 | D1 | 0 | 1 | +1 | `(+1,-1,+1)` | ✅ |
| CRY → NOW THE | 4 | D1 | +1 | 2 | 0 | `(+1,0,+1)` | ✅ |
| NOW THE → IDEA | 6 | D1 | 0 | 1 | +1 | `(0,+1,0)` | ✅ |
| IDEA → OF | 7 | R0 | 0 | 0 | -1 | `(+1,+1,+1)` | ✅ |
| OF → THE | 7 | R0 | -1 | 2 | 0 | `(+1,0,+1)` | ✅ |
| THE → END | 9 | R0 | -1 | 2 | 0 | `(+1,0,+1)` | ✅ |
| END → IS | 11 | R0 | +1 | 1 | -1 | `(0,+1,0)` | ✅ |
| IS → DEATH | 12 | R0 | -1 | 2 | -1 | `(+1,0,+1)` | ✅ |
| DEATH → SEE | 14 | R1 | -1 | 0 | -1 | `(0,0,0)` | ✅ |
| SEE → YOU | 14 | R1 | 0 | 1 | 0 | `(0,+1,0)` | ✅ |
| YOU → SOON | 15 | R1 | +1 | 2 | 0 | `(0,-1,0)` | ✅ |
| SOON → THEN | 17 | R1 | 0 | 1 | 0 | `(0,+1,0)` | ✅ |
| THEN → THE (LL) | 18 | R1 | +2 | 0 | -1 | `(+1,+1,+1)` | ✅ |

**Route convention:** OF and THE are separate blocks. SOON uses its primary X–D–W–H ciphertext route. THE (LL) denotes the continuation after THEN.

The final state at THE (LL) is **$a=1,S=18$**. The next application of the same rule returns phase **1**, signature **$(+1,-1,+1)$**, and counter **19**.

## 9. Reference implementation

The function below accepts the current ciphertext coordinates and state. It calculates the phase, complete signature, next state, selected-cell index, and mode consistency result.

<details>
<summary><strong>Python · no external dependencies</strong></summary>

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

Use a predicted signature to filter candidate keys: calculate each candidate’s signature **before its cyclic shift** and retain those equal to $\sigma_{\mathrm{next}}$. The predicted phase gives that candidate key’s cyclic left shift.

The procedure below is the complete update order:

1. Select the mode from the current $S$.
2. Sum the mode’s Möbius values over the current block.
3. Calculate $p_{\mathrm{next}}$ modulo 3.
4. Select the minimum $90^\circ$ index $m$.
5. Update the outer state modulo 2.
6. Recover the middle component and full signature.
7. Add $p_{\mathrm{next}}$ to $S$ and carry the returned state forward.

