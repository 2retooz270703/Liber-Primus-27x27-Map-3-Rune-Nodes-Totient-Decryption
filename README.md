<h1 align="center">Liber Primus</h1>

<p align="center">
  <strong>LP2 · Pages 0–2 · 27 × 27 Matrix</strong><br>
  <sub>An investigation into a proposed geometric reconstruction of the plaintext</sub>
</p>

<p align="center">
  <a href="https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/">Interactive matrix</a>
  &nbsp;·&nbsp;
  <a href="./plaintext-i-found/">Plaintext records</a>
  &nbsp;·&nbsp;
  <a href="./Start-reading-here/00-decryption-method.md">Decryption method</a>
</p>

---

<h3 align="center">Proposed plaintext</h3>

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
  <sub>AS I GO → THEN: 17 recorded stages · THE KEY IS TO GO: proposed continuation</sub>
</p>

---

## Numerical observations

Two numerical relationships emerge from the **17-stage path**, from **AS I GO** through **THEN**:

| **3301 correspondence** | **Prime-index correspondence** |
| :---: | :---: |
| **3274 + 27 = 3301** | **26083 is the 2867th prime** |
| <sub>61 ciphertext-cell uses: 54 unique cells + 7 repeated uses. Their GP values sum to 3274; 27 is the matrix side length.</sub> | <sub>The 54 unique cells have a GP sum of 2867, while the sum of their absolute positions is 26083.</sub> |

The first relationship resembles a possible **3301 signature**. The second links the GP sum of the unique cells directly to the prime-number index of their summed positions. Whether these correspondences were intentional is part of the investigation.

---

## Explore the reconstruction

For a first visit, the most useful reading order is:

1. **[Open the interactive matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)** — Inspect the proposed ciphertext, key locations, and plaintext path visually. The map was built to make the geometric relationships easier to check.
2. **[Browse the plaintext records](./plaintext-i-found/)** — See the individual plaintext stages and their supporting records in the matrix.
3. **[Start with the decryption method (00)](./Start-reading-here/00-decryption-method.md)** — Understand the three-rune key construction before moving on to the transition rules in 01–06.

The initial plaintext path was found largely by manual exploration. The later documents examine whether the observed geometry and arithmetic can be turned into **rules that constrain the next stage**.

---

## Research notes · 00–06

The notes are organized in the order the proposed method develops: **decryption → key prediction → reading direction → geometric constraints**.

| Document | Focus |
| :--- | :--- |
| **[00 — The Decryption Method](./Start-reading-here/00-decryption-method.md)** | Three-rune key structures, Euler's totient and Möbius functions, cyclic alignment, and modular subtraction to obtain plaintext. |
| **[01 — Predicting the Next-Key Signature](./Start-reading-here/01-next-key-signature.md)** | Predicting the next key's phase and Möbius signature; cumulative phase, Direct/Reflected modes, and 90°/180° rotations. |
| **[02 — The Leftmost Cell and Rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md)** | The leftmost ciphertext cell, its Möbius state, and a 270° rule for predicting whether it is the beginning or end of the next ciphertext. |
| **[03 — Predicting the Reading Axis](./Start-reading-here/03-predicting-axis-and-reading-direction.md)** | Constraining horizontal, vertical, or diagonal reading axes and direction using the 270° rule. |
| **[04 — Predicting the Next Key’s Center Parity](./Start-reading-here/04-predicting-next-key-center-parity.md)** | Two coordinate formulas match **16/16 recorded transitions**; after THEN, they narrow **44 → 16** mirror-node candidates with signature (+1, +1, +1). |
| **[05 — Predicting the Next Ciphertext’s Row Parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md)** | Two row-parity predictions match **16/16 recorded transitions** (conditional **17/17** with the proposed THE); after THEN, they narrow **337 → 186** leftmost-cell candidates. |
| **[06 — Ciphertext Ray & Möbius Deviation](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md)** | An eight-ray, one-cell-tolerance geometric rule matching **16/16 recorded transitions**; zero-Möbius deviations and the SEE/YOU mirror relationship. |

These counts describe the documented path and proposed continuation; they are not independent confirmation of a complete decryption.

---

## Further plaintext evidence

<p align="center">
  <strong>2163 = 3 × 7 × 103</strong><br>
  <sub>GP sum from AS I GO through DEATH · U = 3 · O = 7 · Y = 103</sub>
</p>

The Gematria Primus sum of the runes from **AS I GO** through **DEATH** is **2163**. Its prime factors correspond to the GP values of the three runes spelling **YOU**. This is an intriguing connection to the 2016 Cicada 3301 message, **“Seek and you will be found.”**

**[Read the complete collection of plaintext evidence →](./Start-reading-here/strongest-plaintext-evidence.md)**

---

## Working hypothesis

The proposed sequence contains **17 stages from AS I GO through THEN**, with **DEATH at stage 13**. My hypothesis is that these opening stages may have been deliberately arranged to teach a geometric method: the solver reconstructs the first plaintext, detects relationships between ciphertext cells and keys, and uses those relationships to search for what follows.

Under this interpretation, the **27 × 27 matrix** is more than a grid of rune values. Rotations of **0°, 90°, 180°, and 270°**, Möbius signatures, key placement, and ciphertext geometry together constrain possible continuations. The crossroads and directional imagery, and the wording **“SEE YOU SOON, THEN,”** may be clues to that procedure.

Some rules described in **00**—notably the coordinate selector and center/outer rule—no longer appear to hold after **THEN**. The rules in **01–06** are attempts to identify constraints that remain useful beyond the initial stages. It is possible that the opening path was carefully constructed as a guide, while later plaintext was placed systematically.

The central open question is whether those constraints can identify **new, meaningful plaintext after THEN** without introducing arbitrary exceptions. This repository documents the proposed path, the calculations behind it, and the rules needed to test that idea.

<p align="center">
  <sub>Independent research · Proposed reconstruction, not a confirmed solution to Liber Primus</sub>
</p>
