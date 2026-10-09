# 02 — WEATHER

AS I GO, THE WEATHER

## 1. Continue from the end of AS I GO, THE

The previous chapter, [`01-AS-I-GO-THE.md`](./01-AS-I-GO-THE.md), ends at **X(14,4)**. This rune is also the left outer of a small horizontal mirror:

```text
X(14,4) — OE(14,5) — X(14,6)
```

The mirror **X-OE-X** provides the key for the next stage. As in the previous chapter, we apply Euler's totient to the center while keeping the two outer runes unchanged:

```text
OE = 22
φ(22) = 10 = I

X-OE-X → X-I-X
```

The transformation ```φ(22) = 10 = I``` also produces the number **10**, which has a second role: it determines how far the route moves from the previous endpoint.

## 2. The same number leads to the center of the grid

Starting at **X(14,4)**, move **RIGHT 10** along row 14:

```text
X(14,4) → RIGHT 10 → NG(14,14)
```

The destination **NG(14,14)** is the exact center of the 27×27 matrix. The connection is particularly clear: the value obtained from the mirror's center, **φ(OE) = 10**, is used both to generate **I** in the key and to reach the center of the entire grid.

From this central cell, the next ciphertext is read along the same row.

## 3. Calculate the key's Möbius phase

We already have **X-I-X**. To determine its rotation, first calculate Euler's totient for each rune:

```text
φ(X=14) = 6
φ(I=10) = 4
φ(X=14) = 6

Totient signature: (6,4,6)
```

Now apply the Möbius function to that signature:

```text
μ(6) = +1
μ(4) =  0
μ(6) = +1

Möbius signature: (+1,0,+1)
Phase:              (1+0+1) mod 3 = 2
```

**Phase 2** rotates the key structure to **X-X-I**. The ciphertext contains five runes, so the three-rune key repeats from the beginning:

```text
X-I-X → phase 2 → X-X-I

Active key: X-X-I-X-X
```

The key is now determined by the mirror and its calculated phase.

## 4. Read the ciphertext and decrypt WEATHER

Return to **NG(14,14)**, the grid center reached by **RIGHT 10**. Reading five consecutive runes to the right gives:

```text
NG(14,14) → P(14,15) → EO(14,16) → O(14,17) → E(14,18)
```

This is **ciphertext `NG-P-EO-O-E`**. Subtract the active key `X-X-I-X-X`, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `NG = 21` | `X = 14` | `21 − 14 = 7` | **W** |
| `P = 13` | `X = 14` | `13 − 14 ≡ 28` | **EA** |
| `EO = 12` | `I = 10` | `12 − 10 = 2` | **TH** |
| `O = 3` | `X = 14` | `3 − 14 ≡ 18` | **E** |
| `E = 18` | `X = 14` | `18 − 14 = 4` | **R** |

```text
Ciphertext: NG - P  - EO - O - E
Key:        X  - X  - I  - X - X
Plaintext:  W  - EA - TH - E - R
```

The result is **WEATHER**. Although it has seven Latin letters, it consists of five runes because **EA** and **TH** are single runes in Gematria Primus.

## 5. Additional connections around the grid center

There are two useful relationships alongside the decryption.

First, the key-generating centers in the opening chapters reduce to the same rune:

```text
J  = 11 → φ(11) = 10 = I
OE = 22 → φ(22) = 10 = I
```

So both center transformations produce **I**, even though their original rune values differ.

Second, the grid contains a striking alignment directly above the beginning of this ciphertext:

```text
Plaintext runes: W - EA - TH
Ciphertext:      NG - P - EO
```

These are adjacent rows of the matrix. The alignment is an additional geometric connection; the modular subtraction above is what actually recovers the word.

## 6. The endpoint belongs to a unique E-NG-E mirror

`WEATHER` ends at **E(14,18)**. That cell is also an outer rune of a larger diagonal mirror:

```text
E(6,10) —4 diagonal steps— NG(10,14) —4 diagonal steps— E(14,18)
```

The equal distances form **E-NG-E**, with **NG(10,14)** at its center. This is the only mirror of that exact rune pattern found in the grid when checking horizontal, vertical, and diagonal axes at all integer radii.

There is also a numerical connection to the key state. The **X-I-X** structure used to decrypt `WEATHER` has:

```text
Totient signature: (6,4,6)
Möbius signature: (+1,0,+1)
```

In the project's **CENTER / OUTER** interpretation, **(+1,0,+1)** corresponds to an **OUTER** continuation. The final cell **E(14,18)** is indeed the outer rune of the `E-NG-E` mirror.

This repeats the geometric relationship also seen in later chapters: the key's Möbius state matches the role of the endpoint in the next mirror structure.

## 7. The next cell leads to TURNS

Immediately to the right of the final **E(14,18)** lies **A(14,19)**. This cell becomes the crossroads used in the next stage.

We carry forward the two related values already produced by the key:

```text
I = 10
φ(I) = 4
```

With **phase 2**, the coordinate selector at `A(14,19)` gives:

```text
V₂(14,19) = (-1,+1) → UP + RIGHT
```

The directions **UP** and **RIGHT**, together with the inherited distances **10** and **4**, locate the next key structure and ciphertext. This continuation produces **TURNS**, explained in [`03-TURNS.md`](./03-TURNS.md).
