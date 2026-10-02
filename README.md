Last updated: **2 October 2026**

## Liber Primus 27×27 route research

This repository contains an ongoing reconstruction of a possible route through **Liber Primus pages 0–2**.

The work is organized into two parts: the recovered plaintext itself and the rules that repeatedly reproduce the route.

---

### Current recovered plaintext

<p align="center">
  <br>
  <strong>AS I GO, THE WEATHER TURNS COLD.</strong><br>
  <strong>I MAY CRY NOW.</strong><br>
  <strong>THE IDEA OF THE END IS DEATH.</strong><br>
  <strong>SEE YOU ...</strong>
  <br><br>
</p>

---

### Read the reconstruction

**[Plaintext](./plaintext-i-found/)**  
Each recovered segment is shown separately, with the exact grid positions, key, ciphertext, movement, and decryption used to obtain it.

**[Rules](./rules/)**  
The current rule set extracted from the recovered route: core mechanics, key-phase selection, totient movement, coordinate selection, and CENTER / OUTER states.

---

### Current method

The reconstruction currently relies on:

- a **27×27 rune grid** built from the 729 rune positions;
- recurring **three-rune structures**;
- **Euler totient** transformations;
- **Möbius-based key phase selection**;
- **totient-derived movement values**;
- a **coordinate selector** for movement direction;
- **CENTER / OUTER** structural states.

These rules are separated from the plaintext files so that each mechanism only needs to be explained once.

---

### Current status

This is an **independent cryptanalytic reconstruction** and is not an officially verified Liber Primus solution.

The recovered route currently reaches:

> **SEE YOU ...**

The main unresolved problem is the deterministic rule that selects the next continuation from that point.
