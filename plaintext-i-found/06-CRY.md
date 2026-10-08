# 06 — CRY

AS I GO, THE WEATHER TURNS COLD. I MAY CRY.

## 1. Continue from the end of I MAY

The previous chapter, [`05-I-MAY.md`](./05-I-MAY.md), ends at **E(26,16)**. This cell is the lower outer rune of a vertical mirror:

```text
E(24,16)
   |
X(25,16)  ← center
   |
E(26,16)  ← end of I MAY
```

The mirror is **E-X-E**. Its center, `X(25,16)`, provides the new key through the same Euler-totient transformation used in earlier stages:

```text
X = 14
φ(14) = 6 = G

E-X-E → E-G-E
```

The key therefore begins with **E-G-E**. Its transformed center also introduces the value **6**, which will connect the key calculation to the next movement through the matrix.

## 2. Calculate the active key

Apply Euler's totient to the three runes of `E-G-E`, then use their Möbius values to determine the rotation:

```text
φ(E=18) = 6 → μ(6) = +1
φ(G=6)  = 2 → μ(2) = -1
φ(E=18) = 6 → μ(6) = +1

Totient signature: (6,2,6)
Möbius signature: (+1,-1,+1)
Phase:              (1-1+1) mod 3 = 1
```

**Phase 1** rotates the key once, placing `G` first:

```text
E-G-E → phase 1 → G-E-E

Active key: G-E-E
```

Notice that **6** appears at both ends of the totient signature. This same number is used to locate the ciphertext.

## 3. The value 6 leads to a new mirror

Return to **X(25,16)**, the center of the original `E-X-E` mirror. Moving **six cells upward** reaches **J(19,16)**:

```text
X(25,16) → UP 6 → J(19,16)
```

The landing point is also the center of another exact vertical mirror:

```text
OE(18,16)
    |
 J(19,16)  ← center
    |
OE(20,16)
```

This is **OE-J-OE**. The movement connects two key pieces of the geometry: the center `X` that produced **6**, and the center `J` reached by moving exactly that distance.

The `OE-J-OE` mirror is also important in the next chapter, where it generates the key for `NOW THE`.

## 4. Read and decrypt the ciphertext

Starting at **J(19,16)**, read upward through the two adjacent runes:

```text
J(19,16) → OE(18,16) → S(17,16)
```

This gives **ciphertext `J-OE-S`**. Subtract the active key `G-E-E`, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `J = 11` | `G = 6` | `11 − 6 = 5` | **C** |
| `OE = 22` | `E = 18` | `22 − 18 = 4` | **R** |
| `S = 15` | `E = 18` | `15 − 18 ≡ 26` | **Y** |

```text
Ciphertext: J - OE - S
Key:        G - E  - E
Plaintext:  C - R  - Y
```

The result is **CRY**. Its final ciphertext rune is **S(17,16)**, which provides the starting point for the following stage.

## 5. The same 6 appears again after CRY

The endpoint **S(17,16)** is the right outer of a horizontal mirror with radius **6**:

```text
S(17,4) ── 6 ── IA(17,10) ── 6 ── S(17,16)
```

Its center is `IA(17,10)`. Applying Euler's totient twice to that center gives the same value:

```text
IA = 27
φ(27) = 18
φ(18) = 6

φ²(IA) = 6
```

The same `IA` also sits at the center of a diagonal mirror, again with radius **6**:

```text
TH(11,16) ── 6 ── IA(17,10) ── 6 ── TH(23,4)
```

One of its outer runes, **TH(11,16)**, lies exactly six cells above the final `S`:

```text
S(17,16) → UP 6 → TH(11,16)
```

So the value **6** connects the two stages in several concrete ways: it appears in the `CRY` key signature, determines the earlier **UP 6** movement, equals the radii of both mirrors around `IA`, and is also obtained from **φ²(IA)**. The same movement distance now points to the beginning of the next ciphertext.

## 6. The state passed to NOW THE

The key for `CRY` came from `E-G-E`, with Möbius signature **`(+1,-1,+1)`** and **phase 1**. The route model associates this signature with a reflection or outer-node continuation.

At the final **S(17,16)**, the phase-1 coordinate selector is:

```text
φ(17) = 16 → μ(16) = 0
φ(16) =  8 → μ(8)  = 0

V₁(17,16) = (0,0)
```

Since this selector gives no direction, the connected radius-6 mirrors provide the geometric continuation. They lead to **TH(11,16)**, where the next chapter, [`07-NOW-THE.md`](./07-NOW-THE.md), begins its ciphertext.
