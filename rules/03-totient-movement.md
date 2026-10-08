# 03 — Totient Movement

Euler's totient function does more than transform rune centers into keys. Across the route, **numbers already produced by the totient calculations are reused as distances between cells** in the 27×27 matrix. This is the basis of *totient movement*: the arithmetic that helps decrypt one segment also helps locate another.

The distinction is important: **a totient-derived value supplies a distance, not necessarily a direction**. The directions come from the surrounding geometry and, in the later reconstruction, the coordinate-selector rule in [`04-coordinate-selector.md`](./04-coordinate-selector.md). The key transformations themselves are explained in [`01-core-mechanics.md`](./01-core-mechanics.md).

## 1. Where movement values come from

The route uses several closely related sources of movement distances. A value can be obtained by applying `φ` to the center of a three-rune structure, by applying `φ` a second time, or by reading one or more numbers from a key's **totient signature**.

For example, a center with index `11` produces `φ(11)=10` and then `φ(10)=4`. Elsewhere, a generated key with signature `(4,1,4)` supplies the distances **4** and **1** directly. These are not different encryption algorithms: they are different uses of numbers already present in the same totient calculations.

The examples below show how those distances connect actual positions in the matrix.

## 2. The first two movements: 14 and 10

The first key-generating structure, `AE-J-EA`, is centered on **J(13,12)**. Its center gives two successive totient values:

```text
J = 11
φ(11) = 10 = I
φ(10) = 4

10 + 4 = 14
```

The value **10** transforms the center from `J` to `I`, producing the key `AE-I-EA`. Adding the next totient value **4** gives the first movement distance, **14**. Starting from the left outer rune of the structure:

```text
AE(13,11) → RIGHT 14 → L(13,25)
```

`L(13,25)` begins the seven-rune ciphertext decrypted as **AS I GO THE** in [`01-AS-I-GO-THE.md`](../plaintext-i-found/01-AS-I-GO-THE.md). The same center therefore contributes to both **key generation** and **navigation**.

The next stage uses the simpler form of this relationship. **AS I GO THE** ends at `X(14,4)`, an outer rune of `X-OE-X`. Its center produces:

```text
OE = 22
φ(22) = 10 = I

X-OE-X → X-I-X
```

Instead of adding another value, the route reuses **10** directly:

```text
X(14,4) → RIGHT 10 → NG(14,14)
```

That destination is the **exact center of the 27×27 grid**. Reading rightward from `NG(14,14)` begins the ciphertext for **WEATHER**, detailed in [`02-WEATHER.md`](../plaintext-i-found/02-WEATHER.md). Here `φ(OE)=10` simultaneously produces the new key center `I` and the movement to the matrix center.

## 3. The values 10 and 4 continue into TURNS

The numbers **10** and **4** do not disappear after **WEATHER**. Its ciphertext ends at `E(14,18)`, immediately before the crossroads **A(14,19)**. At this point, the inherited values are used together again.

The phase-2 coordinate selector gives `V₂(14,19)=(-1,+1)`, indicating **UP** and **RIGHT**. The horizontal distance **4** takes the route from the crossroads to the central `NG` of a new structure:

```text
A(14,19) → RIGHT 4 → NG(14,23)

A(14,19) ── 4 ── NG(14,23) ── 4 ── A(14,27)
```

The other inherited distance, **10**, then identifies the two vertical outer runes around `NG(14,23)`:

```text
NG(14,23) → UP 10   → H(4,23)
NG(14,23) → DOWN 10 → C(24,23)
```

The upward move agrees with the selector; the equal downward distance completes the three-rune structure. Together the cells give **H-NG-C**, the key for [`03-TURNS.md`](../plaintext-i-found/03-TURNS.md).

This is a good example of inheritance: **10** and **4** originally came from a preceding totient chain, but later become the distances needed to identify an entirely new key structure. The two values serve different geometric purposes rather than representing one combined move from a single starting cell.

## 4. NG generates the distance 12 for COLD

The newly found `H-NG-C` structure has **NG = 21** at its center. Applying Euler's totient gives another movement value:

```text
NG = 21
φ(21) = 12
```

The route returns to **A(14,19)**, where the phase-0 selector indicates `V₀(14,19)=(+1,-1)`, or **DOWN** and **LEFT**. The same distance **12** is used in both directions:

```text
A(14,19) → DOWN 12 → TH(26,19)
A(14,19) → LEFT 12 → G(14,7)
```

These are two distinct but coordinated destinations. **TH(26,19)** is the center of the `H-TH-H` mirror, which supplies the next key; **G(14,7)** is the starting rune of the next ciphertext. Together, they lead to **COLD** in [`04-COLD.md`](../plaintext-i-found/04-COLD.md).

In other words, the center of the **TURNS** key supplies the single distance that locates **both** the key structure and the ciphertext for the following stage.

## 5. A key signature becomes movement: 4 and 1

A movement distance can also come from a **totient signature**, rather than directly from one transformed center. The `COLD` key starts with `H-TH-H`, whose center transforms as `TH=2 → φ(2)=1=U`. This gives `H-U-H` and the signature:

```text
φ(H=8) = 4
φ(U=1) = 1
φ(H=8) = 4

Totient signature: (4,1,4)
```

**COLD** ends at `A(11,7)`. The phase-1 coordinate selector there gives `V₁(11,7)=(+1,+1)`, pointing **DOWN** and **RIGHT**. The inherited signature supplies the matching distances **4** and **1**:

```text
A(11,7) → DOWN 4  → S(15,7)
S(15,7) → RIGHT 1 → B(15,8)
```

The destination **B(15,8)** is the center of `NG-B-NG`. Its totient transformation produces the key structure used for **I MAY**, as shown in [`05-I-MAY.md`](../plaintext-i-found/05-I-MAY.md).

Notice the difference from the previous example. For **COLD**, the single transformed center `NG` gave the distance **12**. For **I MAY**, two entries of the preceding key's signature—**4** and **1**—supply two successive distances.

## 6. One inherited value connects CRY and NOW THE

The transition around **CRY** gives the clearest example of a value playing several roles without being newly calculated at every step. **I MAY** ends at `E(26,16)`, the lower outer rune of `E-X-E`. Transforming that structure's center gives:

```text
X = 14
φ(14) = 6 = G

E-X-E → E-G-E

φ(E=18) = 6
φ(G=6)  = 2
φ(E=18) = 6

Totient signature: (6,2,6)
```

The outer signature value **6** is then used as a straight movement:

```text
X(25,16) → UP 6 → J(19,16)
```

This landing reaches the center of `OE-J-OE`, and the upward ciphertext from `J(19,16)` decrypts to **CRY**. The complete step is documented in [`06-CRY.md`](../plaintext-i-found/06-CRY.md).

The value **6** continues beyond that word. **CRY** ends at `S(17,16)`, an outer rune of a horizontal mirror whose radius is also **6**:

```text
S(17,4) ── 6 ── IA(17,10) ── 6 ── S(17,16)
```

Its center reproduces the same value through a *double totient*:

```text
IA = 27
φ(27) = 18
φ(18) = 6

φ²(IA) = 6
```

That very same `IA(17,10)` is the center of a diagonal `TH-IA-TH` mirror, again with radius **6**:

```text
TH(11,16) ── 6 ── IA(17,10) ── 6 ── TH(23,4)
```

The relevant `TH` outer is located exactly six cells above the final `S` of **CRY**:

```text
S(17,16) → UP 6 → TH(11,16)
```

That `TH` begins the ciphertext for **NOW THE**, described in [`07-NOW-THE.md`](../plaintext-i-found/07-NOW-THE.md). Across these two stages, **6** occurs as a key-derived number, a movement distance, two mirror radii, the double totient of a shared center, and the next movement distance. The repeated agreement is more informative than any one occurrence on its own.

## 7. What totient movement explains—and what it does not

These examples establish a recurring relationship within the reconstruction: **totient-derived numbers can remain active after the key calculation and become exact distances to new matrix structures**. Sometimes the source is `φ(center)`, sometimes `φ²(center)` or a sum of the two, and sometimes one or more values from a key's signature.

This continuing reuse is called **totient inheritance**. It is what lets a number first introduced for arithmetic reappear later in the geometry of the route. The examples above preserve the main observed chains: **10 and 4**, **12**, **4 and 1**, and **6**.

Two questions must still be kept separate. First, a **distance** does not by itself choose between up, down, left, or right; that requires the directional and structural information discussed in [`04-coordinate-selector.md`](./04-coordinate-selector.md). Second, not every available totient value is used for movement. The current reconstruction documents where values are carried forward, but it does not yet define one universal activation rule that determines **which value is inherited, when it becomes active, and when it is used as a movement distance**.

That boundary matters: the arithmetic explains why the distances are numerically connected to the keys, while the subsequent route-selection rules explain how particular locations are chosen.
