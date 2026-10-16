# Unified Geometric Key Prediction — 27×27 Matrix

**Phase, Möbius signature, and the 90° sign constraint**

> **Scope:** The proposed model reproduces the next-key **phase and complete Möbius signature in 16/16 recorded transitions**, from `AS I GO THE → WEATHER` through `SOON → THEN`. The additional sign constraint holds for **17/17 known ciphertext blocks**, including `THEN`. The key *after* `THEN` remains unknown, so its predicted signature is **not verified**.

This document combines the results previously recorded in `Next-Key.md` and `Predicted-Signature.md` and explains their shared geometry. All numerical matches below refer to the selected plaintext/key route in the supplied 27×27 map, **not** to an independently confirmed Cicada 3301 decryption.

---

## 1. Definitions and inputs

For a 27×27 matrix, with **one-based** rows `r` (top to bottom) and columns `c` (left to right):

| Symbol | Meaning |
|:--|:--|
| `C` | Set of `(r,c)` positions in the **current** ciphertext block; its boundaries and reading route must already be known. |
| `n(r,c)` | Original absolute position: `27(r−1)+c`, between 1 and 729. |
| `μ(n)` | Möbius function: `−1`, `0`, or `+1`. Zero means the number has a squared prime factor. |
| `φ(n)` | Euler's totient function. |
| `K=(k₁,k₂,k₃)` | **Derived, unrotated** three-rune key (including any center-totient transformation used to derive it); `kᵢ` are rune indices, modulo 29. |
| `σ(K)` | Möbius signature `(μ(φ(k₁)), μ(φ(k₂)), μ(φ(k₃)))`. |
| `p` | Phase label, `p = (sum of the three signature components) mod 3`. |
| `S` | Cumulative sum of previously predicted **next-key** phases, initially `S=0`. |
| `a` | Shared outer component of the **current** unrotated key's signature, either 0 or +1. |

The 17 recorded keys satisfy the empirical signature class

$$
\sigma(K)=(a,b,a),\qquad a\in\{0,1\},\qquad b\in\{-1,0,+1\}
$$

The first key, `AE–I–EA`, has `σ=(0,0,0)`, so the initial outer state is **`a=0`**. This is an observed property of that key, not an arbitrary seed. The signature describes *numerical* Möbius values; the two outer runes need not be identical (e.g. `AE–I–EA`, `H–NG–C`, and `L–R–EA`).

---

## 2. The shared geometry: 0°, 90°, and 180°

Define a **90° clockwise** rotation of cell coordinates:

$$
R(r,c)=(c,28-r)
$$

Applying it twice gives

$$
R^2(r,c)=(28-r,28-c)
$$

The original absolute position is `n=27(r−1)+c`. After the 180° rotation:

$$
\begin{aligned}
n\bigl(R^2(r,c)\bigr)&=27(27-r)+(28-c)\\
&=730-[27(r-1)+c]\\
&=730-n
\end{aligned}
$$

**Thus the `730−n` operation in the phase rule is exactly the same as two applications of the `90° clockwise` rotation in the signature rule.** It is a half-turn about the matrix center (point reflection), not reflection across a single horizontal or vertical axis.

| Power of `R` | Matrix operation | Role in the proposed model |
|:--:|:--|:--|
| `R⁰` | 0° / original positions, `n` | **Direct** phase sum |
| `R¹` | 90° clockwise, `27(c−1)+28−r` | Selects one cell for **outer-signature update** and **sign constraint** |
| `R²` | 180° / center reflection, `730−n` | **Reflected** phase sum |
| `R³` | 270° clockwise | No role established by these two rules |

**Important distinction:** The identity `R² = central reflection` is a mathematical fact. Whether Cicada intentionally used these powers of a common rotation is a separate, unproven interpretation.

---

## 3. Rule A — next-key phase from all ciphertext cells

For each ciphertext cell compute `n=27(r−1)+c`. The phase prediction is

$$
p_{\mathrm{next}}=\left(\delta+\sum_{(r,c)\in C}\mu\bigl(T(n(r,c))\bigr)\right)\bmod 3
$$

The position transform `T` and additive constant `δ` depend on the **current** cumulative phase total `S`:

| Before the transition | Mode | `T(n)` | `δ` | Status |
|:--|:--|:--:|:--:|:--|
| `0 ≤ S < 7` | **Direct/+1** | `n` | `1` | Observed: 7 transitions |
| `7 ≤ S < 14` | **Reflected/+0** | `730−n` | `0` | Observed: 5 transitions |
| `14 ≤ S < 21` | **Reflected/+1** | `730−n` | `1` | Observed: 4 transitions; also applies to `THEN` |
| `21 ≤ S < 28` | **Direct/+0** | `n` | `0` | **Hypothetical fourth state; not yet tested** |

After predicting the phase, update the cumulative sum:

$$
S_{\mathrm{next}}=S+p_{\mathrm{next}}
$$

The first seven predicted phases are `2,0,1,0,1,2,1`, reaching `S=7`. The next five are `0,2,2,1,2`, reaching `S=14`. The final four recorded transitions are `0,1,2,1`, reaching `S=18`.

The hypothesized full state sequence is

`Direct/+0 → Direct/+1 → Reflected/+0 → Reflected/+1 → Direct/+0 → …`

The observed route **starts at Direct/+1**. Only the first three modes have recorded next-key comparisons; the fourth and any repeated cycle are extrapolations. The switching thresholds 7 and 14 were identified from this route, not independently fixed in advance.

---

## 4. Rule B — the next outer signature state from one 90°-rotated cell

For every cell `(r,c)` in the **current** ciphertext, its absolute position after the 90° clockwise rotation is

$$
n_{90}(r,c)=27(c-1)+28-r
$$

Select the **minimum** rotated position:

$$
m(C)=\min_{(r,c)\in C}\left[27(c-1)+28-r\right]
$$

Without physically rotating the matrix, this means:

1. Find the **leftmost occupied column** of the current ciphertext.
2. If several cells are in that column, choose the **bottommost** one.
3. Calculate its rotated position `m` using the formula above.

The selected cell can be the start, end, or an interior cell of the ciphertext. The selection rule is always the same.

Update the shared outer signature component:

$$
a_{\mathrm{next}}=(a+\mu(m))\bmod 2
$$

| `μ(m)` | Arithmetic | Meaning |
|:--:|:--|:--|
| `0` | `a_next=a` | Preserve the outer state |
| `+1` or `−1` | `a_next=1−a` | Toggle the outer state |

Both nonzero values behave identically **modulo 2**. Equivalently: **toggle if `m` is square-free; otherwise preserve the state**.

### Recover the *entire* next-key signature

For the observed `(a,b,a)` signature class, the phase obeys

$$
p_{\mathrm{next}}\equiv 2a_{\mathrm{next}}+b_{\mathrm{next}}\pmod{3}
$$

so

$$
b_{\mathrm{next}}\equiv p_{\mathrm{next}}-2a_{\mathrm{next}}\pmod{3}
$$

Interpret residues as `0 → 0`, `1 → +1`, `2 → −1`:

| Predicted phase | `a_next=0` | `a_next=1` |
|:--:|:--:|:--:|
| `0` | `(0,0,0)` | `(+1,+1,+1)` |
| `1` | `(0,+1,0)` | `(+1,−1,+1)` |
| `2` | `(0,−1,0)` | `(+1,0,+1)` |

**Rule A predicts the row of this table; Rule B predicts its column.** The middle component is determined algebraically, not obtained from a third independent rule.

---

## 5. Rule C — Direct/Reflected sign constraint on the same 90° cell

The same `m(C)` also satisfies an observed sign restriction:

$$
\text{Direct:}\quad \mu(m)\in\{0,+1\}\qquad \text{Reflected:}\quad \mu(m)\in\{0,-1\}
$$

- **Direct/+1:** 4 occurrences of `+1`, 3 of `0`, none of `−1`.
- **Reflected/+0 and Reflected/+1, combined over the 16 transitions:** 4 occurrences of `−1`, 5 of `0`, none of `+1`.
- **`THEN` itself:** `μ(m)=−1`, another passing Reflected/+1 block. Thus **17/17 known ciphertext blocks** satisfy the restriction, although the next key for `THEN` is unverified.

The sign restriction changes when the position transform switches from `n` to `730−n` at **`S=7`**. It does **not** change when only the offset switches from `+0` to `+1` at **`S=14`**. This suggests a possible connection to the *geometric mode*, not the additive constant.

### Prime-factor parity behind the Direct/Reflected sign split

The sign of the Möbius function has a simple arithmetic interpretation. For a **square-free** integer `m`, let `ω(m)` be its number of **distinct prime factors**. Then:

$$
\mu(m)=(-1)^{\omega(m)}
$$

Thus **an even number of distinct prime factors gives `μ(m)=+1`**, while **an odd number gives `μ(m)=−1`**. If any prime factor is repeated, `μ(m)=0` and the parity rule does not apply.

The following are **all the selected positions with nonzero `μ(m)`** among the 17 known ciphertext blocks (including `THEN`):

**Direct mode — `μ(m)=+1`**

| Current ciphertext | Rotated position `m` | Prime factorization | `ω(m)` |
|:--|--:|:--|--:|
| `AS I GO THE` | 14 | `2 × 7` | 2 |
| `WEATHER` | 365 | `5 × 73` | 2 |
| `I MAY` | 407 | `11 × 37` | 2 |
| `NOW THE` | 422 | `2 × 211` | 2 |

All **four** nonzero Direct cases have **exactly two distinct prime factors**, not merely an even number.

**Reflected mode — `μ(m)=−1`**

| Current ciphertext | Rotated position `m` | Prime factorization | `ω(m)` |
|:--|--:|:--|--:|
| `IDEA` | 470 | `2 × 5 × 47` | 3 |
| `END` | 601 | `601` (prime) | 1 |
| `IS` | 223 | `223` (prime) | 1 |
| `DEATH` | 2 | `2` (prime) | 1 |
| `THEN` | 651 | `3 × 7 × 31` | 3 |

All **five** nonzero Reflected cases have an **odd number of distinct prime factors**: one or three. The `THEN` position provides the fifth such example; its following key is still unknown.

**Interpretation:** The Direct/Reflected sign restriction can be expressed as **even/odd prime-factor parity for square-free selected positions**. This is an *arithmetic explanation of Rule C*, **not** a separate independent prediction: the parity distinction follows from the definition of `μ`. The more specific observation that all four nonzero Direct positions have exactly *two* distinct prime factors is descriptive and has not been tested on new ciphertexts.

A compact combined notation is

$$
\varepsilon=+1\ \text{(Direct)},\qquad \varepsilon=-1\ \text{(Reflected)};\qquad q=\varepsilon\mu(m)
$$

**If the sign rule holds**, then `q∈{0,1}` and the outer-state update can be written

$$
a_{\mathrm{next}}=(a+q)\bmod 2
$$

Here `q=1` means *toggle* and `q=0` means *preserve*. This unifies the notation, but **it is not a new independent 16/16 result**: Rule B already uses `μ(m) mod 2`, and Rule C constrains the **sign of that same number**. In the 16 transitions, only eight nonzero values actually distinguish the two mode-specific sign sets; zero is allowed in both.

---

## 6. Combined verification — all 16 recorded transitions

All values below are calculated from the selected route's current ciphertext coordinates and key signatures. `D+1 = Direct/+1`, `R+0 = Reflected/+0`, `R+1 = Reflected/+1`. `Σμ` uses the regime's position transform; `S` is the **total after** that transition. In the last column, the predicted complete signature **equals the recorded next-key signature in every row**. Each row also passes Rule C.

| # | Current ciphertext → next key | Mode | `Σμ` | `p_next` | `S` | `m` | `μ(m)` | `a → a_next` | Predicted = observed `σ_next` |
|--:|:--|:--:|--:|--:|--:|--:|--:|:--:|:--:|
| 1 | `AS I GO THE` → `WEATHER` | D+1 | −2 | 2 | 2 | 14 | +1 | 0→1 | `(+1,0,+1)` |
| 2 | `WEATHER` → `TURNS` | D+1 | −1 | 0 | 2 | 365 | +1 | 1→0 | `(0,0,0)` |
| 3 | `TURNS` → `COLD` | D+1 | 0 | 1 | 3 | 500 | 0 | 0→0 | `(0,+1,0)` |
| 4 | `COLD` → `I MAY` | D+1 | −1 | 0 | 3 | 176 | 0 | 0→0 | `(0,0,0)` |
| 5 | `I MAY` → `CRY` | D+1 | 0 | 1 | 4 | 407 | +1 | 0→1 | `(+1,−1,+1)` |
| 6 | `CRY` → `NOW THE` | D+1 | +1 | 2 | 6 | 414 | 0 | 1→1 | `(+1,0,+1)` |
| 7 | `NOW THE` → `IDEA` | D+1 | 0 | 1 | 7 | 422 | +1 | 1→0 | `(0,+1,0)` |
| 8 | `IDEA` → `OF` | R+0 | 0 | 0 | 7 | 470 | −1 | 0→1 | `(+1,+1,+1)` |
| 9 | `OF` → `THE` | R+0 | −1 | 2 | 9 | 388 | 0 | 1→1 | `(+1,0,+1)` |
| 10 | `THE` → `END` | R+0 | −1 | 2 | 11 | 414 | 0 | 1→1 | `(+1,0,+1)` |
| 11 | `END` → `IS` | R+0 | +1 | 1 | 12 | 601 | −1 | 1→0 | `(0,+1,0)` |
| 12 | `IS` → `DEATH` | R+0 | −1 | 2 | 14 | 223 | −1 | 0→1 | `(+1,0,+1)` |
| 13 | `DEATH` → `SEE` | R+1 | −1 | 0 | 14 | 2 | −1 | 1→0 | `(0,0,0)` |
| 14 | `SEE` → `YOU` | R+1 | 0 | 1 | 15 | 352 | 0 | 0→0 | `(0,+1,0)` |
| 15 | `YOU` → `SOON` | R+1 | +1 | 2 | 17 | 408 | 0 | 0→0 | `(0,−1,0)` |
| 16 | `SOON` → `THEN` | R+1 | 0 | 1 | 18 | 408 | 0 | 0→0 | `(0,+1,0)` |

**Results on this fixed route:**

- Phase: **16/16** next-key phase matches (7 + 5 + 4 by regime).
- Complete three-component signature: **16/16** matches, with the outer state propagated **recursively** from the first key rather than reset to each observed next state.
- Selected-cell sign: **16/16** on transitions, plus `THEN` itself = **17/17 known ciphertext blocks**.
- The combined figures are **not independent statistical trials**: phase and signature are algebraically linked, and Rules B/C both use `μ(m)`.

### Examples worth checking by hand

**`I MAY → CRY`:** The leftmost selected cell is `E(26,16)`, giving `m=407=11×37` and `μ(m)=+1` in Direct mode. Thus `a:0→1`; the phase prediction is `p_next=1`, giving `b_next=−1` and the complete signature **`(+1,−1,+1)`**.

**`IDEA → OF`:** The selected cell is `D(17,18)`, giving `m=470=2×5×47` and `μ(m)=−1` in Reflected mode. Thus `a:0→1`; the phase prediction is `p_next=0`, giving `b_next=+1` and **`(+1,+1,+1)`**.

**`YOU → SOON`:** The selected cell is `X(25,16)`, giving `m=408=2³×3×17` and `μ(m)=0`. Thus `a` stays 0; `p_next=2` gives **`(0,−1,0)`** for the primary `SOON` route.

The table treats `OF` and `THE` as **separate ciphertext blocks** and uses the **primary `X–D–W–H` route for `SOON`**, not its alternative `P–S–U–W` reading. Changing the selected plaintext route may change the recorded fit.

---

## 7. The prediction after `THEN` (not yet verified)

The current ciphertext `THEN` occupies the runes:

| Cell | Rune | Original absolute position |
|:--:|:--:|--:|
| `(25,25)` | L | 673 |
| `(25,26)` | T | 674 |
| `(25,27)` | W | 675 |

Its derived **unrotated** key is `IA–E–IA`, whose signature is `(0,+1,0)`. Thus the current outer state is `a=0`. The cumulative phase total is `S=18`, within **Reflected/+1**.

### 7.1 Phase of the next key

Use the **180°** positions `730−n`:

| `n` | `730−n` | `μ(730−n)` |
|--:|--:|:--:|
| 673 | 57 | +1 |
| 674 | 56 | 0 |
| 675 | 55 | +1 |

$$
p_{\mathrm{next}}=(1+1+0+1)\bmod 3=0
$$

The cumulative total remains **`S_next=18`**.

### 7.2 Outer state of the next key and the `THEN` sign check

The selected cell for `THEN` is **`L(25,25)`**. Rotate 90° clockwise:

$$
\begin{aligned}
m&=27(25-1)+28-25=651\\
651&=3\times7\times31\\
\mu(651)&=-1
\end{aligned}
$$

The `−1` sign **passes the Reflected/+1 restriction**. This is a verified calculation for the known `THEN` ciphertext, **not** a verified next key.

The outer state switches:

$$
a_{\mathrm{next}}=(0-1)\bmod 2=1
$$

For phase 0 and outer state 1, the central value is also +1:

$$
\sigma(K_{\mathrm{next}})=(+1,+1,+1),\qquad p_{\mathrm{next}}=0
$$

| Property | Result | Verification status |
|:--|:--|:--|
| `THEN` rotated-cell sign | `μ(651)=−1`, allowed in Reflected/+1 | **Verified for the known ciphertext** |
| Next-key phase | `0` | **Prediction only** |
| Next-key complete signature | `(+1,+1,+1)` | **Prediction only** |
| Next ciphertext's selected-cell sign | `μ(m_next) ∈ {−1,0}` while still Reflected | **Prediction only** |
| Return to Direct/+0 at `S=21` | `μ(m) ∈ {0,+1}` in that mode | **Hypothetical extrapolation** |

The existing search documented in `Predicted-Signature.md` counted **155** eligible equally spaced mirror nodes under the phase-only filter, reduced to **44 nodes / 26 distinct three-rune keys** after imposing `(+1,+1,+1)`. Those are *candidate counts under that search's assumptions*, not independently verified evidence that one of them is the intended key. The signature still does **not** determine the exact key, next ciphertext location, reading direction, length, or plaintext.

---

## 8. Minimal algorithm

The following reproduces the proposed state updates **given** the current ciphertext coordinates, its existing derived-key outer state `a`, and cumulative total `S`:

```python
from sympy import mobius


def predict_next(cells, a, S):
    # cells: list of (row, column), with one-based coordinates
    if 0 <= S < 7:       reflected, delta = False, 1
    elif 7 <= S < 14:    reflected, delta = True, 0
    elif 14 <= S < 21:   reflected, delta = True, 1
    elif 21 <= S < 28:   reflected, delta = False, 0  # untested
    else:
        raise ValueError("Further cycle extrapolation not established")

    original = [27*(r-1) + c for r, c in cells]
    total = sum(int(mobius(730-n if reflected else n)) for n in original)
    p_next = (delta + total) % 3

    m = min(27*(c-1) + 28-r for r, c in cells)
    mu_m = int(mobius(m))
    sign_ok = mu_m in ((-1, 0) if reflected else (0, 1))

    a_next = (a + mu_m) % 2
    b_next = {0: 0, 1: +1, 2: -1}[(p_next - 2*a_next) % 3]
    sigma_next = (a_next, b_next, a_next)

    return p_next, sigma_next, S + p_next, m, mu_m, sign_ok
```

For the recorded route, start with **`a=0, S=0`** at `AS I GO THE`; pass the returned `a_next` (the first and last component of `sigma_next`) and new `S` to the next ciphertext block. This requires no observed-next-key correction between transitions.

---

## 9. Evidence, dependencies, and what would constitute a stronger test

**Established mathematically:** `R²(r,c)=(28-r,28-c)`, which produces `730−n` under absolute numbering; the algebra converting `(p_next,a_next)` into the central Möbius component; and the documented arithmetic of each selected `m`.

**Observed on the chosen route:** Three phase regimes reproduce 16 next-key phases; the 90° minimum rule reproduces 16 recursively updated outer states; the resulting complete signatures match all 16 next keys; the Direct/Reflected sign restriction holds on 17 known ciphertext blocks including `THEN`.

**Not established:** That these patterns were intentionally planted by Cicada; that the recorded plaintext/key route is uniquely correct; that `S=7,14,21` are genuine cipher control thresholds rather than fitted regularities; that the fourth phase regime exists; or that the extrapolated `(+1,+1,+1)` key produces the intended plaintext after `THEN`.

The strongest next test is **prospective**: fix the predictions above before selecting a continuation, derive a defensible next key and ciphertext by independently motivated geometric rules, and check whether the candidate satisfies the frozen phase/signature/sign constraints *without redefining the rule to fit it*. Testing alternative branches, false-positive rates, and competing geometric selectors matters as much as the in-sample 16/16 fit.

### Source notes

- Consolidated from the supplied `Next-Key.md` (phase regimes, 90° sign observation) and `Predicted-Signature.md` (outer-state update and full-signature reconstruction).
- Ciphertext coordinates / selected reading route: `plaintext-i-found/` in the supplied `Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption` repository.
- The **90°/180° identity** and its algebraic implications are written explicitly here; this identity is exact regardless of whether the predictive hypotheses are ultimately valid.
