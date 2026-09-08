<div align="center">

<sub><b>STRONGEST PLAINTEXT CANDIDATE</b></sub>

# AS I GO, THE WEATHER TURNS COLD.  
# I MAY CRY NOW. THE ...

<sub>Proposed Liber Primus 0–2 plaintext · ongoing research · not officially verified</sub>

</div>

---

## 27×27 Map

<p align="center">
  <img src="assets/27x27-map.png" alt="Liber Primus 27×27 rune map" width="100%">
</p>

**Map legend**

- 🟪 **Purple** — ciphertext cells that decrypt into the proposed plaintext.
- 🟦 **Blue** — hidden-key points; their position and geometry are used as clues.
- 🟩 **Green** — geometrically connected points that indicate or confirm the next move.
- **Thin purple outline** — mirror structures directly involved in producing or confirming plaintext.

---

## Full Research

The PDFs contain the complete derivations, maps, calculations, and reasoning behind each stage.

### **[Open the complete PDF archive →](./volumes/)**

[**Volume I**](./volumes/volume-1.pdf) · [**Volume II**](./volumes/volume-2.pdf) · [**Volume III**](./volumes/volume-3.pdf)

---

## How the Algorithm Works

The proposal treats the 729 runes of Liber Primus 0–2 as a **27×27 geometric map**, not only as a linear ciphertext.

> **729 runes → 27×27 map → mirror structure → Euler φ → key / movement → Möbius phase → mod-29 decryption → plaintext → next structure**

1. **Build the map.**  
   Place all 729 runes in their original order into a 27×27 matrix.

2. **Follow the geometry.**  
   Mirrored structures such as `A–B–A` act as nodes. If the route reaches an outer rune, the mirror naturally points **toward its center**. If it reaches the center, the route can trigger a **hidden-key search**, often on the perpendicular axis.

3. **Generate or locate the key with Euler’s totient.**  
   For a mirrored node, transform its center:
   `A–B–A → A–φ(B)–A`.  
   Totient values and signatures can persist between stages, reappearing as **movement distances**, **matching structural fingerprints**, or even **geometric radii**.

4. **Choose the key phase mathematically.**  
   A three-rune key has three cyclic phases. The active one is fixed by:
   `p = Σ μ(φ(Kᵢ)) mod 3`

5. **Decrypt with Gematria Primus.**  
   Read the ciphertext from the geometry selected by the route and subtract the active key modulo 29:
   `P = C − K mod 29`

6. **Use the endpoint as the next clue.**  
   The end of one plaintext segment repeatedly falls on, inside, or beside another meaningful structure. The next node inherits information from the previous one, so the process continues as a chain rather than restarting from scratch.

### Core idea

The same numerical information repeatedly appears in different forms — **key transformations, totient signatures, movement distances, mirror radii, and key phases**. The working hypothesis is that these are not separate tricks, but different layers of one geometric-cryptographic system.

---

<sub>This repository documents an independent cryptanalytic hypothesis for Cicada 3301's Liber Primus. The plaintext and route are proposed research results, not an officially verified solution.</sub>
