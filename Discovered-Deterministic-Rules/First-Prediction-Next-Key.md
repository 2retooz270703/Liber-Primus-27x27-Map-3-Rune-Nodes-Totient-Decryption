# First Prediction: Know the Next Key in Advance

> **Research finding — 16 matching transitions across three phases of the rule.**  
> This is a mathematical pattern found in the *proposed* 27×27 plaintext route.

## The idea

Every cell in the 27×27 matrix has an **absolute position from 1 to 729**. I investigated whether the positions of the **current ciphertext cells** could reveal the Möbius phase (0, 1, or 2) of the **next decryption key**.

I found a simple relationship that reproduces **7 consecutive transitions from the very beginning**. After those 7 predictions, their phases add up to **7**, and the calculation changes. It then reproduces **5 more transitions**, whose phases also add up to **7**. The calculation changes again and reproduces **4 further transitions**.

The three matching sections are shown below. **`OF` and `THE` must be treated as separate decryption-key operations**, because they use different keys and phases.

### Definitions

- **`n`** — the absolute position (1–729) of a cell in the *current* ciphertext, calculated as `n = 27 × (row − 1) + column`.
- **`μ(n)`** — the Möbius function, which returns `−1`, `0`, or `+1`.
- **`p_next`** — predicted phase of the *next* 3-rune key (`0`, `1`, or `2`).
- **`S`** — cumulative sum of the **previously predicted** next-key phases, starting at `S = 0`.
- **`730 − n`** — the centrally reflected cell position, because `27² + 1 = 730` (cell `1 ↔ 729`, `2 ↔ 728`, etc.).

---

## 1. Direct mode — First 7 transitions

**Formula:**

$$
p_{\text{next}} = \left(1+\sum_{n\in C}\mu(n)\right)\bmod 3
$$

Use the **original ciphertext cell positions** and **add 1**.

| Current ciphertext → Next key | Möbius sum | Predicted phase | Actual phase | Cumulative Σ phases |
|:--|--:|--:|--:|--:|
| `AS I GO THE` → `WEATHER` | -2 | **2** | 2 ✓ | **2** |
| `WEATHER` → `TURNS` | -1 | **0** | 0 ✓ | **2** |
| `TURNS` → `COLD` | 0 | **1** | 1 ✓ | **3** |
| `COLD` → `I MAY` | -1 | **0** | 0 ✓ | **3** |
| `I MAY` → `CRY` | 0 | **1** | 1 ✓ | **4** |
| `CRY` → `NOW THE` | +1 | **2** | 2 ✓ | **6** |
| `NOW THE` → `IDEA` | 0 | **1** | 1 ✓ | **7** |

**Result: 7/7 matches.** The predicted phases are `2, 0, 1, 0, 1, 2, 1`; their cumulative sum reaches **7** immediately after `NOW THE → IDEA`.

---

## 2. Mirror mode — IDEA → DEATH (5 transitions)

Once `S = 7`, the rule appears to enter a **mirror mode**: replace every ciphertext position `n` with `730 − n` and **do not add 1**.

**Formula:**

$$
p_{\text{next}} = \left(\sum_{n\in C}\mu(730-n)\right)\bmod 3
$$

| Current ciphertext → Next key | Möbius sum | Predicted phase | Actual phase | Cumulative Σ phases |
|:--|--:|--:|--:|--:|
| `IDEA` → `OF` | 0 | **0** | 0 ✓ | **7** |
| `OF` → `THE` | -1 | **2** | 2 ✓ | **9** |
| `THE` → `END` | -1 | **2** | 2 ✓ | **11** |
| `END` → `IS` | +1 | **1** | 1 ✓ | **12** |
| `IS` → `DEATH` | -1 | **2** | 2 ✓ | **14** |

**Result: 5/5 matches.** The predicted phases are `0, 2, 2, 1, 2`; their sum is **7**, so the overall cumulative sum reaches **14** after `IS → DEATH`.

---

## 3. Mirror mode + 1 — DEATH → THEN (4 transitions)

Once `S = 14`, the reflected positions remain in use, but **+1 returns**.

**Formula:**

$$
p_{\text{next}} = \left(1+\sum_{n\in C}\mu(730-n)\right)\bmod 3
$$

| Current ciphertext → Next key | Möbius sum | Predicted phase | Actual phase | Cumulative Σ phases |
|:--|--:|--:|--:|--:|
| `DEATH` → `SEE` | -1 | **0** | 0 ✓ | **14** |
| `SEE` → `YOU` | 0 | **1** | 1 ✓ | **15** |
| `YOU` → `SOON` | +1 | **2** | 2 ✓ | **17** |
| `SOON` → `THEN` | 0 | **1** | 1 ✓ | **18** |

**Result: 4/4 matches.** The predicted phases are `0, 1, 2, 1`; their sum is **4**. Therefore, the total accumulated phase sum at the end of `SOON → THEN` is **18**, still below the next suggested threshold of 21.

---

## One possible deterministic mechanism: a phase budget of 7

Instead of hard-coding the three sections by word name, the model can switch modes **using only the running sum of its own predictions**:

1. Start at `S = 0`.
2. Before each transition, set `q = floor(S / 7)`.
3. If `S < 7`, use `n`; otherwise, use the reflected position `730 − n`.
4. Add `b = 1 − (q mod 2)` to the Möbius sum; take the result modulo 3.
5. Update `S ← S + p_next` and continue.

In compact form:

```text
S = 0
for each known current ciphertext C:
    q = floor(S / 7)
    b = 1 - (q mod 2)
    X = positions(C)               if S < 7
        [730 - n for n in C]       otherwise
    p_next = (b + sum(mu(x) for x in X)) mod 3
    S = S + p_next
```

The observed regimes are **`S = 0…6` → direct/+1**, **`S = 7…13` → reflected/+0**, and **`S = 14…20` → reflected/+1**. The first 16 steps match **without feeding the actual phases back into `S`**. What happens at `S ≥ 21` is an **untested extrapolation**.

### Why the number 7 is interesting

- The first matching section contains **7 transitions**, and its predicted phase sum is **7**.
- The next matching section contains **5 transitions**, but its phase sum is again **7**.
- The formula changes at cumulative totals **7** and **14**, not simply after a fixed number of words.
- On the currently tested route, this produces **16/16 matching next-key phases** across three modes.

These are exact properties of the recorded sequence, but the threshold and mode switches were **identified after inspecting the known stages**. They are not yet an independently established rule of the cipher.

## New test: the predicted phase after THEN

The `THEN` ciphertext occupies absolute positions **673, 674, 675**. At this point `S = 18`, so the proposed rule still uses **mirror mode +1**:

```text
Current positions:   673, 674, 675
Reflected positions:   57,  56,  55
Möbius values:         +1,   0,  +1
Möbius sum:            2
Next phase:           (1 + 2) mod 3 = 0
```

### **Prediction: the next true decryption key after THEN has phase 0.**

Every fixed 3-rune key has **only one Möbius phase**, so a predicted phase can eliminate incompatible candidate keys. **However, many different nodes can share phase 0:** the phase alone does *not* uniquely identify the correct 3-rune mirror or prove a candidate plaintext. Geometry, separators, and a valid next route are still required.

## Verification limits

- **16/16 is an exact fit to a previously known candidate route**, not 16 independently predicted discoveries; the threshold 7, reflection rule, and offsets were developed during analysis.
- The model uses the **primary `SOON` ciphertext route (positions 664–667)**. Using the alternative route (726–729) changes the prediction and breaks the match to `THEN`.
- The model predicts a **phase conditional on a selected current ciphertext**. It does not itself determine which ciphertext cells, mirror, or route to choose next.
- A robust validation would freeze the model **before** a new stage is discovered, then find the next key using independent geometric constraints and check whether its phase equals the predicted **0**.

**Bottom line:** the phase-budget model is a compact and reproducible **hypothesis** linking absolute ciphertext positions, the Möbius function, reflection of the 27×27 matrix, and cumulative phase totals. Its most useful contribution is a falsifiable prediction after `THEN`.
