# 01 — AS I GO THE

> **Recovered fragment:** `AS I GO THE`  
> **Status:** proposed research, not an officially verified Cicada 3301 solution.

This is the first readable plaintext fragment I recovered from **Liber Primus pages 0–2**.

Before reading this chapter, open the exact 27×27 rune grid I used:

> **[Open `0-2-grid-i-used.txt`](../0-2-grid-i-used.txt)**

That `.txt` file is the basis for everything below.  
All coordinates, movements, nodes, and ciphertext positions refer to that grid.

Coordinates are written as:

```text
(row, column)
```

and are **1-based**.

---

## 1. Why I turned pages 0–2 into a grid

Pages 0–2 contain exactly:

```text
729 runes
```

and:

```text
729 = 27 × 27
```

So I placed all 729 runes into a **27×27 grid**, left to right, row by row.

That is the grid stored in:

```text
0-2-grid-i-used.txt
```

The important idea is that I stopped treating the text only as one long rune sequence and started treating it as a **map**.

---

## 2. The first structure that stood out

While looking through the grid, I noticed an unusual small symmetric area near the center-left.

The middle row of that structure is:

```text
AE — J — EA
```

This became the first useful 3-rune node.

Using the **0-based Gematria Primus index**:

```text
J = 11
```

Apply Euler's totient function:

```text
φ(11) = 10
```

Gematria Primus index `10` corresponds to:

```text
I
```

So:

```text
AE — J — EA
      ↓
   φ(J)=I
      ↓
AE — I — EA
```

This gives the repeating key:

```text
AE-I-EA
```

---

## 3. The same center rune gives the first movement

The same `J` also produces the movement distance.

Start again with:

```text
J = 11
```

Apply the totient:

```text
φ(11) = 10
```

Apply it again:

```text
φ(10) = 4
```

Then:

```text
10 + 4 = 14
```

So the first movement I tested was:

```text
RIGHT 14
```

In the grid, the left `AE` of the node is at:

```text
AE(13,11)
```

Moving 14 cells right gives:

```text
AE(13,11) → L(13,25)
```

This is the exact point where the first ciphertext segment begins.

---

## 4. The first ciphertext

Starting at:

```text
L(13,25)
```

I read to the end of row 13 and then continued at the beginning of row 14.

The seven runes are:

```text
L — AE — N — TH — P — U/V — X
```

Their coordinates are:

```text
L    (13,25)
AE   (13,26)
N    (13,27)
TH   (14,1)
P    (14,2)
U/V  (14,3)
X    (14,4)
```

So the first ciphertext block is:

```text
L-AE-N-TH-P-U/V-X
```

---

## 5. Decryption

Now repeat the key `AE-I-EA` across the seven ciphertext runes:

```text
Ciphertext: L   AE  N   TH  P   U/V X
Key:        AE  I   EA  AE  I   EA  AE
```

The decryption rule is:

```text
P = (C - K) mod 29
```

using the 0-based Gematria Primus indices.

This gives:

| # | Cipher | Key | Result |
|---:|---|---|---|
| 1 | `L` | `AE` | `A` |
| 2 | `AE` | `I` | `S` |
| 3 | `N` | `EA` | `I` |
| 4 | `TH` | `AE` | `G` |
| 5 | `P` | `I` | `O` |
| 6 | `U/V` | `EA` | `TH` |
| 7 | `X` | `AE` | `E` |

So:

```text
L-AE-N-TH-P-U/V-X
        minus
AE-I-EA-AE-I-EA-AE
        =
A-S-I-G-O-TH-E
```

which reads:

# **AS I GO THE**

---

## 6. Why I consider this first fragment important

The result is not based only on finding English words.

The same local structure gives both:

```text
AE-J-EA
   ↓
AE-I-EA
```

and:

```text
J = 11
↓
φ(11)=10
↓
φ(10)=4
↓
10+4=14
↓
RIGHT 14
```

That movement lands exactly on the start of the seven-rune ciphertext:

```text
L-AE-N-TH-P-U/V-X
```

and the generated key decrypts it directly into:

```text
AS I GO THE
```

So the full first step is:

```text
729 runes
↓
27×27 grid
↓
AE-J-EA
↓
φ(J)=I
↓
AE-I-EA
↓
J: 11 → 10 → 4
↓
10+4 = RIGHT 14
↓
L-AE-N-TH-P-U/V-X
↓
subtract AE-I-EA mod 29
↓
AS I GO THE
```

---

## 7. Later cross-check

Later in the research, I found a Möbius-based rule for choosing the cyclic phase of 3-rune keys.

For:

```text
AE-I-EA
```

the totient signature is:

```text
20-4-12
```

and the Möbius values are:

```text
0-0-0
```

Therefore:

```text
p = 0
```

So the key is used without rotation:

```text
AE-I-EA
```

This independently matches the orientation used in the original decryption.

---

## Next

The final ciphertext rune of this fragment is:

```text
X(14,4)
```

That `X` becomes part of the next structural handoff.

The next chapter continues from there:

```text
AS I GO THE → WEATHER
```

---

[← Back to the main page](../README.md)
