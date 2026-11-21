# Python Decoder

I built a Python decoder that uses my decryption method to recover the hidden text in pages 0–2 of *Liber Primus* (LP2). The default search starts with the 27×27 rune matrix and the bundled English frequency dictionary. It takes no reference plaintext, preset route, starting coordinates, preselected keys, block boundaries, or target block count. It finds the openings by scanning the grid, uses the rules in Reports 00–27 to test possible moves, and ranks the resulting plaintext candidates by English word frequency.

> [!IMPORTANT]
> [Download the decoder ZIP](./liber_primus_decoder.zip)

Extract the archive and run the commands from the folder containing `decode.py` and `matrix.txt`.

### Default run

```bash
python3 decode.py matrix.txt
```

The default run shows the five highest-ranked readings from the longest completed routes.

### Best reading at a specific length

```bash
python3 decode.py matrix.txt --blocks 38 --top 1
```

This shows the highest-ranked reading among routes that end at exactly 38 blocks. Change `38` to the block count you want to check.

### Best readings at every depth

```bash
python3 decode.py matrix.txt --by-depth
```

This shows up to three best readings at each depth, from block 1 through the deepest block reached. On the included matrix, it covers all 39 depths. Each ranking includes every valid reading that reaches that depth, whether the route ends there or has more moves to explore. For example, the ranking at depth 13 scores the first 13 blocks of every route that reaches that point.

Use `--top` to change the number of readings per depth:

```bash
python3 decode.py matrix.txt --by-depth --top 5
```

### Trace the highest-ranked reading

```bash
python3 decode.py matrix.txt --top 1 --trace
```

This shows how each block of the highest-ranked reading was decrypted, including the ciphertext cells, the aligned key, and the resulting runes.

### Show the full ranking

```bash
python3 decode.py matrix.txt --top 192
```

This shows all 192 ranked readings from the two 39-block routes on the included matrix.

> [!IMPORTANT]
> [Full ranking of all 192 readings](./Start-reading-here/liber_primus_192_ranked_readings.md)

I wanted the opening search to be transparent. On the original 27×27 matrix, the decoder finds 87,115 admissible starting states. Even with that much larger search space, my 39-block plaintext ending in DIE still ranks first.

The decoder infers the height and width from the input and uses them to calculate coordinates, rotations, and grid-dependent bounds. I kept the numerical thresholds of 7 and 13 from the reports because they may also apply to LP2 pages 3 onward. That still needs to be tested. The default run took about two minutes in testing.

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

### DIE

After `DIE`, the route rules allow no further move. The first cell of the opening key is at map position **335**. Its reflection across the main diagonal contains `T`, rune index **16**. Their product, **335 × 16 = 5,360**, equals the GP sum of the proposed DIE reading. `DIE` supplies the final **187**, bringing the total from **5,173** to **5,360**.

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

| Report | |
| :---: | :--- |
| [00](./Start-reading-here/00-decryption-method.md) | Decryption method |
| [01](./Start-reading-here/01-next-key-signature.md) | Next-key signature |
| [02](./Start-reading-here/02-leftmost-cell-and-rotations.md) | Leftmost cell and rotations |
| [03](./Start-reading-here/03-predicting-axis-and-reading-direction.md) | Axis and reading direction |
| [04](./Start-reading-here/04-predicting-next-key-center-parity.md) | Key-center parity |
| [05](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md) | Ciphertext row parity |
| [06](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) | Ray alignment |
| [07](./Start-reading-here/07-predicting-next-key-mirror-status.md) | Mirror status |
| [08](./Start-reading-here/08-minimum-ciphertext-block-length.md) | Minimum block length |
| [09](./Start-reading-here/09-predicting-next-ciphertext-column-parity.md) | Ciphertext column parity |
| [10](./Start-reading-here/10-squarefree-gcd-compatibility.md) | Squarefree-GCD compatibility |
| [11](./Start-reading-here/11-seven-thresholds-and-cyclic-phase-modes.md) | Seven-phase thresholds and cyclic modes |
| [12](./Start-reading-here/12-predicting-exact-ray-deviation.md) | Deterministic ray deviation using Möbius zeroes |
| [13](./Start-reading-here/13-predicting-next-key-axis-group.md) | Axis-group prediction using Möbius signs |
| [14](./Start-reading-here/14-predicting-exact-next-key-axis.md) | Exact next key-axis prediction using Möbius signs and GP weights |
| [15](./Start-reading-here/15-predicting-next-key-radius-parity.md) | Next key-node radius parity prediction using Möbius signs |
| [16](./Start-reading-here/16-whole-word-block-boundaries.md) | Whole-word block boundaries |
| [17](./Start-reading-here/17-xor-next-key-center-column.md) | XOR filter for the next key-center column |
| [18](./Start-reading-here/18-predicting-next-ciphertext-start-and-end.md) | Next ciphertext start and end |
| [19](./Start-reading-here/19-predicting-next-ciphertext-start-distance.md) | Predicting the next ciphertext start with two distances |
| [20](./Start-reading-here/20-two-orientation-gcd-filter.md) | Two-orientation GCD filter for the next key center |
| [21](./Start-reading-here/21-conditional-seven-step-bound.md) | Conditional seven-step bound on key radius and ciphertext span |
| [22](./Start-reading-here/22-seven-step-key-cell-coverage.md) | Seven-step coverage by a single key cell |
| [23](./Start-reading-here/23-mobius-forecast-for-next-key-extreme.md) | Möbius forecast for the next key extreme |
| [24](./Start-reading-here/24-mod-seven-key-center-ciphertext-alignment.md) | Modulo-seven key-center and ciphertext alignment |
| [25](./Start-reading-here/25-reflected-start-cell-seven-step-bound.md) | Reflected start-cell seven-step bound |
| [26](./Start-reading-here/26-mod-seven-next-key-center-start-distance.md) | Next key-center distance modulo seven |
| [27](./Start-reading-here/27-key-alignment-from-node-geometry.md) | Key alignment from node geometry |

## Plaintext walkthroughs

Each walkthrough identifies the source node, key, phase, ciphertext cells, and resulting runes. The numbering follows the interactive map. A block can contain several English words.

| Block | |
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
| 39 | [DIE](./plaintext-i-found/39-DIE.md) |

## Structural evidence and the red heading

> [!IMPORTANT]
> The [Strongest Plaintext Evidence](./Start-reading-here/strongest-plaintext-evidence.md) report examines relationships between the selected reading, its ciphertext, the matrix, and LP1.

A separate [red-heading analysis](./Start-reading-here/red-heading-SEQUENDI-RATIO.md) documents the literal output SECUENDI RATIO, interpreted as Latin SEQUENDI RATIO — “a method of following” — with the C/K rune read as Q.

## Interactive Map

I created this [interactive 27 × 27 map](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/) to visualize the ciphertext blocks, key nodes, and proposed plaintext directly on the matrix.

## New Strongest Findings

Leading AI models helped uncover [new patterns](./New-strongest-findings/) in the 27×27 grid and its decoding route during a closer look at my original discovery.
