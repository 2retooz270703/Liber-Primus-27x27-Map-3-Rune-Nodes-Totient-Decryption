# Strongest Plaintext Evidence

*Starting point → Repeated numbers → Ciphertext checks*

These connections were found after reconstructing the candidate plaintext. Unless noted otherwise, sums use **rune indices (0–28)**, not Gematria Primus prime values. `TH`, `EA`, and `NG` each count as one rune.

## 1. The starting J

The red heading on page 0 contains **13 runes** in two words of 8 and 5. Euler's totient gives φ(13) = 12.

| Step | Calculation | Result |
|:---|:---|:---|
| Coordinates | (13, φ(13)) = (13,12) | J(13,12) |
| Radius | 13 − 12 = 1 | 1 cell |
| Outer value | 13 + 12 = 25 | AE = 25 |

At radius 1, the horizontal cells around J are:

| (13,11) | (13,12) | (13,13) |
|:---:|:---:|:---:|
| AE | J | EA |

The left outer is **AE = 25**. The right outer is **EA**: its Latin letters are reversed, but AE and EA are different runes, not a true mirror pair.

From AE(13,11), the opening movement is:

**φ(J = 11) + φ(10) = 10 + 4 = 14**

**AE(13,11) → RIGHT 14 → L(13,25)**

The heading may also relate to the page's word count:

**158 total words − 2 heading words = 156 = 13 × 12**

So the same pair **(13,12)** could describe a 13 × 12 arrangement of the body words. This is a hypothesis, not yet a reading rule; the word count needs independent verification.

## 2. Two seven-word blocks

| Plaintext | Words | Runes | Index sum |
|:---|:---:|:---:|---:|
| AS I GO, THE WEATHER TURNS COLD | 7 | 21 | **233** |
| THE IDEA OF THE END IS DEATH | 7 | 17 | **232** |

**φ(233) = 232**, because 233 is prime. The same totient operation appears in the key calculations.

Several other numbers connect the blocks to the matrix:

| Connection | Calculation |
|:---|:---|
| Matrix center | 21 runes in the first block; NG = 21 at (14,14) |
| Fibonacci | 7 → F₇ = 13 → F₁₃ = 233 |
| DEATH key | 7th prime = 17 = B; φ(17) = 16 = T |
| DEATH sum | 16th prime = 53; DEATH = 23 + 28 + 2 = 53 |

The **B → T** transformation also occurs in the key for DEATH.

## 3. Eight wraps in both blocks

Decryption subtracts each key index from its ciphertext index modulo 29. A *wrap* occurs when a negative result needs 29 added.

**Plaintext sum = Ciphertext sum − Key sum + 29 × wraps**

| Block | Ciphertext sum | Key sum | Wraps | Plaintext sum |
|:---|---:|---:|---:|---:|
| First | 299 | 298 | 8 | **233** |
| Second | 256 | 256 | 8 | **232** |

**299 − 298 + 8 × 29 = 233**  
**256 − 256 + 8 × 29 = 232**

Both blocks have **8 wraps**. Their ciphertext-minus-key totals differ by 1, matching **233 − 232 = 1**. Also, φ(8) = 4.

These equations check the reconstructed decryptions; they do not independently establish the route.

## 4. The total through DEATH points to YOU

This is the one section using **prime-valued Gematria Primus**, not rune indices.

| Plaintext | Prime-value sum |
|:---|---:|
| AS I GO, THE WEATHER TURNS COLD | 825 |
| I MAY CRY NOW | 484 |
| THE IDEA OF THE END IS DEATH | 854 |
| **Total** | **2163** |

**2163 = 103 × 7 × 3 = Y × O × U**

The factors, ordered from largest to smallest, spell **YOU**, a word recovered later. Factorization alone does not determine their order.

## 5. Four appearances of 51

| Connection | Calculation |
|:---|:---|
| COLD | 5 + 3 + 20 + 23 = **51** |
| SEE | 15 + 18 + 18 = **51** |
| First block | 233 is the **51st prime** |
| Runes through SEE | 21 + 10 + 17 + 3 = **51** |

Also, **51 = 3 × 17**: SEE YOU SOON contains 3 words, while THE IDEA OF THE END IS DEATH contains 17 runes.

## 6. The 27 and 343 cubes

| Plaintext | Words | Runes | Index sum |
|:---|---:|---:|---:|
| THE IDEA OF THE END IS DEATH | 7 | 17 | 232 |
| SEE YOU SOON | 3 | 10 | 111 |
| **Combined** | **10** | **27** | **343** |

**17 + 10 = 27 = 3³**  
**232 + 111 = 343 = 7³**

The cube roots **3** and **7** match the two segments' word counts. This comparison ends at SOON, before THEN.

These are reproducible numerical correspondences, not proof that the reconstructed plaintext was intended by Cicada. The starting-point proposal was found retrospectively, and a rule that predicts each next structure is still missing.
