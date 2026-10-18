*LIBER PRIMUS II · PAGES 0–2*

# Strongest Plaintext Evidence

**A Numerical and Structural Correspondence Report**

*Rune values · Prime numbers · Euler's totient · Passage structure · LP1 connections*

---

The proposed reading of *Liber Primus* LP2, pages 0–2, contains more than a sequence of English words. When the recovered passages are grouped and measured by their **rune counts, rune-index sums, and assigned prime values**, several numerical relationships appear across different parts of the text. Some also point back to the geometry of the **27 × 27 matrix** and to a passage from LP1.

This report gathers the strongest of those recorded correspondences and explains them one at a time. The aim is to make each calculation easy to follow: **what is being counted, where each number comes from, and what the result connects to**.

These are observations on the **selected plaintext route**. They are presented separately from the predictive rules: an exact arithmetic equality can be reproduced directly, while the interpretation of that equality as an intentional clue requires additional testing.

**Contents**

[01. The opening geometry](#the-opening-geometry) · [02. Two seven-word passages](#two-seven-word-passages) · [03. Ciphertext and key totals](#ciphertext-and-key-totals) · [04. The sum that spells YOU](#the-sum-that-spells-you) · [05. Four appearances of 51](#four-appearances-of-51) · [06. Two perfect cubes](#two-perfect-cubes) · [07. Two four-word passages](#two-four-word-passages) · [08. The LP1 correspondence](#the-lp1-correspondence)

---

## Reading the Numbers

The following distinctions are important throughout the report.

A **rune count** counts rune symbols, not English letters. A transliteration such as `TH` or `EA` can represent one rune. A **rune-index sum** adds the numerical indices of those symbols in the project's 29-rune alphabet. A **prime-value sum** instead adds the prime numbers assigned to the corresponding runes. These are two different totals and should not be confused.

Matrix coordinates are written as **(row, column)**, beginning at 1. For example, `J(13,12)` is the rune `J` in row 13, column 12. The symbol $\varphi(n)$ denotes **Euler's totient function**.

For how these rune values are used in the actual decryption, see **[Report 00 — The Decryption Method](./00-decryption-method.md)**. Here, the focus is the numerical structure of the resulting passages.

---

## The Opening Geometry

### From the red heading to a three-rune structure

The recorded red heading on page 0 contains **13 runes**. Applying Euler's totient function gives a second number:

$$
\varphi(13)=12
$$

The pair **13 and 12** can be interpreted geometrically as the matrix coordinate **`J(13,12)`**. Their difference supplies a radius of one cell:

$$
13-12=1
$$

At that radius, the horizontal structure around `J(13,12)` is:

- **Left:** `AE(13,11)`
- **Center:** `J(13,12)`
- **Right:** `EA(13,13)`

The sum of the same two numbers also gives a rune value:

$$
13+12=25=\mathrm{AE}
$$

In this reading, the heading length therefore connects **a coordinate**, **a radius**, and **a flanking rune value** in one local structure.

### A totient-derived distance

The next recorded operation starts at the left-hand `AE(13,11)`. For the central rune `J`, the two successive totient values are **10** and **4**:

$$
\varphi(\mathrm{J})+\varphi(\varphi(\mathrm{J}))=10+4=14
$$

Moving **14 columns to the right** from `AE(13,11)` reaches **`L(13,25)`**:

$$
(13,11)\longrightarrow(13,25)
$$

There is also a text-count correspondence in the recorded material. Subtracting two heading words from the recorded total of 158 words leaves **156**, which is the product of the original pair:

$$
158-2=156=13\times12
$$

The geometric construction and the word-count equality are distinct observations. Their connection is that each uses the same **13 / 12** starting values.

---

## Two Seven-Word Passages

### Equal word counts, neighboring index totals

Two passages in the proposed plaintext each contain **seven words**, but have different rune counts.

**First passage** — `AS I GO, THE WEATHER TURNS COLD`

- **7 words**
- **21 runes**
- **Rune-index sum: 233**

**Second passage** — `THE IDEA OF THE END IS DEATH`

- **7 words**
- **17 runes**
- **Rune-index sum: 232**

The index totals are consecutive numbers. More specifically, **233 is prime**, so its totient is exactly 232:

$$
\varphi(233)=232
$$

This makes the relationship more specific than a difference of one: the second passage's sum is the **totient of the first passage's sum**.

### Connections to the matrix and its keys

The first passage contains **21 runes**. That number can be written as **3 × 7**; in the recorded rune mapping, `NG = 21`. The rune `NG` also occupies the center of the **27 × 27 matrix**, at **`NG(14,14)`**.

Another connection begins with **COLD**. Its rune-index values are `C = 5`, `O = 3`, `L = 20`, and `D = 23`, giving:

$$
5+3+20+23=51
$$

The **51st prime** is **233**, the index sum of the first seven-word passage.

The same values can be followed through the Fibonacci sequence, using the convention $F_1=F_2=1$:

$$
F_7=13,\qquad F_{13}=233
$$

The number **7** also relates to a recorded key change near `DEATH`. The seventh prime is **17**, corresponding to `B`; applying the totient gives **16**, corresponding to `T`:

$$
\varphi(17)=16
$$

This is the numerical change shown by the recorded **`J–B–J` → `J–T–J`** structure.

Finally, the **16th prime is 53**. The three recorded values `D = 23`, `EA = 28`, and `TH = 2` also sum to 53:

$$
23+28+2=53
$$

These are different kinds of correspondences: a passage sum, a central matrix rune, a word's index sum, a Fibonacci relation, and a key transformation. The notable feature is their convergence around a relatively small set of values — especially **7, 13, 17, 21, 51, 232, and 233**.

---

## Ciphertext and Key Totals

### Why the modular arithmetic matters

The two seven-word passages can also be compared at the **ciphertext** and **key** levels. Because the proposed decryption subtracts key indices from ciphertext indices **modulo 29**, each negative difference contributes a correction of 29 when represented as a nonnegative rune index.

For a complete passage, the totals therefore obey:

$$
P=C-K+29w
$$

Here **`C`** is the sum of ciphertext indices, **`K`** is the sum of aligned key indices, **`P`** is the resulting plaintext-index sum, and **`w`** is the number of wraparound corrections.

### First seven-word passage

The recorded totals are **ciphertext 299**, **key 298**, and **8 wraparounds**:

$$
299-298+8\times29=233
$$

This reproduces the plaintext index sum **233**.

### Second seven-word passage

The corresponding totals are **ciphertext 256**, **key 256**, and again **8 wraparounds**:

$$
256-256+8\times29=232
$$

This reproduces the plaintext index sum **232**.

Both passages therefore require **eight wraparounds**, even though their raw ciphertext and key totals differ. The second passage has exactly equal ciphertext and key sums; the first differs by one. The shared wraparound count is the additional pattern here.

A further numerical observation is:

$$
\varphi(8)=4
$$

The modular identities are a direct consequence of the reported decryption values. The recurrence of **eight** in two distinct passages is the part being compared.

---

## The Sum That Spells YOU

### A prime-value total across three passages

A different calculation assigns each rune its corresponding **prime value** rather than its ordinary rune index. The recorded totals through the word `DEATH` are:

- `AS I GO, THE WEATHER TURNS COLD` — **825**
- `I MAY CRY NOW` — **484**
- `THE IDEA OF THE END IS DEATH` — **854**

Adding the three blocks gives:

$$
825+484+854=2163
$$

The total has the factorization:

$$
2163=103\times7\times3
$$

In the project's rune-to-prime mapping, these three factors correspond, in order, to:

- **103 → Y**
- **7 → O**
- **3 → U**

The factorization therefore reads **`YOU`**.

This is particularly interesting because the next proposed recovered passage contains **`SEE YOU`**. The earlier numerical total appears to anticipate a word in the subsequent reading.

The phrase *“Seek and you will be found”* is also noted in the project's Cicada 3301 context (2016). It provides a thematic comparison, distinct from the arithmetic factorization itself.

---

## Four Appearances of 51

The number **51** occurs in four separate measurements along the selected route.

**1. The rune-index sum of COLD**

$$
5+3+20+23=51
$$

**2. The rune-index sum of SEE**

$$
15+18+18=51
$$

**3. The ordinal position of the prime 233**

**233 is the 51st prime**, linking 51 to the first seven-word passage's index sum.

**4. The number of runes counted through SEE**

The count combines the first seven-word passage (**21** runes), `I MAY CRY NOW` (**10**), the second seven-word passage (**17**), and `SEE` itself (**3**):

$$
21+10+17+3=51
$$

The two word sums, the prime ordinal, and the cumulative rune count all meet at **51**. They are not four independent predictions, but they give several reproducible ways in which the same number appears within the proposed reading.

---

## Two Perfect Cubes

### Adjacent passages produce 27 and 343

Consider the following two blocks:

**`THE IDEA OF THE END IS DEATH`**

- **7 words**
- **17 runes**
- **Rune-index sum: 232**

**`SEE YOU SOON`**

- **3 words**
- **10 runes**
- **Rune-index sum: 111**

Together they contain **10 words** and **27 runes**, with a combined index sum of **343**.

The rune count is a perfect cube:

$$
17+10=27=3^3
$$

And so is the index sum:

$$
232+111=343=7^3
$$

These exponents echo the respective word counts: **3 words** in `SEE YOU SOON` and **7 words** in the preceding `DEATH` passage. The observed relationship is thus not only that the totals are cubes, but that **their exponents are present in the passage structure itself**.

---

## Two Four-Word Passages

### A difference sequence of 3, 7, and 13

A second comparison pairs two four-word portions of the proposed reading.

**`I MAY CRY NOW`**

- **4 words**
- **10 runes**
- **Rune-index sum: 133**
- **Prime-value sum: 484**

**`SEE YOU SOON, THEN`**

- **4 words**
- **13 runes**
- **Rune-index sum: 140**
- **Prime-value sum: 497**

Although both contain four words, the differences in their three numerical measurements are:

- **Rune count:** `13 − 10 = 3`
- **Rune-index sum:** `140 − 133 = 7`
- **Prime-value sum:** `497 − 484 = 13`

The resulting sequence is **3, 7, 13**. The values **7** and **13** also reappear in the Fibonacci connection discussed earlier:

$$
F_7=13,\qquad F_{13}=233
$$

This comparison depends on a specific grouping into two four-word passages. With that grouping fixed, the three differences follow directly from the recorded totals.

---

## The LP1 Correspondence

### A seven-word passage in the opening warning

The opening warning in LP1 is transcribed in the research notes as follows:

```text
BELIEVE NOTHNG FROM THIS BOOC
EXCEPT WHAT YOV CNOW TO BE TRVE
TEST THE CNOWLEDGE
FIND YOVR TRVTH
```

A seven-word passage can be read across the line break between `TRVE` and `TEST`:

> **YOV CNOW TO BE TRVE TEST THE**

Compare that sequence with the first proposed seven-word LP2 passage:

> **AS I GO, THE WEATHER TURNS COLD**

The two passages have matching values in three measurements:

- **Word count:** 7 in each passage.
- **Rune count:** 21 in each passage.
- **Prime-value sum:** 825 in each passage.

Their rune-index totals are not equal, but they form the same consecutive pair encountered earlier:

- **LP2 passage:** 233
- **LP1 passage:** 232

And therefore:

$$
\varphi(233)=232
$$

The exact agreement in **word count, rune count, and prime-value sum**, together with the totient relationship between index totals, makes this the report's principal **cross-text correspondence**. Unlike comparisons between neighboring blocks of the proposed LP2 reading, it involves a passage selected from a different part of *Liber Primus*.

---

## Reading the Evidence Together

The patterns in this report operate at several levels. Some arise from the **geometry of the opening matrix**, others from the **structure of the proposed English passages**, and others from **rune-index or prime-value arithmetic**. The LP1 comparison adds a possible connection across the two parts of *Liber Primus*.

The most useful way to examine these findings is to keep three questions separate:

1. **Does the calculation reproduce the recorded numbers?** The equations above make these equalities straightforward to check.
2. **How was the passage or grouping selected?** Word boundaries, the chosen route, and the rune-to-number mapping matter to each comparison.
3. **Would the same pattern remain distinctive among alternative readings?** That is the stronger test of whether a numerical match is meaningful rather than coincidental.

None of these correspondences needs to be treated as a standalone proof. Their significance lies in how often the **same values connect different kinds of measurements** within the selected reading — and in whether those relationships survive comparison with other plausible routes.

The related reports in the project address a complementary question: whether the geometry can **predict properties of the next key or ciphertext before a continuation is chosen**. These numerical observations provide supporting context for that predictive work, rather than replacing it.

---

*Research source:* [Liber Primus — 27×27 Map, 3-Rune Nodes & Totient Decryption](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption). The calculations and selected passage groupings in this document are consolidated from the project's recorded **Strongest Plaintext Evidence** notes.
