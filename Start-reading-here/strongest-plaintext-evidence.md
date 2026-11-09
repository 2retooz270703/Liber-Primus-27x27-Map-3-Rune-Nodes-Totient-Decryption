# Strongest Plaintext Evidence

The proposed reading of *Liber Primus* LP2, pages 0–2, yields numerical correspondences involving **rune counts, rune-index sums, and Gematria Primus values**. These link parts of the plaintext to the geometry of the **27 × 27 matrix**, to three-rune key sources, and to material from LP1.

The route reaches **THE KEY IS TO GO TO THE EAST OF THE MAP** and **LIFE MAY BE THE DEATH OF YOU** before four more blocks extend it through **GO, DO AS I ASK**. That branch links **3301** to the complete plaintext index sum through prime ordinals and Euler's totient. Its last key source reflects the opening source across the main diagonal.

The numerical correspondences are observations on the **selected plaintext route**, evaluated separately from the decryption and transition rules.

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
10. [The opening route and 3301](#the-opening-route-and-3301)
11. [Cell values and prime-indexed positions](#cell-values-and-prime-indexed-positions)
12. [The GO closure: a return to J](#the-go-closure-a-return-to-j)
13. [Completing the map instruction](#completing-the-map-instruction)
14. [MAP LIFE: one continuous block](#map-life-one-continuous-block)
15. [Another seven-word passage: LIFE MAY BE THE DEATH OF YOU](#another-seven-word-passage-life-may-be-the-death-of-you)
16. [The reflection between MAY and YOU](#the-reflection-between-may-and-you)
17. [Coordinates match ciphertext and key indices](#coordinates-match-ciphertext-and-key-indices)
18. [The new branch, 729 cells, and the previous keys](#the-new-branch-729-cells-and-the-previous-keys)
19. [How selective are the new relationships?](#how-selective-are-the-new-relationships)
20. [The GO, DO AS I ASK branch](#the-go-do-as-i-ask-branch)
21. [The current reading boundary](#the-current-reading-boundary)
22. [Reading the evidence together](#reading-the-evidence-together)

---

## Reading the Numbers

The following distinctions are important throughout the report.

A **rune count** counts rune symbols, not English letters. A transliteration such as `TH` or `EA` can represent one rune. A **rune-index sum** adds the numerical indices of those symbols in the project's 29-rune alphabet, numbered **0 through 28**. A **prime-value sum**, written **GP**, instead adds the corresponding Gematria Primus prime values: index 0 maps to 2, index 1 to 3, and so on through index 28, which maps to 109. These are two different totals and should not be confused.

Matrix coordinates are written as **(row, column)**, beginning at 1. For example, `J(13,12)` is the rune `J` in row 13, column 12. The symbol $\varphi(n)$ denotes **Euler's totient function**.

Block numbers follow the recorded plaintext route. **GO (22)** is part of the map instruction. **GO (35)** begins the branch after **YOU (34)**. A single decryption block can contain several English words, as in **MAP LIFE (28)** and **I ASK (38)**. Unless a distinct-cell set is explicitly specified, each actual ciphertext or key use is counted again when repeated. The notation $p_n$ means the $n$th prime, with $p_1=2$.

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

The cube bases echo the respective word counts: **3 words** in `SEE YOU SOON` and **7 words** in the preceding `DEATH` passage. Both exponents are 3; the values matching the word counts are the **bases, 3 and 7**.

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

The center of the second LP1 magic square is **809**, the **140th prime number**. Interestingly, **140** is also the exact **rune-index sum** of the 13 runes in **`SEE YOU SOON, THEN`** (51 + 30 + 30 + 29).

The first square has **FORM = 91** at its center, and $\varphi(91)=72$. Similarly, **`SEE YOU SOON`** has a rune-index sum of **111**, with $\varphi(111)=72$. This also matches the **derived key for `THEN`**: **`E–IA–IA`** = 18 + 27 + 27 = **72**.

These are exact numerical correspondences within the selected reading; whether they were intentionally encoded remains to be established.

---

## The Opening Route and 3301

### 61 ciphertext-cell uses across the first 17 stages

The first **17 decryption stages**, ending at `THEN`, produce the following proposed plaintext:

```text
AS I GO, THE WEATHER TURNS COLD.
I MAY CRY NOW.
THE IDEA OF THE END IS DEATH.
SEE YOU SOON, THEN.
```

This stretch involves **61 uses of ciphertext cells**, covering **54 distinct coordinates**. The difference represents **7 additional uses of previously counted cells**. Each repeated use contributes again to the total through THEN.

Let $C_t$ be the ciphertext rune used at step $t$. Summing the **GP prime values of the ciphertext runes before key subtraction** gives:

$$
\sum_{t=1}^{61}GP(C_t)=3274.
$$

Adding the side length of the **27 × 27 matrix** produces the signature number **3301**:

$$
\boxed{3274+27=3301.}
$$

This is a possible **authorial checksum**: the ciphertext total for the complete selected block combines with the matrix dimension to recover 3301.

The calculation uses the **main `SOON` placement in row 25**. The recorded alternative in row 27 gives a GP total of **3214** through THEN, for which $3214+27=3241$. Both placements decrypt to `SOON`, so this numerical condition distinguishes the two recorded routes even though their plaintext is the same.

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

The **3301 equality through THEN** counts every use, including repetitions. The **prime-index equality** counts each coordinate once, in the original matrix orientation. Both describe the selected `AS I GO`–`THEN` route, using two explicitly defined counting conventions.

The prime-index equality is a property of the **visited set of cells**; it does not determine their reading order or the keys. These are exact, reproducible numerical observations. Their interpretation as intentional clues should be tested against alternative routes using the same counting and numbering conventions.

---

## The GO Closure: A Return to J

### The 22nd decryption block completes a 27-word reading

The proposed continuation beyond `THEN` is **`THE KEY IS TO GO`**, with **`GO` appearing as the 22nd decryption block**. At this exact endpoint, the accumulated plaintext contains **27 English words** — the same number as the side length of the **27 × 27 rune matrix**.

| Consecutive plaintext passage | Words | Rune-index sum | GP prime-value sum |
|---|---:|---:|---:|
| `AS I GO, THE WEATHER TURNS COLD` | 7 | 233 | 825 |
| `I MAY CRY NOW` | 4 | 133 | 484 |
| `THE IDEA OF THE END IS DEATH` | 7 | 232 | 854 |
| `SEE YOU SOON, THEN` | 4 | 140 | 497 |
| **`THE KEY IS TO GO`** | **5** | **122** | **429** |
| **Total through GO** | **27** | **860** | **3089** |

The endpoint is therefore marked by both **map-block position 22** and a **27-word total**. More importantly, the two numerical totals independently lead to properties of the matrix and its permitted key structures.

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

The same continuation produces a **22nd-block endpoint**, a **27-word text** matching the matrix dimension, a **totient return to the exact starting coordinate**, and a **prime-index match to the matrix-wide admissible-node count**. The last two are especially compelling because they connect separate levels of the construction: **the accumulated plaintext to the origin of the route**, and **the accumulated prime values to the global key-space inventory**.

These correspondences provide **strong additional structural evidence for the selected `THE KEY IS TO GO` continuation**. The arithmetic is exact; the 442-node comparison relies on the project's specified admissibility filter and should be reproduced from the complete node inventory. Establishing whether the entire combination is exceptional among competing valid continuations remains the appropriate next test. But taken together, these results identify `GO` as a particularly consequential endpoint, not just another plausible plaintext fragment.

---

## Completing the Map Instruction

### From GO to the complete sentence

The selected continuation after THEN now reads:

> **THE KEY IS TO GO TO THE EAST OF THE MAP.**

It contains **11 English words and 25 runes**. Its two consecutive parts have the following plaintext totals:

| Portion of the instruction | Words | Runes | Rune-index sum | GP sum |
|---|---:|---:|---:|---:|
| THE KEY IS TO GO — blocks 18–22 | 5 | 11 | 122 | 429 |
| TO THE EAST OF THE MAP — blocks 23–28, through MAP only | 6 | 14 | 177 | 651 |
| **Complete instruction** | **11** | **25** | **299** | **1080** |

The boundary after MAP is an **English word boundary inside the extended block 28**. The same ciphertext and key continue into LIFE; the MAP-only totals remain valid when that boundary is stated explicitly.

### 530: the entry to the continuation

The word THEN has **GP = 101**. Adding the GP of the next five words gives:

$$
GP(\text{THEN})+GP(\text{THE KEY IS TO GO})=101+429=\boxed{530}.
$$

The first new block, THE (18), uses the original center **`M(20,17)`**. Its absolute position is:

$$
a(20,17)=27(20-1)+17=\boxed{530}.
$$

Thus the GP total of **THEN THE KEY IS TO GO** equals the position of the key center that begins this continuation. This uses the original source center, before its center-totient transformation.

### 359: TO THE EAST and the preceding rune count

The next three words contain **seven runes**:

| Word | Decrypted runes | Runes | GP sum |
|---|---|---:|---:|
| TO | T · O | 2 | 66 |
| THE | TH · E | 2 | 72 |
| EAST | EA · S · T | 3 | 221 |
| **TO THE EAST** | | **7** | **359** |

The accumulated plaintext through the preceding GO contains **72 runes**, and **359 is the 72nd prime**:

$$
\boxed{GP(\text{TO THE EAST})=359=p_{72}.}
$$

This connects the GP of the new three-word group with the rune count of the text immediately before it. The intervening THE also has **GP = 72**; that is a word-value coincidence within the same comparison, not another independent count of the preceding text.

### Seven eastern cells and seven western cells

The fourteen ciphertext cells for **TO THE EAST OF THE MAP** split into two equal groups on opposite sides of the matrix's central column 14:

| Plaintext group | Ciphertext cells in reading order | Runes | Side of the matrix |
|---|---|---:|---|
| TO | (12,23), (12,22) | 2 | East |
| THE | (9,19), (9,18) | 2 | East |
| EAST | (14,24), (15,23), (16,22) | 3 | East |
| **TO THE EAST** | **Columns 18–24** | **7** | **All east of column 14** |
| OF | (6,12), (7,13) | 2 | West |
| THE | (20,12), (20,13) | 2 | West |
| MAP | (19,11), (18,12), (17,13) | 3 | West |
| **OF THE MAP** | **Columns 11–13** | **7** | **All west of column 14** |

In particular, the ciphertext producing the word **EAST** occupies columns **24, 23, and 22**, on the eastern side of the map. The two seven-rune groups are a geometric partition of the selected placement; they are not claimed to be mirror images or a rule that forces every coordinate.

The three EAST ciphertext runes have **GP = 5 + 29 + 13 = 47**. This equals **GP(X)**, the original center rune of the preceding THE source and, later, the MAP LIFE source. This additional comparison uses GP values, not the ordinary index **X = 14**.

### 299: the instruction and the opening ciphertext

The complete instruction's **plaintext-index sum is 299**. The same number was recorded earlier as the **ciphertext-index sum of AS I GO, THE WEATHER TURNS COLD**:

$$
\boxed{\sum P_{\text{THE KEY IS TO GO TO THE EAST OF THE MAP}}
=299
=\sum C_{\text{AS I GO, THE WEATHER TURNS COLD}}.}
$$

The compared passages have different lengths: **25 plaintext runes** in the instruction and **21 ciphertext runes** in the opening passage. The equality concerns their totals, not a rune-by-rune correspondence. It is an additional exact cross-passage observation on the selected route.

---

## MAP LIFE: One Continuous Block

### The same key continues beyond MAP

Block 28 uses the original, non-mirror source **EO–X–I**, at **(15,9), (16,9), (17,9)**. Its phase is **1**, producing the aligned key **X–I–EO**, with indices **(14,10,12)**.

The ciphertext continues along the same up-right diagonal for **seven consecutive cells**:

| Order | Ciphertext cell | Ciphertext index | Consumed key index | Plaintext rune |
|---:|---|---:|---:|---|
| 1 | R(19,11) | 4 | 14 | M = 19 |
| 2 | C/K(18,12) | 5 | 10 | A = 24 |
| 3 | AE(17,13) | 25 | 12 | P = 13 |
| 4 | C/K(16,14) | 5 | 14 | L = 20 |
| 5 | L(15,15) | 20 | 10 | I = 10 |
| 6 | EO(14,16) | 12 | 12 | F = 0 |
| 7 | O(13,17) | 3 | 14 | E = 18 |

Each plaintext index is **(ciphertext index − consumed key index) mod 29**. The result is **M·A·P·L·I·F·E**, read as **MAP LIFE**. LIFE does not receive another key, phase calculation, or independent block number.

| Portion of block 28 | Runes | Plaintext-index sum | Plaintext GP |
|---|---:|---:|---:|
| MAP | 3 | 56 | 211 |
| LIFE | 4 | 48 | 173 |
| **MAP LIFE** | **7** | **104** | **384** |

### Transposed word-end coordinates

MAP ends at **(17,13)**, while the complete block ends at **(13,17)**:

$$
\boxed{(17,13)\longrightarrow(13,17).}
$$

Both points lie on the same anti-diagonal, **row + column = 30**. Reflection across **row = column** exchanges them. The geometric observation therefore belongs to a continuous seven-rune decryption, rather than to two separately placed words.

### The earlier MAP reflection remains an internal landmark

The opening center **J(13,12)** and the MAP LIFE source center **X(16,9)** are reflections across **row − column = 4**. The MAP word-end **P = (17,13)** lies on this axis, with equal squared distances:

$$
d^2(J,P)=4^2+1^2=17,
\qquad
d^2(X,P)=1^2+4^2=17.
$$

This connects the original starting center, the source center of MAP LIFE, and the internal MAP boundary. It should not be reassigned to the later endpoint **(13,17)**.

For the next transition, the complete seven-cell block and its actual endpoint **(13,17)** must be used. The extended block predicts a **horizontal** next ciphertext, matching MAY. Truncating the block after MAP changes that prediction to **diagonal**. The extension into LIFE therefore matters to the transition calculation as well as to the wording.

See the [block 28 walkthrough](../plaintext-i-found/28-map-life.md) for the source, subtraction, and endpoint checks.

---

## Another Seven-Word Passage: LIFE MAY BE THE DEATH OF YOU

### Separating the sentence from the decryption blocks

The new sentence is:

> **LIFE MAY BE THE DEATH OF YOU.**

Like the opening AS I GO passage and THE IDEA OF THE END IS DEATH, it contains **seven English words**. Here, however, the first word is already produced by the last four cells of MAP LIFE. Only the following **six words** are newly decrypted as blocks **29–34**.

| Scope | Words | Runes | Plaintext-index sum | Plaintext GP |
|---|---:|---:|---:|---:|
| LIFE — inside block 28 | 1 | 4 | 48 | 173 |
| MAY BE THE DEATH OF YOU — blocks 29–34 | 6 | 15 | 210 | 796 |
| **Complete sentence** | **7** | **19** | **258** | **969** |

The distinction between **15 runes after LIFE** and **19 runes in the complete sentence** is essential to the following calculations.

### 210 returns to LIFE through the totient function

LIFE has indices **L = 20, I = 10, F = 0, E = 18**, summing to **48**. The following six words have plaintext-index sum **210**:

$$
\boxed{\varphi(210)=\varphi(2\times3\times5\times7)=48
=20+10+0+18.}
$$

The last YOU ciphertext, at **(6,11), (6,12), (6,13)**, has indices **28, 11, 9**, also summing to **48**. Thus the same number occurs as the LIFE plaintext-index sum, the totient of the following plaintext-index sum, and the last ciphertext-index sum.

### 113 connects the first ciphertext to the last plaintext

The MAY ciphertext has indices **6, 5, 22**, giving GP **17 + 13 + 83 = 113**. The final plaintext YOU has indices **26, 3, 1**, giving GP **103 + 7 + 3 = 113**:

$$
\boxed{GP(C_{\mathrm{MAY}})=GP(P_{\mathrm{YOU}})=113.}
$$

YOU itself has index sum **30**, and **113 is the 30th prime**:

$$
GP(\mathrm{YOU})=p_{26+3+1}=p_{30}=113.
$$

The suffix total also satisfies **210 = 7 × 30**, where 7 is the complete sentence's word count. These are exact relationships, but the intrinsic values of YOU repeat wherever the same word is found; they do not by themselves select this placement or the words between MAY and YOU.

---

## The Reflection Between MAY and YOU

### The first and last blocks reflect in reading order

The first and last ciphertext blocks after LIFE occupy the same three columns:

| Reading order | MAY ciphertext | YOU ciphertext |
|---:|---|---|
| 1 | (18,11) | (6,11) |
| 2 | (18,12) | (6,12) |
| 3 | (18,13) | (6,13) |

Reflection across **row 12** exchanges the blocks, preserving their reading order:

$$
(r,c)\longmapsto(24-r,c).
$$

Both ciphertext cells of **OF**, at **(12,18) and (12,17)**, lie on the reflection axis. This is an exact relation between the first block, an intermediate block, and the last block. It does not assert that all six blocks form a symmetric figure.

MAY also shares **C/K(18,12)** with MAP LIFE. Both uses subtract **I = 10** and yield **A = 24**. The MAY source's lower outer cell, **AE(17,13)**, is the MAP word-end. These are concrete shared-cell connections between the two sentences.

### The final source reuses an earlier node

YOU uses the mirror **H–R–H**, at **(21,17), (21,22), (21,27)**. It is the same original node used for the earlier **IS (12)**. The center transformation gives **H–TH–H**, and phase 1 aligns the key as **TH–H–H**. All three components are consumed by YOU.

The source and derived index sums match the two ends of LIFE:

| Measurement | Index sum | Corresponding LIFE rune |
|---|---:|---|
| Original H–R–H | 8 + 4 + 8 = **20** | First rune: **L = 20** |
| Derived H–TH–H | 8 + 2 + 8 = **18** | Last rune: **E = 18** |

The node is not literally decrypted into LE; its two sums match those rune indices.

Its original GP is **23 + 11 + 23 = 57 = 3 × 19**, where 3 is the node length and 19 is the complete sentence's rune count. Its derived GP is **23 + 5 + 23 = 51**. This also returns to the number 51 discussed earlier, although here 51 is a **key GP total**, not a COLD or SEE index sum.

The final ciphertext's original absolute positions provide another local correspondence:

$$
146+147+148=441=21^2,
$$

where **21** is the row of the final key center. This is a supplementary relationship between ciphertext positions and the final key center.

---

## Coordinates Match Ciphertext and Key Indices

### Exactly what is counted

Take the **15 ciphertext-cell uses** producing **MAY BE THE DEATH OF YOU**, excluding LIFE. For each use, record its row number, column number, ciphertext rune index, and the aligned key index actually subtracted. Coordinates are **1-based**; rune indices are **0–28**.

For example, MAY uses **(18,11), (18,12), (18,13)**:

- Its row contribution is **18 + 18 + 18 = 54**.
- Its column contribution is **11 + 12 + 13 = 36**.
- Its ciphertext-index contribution is **6 + 5 + 22 = 33**.
- Its consumed-key contribution is **16 + 10 + 25 = 51**.

The individual MAY totals are different. The two matches emerge when the contributions of **all six blocks** are added:

| Block | Runes | Sum of rows | Sum of columns | Sum of ciphertext indices | Sum of consumed key indices |
|---|---:|---:|---:|---:|---:|
| MAY | 3 | 54 | 36 | 33 | 51 |
| BE | 2 | 51 | 23 | 5 | 28 |
| THE | 2 | 22 | 23 | 36 | 45 |
| DEATH | 3 | 33 | 27 | 25 | 30 |
| OF | 2 | 24 | 35 | 33 | 30 |
| YOU | 3 | 18 | 36 | 48 | 18 |
| **Total** | **15** | **202** | **180** | **180** | **202** |

Thus:

$$
\boxed{\sum r=\sum K=202,\qquad\sum c=\sum C=180.}
$$

These are **exact integer equalities**, before any reduction modulo 29. They connect the locations of the selected ciphertext cells to the indices of their ciphertext and consumed key stream.

Only consumed components are counted. In the two-rune blocks BE, THE, and OF, the unused third component of the aligned key contributes nothing. A repeated cell or key component contributes again whenever it is actually used; the calculation does not deduplicate the whole route.

### Checking the modular subtraction

The same ciphertext and key totals reproduce the suffix's plaintext-index sum:

$$
210=180-202+8\times29.
$$

There are **eight actual wraparounds**. This last identity follows from modular subtraction and verifies the bookkeeping. The additional observations are the equalities with **row and column sums**; modular subtraction does not require them.

The scope cannot silently be widened to include LIFE. For the complete nineteen-rune sentence, the row/key totals become **260 / 252**, and the column/ciphertext totals become **242 / 220**. The stated matches belong specifically to the **six-block continuation after LIFE**.

---

## The New Branch, 729 Cells, and the Previous Keys

### Prime-value totals of the consumed data

The comparisons in this section use **GP prime values** for the LIFE sentence and its six-block suffix through **YOU (34)**.

| Block after LIFE | Ciphertext GP | Consumed key GP | Plaintext GP |
|---|---:|---:|---:|
| MAY | 113 | 191 | 271 |
| BE | 14 | 96 | 128 |
| THE | 132 | 176 | 72 |
| DEATH | 92 | 105 | 203 |
| OF | 124 | 114 | 9 |
| YOU | 175 | 51 | 113 |
| **Total after LIFE** | **650** | **733** | **796** |

LIFE adds **173** to the plaintext GP, so the complete sentence has **GP = 173 + 796 = 969**.

### Two exact references to the matrix's 729 cells

The consumed key GP after LIFE is **733**. Subtracting LIFE's **four-rune length** gives the matrix's cell count:

$$
\boxed{GP(K_{\text{after LIFE}})-4=733-4=729=27^2.}
$$

A second expression uses the complete sentence's GP and the suffix ciphertext GP:

$$
\boxed{GP(P_{\text{LIFE sentence}})-\varphi(GP(C_{\text{after LIFE}}))
=969-\varphi(650)=969-240=729.}
$$

Here **650 = 2 × 5² × 13**, giving **φ(650) = 240**. The second formula deliberately compares the **19-rune plaintext sentence** with the **15-rune ciphertext suffix**. The two scopes are different and are specified rather than hidden.

### 969 connects the sentence's length and its final key

The complete sentence contains **19 runes**, and the fully consumed final key TH–H–H has **GP = 51**:

$$
\boxed{969=19\times51.}
$$

The same GP is also the number of ways to choose three positions from nineteen:

$$
\boxed{969=\binom{19}{3}=\frac{19\times18\times17}{3\times2\times1}.}
$$

The choice size **3** matches the three-rune node length. These are related descriptions of the same number: at a fixed length of 19, the binomial equality implies a quotient of 51. They should not be counted as statistically independent confirmations.

### 576 links the new sentence to TO THE EAST OF THE MAP

Factorizing **969 = 3 × 17 × 19** gives:

$$
\boxed{\varphi(969)=2\times16\times18=576=24^2.}
$$

The value **24** is the accumulated state **S** after MAP LIFE. More specifically, **576** is also the GP total of the key stream actually consumed by the preceding six-word segment **TO THE EAST OF THE MAP**:

| Earlier block | Key components consumed through this word | Consumed key GP |
|---|---|---:|
| TO (23) | G · D | 106 |
| THE (24) | X · S | 100 |
| EAST (25) | O · D · E | 163 |
| OF (26) | H · H | 46 |
| THE (27) | J · TH | 42 |
| MAP — first three runes of block 28 | X · I · EO | 119 |
| **Total through MAP** | **14 consumed components** | **576** |

Therefore:

$$
\boxed{\varphi(GP(\text{LIFE MAY BE THE DEATH OF YOU}))
=GP(K_{\text{TO THE EAST OF THE MAP}})=576.}
$$

This is a direct numerical bridge between the two consecutive passages and their selected keys. The earlier total stops at the **MAP word-end**. Including the following four key uses that produce LIFE would add **166**, changing that earlier key total to **742**.

The coordinate matches and the consumed-data GP relationships survive the three documented source variants obtained when reverse source-node readings are allowed. Those variants change an unused third component in BE. Relationships based on the sum of every full three-rune key are less stable and are not used as primary evidence here.

---

## How Selective Are the New Relationships?

### Comparison within the saved search catalogue

The saved bounded search contains **200,664 different strings**, represented by **600,549 saved routes**, with six to nine new words after LIFE. It includes many grammatically unnatural combinations and is not an exhaustive catalogue of all possible continuations.

A matched subset contains **14,218 different strings** with exactly **six new words** and **19 runes including LIFE**, with word boundaries falling between whole runes. Within that subset:

| Condition satisfied by at least one saved placement of a string | Strings |
|---|---:|
| Sum of rows = sum of consumed key indices | 88 |
| Sum of columns = sum of ciphertext indices | 92 |
| **Both coordinate equalities together** | **1** |

The string satisfying both is **MAY BE THE DEATH OF YOU**. This demonstrates selectivity within the saved comparison set. It is not a probability that the result occurred by chance, and it does not establish Cicada authorship: the properties were investigated after the sentence had been found, and the candidates are neither exhaustive nor equally likely.

### Testing the final block without a dictionary

A separate enumeration fixes only **MAY BE THE DEATH OF**, including all **13** admissible source/placement configurations for those five words. The final plaintext is left unspecified. All allowed straight final ciphertext segments of **2–27 runes**, their source nodes, and the permitted direct or center-totient operations are considered.

| Successive conditions | Remaining final ciphertext/source assignments |
|---|---:|
| Model constraints 01–10 | **80,341** |
| Plus both coordinate equalities | **3** |
| Plus consumed key GP = 729 + LIFE's four runes | **1** |
| Plus the second GP relation to 729 | **1** |

The remaining assignment uses ciphertext **(6,11) → (6,13)** and the final **H–R–H** source, producing **YOU**. Neither the word YOU nor its length of three runes was supplied as a lexical constraint. The second GP relation also holds for the survivor; it does not reduce the final count further.

When reverse source-node readings are additionally allowed, the analogous counts are **466,437 → 12 → 3**. All three survivors have the same YOU ciphertext geometry and final source; they differ in the earlier BE source's unused component.

The canonical **80,341 → 3 → 1** counts were independently reproduced by a second enumerator. Nevertheless, the numerical criteria came from the already observed sentence. This is a **retrospective selection test**, not a successful prediction made before seeing YOU.

### Sums do not recover the word order

All **720 = 6!** permutations of the six fixed block assignments preserve their coordinate and rune totals. The sum equalities therefore cannot determine the English order by themselves.

With those ciphertext cells and source nodes held fixed, the transition rules admit only:

> **MAY → BE → THE → DEATH → OF → YOU.**

The two kinds of evidence have different roles: the numerical equalities constrain the selected collection of cells and keys, while the transition checks constrain their order. This permutation test does not establish uniqueness among every alternative placement or source configuration.

---

## The GO, DO AS I ASK Branch

The continuation after **YOU (34)** consists of four decryption blocks. In **GO | DO | AS | I ASK**, each bar marks a block boundary. **I ASK** is one four-rune block with a continuous key stream across its two words. The branch adds **five English words and ten runes**.

| Block | Plaintext runes | Rune-index sum | GP sum |
| --- | --- | ---: | ---: |
| 35 · GO | G · O | 6 + 3 = 9 | 17 + 7 = 24 |
| 36 · DO | D · O | 23 + 3 = 26 | 89 + 7 = 96 |
| 37 · AS | A · S/Z | 24 + 15 = 39 | 97 + 53 = 150 |
| 38 · I ASK | I · A · S/Z · C/K | 10 + 24 + 15 + 5 = 54 | 31 + 97 + 53 + 13 = 194 |
| **Branch total** | **10 runes** | **128** | **464** |

### Source positions and 3301

In the unrotated matrix, a cell's 1-based row-major position is $n_0(r,c)=27(r-1)+c$. Count each of the three physical cells in each original source node once, including cells whose components are unused in the two-rune blocks.

| Block | Original source cells in reading order | $n_0$ positions | Position sum |
| --- | --- | --- | ---: |
| 35 · GO | Y(3,16) · G(7,20) · Y(11,24) | 70, 182, 294 | 546 |
| 36 · DO | C/K(13,21) · AE(13,11) · AE(13,1) | 345, 335, 325 | 1005 |
| 37 · AS | J(4,14) · B(6,16) · X(8,18) | 95, 151, 207 | 453 |
| 38 · I ASK | T(11,13) · M(12,13) · EA(13,13) | 283, 310, 337 | 930 |
| **Total** | **12 source cells** | | **2934** |

The three-rune key for **I ASK** is **T–M–EA**, with GP **59 + 71 + 109 = 239**. The decryption consumes **T–M–EA–T** across the four ciphertext cells, giving a consumed-stream GP of **298**. The correspondence uses the three-rune key counted once. Adding its GP and the branch's plaintext index sum to the source-position total gives

$$
\boxed{2934+239+128=3301.}
$$

### Prime ordinals and the complete reading

The branch's plaintext GP is **464**, and **3301 is the 464th prime**.

$$
p_{464}=3301.
$$

The plaintext index sum through **YOU (34)** is **1295**. The branch adds **128**, bringing the total from **AS I GO** through **I ASK** to **1423**. Since $464=2^4\times29$, Euler's totient gives

$$
\varphi(464)=2^3(29-1)=224.
$$

The **224th prime** is the complete candidate reading's index sum.

$$
\boxed{p_{\varphi(464)}=p_{224}=1423=1295+128.}
$$

### Reflection back to the opening source

The final source **T–M–EA** is the ordered reflection of the opening **AE–J–EA** source across the main diagonal. The map $(r,c)\mapsto(c,r)$ takes **AE(13,11)** to **T(11,13)** and the opening center **J(13,12)** to the final center **M(12,13)**. It fixes **EA(13,13)**, a cell shared by both sources. The original source center of **DO (36)** is also the opening **AE(13,11)** cell.

The sum to 3301 depends on the selected source positions. The prime and totient identities both use the branch's GP of 464. These relationships were identified after the branch was found. The block walkthroughs record the source order, modular subtraction, and incoming transition checks. [GO (35)](../plaintext-i-found/35-go.md) · [DO (36)](../plaintext-i-found/36-do.md) · [AS (37)](../plaintext-i-found/37-as.md) · [I ASK (38)](../plaintext-i-found/38-i-ask.md)

---

## The Current Reading Boundary

The accumulated plaintext totals distinguish the following boundaries along the selected route.

| Boundary on the selected route | Decryption block | English words | Runes | Plaintext-index sum | Plaintext GP |
|---|---|---:|---:|---:|---:|
| Through the GO in the map instruction | 22 | 27 | 72 | 860 | 3089 |
| Through MAP | Inside block 28 | 33 | 86 | 1037 | 3740 |
| Through MAP LIFE | Complete block 28 | 34 | 90 | 1085 | 3913 |
| Through YOU | 34 | 40 | 105 | 1295 | 4709 |
| **Through I ASK** | **38** | **45** | **115** | **1423** | **5173** |

The selected reading is therefore:

```text
AS I GO, THE WEATHER TURNS COLD.
I MAY CRY NOW.

THE IDEA OF THE END IS DEATH.
SEE YOU SOON, THEN.

THE KEY IS TO GO TO THE EAST OF THE MAP.
LIFE MAY BE THE DEATH OF YOU.
GO, DO AS I ASK.
```

The incoming transition to YOU is evaluated at **S = 27** and produces **S = 28**. The proposed cyclic phase schedule selects **Direct/+1** for the outgoing transition at that point. The four added blocks have phases **2, 0, 2, 0**, bringing the accumulated state to **S = 32** at I ASK. Block 38 is the endpoint of the recorded candidate route. [Report 11 — Cyclic phase modes](./11-seven-thresholds-and-cyclic-phase-modes.md)

---


## Reading the Evidence Together

The patterns in this report operate at several levels. Some arise from the **geometry of the opening matrix**, others from the **structure of the proposed English passages**, and others from **rune-index or prime-value arithmetic**. The LP1 comparisons add possible connections across the two parts of *Liber Primus*, through both a text passage and the numerical matrices. The matrix connection links the central FORM value of 91 to 934, then to the same 233 / 232 passage totals through prime-number indexing and the totient function. Further center-value correspondences link 809 to the 140-rune-index total of `SEE YOU SOON, THEN`, and $\varphi(91)=\varphi(111)=72$ to the derived key for `THEN`.

The ciphertext through THEN gives **$3274+27=3301$** when every use is counted and **$p_{2867}=26083$** when the 54 distinct cells are counted once. The first relates the opening ciphertext content to the matrix dimension. The second relates cell content to absolute position.

The continuation to **`THE KEY IS TO GO`** adds a particularly coherent endpoint. At **map block 22**, the reading reaches **27 words**; its cumulative rune-index sum is **860**, and **$\varphi(860)=336$** leads precisely to the opening **`J(13,12)`** cell. Independently, its cumulative GP value is **3089**, the **442nd prime**, matching the reported **442 admissible mirrored three-rune nodes** after the F-branch exclusions.


The complete map instruction adds a **530** reference to its first key center, a **359 = p₇₂** reference to the preceding rune count, and a division of its final fourteen ciphertext cells into **seven eastern and seven western cells**. Its index sum **299** also matches the opening seven-word passage's ciphertext-index sum. MAP continues into LIFE along the same diagonal and key stream, with transposed word-end coordinates **(17,13)** and **(13,17)**.

The new seven-word LIFE sentence adds an ordered **MAY ↔ YOU reflection**, with OF on its axis, and the recurring value **48** in LIFE, the suffix totient, and the last ciphertext. The final H–R–H source reuses an earlier IS node and supplies index sums matching LIFE's first and last runes.

Over the fifteen runes after LIFE, **Σ rows = Σ consumed key indices = 202** and **Σ columns = Σ ciphertext indices = 180**. GP calculations add the two references to **729**, the equality **969 = 19 × 51 = C(19,3)**, and the bridge **φ(969) = 576** to the keys actually consumed by TO THE EAST OF THE MAP.

The two sums that yield **3301** use different parts of the route. The earlier sum uses ciphertext through THEN and the matrix width. The later sum uses the four blocks after YOU, where the totient of the prime ordinal of 3301 links the branch's GP to the index sum through I ASK.

These observations use explicitly stated boundaries and counting conventions. Some are algebraically related; several reuse the same fixed words, source nodes, or totals. Their recorded selectivity supports further investigation of this route, while the post-selection search limits prevent interpreting the catalogue frequencies as probabilities of authenticity. A stronger test would apply the same criteria, fixed in advance, to material not selected for these numerical properties.
