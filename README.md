<h1 align="center">Liber Primus · 27 × 27 Matrix</h1>

<p align="center">
  <sub>Research into a proposed plaintext path in LP2 · Pages 0–2</sub>
</p>

<p align="center">
  <strong>
    As I go, the weather turns cold.<br>
    I may cry now.
  </strong>
</p>

<p align="center">
  <strong>
    The idea of the end is death.<br>
    See you soon, then.
  </strong>
</p>

<p align="center">
  <strong>The key is to go ...</strong>
</p>

<p align="center">
  <a href="#numerical-observations">Numerical observations</a> ·
  <a href="#start-here">Start here</a> ·
  <a href="#research-notes">Research notes</a> ·
  <a href="#working-hypothesis">Working hypothesis</a>
</p>

---

## Numerical observations

<p align="center">
  <strong>3274 + 27 = 3301</strong><br>
  <sub>61 ciphertext-cell uses · 54 unique cells + 7 repeated uses · 27 × 27 matrix</sub>
</p>

The first 17 stages, from **AS I GO** to **THEN**, use ciphertext cells **61 times**: 54 unique cells and 7 repeated uses. The sum of their Gematria Primus (GP) prime values, counting repetitions, is **3274**. Adding **27**, the side length of the matrix, produces **3301**. To me, this looks like a possible author's signature.

<p align="center">
  <strong>26083 is the 2867th prime number</strong><br>
  <sub>54 unique ciphertext cells · GP sum: 2867 · Sum of absolute positions: 26083</sub>
</p>

The **54 unique cells** have a total GP value of **2867**, while the sum of their absolute positions is **26083**. The crazy part is that **26083 is the 2867th prime number**.

---

## Start here

If you're new to this repository, I recommend following this order:

1. **[Explore the interactive 27 × 27 matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)** — Inspect the ciphertext, keys, and proposed plaintext path visually. I built the map to make the findings easier to examine and verify.
2. **[Browse the plaintext records](./plaintext-i-found/)** — Get an overview of the individual plaintext discoveries and their locations in the matrix.
3. **Read the research notes below** — Start with **00**, which describes the decryption method, then follow the rules developed in **01–06**.

Most of the proposed plaintext was identified manually, guided by the method in **00** and by geometric relationships that stood out to me. I then investigated how one stage might predict the next. The resulting observations are documented in the following notes.

---

## Research notes

### [00 — The Decryption Method](./Start-reading-here/00-decryption-method.md)

The foundation of the proposed system: three-rune structures produce decryption keys; Euler's totient and Möbius functions determine cyclic alignment; and modular subtraction reveals plaintext.

### [01 — Predicting the Next-Key Signature](./Start-reading-here/01-next-key-signature.md)

How the current ciphertext predicts the next key's phase and complete Möbius signature, including cumulative phase cycles, Direct and Reflected modes, and relationships between 90° and 180° rotations.

### [02 — The Leftmost Cell and Rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md)

The leftmost ciphertext cell and its Möbius state. Introduces the 270° rotation rule for predicting whether the next ciphertext's leftmost cell is its beginning or end, and connects all four matrix rotations.

### [03 — Predicting the Reading Axis](./Start-reading-here/03-predicting-axis-and-reading-direction.md)

How to predict the next ciphertext's horizontal, vertical, or diagonal axis, and how the 270° rule further constrains the reading direction.

### [04 — Predicting the Next Key's Center Parity](./Start-reading-here/04-predicting-next-key-center-parity.md)

Two coordinate formulas for predicting the parity of the next key center's row and column. Both match **16/16 recorded transitions**. After **THEN**, the combined filter reduces **44** mirror nodes with signature **(+1, +1, +1)** to **16** candidates.

### [05 — Predicting the Next Ciphertext's Row Parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md)

Two formulas for predicting the row parity of the next ciphertext's endpoint and leftmost cell, linking phase, key center, a 180° rotation, and the center-parity rule. Both match **16/16 recorded transitions**; the proposed **THE** produces a conditional **17/17**. After **THEN**, the leftmost-cell candidates are reduced from **337 to 186**.

### [06 — Ciphertext Ray & Möbius Deviation](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md)

A geometric rule in which the next ciphertext begins on, or within one cell of, eight directional rays from the previous ciphertext's leftmost cell (**16/16 transitions**). The one-cell deviations are linked to zero Möbius values, with a mirror symmetry between **SEE** and **YOU**.

---

## Strongest plaintext evidence

**[Read the full collection of supporting observations →](./Start-reading-here/strongest-plaintext-evidence.md)**

One of my favorite numerical relationships concerns the GP sum of all runes from **AS I GO** through **DEATH**:

<p align="center">
  <strong>2163 = 3 × 7 × 103</strong><br>
  <sub>U = 3 · O = 7 · Y = 103</sub>
</p>

These are precisely the three GP primes associated with the runes in **YOU** (Y = 103, O = 7, U = 3). I find this particularly interesting alongside Cicada 3301's 2016 message: **“Seek and you will be found.”** The linked document covers this and other evidence in greater detail.

---

## Working hypothesis

From **AS I GO** to **THEN**, there are **17 plaintext-generation stages**, with **DEATH** at stage **13**. I suspect that the initial stages were deliberately arranged to reveal the structure of a larger geometric encryption method.

In this interpretation, the first 17 stages serve two purposes: they are part of the plaintext, and they provide examples from which the underlying rules can be inferred. This could explain the imagery of crossroads and directional signs, as well as the phrase **“SEE YOU SOON, THEN.”**

The idea is that a solver first reconstructs the early stages, notices their geometric and numerical relationships, and then uses the derived constraints to search the rest of the **27 × 27** matrix. Those constraints include **0°, 90°, 180°, and 270° rotations**, predicted Möbius signatures, key placement, and ciphertext geometry. Without the rules, the matrix may look like a collection of unrelated cells; with them, it may become possible to trace further plaintext.

Some constraints from **00**, including the coordinate selector and center/outer rule, no longer appear to hold beyond **THEN**, while the rules developed in **01–06** are intended to help investigate subsequent stages. One possibility is that the initial 17 stages were carefully constructed as clues and that later stages could be generated systematically.

This remains **my working interpretation**, not a demonstrated account of Cicada's original design. The links above contain the underlying methods, recorded transitions, and supporting observations so that the proposed path can be examined independently.
