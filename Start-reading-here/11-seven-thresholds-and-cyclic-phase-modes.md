# Seven-Phase Thresholds and Cyclic Mode Transitions

**Status: proposed continuation filter and cyclic extension of [Report 01](01-next-key-signature.md).** The 34 selected plaintext blocks satisfy the no-skipping condition. A return to **Direct/+1** at `S = 28` follows from the proposed cyclic extension.

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

**Application order:** Predict the next phase using the active formula from Report 01; apply this filter to the resulting phase and accumulated sum. Do **not** change a predicted phase of `2` into `1` just to pass the filter. If the deterministic prediction skips a threshold, that proposed transition is incompatible with this additional rule.

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

## 4. Four exact threshold hits in the selected 34-block route

The phase values below are taken from the keys documented in [`plaintext-i-found/`](../plaintext-i-found/). The accumulating sum reaches every successive threshold without skipping one.

| Block | Plaintext | Phase | S before | S after | Mode after |
| ---: | :--- | ---: | ---: | ---: | :--- |
| **08** | **IDEA** | **1** | **6** | **7** | **Reflected/+0** |
| **13** | **DEATH** | **2** | **12** | **14** | **Reflected/+1** |
| **23** | **TO** | **1** | **20** | **21** | **Direct/+0** |
| **34** | **YOU** | **1** | **27** | **28** | **Direct/+1*** |

The last three threshold words, taken in numerical order, read:

> **DEATH TO YOU**

This is an intelligible English phrase. The highlighted words are **not consecutive words in the plaintext**: they come from blocks `13`, `23`, and `34`, at `S = 14, 21, 28`. The earlier threshold word is **IDEA** (`S = 7`), which can be *interpreted* as an introductory label, yielding the secondary reading **“IDEA: DEATH TO YOU.”**

## 5. Complete phase trace (34 selected blocks)

| # | Block | p | S before | S after | Mode after |
| ---: | :--- | ---: | ---: | ---: | :--- |
| 01 | AS I GO THE | 0 | 0 | 0 | D+1 |
| 02 | WEATHER | 2 | 0 | 2 | D+1 |
| 03 | TURNS | 0 | 2 | 2 | D+1 |
| 04 | COLD | 1 | 2 | 3 | D+1 |
| 05 | I MAY | 0 | 3 | 3 | D+1 |
| 06 | CRY | 1 | 3 | 4 | D+1 |
| 07 | NOW THE | 2 | 4 | 6 | D+1 |
| **08** | **IDEA** | **1** | **6** | **7** | **R+0** |
| 09 | OF | 0 | 7 | 7 | R+0 |
| 10 | THE | 2 | 7 | 9 | R+0 |
| 11 | END | 2 | 9 | 11 | R+0 |
| 12 | IS | 1 | 11 | 12 | R+0 |
| **13** | **DEATH** | **2** | **12** | **14** | **R+1** |
| 14 | SEE | 0 | 14 | 14 | R+1 |
| 15 | YOU | 1 | 14 | 15 | R+1 |
| 16 | SOON | 2 | 15 | 17 | R+1 |
| 17 | THEN | 1 | 17 | 18 | R+1 |
| 18 | THE | 0 | 18 | 18 | R+1 |
| 19 | KEY | 1 | 18 | 19 | R+1 |
| 20 | IS | 1 | 19 | 20 | R+1 |
| 21 | TO | 0 | 20 | 20 | R+1 |
| 22 | GO | 0 | 20 | 20 | R+1 |
| **23** | **TO** | **1** | **20** | **21** | **D+0** |
| 24 | THE | 1 | 21 | 22 | D+0 |
| 25 | EAST | 1 | 22 | 23 | D+0 |
| 26 | OF | 0 | 23 | 23 | D+0 |
| 27 | THE | 0 | 23 | 23 | D+0 |
| 28 | MAP LIFE | 1 | 23 | 24 | D+0 |
| 29 | MAY | 0 | 24 | 24 | D+0 |
| 30 | BE | 0 | 24 | 24 | D+0 |
| 31 | THE | 0 | 24 | 24 | D+0 |
| 32 | DEATH | 1 | 24 | 25 | D+0 |
| 33 | OF | 2 | 25 | 27 | D+0 |
| **34** | **YOU** | **1** | **27** | **28** | **D+1** |

`D` = Direct; `R` = Reflected. The displayed **mode after** is the one selected for the **next** prediction. The 34 recorded phases contain **13 zeros, 14 ones, and 7 twos**, for a final sum of **28**. `MAP LIFE` is **one continuous ciphertext block** and contributes its phase only once.

## 6. Conditional prediction after YOU

Rule B makes a specific, testable prediction that the original finite schedule in Report 01 does **not** make.

At **YOU (34)**, `S = 28`; thus the proposed cycle selects **Direct/+1** for the transition to block 35. The three current ciphertext cells are `(6,11)`, `(6,12)`, `(6,13)`:

| Cell | n | μ(n) |
| :--- | ---: | ---: |
| (6,11) | 146 | +1 |
| (6,12) | 147 | 0 |
| (6,13) | 148 | 0 |

Therefore:

$$
p_{35}=(1+1+0+0)\bmod3=\boxed{2}.
$$

The outer signature state of YOU is `a = 0`. Its leftmost cell `(6,11)` gives the 90° clockwise index `m = 27(11−1)+28−6 = 292` and `μ(292)=0`, so the outer state remains `a_{35}=0`. Applying Report 01's signature table gives:

**Conditional next-key prediction: `p₃₅ = 2`, signature `(0,−1,0)`, and `S₃₅ = 30`.**
