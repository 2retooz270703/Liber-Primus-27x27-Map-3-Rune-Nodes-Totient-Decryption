# Cicada 3301 Liber Primus 0–2
## 27×27 Rune Grid / Totient Decryption Framework

# Current progress

| Item | Current result |
|---|---|
| **Plaintext found** | **10 proposed words** |
| **Volume 1** | 7 words |
| **Volume 2** | +3 words |
| **Current strongest plaintext** | **AS I GO, THE WEATHER TURNS COLD. I MAY CRY...** |
| **Grid** | 729 runes arranged as **27×27** |
| **Main mechanism** | mirrored 3-rune nodes + Euler totient + Möbius phase + grid movement |
| **New Volume 2 finding** | totient values can persist and later act as movement instructions that lead to hidden keys |
| **Current open problem** | make every movement / transition fully deterministic before plaintext is known |

The strongest result so far is not only the plaintext itself, but the repeated structural behavior behind it: **mirrored nodes, totient-derived values, key generation, phase selection, and movement through the grid appear to form one connected process.**

---
<!-- Add current route / progress image here -->

---

# About this project

A proposed cryptanalytic model for **Liber Primus pages 0–2**.

Pages 0–2 contain exactly **729 rune tokens**:

`729 = 27 × 27`

Keeping the original rune order and placing the runes row by row creates a **27×27 grid**.

The working hypothesis is that this grid behaves not only as ciphertext, but also as a **map**: 3-rune structures generate or reveal keys, Euler totients produce numerical control values, the Möbius function determines key phase, and some of those values can later be reused as movement distances through the grid.

> **Status:** proposed and reproducible research, not an officially verified Cicada 3301 solution.

---

# Start here

| | Human-readable / visual | Technical / AI-readable |
|---|---|---|
| **Volume 1** | [SOLUTION 0-2 volume 1.pdf](./SOLUTION%200-2%20volume%201.pdf) | [SOLUTION-0-2-volume-1.md](./SOLUTION-0-2-volume-1.md) |
| **Volume 2** | [SOLUTION 0-2 volume 2.pdf](./SOLUTION%200-2%20volume%202.pdf) | [SOLUTION-0-2-volume-2.md](./SOLUTION-0-2-volume-2.md) |

**First time here?** Read the PDFs. They show the grid, routes, nodes, and key locations visually.

**Checking the method, reproducing calculations, or giving the research to an AI?** Use the Markdown versions.

- **Volume 1** establishes the 27×27 framework and the main decryption route.
- **Volume 2** continues the route and develops the ideas of **totient inheritance** and **hidden-key discovery**.

For the conceptual interpretation of the system, see [`WHAT-IS-LIBER-PRIMUS.md`](./WHAT-IS-LIBER-PRIMUS.md).

---

# How the model works

The proposed process is a loop:

```text
729 runes in original order
          ↓
      27×27 grid
          ↓
 find a 3-rune structure
          ↓
 generate / locate a key
          ↓
 Euler totient φ produces
 key values and signatures
          ↓
 Möbius μ selects key phase
          ↓
 Gematria Primus subtraction mod 29
          ↓
       plaintext
          ↓
 derived values / geometry
 lead to the next structure
          ↺
```

The important idea is that **the arithmetic and the geometry are connected**. A value obtained at one stage can remain relevant later instead of being discarded.

---

# 1. The 27×27 grid

The 729 runes are placed **left-to-right, row-by-row**, preserving their original order.

This gives every rune a fixed coordinate `(row, column)` and allows the ciphertext to be treated as a spatial structure.

Raw data:

[`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt)

Visual grid:

[`liber-primus-27x27-matrix.png`](./liber-primus-27x27-matrix.png)

---

# 2. 3-rune nodes

The grid contains recurring 3-rune structures that act as functional nodes.

A particularly important form is a mirrored node:

```text
a - b - a
```

For mirrored nodes, the center is transformed through Euler's totient:

```text
a-b-a  →  a-φ(b)-a
```

The transformed structure can become a cipher key.

This is one of the main recurring operations of the model.

---

# 3. Two ways keys appear

The current research shows two different key mechanisms.

### Directly generated keys

A mirrored 3-rune node generates a key by applying `φ` to its center.

```text
mirrored node
      ↓
 φ(center)
      ↓
     key
```

### Hidden / located keys

Some keys are not generated directly at the current node.

Instead, **specific totient values already obtained in the route are reused as movement distances**. Those movements lead to another location in the grid where the next key or key-structure is found.

```text
known totient values
        ↓
 movement in the grid
        ↓
 hidden key location
```

If the discovered structure is **mirrored**, its center is transformed with `φ` before use.

If the discovered key is **non-mirrored**, it is used directly.

The examples are reproducible in the current route, but the exact general rule that determines **when hidden-key search is activated** is still unresolved.

---

# 4. Totient signatures and inheritance

For a 3-rune key:

```text
K = (k1, k2, k3)
```

its totient signature is:

```text
σ(K) = (φ(k1), φ(k2), φ(k3))
```

These numbers can have more than one role.

In the current model they can participate in:

- identifying related structures;
- determining key phase;
- defining movement distances;
- locating later keys.

Volume 2 refers to this repeated reuse of previously derived values as **totient inheritance** or a **totient chain**.

This does **not** mean every totient value is always reused. The observed claim is narrower: specific values recur at important transitions and connect separate parts of the grid.

---

# 5. Möbius key phase

Once a 3-rune key is known, its cyclic phase is determined numerically rather than chosen by whichever rotation produces readable English.

The proposed phase rule is:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

where `μ` is the Möbius function.

The result `p ∈ {0,1,2}` selects one of the three cyclic rotations of the key.

```text
phase 0: K1 K2 K3
phase 1: K2 K3 K1
phase 2: K3 K1 K2
```

---

# 6. Decryption

Rune values use **0-based Gematria Primus**.

Decryption is:

```text
P = C - K mod 29
```

where:

- `C` = ciphertext rune value
- `K` = active key rune value
- `P` = plaintext rune value

The resulting plaintext is not treated as the end of the process. Its endpoint, surrounding geometry, and already derived numerical values can lead to the next node or key.

That feedback loop is the central idea of the proposed framework.

---

# Algorithm at a glance

```text
SOURCE
729 rune tokens
      │
      ▼
27×27 GRID
fixed coordinates
      │
      ▼
STRUCTURE
3-rune node / geometric relation
      │
      ├──────── mirrored node ────────┐
      │                               ▼
      │                         φ(center)
      │                               │
      │                               ▼
      │                              KEY
      │
      └──── totient-guided movement ──► hidden key
                                      │
                                      ▼
                              TOTIENT SIGNATURE
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
                    Möbius phase             grid movement
                         │                         │
                         ▼                         │
                    active key                    │
                         │                         │
                         ▼                         │
                 GP subtraction mod 29            │
                         │                         │
                         ▼                         │
                     plaintext                    │
                         │                         │
                         └──── next structure ◄────┘
```

---

# Repository guide

| File | What it is for |
|---|---|
| [`SOLUTION 0-2 volume 1.pdf`](./SOLUTION%200-2%20volume%201.pdf) | Visual, reader-friendly Volume 1 |
| [`SOLUTION-0-2-volume-1.md`](./SOLUTION-0-2-volume-1.md) | Exact technical / machine-readable Volume 1 |
| [`SOLUTION 0-2 volume 2.pdf`](./SOLUTION%200-2%20volume%202.pdf) | Visual, reader-friendly Volume 2 |
| [`SOLUTION-0-2-volume-2.md`](./SOLUTION-0-2-volume-2.md) | Exact technical / machine-readable Volume 2 |
| [`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt) | Raw 729-rune source dataset |
| [`liber-primus-27x27-matrix.png`](./liber-primus-27x27-matrix.png) | Visual reference for the 27×27 grid |
| [`verify-volume-1.py`](./verify-volume-1.py) | Reproducibility checks for the Volume 1 core |
| [`WHAT-IS-LIBER-PRIMUS.md`](./WHAT-IS-LIBER-PRIMUS.md) | Conceptual explanation of the proposed architecture |

---

# Reproducibility

Volume 1 includes a Python verifier:

```bash
python3 verify-volume-1.py
```

No third-party packages are required.

The verifier checks the encoded core of the proposal: grid size, coordinates, node locations, totient transformations, Möbius phases, key streams, and mod-29 arithmetic.

A successful run shows that the documented operations reproduce the documented result from the repository data.

It does **not** by itself prove that the model is the intended Cicada 3301 solution.

---

# What remains open

The strongest unresolved question is not whether the framework can produce readable plaintext.

It is whether the complete transition logic can be made **fully deterministic**:

> Can the next movement, node, and key be predicted from the existing state **before the next plaintext is known**?

In particular, the rule controlling when totient-derived values become movement instructions is still being investigated.

For the actual routes, coordinates, plaintext, and evidence, read **Volume 1** and **Volume 2** rather than this README.
