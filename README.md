<div align="center">

<sub>🧩 <b>LIBER PRIMUS 0–2 · 27×27 MODEL</b></sub>

<br>

## **AS I GO, THE WEATHER TURNS COLD.**  
## **I MAY CRY NOW. THE ...**

<sub>✨ Strongest plaintext found so far with the current route</sub>

</div>

---

## 📚 Want the full walkthrough?

The README keeps things short.  
The PDFs show the **complete route** with the highlighted map, coordinates, keys, calculations, and the reasoning behind every step.

### **[📖 Open the PDF archive →](./Read-PDFs-Here/)**

*Volumes 1–3 · visual research editions*

---

## 🗺️ Current map

<p align="center">
  <img src="./liber-primus-27x27-matrix.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

🟪 **Purple** — ciphertext used for plaintext  
🟦 **Blue** — hidden-key points  
🟩 **Green** — geometric clues and transitions  
🟣 **Purple outline** — mirrors directly involved in the route

---

## 🧭 How does the model work?

The basic idea is simple:

> **The 729 runes are treated as both ciphertext and a map.**

Since:

```text
729 = 27 × 27
```

the runes fit exactly into a **27×27 grid** without changing their original order.

From there, the route keeps repeating the same general pattern:

```text
🪞 find a structure
        ↓
🔑 get a key / number
        ↓
🧭 move or decrypt
        ↓
✨ recover plaintext
        ↓
➡️ reach the next structure
```

### 🪞 1 · Mirrors act like nodes

A recurring structure is:

```text
A — B — A
```

The center rune can be transformed with **Euler's totient function φ**.

That result may become a **key**, a **movement value**, or a clue to another point in the grid.

---

### 🔑 2 · Some keys are direct, others are hidden

Sometimes a mirror gives the next key immediately.

```text
mirror → φ(center) → key
```

Other times, a number found earlier tells us how far to move:

```text
earlier value → move through the map → hidden key
```

So the grid is doing two jobs at once: it holds the ciphertext **and** guides the route.

---

### 🔁 3 · Useful numbers can come back later

A value can first appear in one calculation and later return as:

- 📏 a movement distance
- 🧩 a matching signature
- 🔑 a hidden-key clue
- 🪞 a mirror radius

This repeated reuse is called **totient inheritance** in the research.

In plain language: **a number found earlier can still matter later.**

---

### 🧮 4 · Möbius chooses the key phase

A three-rune key can start in three cyclic positions.

Instead of choosing the one that looks best afterward, the phase is calculated first:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

Then the ciphertext is decrypted with zero-based Gematria Primus:

```text
P = C − K mod 29
```

So the arithmetic at the end is simple.  
The hard part is finding the right **place, structure, key, and direction**.

---

### ➡️ 5 · One result points to the next

The end of one plaintext block often lands on or near another meaningful structure.

That makes the whole route feel less like separate decryptions and more like one connected system:

```text
structure → key → movement → plaintext → next structure
```

This is the core idea behind the current **geometric state-machine** interpretation.

---

## ✨ What has been recovered so far?

**📘 Volume 1**  
Builds the 27×27 map and the core key / phase mechanism.

> **AS I GO, THE WEATHER TURNS COLD.**

**📗 Volume 2**  
Adds hidden keys and reuse of earlier totient values.

> **I MAY CRY...**

**📙 Volume 3**  
Adds mirror geometry as a direction clue and the radius-6 continuation.

> **NOW THE**

### Current combined reading

> **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

---

## 🧪 Want to check the mechanics?

You can reproduce the documented arithmetic and coordinates here:

- 🧱 **[Raw 0–2 runes](./other-stuff/0-2-runes.txt)**
- 🗺️ **[27×27 matrix](./liber-primus-27x27-matrix.png)**
- ✅ **[Volume 1 verifier](./verify_volume_1.py)**
- ✅ **[Volume 2 verifier](./verify_volume_2.py)**

The verifier scripts check the documented coordinates, transformations, key phases, and mod-29 arithmetic.

*They test whether the proposed route reproduces its stated results — not whether it is an official Cicada 3301 solution.*

---

## 🜏 New to Liber Primus?

No problem — start with the short introduction:

### **[🜏 What is Liber Primus? →](./WHAT-IS-LIBER-PRIMUS.md)**

It explains the puzzle itself and why this project treats pages 0–2 as a 27×27 map.

---

## 🤖 Working with AI?

For searchable text, exact coordinates, formulas, and machine-readable reasoning:

### **[🤖 Open the technical Markdown archive →](./other-stuff/md/)**

*Volumes 1–3 · better suited for AI analysis and detailed checking*

---

<div align="center">

<sub>🧭 Ongoing independent research · current model · not officially verified</sub>

</div>
