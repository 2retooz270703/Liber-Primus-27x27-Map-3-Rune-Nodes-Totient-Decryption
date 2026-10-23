<h1 align="center">Liber Primus</h1>

<p align="center">
  <strong>A proposed plaintext path through the 27 × 27 matrix</strong><br>
  <sub>Cicada 3301 · LP2, pages 0–2 · Independent research</sub>
</p>

<p align="center">
  <em>
    As I go, the weather turns cold.<br>
    I may cry now.<br>
    The idea of the end is death.<br>
    See you soon, then.
  </em>
</p>

<p align="center">
  <sub>PROPOSED CONTINUATION</sub><br>
  <em>The key is to go …</em>
</p>

<p align="center">
  <a href="https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/"><strong>Explore the interactive matrix →</strong></a>
</p>

<p align="center">
  <a href="#numerical-observations">Numerical observations</a> ·
  <a href="#start-here">Start here</a> ·
  <a href="#research-notes">Research notes</a> ·
  <a href="#working-hypothesis">Working hypothesis</a>
</p>

---

## Numerical observations

The first **17 stages**, from **AS I GO** through **THEN**, use ciphertext cells **61 times**: **54 unique cells** and **7 repeated uses**. Two relationships emerge from their Gematria Primus (GP) prime values and absolute positions.

| Counting every ciphertext-cell use | Counting unique ciphertext cells |
| :--- | :--- |
| **3274 + 27 = 3301** | **26083 is the 2867th prime number** |
| The GP sum is **3274**, including repeated uses. Adding **27**, the side length of the matrix, gives **3301**. | The **54 unique cells** have a GP sum of **2867**. Their absolute positions sum to **26083**. |

Both GP totals use the **ciphertext runes before key subtraction**. Absolute positions are numbered from **1 to 729** in row-major order. I see the first relationship as a possible author's signature; the second connects rune values to cell positions through prime indexing.

### A further link to YOU

The proposed **plaintext** from **AS I GO** through **DEATH** has a GP sum of **2163**:

<p align="center">
  <strong>2163 = 103 × 7 × 3</strong><br>
  <sub>103 → Y &nbsp; · &nbsp; 7 → O &nbsp; · &nbsp; 3 → U</sub>
</p>

These factors correspond to the runes in **YOU**, a word in the later passage **SEE YOU SOON, THEN**. I also find the connection to Cicada 3301's 2016 message, *“Seek and you will be found,”* particularly interesting.

**[Read the full collection of supporting observations →](./Start-reading-here/strongest-plaintext-evidence.md)**

## Start here

| Order | Resource | What to explore |
| :---: | :--- | :--- |
| **1** | **[Interactive matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)** | Inspect ciphertext cells, keys, and the proposed plaintext path visually. |
| **2** | **[Plaintext records](./plaintext-i-found/)** | Review the individual stages and their locations in the matrix. |
| **3** | **[The decryption method](./Start-reading-here/00-decryption-method.md)** | Read **00** first, then follow the observations developed in **01–06** below. |

I built the map to make the findings easier to examine and verify. Most of the proposed plaintext was found manually, using the method in **00** and geometric relationships that stood out to me. I then investigated how each stage might constrain the next.

## Research notes

Read the notes in order: **00** introduces the decryption method; **01–06** develop constraints for following the path.

| Note | Focus |
| :--- | :--- |
| **[00 · Decryption method](./Start-reading-here/00-decryption-method.md)** | Three-rune keys, totient and Möbius functions, cyclic alignment, and modular subtraction. |
| **[01 · Next-key signature](./Start-reading-here/01-next-key-signature.md)** | Phase cycles, full Möbius signatures, Direct and Reflected modes, and 90°/180° rotations. |
| **[02 · Leftmost cell & rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md)** | The leftmost cell's Möbius state and the 270° beginning/end rule, connecting all four rotations. |
| **[03 · Axis & reading direction](./Start-reading-here/03-predicting-axis-and-reading-direction.md)** | Predicting a horizontal, vertical, or diagonal axis, then constraining direction with the 270° rule. |
| **[04 · Key-center parity](./Start-reading-here/04-predicting-next-key-center-parity.md)** | Two formulas predicting whether the next key center's row and column are even or odd. |
| **[05 · Ciphertext row parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md)** | Next endpoint and leftmost-cell row parities, linked to phase, key center, 180° rotation, and note **04**. |
| **[06 · Rays & Möbius deviation](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md)** | Eight rays from the current leftmost cell; endpoint Möbius values at 0° and 270° control the one-cell allowance. |

Notes **04–06** report matches across **16/16 recorded transitions**. The detailed counts and candidate reductions are collected below.

<details>
<summary><strong>Recorded checks and candidate reductions</strong></summary>

| Note | Reported result |
| :--- | :--- |
| **04 · Key-center parity** | Both formulas match **16/16** transitions. After **THEN**, their combined filter reduces **44 → 16** mirror nodes with signature **(+1, +1, +1)**. |
| **05 · Ciphertext row parity** | Both formulas match **16/16** transitions. Including the proposed **THE** gives a conditional **17/17**. After **THEN**, the possible leftmost cells are reduced from **337 → 186**. |
| **06 · Rays and deviations** | **12** exact ray alignments and **4** one-cell deviations give **16/16** matches. All four deviations meet the double-zero Möbius condition; **SEE → YOU** meets it while remaining exactly aligned, with reversed mirror geometry about column **16**. |

</details>

## Working hypothesis

**DEATH** appears at stage **13**; **THEN** completes stage **17**. My hypothesis is that these opening stages were deliberately constructed to serve as both plaintext and clues to a larger geometric encryption method.

<details>
<summary><strong>How the method might extend beyond THEN</strong></summary>

In this interpretation, a solver reconstructs the early path and learns to combine **0°, 90°, 180°, and 270° rotations**, predicted Möbius signatures, key placement, and ciphertext geometry. The resulting constraints could then guide a systematic search across the rest of the **27 × 27** matrix. This may also explain the imagery of crossroads and directional signs, together with **“SEE YOU SOON, THEN.”**

Some constraints from **00**, including the coordinate selector and center/outer rule, no longer appear to hold beyond **THEN**. The rules developed in **01–06** are intended to help investigate subsequent stages. One possibility is that Cicada carefully arranged the first 17 stages as examples, then placed later ciphertexts and keys programmatically using the continuing constraints.

</details>

This remains **my working interpretation**, not a demonstrated account of Cicada's original design. The linked records and notes provide the methods, transitions, and observations needed to examine the proposed path independently.
