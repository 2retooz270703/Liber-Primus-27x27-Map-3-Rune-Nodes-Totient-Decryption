These patterns were noticed after the candidate plaintext was reconstructed, not used to choose its words. Unless noted otherwise, sums use rune indices 0–28, not prime-valued Gematria Primus.

## 1. The starting J

The red heading on page 0 has 13 runes. Since φ(13) = 12, those numbers suggest the starting coordinates:

| Connection | Calculation | Result |
|:---|:---|:---|
| Position | (13, φ(13)) = (13, 12) | J(13,12) |
| Radius | 13 − 12 = 1 | 1 cell |
| Outer value | 13 + 12 = 25 | AE = 25 |

The three horizontal cells at radius 1 are:

| (13,11) | (13,12) | (13,13) |
|:---:|:---:|:---:|
| AE | J | EA |

The proposed departure is the left AE(13,11):

φ(J) + φ(φ(J)) = 10 + 4 = 14

AE(13,11) → RIGHT 14 → L(13,25)

Using the word count for pages 0–2 gives another possible connection:

158 total words − 2 heading words = 156 = 13 × 12

## 2. Two seven-word blocks

The first two complete seven-word segments have totals differing by exactly one:

| Plaintext | Words | Runes | Index sum |
|:---|:---:|---:|---:|
| AS I GO, THE WEATHER TURNS COLD | 7 | 21 | 233 |
| THE IDEA OF THE END IS DEATH | 7 | 17 | 232 |

Because 233 is prime, its totient is φ(233) = 232.

The two blocks contain several further connections:

| Connection | Calculation | Meaning |
|:---|:---|:---|
| Matrix center | 21 = 3 × 7 = NG | First block: 21 runes; NG(14,14) is the matrix's central rune |
| Final word COLD | C(5) + O(3) + L(20) + D(23) = 51 | 233 is the 51st prime |
| Fibonacci | 7 → F₇ = 13 → F₁₃ = 233 | The seven-word count also leads to 233 |
| DEATH key | 7th prime = 17 = B; φ(17) = 16 = T | The center of J–B–J changes B → T |
| Final word DEATH | 16th prime = 53; 23 + 28 + 2 = 53 | D–EA–TH has index sum 53 |


## 3. Eight wraps in both blocks

A wrap means the subtraction is negative, so 29 is added once. For a whole segment:

**Plaintext sum = Ciphertext sum − Key sum + 29 × wraps**

### First block — 233

| Stage | Ciphertext sum | Key sum | Wraps | Plaintext sum |
|:---|---:|---:|---:|---:|
| AS I GO THE | 84 | 151 | 5 | 78 |
| WEATHER | 67 | 66 | 2 | 59 |
| TURNS | 79 | 63 | 1 | 45 |
| COLD | 69 | 18 | 0 | 51 |
| Total | **299** | **298** | 8 | 233 |

**299 − 298 + 8 × 29 = 233**

### Second block — 232

| Stage | Ciphertext sum | Key sum | Wraps | Plaintext sum |
|:---|---:|---:|---:|---:|
| THE | 35 | 44 | 1 | 20 |
| IDEA | 52 | 49 | 2 | 61 |
| OF THE | 71 | 77 | 1 | 23 |
| END | 30 | 38 | 2 | 50 |
| IS | 35 | 10 | 0 | 25 |
| DEATH | 33 | 38 | 2 | 53 |
| **Total** | **256** | **256** | **8** | **232** |

**256 − 256 + 8 × 29 = 232**

Both blocks have **8 wraps**, but their ciphertext-minus-key totals are **1** and **0**. This accounts for the one-point difference between **233** and **232**. Another numerical connection is φ(8) = 4.

<details>
<summary>Exact ciphertext and key sequences</summary>

The tables above come from these rune sequences. Values in parentheses are their index sums.

**First block**

| Stage | Ciphertext | Active key |
|:---|:---|:---|
| AS I GO THE | L–AE–N–TH–P–U–X (84) | AE–I–EA–AE–I–EA–AE (151) |
| WEATHER | NG–P–EO–O–E (67) | X–X–I–X–X (66) |
| TURNS | A–OE–N–B–W (79) | H–NG–C–H–NG (63) |
| COLD | G–J–EA–A (69) | U–H–H–U (18) |

**Second block**

| Stage | Ciphertext | Active key |
|:---|:---|:---|
| THE | A–J (35) | OE–OE (44) |
| IDEA | J–E–D (52) | U–A–A (49) |
| OF THE | X–OE–A–J (71) | J–OE–OE–OE (77) |
| END | F–L–I (30) | J–J–T (38) |
| IS | EO–D (35) | TH–H (10) |
| DEATH | C–I–E (33) | J–J–T (38) |

The first **THE** is the end of **NOW THE**; the later **THE** belongs to **OF THE**. Both use ciphertext **A–J** and key **OE–OE**, and are counted as separate occurrences.

</details>

The modular identity verifies the arithmetic of the proposed decryptions. It does **not** independently prove that the selected ciphertext positions and keys form the intended route.

## 4. The total through DEATH spells YOU

This is the only section using **prime-valued Gematria Primus**, rather than rune indices. The sum covers all recovered runes from the beginning through DEATH:

| Plaintext | Prime-value sum |
|:---|---:|
| AS I GO, THE WEATHER TURNS COLD | 825 |
| I MAY CRY NOW | 484 |
| THE IDEA OF THE END IS DEATH | 854 |
| **Total** | **2163** |

**2163 = 3 × 7 × 103**

| Rune | U | O | Y |
|:---|:---:|:---:|:---:|
| Prime value | 3 | 7 | 103 |

Read from largest to smallest, the factors give **103–7–3 = Y–O–U**. The next recovered words are **SEE YOU**.

Multiplication does not determine the order of the letters; this is a retrospective correspondence, not a method for deriving YOU.

*Seek and you will be found.*

## 5. Four appearances of 51

| Connection | Calculation |
|:---|:---|
| COLD | C(5) + O(3) + L(20) + D(23) = **51** |
| SEE | S(15) + E(18) + E(18) = **51** |
| First block | **233 is the 51st prime** |
| Runes through SEE | 21 + 10 + 17 + 3 = **51** |

The rune count consists of **21** in the first seven-word block, **10** in I MAY CRY NOW, **17** in the second seven-word block, and **3** in SEE.

Also, **51 = 3 × 17**: SEE YOU SOON contains **3 words**, while THE IDEA OF THE END IS DEATH contains **17 runes**.

## 6. The two cubes: 27 and 343

Combine the second seven-word block with the following three-word phrase:

| Plaintext | Words | Runes | Index sum |
|:---|---:|---:|---:|
| THE IDEA OF THE END IS DEATH | 7 | 17 | 232 |
| SEE YOU SOON | 3 | 10 | 111 |
| **Combined** | **10** | **27** | **343** |

**17 + 10 = 27 = 3³** — the cube root **3** matches the word count of SEE YOU SOON.

**232 + 111 = 343 = 7³** — the cube root **7** matches the word count of the DEATH block.

For SEE YOU SOON, the index sum is **51 + 30 + 30 = 111**. The comparison deliberately stops at **SOON**, before the later continuation THEN.
