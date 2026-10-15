## 1. The starting J

The red heading on page 0 has 13 runes. The number 13 and its totient, φ(13) = 12, lead to three related calculations:

| Connection | Calculation | Result |
|:---|:---|:---|
| Coordinates | (13, φ(13)) = (13, 12) | J(13,12) |
| Radius | 13 − 12 = 1 | 1 cell |
| Outer value | 13 + 12 = 25 | AE = 25 |

At radius 1, the horizontal cells are:

| Left (13,11) | Center (13,12) | Right (13,13) |
|:---:|:---:|:---:|
| AE | J | EA |

Starting from the left AE:

φ(J) + φ(φ(J)) = 10 + 4 = 14

AE(13,11) → RIGHT 14 → L(13,25)

158 words − 2 heading words = 156 = 13 × 12

## 2. Two seven-word blocks

| Plaintext | Words | Runes | Index sum |
|:---|:---:|:---:|---:|
| AS I GO, THE WEATHER TURNS COLD | 7 | 21 | 233 |
| THE IDEA OF THE END IS DEATH | 7 | 17 | 232 |

233 is prime, so φ(233) = 232.

| Connection | Calculation and meaning |
|:---|:---|
| Matrix center | 21 = 3 × 7 = NG; NG(14,14) is the center of the 27 × 27 matrix |
| COLD → 233 | COLD = 5 + 3 + 20 + 23 = 51; 233 is the 51st prime |
| Fibonacci | 7 → F₇ = 13 → F₁₃ = 233 |
| DEATH key | 7th prime = 17 = B; φ(17) = 16 = T, the J–B–J → J–T–J change |
| DEATH total | 16th prime = 53; D(23) + EA(28) + TH(2) = 53 |

## 3. Ciphertext sum = Key sum

| Seven-word block | Ciphertext sum | Key sum | Wraps | Plaintext sum |
|:---|---:|---:|---:|---:|
| First | **299** | **298** | 8 | 233 |
| Second | **256** | **256** | 8 | 232 |

First: 299 − 298 + 8 × 29 = 233

Second: 256 − 256 + 8 × 29 = 232

Also, φ(8) = 4.

## 4. The total through DEATH points to YOU

| Plaintext block | Prime-value sum |
|:---|---:|
| AS I GO, THE WEATHER TURNS COLD | 825 |
| I MAY CRY NOW | 484 |
| THE IDEA OF THE END IS DEATH | 854 |
| Total through DEATH | 2163 |

2163 = 103 × 7 × 3

| Factor | 103 | 7 | 3 |
|:---|:---:|:---:|:---:|
| Rune | Y | O | U |

The next recovered words are "SEE YOU". 

*Seek and **you** will be found. (2016)*

## 5. Four appearances of 51

| Connection | Calculation |
|:---|:---|
| COLD | 5 + 3 + 20 + 23 = 51 |
| SEE | 15 + 18 + 18 = 51 |
| First block | 233 is the 51st prime |
| Runes through SEE | 21 + 10 + 17 + 3 = 51 |

The rune count includes the first seven-word block (21), I MAY CRY NOW (10), the second seven-word block (17), and SEE (3).

## 6. The two cubes

| Plaintext | Words | Runes | Index sum |
|:---|---:|---:|---:|
| THE IDEA OF THE END IS DEATH | 7 | 17 | 232 |
| SEE YOU SOON | 3 | 10 | 111 |
| Combined | 10 | 27 | 343 |

17 + 10 = 27 = 3³ — 3 words in SEE YOU SOON.

232 + 111 = 343 = 7³ — 7 words in the DEATH block.

## 7. Two four-word blocks

| Plaintext | Words | Runes | Index sum | Prime-value sum |
|:---|:---:|:---:|---:|---:|
| I MAY CRY NOW | 4 | 10 | 133 | 484 |
| SEE YOU SOON, THEN | 4 | 13 | 140 | 497 |

| Difference | Calculation | Result |
|:---|:---|---:|
| Runes | 13 − 10 | 3 |
| Index sum | 140 − 133 | 7 |
| Prime-value sum | 497 − 484 | 13 |

The values 7 and 13 also connect to the Fibonacci relation in Section 2: F₇ = 13 and F₁₃ = 233 (with F₁ = F₂ = 1).

## 8. The opening LP1 warning matches the first LP2 sentence

The opening warning in LP1 says:

```text
BELIEVE NOTHNG FROM THIS BOOC
EXCEPT WHAT YOV CNOW TO BE TRVE
TEST THE CNOWLEDGE
FIND YOVR TRVTH
```

A **seven-word passage crossing the line break** between `TRVE` and `TEST` is:

**YOV CNOW TO BE TRVE TEST THE**

Compare it with the first recovered sentence proposed for LP2 pages 0–2:

**AS I GO, THE WEATHER TURNS COLD.**

| Property | LP2: AS I GO ... COLD | LP1: YOV CNOW ... THE |
|:---|---:|---:|
| Words | **7** | **7** |
| Runes | **21** | **21** |
| Prime-value sum | **825** | **825** |
| Rune-index sum | **233** | **232** |

These counts use Gematria Primus rune segmentation (`TH` and `EA` are single runes; LP1's `V` represents `U`). The sums can be checked word by word:

| LP2 word | Runes | Index sum | Prime sum | LP1 word | Runes | Index sum | Prime sum |
|:---|---:|---:|---:|:---|---:|---:|---:|
| AS | 2 | 39 | 150 | YOV | 3 | 30 | 113 |
| I | 1 | 10 | 31 | CNOW | 4 | 24 | 68 |
| GO | 2 | 9 | 24 | TO | 2 | 19 | 66 |
| THE | 2 | 20 | 72 | BE | 2 | 35 | 128 |
| WEATHER | 5 | 59 | 211 | TRVE | 4 | 39 | 140 |
| TURNS | 5 | 45 | 155 | TEST | 4 | 65 | 238 |
| COLD | 4 | 51 | 182 | THE | 2 | 20 | 72 |
| **Total** | **21** | **233** | **825** | **Total** | **21** | **232** | **825** |

The one-point difference is the same number pair already present in Section 2:

- The **first LP2 seven-word block** has rune-index sum **233**.
- The **LP1 warning passage** has rune-index sum **232**.
- The **second LP2 seven-word block**, `THE IDEA OF THE END IS DEATH`, also has rune-index sum **232**.
- Since **233 is prime**, **φ(233) = 232**.

The location gives the match an additional thematic connection: rather than coming from an arbitrary passage deep in LP1, the seven words belong to its **opening instruction to test what one knows to be true**. That is an especially suggestive place to find a numerical parallel with the proposed beginning of LP2.

**Interpretation:** the exact `7 words / 21 runes / prime sum 825` match, together with the `233 / 232` index relationship, is a striking cross-text correspondence. It is consistent with the possibility of an intentional marker, but **does not by itself prove deliberate placement or authenticate the proposed LP2 plaintext**; the significance should also be tested against alternative passages and selection rules.
