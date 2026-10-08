# 10 — END

AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END

## 1. The end of OF THE reveals a radius-4 mirror

The previous chapter, [`09-OF-THE.md`](./09-OF-THE.md), finishes at **J(19,16)**. Immediately to its left is **F(19,15)**, the outer rune of a horizontal mirror:

```text
F(19,15) ── 4 ── X(19,19) ── 4 ── F(19,23)
```

The two `F` runes are equally distant from the center `X`. Following this mirror from the nearby `F(19,15)` to its opposite outer leads to **F(19,23)**, where the new ciphertext begins.

The center **X(19,19)** also belongs to a perpendicular mirror of the same radius:

```text
Y(15,19)
    |
    4
    |
X(19,19)
    |
    4
    |
Y(23,19)
```

Both structures are centered on the same cell and use a distance of **4**. This makes the movement through `F-X-F` part of a connected local pattern rather than an isolated jump.

## 2. The final J also leads to the key

The same **J(19,16)** is the upper outer of another radius-4 mirror, this time diagonal:

```text
J(19,16) ── 4 ── B(23,12) ── 4 ── J(27,8)
```

This **J-B-J** mirror provides the key. As in the preceding chapters, we apply Euler's totient to its center while leaving the outer runes unchanged:

```text
B = 17
φ(17) = 16 = T

J-B-J → J-T-J
```

Next, calculate the totient and Möbius signatures of the transformed structure:

```text
φ(J=11) = 10  → μ(10) = +1
φ(T=16) =  8  → μ(8)  =  0
φ(J=11) = 10  → μ(10) = +1

Totient signature: (10,8,10)
Möbius signature: (+1,0,+1)
Phase:              (1+0+1) mod 3 = 2
```

**Phase 2** rotates `J-T-J` to **J-J-T**. This gives the active key without selecting its order from the desired plaintext:

```text
J-T-J → phase 2 → J-J-T

Active key: J-J-T
```

The transition therefore uses **two mirrors of radius 4 near the same ending cell**: `F-X-F` identifies the ciphertext's starting position, while `J-B-J` generates its key.

## 3. Read the ciphertext from F(19,23)

Return to **F(19,23)**, the outer rune reached through `F-X-F`. Reading downward along column 23 gives three consecutive cells:

```text
F(19,23)
   ↓
L(20,23)
   ↓
I(21,23)
```

These form the ciphertext **F-L-I**. We already have a three-rune active key, **J-J-T**, so the two sequences can now be decrypted together.

## 4. Decrypting F-L-I

Subtract each key value from its corresponding ciphertext value, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `F = 0` | `J = 11` | `0 − 11 ≡ 18` | **E** |
| `L = 20` | `J = 11` | `20 − 11 = 9` | **N** |
| `I = 10` | `T = 16` | `10 − 16 ≡ 23` | **D** |

```text
Ciphertext: F - L - I
Key:        J - J - T
Plaintext:  E - N - D
```

The result is **END**. The last rune is **I(21,23)**, which is already part of the mirror network needed for the next word.

## 5. The endpoint matches the OUTER pattern

The key generator `J-T-J` produced Möbius signature **`(+1,0,+1)`**. In the route model, this signature is associated with an **OUTER** continuation.

That is exactly where `END` finishes: **I(21,23)** is the right outer of a horizontal mirror:

```text
I(21,21) ── 1 ── R(21,22) ── 1 ── I(21,23)
```

This repeats the same **`(+1,0,+1) → OUTER`** relationship seen earlier in `NOW THE`. The final cell is not just the end of the ciphertext; it also connects the current key signature to the geometry of the following stage.

## 6. The same center prepares IS

The `I-R-I` mirror has center **R(21,22)**. Transforming that center gives:

```text
R = 4
φ(4) = 2 = TH

I-R-I → I-TH-I
```

The same `R(21,22)` is also the center of a larger mirror on row 21:

```text
H(21,17) ── 5 ── R(21,22) ── 5 ── H(21,27)
```

It transforms to **H-TH-H**. Although the outer runes differ, **both structures produce the same totient signature**:

```text
I-TH-I → (4,1,4)
H-TH-H → (4,1,4)
```

One more coordinate check comes from the phase **2** already generated for `END`. At its endpoint, **I(21,23)**:

```text
φ²(21) =  4 → μ(4)  = 0
φ²(23) = 10 → μ(10) = +1

V₂(21,23) = (0,+1) → RIGHT-compatible
```

This gives a right-compatible horizontal component, while the shared `R` center supplies a concrete local continuation. The connected `I-R-I` and `H-R-H` mirrors are used in the next chapter, [`11-IS.md`](./11-IS.md), to generate the key for **IS**.
