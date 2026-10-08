# 05 — I MAY

AS I GO, THE WEATHER TURNS COLD. I MAY

## 1. Continue from the end of COLD

The previous chapter, [`04-COLD.md`](./04-COLD.md), ends at **A(11,7)**. Its key came from the `H-TH-H` mirror, whose transformed structure `H-U-H` produced the totient signature **(4,1,4)** and **phase 1**.

At the final `A`, the phase-1 coordinate selector gives:

```text
φ(11) = 10 → μ(10) = +1
φ(7)  =  6 → μ(6)  = +1

V₁(11,7) = (+1,+1) → DOWN + RIGHT
```

Both components point toward positive directions. Reusing **4** and **1** from the preceding key signature as movement distances leads to:

```text
A(11,7) → DOWN 4 → S(15,7) → RIGHT 1 → B(15,8)
```

The destination **B(15,8)** is important because it sits at the center of another exact mirror.

## 2. The new mirror generates NG-T-NG

The rune `B(15,8)` is the center of a vertical **NG-B-NG** mirror, with both outer runes two cells away:

```text
NG(13,8)
    |
 B(15,8)  ← center
    |
NG(17,8)
```

Transforming the center by Euler's totient gives:

```text
B = 17
φ(17) = 16 = T

NG-B-NG → NG-T-NG
```

This produces the new three-rune key structure **NG-T-NG**. Its connection to the previous word becomes clearer when we compare the numerical signatures of the two mirrors.

## 3. The COLD endpoint and the new key share one signature

The final `A(11,7)` of `COLD` is itself the center of a small vertical mirror:

```text
EA(10,7)
    |
 A(11,7)  ← end of COLD
    |
EA(12,7)
```

This **EA-A-EA** mirror has the totient signature **(12,8,12)**:

```text
φ(EA=28) = 12
φ(A=24)  =  8
φ(EA=28) = 12
```

Now calculate the same signature for the newly generated `NG-T-NG`:

```text
φ(NG=21) = 12
φ(T=16)  =  8
φ(NG=21) = 12
```

**Both structures produce exactly (12,8,12)**. One is centered on the endpoint of `COLD`; the other provides the key for `I MAY`. This connects the two stages through the same mathematical signature, even though the mirrors occupy different parts of the matrix.

## 4. Determine the active key

Apply the Möbius function to the signature of `NG-T-NG`:

```text
Totient signature: (12,8,12)
Möbius signature: (0,0,0)
Phase:              (0+0+0) mod 3 = 0
```

**Phase 0** leaves the three-rune structure unchanged. To cover four ciphertext positions, repeat its first rune:

```text
NG-T-NG → phase 0 → NG-T-NG

Active key: NG-T-NG-NG
```

The key is now fixed by the mirror transformation and its Möbius phase.

## 5. Return to the earlier H-TH-H mirror and decrypt I MAY

The reconstruction returns to **H-TH-H**, the mirror that generated the key for `COLD`. Its center is **TH(26,19)** — the point reached in the previous chapter by moving **DOWN 12** from `A(14,19)`.

Reading left from that center gives four consecutive runes:

```text
TH(26,19) → G(26,18) → T(26,17) → E(26,16)
```

These form **ciphertext `TH-G-T-E`**. Subtract the active key `NG-T-NG-NG`, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `TH = 2` | `NG = 21` | `2 − 21 ≡ 10` | **I** |
| `G = 6` | `T = 16` | `6 − 16 ≡ 19` | **M** |
| `T = 16` | `NG = 21` | `16 − 21 ≡ 24` | **A** |
| `E = 18` | `NG = 21` | `18 − 21 ≡ 26` | **Y** |

```text
Ciphertext: TH - G - T  - E
Key:        NG - T - NG - NG
Plaintext:  I  - M - A  - Y
```

The result is **I MAY**. The new key comes from `NG-B-NG`, while the ciphertext begins at the center of the earlier `H-TH-H` mirror. In this way, the previous stage contributes both a movement signature and a location reused in the new decryption.

## 6. The final E connects directly to CRY

`I MAY` ends at **E(26,16)**. This cell is the lower outer of a vertical **E-X-E** mirror:

```text
E(24,16)
    |
X(25,16)  ← center
    |
E(26,16)  ← end of I MAY
```

The phase-0 coordinate selector at this endpoint gives **`V₀(26,16)=(+1,0)`**, while the nearby mirror identifies the next key-generating center, `X(25,16)`.

Transforming that center gives:

```text
X = 14
φ(14) = 6 = G

E-X-E → E-G-E
```

The transformed mirror introduces the value **6**, which guides the movement used to recover the next word, **CRY**, in [`06-CRY.md`](./06-CRY.md).
