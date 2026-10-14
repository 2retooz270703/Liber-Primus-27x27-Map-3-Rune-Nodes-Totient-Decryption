<!-- AUTO-PLAINTEXT:START -->
<p align="center">
  <a href="./plaintext-i-found/">
    <img src="./assets/plaintext-banner.gif" width="900" alt="Plaintext found in the 27x27 matrix">
  </a>
</p>
<!-- AUTO-PLAINTEXT:END -->

Plaintext.

---

<p align="center">
  <a href="https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/">
    <img src="./assets/example.gif" alt="Liber Primus Interactive Route Map" width="900">
  </a>
</p>

Map.

---


## About This Research

This repository documents my ongoing attempt to decipher **Liber Primus (LP2), pages 0–2** of Cicada 3301.

My approach treats all **729 runes as a single 27×27 matrix**, exploring relationships between rune positions, three-rune key structures, Euler's totient function, the Möbius function, and Gematria Primus.

Through this approach, I have identified a proposed sequence of English plaintext hidden within the matrix. But my main goal goes beyond finding readable words: **I am trying to reconstruct the deterministic algorithm that connects every decryption step and makes the next one predictable.**

### Research & Documentation

#### 01. [Discovered Deterministic Rules →](./Discovered-Deterministic-Rules/)

**The most important part of my current research.**

This folder documents mathematical rules discovered within the plaintext route, including methods for predicting the next decryption key's phase and its complete Möbius signature.

The latest combined prediction method reproduces **all 16 known consecutive key-signature transitions**, including the rarest signatures, using the geometry of the matrix and the Möbius function.

These are reproducible results on the known route, with predictions beyond it still awaiting independent verification.

#### 02. [Plaintext I Found →](./plaintext-i-found/)

The proposed plaintext recovered from pages 0–2, documented step by step.

Each file contains the ciphertext coordinates, three-rune key, mathematical transformations, and modular calculations that produce the corresponding plaintext.

#### 03. [Decryption Rules & Supporting Evidence →](./rules/)

A detailed explanation of the underlying decryption method, including:

- How three-rune keys are constructed and applied.
- How the algorithm navigates the 27×27 matrix.
- How mirrored rune structures are used.
- The strongest mathematical evidence supporting the proposed plaintext.

---

### Current Research Status

The proposed plaintext and its mathematical relationships have led to several increasingly specific deterministic patterns.

**The next challenge is to extend these rules beyond the currently recovered text and independently predict new plaintext.**

This is not yet a complete, independently verified solution to LP2 pages 0–2. It is an ongoing investigation, with the calculations, evidence, and proposed mechanisms documented openly for anyone interested in examining or reproducing them.
