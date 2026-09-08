<div align="center">

<sub><b>CICADA 3301 · LIBER PRIMUS 0–2</b></sub>

# 𐌙 27×27 RUNE MATRIX RESEARCH 𐌙

<sub><b>CURRENT STRONGEST PLAINTEXT</b></sub>

# AS I GO, THE WEATHER TURNS COLD.
# I MAY CRY NOW. THE ...

<sub>Independent cryptanalytic research · ongoing · not officially verified</sub>

<br>

**A geometric / number-theoretic approach to Liber Primus pages 0–2**  
729 runes · 27×27 map · mirrored nodes · Euler φ · Möbius μ · Gematria Primus mod 29

</div>

---

## 🗺️ The current map

<p align="center">
  <img src="./liber-primus-27x27-matrix.png" alt="Liber Primus 27×27 rune matrix and current route" width="100%">
</p>

<div align="center">

**🟪 Purple** — ciphertext that decrypts into the proposed plaintext  
**🟦 Blue** — hidden-key points whose position is used as a geometric clue  
**🟩 Green** — geometric confirmation / transition points  
**🟣 Thin purple outline** — mirrors directly involved in forming or confirming plaintext

</div>

> The same 729-rune matrix is used throughout the research. The route continues from one state to the next; each volume adds another part of the same map rather than starting over.

---

<table>
<tr>
<td width="50%" align="center">

### 📚 Read the research

**[OPEN THE PDF ARCHIVE →](./Read-PDFs-Here/)**

The visual editions of the research.  
Start here if you want to follow the route, highlighted matrix, keys, geometry and decryption step by step.

**Volumes 1–3 are kept together in one archive.**

</td>
<td width="50%" align="center">

### 🜏 What is Liber Primus?

**[READ THE CONCEPTUAL EXPLANATION →](./WHAT-IS-LIBER-PRIMUS.md)**

A shorter explanation of what Liber Primus is, why I began treating the ciphertext as a map, and how I currently interpret the architecture of the puzzle.

**Best starting point before the technical details.**

</td>
</tr>
</table>

<br>

<div align="center">

### 🤖 Working with AI or checking the method?

The PDF archive is designed for human reading.  
For searchable text, exact formulas, coordinates and machine-readable reasoning, use the Markdown editions:

## **[OPEN THE TECHNICAL MARKDOWN ARCHIVE →](./other-stuff/md/)**

<sub>Contains the technical Volume 1, Volume 2 and Volume 3 notes.</sub>

</div>

---

# ✨ What this project is actually proposing

The starting observation is simple: **Liber Primus pages 0–2 contain exactly 729 rune tokens.**

```text
729 = 27 × 27
```

If the rune sequence is kept in its original order and written **left-to-right, row-by-row**, it forms a perfect **27×27 matrix**.

That gives every rune a fixed coordinate `(row, column)`.

The working hypothesis is that this matrix is doing two jobs at the same time:

1. it is the **ciphertext**;
2. it is also a **map through the ciphertext**.

The route is therefore not simply:

```text
ciphertext → key → plaintext
```

Instead, the current model behaves more like:

```text
729 runes
   ↓
27×27 map
   ↓
geometric / 3-rune structure
   ↓
Euler totient φ
   ↓
key, signature or movement value
   ↓
Möbius phase μ
   ↓
Gematria Primus subtraction mod 29
   ↓
plaintext
   ↓
endpoint + inherited geometry
   ↓
next structure
   ↺
```

The important part is the **loop**. A plaintext block does not simply end. Its endpoint can already lie on the next useful structure, while numbers obtained earlier can return as movement distances, key signatures, or geometric radii.

---

# 🪞 1. Mirrored 3-rune structures

A recurring object in the matrix is a three-rune mirror:

```text
A — B — A
```

When such a structure acts as a key-generating node, the center is transformed with Euler's totient function:

```text
A — B — A
      ↓ φ
A — φ(B) — A
```

For example, one of the first nodes is:

```text
AE — J — EA
```

With zero-based Gematria Primus values:

```text
J = 11
φ(11) = 10 = I
```

so:

```text
AE — J — EA  →  AE — I — EA
```

The matrix supplies the **structure**, and the totient operation supplies the **transformed center** used in the key.

This same behavior appears again with structures such as:

```text
X  — OE — X   → X  — I — X
H  — TH — H   → H  — U — H
E  — X  — E   → E  — G — E
OE — J  — OE  → OE — I — OE
```

---

# 🧭 2. The geometry can determine direction

One problem in the early route was direction: if a number says “move 6,” what tells us **which way**?

Volume 3 suggests a simple geometric answer.

For a horizontal mirror:

```text
A — B — A
```

If the route lands on the left `A`, the structure points right — toward `B`.  
If it lands on the right `A`, the structure points left — again toward `B`.

For a vertical mirror:

```text
A
│
B
│
A
```

The same principle applies: an outer rune points **toward the center**.

So, when the route lands on an outer rune of a mirror, the geometry itself can define the direction without choosing it after seeing plaintext.

If the route lands **exactly on the center**, both directions are symmetrical. In the current model, that is where another mechanism becomes relevant: a matching signature or a hidden-key search can point to a related structure, often on the perpendicular axis.

---

# 🔑 3. Two kinds of keys

The route currently contains two different ways of obtaining a key.

### Directly generated key

A mirrored node is already present at the current location:

```text
mirror → φ(center) → key
```

Example:

```text
H — TH — H
φ(TH=2) = 1 = U
H — U — H
```

### Hidden / located key

Sometimes the current stage does not directly contain the next key. Instead, values derived earlier are reused as movement distances and lead to another structure elsewhere in the map:

```text
previous values
     ↓
movement
     ↓
hidden key location
```

An important Volume 1 example is the non-mirrored structure:

```text
H — NG — C
```

An important Volume 2 example is:

```text
NG — B — NG
      ↓ φ
NG — T — NG
```

The current working distinction is:

- **mirrored discovered structure** → transform its center with `φ`;
- **non-mirrored discovered key** → use the discovered structure directly.

The exact general activation rule for every hidden-key search is still being tested, but the individual routes and coordinates can be reproduced from the grid.

---

# 🔁 4. Totient signatures — the same numbers return

For a three-rune key:

```text
K = (k₁, k₂, k₃)
```

I use its totient signature:

```text
σ(K) = (φ(k₁), φ(k₂), φ(k₃))
```

These signatures act like numerical fingerprints between apparently different structures.

A strong example occurs between **COLD** and **I MAY**.

At the endpoint of COLD:

```text
EA — A — EA
```

its signature is:

```text
12 — 8 — 12
```

Later, the hidden structure used for `I MAY` becomes:

```text
NG — T — NG
```

and it has exactly the same signature:

```text
12 — 8 — 12
```

So:

```text
EA — A — EA  →  12 — 8 — 12  ←  NG — T — NG
```

This is what Volume 2 calls **totient inheritance**: a numerical result can remain active beyond the place where it first appeared and re-enter the route later in another role.

---

# 🧮 5. Möbius selects the key phase

A 3-rune key can repeat in three cyclic phases.

For:

```text
K = K₁ K₂ K₃
```

there are three possible starts:

```text
phase 0 → K₁ K₂ K₃ ...
phase 1 → K₂ K₃ K₁ ...
phase 2 → K₃ K₁ K₂ ...
```

The model does **not** choose whichever phase happens to produce readable English.

The phase is calculated first:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

where `μ` is the Möbius function.

This matters because the key rotation is fixed numerically **before the plaintext is evaluated**.

The same phase rule continues through the later route, including `I MAY`, `CRY`, and `NOW THE`.

---

# 🔓 6. Decryption itself is simple

Once the ciphertext path and the active key are known, the actual decryption is ordinary Gematria Primus subtraction:

```text
P = C − K mod 29
```

where:

```text
C = ciphertext rune index
K = active key rune index
P = plaintext rune index
```

The complexity of the model is therefore not mainly in the subtraction. The difficult part is discovering **where to read**, **which structure supplies the key**, and **how the current state leads to the next state**.

---

# 🧩 7. How the plaintext chain grows

The strongest feature of the current route is that the stages are not isolated.

### `AS I GO THE`

```text
AE-J-EA
→ φ(J)=I
→ key AE-I-EA
→ movement 14
→ ciphertext L-AE-N-TH-P-U-X
→ AS I GO THE
```

The final ciphertext rune is `X`, which is immediately part of the next mirror:

```text
X — OE — X
```

### `WEATHER`

```text
X-OE-X
→ φ(OE)=I
→ X-I-X
→ RIGHT 10
→ exact center NG(14,14)
→ WEATHER
```

This is the first strong example of one stage ending directly on the structure that opens the next stage.

### `TURNS`

The route reaches the crossroads `A(14,19)` and reuses the already known values `10` and `4` geometrically. This leads to `H-NG-C`, which becomes the key used to decrypt:

```text
TURNS
```

### `COLD`

The route reaches the mirrored structure:

```text
H — TH — H
```

which becomes:

```text
H — U — H
```

and produces:

```text
COLD
```

At the COLD endpoint, the new structure `EA-A-EA` already contains the `12-8-12` signature that later reappears in the I MAY key.

### `I MAY`

The inherited values from the previous state move through the map to `B(15,8)`, the center of:

```text
NG — B — NG
```

Transforming the center gives:

```text
NG — T — NG
```

with the same `12-8-12` signature. The Möbius rule chooses phase 0, and the preserved `H-TH-H` area decrypts to:

```text
I MAY
```

### `CRY`

The final `E` of the I MAY ciphertext belongs to the next mirror:

```text
E — X — E
```

which becomes:

```text
E — G — E
```

Its signature contains the value `6`:

```text
6 — 2 — 6
```

That same `6` is then reused as movement:

```text
X(25,16) → UP 6 → J(19,16)
```

and the resulting ciphertext decrypts to:

```text
CRY
```

### `NOW THE`

After `CRY`, the endpoint is `S(17,16)`.

Here the number `6` appears again — not only as an inherited value, but as actual geometry:

```text
S(17,4) —6— IA/O(17,10) —6— S(17,16)
```

The center confirms it independently:

```text
IA/O = 27
φ(27) = 18
φ(18) = 6
```

so:

```text
φ²(IA/O) = 6
```

The same center participates in a second radius-6 mirror, allowing the route to transfer to `TH(11,16)`.

From there, the already generated key `OE-I-OE` and its Möbius-selected phase decrypt the next five runes to:

```text
NOW THE
```

This gives the current strongest reading:

<div align="center">

## **AS I GO, THE WEATHER TURNS COLD.**
## **I MAY CRY NOW. THE ...**

</div>

---

# 🧠 The core idea in one sentence

> **The same information keeps changing form: a rune becomes a totient value, a totient value becomes a key or movement, a movement reaches a mirror, the mirror fixes direction, its geometry confirms the number, and the endpoint becomes the beginning of the next stage.**

That is why I currently think the 27×27 object is better understood as a **geometric-cryptographic state machine** than as a conventional linear cipher.

---

# 🧪 Reproduce the mechanics

The repository includes the source data and machine-checkable parts of the research separately from the visual interpretation.

| Resource | Purpose |
|---|---|
| **[🧱 Raw rune source](./other-stuff/0-2-runes.txt)** | The rune sequence used to reconstruct the 27×27 grid |
| **[🗺️ Matrix image](./liber-primus-27x27-matrix.png)** | Visual reference for coordinates, nodes and the current route |
| **[🧪 Volume 1 verifier](./verify_volume_1.py)** | Checks grid shape, coordinates, node transformations, phases and mod-29 arithmetic |
| **[🧪 Volume 2 verifier](./verify_volume_2.py)** | Checks the reproducible I MAY / CRY continuation and inherited-value relations |
| **[📝 Technical Markdown archive](./other-stuff/md/)** | Searchable versions of the research for detailed checking or AI analysis |

Typical verifier use:

```bash
python3 verify_volume_1.py
python3 verify_volume_2.py
```

A successful verifier run means the stated mechanical operations reproduce the documented result from the supplied data. It does **not** by itself establish that the plaintext is the intended official solution to Liber Primus.

---

# 🔭 What remains open

The research is strongest when a transition is fixed by information that already exists **before** the resulting plaintext is inspected.

The main question is therefore:

> **Can every future movement, structure and key be predicted from the current state without introducing a new rule after seeing the plaintext?**

Volume 3 significantly narrows the earlier direction problem by connecting movement to mirror geometry and by showing the inherited value `6` reappearing as a literal radius whose center independently encodes the same value.

The next useful continuation should preserve that standard.

---

<div align="center">

### 📚 **[PDF ARCHIVE](./Read-PDFs-Here/)** · 🜏 **[WHAT IS LIBER PRIMUS?](./WHAT-IS-LIBER-PRIMUS.md)** · 🤖 **[TECHNICAL MARKDOWN](./other-stuff/md/)**

<sub>Independent research into Cicada 3301's Liber Primus · proposed, reproducible where stated, and still under active analysis.</sub>

</div>
