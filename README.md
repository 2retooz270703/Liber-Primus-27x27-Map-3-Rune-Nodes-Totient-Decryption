

<div align="center">

<p align="center">
  <h3>
    AS I GO, THE WEATHER TURNS COLD.<br>
    I MAY CRY NOW.<br>
    THE ...
  </h3>
</p>

<sub>✨ current plaintext</sub>

</div>


#### 🔎 See how the plaintext was found

Click below to start reading from Volume 1, then continue with the next volumes.

#### **[🔍 View all volumes →](./Read-PDFs-Here/)**

---

### 🗺️ The map

<p align="center">
  <img src="./other-stuff/grid.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

🟪 **Purple** — plaintext route  
🟦 **Blue** — hidden-key locations  
🟩 **Green** — navigation clues

---

### 🧭 What is the idea?

The model starts from one simple observation:

> **729 runes = 27 × 27**

So the runes from Liber Primus pages 0–2 can be placed, in their original order, into a perfect **27×27 grid**.

The grid is then treated as two things at once:

**ciphertext** + **map**

The route repeatedly follows the same general pattern:

```text
🪞 find a structure
      ↓
🔑 get a key or useful number
      ↓
🧭 move through the grid
      ↓
🔓 decrypt
      ↓
✨ reach plaintext
      ↓
➡️ continue from that point
```

The important part is that one stage often leads directly into the next.

---

### 🪞 Mirrors

A recurring structure looks like this:

```text
A — B — A
```

These three-rune mirrors often appear at important points of the route.

The center rune can be transformed with **Euler's totient function φ**:

```text
A — B — A
      ↓
    φ(B)
```

That result can become a **key**, a **number used for movement**, or a clue to another structure.

---

### 🔑 Keys and movement

Some keys are generated directly from the mirror currently being used:

```text
mirror → transform center → key
```

Other keys are found elsewhere in the matrix.

In those cases, values discovered earlier can be reused as distances:

```text
earlier value → move → hidden key
```

So the numbers are not always used once and forgotten.

A value can return later as a distance, a matching signature, or even the radius of another mirror.

---

### 🌀 Key phase

A three-rune key can start in three cyclic positions.

The current model uses the Möbius function to choose that phase before looking at the plaintext:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

Once the phase is fixed, the actual decryption is simple:

```text
P = C − K mod 29
```

using zero-based Gematria Primus values.

---

### 🔁 Why the route is interesting

The recovered text does not appear as isolated words.

The end of one stage often lands on or points toward another meaningful structure.

So the model behaves more like:

```text
structure → key → movement → plaintext → next structure
```

That is the main idea behind the current **27×27 geometric route**.

---

### ✅ Verify the results

For anyone who wants to reproduce the documented steps:

- 🗒️ **[Raw 0–2 runes](./other-stuff/0-2-runes.txt)**
- 🗺️ **[27×27 grid](./other-stuff/grid.png)**
- 💻 **[Verification scripts](./other-stuff/verify/)**

---

### ✨ How I see Liber Primus
A short look at how I understand the puzzle and why I started exploring it as a 27×27 structure.

#### **[🔍 Read my view →](./other-stuff/md/What-Is-Liber-Primus.md)**

---

### 🧠 Working with AI?

The Markdown versions are easier to search and analyze.

#### **[🔍 Open the Markdown archive →](./other-stuff/md/)**

<div align="center">

<sub>Independent ongoing research · not officially verified</sub>

</div>
