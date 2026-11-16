# Report 01 — The 3301 Constraints and the Recovery of I ASK

**Liber Primus, LP2 pages 0–2 · The 27 × 27 map · 16 November 2026**

Two arithmetic checks tied to **3301** reduce **21,342** admissible final assignments to a single key and ciphertext segment. That segment decrypts to **I ASK**. Starting after block 34, **YOU**, the wider search recovers the runes of **GO | DO | AS | I ASK** without a dictionary. Two assignments survive. They use the same source coordinates, read the same ciphertext, and differ only in an unused key component.

## 1. The phase boundary after YOU

The recorded route through **YOU** ends at block 34 with accumulated phase $S=28$ and outer state $a=0$. Since the phase mode is selected by $\lfloor S/7\rfloor\bmod 4$, this is the route's first return to its initial mode. The arithmetic below begins with the next block. The accumulated phase itself continues from 28.

Coordinates are one-based `(row, column)` pairs. The row-major position is $n_0(r,c)=27(r-1)+c$. Rune indices range from 0 to 28. A rune with index $j$ has Gematria Primus weight $p_{j+1}$, where $p_1=2$. Write $R(W)$ for the sum of rune indices in a sequence $W$, and $\mathrm{GP}(W)$ for the sum of its prime weights. Let $P$ and $C_{\mathrm{tail}}$ denote the candidate plaintext and ciphertext after **YOU**.

## 2. The arithmetic and geometric checks

| Check | Required equality or placement |
| --- | --- |
| **G · Prime ordinal** | $\mathrm{GP}(P)=\pi(3301)=464$, where $\pi(x)$ counts primes up to $x$. |
| **C · Composite total** | $\sum n_0(\text{original source cells})+\mathrm{GP}(K_{\mathrm{last}})+R(P)=3301$. Count each source triple once per block and the last derived key once as a triple. |
| **I · Full plaintext index sum** | $1295+R(P)=p_{\varphi(\pi(3301))}=p_{224}=1423$. The index sum through **YOU** is 1295, so the ending must contribute 128. |
| **T · Ordered transpose** | Apply $(r,c)\mapsto(c,r)$ to each cell of the opening source, preserving the order of the three cells. The resulting terminal source is `(11,13), (12,13), (13,13)`. |
| **X · Ciphertext index sum** | $R(C_{\mathrm{tail}})=n_0(B)$, where $B$ is the first ciphertext cell of the candidate ending. |
| **K · Consumed-key totient** | $\varphi(\mathrm{GP}(K_{\mathrm{stream}}))=n_0(13,12)=336$. The stream counts only the key components applied to ciphertext, including repeated components. |

The index check **I** uses $\varphi(464)=224$. It shares the prime ordinal with **G**. Check **X** uses the first cell of **each candidate** after **YOU**, so the search does not supply the documented starting coordinate `(7,2)` or the number 164. The source identities and the original endpoint test are documented in the project. [Strongest Plaintext Evidence](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/blob/main/Start-reading-here/strongest-plaintext-evidence.md) · [Block 38 walkthrough](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/blob/main/plaintext-i-found/38-i-ask.md#12-retrospective-endpoint-check-without-a-dictionary)

## 3. Recovering the last block from AS

Hold the recorded route through **AS** fixed. At this point $S=32$ and $a=1$. The three blocks after **YOU** already contribute **270 GP**, **74 plaintext index units**, and **2,004** from the positions of their original source cells. The two checks tied to 3301 therefore become

$$
\mathrm{GP}(P_{\mathrm{last}})=464-270=194
$$

$$
\sum_{\text{last source cells}}n_0+\mathrm{GP}(K_{\mathrm{last}})+R(P_{\mathrm{last}})
=3301-2004-74=1223.
$$

The search enumerates straight ciphertext segments of **2–27 runes** and equally spaced three-cell source nodes on the four grid axes. It applies the axis, orientation, phase, parity, and compatibility rules in Reports 00–15. Source rune indices range from 1 to 28, following Report 00. Non-mirror sources may be read in either order, and the center may be used directly or transformed by Euler's totient. Reversing a mirror source or applying a transformation that leaves the key identical counts once. Each assignment specifies a source, a key operation, and a ciphertext segment.

| Conditions beyond Reports 00–15 | Remaining assignments |
| --- | ---: |
| Baseline | 21,342 |
| **G** alone | 48 |
| **C** alone | 15 |
| **I** alone | 132 |
| **T** alone | 119 |
| **G + C** | **1** |
| **G + I** | 9 |
| **G + T** | **1** |
| **C + I** | 3 |
| **C + T** | 2 |
| **I + T** | 2 |
| **C + X** | **1** |
| **T + X** | **1** |

Every one-assignment row selects the same result. The original source runs down column 13 from row 11 to row 13. Phase 0 leaves the direct key **T–M–EA** in order. The ciphertext runs down column 17 from row 5 to row 8.

| Cell | Ciphertext index | Key index | Plaintext index modulo 29 | Rune |
| --- | ---: | ---: | ---: | --- |
| `(5,17)` | 26 | 16 | 10 | I |
| `(6,17)` | 14 | 19 | 24 | A |
| `(7,17)` | 14 | 28 | 15 | S |
| `(8,17)` | 21 | 16 | 5 | C/K |

The four runes give **I ASK** with the K reading of the last rune. Their index sum is **54** and their GP sum is **194**. The source positions sum to $283+310+337=930$. The key triple has GP $59+71+109=239$, so $930+239+54=1223$. Repeating the key for the fourth cell is part of decryption. The composite check uses the three-rune key once.

- **G + C** recovers the assignment without a prescribed block length, dictionary, or terminal geometry.
- **G + T** depends on ordered transposition. Allowing both orders of the three transposed cells gives two assignments under **G**, one reading **I ASK** and the other **AA**. The composite check rejects the reverse-order alternative.
- **T + X** recovers the same source and ciphertext using geometry and ciphertext indices alone. This reproduces the separate endpoint check recorded in the project. [Block 38 endpoint test](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/blob/main/plaintext-i-found/38-i-ask.md#12-retrospective-endpoint-check-without-a-dictionary)

A sensitivity scan replaced 3301 with each of the five preceding and five following primes, using the corresponding prime ordinal in **G**. In this eleven-prime window, only $p_{464}=3301$ produced a joint **G + C** match. The scan uses the same fixed prefix and candidate catalog.

## 4. Recovering the ending from YOU

The broader search fixes the route only through block 34 and enumerates endings of **one through four blocks**. The words, intermediate coordinates, individual block lengths, and position of the first new ciphertext cell are free variables. Each branch carries the phase state forward. The arithmetic selects from the branches that satisfy the transition rules.

An equally spaced source triple centered at $M$ contributes $3n_0(M)$ because $n_0$ is affine in row and column. Each triple contributes a multiple of three, so **C** and **I** determine the residue of the final key's GP.

$$
\mathrm{GP}(K_{\mathrm{last}})\equiv3301-128\equiv2\pmod 3.
$$

The transposed source has the direct key **T–M–EA**, with GP **239**, and the center-transformed key **T–E–EA**, with GP **235**. Only 239 has the required residue. With the terminal center at $n_0=310$, the other centers must sum to

$$
\frac{3301-128-239}{3}-310=668.
$$

| Terminal geometry | Checks used after YOU | Assignments | Distinct rune sequences |
| --- | --- | ---: | ---: |
| Ordered transpose | **G + C + I + T** | 12 | 10 |
| Ordered transpose | **G + C + I + T + X** | **2** | **1** |
| Transposed cells, either reading order | **G + C + I**, with the transposed cell set fixed | 17 | 14 |
| Transposed cells, either reading order | **G + C + I + X**, with the transposed cell set fixed | **2** | **1** |

Four blocks are the **shortest feasible ending** under these conditions. The bound of four comes from the recorded route. Within that range, **X** resolves the plaintext ambiguity even when the terminal source order is left open.

Both surviving assignments give **GO | DO | AS | I ASK**. The two aligned keys for **AS** are `(14,11,17)` and `(14,11,16)`. The block consumes only `(14,11)`, so the distinction does not change any decrypted rune. Among the six orders of the three recovered blocks before **I ASK**, only **GO → DO → AS** passes the transitions from **YOU**. The position sum and the rune totals are shared by all six orders. The transition rules supply the ordering.

### Recovered values

| Block | Ciphertext segment | Plaintext indices | Plaintext GP | Ciphertext index sum | Source-position sum |
| --- | --- | --- | ---: | ---: | ---: |
| **GO** | `(7,2) → (8,1)` | `6, 3` | 24 | 3 | 546 |
| **DO** | `(27,1) → (27,2)` | `23, 3` | 96 | 51 | 1,005 |
| **AS** | `(22,2) → (22,1)` | `24, 15` | 150 | 35 | 453 |
| **I ASK** | `(5,17) → (8,17)` | `10, 24, 15, 5` | 194 | 75 | 930 |
| **Total** | **10 runes** | **Index sum 128** | **464** | **164** | **2,934** |

The recovered branch satisfies $2934+239+128=3301$ and $R(C_{\mathrm{tail}})=164=n_0(7,2)$. The earlier dictionary check also accepted only these two assignments among the twelve ordered candidates. Check **X** reaches the same result using the ciphertext. [Word-frequency list used for the earlier check](https://www.norvig.com/ngrams/)

### A second recovery without the earlier plaintext sum

With ordered transposition fixed, I removed **I** and searched again with **G + C + T + X**, admitting both terminal center operations. This left **three assignments**. Two give **GO | DO | AS | I ASK**. The third gives the literal transliteration `GO | PDOEBI | FFS | HS`. Both readings have GP 464, the same source-position total of 2,934, and ciphertext index sum 164. The third assignment raises the plaintext index sum from 128 to 132 and lowers the final key's GP from 239 to 235. The changes cancel in **C**.

| Reading | Final derived key | Plaintext index sum | GP of consumed key stream | Totient |
| --- | --- | ---: | ---: | ---: |
| **GO \| DO \| AS \| I ASK** | T–M–EA | 128 | 674 | **336** |
| `GO, PDOEBI, FFS, HS` | T–E–EA | 132 | 886 | 442 |

Check **K** removes the third assignment. The recovered key stream has GP $674=2\times337$, so its totient is **336**, the row-major position of the opening source center `(13,12)`. This supplies an alternative to **I** for the ordered search. It uses the opening center and the state after **YOU**, with no earlier plaintext sum in the test. The project had previously used this totient check in its fixed-prefix endpoint search. [Block 38 endpoint test](https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/blob/main/plaintext-i-found/38-i-ask.md#12-retrospective-endpoint-check-without-a-dictionary)

## 5. Reproduction and scope

The endpoint counts use the map and route in project snapshot `ab9d8190e60009179563ac21b2d750271c2782b3`. The baseline verifier reproduces the 21,342-candidate endpoint search and the 12 ordered continuations from **YOU**.

```bash
python3 verify.py "/path/to/original-project.zip" --tail 34
```

To reproduce the ciphertext-only comparison on the ordered continuations, evaluate **X** on every retained path before applying any word list. In the verifier, a path consists of `(node, block)` pairs.

```python
def passes_ciphertext_check(path):
    first_cell = path[0][1].start
    total = sum(cell_value(c) for _, block in path for c in block.cells)
    return total == POSITION[first_cell][0]
```

For the two-order comparison, retain both readings of the transposed source and use the same GP, plaintext-index, and center-position targets for each. For the search without **I**, enumerate both center operations for the final key. For each terminal key, the target for the suffix index sum plus three times the sum of the nonterminal center positions is `3301 − GP(final key) − 3 × 310`, or **2,132** for the direct key and **2,136** for the transformed key. At each step, enumerate the source–segment pairs admitted by the transition rules. Close the branch only when its accumulated totals satisfy the chosen equalities. [Reproduction archive](https://chatgpt.com/library?file_id=libfile_179cbd74ead881918550a88c7c067947)

The identities were documented after the candidate route was found. The counts establish uniqueness of the plaintext within the stated search model and prefix. Establishing a decoding rule for the rest of pages 0–2 would require applying fixed conditions to a segment chosen independently of its proposed plaintext.
