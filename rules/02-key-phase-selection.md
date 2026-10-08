# 02 — Key Phase Selection

A three-rune key can begin at three different positions, but the order matters: changing the starting rune changes every subtraction in the ciphertext. **The Möbius phase rule selects one starting position mathematically**, using the key's totient signature. This chapter explains the calculation and shows how it works in the recovered stages.

The basic key-generation process is explained in [`01-core-mechanics.md`](./01-core-mechanics.md). Here we begin with a three-rune key that has already been generated.

## 1. Why a key needs a phase

Consider the key `H-U-H`. It has three possible cyclic orders:

```text
Phase 0: H-U-H
Phase 1: U-H-H
Phase 2: H-H-U
```

A phase is simply a **left rotation** of the same three runes. Phase 0 keeps their original order, phase 1 moves the first rune to the end, and phase 2 rotates the order once more.

The phase must be calculated **before** repeating the key across a ciphertext. Otherwise, the same three runes could produce three different decryptions.

## 2. How the Möbius phase is calculated

Start with a generated key `k₁-k₂-k₃`. The calculation has three steps.

**First, calculate the totient signature.** Apply Euler's totient function `φ` to the value of each rune in the key:

```text
Key:                k₁ - k₂ - k₃
Totient signature:  φ(k₁), φ(k₂), φ(k₃)
```

**Second, apply the Möbius function `μ`** to each of those three numbers. Each result is `−1`, `0`, or `+1`. For example, `μ(2)=−1`, `μ(6)=+1`, and `μ(4)=0`. The value is `0` when the number is divisible by the square of a prime, while `μ(1)=+1`.

**Third, add the three Möbius values and take the result modulo 3:**

```text
p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3
```

The result is always one of the three key phases:

```text
p = 0  →  keep k₁-k₂-k₃
p = 1  →  use  k₂-k₃-k₁
p = 2  →  use  k₃-k₁-k₂
```

This means the rotation follows from the key's numerical properties, not from testing different orders against a desired word.

## 3. Example: phase 1 produces the COLD key

In [`04-COLD.md`](../plaintext-i-found/04-COLD.md), the mirror `H-TH-H` is transformed into `H-U-H`. We can now calculate which of the three rotations to use.

The totient signature is:

```text
φ(H = 8) = 4
φ(U = 1) = 1
φ(H = 8) = 4

Totient signature: (4,1,4)
```

Apply Möbius and add the results:

```text
μ(4) = 0
μ(1) = +1
μ(4) = 0

p = (0 + 1 + 0) mod 3 = 1
```

**Phase 1** rotates `H-U-H` to **`U-H-H`**. Since the ciphertext for `COLD` contains four runes, the active key repeats once more from its first position:

```text
Generated key: H-U-H
Phase 1:       U-H-H
4-rune key:    U-H-H-U
```

That is the key used to decrypt `G-J-EA-A` into **COLD**.

## 4. The same rule produces the other phases

The calculation works without changing the procedure for different keys.

### Phase 0 — AS I GO THE

The first stage, [`01-AS-I-GO-THE.md`](../plaintext-i-found/01-AS-I-GO-THE.md), generates `AE-I-EA`. Its totient signature consists of `20`, `4`, and `12`, all of which have Möbius value `0`:

```text
AE-I-EA
φ → (20,4,12)
μ → (0,0,0)

p = (0 + 0 + 0) mod 3 = 0
```

**Phase 0** leaves the key as `AE-I-EA`. For the seven-rune ciphertext, it repeats as `AE-I-EA-AE-I-EA-AE`.

### Phase 2 — WEATHER

In [`02-WEATHER.md`](../plaintext-i-found/02-WEATHER.md), the generated key is `X-I-X`:

```text
X-I-X
φ → (6,4,6)
μ → (+1,0,+1)

p = (1 + 0 + 1) mod 3 = 2
```

**Phase 2** changes the order to `X-X-I`. Repeating it over five ciphertext positions gives `X-X-I-X-X`, the active key for **WEATHER**.

### Phase 2 — END and DEATH

Both [`10-END.md`](../plaintext-i-found/10-END.md) and [`12-DEATH.md`](../plaintext-i-found/12-DEATH.md) use the same generated key, `J-T-J`:

```text
J-T-J
φ → (10,8,10)
μ → (+1,0,+1)

p = (1 + 0 + 1) mod 3 = 2
```

Again, **phase 2** is selected. The active three-rune key is **`J-J-T`**, used in both stages.

## 5. What this rule determines

The Möbius phase answers one specific question: **once a three-rune key has been found, which rune should its repeating cycle start with?**

For example, `H-U-H` gives phase 1, while `X-I-X` gives phase 2. Those results are fixed by the totient and Möbius calculations. After rotation, the key is repeated to cover the ciphertext and its values are subtracted modulo 29, as explained in [`01-core-mechanics.md`](./01-core-mechanics.md).

**Phase selection is separate from route selection.** This rule determines the order of an existing key; the following rules explain how totient values, coordinates, and matrix structures are used to move through the grid. The next chapter is [`03-totient-movement.md`](./03-totient-movement.md).
