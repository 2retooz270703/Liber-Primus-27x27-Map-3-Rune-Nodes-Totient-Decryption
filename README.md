<sub>Last updated · **2 October 2026**</sub>

## Liber Primus · 27×27 Route Research

This repository documents an ongoing reconstruction of a possible route through **Liber Primus pages 0–2**. The aim is to keep only the parts of the method that can be followed, checked, and reproduced directly from the rune grid.

---

### Recovered plaintext

<div align="center">

<br>

**AS I GO, THE WEATHER TURNS COLD.**

**I MAY CRY NOW.**

**THE IDEA OF THE END IS DEATH.**

**SEE YOU ...**

<br>

</div>

---

### Repository structure

**[Plaintext reconstruction](./plaintext-i-found/)**  
Step-by-step reconstruction of the recovered text. Each file records the relevant grid position, three-rune structure, active key, movement, ciphertext, and modular decryption for that stage.

**[Rules](./rules/)**  
The general mechanics used across the route, collected separately so each rule is defined once and then only applied in the plaintext files.

---

### Current framework

The reconstruction begins with the **729 rune positions arranged as a 27×27 grid**. Repeating three-rune structures are treated as functional nodes, and their centers can be transformed with Euler's totient function to generate keys and numerical signatures.

The current route is built from four recurring layers:

- **Möbius phase** — selects the active cyclic key position
- **Totient movement** — provides movement distances
- **Coordinate selector** — constrains movement direction
- **CENTER / OUTER states** — indicate the structural role of the next position

Together, these mechanisms connect the cryptographic operations with the geometry of the grid and form the current working route.

---

<sub>Independent cryptanalytic research · not an officially verified Liber Primus solution.</sub>
