01&nbsp;&nbsp;&nbsp;&nbsp;<b>AS I GO, THE WEATHER TURNS COLD.</b>  
02&nbsp;&nbsp;&nbsp;&nbsp;<b>I MAY CRY NOW.</b>  
03&nbsp;&nbsp;&nbsp;&nbsp;<b>THE IDEA OF THE END ...</b>

---

#### 🗺️ The Map

<p align="center">
  <img src="./other-stuff/grid.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

🟪 **Purple** — plaintext route  
🟦 **Blue** — hidden-key locations  
🟩 **Green** — navigation clues

---

#### 🔮 See how the plaintext was found

Click below to start reading from Volume 1, then continue with the next volumes.

[View all volumes](./Read-PDFs-Here/)

#### 🧠 Working with AI?

The Markdown versions are easier to search and analyze.

[Open the markdown archive](./other-stuff/md/)

---

#### 💯 A numerical fingerprint

These numerical coincidences strongly support the idea that this may be a real solution to Liber Primus 0–2, rather than an arbitrary plaintext produced by chance.

```text
AS I GO, THE WEATHER TURNS COLD.
```

<sub>**7 words** · **21 runes** · **GP sum = 233**</sub>

```text
7 words
↓
21 plaintext runes = 3 × 7
↓
Sum of the 0-based Gematria Primus indices
of all 21 plaintext runes = 233
↓
COLD: sum of the 0-based GP indices = 51
↓
233 is the 51st prime

TURNS ends on W in column 19
COLD begins in column 7

W has:
0-based GP index = 7
prime value = 19

W is the only rune where:
19 − 7 = 12 = φ(NG)

So the same 19 → 7 relation appears twice:
numerically inside W
and geometrically in the route from TURNS to COLD

NG = GP index 21
NG = center of the 27×27 matrix

13 is the 7th Fibonacci number
233 is the 13th Fibonacci number

7 → F₇ = 13 → F₁₃ = 233
```

These connections tie together the plaintext length, its Gematria Primus values, the word COLD, the route through the grid, the central NG rune, and the Fibonacci pattern. Since all of them point back to the same recovered sentence, the result is difficult to explain as an arbitrary coincidence.

These relationships **were not used** to produce the original 7-word plaintext. They were discovered afterward. Now, the patterns found in those 7 words are being used as constraints to search for and test the real continuation of the plaintext.

---

#### 💡 What is the idea?

The model starts from one simple observation:

**729 runes = 27 × 27**

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

#### 🪞 Mirrors

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

#### 🚦 Keys and movement

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

#### 🗝️ Key phase

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

#### 🔗 Why the route is interesting

The recovered text does not appear as isolated words.

The end of one stage often lands on or points toward another meaningful structure.

So the model behaves more like:

```text
structure → key → movement → plaintext → next structure
```

That is the main idea behind the current **27×27 geometric route**.

---

#### ✅ Verify the results

For anyone who wants to reproduce the documented steps:

- 🗒️ [Raw 0–2 runes](./other-stuff/0-2-runes.txt)
- 🗺️ [27×27 grid](./other-stuff/grid.png)
- 💻 [Verification scripts](./other-stuff/verify/)

---

#### 🕸️ Urizen’s Labyrinth

The strongest interpretation of Liber Primus pages 0–2, connecting the labyrinth, geometry, plaintext, and William Blake’s *The First Book of Urizen*.

[My thoughts](./other-stuff/md/urizen.md)

---

#### 📚 Favorite Books

A small archive of books I love and recommend.

[See my books](./other-stuff/my-favorite-books/)
