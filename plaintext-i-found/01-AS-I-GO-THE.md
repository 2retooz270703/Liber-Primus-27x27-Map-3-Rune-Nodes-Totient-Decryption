# 01 — AS I GO, THE

AS I GO, THE

## 1. Arrange the runes into a 27×27 matrix

The rune sequence from pages 0–2 of *Liber Primus* contains **729 runes**. Since **729 = 27 × 27**, the runes can be arranged row by row into a square matrix. This gives each rune a position and lets us examine the geometric relationships between nearby cells.

The first key comes from this small region of the matrix:

```text
M (12,11)    H (12,12)    M  (12,13)
AE(13,11)    J (13,12)    EA (13,13)
EO(14,11)    AE(14,12)    OE (14,13)
```

The important part is its middle row: **AE(13,11) – J(13,12) – EA(13,13)**. Here **J** is the center of a three-rune structure that supplies both the key and the first movement distance.

## 2. Generate the key from the center J

As in the later chapters, apply Euler's totient function to the center rune while keeping the two outer runes unchanged. The value of **J** is **11**:

```text
J = 11
φ(11) = 10 = I

AE-J-EA → AE-I-EA
```

This produces the three-rune key **AE-I-EA**. To determine whether it needs to be rotated, calculate its totient signature and then apply the Möbius function:

```text
φ(AE=25) = 20 → μ(20) = 0
φ(I=10)  =  4 → μ(4)  = 0
φ(EA=28) = 12 → μ(12) = 0

Totient signature: (20,4,12)
Möbius signature: (0,0,0)
Phase: 0
```

**Phase 0** leaves the key in its original order: **AE-I-EA**.

## 3. The same J center gives the first movement

The center **J** also supplies the movement values. Apply Euler's totient twice, using the second result together with the first:

```text
J = 11
φ(11) = 10
φ(10) = 4

10 + 4 = 14
```

The route uses **14** as its movement distance. Starting from the left outer rune of the structure, **AE(13,11)**, move 14 cells to the right:

```text
AE(13,11) → RIGHT 14 → L(13,25)
```

This lands on **L(13,25)**, where the first ciphertext begins. The same center has therefore supplied **I** for the key and **14** for the movement.

## 4. Read the ciphertext across the row boundary

Starting at **L(13,25)**, follow the original rune order. The first three runes finish row 13; the sequence then continues at the beginning of row 14:

```text
Row 13: L(13,25) → AE(13,26) → N(13,27)
Row 14: TH(14,1) → P(14,2) → U(14,3) → X(14,4)
```

Together these form the seven-rune ciphertext **L-AE-N-TH-P-U-X**.

The key has three runes, so repeat **AE-I-EA** until it covers all seven ciphertext positions:

```text
Ciphertext: L  - AE - N  - TH - P  - U  - X
Key:        AE - I  - EA - AE - I  - EA - AE
```

## 5. Decrypt AS I GO, THE

Subtract each key value from the corresponding ciphertext value, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `L = 20` | `AE = 25` | `20 − 25 ≡ 24` | **A** |
| `AE = 25` | `I = 10` | `25 − 10 = 15` | **S** |
| `N = 9` | `EA = 28` | `9 − 28 ≡ 10` | **I** |
| `TH = 2` | `AE = 25` | `2 − 25 ≡ 6` | **G** |
| `P = 13` | `I = 10` | `13 − 10 = 3` | **O** |
| `U = 1` | `EA = 28` | `1 − 28 ≡ 2` | **TH** |
| `X = 14` | `AE = 25` | `14 − 25 ≡ 18` | **E** |


## 6. The final X opens the next stage

The last ciphertext rune is **X(14,4)**. This cell is also the left outer of a small horizontal mirror:

```text
X(14,4) — OE(14,5) — X(14,6)
```

The shared endpoint therefore leads directly into **X-OE-X**. Transforming its center produces the next key structure:

```text
OE = 22
φ(22) = 10 = I

X-OE-X → X-I-X
```

This begins the continuation to **WEATHER**, explained in [`02-WEATHER.md`](./02-WEATHER.md).
