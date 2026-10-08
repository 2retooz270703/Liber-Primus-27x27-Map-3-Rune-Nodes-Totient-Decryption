# 04 — COLD

AS I GO, THE WEATHER TURNS COLD.

## 1. Continue from the end of TURNS

The previous chapter, [`03-TURNS.md`](./03-TURNS.md), returns to **A(14,19)**. Its mirror structure contains the central rune **NG**, whose value provides the number used for the next movement:

```text
NG = 21
φ(21) = 12
```

From `A(14,19)`, the same distance **12** is used in two directions: downward to find the next key-generating mirror, and leftward to find the ciphertext.

The coordinate selector also agrees with these directions:

```text
V₀(14,19) = (+1,-1) → DOWN + LEFT
```

The selector gives the orientation, while **φ(NG) = 12** supplies the distance. Together they describe two connected branches from the same starting cell.

## 2. Two movements of 12 find the key and ciphertext

First, move **DOWN 12** from the `TURNS` endpoint:

```text
A(14,19) → DOWN 12 → TH(26,19)
```

The destination **TH(26,19)** is the center of an **H-TH-H** mirror. This is the structure that will generate the key.

Now return to `A(14,19)` and move **LEFT 12**:

```text
A(14,19) → LEFT 12 → G(14,7)
```

The second destination **G(14,7)** is the first rune of the ciphertext. Thus, one value obtained from the earlier `NG` center identifies **both parts of the decryption**: where the key comes from and where the encrypted run begins.

## 3. Transform H-TH-H into the active key

The center of the `H-TH-H` mirror is **TH = 2**. Apply Euler's totient to that center, leaving the two outer runes unchanged:

```text
TH = 2
φ(2) = 1 = U

H-TH-H → H-U-H
```

To determine how the key is rotated, calculate the totient signature of `H-U-H` and apply the Möbius function:

```text
φ(H=8) = 4 → μ(4) = 0
φ(U=1) = 1 → μ(1) = +1
φ(H=8) = 4 → μ(4) = 0

Totient signature: (4,1,4)
Möbius signature: (0,+1,0)
Phase:              (0+1+0) mod 3 = 1
```

**Phase 1** rotates `H-U-H` into **U-H-H**. The ciphertext has four runes, so the first key rune repeats to cover the fourth position:

```text
H-U-H → phase 1 → U-H-H

Active key: U-H-H-U
```

The key is now determined by the mirror and its calculated phase.

## 4. Read the ciphertext and decrypt COLD

The leftward branch reached **G(14,7)**. Reading upward from that position gives four consecutive runes:

```text
G(14,7) → J(13,7) → EA(12,7) → A(11,7)
```

This is **ciphertext `G-J-EA-A`**. Subtract the active key `U-H-H-U`, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `G = 6` | `U = 1` | `6 − 1 = 5` | **C** |
| `J = 11` | `H = 8` | `11 − 8 = 3` | **O** |
| `EA = 28` | `H = 8` | `28 − 8 = 20` | **L** |
| `A = 24` | `U = 1` | `24 − 1 = 23` | **D** |

```text
Ciphertext: G - J - EA - A
Key:        U - H - H  - U
Plaintext:  C - O - L  - D
```

The result is **COLD**, completing the sentence **“AS I GO, THE WEATHER TURNS COLD.”** The two movements of **12** supplied its ciphertext and key-generating mirror without changing the established decryption method.

## 5. The final A becomes the center of another mirror

`COLD` ends at **A(11,7)**. This cell is the center of a small vertical mirror:

```text
EA(10,7)
    |
 A(11,7)  ← end of COLD, mirror center
    |
EA(12,7)
```

The resulting **EA-A-EA** structure is significant because the key for `COLD` has the Möbius signature **(0,+1,0)**. In the route's state interpretation, that signature is associated with a **CENTER** continuation — and the endpoint is exactly the center of this mirror.

The mirror also has a useful totient signature:

```text
φ(EA=28) = 12
φ(A=24)  =  8
φ(EA=28) = 12

Signature: (12,8,12)
```

This same signature will appear in the next stage, linking the `COLD` endpoint to the new key structure.

## 6. The next movement leads to I MAY

The active key leaves us with the signature **(4,1,4)** and **phase 1**. Apply the phase-1 coordinate selector to the final cell `A(11,7)`:

```text
φ(11) = 10 → μ(10) = +1
φ(7)  =  6 → μ(6)  = +1

V₁(11,7) = (+1,+1) → DOWN + RIGHT
```

Using the retained values **4** and **1** as distances gives:

```text
A(11,7) → DOWN 4 → S(15,7) → RIGHT 1 → B(15,8)
```

The landing cell **B(15,8)** is the center of an **NG-B-NG** mirror. Its transformed form **NG-T-NG** produces the same totient signature **(12,8,12)** as `EA-A-EA` at the end of `COLD`.

This is the starting connection for the next recovered words, **I MAY**, explained in [`05-I-MAY.md`](./05-I-MAY.md).
