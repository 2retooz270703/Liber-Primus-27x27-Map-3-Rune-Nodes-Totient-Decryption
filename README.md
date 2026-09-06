# Cicada 3301 — Liber Primus 0–2

## 🗝️ Current progress

The strongest plaintext recovered by the current model is:

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY...**

![Plaintext](https://img.shields.io/badge/Plaintext-10_proposed_words-2ea44f)
![Volume 1](https://img.shields.io/badge/Volume_1-7_words-2563eb)
![Volume 2](https://img.shields.io/badge/Volume_2-%2B3_words-7c3aed)

<!-- Add current progress / route image here -->

---

## 📖 Read the research

If you are opening this project for the first time, start with the PDFs. They are designed to be read visually and show the grid, routes, nodes, key locations, and decryption flow.

### Volume 2

📄 **[Read Volume 2 — visual PDF](./SOLUTION%200-2%20volume%202.pdf)**  
Continues the route beyond Volume 1 and develops the ideas of totient inheritance and hidden-key discovery.

📝 **[Open Volume 2 — technical Markdown](./SOLUTION-0-2-volume-2.md)**  
A structured technical version of the same research, optimized for reproducibility and further analysis.

### Volume 1

[📄 Read Volume 1 — visual PDF](./SOLUTION%200-2%20volume%201.pdf)
A visual walkthrough of the original 27×27 framework and the first major plaintext route.

📝 **[Open Volume 1 — technical Markdown](./SOLUTION-0-2-volume-1.md)**  
A cleaner machine-readable version for exact coordinates, arithmetic, verification, or AI analysis.

💡 **[What is this model trying to describe?](./WHAT-IS-LIBER-PRIMUS.md)**  
A conceptual explanation of the architecture behind the proposed system.

---

## What this project is

Pages 0–2 of Liber Primus contain exactly **729 rune tokens**.

`729 = 27 × 27`

If the runes are kept in their original order and placed row by row, they form a **27×27 grid**.

The central hypothesis of this project is that the grid is not only ciphertext. It may also act as a **map**.

In the proposed model, 3-rune structures can generate or reveal keys, Euler's totient function produces numerical values, the Möbius function selects the phase of a key, and some of those values can later be reused as movement distances through the grid.

So the model is not simply:

`ciphertext → plaintext`

It behaves more like:

```text
runes
  ↓
27×27 grid
  ↓
3-rune structure
  ↓
key / totient values
  ↓
Möbius phase
  ↓
decryption
  ↓
movement through the grid
  ↓
next structure
  ↺
```

The main idea is that **arithmetic and geometry are linked**.

---

## 🪞 Mirrored 3-rune nodes

A recurring structure is a mirrored node:

```text
a - b - a
```

When a mirrored node is used to generate a key, its center is transformed through Euler's totient:

```text
a-b-a → a-φ(b)-a
```

This produces a new 3-rune key while preserving the outer symmetry.

Mirrored structures are especially important in the current model because they repeatedly appear at transition points between different stages of the route.

---

## 🔑 Two ways keys appear

Not every key is found in the same way.

Some keys are generated **directly** from a mirrored 3-rune node by applying `φ` to its center.

Other keys appear to be **hidden elsewhere in the grid**. In those cases, specific totient values already obtained earlier in the route are reused as movement distances, leading to the location of the next key or key-structure.

In simple form:

```text
direct:
mirrored node → φ(center) → key

hidden:
known totient values → movement → hidden key location
```

A further pattern appears in the current route:

- if the discovered structure is **mirrored**, its center is transformed through `φ`;
- if the discovered key is **non-mirrored**, it is used directly.

The exact rule that decides **when hidden-key search becomes active** is still unknown, but the observed examples are reproducible.

---

## 🔁 Totient inheritance

One of the main findings of Volume 2 is that a totient value may remain important after its first use.

A derived number can later reappear as:

- a movement distance,
- part of a structural signature,
- a key-generation value,
- or an input to the Möbius phase rule.

This repeated reuse is described in the project as **totient inheritance** or a **totient chain**.

The claim is not that every previous totient is always reused. The narrower observation is that **specific derived values repeatedly return at structurally important points in the route**.

---

## 🧭 Möbius phase selection

Once a 3-rune key is known, the model does not choose the rotation that happens to look most like English.

Its phase is determined numerically:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

where `μ` is the Möbius function.

The result selects one of the three cyclic rotations:

```text
phase 0 → K1 K2 K3
phase 1 → K2 K3 K1
phase 2 → K3 K1 K2
```

This is important because the phase can be fixed **before** evaluating the resulting plaintext.

---

## 🔓 Decryption

The model uses **0-based Gematria Primus** values.

Plaintext is calculated as:

```text
P = C - K mod 29
```

where:

- `C` is the ciphertext rune value,
- `K` is the active key rune value,
- `P` is the resulting plaintext rune value.

The endpoint of one decryption can then become part of the next geometric structure, allowing the process to continue.

---

## 🧩 The model in one view

```text
729 original rune tokens
          ↓
      27×27 grid
          ↓
   find a structure
          ↓
 generate or locate key
          ↓
    Euler totient φ
          ↓
 totient signature / values
          ↓
      Möbius μ
          ↓
      key phase
          ↓
 GP subtraction mod 29
          ↓
       plaintext
          ↓
 geometry + inherited values
          ↓
   next structure / key
          ↺
```

---

## 📂 Useful files

🧱 **[Raw 729-rune dataset](./liber-primus-0-2-729-runes.txt)**  
The source rune sequence used to construct the 27×27 grid.

🗺️ **[27×27 matrix image](./liber-primus-27x27-matrix.png)**  
A visual reference for coordinates, routes, and node locations.

🧪 **[Volume 1 verifier](./verify-volume-1.py)**  
Checks the encoded coordinates, totient transformations, Möbius phases, key streams, and mod-29 arithmetic used in the Volume 1 core.

💡 **[Conceptual model](./WHAT-IS-LIBER-PRIMUS.md)**  
Explains the broader interpretation of the system and why previously derived values may become later instructions.

---

## ✅ Reproducibility

Volume 1 includes a Python verifier:

```bash
python3 verify-volume-1.py
```

No third-party packages are required.

A successful run confirms that the documented coordinates and arithmetic reproduce the documented result from the repository data.

It does **not** by itself prove that this is the intended Cicada 3301 solution.

---

## Where the research stands now

The current model can already reproduce a connected sequence of plaintext while repeatedly returning to the same families of structures, totient values, and key-generation behavior.

The main unresolved problem is now more demanding:

> **Can the next movement, node, and key be predicted from the current state before the next plaintext is known?**

That is the key test for turning the observed structure into a fully deterministic algorithm.

For the actual routes, coordinates, plaintext, and evidence, continue with **Volume 1** and **Volume 2**.

---

> **Research status:** proposed, reproducible, and still under active analysis.  
> This repository does not claim an officially verified Cicada 3301 solution.
