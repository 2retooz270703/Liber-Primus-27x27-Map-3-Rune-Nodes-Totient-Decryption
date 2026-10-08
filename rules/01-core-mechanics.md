# 01 — Core Mechanics

The reconstruction uses three connected ideas: a **27×27 rune matrix**, **three-rune key structures**, and **modular subtraction**. This chapter explains the basic arithmetic. The following rules describe how a key's phase is chosen and how the route moves between structures.

## 1. Arrange the runes into a 27×27 matrix

Pages 0–2 of *Liber Primus* contain **729 rune positions**. Since **729 = 27 × 27**, the rune sequence can be arranged into a square matrix, filling each row from left to right before continuing to the next.

Every rune now has a fixed position. For example, **J(13,12)** means the rune `J` in row 13, column 12. The first cell is `(1,1)`.

This arrangement lets us examine more than the original reading order. The route also uses the distances between cells and the patterns formed by runes along rows, columns, and diagonals. These patterns are important because many of the keys come from three-rune structures in the matrix.

## 2. Assign numerical values to the runes

Calculations use the **Gematria Primus rune indices**, numbered from **0 to 28**. Some examples are:

| Rune | Index |
|---|---:|
| `U` | 1 |
| `TH` | 2 |
| `I` | 10 |
| `J` | 11 |
| `NG` | 21 |
| `EA` | 28 |

**One rune is not always one Latin letter.** For example, `TH`, `AE`, `EA`, `OE`, `EO`, and `NG` each represent a single rune. This matters when counting ciphertext positions, repeating keys, or interpreting a decrypted word.

Throughout the reconstruction, these indices are used for key calculations and decryption. They are different from the prime-number values sometimes examined as additional numerical connections.

## 3. Identify three-rune structures

A basic structure consists of three runes, with the middle rune acting as the **center**:

```text
outer — center — outer
```

A **mirror** has the same rune on both sides. Examples from the recovered stages include `X-OE-X`, `H-TH-H`, and `OE-J-OE`. The outer runes can be separated from the center by more than one cell, as long as both sides have the same distance.

The system also uses **non-mirrored structures**, such as `H-NG-C` in [`03-TURNS.md`](../plaintext-i-found/03-TURNS.md). Unlike the symmetric examples, that key is used directly after the relevant cells are located.

Three-rune structures matter because they can supply keys, connect one part of the matrix to another, and produce numerical signatures that can be compared across different locations.

## 4. Generate a key with Euler's totient function

For a selected three-rune structure, the usual key-generation step transforms **only the center** using Euler's totient function, written as `φ`. This function counts the positive integers up to a number that are coprime to it.

The two outer runes stay unchanged. The transformed center is then replaced by the rune with the corresponding index:

```text
A-B-C  →  A-φ(B)-C
```

For example, the first stage uses `AE-J-EA`. Because `J = 11` and `φ(11) = 10 = I`, its center changes from `J` to `I`:

```text
AE-J-EA → AE-I-EA
```

The same operation appears in [`04-COLD.md`](../plaintext-i-found/04-COLD.md):

```text
TH = 2
φ(2) = 1 = U

H-TH-H → H-U-H
```

In both examples, the key is obtained from a visible structure in the matrix rather than assembled one rune at a time from the desired plaintext.

## 5. Calculate the key's totient signature

Once the three-rune key is formed, apply `φ` **separately to all three rune values**. The result is the key's **totient signature**.

For `H-U-H`, the calculation is:

```text
φ(H = 8) = 4
φ(U = 1) = 1
φ(H = 8) = 4

Totient signature: (4,1,4)
```

The distinction is important: **generating the key** transforms its center, while **calculating the signature** transforms all three positions.

The signature is then used by other rules to determine the key's Möbius phase, compare structures, and examine movement or inherited values. The phase calculation is explained in [`02-key-phase-selection.md`](./02-key-phase-selection.md).

## 6. Rotate and repeat the key

The base key contains three runes, but the ciphertext may be longer. Before repeating the key, the **Möbius phase** determines where its cycle starts.

For example, `H-U-H` has signature `(4,1,4)`, which gives **phase 1** under the phase-selection rule. The active order becomes:

```text
Base key:   H-U-H
Phase 1:    U-H-H
```

If the ciphertext contains four runes, repeat the active key from the beginning:

```text
U-H-H-U
```

Another example is the first stage, where **phase 0** leaves `AE-I-EA` unchanged. To cover seven ciphertext runes, it repeats as:

```text
AE-I-EA-AE-I-EA-AE
```

The phase controls the **starting order** of the key; repetition simply extends that order to the required length.

## 7. Decrypt by subtracting modulo 29

After identifying the ciphertext and active key, subtract each key index from the corresponding ciphertext index:

```text
Plaintext = (Ciphertext − Key) mod 29
```

**Modulo 29** keeps every result in the rune-index range `0–28`. If subtraction is negative, add `29` until the result is in that range.

The first rune of [`01-AS-I-GO-THE.md`](../plaintext-i-found/01-AS-I-GO-THE.md) gives a simple example:

```text
Ciphertext: L  = 20
Key:        AE = 25

20 − 25 = −5
−5 + 29 = 24 = A
```

The same operation works across an entire word. For example, the `THEN` stage uses three ciphertext runes and the key generated from `IA-IA-IA`:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `L = 20` | `E = 18` | `20 − 18 = 2` | **TH** |
| `T = 16` | `IA = 27` | `16 − 27 ≡ 18` | **E** |
| `W = 7` | `IA = 27` | `7 − 27 ≡ 9` | **N** |

The output is **TH-E-N**, or **THEN**. Although the word has four Latin letters, it is represented by three runes. See [`16-THEN.md`](../plaintext-i-found/16-THEN.md) for the complete geometry and key calculation.

## 8. How these mechanics fit together

The arithmetic stays consistent across the stages: **a matrix structure supplies a key, the totient signature is calculated, the Möbius rule fixes the active rotation, and modular subtraction converts ciphertext runes into plaintext**.

The remaining question in each stage is *which* structure or ciphertext segment to use next. That is where the other rules come in: [`02-key-phase-selection.md`](./02-key-phase-selection.md) explains rotation; [`03-totient-movement.md`](./03-totient-movement.md) and [`04-coordinate-selector.md`](./04-coordinate-selector.md) explain movement; and the later rules cover center/outer roles and retained values.
