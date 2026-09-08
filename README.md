<div align="center">

<sub><b>CICADA 3301 · LIBER PRIMUS 0–2</b></sub>

# 27×27 Rune Matrix Research

### CURRENT STRONGEST PLAINTEXT

# **AS I GO, THE WEATHER TURNS COLD.**
# **I MAY CRY NOW. THE ...**

<sub>Independent cryptanalytic research · ongoing · not officially verified</sub>

<br>

**729 runes → 27×27 map → geometry → keys → plaintext**

</div>

---

## 🗺️ Current map

<p align="center">
  <img src="./liber-primus-27x27-matrix.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

<p align="center">
  🟪 <b>Purple</b> — ciphertext used for plaintext &nbsp;&nbsp;
  🟦 <b>Blue</b> — hidden-key points &nbsp;&nbsp;
  🟩 <b>Green</b> — geometric clues
</p>

<p align="center">
  <sub>A thin purple outline marks mirror structures directly involved in the route.</sub>
</p>

---

<div align="center">

## Start here

### 📚 **[PDF ARCHIVE — VOLUMES 1–3](./Read-PDFs-Here/)**  
Visual walkthroughs with the full route, maps, calculations and reasoning.

### 🜏 **[WHAT IS LIBER PRIMUS?](./WHAT-IS-LIBER-PRIMUS.md)**  
A short introduction to the puzzle and the idea behind this research.

<br>

### 🤖 **[TECHNICAL MARKDOWN ARCHIVE](./other-stuff/md/)**  
Searchable versions for AI analysis, exact coordinates, formulas and verification.

</div>

---

## The idea in simple terms

The main hypothesis is that the first 729 runes of Liber Primus should not be read only as a line of ciphertext.

Because:

```text
729 = 27 × 27
```

the runes can be placed in their original order into a perfect **27×27 grid**.

The project treats that grid as both:

- **ciphertext**, and
- **a map that tells us where to look next**.

So the method is not just:

```text
ciphertext → key → plaintext
```

It is closer to:

```text
structure
   ↓
number / key
   ↓
movement or decryption
   ↓
plaintext
   ↓
next structure
```

The route keeps continuing through the same map.

---

## 🪞 Mirrors are the main structural nodes

A recurring pattern is a three-rune mirror:

```text
A — B — A
```

The center rune can be transformed with **Euler's totient function φ**.

In simple form:

```text
A — B — A
      ↓
    φ(B)
      ↓
new key / useful value
```

These structures can do several jobs: generate a key, define a direction, or connect the current point to another part of the map.

---

## 🔑 Keys can be found in two ways

Some keys are created **directly** from the mirror currently being used:

```text
mirror → transform center → key
```

Other keys are **hidden elsewhere in the grid**.

In those cases, numbers found earlier are reused as distances:

```text
previous value → move through grid → hidden key
```

This repeated reuse of earlier values is one of the main discoveries of Volume 2.

---

## 🧭 Geometry helps choose direction

A number may tell us **how far** to move, but the geometry can tell us **where**.

If the route lands on the outer rune of a mirror:

```text
A — B — A
```

the natural direction is **toward the center**.

Volume 3 develops this idea further: the same numerical value can reappear as an actual geometric distance or mirror radius.

So numbers and geometry appear to confirm each other rather than acting as separate systems.

---

## 🧮 Möbius fixes the key phase

A three-rune key can start in three different cyclic positions.

Instead of choosing the version that happens to produce English, the project calculates the phase with:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

This determines how the key starts **before** the plaintext is judged.

---

## 🔓 The actual decryption is simple

Once the position and active key are known, the rune values are decrypted with zero-based Gematria Primus:

```text
P = C − K mod 29
```

The difficult part is therefore not the subtraction.

The difficult part is finding the correct **structure, key, direction and next point**.

---

## 🔁 The important pattern

The strongest recurring behavior across Volumes 1–3 is:

```text
find structure
      ↓
derive key / number
      ↓
move or decrypt
      ↓
get plaintext
      ↓
endpoint reveals next structure
      ↺
```

A value discovered in one stage can later return as:

- a key value,
- a movement distance,
- a matching numerical signature,
- or a geometric radius.

That is the central idea of the current model: **the arithmetic and the geometry appear to be parts of the same chain.**

---

## Progress so far

**Volume 1** establishes the 27×27 map and the core structure, producing:

> **AS I GO, THE WEATHER TURNS COLD.**

**Volume 2** develops inherited values and hidden keys, extending the plaintext to:

> **I MAY CRY...**

**Volume 3** develops the geometric direction rule and the radius-6 transition, producing:

> **NOW THE**

Which gives the current strongest reading:

<div align="center">

### **AS I GO, THE WEATHER TURNS COLD.**
### **I MAY CRY NOW. THE ...**

</div>

---

## 🧪 Reproducibility

For readers who want to inspect the mechanics rather than the presentation:

- **[Raw rune source](./other-stuff/0-2-runes.txt)**
- **[27×27 matrix](./liber-primus-27x27-matrix.png)**
- **[Volume 1 verifier](./verify_volume_1.py)**
- **[Volume 2 verifier](./verify_volume_2.py)**
- **[Technical Markdown archive](./other-stuff/md/)**

The verification scripts reproduce the documented grid coordinates, numerical transformations, key phases and mod-29 arithmetic. They test internal reproducibility; they do not establish that the plaintext is an official Cicada 3301 solution.

---

<div align="center">

<sub><b>Research status:</b> proposed · reproducible in the documented stages · still under active analysis</sub>

</div>
