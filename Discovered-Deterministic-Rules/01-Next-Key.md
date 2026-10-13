# Know the Next Key in Advance

Every cell in the 27×27 matrix has an absolute position from 1 to 729. I decided to investigate whether the positions of the *current ciphertext cells* could predict the Möbius phase of the *next decryption key*.

I found a surprisingly simple pattern. It matches 7 consecutive transitions from the very beginning. The predicted phases add up to 7, and the formula changes. It then matches 5 more transitions, whose phases also add up to 7. The formula changes again and matches the next 4 transitions.

This suggests a possible four-state machine: the calculation changes each time the accumulated phase sum crosses another multiple of 7. Our known plaintext appears to begin in the *Direct/+1* state, rather than at the beginning of the proposed cycle.

### Definitions

- **`C`** — the set of cell positions belonging to the current ciphertext.
- **`n`** — a cell's absolute position (`1–729`), calculated as `n = 27 × (row − 1) + column`.
- **`μ(n)`** — the Möbius function; its result is `−1`, `0`, or `+1`.
- **`p_next`** — predicted phase of the next 3-rune decryption key (`0`, `1`, or `2`).
- **`S`** — cumulative sum of the previously predicted next-key phases, initially `S = 0`.
- **`730 − n`** — the cell position reflected through the center of the 27×27 matrix (`1 ↔ 729`, `2 ↔ 728`, etc.), since `27² + 1 = 730`.

---

## 1. Direct/+1 — AS I GO THE → IDEA

Use the original cell positions and add 1:

$$
p_{\text{next}} = \left(1+\sum_{n\in C}\mu(n)\right)\bmod 3
$$

| Current ciphertext → Next key | Möbius sum | Predicted phase | Known key phase | Cumulative Σ phases |
|:--|--:|--:|--:|--:|
| `AS I GO THE` → `WEATHER` | −2 | 2 | 2 ✓ | 2 |
| `WEATHER` → `TURNS` | −1 | 0 | 0 ✓ | 2 |
| `TURNS` → `COLD` | 0 | 1 | 1 ✓ | 3 |
| `COLD` → `I MAY` | −1 | 0 | 0 ✓ | 3 |
| `I MAY` → `CRY` | 0 | 1 | 1 ✓ | 4 |
| `CRY` → `NOW THE` | +1 | 2 | 2 ✓ | 6 |
| `NOW THE` → `IDEA` | 0 | 1 | 1 ✓ | 7 |

Result: 7/7 matches. The predicted phases 2 + 0 + 1 + 0 + 1 + 2 + 1 sum to 7. In the proposed model, this triggers the first state change.

---

## 2. Reflected/+0 — IDEA → DEATH

At cumulative `S = 7`, the model switches to *reflected cell positions* (`730 − n`) and does not add 1:

$$
p_{\text{next}} = \left(\sum_{n\in C}\mu(730-n)\right)\bmod 3
$$

| Current ciphertext → Next key | Möbius sum | Predicted phase | Known key phase | Cumulative Σ phases |
|:--|--:|--:|--:|--:|
| `IDEA` → `OF` | 0 | 0 | 0 ✓ | 7 |
| `OF` → `THE` | −1 | 2 | 2 ✓ | 9 |
| `THE` → `END` | −1 | 2 | 2 ✓ | 11 |
| `END` → `IS` | +1 | 1 | 1 ✓ | 12 |
| `IS` → `DEATH` | −1 | 2 | 2 ✓ | 14 |

Result: 5/5 matches. These predicted phases 0 + 2 + 2 + 1 + 2 also sum to 7, bringing the cumulative sum to 14 and triggering another proposed state change.

---

## 3. Reflected/+1 — DEATH → THEN

At cumulative `S = 14`, the positions remain reflected, but +1 returns:

$$
p_{\text{next}} = \left(1+\sum_{n\in C}\mu(730-n)\right)\bmod 3
$$

| Current ciphertext → Next key | Möbius sum | Predicted phase | Known key phase | Cumulative Σ phases |
|:--|--:|--:|--:|--:|
| `DEATH` → `SEE` | −1 | 0 | 0 ✓ | 14 |
| `SEE` → `YOU` | 0 | 1 | 1 ✓ | 15 |
| `YOU` → `SOON` | +1 | 2 | 2 ✓ | 17 |
| `SOON` → `THEN` | 0 | 1 | 1 ✓ | 18 |

Result: 4/4 matches. The four phases sum to 4, leaving the overall cumulative total at 18, below the next proposed threshold of 21.

---

## Hypothesis: a closed cycle of four states

The proposed full cycle is:

*Direct/+0 → Direct/+1 → Reflected/+0 → Reflected/+1 → Direct/+0 → ...*

Our known route appears to start at *Direct/+1*. So the sequence observed so far is:

*Direct/+1 → Reflected/+0 → Reflected/+1 → [Direct/+0 predicted next]*

## Direct/+0 (predicted fourth state)

$$
p_{\text{next}}=\left(\sum_{n\in C}\mu(n)\right)\bmod 3
$$

## After THEN

The `THEN` ciphertext occupies 673, 674, 675. The current accumulated total is `S = 18`, so the model stays in `Reflected/+1`:

```text
Current cell positions:    673, 674, 675
Reflected cell positions:   57,  56,  55
Möbius values:             +1,   0,  +1
Möbius sum:                 2
Predicted next phase:      (1 + 2) mod 3 = 0
```
