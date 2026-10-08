# 12 — DEATH

AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA OF THE END IS DEATH.

## 1. Return from IS to the earlier J-B-J mirror

The previous chapter, [`11-IS.md`](./11-IS.md), ends at **D(21,10)**. This rune is the center of a diagonal mirror whose outer runes are both `E`:

```text
E(19,12) ── 2 ── D(21,10) ── 2 ── E(23,8)
```

The two outer runes are each two rows and two columns away from the center. Using the same distance **perpendicular to this diagonal**, we move two rows down and two columns right:

```text
D(21,10) ── (+2,+2) ──→ B(23,12)
```

This brings us back to a familiar location. **B(23,12)** is the center of the `J-B-J` mirror previously used to generate the key for `END`:

```text
J(19,16) ── 4 ── B(23,12) ── 4 ── J(27,8)
```

The route therefore reconnects with an earlier key-generating structure. We can apply the same Euler–Möbius rules to it again.

## 2. J-B-J regenerates the key used for END

Begin with the mirror **J-B-J**. Euler's totient transforms its center `B` while leaving the two outer `J` runes unchanged:

```text
B = 17
φ(17) = 16 = T

J-B-J → J-T-J
```

Next, calculate the totient signature of `J-T-J`, then apply the Möbius function to determine the key's phase:

```text
φ(J=11) = 10
φ(T=16) =  8
φ(J=11) = 10

Totient signature: (10,8,10)
Möbius signature: (+1,0,+1)
Phase:              (1+0+1) mod 3 = 2
```

**Phase 2** rotates `J-T-J` into `J-J-T`:

```text
J-T-J → phase 2 → J-J-T

Active key: J-J-T
```

This is **exactly the same active key used for `END`**. Instead of producing an unrelated key, the route returns to the earlier `J-B-J` mirror and regenerates it.

## 3. Phase 2 selects the other J

The `J-B-J` mirror has two outer runes: **J(19,16)** and **J(27,8)**. To decide which side to follow, apply the coordinate selector with the newly calculated phase 2 to the center **B(23,12)**:

```text
φ²(23) = 10 → μ(10) = +1
φ²(12) =  2 → μ(2)  = -1

V₂(23,12) = (+1,-1) → DOWN + LEFT
```

Of the two outer runes, **J(27,8)** lies down and left from `B(23,12)`. The other `J(19,16)` lies up and right.

The selector therefore points to **J(27,8)**, opening the side of the mirror that leads toward the next ciphertext.

## 4. A connected mirror chain reveals C-I-E

The selected **J(27,8)** is the lower outer rune of a small diagonal mirror:

```text
J(25,6) — C(26,7) — J(27,8)
```

Its center, **C(26,7)**, is also the right outer rune of another mirror on row 26:

```text
C(26,3) ── 2 ── OE(26,5) ── 2 ── C(26,7)
```

These two mirrors connect through the shared **C(26,7)**. Following the horizontal mirror to its opposite outer brings us to **C(26,3)**.

Reading the three adjacent cells from that position to the left gives:

```text
C(26,3) → I(26,2) → E(26,1)
```

We now have **ciphertext `C-I-E`**. The route reaches it through two connected mirrors, beginning at the `J` selected by the phase-2 direction.

## 5. Decrypting C-I-E

The active key `J-J-T` was already generated at the `J-B-J` mirror. Subtract it from the three ciphertext runes, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `C = 5` | `J = 11` | `5 − 11 ≡ 23` | **D** |
| `I = 10` | `J = 11` | `10 − 11 ≡ 28` | **EA** |
| `E = 18` | `T = 16` | `18 − 16 = 2` | **TH** |

```text
Ciphertext: C  - I  - E
Key:        J  - J  - T
Plaintext:  D  - EA - TH
```

The result is **DEATH**. Although it contains five Latin letters, it consists of **three runes**: `D`, `EA`, and `TH`.

The central structural connection is that **the same `J-B-J` mirror and the same `J-J-T` key** appear in the reconstructions of both `END` and `DEATH`. Between them, the route passes through `IS` and returns to the earlier mirror center.

## 6. Two numerical connections

There are two further relationships worth noting alongside the geometric decryption.

**First: the two seven-word passages are connected by Euler's totient.** Their Gematria Primus totals are:

```text
AS I GO THE WEATHER TURNS COLD = 233
THE IDEA OF THE END IS DEATH   = 232

φ(233) = 232
```

Because **233 is prime**, its totient is **232**. The total of the first passage therefore transforms directly into the total of the later passage.

**Second: the key-generating center connects to the numerical value of DEATH.** The passage `THE IDEA OF THE END IS DEATH` contains **17 runes**. The center of the reused `J-B-J` mirror also has value **17**:

```text
B = 17
φ(17) = 16 = T
16th prime = 53

DEATH = D(23) + EA(28) + TH(2) = 53
```

The same chain links the **17-rune passage**, the **B** center, its totient **16**, and the prime-valued total **53** of `DEATH`. These numerical relationships accompany the decryption; the actual plaintext is produced by the `C-I-E` and `J-J-T` subtraction above.

## 7. The endpoint prepares the next transition

The last ciphertext rune is **E(26,1)**. Its key came from `J-T-J`, so the phase and Möbius signature carried forward are:

```text
J-T-J
Totient signature: (10,8,10)
Möbius signature: (+1,0,+1)
Phase:              2
```

In the project's route model, `(+1,0,+1)` is associated with an **outer-rune** continuation. Applying phase 2 to the endpoint coordinates gives:

```text
φ²(26) = 4 → μ(4) = 0
φ²(1)  = 1 → μ(1) = +1

T₂(26,1) = (4,1)
V₂(26,1) = (0,+1) → RIGHT
```

So the next search is guided by an **outer mirror rune on the right-compatible side** of **E(26,1)**. This endpoint is not the `E(26,16)` from the earlier `E-X-E` mirror; the two positions are distinct.

One more number helps connect this ending to the next chapter. The plaintext through `DEATH` can be grouped into **12 major route blocks**:

```text
 1. AS I GO THE       7. NOW THE
 2. WEATHER           8. IDEA
 3. TURNS             9. OF THE
 4. COLD             10. END
 5. I MAY            11. IS
 6. CRY              12. DEATH
```

The central rune of the matrix is **NG = 21**. Its totient is **12**, and applying the totient again gives **4**:

```text
NG = 21 → φ(21) = 12 → φ(12) = 4
```

The following chapter, [`13-SEE.md`](./13-SEE.md), uses this **radius 4** together with the outer-rune signature and RIGHT-compatible direction to examine the next mirror and recover **SEE**.
