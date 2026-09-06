# Cicada 3301 Liber Primus 0–2 — 27×27 Rune Matrix Decryption

A proposed cryptanalytic framework for **Cicada 3301's Liber Primus, pages 0–2**.

The central observation is simple:

> Pages 0–2 contain exactly **729 rune tokens**, and `729 = 27 × 27`.

The rune sequence can therefore be arranged, without adding or removing anything, as a **27×27 grid**.  
This project explores the possibility that the grid is not only ciphertext, but also a spatial structure in which **3-rune nodes, Euler totients, Möbius phases, and movement through the grid** work together.

**Status:** proposed and reproducible research; not an officially verified Cicada 3301 solution.

---

## Read the research

### Volume 1

**Visual / reader-friendly version**

[📄 SOLUTION 0-2 volume 1.pdf](./SOLUTION%200-2%20volume%201.pdf)

**Technical / AI-readable version**

[📝 SOLUTION-0-2-volume-1.md](./SOLUTION-0-2-volume-1.md)

Volume 1 develops the 27×27 framework and follows the route through the first major plaintext sequence.

### Volume 2

**Visual / reader-friendly version**

[📄 SOLUTION 0-2 volume 2.pdf](./SOLUTION%200-2%20volume%202.pdf)

**Technical / AI-readable version**

[📝 SOLUTION-0-2-volume-2.md](./SOLUTION-0-2-volume-2.md)

Volume 2 continues the analysis beyond Volume 1 and focuses on **totient inheritance, hidden-key discovery, mirrored-node behavior, and continuation of the route**.

---

## Core idea

The working structure can be summarized as:

```text
729 rune tokens
        ↓
27×27 grid
        ↓
3-rune structures / nodes
        ↓
Euler totient φ
        ↓
key generation + numerical signatures
        ↓
Möbius μ
        ↓
key phase
        ↓
movement through the grid
        ↓
Gematria Primus subtraction mod 29
        ↓
plaintext
        ↓
next structure
```

The important idea is that the stages are **connected**.

A value produced at one point may later reappear as a movement distance or help locate another key. Some keys are generated directly from 3-rune nodes, while others appear to be found indirectly through **totient-guided movement**.

The exact general rule controlling every transition is still under investigation.

---

## Key structural rules

### Mirrored 3-rune nodes

A recurring transformation is:

```text
a-b-a  →  a-φ(b)-a
```

The center of a mirrored node is transformed with Euler's totient function and can generate a key.

### Möbius key phase

For a 3-rune key `K`, its totient values are used to determine the cyclic key phase:

```text
p = Σ μ(φ(Kᵢ)) mod 3
```

### Grid movement

Totient-derived values can also act as **movement distances** in the 27×27 grid.

In the current model, this can connect one structure to another and, in some cases, reveal a hidden key.

### Decryption

Rune values use **0-based Gematria Primus**, with plaintext calculated by:

```text
P = C - K mod 29
```

---

## Repository files

| File | Purpose |
|---|---|
| [`SOLUTION 0-2 volume 1.pdf`](./SOLUTION%200-2%20volume%201.pdf) | Visual Volume 1 |
| [`SOLUTION-0-2-volume-1.md`](./SOLUTION-0-2-volume-1.md) | Technical Volume 1 |
| [`SOLUTION 0-2 volume 2.pdf`](./SOLUTION%200-2%20volume%202.pdf) | Visual Volume 2 |
| [`SOLUTION-0-2-volume-2.md`](./SOLUTION-0-2-volume-2.md) | Technical Volume 2 |
| [`liber-primus-0-2-729-runes.txt`](./liber-primus-0-2-729-runes.txt) | Raw 729-rune dataset |
| [`liber-primus-27x27-matrix.png`](./liber-primus-27x27-matrix.png) | 27×27 grid visualization |
| [`verify-volume-1.py`](./verify-volume-1.py) | Volume 1 reproducibility checks |
| [`WHAT-IS-LIBER-PRIMUS.md`](./WHAT-IS-LIBER-PRIMUS.md) | Conceptual interpretation of the model |

---

## Reproducibility

The raw rune data is included in the repository, and the main arithmetic operations are explicitly documented.

Volume 1 also includes a Python verifier:

```bash
python3 verify-volume-1.py
```

A successful verification confirms that the encoded coordinates, totient transformations, Möbius phases, key streams, and mod-29 calculations reproduce the stated results.

It does **not** by itself prove that the proposed plaintext is the intended Cicada 3301 solution.

---

## Current direction

The main open problem is no longer only whether readable plaintext can be produced.

The stronger test is whether the same structural rules can **predict the next route and key before the plaintext is known**.

That is the focus of the continuing analysis.
