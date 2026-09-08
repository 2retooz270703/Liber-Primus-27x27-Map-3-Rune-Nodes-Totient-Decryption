<div align="center">

<sub><b>LIBER PRIMUS 0–2 · CURRENT MODEL</b></sub>

<br>

# **AS I GO, THE WEATHER TURNS COLD.**  
# **I MAY CRY NOW. THE ...**

✦

<sub>Strongest plaintext produced by the current 27×27 model</sub>

</div>

---

## 🗺️ Current map

<p align="center">
  <img src="./liber-primus-27x27-matrix.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

<p align="center">
  🟪 <b>Purple</b> — plaintext route &nbsp;&nbsp;·&nbsp;&nbsp;
  🟦 <b>Blue</b> — hidden-key points &nbsp;&nbsp;·&nbsp;&nbsp;
  🟩 <b>Green</b> — geometric clues
</p>

<p align="center">
  <sub>A thin purple outline marks mirror structures directly involved in the route.</sub>
</p>

---

# 📚 Read the full research

The README only shows the core idea.

The PDFs are the best place to understand the actual route: they contain the **highlighted matrix, coordinates, key generation, movement, calculations, and the reasoning behind every plaintext block**.

<div align="center">

## **[OPEN THE PDF ARCHIVE →](./Read-PDFs-Here/)**

<sub>Volumes 1–3 · visual walkthrough of the complete research</sub>

</div>

---

# 🧭 How the model works

The simplest way to understand the idea is this:

> **The 729 runes are treated not only as ciphertext, but as a map.**

Because:

```text
729 = 27 × 27
```

the rune sequence can be placed, without changing its order, into a perfect **27×27 grid**.

From there, the route moves through a repeating cycle:

```text
find a structure
      ↓
get a key or number
      ↓
use it to move / decrypt
      ↓
reach plaintext
      ↓
the endpoint reveals the next structure
```

The same map keeps being reused.

---

## 🪞 1. Mirrored structures act like nodes

A recurring pattern is:

```text
A — B — A
```

These small mirrored structures repeatedly appear at important transition points.

The center rune can be transformed with **Euler's totient function φ**:

```text
A — B — A
      ↓
    φ(B)
```

That transformed value can become:

- part of a key,
- a movement distance,
- or a clue that connects the current point to another structure.

So a mirror is not just visual symmetry — in the current model, it behaves like a **functional node**.

---

## 🔑 2. Some keys are generated, others are found

Sometimes the current mirror directly produces the next key:

```text
mirror → transform center → key
```

But some keys are **hidden elsewhere in the matrix**.

In those cases, values already discovered earlier are reused as distances:

```text
earlier value → move through the grid → hidden key
```

This is one of the most important ideas developed in Volume 2:  
**a useful number can survive beyond the step where it first appeared.**

---

## 🔁 3. The same number can return in a new role

A value may first appear as part of a key calculation, then later return as:

- a distance,
- a matching signature,
- a hidden-key clue,
- or even a geometric radius.

This repeated reuse is what the project calls **totient inheritance**.

The important point is simple:

> **previous steps can leave information behind for later steps.**

The route therefore behaves like a chain with memory rather than a sequence of unrelated decryptions.

---

## 🧮 4. Möbius fixes the key phase

A three-rune key can repeat in three cyclic orders.

Instead of choosing whichever order produces readable English, the active phase is calculated first:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

Only after that phase is fixed is the ciphertext decrypted.

This matters because it reduces one of the biggest sources of arbitrary choice.

---

## 🔓 5. Decryption itself is simple

Once the correct location and active key are known:

```text
P = C − K mod 29
```

using zero-based Gematria Primus values.

So the difficult part is not the subtraction.

The difficult part is discovering:

**where to read → which structure is active → which key belongs to it → where the result points next.**

---

## 🧭 6. Geometry helps decide where to move

Volume 3 adds an important idea: geometry may help determine direction.

If the route lands on the outer rune of a mirror:

```text
A — B — A
```

the mirror naturally points **toward its center**.

Even more interestingly, a value already produced mathematically can later reappear as an exact distance inside the map.

The strongest example so far is the value **6**, which reappears as a **radius-6 mirror** after `CRY`.

That is where the arithmetic and geometry begin to reinforce each other.

---

## ✨ The core idea

Across all three volumes, the same pattern keeps returning:

```text
structure
   ↓
number / key
   ↓
movement
   ↓
decryption
   ↓
plaintext
   ↓
new structure
```

The current hypothesis is that **keys, totient values, movement distances, mirror geometry and plaintext transitions are different layers of one connected system**.

That system currently produces:

<div align="center">

### **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

</div>

---

# 🜏 What is Liber Primus?

If you are new to Cicada 3301 or want the broader idea before reading the technical work:

## **[READ: WHAT IS LIBER PRIMUS? →](./WHAT-IS-LIBER-PRIMUS.md)**

This explains the puzzle itself, why the 27×27 structure became important, and the larger interpretation behind the project.

---

# 🤖 Working with AI?

For AI analysis, searching, quoting exact coordinates, or checking formulas, use the technical Markdown versions rather than the visual PDFs.

## **[OPEN THE TECHNICAL MARKDOWN ARCHIVE →](./other-stuff/md/)**

The archive contains the machine-readable versions of the research, organized for detailed analysis and verification.

---

## 🧪 Reproducibility files

- **[Raw 0–2 rune source](./other-stuff/0-2-runes.txt)**
- **[27×27 matrix image](./liber-primus-27x27-matrix.png)**
- **[Volume 1 verifier](./verify_volume_1.py)**
- **[Volume 2 verifier](./verify_volume_2.py)**

<sub>The verifier scripts reproduce the documented coordinates and arithmetic. They test internal reproducibility, not official Cicada verification.</sub>
