# Experimental Python Decoder

I’ve added a runnable Python decoder for *Liber Primus* (LP2, pages 0–2). It takes a 27×27 rune matrix, explores the block transitions allowed by Reports 00–27, and ranks candidate readings by English word frequency. The search runs without a supplied plaintext or a preset block count.

On the included matrix, the two longest completed routes each contain 39 blocks and 118 runes. They share their first 38 blocks and end in **DIE** and **WINGING**, respectively. Each route yields 96 candidate readings, for a total of 192. The highest-ranked reading matches the proposed plaintext below and ends with **DIE**. The highest-ranked reading ending in **WINGING** places fourth overall.

> [!IMPORTANT]
> [Download the decoder ZIP](./liber_primus_decoder.zip)

Extract the archive and run the decoder from the folder containing `decode.py`.

```bash
python3 decode.py matrix.txt
```

Add `--top 1 --trace` to show only the highest-ranked reading and trace how each block was decrypted.

```bash
python3 decode.py matrix.txt --top 1 --trace
```

Use `--top 192` to show the complete ranking on the included matrix. [Full ranking of all 192 readings](./Start-reading-here/liber_primus_192_ranked_readings.md)

# Plaintext

## Pages 0-2


> [!IMPORTANT]
> **Red runes: Secuendi Ratio ("The Way to Proceed")**
>
> As I go, the weather turns cold.  
I may cry now.  
>
> The idea of the end is death.  
See you soon, then.  
The key is to go to the east of the map.  
>
> Life may be the death of you.  
Go, do as I ask.
>
> Die.

### Closing the Route

The two terminal routes share **Block 38 — I ASK**, reached on transition 37.

Its key-source node is the exact reflection of the opening key-source node across the main diagonal, under `(r, c) → (c, r)`.

| Opening node · Block 1 | Reflected node · Block 38 |
| --- | --- |
| `(13,11) → (13,12) → (13,13)` | `(11,13) → (12,13) → (13,13)` |

The two nodes share **`(13,13)`**, which stays fixed under the reflection.

### DIE

After `DIE`, the route rules allow no further move. The first cell of the opening key is at map position **335**. Its reflection across the main diagonal contains `T`, rune index **16**. Their product, **335 × 16 = 5,360**, equals the GP sum of the proposed DIE reading. `DIE` supplies the final **187**, bringing the total from **5,173** to **5,360**. On the other terminal branch, `WINGING` contributes **177**, giving **5,350**. [Terminal-route replay](./Start-reading-here/27-key-alignment-from-node-geometry.md)

# Welcome

This project arranges the pages’ 729 runes into a single 27 × 27 matrix and investigates how its geometry connects ciphertext, key material, and reading order. The proposed method combines *three-rune key nodes*, *Euler’s totient function*, *Möbius signatures*, and *repeating-key subtraction modulo 29*.

For a first pass, read [Report 00](./Start-reading-here/00-decryption-method.md), follow the [opening block](./plaintext-i-found/01-as-i-go-the.md), and compare its coordinates with the [interactive map](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/).


> [!IMPORTANT]
> [Strongest Plaintext Evidence](./Start-reading-here/strongest-plaintext-evidence.md)


## How the method works

### 1. Identify a three-rune node

A key node consists of three equally spaced cells on a horizontal, vertical, or 45° diagonal line. Nodes may be *mirror* structures with equal outer runes, or *non-mirror* structures with different outer runes.

### 2. Derive the key

For a node using the center transformation, keep its outer rune indices and replace its center index with Euler’s totient:

$$
(a,b,c)\longmapsto\bigl(a,\varphi(b),c\bigr).
$$

Some documented nodes use their original indices directly. Each walkthrough specifies which operation is used.

### 3. Calculate the key phase

For the derived key in its unrotated order, calculate its Möbius signature and phase:

$$
\sigma_i=\mu\\left(\varphi(k_i)\right),
\qquad
p=(\sigma_1+\sigma_2+\sigma_3)\bmod3.
$$

Rotate the three-rune key *left by `p` positions*.

### 4. Decrypt the selected ciphertext

Repeat the aligned key across the block and subtract rune indices:

$$
P_i=(C_i-K_i)\bmod29.
$$

### 5. Evaluate the next transition

The transition reports use the current block’s geometry and key data to predict or filter properties of the next block: signature, reading axis, direction, coordinate parity, alignment, and node type. These constraints narrow the search; selecting an exact next location remains an open problem.

### Worked example: WEATHER

The node `X–OE–X`, at row 14, columns 4–6, becomes `X–I–X` because `φ(22) = 10`. Its signature is `(+1, 0, +1)`, giving phase 2 and the aligned key `X–X–I`.

Read row 14, columns 14–18:

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (14,14) | NG = 21 | X = 14 | 21 − 14 ≡ 7 | **W** |
| (14,15) | P = 13 | X = 14 | 13 − 14 ≡ 28 | **EA** |
| (14,16) | EO = 12 | I = 10 | 12 − 10 ≡ 2 | **TH** |
| (14,17) | O = 3 | X = 14 | 3 − 14 ≡ 18 | **E** |
| (14,18) | E = 18 | X = 14 | 18 − 14 ≡ 4 | **R** |

The result is WEATHER. `EA` and `TH` each represent one rune. See the [complete calculation](./plaintext-i-found/02-weather.md) for the node, movement, coordinates, and subtraction table.

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
| [11](./Start-reading-here/11-seven-thresholds-and-cyclic-phase-modes.md) | Seven-phase thresholds and cyclic modes | Tests exact hits at multiples of seven and proposes a repeating four-mode cycle every 28 phase units. |
| [12](./Start-reading-here/12-predicting-exact-ray-deviation.md) | Deterministic ray deviation using Möbius zeroes | Introduces a new rule that determines the exact 0-or-1 offset from geometric rays using rotated cell indices. |
| [13](./Start-reading-here/13-predicting-next-key-axis-group.md) | Axis-group prediction using Möbius signs | Introduces a new rule that determines the next key node's axis group using rotated cell indices and Möbius signs. |
| [14](./Start-reading-here/14-predicting-exact-next-key-axis.md) | Exact next key-axis prediction using Möbius signs and GP weights | Extends Report 13 with a new diagonal bit derived from rotated cell indices, Möbius signs, and original rune prime weights, predicting the exact axis of the next key node. |
| [15](./Start-reading-here/15-predicting-next-key-radius-parity.md) | Next key-node radius parity prediction using Möbius signs | Introduces a new XOR-based rule combining coordinate parity and Möbius sign tests to predict whether the next key node's radius is even or odd. |
| [16](./Start-reading-here/16-whole-word-block-boundaries.md) | Whole-word block boundaries | Requires each independently decrypted block to contain one or more complete English words and rejects readings that split a word across blocks. |
| [17](./Start-reading-here/17-xor-next-key-center-column.md) | XOR filter for the next key-center column | Uses the rotated index of the current key center and the Möbius function to filter candidate columns. |
| [18](./Start-reading-here/18-predicting-next-ciphertext-start-and-end.md) | Next ciphertext start and end | Tests three XOR rules that narrow the possible starts and ends of the next ciphertext segment. |
| [19](./Start-reading-here/19-predicting-next-ciphertext-start-distance.md) | Predicting the next ciphertext start with two distances | Predicts whether the next ciphertext starts within seven cells of both the current start and leftmost cell, or farther than seven cells from both. |
| [20](./Start-reading-here/20-two-orientation-gcd-filter.md) | Two-orientation GCD filter for the next key center | Requires both GCDs between the next ciphertext start index and the next key center indices at 0° and 180° to be at most seven. |
| [21](./Start-reading-here/21-conditional-seven-step-bound.md) | Conditional seven-step bound on key radius and ciphertext span | Caps the sum of the next key radius and ciphertext span at seven when the current key node’s upper extreme (left for horizontal nodes) is within seven grid steps of the current ciphertext end. |
| [22](./Start-reading-here/22-seven-step-key-cell-coverage.md) | Seven-step coverage by a single key cell | If any cell of the next ciphertext is within seven columns of its key center, the same original key-node cell must be within seven grid steps of both the first and the leftmost ciphertext cells. |
| [23](./Start-reading-here/23-mobius-forecast-for-next-key-extreme.md) | Möbius forecast for the next key extreme | Uses two tests on rotated indices of the current block to predict whether the 180° index of the next key node’s upper extreme (left for horizontal nodes) has positive Möbius value. |
| [24](./Start-reading-here/24-mod-seven-key-center-ciphertext-alignment.md) | Modulo-seven key-center and ciphertext alignment | Uses two arithmetic tests on the current block to predict the modulo-seven relation between the next key center and ciphertext. |
| [25](./Start-reading-here/25-reflected-start-cell-seven-step-bound.md) | Reflected start-cell seven-step bound | Limits the next ciphertext start using rotated coordinates of the current key and ciphertext. |
| [26](./Start-reading-here/26-mod-seven-next-key-center-start-distance.md) | Next key-center distance modulo seven | Uses the current block’s geometry to predict whether the Chebyshev distance between the next key center and ciphertext start is divisible by seven. |
| [27 ✅](./Start-reading-here/27-key-alignment-from-node-geometry.md) | Key alignment from node geometry | Uses the current node and ciphertext start to test the next aligned key against the final ciphertext rune using a modulo-three check and a seven-index distance threshold. |

## Plaintext walkthroughs

Each walkthrough identifies the source node, key, phase, ciphertext cells, and resulting runes. The numbering follows the interactive map. A block can contain several English words.

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
| 28 | [MAP LIFE](./plaintext-i-found/28-map-life.md) |
| 29 | [MAY](./plaintext-i-found/29-may.md) |
| 30 | [BE](./plaintext-i-found/30-be.md) |
| 31 | [THE](./plaintext-i-found/31-the.md) |
| 32 | [DEATH](./plaintext-i-found/32-death.md) |
| 33 | [OF](./plaintext-i-found/33-of.md) |
| 34 | [YOU](./plaintext-i-found/34-you.md) |
| 35 | [GO](./plaintext-i-found/35-go.md) |
| 36 | [DO](./plaintext-i-found/36-do.md) |
| 37 | [AS](./plaintext-i-found/37-as.md) |
| 38 | [I ASK](./plaintext-i-found/38-i-ask.md) |
| 39 ✅ | [DIE](./plaintext-i-found/39-DIE.md) |

## Structural evidence and the red heading

> [!IMPORTANT]
> The [Strongest Plaintext Evidence](./Start-reading-here/strongest-plaintext-evidence.md) report examines relationships between the selected reading, its ciphertext, the matrix, and LP1.

A separate [red-heading analysis](./Start-reading-here/red-heading-SEQUENDI-RATIO.md) documents the literal output SECUENDI RATIO, interpreted as Latin SEQUENDI RATIO — “a method of following” — with the C/K rune read as Q.

## Conventions

| Notation | Meaning |
| :--- | :--- |
| `(row, column)` | One-based coordinates; rows increase downward, columns to the right. |
| Rune index | A value from 0 to 28, used in subtraction modulo 29. |
| `TH`, `EA`, and other multi-letter labels | Each label represents one rune. |
| `φ(n)` | Euler’s totient: the number of integers from 1 to `n` coprime to `n`. |
| `μ(n)` | Möbius function: zero when a prime square divides `n`; otherwise +1 or −1 according to the parity of its distinct prime-factor count. `μ(1) = +1`. |
| `GP` | Gematria Primus prime values, distinct from rune indices: indices 0–28 correspond to primes 2–109. |
| Absolute position | Row-major cell number, `n₀(r,c) = 27(r−1) + c`, from 1 to 729. |
| Rotation | Clockwise matrix rotation used to calculate cell indices; distinct from cyclic rotation of a three-rune key. |

## Interactive Map

I created this [interactive 27 × 27 map](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/) to visualize the ciphertext blocks, key nodes, and proposed plaintext directly on the matrix.

## New Strongest Findings

[new-strongest-findings/](./New-strongest-findings/)

## Commands

| Task | Command |
| --- | --- |
| Show all available options | `python3 decode.py --help` |
| Run the default search | `python3 decode.py matrix.txt` |
| Show the top reading and trace every block | `python3 decode.py matrix.txt --top 1 --trace` |
| Show all 192 readings at the greatest completed depth on the bundled matrix | `python3 decode.py matrix.txt --top 192` |
| Keep only geometrically complete routes of exactly 39 blocks | `python3 decode.py matrix.txt --blocks 39` |
| Compare completed routes of every length | `python3 decode.py matrix.txt --all-lengths` |
| Raise the search depth limit from 128 to 256 blocks | `python3 decode.py matrix.txt --max-depth 256` |

Exit code `0` means the search completed with a result, `2` means invalid arguments or an input error, `3` means the search completed with no qualifying reading, and `4` means the search hit its depth limit with active branches remaining.
