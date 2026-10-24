# Predicting the Next Key's Mirror Status

**A Key-Node Geometry and Modulo-3 Prediction Report**

*27 × 27 matrix · Original key-node outer cells · Ciphertext leftmost cell · Chebyshev distance · Mirror versus non-mirror*

---

The earlier reports investigate the next decryption key's Möbius signature, the following ciphertext's direction and position, and several coordinate restrictions. A separate question remains: **can the current ciphertext and its original key node predict whether the *next* key-generating node is a mirror?**

A compact geometric condition appears in the recorded *Liber Primus* LP2 pages 0–2 reconstruction. Take the **later outer cell of the current original three-rune key node**, measured by its absolute row-major position, and the **leftmost cell of the current ciphertext**. Their distance in eight-direction grid steps, reduced **modulo 3**, separates the recorded next nodes into two classes:

> **Remainder 2 predicts a non-mirrored next key node; remainders 0 and 1 predict a mirrored next key node.**

The rule matches **16/16 recorded transitions** from the initial `AS I GO THE` block through `THEN`: **14 mirror predictions and 2 non-mirror predictions**. It also matches **5/5 transitions** on the *selected candidate* continuation `THE KEY IS TO GO`. These two sets must be kept separate: the 16-transition reconstruction is the dataset from which such rules have been sought, while the five-word continuation was selected through a search for admissible plaintexts and nodes.

**Status:** an **empirical, post-discovery rule for a proposed reconstruction**, not an independently authenticated Cicada 3301 algorithm. Its 16/16 fit is notable but does not establish statistical significance, determine the next key's exact location, or prove any proposed plaintext. On the original 16 transitions, predicting *mirror for every transition* would already score **14/16**, so the two successful non-mirror predictions are the most important part to examine.

**Contents**

[01. Foundations](#foundations) · [02. The modulo-3 rule](#the-modulo-3-rule) · [03. Worked examples](#worked-examples) · [04. Verification across all 16 recorded transitions](#verification-across-all-16-recorded-transitions) · [05. Conditional extension after THEN](#conditional-extension-after-then) · [06. Comparison with alternative continuations](#comparison-with-alternative-continuations) · [07. Relationship to Reports 00–06](#relationship-to-reports-0006) · [08. Limitations and falsification](#limitations-and-falsification) · [Formula reference](#formula-reference)

---

## Foundations

### What counts as a mirror?

The project uses an **original three-rune key node**, selected from the 27 × 27 matrix **before** applying any center-totient transformation or cyclic key rotation. Its three cells are collinear and equally spaced along a horizontal, vertical, or 45° diagonal line.

| Node type | Original outer runes | Example in the recorded route | Key derivation |
|---|---|---|---|
| **Mirror** | **Equal** outer runes | `X–OE–X` (WEATHER) | Keep both outer indices; transform the original center index using `φ` |
| **Non-mirror** | **Different** outer runes | `H–NG–C` (TURNS); `L–C–EA` (SOON) | Follow the construction recorded for that node: some use the original center directly; others still transform its center with `φ`. |

**Mirror status here refers to whether the two outer runes of the original spatial node are identical.** It is **not** a statement about the symmetry of the aligned key stream, the Möbius signature, or the ciphertext. For example, `H–NG–C` can have a symmetric **Möbius signature** `(0,0,0)` without being a mirrored **rune node**.

### Coordinates and the two cells used

The matrix has **one-based** coordinates `(r,c)` from 1 through 27. Rows increase downward; columns increase rightward. The original absolute row-major index is

$$
n_0(r,c)=27(r-1)+c.
$$

For a **current** block `i`, define:

| Symbol | Meaning |
|---|---|
| **`K_i = (A_i,M_i,Z_i)`** | Its **original**, spatially ordered three-rune key node, before totient or cyclic rotation. |
| **`A_i`** | The original outer node cell with the **smaller** row-major index `n₀`. |
| **`Z_i`** | The original outer node cell with the **larger** row-major index `n₀`. This is the **later outer arm** used by this report. |
| **`L_i`** | The **leftmost cell of the current ciphertext**: smallest column; if tied, choose the **bottommost** row. |
| **`T_{i+1}`** | Mirror status of the **next original key-generating node**, the quantity to be predicted. |

`Z_i` is identified **before** the cyclic rotation of the derived key. For a horizontal node it is its right outer cell; for a vertical or diagonal node it is the lower outer cell. These definitions remain valid even if the ciphertext itself is read backward, upward, or diagonally. The original node can be geometrically symmetric **without** having identical outer runes; this report uses the term *mirror* only for the latter case.

**Do not replace `L_i` with the ciphertext beginning or endpoint.** In several recorded words they are different cells. Do not use the next ciphertext's leftmost cell, either: both inputs are properties of the **current** block.

---

## The Modulo-3 Rule

### Eight-direction step distance

Between the two current-block cells `Z_i` and `L_i`, use the **Chebyshev distance**, i.e. the minimum number of king-like steps allowed in any of the eight adjacent directions:

$$
\boxed{d_i=d_{\infty}(Z_i,L_i)=\max\!\bigl(|r(Z_i)-r(L_i)|,\ |c(Z_i)-c(L_i)|\bigr).}
$$

Examples of one eight-direction step:

```text
  NW    N    NE
    \   |   /
  W --- X --- E
    /   |   \
  SW    S    SE
```

A diagonal move changes both coordinates by one but counts as **one step**, not two. The distance is an **integer**. There is no Euclidean square root, Manhattan sum, or Möbius function in this particular formula.

### Predict the next node class

Compute the remainder:

$$
\rho_i=d_i\bmod 3\in\{0,1,2\}.
$$

Then predict:

$$
\boxed{
T_{i+1}=\begin{cases}
\text{NON-MIRROR},&\rho_i=2,\\
\text{MIRROR},&\rho_i\in\{0,1\}.
\end{cases}
}
$$

| `d mod 3` | Prediction for the **next** original key node | Search implication |
|:---:|---|---|
| **0** | **MIRROR** | Require matching outer runes, equally spaced around the original center. |
| **1** | **MIRROR** | Require matching outer runes, equally spaced around the original center. |
| **2** | **NON-MIRROR** | Look for a documented valid original node with **different** outer runes. |

The rule predicts **only the next node's class**. It does not determine the node's center, radius, direction, outer-rune identities, key signature, ciphertext coordinates, or word. Those are separate tests.

---

## Worked Examples

### Example A — WEATHER → TURNS: a non-mirror prediction

The original WEATHER node is the horizontal **`X–OE–X`**:

- Outer arms: `X (14,4)` and **`Z = X (14,6)`**.
- WEATHER ciphertext leftmost cell: **`L = NG (14,14)`**.

The distance is:

$$
d=\max(|14-14|,|6-14|)=\max(0,8)=8.
$$

$$
\boxed{8\bmod 3=2\ \Longrightarrow\ \text{NON-MIRROR next node}.}
$$

The recorded TURNS node is **`H (4,23) – NG (14,23) – C (24,23)`**. Its outer runes **H and C are different**, as predicted. This is an especially informative match: the rule predicts one of the **minority non-mirror events**.

### Example B — YOU → SOON: the second non-mirror prediction

The original YOU key node is vertical **`P–R–P`**, with outer positions `(5,16)` and **`Z = P (27,16)`**. The YOU ciphertext's leftmost cell is **`L = X (25,16)`**.

$$
d=\max(|27-25|,|16-16|)=2,\qquad 2\bmod3=2.
$$

**Prediction: NON-MIRROR.** The recorded SOON construction uses unequal-outer original source triples `L–C–EA`, `L–I–EA`, or `L–EO–EA`. These are different geometric placements that generate the same derived key, with **their center indices transformed using `φ`**. **All have different outer rune symbols, L and EA**, so the prediction is unchanged by the documented choice among them. The SOON page informally calls these arrangements *mirrors* because of their equal-radius spatial geometry; under the **equal-outer-rune definition used by this report**, they are **non-mirrored rune nodes**.

### Example C — THEN → THE: the first conditional extension

The original THEN mirror is vertical **`IA–IA–IA`**:

- Center: `IA (26,22)`.
- Outer arms: `IA (25,22)` and **`Z = IA (27,22)`**.
- Current THEN ciphertext leftmost: **`L = L (25,25)`** (here the rune's name is also `L`).

$$
d=\max(|27-25|,|22-25|)=\max(2,3)=3.
$$

$$
\boxed{3\bmod3=0\ \Longrightarrow\ \text{MIRROR next node}.}
$$

The selected block-18 THE key comes from `N (17,17) – M (20,17) – N (23,17)`, a **mirror**, and agrees with the prediction. **This is a conditional check on a candidate continuation, not a new observation in the original 16-transition dataset.**

---

## Verification Across All 16 Recorded Transitions

The table below transcribes **the selected original key nodes and ciphertext leftmost cells** from the project's first 17 plaintext-block documents. It uses the **later original outer cell** `Z` and the **current** `L`, then compares the prediction with the next block's **original node**.

| # | Current → next | Current `Z` | Current `L` | `d∞` | `d mod 3` | Predicted next type | Recorded next type |
|---:|---|:---:|:---:|---:|:---:|---|---|
| 1 | AS I GO THE → WEATHER | `(13,13)` | `(14,1)` | 12 | **0** | Mirror | **Mirror ✓** |
| **2** | **WEATHER → TURNS** | `(14,6)` | `(14,14)` | **8** | **2** | **Non-mirror** | **Non-mirror ✓** |
| 3 | TURNS → COLD | `(24,23)` | `(14,19)` | 10 | **1** | Mirror | **Mirror ✓** |
| 4 | COLD → I MAY | `(27,19)` | `(14,7)` | 13 | **1** | Mirror | **Mirror ✓** |
| 5 | I MAY → CRY | `(17,8)` | `(26,16)` | 9 | **0** | Mirror | **Mirror ✓** |
| 6 | CRY → NOW THE | `(26,16)` | `(19,16)` | 7 | **1** | Mirror | **Mirror ✓** |
| 7 | NOW THE → IDEA | `(20,16)` | `(11,16)` | 9 | **0** | Mirror | **Mirror ✓** |
| 8 | IDEA → OF | `(14,19)` | `(17,18)` | 3 | **0** | Mirror | **Mirror ✓** |
| 9 | OF → THE | `(19,16)` | `(18,15)` | 1 | **1** | Mirror | **Mirror ✓** |
| 10 | THE → END | `(20,16)` | `(19,16)` | 1 | **1** | Mirror | **Mirror ✓** |
| 11 | END → IS | `(27,8)` | `(21,23)` | 15 | **0** | Mirror | **Mirror ✓** |
| 12 | IS → DEATH | `(21,27)` | `(21,9)` | 18 | **0** | Mirror | **Mirror ✓** |
| 13 | DEATH → SEE | `(27,8)` | `(26,1)` | 7 | **1** | Mirror | **Mirror ✓** |
| 14 | SEE → YOU | `(25,10)` | `(27,14)` | 4 | **1** | Mirror | **Mirror ✓** |
| **15** | **YOU → SOON** | `(27,16)` | `(25,16)` | **2** | **2** | **Non-mirror** | **Non-mirror ✓** |
| 16 | SOON → THEN | `(25,20)` | `(25,16)` | 4 | **1** | Mirror | **Mirror ✓** |

**Result: 16/16 on the recorded route.** The remainder sequence is:

```text
0, 2, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 2, 1
```

There are **2 remainder-2 transitions**; both lead to non-mirrored original nodes. The other **14** lead to mirrored original nodes. No exception occurs within these **selected 16 transitions**.

**SOON source-node ambiguity:** the record provides three unequal-outer nodes that can yield the same key. With the same `L = (25,16)`, their later outer cells can be `EA (25,10)`, `EA (25,15)`, or `EA (25,20)`. Their distances are respectively `6`, `1`, and `4`, giving remainders **0, 1, and 1**. **All three still predict a mirror for THEN.** The table displays the `(25,20)` choice, but its prediction does not depend on that choice.

---

## Conditional Extension After THEN

The repo's selected continuation `THE KEY IS TO GO` has five additional **mirror** nodes. The new test is evaluated **from the current block to the following key**:

| Transition | Current node's later outer cell `Z` | Current ciphertext `L` | `d∞` | `mod 3` | Prediction | Selected next node |
|---|:---:|:---:|---:|:---:|---|---|
| THEN → THE | `(27,22)` | `(25,25)` | 3 | 0 | Mirror | `N–M–N` ✓ |
| THE → KEY | `(23,17)` | `(21,20)` | 3 | 0 | Mirror | `TH–H–TH` ✓ |
| KEY → IS | `(13,16)` | `(21,4)` | 12 | 0 | Mirror | `W–I–W` ✓ |
| IS → TO | `(17,15)` | `(19,6)` | 9 | 0 | Mirror | `X–M–X` ✓ |
| TO → GO | `(11,25)` | `(9,16)` | 9 | 0 | Mirror | `TH–G–TH` ✓ |

**Conditional result: 5/5.** Combined with the original 16, that is **21/21 along this one selected extended route** — **not 21 independent predictions** and not evidence that `THE KEY IS TO GO` is uniquely decryptable.

**An important distinction:** these five examples all have remainder **0**, and all five candidate next keys were chosen to be mirrors. Consequently, this extension demonstrates consistency but offers **no additional non-mirror test**. Alternative five-mirror plaintext branches can also satisfy the rule.

---

## Comparison with Alternative Continuations

A subsequent candidate-branch search, using the same project matrix and the geometric constraints in Reports 01–06, produced the following **best reported matches** for this specific mirror-type rule:

| Candidate phrase after THEN | Rule matches | Qualification |
|---|---:|---|
| **THE KEY IS TO GO** | **5/5** | All five selected keys mirrored. |
| **THE KEY IS THE SEA** | **5/5** | Also entirely compatible with this rule; **not eliminated**. |
| **THE LIE IS DEATH** | **3/4** | One of the four transitions disagrees in the reported best chain. |
| **THE LIE IS THE SEA** | **4/5** | One disagreement in the reported best chain. |
| **I GO TO THE SEA** | **3/5** | Two disagreements. |
| **WE GO WITH THE SEA** | **1/5** | Four disagreements. |
| **SEA IS THE PATH** | **3/4** | One disagreement. |

These are **selected candidate chains and best scores**, not an exhaustive uniqueness statement about each English phrase. For a fresh candidate, always evaluate the actual node and ciphertext coordinates; do not simply assign the aggregate score above.

There is also a useful negative test: the previously explored complete `BE A GOD` candidates use a **non-mirror BE node** immediately after THEN, whereas the measured THEN distance is `3 ≡ 0 (mod 3)` and predicts a **mirror**. Thus those candidates **fail this new constraint at the first step** even though some passed Reports 01–06. The rule can therefore exclude some otherwise allowable branches.

**Critically, it does not distinguish `THE KEY IS TO GO` from `THE KEY IS THE SEA`.** A future selection method must use additional independent geometry or a rule that predicts an exact key or ciphertext location.

---

## Relationship to Reports 00–06

This is a **new proposed Report 07**. It measures a different property from the existing tests:

| Report | Main predicted / checked property | How this rule differs |
|---|---|---|
| [00 — Decryption method](00-decryption-method.md) | Construct and align the key; subtract rune indices mod 29 | Predicts **whether next original outer runes match**, before key construction. |
| [01 — Next key signature](01-next-key-signature.md) | Next derived key's Möbius signature and phase | **Mirror status is not the same as symmetric signature**; non-mirror `H–NG–C` has signature `(0,0,0)`. |
| [02 — Leftmost cell and rotations](02-leftmost-cell-and-rotations.md) | Leftmost-cell Möbius class and its role in reading order | Reuses the **geometric definition** of `L`, but applies no rotation. |
| [03 — Reading axis](03-predicting-axis-and-reading-direction.md) | Next ciphertext's reading axis and direction | Predicts a **key-node class**, not the ciphertext direction. |
| [04 — Key-center parity](04-predicting-next-key-center-parity.md) | Next original key center's row/column parity | This rule does **not** predict center coordinates or parity. |
| [05 — Ciphertext row parity](05-predicting-next-ciphertext-row-parity.md) | Next endpoint and leftmost row parities | This rule uses `L` only as an **input coordinate**, not a parity output. |
| [06 — Ciphertext ray](06-predicting-next-ciphertext-ray-and-mobius-deviation.md) | Next ciphertext beginning's allowable deviation from a ray | The distances are **different**: here `d∞(Z,L)` is a **Chebyshev movement distance**, while Report 06 uses `d₈(L,B′)` as a **deviation from a ray**. |

**The value 3 appears in two different places in the project:** Report 01 uses modulo 3 for the cyclic rotation phase; this report uses modulo 3 for a **spatial distance between two original matrix cells**. Their input quantities are not interchangeable, and no causal connection between the two has yet been established.

### Suggested workflow for the next key

1. Start with an already-selected **current** ciphertext and its **original**, unrotated spatial key node.
2. Determine `L` from the current ciphertext and `Z` from the original source node.
3. Compute `d∞(Z,L) mod 3` and **filter prospective next nodes by mirror status**.
4. Apply Report 01 (signature), Report 04 (center parity), and the other Report 02–06 constraints; then perform the exact rune arithmetic in Report 00.
5. Keep multiple candidates when they survive. **Do not treat a surviving English word as automatically authenticated plaintext.**

The classification is useful as an **additional filter**, not a unique next-key selector.

---

## Limitations and Falsification

### Why 16/16 is not proof

- **Small, reconstructed sample.** The 16 recorded transitions originate from one selected, non-authenticated research path rather than a random independent validation set.
- **Strong class imbalance.** Of 16 outcomes, **14 are mirror** and **2 are non-mirror**. An always-mirror baseline already obtains **14/16 = 87.5%**; the new rule's added value is correctly isolating the two non-mirror transitions.
- **Rule search / post-selection.** The geometry, distance metric, remainder classification, and candidate paths were examined retrospectively. Therefore the perfect observed fit cannot be assigned a naive chance probability.
- **Current-node selection matters.** Different valid source nodes for the same key may produce different `Z` values. The SOON examples happen to keep the same predicted class, but this invariance has not been demonstrated for every admissible key assignment.
- **Candidate continuation is not independent evidence.** The `THE KEY IS TO GO` sequence was found with multiple project constraints and is not confirmed LP2 plaintext. Passing this rule does not distinguish it from all alternatives.
- **No physical derivation yet.** The use of an eight-direction distance and residue class 2 is geometrically clear, but why Cicada would choose exactly this condition is not established.

### What would test the rule more strongly?

A meaningful prospective test would **freeze the formula** and the method for selecting the current node **before** deciding on the next plaintext. Then record its mirror/non-mirror prediction and look for a uniquely constrained next placement. A next node of the wrong class would **falsify the proposed rule for that reconstruction**.

A stronger statistical test would compare the rule against alternatives (other distances, anchors, moduli and residue assignments) across many equally admissible branches, **counting different assignments of the same word or center appropriately**. In particular, new accurately established **non-mirror** stages would be disproportionately informative.

**Conclusion:** a simple original-node-to-leftmost-cell distance gives a clean **16/16 empirical fit** and correctly identifies the **two** recorded non-mirror events. On the selected five-word extension it remains consistent, but it is currently a **research-level predictive constraint**, not a proven historical decryption procedure.

---

## Formula Reference

| Quantity | Formula or instruction |
|---|---|
| Absolute position | $n_0(r,c)=27(r-1)+c$ |
| Current last outer arm | $Z=\operatorname*{arg\,max}_{X\in\{O_1,O_2\}}n_0(X)$, where $O_1,O_2$ are the original two outer node cells |
| Current leftmost ciphertext cell | Minimum column, breaking ties by **maximum row** |
| Eight-direction step distance | $d_{\infty}(Z,L)=\max(|r_Z-r_L|,|c_Z-c_L|)$ |
| Residue | $\rho=d_{\infty}(Z,L)\bmod3$ |
| Next type for $\rho=2$ | **NON-MIRROR** (different outer runes) |
| Next type for $\rho=0$ or $1$ | **MIRROR** (equal outer runes) |
| Recorded reconstruction | **16/16** matches: 14 mirrored + 2 non-mirrored outcomes |
| Selected `THEN → … → GO` extension | **5/5** conditional matches; all five next keys are mirrors |

**Source material:** the 27 × 27 matrix and `plaintext-i-found/01-as-i-go-the.md` through `17-then.md`; the selected continuation in `plaintext-i-found/18-the.md` through `22-go.md`; and the previous [Reports 00–06](00-decryption-method.md). This report adds a **new hypothesis** to that recorded project; the source materials do not claim external authentication of LP2's intended plaintext.
