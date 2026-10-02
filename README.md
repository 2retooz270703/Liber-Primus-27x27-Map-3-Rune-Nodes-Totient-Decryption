<sub>Last updated · **2 October 2026**</sub>

## Liber Primus · 27×27 Route Research

This repository documents an ongoing reconstruction of a possible route through **Liber Primus pages 0–2**.  
Only the parts of the method that can be checked directly against the rune grid are kept in the main structure.

---

### Recovered plaintext

<div align="center">

**AS I GO, THE WEATHER TURNS COLD.**  
**I MAY CRY NOW.**  
**THE IDEA OF THE END IS DEATH.**  
**SEE YOU ...**

</div>

---

### Repository

**[Plaintext reconstruction](./plaintext-i-found/)**  
The route is split into **14 stages**. Each file shows how one plaintext segment is recovered from the grid, including the relevant position, structure, movement, key, ciphertext, and decryption.

**[Rules](./rules/)**  
The repeated mechanics are collected into **5 working rules**, so the same explanations do not need to be repeated in every stage.

The full **27×27 rune map** is kept separately as a `.txt` file and serves as the common reference for coordinates, structures, and route positions.

---

### Current framework

The reconstruction currently uses:

- a **27×27 grid** built from 729 rune positions;
- recurring **three-rune structures**;
- **Euler totient** transformations for key generation and numerical values;
- **Möbius phase selection** for cyclic key position;
- **totient-derived movement** for distance;
- a **coordinate selector** for direction;
- **CENTER / OUTER states** for structural role.

These parts are treated as one connected route system rather than as separate tricks for individual plaintext segments.

---

<sub>Independent cryptanalytic research · not an officially verified Liber Primus solution.</sub>
