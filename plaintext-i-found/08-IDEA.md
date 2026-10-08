# 08 — IDEA

AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE IDEA

## 1. NOW THE leads directly to the next ciphertext

The previous chapter, [`07-NOW-THE.md`](./07-NOW-THE.md), ends at **J(15,20)**. This same cell becomes the first ciphertext rune of **IDEA**, so the new stage begins exactly where the previous one finished.

The key comes from a mirror connected to the route we have just followed. One step up-left from `J(15,20)` is **A(14,19)**, the lower outer rune of this diagonal mirror:

```text
A(8,13) ── 3 ── TH(11,16) ── 3 ── A(14,19)
```

The route used **A(14,19)** before reaching **J(15,20)**. Both cells lie on the same diagonal, making **A-TH-A** the natural nearby structure to examine for the next key.

## 2. The A-TH-A mirror generates the key

As in the earlier stages, transform only the center rune using Euler's totient. The center is `TH(11,16)`, whose rune value is **2**:

```text
TH = 2
φ(2) = 1 = U

A-TH-A → A-U-A
```

We now calculate the totient signature of the transformed structure **A-U-A**, then apply Möbius to determine its rotation:

```text
φ(A=24) = 8  → μ(8) = 0
φ(U=1)  = 1  → μ(1) = +1
φ(A=24) = 8  → μ(8) = 0

Totient signature: (8,1,8)
Möbius signature: (0,+1,0)
Phase:              (0+1+0) mod 3 = 1
```

**Phase 1** rotates `A-U-A` into **U-A-A**:

```text
A-U-A → phase 1 → U-A-A

Active key: U-A-A
```

The mirror therefore gives us the full three-rune key without needing to choose its rotation manually.

## 3. Read the ciphertext and decrypt IDEA

Starting at the last `NOW THE` cell **J(15,20)**, read diagonally down-left through two adjacent cells:

```text
J(15,20) → E(16,19) → D(17,18)

Ciphertext: J-E-D
```

Subtract the generated key **U-A-A** from these runes, modulo 29:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `J = 11` | `U = 1` | `11 − 1 = 10` | **I** |
| `E = 18` | `A = 24` | `18 − 24 ≡ 23` | **D** |
| `D = 23` | `A = 24` | `23 − 24 ≡ 28` | **EA** |

```text
Ciphertext: J  - E - D
Key:        U  - A - A
Plaintext:  I  - D - EA
```

The result is **IDEA**. It is written with four Latin letters but uses **three runes**: `I`, `D`, and `EA`.

The final ciphertext cell is **D(17,18)**. Its location is important because it is also the center of the mirror that connects to the next stage.

## 4. The endpoint matches the 010 → CENTER pattern

The key-generating structure **A-U-A** produced the Möbius signature **`(0,+1,0)`**. In the project's route model, this signature is associated with a **CENTER** continuation.

The final cell of **IDEA**, **D(17,18)**, is exactly the center of a diagonal mirror:

```text
J(15,20) ── 2 ── D(17,18) ── 2 ── J(19,16)
```

This is the **J-D-J** mirror. Notice that one of its outer runes, **J(15,20)**, is also where the **IDEA** ciphertext began. The new mirror therefore connects **both ends of the ciphertext**: it starts at one `J` and ends at the central `D`.

The same `010 → CENTER` relationship appears at the ending of **COLD**, and it appears again later at **IS**. Here, it connects the key's Möbius signature to the precise geometric role of the final rune.

## 5. J-D-J prepares OF THE

The center **D(17,18)** also supplies the next transformation. Its rune value is **23**, so Euler's totient gives:

```text
D = 23
φ(23) = 22 = OE

J-D-J → J-OE-J
```

The transformed structure has an especially clear totient signature:

```text
φ(J=11)  = 10
φ(OE=22) = 10
φ(J=11)  = 10

Totient signature: (10,10,10)
```

Now look at **J(19,16)**, the opposite outer rune of `J-D-J`. This same cell is the center of another mirror:

```text
OE(18,16)
    |
 J(19,16)   ← shared J
    |
OE(20,16)
```

The **OE-J-OE** mirror has **the same totient signature `(10,10,10)`**, because `φ(OE)=10` and `φ(J)=10`.

This gives a direct connection to [`09-OF-THE.md`](./09-OF-THE.md): **J-D-J** and **OE-J-OE** share the cell `J(19,16)`, and both produce the same totient signature. The next chapter uses these connected mirrors to recover **OF THE**.

The phase carried by **IDEA** is **1**. At its final cell, the coordinate selector also gives a right-compatible component:

```text
φ(17) = 16 → μ(16) = 0
φ(18) =  6 → μ(6)  = +1

V₁(17,18) = (0,+1)
```

Together, the **CENTER** endpoint, the shared `J` rune, and the matching `(10,10,10)` signatures explain how this local mirror network leads into the following chapter.
