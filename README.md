<div align="center">

<sub><b>LIBER PRIMUS 0–2 · 27×27 MODEL</b></sub>

<br>

## **AS I GO, THE WEATHER TURNS COLD.**  
## **I MAY CRY NOW. THE ...**

<sub>Current strongest plaintext from the documented 0–2 route</sub>

</div>

---

## 📚 Full research

The README gives only the core idea.  
The PDFs contain the **full route, highlighted geometry, coordinates, keys, calculations, and reasoning** for each stage.

### **[→ Open the PDF archive](./Read-PDFs-Here/)**

*Volumes 1–3 · visual research editions*

---

## 🗺️ Current map

<p align="center">
  <img src="./liber-primus-27x27-matrix.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

**🟪 Purple** — ciphertext used for plaintext  
**🟦 Blue** — hidden-key points  
**🟩 Green** — geometric clues / transitions  
**🟣 Purple outline** — mirrors directly involved in the route

---

## 🧭 The model in one minute

The central idea is simple:

> **The 729 runes are treated as both ciphertext and a map.**

Because:

```text
729 = 27 × 27
```

the runes fit exactly into a **27×27 grid** without changing their original order.

From there, the route behaves roughly like this:

```text
find a structure
      ↓
derive a key or number
      ↓
move / decrypt
      ↓
recover plaintext
      ↓
the endpoint reveals the next structure
      ↺
```

The same grid keeps being reused from one stage to the next.

---

### 🪞 1 · Mirrored structures act like nodes

A recurring form is:

```text
A — B — A
```

These three-rune mirrors repeatedly appear at important transition points.

The center rune can be transformed with **Euler's totient function φ**:

```text
A — B — A
      ↓
    φ(B)
```

The result can become a **key**, a **number**, or a clue for the next move.

---

### 🔑 2 · Keys can be direct or hidden

Sometimes the current mirror produces the key directly:

```text
mirror → transform center → key
```

Sometimes earlier values lead to a key somewhere else in the grid:

```text
earlier value → movement → hidden key
```

So the map is not only where the ciphertext sits — its geometry helps locate the next cryptographic state.

---

### 🔁 3 · Earlier numbers can return later

A value found in one stage may reappear later as:

- a movement distance,
- a matching numerical signature,
- a hidden-key clue,
- or a mirror radius.

This reuse is called **totient inheritance** in the research.

In simple terms:

> **a useful number can survive one step and become meaningful again later.**

---

### 🧮 4 · Möbius fixes the key phase

A three-rune key has three cyclic starting positions.

Instead of choosing whichever one gives readable English, the phase is calculated first:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

That fixes the active key **before** judging the plaintext.

---

### 🔓 5 · The final subtraction is simple

Once the location and active key are known:

```text
P = C − K mod 29
```

using zero-based Gematria Primus values.

So the difficult part is not the subtraction itself.

The difficult part is finding:

**where to read → which structure is active → which key belongs to it → where the result points next.**

---

### 🧩 6 · One stage leads into the next

The endpoint of a plaintext block often lands on, beside, or inside another meaningful structure.

That gives the model its repeating shape:

```text
structure
   ↓
key / number
   ↓
movement
   ↓
plaintext
   ↓
new structure
```

This is why the current interpretation is closer to a **geometric state machine** than to one static substitution cipher.

---

## ✨ Progress so far

**Volume 1** — establishes the 27×27 map, mirrored nodes, φ, Möbius phase and mod-29 decryption.

> **AS I GO, THE WEATHER TURNS COLD.**

**Volume 2** — develops hidden keys and reuse of earlier totient values.

> **I MAY CRY...**

**Volume 3** — develops mirror geometry as a direction clue and the radius-6 continuation.

> **NOW THE**

Together, the current strongest reading is:

> ### **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

---

## 🧪 Check the mechanics

For reproducibility and raw data:

- **[Raw 0–2 runes](./other-stuff/0-2-runes.txt)**
- **[27×27 matrix](./liber-primus-27x27-matrix.png)**
- **[Volume 1 verifier](./verify_volume_1.py)**
- **[Volume 2 verifier](./verify_volume_2.py)**

The verifier scripts check the documented coordinates, numerical transformations, key phases, and mod-29 arithmetic.

They test **internal reproducibility** of the proposed route; they do not establish an official Cicada 3301 solution.

---

## 🜏 New to Liber Primus?

If you want the broader context first:

### **[→ What is Liber Primus?](./WHAT-IS-LIBER-PRIMUS.md)**

A short introduction to the puzzle and the idea behind the 27×27 approach.

---

## 🤖 Working with AI?

For AI analysis, exact coordinates, searchable formulas, and machine-readable reasoning, use the Markdown versions:

### **[→ Open the technical Markdown archive](./other-stuff/md/)**

*Volumes 1–3 · searchable technical versions*

---

<div align="center">

<sub>Ongoing independent research · current model, not officially verified</sub>

</div>
