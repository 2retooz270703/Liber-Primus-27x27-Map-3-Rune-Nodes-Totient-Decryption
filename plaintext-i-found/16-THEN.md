# 16 — THEN

> **Recovered plaintext candidate:** `THEN` (`TH-E-N` — three runes)  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON THEN`  
> **Status:** strongest current direct continuation after `SOON`. The coordinates and decryption are exact; the route-selection rule is still a hypothesis.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. Start from the end of SOON

The primary `SOON` route in [`15-SOON.md`](./15-SOON.md) ends at:

```text
H(25,19)
```

Its **Möbius phase is already 2**. We keep that phase; nothing is selected to fit the next word.

Apply the existing coordinate selector:

```text
φ²(25) = 8     μ(8) = 0
φ²(19) = 6     μ(6) = +1

T₂(25,19) = (8,6)
V₂(25,19) = (0,+1) → RIGHT
```

The selector gives **RIGHT**, with the two retained numbers **8 and 6**.

---

## 2. The numbers 6 and 8 reach both ends of the ciphertext

Look right along row 25 from the last `SOON` rune:

```text
Column:  19  20  21  22  23  24  25  26  27
Rune:     H  EA  TH  IA  AE   C   L   T   W
Distance: 0  +1  +2  +3  +4  +5  +6  +7  +8
```

Both retained values land exactly on the boundaries of one short sequence:

```text
H(25,19) → RIGHT 6 → L(25,25)   START
H(25,19) → RIGHT 8 → W(25,27)   END
```

The three consecutive runes between these two positions are:

```text
L(25,25) → T(25,26) → W(25,27)

CIPHERTEXT = L-T-W
```

This directed `L-T-W` occurs **only once** among all straight three-rune paths in the grid.

**The key detail:** the direction and the pair `(8,6)` come from the previous stage. Treating 6 and 8 as the ciphertext boundaries is the proposed step, not yet a universal rule.

---

## 3. An exact midpoint reveals the key mirror

From the `SOON` endpoint `H(25,19)` to the start `L(25,25)` is a distance of 6. The midpoint is exactly three cells from each:

```text
H(25,19) ── 3 ── IA(25,22) ── 3 ── L(25,25)
```

That midpoint `IA(25,22)` belongs to a vertical mirror:

```text
IA(25,22)   ← midpoint
    |
IA(26,22)   ← center
    |
IA(27,22)
```

So the mirror is **IA-IA-IA**, radius 1. A scan of the 27×27 grid over horizontal, vertical and diagonal axes finds **exactly one** such mirror.

Transform its center using Euler's totient:

```text
IA = 27
φ(27) = 18 = E

IA-IA-IA → IA-E-IA
```

This gives the unrotated key **IA-E-IA**.

---

## 4. Möbius fixes the key phase

Apply the same phase rule used in the earlier chapters:

```text
KEY = IA-E-IA

Totient signature:
φ(27), φ(18), φ(27) = (18,6,18)

Möbius signature:
μ(18), μ(6), μ(18) = (0,+1,0)

phase = (0+1+0) mod 3 = 1
```

Rotate the key by phase 1:

```text
IA-E-IA → E-IA-IA

ACTIVE KEY = E-IA-IA
```

The key and its rotation are generated from the mirror; they are **not manually chosen** to spell `THEN`.

---

## 5. Decrypt L-T-W

Use the standard rule `P = (C − K) mod 29`:

| Ciphertext | Key | Calculation | Plaintext |
|---|---|---|---|
| `L = 20` | `E = 18` | `20 − 18 = 2` | **TH** |
| `T = 16` | `IA = 27` | `16 − 27 ≡ 18` | **E** |
| `W = 7` | `IA = 27` | `7 − 27 ≡ 9` | **N** |

```text
CIPHERTEXT: L   T    W
KEY:        E   IA   IA
            ----------
PLAINTEXT:  TH  E    N
```

# **THEN**

`TH` is **one rune**, so `THEN` contains three plaintext runes.

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON THEN**

---

## 6. THEN connects to the hidden second SOON route

This is the strongest geometric cross-check.

The new word ends at **W(25,27)**. The **secondary `SOON` route**, documented separately in [`15-SOON.md`](./15-SOON.md), ends at **W(27,27)**.

These two endpoints are the outers of the same exact local mirror:

```text
W (25,27)   ← end of THEN
    |
NG(26,27)  ← center
    |
W (27,27)  ← end of secondary SOON
```

**W-NG-W** links the new continuation to the previously discovered second branch of `SOON`.

This specific geometric connection is exact. The pattern `W-NG-W` itself is not globally unique.

---

## 7. The same mathematical state appears again

If the connecting `W-NG-W` mirror is selected as the next key generator:

```text
NG = 21
φ(21) = 12 = EO

W-NG-W → W-EO-W

Totient signature = (6,4,6)
Möbius signature = (+1,0,+1)
phase = 2
```

Now apply phase 2 at the end of `THEN`, `W(25,27)`:

```text
φ²(25) = 8     μ(8) = 0
φ²(27) = 6     μ(6) = +1

T₂(25,27) = (8,6)
V₂(25,27) = (0,+1) → RIGHT
```

Compare the two endpoints:

| | End of SOON | End of THEN, **if W-NG-W is selected** |
|---|---|---|
| Cell | `H(25,19)` | `W(25,27)` |
| Phase | **2** | **2** |
| Totient | **(8,6)** | **(8,6)** |
| Coordinate Möbius | **(0,+1)** | **(0,+1)** |

The endpoints are also exactly **8 columns apart** — the first number of the shared state.

**Important:** this return is *conditional*, not automatic. If we simply carry the `THEN` key phase **1** forward, the coordinate state is instead `T₁=(20,18)`, `V₁=(0,0)`. The endpoint also belongs to a `W-W-W` mirror that gives **phase 1**. The rule choosing `W-NG-W` must still be established.

---

## 8. One more numerical connection

The earlier words have rune-index sum:

```text
SEE  = 51
YOU  = 30
SOON = 30
        ---
TOTAL = 111

φ(111) = 72
```

The newly generated active key also sums to **72**:

```text
E + IA + IA = 18 + 27 + 27 = 72
```

Therefore:

```text
φ(GP(SEE YOU SOON)) = 72 = GP(KEY for THEN)
```

This is an exact observation found **after** the decryption, not an independent proof.

---

## 9. Why THEN stands out

The strongest point is how the route connects **previously established structures**, rather than just producing an English word:

1. The **phase 2 inherited from SOON** gives RIGHT and `(8,6)`. Those numbers land exactly on the start and end of `L-T-W`.
2. Halfway to the ciphertext's starting point lies the grid's **only `IA-IA-IA` mirror**. The existing Euler–Möbius rules turn it into the exact key `E-IA-IA` and decrypt `TH-E-N`.
3. The final rune of THEN, **W(25,27)**, forms `W-NG-W` with **W(27,27)** — the endpoint of the *hidden secondary SOON route already documented in [`15-SOON.md`](./15-SOON.md)*.

**This makes `W-NG-W` a natural mirror to examine next.** It is not selected simply because it happens to give phase 2: it directly bridges the new endpoint and an endpoint independently established in the previous chapter.

```text
THEN ends:           W(25,27)
                       |
                      NG(26,27)
                       |
Secondary SOON ends: W(27,27)
```

Using this connecting mirror gives **phase 2**, which restores the same coordinate state `(8,6)` and Möbius pair `(0,+1)` that SOON had before THEN began. The geometric link explains *why this mirror is especially relevant*; the repeated state is an additional result, not the reason the mirror was noticed.

The remaining open point is **formalizing the selection rule**. The meanings of `6` and `8` as ciphertext boundaries and the midpoint-mirror rule still need prospective tests. Another mirror (`W-W-W`) also passes through the endpoint, so the cross-branch connection makes `W-NG-W` well-motivated, **not mathematically mandatory**. A global search also finds other ways to obtain `THEN` if keys and routes are freely combined.

**Conclusion:** `THEN` is the strongest current stage-16 candidate because the inherited numbers, unique key mirror, and previously hidden SOON branch meet in one local construction. The geometry and decryption are exact; the full route is not yet proven to be the intended Cicada 3301 plaintext.

---

## 10. Compact route

```text
SOON ends: H(25,19), inherited phase 2
                  |
           T₂=(8,6), RIGHT
                  |
       RIGHT 6 → L(25,25)
       RIGHT 8 → W(25,27)
                  |
          CIPHER = L-T-W
                  |
       H → 3 → IA → 3 → L
                  |
       unique IA-IA-IA mirror
                  |
       φ(center): IA-E-IA
       μ signature: (0,+1,0)
       phase 1 → E-IA-IA
                  |
        L-T-W − E-IA-IA
                  |
                THEN
                  |
          ends at W(25,27)
                  |
   W-NG-W ↔ secondary SOON endpoint W(27,27)
                  |
    [if selected] phase 2 → T₂=(8,6)
```

The full coordinate and arithmetic checks can be reproduced against the [live map](../0-2-live-map.html) and the repository's [`rules/`](../rules/) documents.
