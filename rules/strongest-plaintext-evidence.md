# Strongest Plaintext Evidence

*Starting point → Repeated numbers → Ciphertext checks*

The connections below come from the reconstructed plaintext and its 27 × 27 rune matrix. Unless noted otherwise, sums use **rune indices (0–28)**, not Gematria Primus prime values. `TH`, `EA`, and `NG` each count as one rune.

## 1. Why start at J(13,12)?

The red heading on page 0 has been counted as **13 runes**, split into two words of **8 + 5**. Euler's totient gives φ(13) = 12.

| Step | Calculation | Result |
|:---|:---|:---|
| Coordinates | (13, φ(13)) = (13, 12) | J(13,12) |
| Radius | 13 − 12 = 1 | One cell |
| Outer rune | 13 + 12 = 25 | AE = 25 |

At radius 1, the horizontal neighbors of J are:

| Cell | (13,11) | (13,12) | (13,13) |
|:---|:---:|:---:|:---:|
| Rune | AE | J | EA |

**AE–J–EA** has the predicted left outer `AE`. Its right outer `EA` reverses the same two letters; `AE` and `EA` are **different runes**, not identical mirror outers. Among the four radius-1 axes through J, only this one has the `AE / EA` pair.

The existing opening calculation then gives:

**φ(J = 11) + φ(10) = 10 + 4 = 14**

**AE(13,11) → RIGHT 14 → L(13,25)** — the beginning of [AS I GO, THE](./plaintext-i-found/01-AS-I-GO-THE.md).

This is a possible explanation for the starting node, found *after* the opening route was known. It is not yet a blind prediction.

## 2. The same numbers describe the page's words

A second count gives **158 words** across pages 0–2, including the two heading words.

| Count | Calculation | Result |
|:---|:---|:---|
| Body words | 158 − 2 | 156 |
| Heading pair | 13 and φ(13) = 12 | 13 × 12 = 156 |

The same **(13,12)** pair that identifies J can therefore also form a **13 × 12 word rectangle**, keeping the original word order and boundaries.

The word count and rectangle are a proposed structural connection. No reading instruction has yet shown how that rectangle should be used, and the word count should be checked against the original page transcription.

## 3. Two seven-word blocks: 233 and 232

| Recovered text | Words | Runes | Index sum |
|:---|:---:|:---:|---:|
| AS I GO, THE WEATHER TURNS COLD | 7 | 21 | **233** |
| THE IDEA OF THE END IS DEATH | 7 | 17 | **232** |

The first block runs through [COLD](./plaintext-i-found/04-COLD.md); the second begins with `THE` in [NOW THE](./plaintext-i-found/07-NOW-THE.md) and ends at [DEATH](./plaintext-i-found/12-DEATH.md).

| Connection | Calculation |
|:---|:---|
| Totient link | **φ(233) = 232**, since 233 is prime |
| Matrix center | **21** runes in the first block; **NG = 21** at the grid center (14,14) |
| Final word → block | **COLD = 5 + 3 + 20 + 23 = 51**; 233 is the **51st prime** |
| Fibonacci | **7 → F₇ = 13 → F₁₃ = 233** |
| DEATH key and sum | 7th prime = **17 = B**; φ(17) = **16 = T**; 16th prime = **53** |

The last row reproduces the center transformation **B → T** in the DEATH key. The word's index sum is also **DEATH = 23 + 28 + 2 = 53**.

## 4. The ciphertext–key totals

Each rune is decrypted by subtraction modulo 29. When subtraction is negative, add 29 once. Let **wraps** be the number of such additions.

**Plaintext sum = Ciphertext sum − Key sum + 29 × wraps**

### First block — 233

| Stage | Ciphertext | Key | Wraps | Plaintext |
|:---|---:|---:|---:|---:|
| [AS I GO THE](./plaintext-i-found/01-AS-I-GO-THE.md) | 84 | 151 | 5 | 78 |
| [WEATHER](./plaintext-i-found/02-WEATHER.md) | 67 | 66 | 2 | 59 |
| [TURNS](./plaintext-i-found/03-TURNS.md) | 79 | 63 | 1 | 45 |
| [COLD](./plaintext-i-found/04-COLD.md) | 69 | 18 | 0 | 51 |
| **Total** | **299** | **298** | **8** | **233** |

**299 − 298 + (8 × 29) = 233**

### Second block — 232

| Stage | Ciphertext | Key | Wraps | Plaintext |
|:---|---:|---:|---:|---:|
| [THE](./plaintext-i-found/07-NOW-THE.md) | 35 | 44 | 1 | 20 |
| [IDEA](./plaintext-i-found/08-IDEA.md) | 52 | 49 | 2 | 61 |
| [OF THE](./plaintext-i-found/09-OF-THE.md) | 71 | 77 | 1 | 23 |
| [END](./plaintext-i-found/10-END.md) | 30 | 38 | 2 | 50 |
| [IS](./plaintext-i-found/11-IS.md) | 35 | 10 | 0 | 25 |
| [DEATH](./plaintext-i-found/12-DEATH.md) | 33 | 38 | 2 | 53 |
| **Total** | **256** | **256** | **8** | **232** |

**256 − 256 + (8 × 29) = 232**

Both blocks have **8 wraps**. Their ciphertext-minus-key totals are **1** and **0**, giving the one-point difference between **233** and **232**. Also, φ(8) = 4.

The two instances of `THE` use the same `A–J` ciphertext and `OE–OE` key. These tables audit the arithmetic of the reconstructed words; the modular identity itself is not independent proof of the route.

## 5. The total through DEATH contains YOU

This section uses **prime-valued Gematria Primus**, not rune indices.

| Plaintext | Prime-valued sum |
|:---|---:|
| AS I GO, THE WEATHER TURNS COLD | 825 |
| I MAY CRY NOW | 484 |
| THE IDEA OF THE END IS DEATH | 854 |
| **Total through DEATH** | **2163** |

**2163 = 3 × 7 × 103**

| Rune | Y | O | U |
|:---|:---:|:---:|:---:|
| Prime value | 103 | 7 | 3 |

The prime factors, arranged from largest to smallest, spell **YOU** — part of the next recovered phrase, [SEE YOU](./plaintext-i-found/14-YOU.md). The multiplication alone does not specify this order.

## 6. Four appearances of 51

| Connection | Calculation |
|:---|:---|
| COLD | 5 + 3 + 20 + 23 = **51** |
| SEE | 15 + 18 + 18 = **51** |
| First block | **233** is the **51st prime** |
| Runes through SEE | 21 + 10 + 17 + 3 = **51** |

Also, **51 = 3 × 17**: `SEE YOU SOON` has **3 words**, and `THE IDEA OF THE END IS DEATH` has **17 runes**.

## 7. The 27 and 343 cubes

| Plaintext | Words | Runes | Index sum |
|:---|---:|---:|---:|
| THE IDEA OF THE END IS DEATH | 7 | 17 | 232 |
| [SEE YOU SOON](./plaintext-i-found/15-SOON.md) | 3 | 10 | 111 |
| **Combined** | **10** | **27** | **343** |

**17 + 10 = 27 = 3³**

**232 + 111 = 343 = 7³**

The cube roots **3** and **7** match the word counts of the two segments. This comparison ends at `SOON`, before [THEN](./plaintext-i-found/16-THEN.md).

---

All listed equalities can be checked, but numerical agreement does not by itself establish Cicada's intended plaintext. The starting-point proposal and these later patterns were identified retrospectively; a rule that predicts the next structure without knowing the next word is still needed.
