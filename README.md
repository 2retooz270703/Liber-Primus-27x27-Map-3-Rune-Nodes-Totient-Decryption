<div align="center">

<sub><b>CICADA 3301 · LIBER PRIMUS 0–2</b></sub>

# 27×27 Rune Matrix Research

<br>

<sub><b>CURRENT STRONGEST PLAINTEXT</b></sub>

<h1>
AS I GO, THE WEATHER TURNS COLD.<br>
I MAY CRY NOW. THE ...
</h1>

<sub>Independent cryptanalytic research · ongoing · not officially verified</sub>

</div>

---

## 🗺️ Current map

<p align="center">
  <img src="./liber-primus-27x27-matrix.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

| | Meaning |
|---|---|
| 🟪 **Purple** | ciphertext cells used to produce plaintext |
| 🟦 **Blue** | hidden-key points and geometric clues |
| 🟩 **Green** | transition / confirmation points |
| **Purple outline** | mirror structures directly involved in the route |

---

## Read the research

<table>
<tr>
<td width="50%" valign="top">

### 📚 PDF archive

**[Open Volumes 1–3 →](./Read-PDFs-Here/)**

The visual version of the research: maps, routes, highlighted structures, calculations and the full reasoning.

</td>
<td width="50%" valign="top">

### 🜏 What is Liber Primus?

**[Read the introduction →](./WHAT-IS-LIBER-PRIMUS.md)**

A short explanation of the puzzle, the idea behind this project, and why the 27×27 map matters.

</td>
</tr>
</table>

> 🤖 **Working with AI, checking coordinates, or reproducing calculations?**  
> Use the **[technical Markdown archive →](./other-stuff/md/)**

---

# The model, simply

The central idea is that the first 729 runes are not treated only as a line of ciphertext.

Because:

```text
729 = 27 × 27
```

they can be placed in their original order into a perfect **27×27 grid**.

The working hypothesis is that this grid behaves as both:

**ciphertext** + **map**

So the process is not just:

```text
ciphertext → key → plaintext
```

It is closer to:

```text
729 runes
   ↓
27×27 map
   ↓
find a structure
   ↓
derive a key or useful number
   ↓
move / decrypt
   ↓
plaintext
   ↓
next structure
   ↺
```

---

## 01 — The grid is the map

Every rune receives a fixed coordinate inside the 27×27 matrix.

That makes it possible to study not only the rune sequence, but also the **distance, symmetry and position** between runes.

The route is therefore spatial: one result can point to another place in the same matrix.

---

## 02 — Mirrored 3-rune structures act like nodes

A recurring structure is:

```text
A — B — A
```

The important rune is the center.

The project repeatedly finds that these mirrored 3-rune structures can act as **nodes**: they may generate a key, define a direction, or connect one stage of the route to the next.

For a mirrored node, the center can be transformed with Euler's totient function:

```text
A — B — A
      ↓
    φ(B)
```

This can produce a new rune value and therefore a new key or movement value.

---

## 03 — Earlier numbers can return later

One of the strongest observations across the later stages is that a number does not always disappear after being used once.

A value produced by a structure can later return as:

- a movement distance,
- a matching numerical signature,
- a hidden-key clue,
- or a geometric radius.

This is the idea referred to in the research as **totient inheritance**.

In simple terms:

```text
a structure gives a number
        ↓
the number is used
        ↓
the same number appears again later
        ↓
it helps locate the next structure
```

---

## 04 — The key phase is chosen before reading the plaintext

A 3-rune key can be rotated in three ways.

The project uses the Möbius function to determine which rotation is active:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

This matters because the phase is calculated **before** deciding whether the resulting plaintext looks meaningful.

Once the active key is known, decryption itself is simple:

```text
P = C − K mod 29
```

using zero-based Gematria Primus values.

---

## 05 — The end of one stage becomes the beginning of the next

The plaintext is not treated as the end of the process.

The final position of one decryption often lands on, beside, or inside another meaningful structure.

That gives the route its most important recurring shape:

```text
structure
   ↓
key / number
   ↓
plaintext
   ↓
endpoint
   ↓
new geometry
   ↓
next structure
```

This is why the project increasingly looks less like one static cipher and more like a **geometric state machine**.

---

## Why the geometry matters

The later stages suggest that geometry may help remove ambiguity from movement.

If the route reaches the outer rune of a mirror:

```text
A — B — A
```

the natural direction is toward the center.

Volume 3 also shows an especially interesting case where a previously derived value reappears as the actual radius of a mirror. In other words, the arithmetic and the geometry begin to confirm the same movement independently.

That is the main idea of the project:

> **The numbers, keys, movement and mirror geometry may be different parts of one connected system.**

---

## Progress across the three volumes

| Volume | Main contribution | Plaintext reached |
|---|---|---|
| **Volume 1** | 27×27 map, mirrored nodes, Euler φ, Möbius phase, mod-29 decryption | **AS I GO, THE WEATHER TURNS COLD.** |
| **Volume 2** | hidden keys and reuse of earlier totient values | **I MAY CRY...** |
| **Volume 3** | mirror geometry as a direction rule; radius-based continuation | **NOW THE** |

<div align="center">

### Current strongest reading

## **AS I GO, THE WEATHER TURNS COLD. I MAY CRY NOW. THE ...**

</div>

---

## 🧪 Reproducibility

For readers who want the raw material rather than the presentation:

- **[Raw rune source](./other-stuff/0-2-runes.txt)**
- **[27×27 matrix image](./liber-primus-27x27-matrix.png)**
- **[Volume 1 verifier](./verify_volume_1.py)**
- **[Volume 2 verifier](./verify_volume_2.py)**
- **[Technical Markdown archive](./other-stuff/md/)**

The verifier scripts check the documented coordinates, numerical transformations, key phases and mod-29 arithmetic.

They test whether the stated method reproduces the stated result. They do **not** prove that the plaintext is the official Cicada 3301 solution.

---

<div align="center">

<sub><b>Status:</b> proposed research · reproducible in the documented stages · still under active analysis</sub>

</div>
