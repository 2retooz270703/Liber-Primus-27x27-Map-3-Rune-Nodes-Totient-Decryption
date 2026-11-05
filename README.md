# Plaintext

<sub>4.11.2026</sub>

**Red runes: Secuendi Ratio ("The method of following.")**

As I go, the weather turns cold.  
I may cry now.  

The idea of the end is death.  
See you soon, then.  

The key is to go to the east of the map.  
Life may be the death of you.

---
---

## Welcome

This project arranges the pages’ 729 runes into a single 27 × 27 matrix and investigates how its geometry connects ciphertext, key material, and reading order. The proposed method combines *three-rune key nodes*, *Euler’s totient function*, *Möbius signatures*, and *repeating-key subtraction modulo 29*.

For a first pass, read **[Report 00](./Start-reading-here/00-decryption-method.md)**, follow the **[opening block](./plaintext-i-found/01-as-i-go-the.md)**, and compare its coordinates with the **[map](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)**.

## How the method works

### 1. Identify a three-rune node

A key node consists of three equally spaced cells on a horizontal, vertical, or 45° diagonal line. Nodes may be **mirror** structures with equal outer runes, or **non-mirror** structures with different outer runes.

### 2. Derive the key

For a node using the center transformation, keep its outer rune indices and replace its center index with Euler’s totient:

$$
(a,b,c)\longmapsto\bigl(a,\varphi(b),c\bigr).
$$

Some documented nodes use their original indices directly. Each walkthrough specifies which operation is used.

### 3. Calculate the key phase

For the derived key in its unrotated order, calculate its Möbius signature and phase:

$$
\sigma_i=\mu\!\left(\varphi(k_i)\right),
\qquad
p=(\sigma_1+\sigma_2+\sigma_3)\bmod3.
$$

Rotate the three-rune key **left by `p` positions**.

### 4. Decrypt the selected ciphertext

Repeat the aligned key across the block and subtract rune indices:

$$
P_i=(C_i-K_i)\bmod29.
$$

### 5. Evaluate the next transition

The transition reports use the current block’s geometry and key data to predict or filter properties of the next block: signature, reading axis, direction, coordinate parity, alignment, and node type. These constraints narrow the search; selecting an exact next location remains an open problem.

### Worked example: WEATHER

The node **`X–OE–X`**, at row 14, columns 4–6, becomes **`X–I–X`** because `φ(22) = 10`. Its signature is `(+1, 0, +1)`, giving phase **2** and the aligned key **`X–X–I`**.

Read row 14, columns 14–18:

| Ciphertext indices | Repeated key indices | Plaintext indices | Plaintext runes |
| :--- | :--- | :--- | :--- |
| `21, 13, 12, 3, 18` | `14, 14, 10, 14, 14` | `7, 28, 2, 18, 4` | `W · EA · TH · E · R` |

The result is **WEATHER**. `EA` and `TH` each represent one rune. See the **[complete calculation](./plaintext-i-found/02-weather.md)** for the node, movement, coordinates, and subtraction table.

## Method and transition reports

Read these in order for the full model, or go directly to a specific constraint.

| Report | Subject | What it defines or tests |
| :---: | :--- | :--- |
| [00](./Start-reading-here/00-decryption-method.md) | Decryption method | Rune indices, key derivation, phase, and subtraction modulo 29. |
| [01](./Start-reading-here/01-next-key-signature.md) | Next-key signature | Predicts the next signature and phase using ciphertext positions and running state. |
| [02](./Start-reading-here/02-leftmost-cell-and-rotations.md) | Leftmost cell and rotations | Checks the current mode and predicts whether the next leftmost cell is read first or last. |
| [03](./Start-reading-here/03-predicting-axis-and-reading-direction.md) | Axis and reading direction | Predicts a horizontal, vertical, or diagonal axis and the reading boundary. |
| [04](./Start-reading-here/04-predicting-next-key-center-parity.md) | Key-center parity | Predicts the row and column parity of the next original key center. |
| [05](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md) | Ciphertext row parity | Predicts row parity for the next endpoint and leftmost cell. |
| [06](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) | Ray alignment | Tests the next beginning against eight rays and a conditional one-cell allowance. |
| [07](./Start-reading-here/07-predicting-next-key-mirror-status.md) | Mirror status | Predicts whether the next original node has matching outer runes. |
| [08](./Start-reading-here/08-minimum-ciphertext-block-length.md) | Minimum block length | Requires at least two runes per independently decrypted block. |
| [09](./Start-reading-here/09-predicting-next-ciphertext-column-parity.md) | Ciphertext column parity | Predicts the column parity of the next leftmost cell. |
| [10](./Start-reading-here/10-squarefree-gcd-compatibility.md) | Squarefree-GCD compatibility | Tests four numerical relationships between a proposed key center and ciphertext cells. |

## Plaintext walkthroughs

Each walkthrough identifies the source node, key, phase, ciphertext cells, and resulting runes. The numbering follows the interactive map. **A block can contain several English words.**

### Original reconstruction — blocks 01–17

| Block | Proposed reading |
| :---: | :--- |
| 01 | [AS I GO, THE](./plaintext-i-found/01-as-i-go-the.md) |
| 02 | [WEATHER](./plaintext-i-found/02-weather.md) |
| 03 | [TURNS](./plaintext-i-found/03-turns.md) |
| 04 | [COLD](./plaintext-i-found/04-cold.md) |
| 05 | [I MAY](./plaintext-i-found/05-i-may.md) |
| 06 | [CRY](./plaintext-i-found/06-cry.md) |
| 07 | [NOW THE](./plaintext-i-found/07-now-the.md) |
| 08 | [IDEA](./plaintext-i-found/08-idea.md) |
| 09 | [OF](./plaintext-i-found/09-of.md) |
| 10 | [THE](./plaintext-i-found/10-the.md) |
| 11 | [END](./plaintext-i-found/11-end.md) |
| 12 | [IS](./plaintext-i-found/12-is.md) |
| 13 | [DEATH](./plaintext-i-found/13-death.md) |
| 14 | [SEE](./plaintext-i-found/14-see.md) |
| 15 | [YOU](./plaintext-i-found/15-YOU.md) |
| 16 | [SOON](./plaintext-i-found/16-soon.md) |
| 17 | [THEN](./plaintext-i-found/17-then.md) |

### Candidate continuation — blocks 18–34

| Block | Proposed reading |
| :---: | :--- |
| 18 | [THE](./plaintext-i-found/18-the.md) |
| 19 | [KEY](./plaintext-i-found/19-key.md) |
| 20 | [IS](./plaintext-i-found/20-is.md) |
| 21 | [TO](./plaintext-i-found/21-to.md) |
| 22 | [GO](./plaintext-i-found/22-go.md) |
| 23 | [TO](./plaintext-i-found/23-to.md) |
| 24 | [THE](./plaintext-i-found/24-the.md) |
| 25 | [EAST](./plaintext-i-found/25-east.md) |
| 26 | [OF](./plaintext-i-found/26-of.md) |
| 27 | [THE](./plaintext-i-found/27-the.md) |
| 28 | [MAP LIFE](./plaintext-i-found/28-map.md) |
| 29 | [MAY](./plaintext-i-found/29-may.md) |
| 30 | [BE](./plaintext-i-found/30-be.md) |
| 31 | [THE](./plaintext-i-found/31-the.md) |
| 32 | [DEATH](./plaintext-i-found/32-death.md) |
| 33 | [OF](./plaintext-i-found/33-of.md) |
| 34 | [YOU](./plaintext-i-found/34-you.md) |

## Structural evidence and the red heading

The **[Strongest Plaintext Evidence](./Start-reading-here/strongest-plaintext-evidence.md)** report examines relationships between the selected reading, its ciphertext, the matrix, and LP1. Examples include:

| Observation | Recorded relationship |
| :--- | :--- |
| Two seven-word passages | The rune-index sums of `AS I GO, THE WEATHER TURNS COLD` and `THE IDEA OF THE END IS DEATH` are **233** and **232**; `φ(233) = 232`. |
| Ciphertext total through `THEN` | Counting every ciphertext-cell use on the main `SOON` route gives a GP total of **3274**; `3274 + 27 = 3301`. |
| Return to the opening cell through `GO` | The cumulative plaintext-index sum is **860**; `φ(860) = 336`, the absolute position of **`J(13,12)`**. |

A separate **[red-heading analysis](./Start-reading-here/red-heading-SEQUENDI-RATIO.md)** documents the literal output **`SECUENDI RATIO`**, interpreted as Latin **`SEQUENDI RATIO`** — “a method of following” — with the C/K rune read as Q.

## Conventions

| Notation | Meaning |
| :--- | :--- |
| `(row, column)` | One-based coordinates; rows increase downward, columns to the right. |
| Rune index | A value from **0 to 28**, used in subtraction modulo 29. |
| `TH`, `EA`, and other multi-letter labels | Each label represents one rune. |
| `φ(n)` | Euler’s totient: the number of integers from 1 to `n` coprime to `n`. |
| `μ(n)` | Möbius function: zero when a prime square divides `n`; otherwise +1 or −1 according to the parity of its distinct prime-factor count. `μ(1) = +1`. |
| `GP` | Gematria Primus **prime values**, distinct from rune indices: indices 0–28 correspond to primes 2–109. |
| Absolute position | Row-major cell number, `n₀(r,c) = 27(r−1) + c`, from **1 to 729**. |
| Rotation | Clockwise matrix rotation used to calculate cell indices; distinct from cyclic rotation of a three-rune key. |
