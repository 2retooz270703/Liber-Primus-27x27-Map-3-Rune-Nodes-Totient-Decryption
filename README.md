<sub>Last updated · **2 October 2026**</sub>

<div align="center">

## Liber Primus · 27×27 Route Research

*An ongoing reconstruction of a possible route through Liber Primus pages 0–2.*

</div>

---

### Recovered plaintext

> **AS I GO, THE WEATHER TURNS COLD.**  
> **I MAY CRY NOW.**  
> **THE IDEA OF THE END IS DEATH.**  
> **SEE YOU ...**

---

### About this repository

This repository keeps the current reconstruction in a form that can be **followed, checked, and reproduced directly from the rune grid**.

The focus is on mechanisms that repeat across the recovered route: the 27×27 grid, three-rune structures, Euler-totient transformations, key generation, Möbius-based phase selection, movement values, coordinate direction selection, and CENTER / OUTER structural states.

Numerical coincidences and secondary observations are kept out of the main explanation unless they contribute directly to the working route.

---

### Research files

#### [Plaintext reconstruction](./plaintext-i-found/)

The recovered text is divided into individual stages. Each file shows the exact grid position, relevant structure, active key, movement, ciphertext, and modular decryption used to obtain that part of the plaintext.

#### [Rules](./rules/)

The general mechanisms are documented separately so they only need to be defined once. The plaintext files then apply those rules without repeating the full theory at every stage.

---

### Current working model

The reconstruction begins with the **729 rune positions arranged as a 27×27 grid**. Repeating three-rune structures are treated as functional nodes whose center can be transformed with Euler's totient function to generate keys and numerical signatures.

Those derived values are then reused across the route. The **Möbius function** determines the active cyclic phase of a key, **totient-derived values** provide movement distances, the **coordinate selector** constrains direction, and the **full Möbius state** can distinguish CENTER-like and OUTER-like structural roles.

The result is a route in which cryptographic operations and grid geometry are not treated as separate systems, but as parts of the same working mechanism.

---

<sub>Independent cryptanalytic research · not an officially verified Liber Primus solution.</sub>
