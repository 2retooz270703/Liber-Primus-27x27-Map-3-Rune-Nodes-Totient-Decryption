# Strongest Plaintext Evidence

The reconstructed plaintext contains several numerical relationships that connect its wording, rune counts, Gematria Primus values, and the ciphertext–key arithmetic. These relationships were examined **after** the route produced the candidate words; they were not used to choose the plaintext.

Unless stated otherwise, **GP sum** means the sum of the runes' **0-based Gematria Primus indices (0–28)**. The later factorization of `2163` uses the separate **prime-valued Gematria Primus** mapping. Multi-letter transliterations such as `TH`, `EA`, and `NG` each represent one rune.

## 1. The first seven-word block: 233

**AS I GO, THE WEATHER TURNS COLD**

The opening block, reconstructed across [`01-AS-I-GO-THE.md`](./plaintext-i-found/01-AS-I-GO-THE.md) through [`04-COLD.md`](./plaintext-i-found/04-COLD.md), contains **7 words, 21 runes, and a GP sum of 233**.

The rune count has a direct connection to the grid: **21 = 3 × 7**, and **NG = 21** is the rune at `NG(14,14)`, the exact center of the 27×27 matrix reached in `WEATHER`. Thus the number of runes in the first complete block matches the index of the matrix's central rune.

The final word offers a different connection:

```text
COLD = C(5) + O(3) + L(20) + D(23) = 51
233 = the 51st prime

COLD → 51 → 233 (whole-block GP sum)
```

The block's **last-word sum is the prime index of its entire sum**. The number 233 also appears in the Fibonacci sequence: `F₇ = 13` and `F₁₃ = 233`. Starting with the seven-word count gives a second path to the same value:

```text
7 → F₇ = 13 → F₁₃ = 233
```

These are different numerical relationships converging on **233**: word count, rune count, the central rune `NG`, the value of `COLD`, prime position, and Fibonacci indices.

## 2. The second seven-word block: 232

**THE IDEA OF THE END IS DEATH**

This block begins with the `THE` at the end of [`07-NOW-THE.md`](./plaintext-i-found/07-NOW-THE.md) and continues through [`12-DEATH.md`](./plaintext-i-found/12-DEATH.md). It contains **7 words, 17 runes, and a GP sum of 232**. Its total is related to the preceding block by Euler's totient function:

```text
First seven-word block:   233
Second seven-word block:  232

233 is prime → φ(233) = 233 − 1 = 232
```

This is the same `φ` operation used to transform rune values and generate keys throughout the reconstruction.

The second block also connects its **word count** and **rune count** to its final word. The **7th prime is 17**, and `B = 17` is the center of the `J-B-J` mirror used to generate the key for `DEATH`:

```text
7 words → 7th prime = 17 = B
φ(B = 17) = 16 = T
16th prime = 53
DEATH = D(23) + EA(28) + TH(2) = 53
```

In other words, **7 → 17 → 16 → 53 → DEATH**. The intermediate `17 → 16` is not just arithmetic: it reproduces the **`B → T`** center transformation in the `DEATH` key construction.

## 3. Both blocks reproduce their totals in the ciphertext–key layer

The two totals, **233** and **232**, can also be audited without simply summing the final plaintext. In each rune position, decryption subtracts the active key from the ciphertext modulo 29:

```text
Pᵢ = (Cᵢ − Kᵢ) mod 29

ΣP = ΣC − ΣK + 29 × wraps
```

Here **`wraps`** counts positions where `Cᵢ − Kᵢ` is negative and therefore needs **29** added to bring the result into the range `0–28`. This makes it possible to check the complete arithmetic of each block from its ciphertext and keys.

### First block — AS I GO, THE WEATHER TURNS COLD

| Stage | Ciphertext | Active key | Wraps | Plaintext GP |
|---|---|---|---:|---:|
| [`AS I GO THE`](./plaintext-i-found/01-AS-I-GO-THE.md) | `L-AE-N-TH-P-U-X` = **84** | `AE-I-EA-AE-I-EA-AE` = **151** | 5 | 78 |
| [`WEATHER`](./plaintext-i-found/02-WEATHER.md) | `NG-P-EO-O-E` = **67** | `X-X-I-X-X` = **66** | 2 | 59 |
| [`TURNS`](./plaintext-i-found/03-TURNS.md) | `A-OE-N-B-W` = **79** | `H-NG-C-H-NG` = **63** | 1 | 45 |
| [`COLD`](./plaintext-i-found/04-COLD.md) | `G-J-EA-A` = **69** | `U-H-H-U` = **18** | 0 | 51 |
| **Total** | **299** | **298** | **8** | **233** |

The entire block therefore satisfies:

```text
ΣC = 299
ΣK = 298
wraps = 8

ΣP = 299 − 298 + (8 × 29)
   = 1 + 232
   = 233
```

### Second block — THE IDEA OF THE END IS DEATH

The first `THE` here is the ending of `NOW THE` in chapter 07, while the later `THE` appears inside `OF THE` in chapter 09. Both occurrences decrypt the same **`A-J`** ciphertext under **`OE-OE`**, so the table counts the first separately and the second within `OF THE`.

| Stage | Ciphertext | Active key | Wraps | Plaintext GP |
|---|---|---|---:|---:|
| [`THE`](./plaintext-i-found/07-NOW-THE.md) | `A-J` = **35** | `OE-OE` = **44** | 1 | 20 |
| [`IDEA`](./plaintext-i-found/08-IDEA.md) | `J-E-D` = **52** | `U-A-A` = **49** | 2 | 61 |
| [`OF THE`](./plaintext-i-found/09-OF-THE.md) | `X-OE-A-J` = **71** | `J-OE-OE-OE` = **77** | 1 | 23 |
| [`END`](./plaintext-i-found/10-END.md) | `F-L-I` = **30** | `J-J-T` = **38** | 2 | 50 |
| [`IS`](./plaintext-i-found/11-IS.md) | `EO-D` = **35** | `TH-H` = **10** | 0 | 25 |
| [`DEATH`](./plaintext-i-found/12-DEATH.md) | `C-I-E` = **33** | `J-J-T` = **38** | 2 | 53 |
| **Total** | **256** | **256** | **8** | **232** |

Here the two aggregate values match **exactly**, and there are again eight wraps:

```text
ΣC = 256
ΣK = 256
wraps = 8

ΣP = 256 − 256 + (8 × 29)
   = 232
```

The contrast is unusually neat: the first block has **299 − 298 = 1**, while the second has **256 − 256 = 0**. Because both contain **8 wraps**, their plaintext sums differ by precisely one: **233 and 232**. As a smaller numerical correspondence, `φ(8) = 4`.

This table provides an **arithmetic audit of the reconstructed ciphertext–key pairs**. The modular identity must hold when the individual decryptions are correct; the additional observation is that the two blocks have the same wrap count and nearly identical ciphertext and key totals.

## 4. The prime-valued total through DEATH factors into YOU

For this comparison, switch from the 0-based rune indices to **standard prime-valued Gematria Primus**. Sum every recovered rune from the beginning through `DEATH`:

**AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH.**

The prime-valued subtotals make the result checkable:

| Plaintext block | Prime-valued GP sum |
|---|---:|
| `AS I GO THE WEATHER TURNS COLD` | 825 |
| `I MAY CRY NOW` | 484 |
| `THE IDEA OF THE END IS DEATH` | 854 |
| **Total through DEATH** | **2163** |

The factorization is:

```text
2163 = 3 × 7 × 103

U = 3
O = 7
Y = 103

2163 = Y × O × U
```

The next recovered words are **SEE YOU**. That creates an intriguing linguistic connection: the prime factors of the earlier plaintext total are exactly the prime-valued rune values needed to spell **YOU**.

Multiplication does **not** specify letter order. The factors `103, 7, 3`, when read from largest to smallest, give **Y-O-U**. This is a post-reconstruction correspondence, not a rule used to derive the words [`SEE`](./plaintext-i-found/13-SEE.md) or [`YOU`](./plaintext-i-found/14-YOU.md).

## 5. Four appearances of 51

The number **51** connects both an early word and a much later point in the text:

- **COLD = 51:** `C(5) + O(3) + L(20) + D(23)`.
- **SEE = 51:** `S(15) + E(18) + E(18)`.
- **233 is the 51st prime:** the sum of the first seven-word block.
- **51 plaintext runes have appeared by the end of SEE.**

The last count can be checked by taking the completed blocks and then adding the three runes of `SEE`:

```text
AS I GO THE WEATHER TURNS COLD    21 runes
I MAY CRY NOW                     10 runes
THE IDEA OF THE END IS DEATH      17 runes
SEE                                3 runes
                                  ──
Total                             51 runes
```

There is also a cross-block factorization:

```text
51 = 3 × 17
```

**3** is the word count of `SEE YOU SOON`; **17** is the rune count of `THE IDEA OF THE END IS DEATH`. These are separate features of neighboring parts of the same reconstructed text.

## 6. The 27 / 343 cube pair

Another exact relationship appears when the seven-word `DEATH` block is combined with the following three-word phrase **SEE YOU SOON**:

| Plaintext segment | Words | Runes | 0-based GP sum |
|---|---:|---:|---:|
| `THE IDEA OF THE END IS DEATH` | 7 | 17 | 232 |
| [`SEE YOU SOON`](./plaintext-i-found/15-SOON.md) | 3 | 10 | 111 |
| **Combined** | **10** | **27** | **343** |

Both combined totals are perfect cubes:

```text
17 + 10   = 27  = 3³
232 + 111 = 343 = 7³
```

The **3-word** count reappears as the cube root of the combined **rune count**, while the **7-word** count reappears as the cube root of the combined **GP sum**. These calculations intentionally stop at `SOON`, before the later continuation [`THEN`](./plaintext-i-found/16-THEN.md).

## 7. What these relationships show

The most striking feature for me is how many distinct parts of the reconstruction meet numerically: **233 → 232** through Euler's totient, the two blocks' matching **eight modular wraps**, the factorization **2163 = 3 × 7 × 103**, the repeated **51**, and the paired cubes **27** and **343**.

I found these relationships **after reconstructing the candidate plaintext from the grid and its keys**. I did not select words to satisfy the totals. That separation matters: the numbers offer ways to inspect the resulting text from a different angle, rather than being extra instructions inserted into the decryption.

The exact arithmetic is reproducible, but the larger question remains whether all route decisions can be derived from a single deterministic procedure. Some branch-selection steps still need a precise rule. For now, these connections are the most useful numerical patterns I have found for examining how the proposed plaintext fits together.
