# 07 — NOW THE

AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE

## 1. CRY leaves a useful value: 6

The previous chapter, [`06-CRY.md`](./06-CRY.md), ends at **S(17,16)**. Its key came from the `E-X-E` mirror, whose center was transformed into `G`:

```text
X = 14 → φ(14) = 6 = G

E-X-E → E-G-E
Totient signature: (6,2,6)
```

The outer value **6** had already determined an exact movement in `CRY`: **UP 6** from `X(25,16)` to `J(19,16)`. The next stage reveals this same number in the geometry surrounding the final `S`.

## 2. Two mirrors confirm the distance of 6

The endpoint **S(17,16)** is the right outer rune of a horizontal mirror:

```text
S(17,4) ── 6 ── IA(17,10) ── 6 ── S(17,16)
```

Its radius is **6**. More importantly, the center `IA(17,10)` independently produces the same number through Euler's totient applied twice:

```text
IA = 27
φ(27) = 18
φ(18) = 6

φ²(IA) = 6
```

That `IA` is also the center of a second mirror, this time on the opposite diagonal:

```text
TH(11,16) ── 6 ── IA(17,10) ── 6 ── TH(23,4)
```

The two mirrors share **IA(17,10)**, have the same radius **6**, and connect `S` to a pair of `TH` runes. Of those two `TH` positions, **TH(11,16)** is exactly six cells straight above the `CRY` endpoint:

```text
S(17,16) → UP 6 → TH(11,16)
```

This gives a direct geometric starting point for the next ciphertext. The distance is supported by the previous key signature, both mirror radii, and the double totient of their shared center.

## 3. Read the new ciphertext

Starting at **TH(11,16)**, follow the diagonal down-right through four consecutive cells:

```text
TH(11,16) → AE(12,17) → B(13,18) → A(14,19) → J(15,20)
```

The five runes form the ciphertext **TH-AE-B-A-J**. Its final cell, **J(15,20)**, will also connect to the next chapter.

## 4. Reuse the OE-J-OE mirror to generate the key

The key comes from a mirror already encountered in `CRY`. That chapter's **UP 6** movement landed at `J(19,16)`, the center of the vertical structure:

```text
OE(18,16)
    |
 J(19,16)  ← center
    |
OE(20,16)
```

This is **OE-J-OE**. Transform its center using Euler's totient:

```text
J = 11
φ(11) = 10 = I

OE-J-OE → OE-I-OE
```

Now calculate the totient and Möbius signatures of `OE-I-OE` to determine the active rotation:

```text
φ(OE=22) = 10 → μ(10) = +1
φ(I=10)  =  4 → μ(4)  =  0
φ(OE=22) = 10 → μ(10) = +1

Totient signature: (10,4,10)
Möbius signature: (+1,0,+1)
Phase:              (1+0+1) mod 3 = 2
```

**Phase 2** rotates the three-rune structure into **OE-OE-I**. Repeating the cycle across the five ciphertext positions gives:

```text
OE-I-OE → phase 2 → OE-OE-I

Active key: OE-OE-I-OE-OE
```

The key therefore reuses the same `OE-J-OE` mirror that was already part of the previous stage's geometry.

## 5. Decrypting TH-AE-B-A-J

Subtract the active key from the ciphertext, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `TH = 2` | `OE = 22` | `2 − 22 ≡ 9` | **N** |
| `AE = 25` | `OE = 22` | `25 − 22 = 3` | **O** |
| `B = 17` | `I = 10` | `17 − 10 = 7` | **W** |
| `A = 24` | `OE = 22` | `24 − 22 = 2` | **TH** |
| `J = 11` | `OE = 22` | `11 − 22 ≡ 18` | **E** |

```text
Ciphertext: TH - AE - B - A  - J
Key:        OE - OE - I - OE - OE
Plaintext:  N  - O  - W - TH - E
```

The result is **NOW THE**. It contains **five runes** even though the Latin transcription has six letters, because `TH` is one rune.

## 6. A numerical connection between CRY and NOW THE

The two consecutive plaintext blocks have exactly the same **prime-valued Gematria Primus sum**:

```text
CRY:      C + R + Y          = 13 + 11 + 103        = 127
NOW THE:  N + O + W + TH + E = 29 + 7 + 19 + 5 + 67 = 127
```

There is another connection to the key. **127 is the 31st prime**, and **31** is the prime-valued Gematria Primus weight of `I` — the rune produced by transforming the key mirror's center `J`:

```text
OE-J-OE → OE-I-OE

prime-sum(CRY) = prime-sum(NOW THE) = 127
127 = 31st prime
prime-value(I) = 31
```

Thus, the equal prime sums of the two plaintext blocks also point numerically to the new key's transformed center.

## 7. The endpoint connects directly to IDEA

The active key `OE-I-OE` has Möbius signature **`(+1,0,+1)`**, which the route model associates with an **OUTER** continuation.

The ciphertext ends at **J(15,20)**. This exact rune is an outer of a diagonal mirror:

```text
J(15,20) ── 2 ── D(17,18) ── 2 ── J(19,16)
```

This is **J-D-J**. Notice the second outer, **J(19,16)**: it is the same `J` reached by **UP 6** in `CRY` and used above as the center of the key-generating `OE-J-OE` mirror.

That makes the connection especially clear. The final `J` of **NOW THE** is joined by one mirror to a `J` that has already played an important role in both **CRY** and this stage's key generation.

At `J(15,20)`, the phase-2 coordinate selector gives:

```text
φ²(15) = 4 → μ(4) = 0
φ²(20) = 4 → μ(4) = 0

V₂(15,20) = (0,0)
```

The continuation is therefore found through nearby mirror geometry. One step up-left from `J(15,20)` lies **A(14,19)**, the outer of the diagonal `A-TH-A` mirror:

```text
A(8,13) ── 3 ── TH(11,16) ── 3 ── A(14,19)
```

This mirror supplies the key in the next chapter, [`08-IDEA.md`](./08-IDEA.md). Its lower `A(14,19)` also lies directly on the ciphertext diagonal used to recover **NOW THE**, making the handoff to **IDEA** continuous.
