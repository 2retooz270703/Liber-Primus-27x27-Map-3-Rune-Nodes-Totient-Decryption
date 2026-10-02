<sub>Last updated: **2 October 2026**</sub>

## Liber Primus · 27×27 Route Research

This repository documents an ongoing reconstruction of a possible route through **Liber Primus pages 0–2**.  
The goal is not to collect every numerical coincidence, but to preserve only the mechanisms that can be followed, checked, and reproduced directly from the rune grid.

### Recovered plaintext

> **AS I GO, THE WEATHER TURNS COLD.**  
> **I MAY CRY NOW.**  
> **THE IDEA OF THE END IS DEATH.**  
> **SEE YOU ...**

### Repository structure

**[Plaintext reconstruction](./plaintext-i-found/)**  
The recovered text is split into individual stages. Each file shows the relevant grid position, three-rune structure, active key, movement, ciphertext, and modular decryption for that segment.

**[Rules](./rules/)**  
The general mechanics are collected separately so they only need to be explained once. This includes the 27×27 grid model, totient-based key construction, key-phase selection, movement values, coordinate direction selection, and CENTER / OUTER structural states.

### Current framework

The reconstruction begins from the **729 rune positions**, arranged as a **27×27 grid**. Repeating three-rune structures are treated as functional nodes. Their centers can be transformed with Euler's totient function to generate keys and numerical signatures.

Those values are then reused across the route. The Möbius function determines the active cyclic phase of a key, totient-derived values provide movement distances, the coordinate selector constrains direction, and the full Möbius state can distinguish CENTER-like and OUTER-like structural roles.

The plaintext files show these rules in use. The rules folder contains only the general mechanisms that currently repeat strongly enough to be treated as part of the working system.

---

<sub>Independent cryptanalytic research · not an officially verified Liber Primus solution.</sub>
