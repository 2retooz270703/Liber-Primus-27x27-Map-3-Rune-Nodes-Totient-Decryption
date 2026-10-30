# Strongest Plaintext Evidence

The proposed reading of *Liber Primus* LP2, pages 0–2, contains more than a sequence of English words. When the recovered passages are grouped and measured by their **rune counts, rune-index sums, and assigned prime values**, several numerical relationships appear across different parts of the text. Some also point back to the geometry of the **27 × 27 matrix**, a passage from LP1, and the numerical matrices in LP1. The continuation through **`THE KEY IS TO GO`** produces an especially striking result: its cumulative index sum maps directly back to the original `J(13,12)` cell, while its cumulative prime-value sum identifies the total number of admissible mirrored nodes.

This report gathers the strongest of those recorded correspondences and explains them one at a time. The aim is to make each calculation easy to follow: **what is being counted, where each number comes from, and what the result connects to**.

These are observations on the **selected plaintext route**. They are presented separately from the predictive rules: an exact arithmetic equality can be reproduced directly, while the interpretation of that equality as an intentional clue requires additional testing.

**Contents**

1. [The opening geometry](#the-opening-geometry)
2. [Two seven-word passages](#two-seven-word-passages)
3. [Ciphertext and key totals](#ciphertext-and-key-totals)
4. [The sum that spells YOU](#the-sum-that-spells-you)
5. [Four appearances of 51](#four-appearances-of-51)
6. [Two perfect cubes](#two-perfect-cubes)
7. [Two four-word passages](#two-four-word-passages)
8. [The LP1 correspondence](#the-lp1-correspondence)
9. [The LP1 matrix connection](#the-lp1-matrix-connection)
10. [The full-route sum and 3301](#the-full-route-sum-and-3301)
11. [Cell values and prime-indexed positions](#cell-values-and-prime-indexed-positions)
12. [The GO closure: a return to J](#the-go-closure-a-return-to-j)

---

## Reading the Numbers

The following distinctions are important throughout the report.

A **rune count** counts rune symbols, not English letters. A transliteration such as `TH` or `EA` can represent one rune. A **rune-index sum** adds the numerical indices of those symbols in the project's 29-rune alphabet, numbered **0 through 28**. A **prime-value sum**, written **GP**, instead adds the corresponding Gematria Primus prime values: index 0 maps to 2, index 1 to 3, and so on through index 28, which maps to 109. These are two different totals and should not be confused.

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

The phrase *“Seek and you will be found”* is also noted in the project's 3301 context (2016). It provides a thematic comparison, distinct from the arithmetic factorization itself.

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

## The LP1 Matrix Connection

### From FORM to a number in the second matrix

A further correspondence connects the same **233 / 232** pair to the two numerical matrices in LP1.

The center of the first matrix is **FORM**, whose Gematria Primus prime-value sum is **91**:

$$
\mathrm{FORM}=2+7+11+71=91.
$$

Let $p_n$ denote the **n-th prime**, with $p_1=2$. The 91st prime is 467; doubling it gives 934:

$$
\boxed{p_{91}=467,\qquad 2p_{91}=934.}
$$

The number **934** appears immediately **above and below the center of the second LP1 matrix**. In its one-based 5 × 5 coordinates, these are cells **`(2,3)`** and **`(4,3)`**, surrounding the central **809**.

### Recovering the two passage totals

Applying Euler's totient function to 934 gives:

$$
\varphi(934)=\varphi(2\times467)=466=2\times233.
$$

Thus the first passage's index sum can be recovered as:

$$
\boxed{\frac{\varphi(934)}{2}=233.}
$$

Applying the totient function once more gives the second passage's sum:

$$
\boxed{\varphi(\varphi(934))=\varphi(466)=\varphi(2\times233)=232.}
$$

Both results match the totals already recorded in [Two Seven-Word Passages](#two-seven-word-passages):

| Proposed LP2 passage | Rune-index sum | Expression from the LP1 number 934 |
|---|---:|---|
| **AS I GO, THE WEATHER TURNS COLD** | **233** | $\varphi(934)/2$ |
| **THE IDEA OF THE END IS DEATH** | **232** | $\varphi(\varphi(934))$ |

The relationship between the two totals also remains:

$$
\varphi(233)=232.
$$

### Reading the connection

The complete calculation starts with **FORM = 91** at the center of the first LP1 matrix, takes the **91st prime**, doubles it to obtain **934** from the second matrix, and uses the totient function to recover **233 and 232** from the proposed LP2 reading.

This connects **both LP1 matrices**, **prime-number indexing**, **Euler's totient function**, and **the two previously recorded seven-word passage totals**. The starting 91 is a **prime-value sum**; the resulting 233 and 232 are **rune-index sums**. The calculation relates these different numerical representations without identifying them as the same kind of measurement.

The arithmetic is exact. Whether it reflects an intentional connection to the selected plaintext remains a hypothesis requiring further independent checks.

### Two further correspondences involving the matrix centers

The center of the second LP1 magic square is **809**, the **140th prime number**. Interestingly, **140** is also the exact Gematria Primus **rune-index sum** of the 13 runes in **`SEE YOU SOON, THEN`** (51 + 30 + 30 + 29).

The first square has **FORM = 91** at its center, and $\varphi(91)=72$. Similarly, **`SEE YOU SOON`** has a rune-index sum of **111**, with $\varphi(111)=72$. This also matches the **derived key for `THEN`**: **`E–IA–IA`** = 18 + 27 + 27 = **72**.

These are exact numerical correspondences within the selected reading; whether they were intentionally encoded remains to be established.

---

## The Full-Route Sum and 3301

### 61 ciphertext-cell uses across the first 17 stages

The first **17 decryption stages**, ending at `THEN`, produce the following proposed plaintext:

```text
AS I GO, THE WEATHER TURNS COLD.
I MAY CRY NOW.
THE IDEA OF THE END IS DEATH.
SEE YOU SOON, THEN.
```

This block involves **61 uses of ciphertext cells**, covering **54 distinct coordinates**. The difference represents **7 additional uses of previously counted cells**. Each repeated use contributes again to the full-route total.

Let $C_t$ be the ciphertext rune used at step $t$. Summing the **GP prime values of the ciphertext runes before key subtraction** gives:

$$
\sum_{t=1}^{61}GP(C_t)=3274.
$$

Adding the side length of the **27 × 27 matrix** produces the signature number **3301**:

$$
\boxed{3274+27=3301.}
$$

This is a possible **authorial checksum**: the ciphertext total for the complete selected block combines with the matrix dimension to recover 3301.

The calculation uses the **main `SOON` placement in row 25**. The recorded alternative in row 27 gives a full-route GP total of **3214**, for which $3214+27=3241$. Both placements decrypt to `SOON`, so this numerical condition distinguishes the two recorded routes even though their plaintext is the same.

---

## Cell Values and Prime-Indexed Positions

### The 54 unique cells link content to location

A second calculation counts each of the **54 distinct ciphertext cells exactly once**. Let $U$ denote this set of coordinates.

An **absolute position** is the cell's one-based number in the original matrix, counted from left to right across each row, starting at the top-left cell. For row $r$ and column $c$:

$$
a(r,c)=27(r-1)+c,\qquad 1\leq a(r,c)\leq729.
$$

For example, cell **`L(13,25)`** has absolute position **349** and GP prime value **73**. These are separate measurements of the same cell.

For the complete set $U$, the two sums are:

$$
\sum_{u\in U}GP(C_u)=2867,
\qquad
\sum_{u\in U}a_u=26083.
$$

The connection is exact: **26083 is the 2867th prime number**. With $p_n$ denoting the $n$-th prime and $p_1=2$:

$$
\boxed{p_{2867}=26083.}
$$

In other words, **the sum of the ciphertext rune values gives the prime's ordinal number, while the sum of the cells' absolute positions gives the prime itself**.

### Keeping the counting conventions distinct

| Measurement | Count every ciphertext-cell use | Count each distinct cell once |
|---|---:|---:|
| Number of counted entries | 61 | 54 |
| Ciphertext GP prime-value sum | **3274** | **2867** |
| Absolute-position sum | 29848 | **26083** |

The **3301 equality** counts every use, including repetitions. The **prime-index equality** counts each coordinate once, in the original matrix orientation. Both describe the selected `AS I GO`–`THEN` route, using two explicitly defined counting conventions.

The prime-index equality is a property of the **visited set of cells**; it does not determine their reading order or the keys. These are exact, reproducible numerical observations. Their interpretation as intentional clues should be tested against alternative routes using the same counting and numbering conventions.

---

## The GO Closure: A Return to J

### The 21st generation block completes a 27-word reading

The proposed continuation beyond `THEN` is **`THE KEY IS TO GO`**, with **`GO` appearing as the 21st generation block**. At this exact endpoint, the accumulated plaintext contains **27 English words** — the same number as the side length of the **27 × 27 rune matrix**.

| Consecutive plaintext passage | Words | Rune-index sum | GP prime-value sum |
|---|---:|---:|---:|
| `AS I GO, THE WEATHER TURNS COLD` | 7 | 233 | 825 |
| `I MAY CRY NOW` | 4 | 133 | 484 |
| `THE IDEA OF THE END IS DEATH` | 7 | 232 | 854 |
| `SEE YOU SOON, THEN` | 4 | 140 | 497 |
| **`THE KEY IS TO GO`** | **5** | **122** | **429** |
| **Total through GO** | **27** | **860** | **3089** |

The endpoint is therefore marked by both **generation-block position 21** and a **27-word total**. More importantly, the two numerical totals independently lead to properties of the matrix and its permitted key structures.

### 860 → 336: the plaintext returns to its starting cell

Adding the **rune indices** of the complete 27-word reading gives:

$$
233+133+232+140+122=\boxed{860}.
$$

Applying Euler's totient function yields:

$$
\boxed{\varphi(860)=336}.
$$

The number **336** is not merely associated with the starting rune. It is the **exact absolute, one-based position** of **`J(13,12)`** in the 27 × 27 matrix, using the same row-major coordinate convention defined earlier:

$$
a(13,12)=27(13-1)+12=\boxed{336}.
$$

This is the original center rune of the **`AE(13,11)–J(13,12)–EA(13,13)`** structure established in [The Opening Geometry](#the-opening-geometry). The arithmetic now closes the circle:

$$
\boxed{\text{27-word plaintext through GO}\ \longrightarrow\ 860\ \xrightarrow{\ \varphi\ }\ 336\ \longrightarrow\ J(13,12)}.
$$

**The extended plaintext points back, numerically and exactly, to the cell from which the proposed construction began.** This is a genuine arithmetic closure in the selected route: it does not require interpreting a word, choosing a different coordinate orientation, or moving the starting point. It should be distinguished from a physical return of the navigation path to that cell.

### 3089: a prime-number index matching the entire admissible node set

The second cumulative total uses **Gematria Primus prime values** for the same passages:

$$
825+484+854+497+429=\boxed{3089}.
$$

Here **3089 is prime**, and its position in the ordered sequence of primes is **442**:

$$
\boxed{p_{442}=3089}.
$$

That ordinal matches the project's enumerated inventory of **exactly 442 admissible mirrored three-rune nodes** across the complete matrix, under the totient/Möbius key-generation rules **after excluding the F branches**. This comparison uses the **global set of eligible nodes**, not merely the keys selected along the `GO` route.

Thus, the complete reading through `GO` yields two complementary numerical references:

- **Rune-index sum → totient → position 336:** the **original `J` cell**.
- **GP sum → prime ordinal 442:** the **total population of admissible mirrored nodes**.

### Why this endpoint stands out

The same continuation produces a **21st-block endpoint**, a **27-word text** matching the matrix dimension, a **totient return to the exact starting coordinate**, and a **prime-index match to the matrix-wide admissible-node count**. The last two are especially compelling because they connect separate levels of the construction: **the accumulated plaintext to the origin of the route**, and **the accumulated prime values to the global key-space inventory**.

These correspondences provide **strong additional structural evidence for the selected `THE KEY IS TO GO` continuation**. The arithmetic is exact; the 442-node comparison relies on the project's specified admissibility filter and should be reproduced from the complete node inventory. Establishing whether the entire combination is exceptional among competing valid continuations remains the appropriate next test. But taken together, these results identify `GO` as a particularly consequential endpoint, not just another plausible plaintext fragment.

---

## Reading the Evidence Together

The patterns in this report operate at several levels. Some arise from the **geometry of the opening matrix**, others from the **structure of the proposed English passages**, and others from **rune-index or prime-value arithmetic**. The LP1 comparisons add possible connections across the two parts of *Liber Primus*, through both a text passage and the numerical matrices. The matrix connection links the central FORM value of 91 to 934, then to the same 233 / 232 passage totals through prime-number indexing and the totient function. Further center-value correspondences link 809 to the 140-rune-index total of `SEE YOU SOON, THEN`, and $\varphi(91)=\varphi(111)=72$ to the derived key for `THEN`.

The full-route ciphertext checks add two further correspondences: **$3274+27=3301$** when every use is counted, and **$p_{2867}=26083$** when the 54 distinct cells are counted once. The first relates the route's ciphertext content to the matrix dimension; the second relates cell content to absolute position.

The continuation to **`THE KEY IS TO GO`** adds a particularly coherent endpoint. At **generation block 21**, the reading reaches **27 words**; its cumulative rune-index sum is **860**, and **$\varphi(860)=336$** leads precisely to the opening **`J(13,12)`** cell. Independently, its cumulative GP value is **3089**, the **442nd prime**, matching the reported **442 admissible mirrored three-rune nodes** after the F-branch exclusions.
