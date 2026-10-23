<h1 align="center">Liber Primus</h1>

<p align="center">
  <strong>LP2 · Pages 0–2</strong><br>
  <sub>27 × 27 rune matrix · A proposed plaintext reconstruction</sub>
</p>

<p align="center">
  <a href="https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/"><strong>Interactive matrix</strong></a>
  &nbsp; · &nbsp;
  <a href="./plaintext-i-found/">Plaintext records</a>
  &nbsp; · &nbsp;
  <a href="./Start-reading-here/00-decryption-method.md">Decryption method</a>
</p>

---

<p align="center"><sub>PROPOSED PLAINTEXT</sub></p>

<p align="center">
  <em>As I go, the weather turns cold.<br>
  I may cry now.</em>
</p>

<p align="center">
  <em>The idea of the end is death.<br>
  See you soon, then.</em>
</p>

<p align="center">
  <sub>AS I GO → THEN · 17 recorded stages</sub>
</p>

<p align="center">
  <em>The key is to go…</em><br>
  <sub>Proposed continuation</sub>
</p>

---

## About the project

This repository investigates pages 0–2 of Cicada 3301's *Liber Primus* as a **27 × 27 rune matrix**. It documents a proposed plaintext path, the keys used to recover it, and the relationships between their positions.

The method constructs three-rune keys using Euler's totient and Möbius functions, then applies modular subtraction. Most of the initial path was found manually. The research now asks whether its geometric patterns can help predict the next words.

Use the **[interactive matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)** to follow the path visually and the **[plaintext records](./plaintext-i-found/)** to inspect individual stages.

## Research notes

The notes build on one another. Begin with **00**, then continue in order.

| No. | Note | Focus |
| :---: | --- | --- |
| 00 | [Decryption method](./Start-reading-here/00-decryption-method.md) | Three-rune keys and plaintext extraction. |
| 01 | [Next-key signature](./Start-reading-here/01-next-key-signature.md) | The next key's phase and Möbius signature. |
| 02 | [Leftmost cell & rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md) | Whether the leftmost ciphertext cell is its beginning or end. |
| 03 | [Reading axis & direction](./Start-reading-here/03-predicting-axis-and-reading-direction.md) | The next ciphertext's axis and reading direction. |
| 04 | [Key-center parity](./Start-reading-here/04-predicting-next-key-center-parity.md) | Even or odd rows and columns for the next key's center. |
| 05 | [Ciphertext row parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md) | Row parity of the next ciphertext's endpoint and leftmost cell. |
| 06 | [Ciphertext ray & Möbius deviation](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) | An eight-direction geometric rule with at most a one-cell deviation. |

## Numerical observations

**GP** denotes the Gematria Primus prime values assigned to the runes.

> **3274 + 27 = 3301**

Across the first 17 stages, **61 ciphertext-cell uses**—54 unique cells and 7 repeated uses—have a total GP value of 3274. Adding the matrix's side length gives 3301.

> **26083 is the 2867th prime**

The **54 unique ciphertext cells** have a GP sum of 2867, while their absolute positions sum to 26083.

> **2163 = 3 × 7 × 103**

The plaintext GP sum from **AS I GO** through **DEATH** is 2163. Its prime factors match the rune values in **YOU**: U = 3, O = 7, Y = 103.

Whether these relationships were deliberately built into the matrix remains an open question. **[Plaintext evidence](./Start-reading-here/strongest-plaintext-evidence.md)** contains the calculations and discusses a possible connection to Cicada's 2016 message.

## Current direction

The working hypothesis is that the first **17 stages**, ending with **THEN**, reveal a geometric method for finding subsequent words.

Some constraints described in note 00 no longer hold after THEN. The later notes explore which constraints may continue to apply. The goal is to extend the plaintext with meaningful, grammatical phrases that satisfy those constraints without changing the rules to fit a preferred reading.
