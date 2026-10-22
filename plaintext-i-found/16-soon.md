# 16 — SOON

This example continues from **YOU**. Two different four-rune ciphertexts decrypt as **SOON**. Both routes begin at **`X (25,16)`**, the final ciphertext cell of **YOU**, but they use different keys and different reading paths.

The **main route** derives the same key from three separate mirrors in row 25. An **alternative route**, preserved below, follows connected mirrors to a second ciphertext and key.

**Notation:** Coordinates are **1-based** and written `(row, column)`. Rune numbers are indices in the **29-rune alphabet**. `φ` denotes Euler's totient function; `μ` denotes the Möbius function. `GP` means **Gematria Primus**, which uses prime values rather than rune indices.

## 1. Find the connected three-rune nodes

The **YOU** ciphertext ends at **`X (25,16)`**. Its key, `TH–P–P`, has **rotation phase 1**. Under the project's direction convention, this gives:

`V₁ = (0, 0)`

This is a **zero vector**: it does not determine a reading direction. The proposed main route therefore uses additional structure in the matrix.

Apply `φ` to the endpoint's row and column numbers:

- `φ(25) = 20` → rune **`L`**.
- `φ(16) = 8` → rune **`H`**.

Row 25 also contains three `EA` runes at **`(25,10)`**, **`(25,15)`**, and **`(25,20)`**. These form an equally spaced horizontal triple, with **`EA (25,15)`** at its center and a radius of **5 cells**.

More importantly for this decryption, each `EA` is an outer endpoint of a **different** `L–center–EA` mirror:

| Mirror | First endpoint | Center | Second endpoint | Radius |
|:---|:---:|:---:|:---:|:---:|
| `L–C–EA` | L (25,4) | **C (25,7)** | EA (25,10) | 3 horizontal cells |
| `L–I–EA` | L (15,15) | **I (20,15)** | EA (25,15) | 5 vertical cells |
| `L–EO–EA` | L (25,8) | **EO (25,14)** | EA (25,20) | 6 horizontal cells |

The three mirrors have **different positions and radii**, but their center runes produce the **same value** under `φ`. This gives a common key without requiring the three centers to lie in one node.

## 2. Derive and align the decryption key

### Replace the center runes

Keep `L` and `EA` as the outer runes of each mirror. Apply `φ` to each original center:

| Original mirror | Center calculation | Derived key |
|:---|:---|:---|
| `L–C–EA` | `C = 5 → φ(5) = 4 → R` | `L–R–EA` |
| `L–I–EA` | `I = 10 → φ(10) = 4 → R` | `L–R–EA` |
| `L–EO–EA` | `EO = 12 → φ(12) = 4 → R` | `L–R–EA` |

**All three mirrors generate the same unrotated key: `L–R–EA`.**

### Calculate its rotation

Apply `φ` to each derived key rune, then `μ` to its totient value:

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| L | 20 | φ(20) = 8 | μ(8) = 0 |
| R | 4 | φ(4) = 2 | μ(2) = −1 |
| EA | 28 | φ(28) = 12 | μ(12) = 0 |

The **totient signature** is `(8, 2, 12)` and the **Möbius signature** is `(0, −1, 0)`.

The Möbius sum determines the number of cyclic left rotations:

`Rotation = (0 − 1 + 0) mod 3 = 2`

Apply **two cyclic left rotations**:

`L–R–EA → R–EA–L → EA–L–R`

**Final repeating key: `EA–L–R`.**

## 3. Locate the ciphertext start and endpoint

The main route starts directly at the final ciphertext cell of **YOU**, **`X (25,16)`**, then reads **rightward along row 25**.

The endpoint-derived value `φ(16) = 8` corresponds to rune `H`. On this row, the selected `H` is at **`(25,19)`**, three cells to the right:

`X (25,16) → D (25,17) → W (25,18) → H (25,19)`

Thus, the selected ciphertext has **four runes** and ends at **`H (25,19)`**. The equality `φ(16) = H = 8` is a numerical connection to that endpoint. Since `V₁ = (0,0)` does not specify a direction, the **rightward choice and length are not uniquely determined by the vector alone**.

## 4. Read and decrypt the ciphertext

Subtract each key rune index from the corresponding ciphertext rune index, **modulo 29**. Repeat `EA–L–R` as necessary:

`Plaintext index = (ciphertext index − key index) mod 29`

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (25,16) | X = 14 | EA = 28 | 14 − 28 ≡ 15 | **S** |
| (25,17) | D = 23 | L = 20 | 23 − 20 ≡ 3 | **O** |
| (25,18) | W = 7 | R = 4 | 7 − 4 ≡ 3 | **O** |
| (25,19) | H = 8 | EA = 28 | 8 − 28 ≡ 9 | **N** |

## Result

**Decrypted rune sequence:** `S · O · O · N`

**Proposed reading: SOON**

All four modular subtractions are correct for the selected ciphertext and rotated key. The common key from three distinct mirrors is an additional structural correspondence; it does not by itself prove that this ciphertext route is unique.

## Alternative route — P–S–U–W

<details>
<summary>Expand the second route to SOON</summary>

This route also begins at **`X (25,16)`**, but decrypts the different ciphertext **`P–S–U–W`** in row 27. Its key is **`IA–EO–IA`**, not `EA–L–R`.

### 1. Reach the branching node

From the previous endpoint, the selected path moves through **`E (24,16)`** to **`TH (23,15)`**:

`X (25,16) → E (24,16) → TH (23,15)`

At `TH (23,15)`, the route splits: one chain of mirrors locates the **ciphertext**, and another locates the **key-generating node**.

### 2. Follow the two mirror chains

| Branch | Mirror | Movement between connected cells | Geometric basis |
|:---|:---|:---|:---|
| Ciphertext | `X–TH–X` | TH (23,15) → X (27,11) | 4 diagonal steps down-left; other X is at (19,19) |
| Ciphertext | `D–X–D` | X (27,11) → D (27,20) | 9 cells right; other D is at (27,2) |
| Ciphertext | `P–D–P` | D (27,20) → P (27,24) | 4 cells right; other P is at (27,16) |
| Key | `D–TH–D` | TH (23,15) → D (22,15) | 1 cell up; other D is at (24,15) |
| Key | `D–NG–D` | D (22,15) → D (22,19) | 4 cells right through NG (22,17) |
| Key | `IA–D–IA` | D (22,19) → IA (22,16) | 3 cells left; other IA is at (22,22) |
| Key | `IA–EA–IA` | IA (22,16) → EA (19,13) | 3 diagonal steps up-left; other IA is at (16,10) |

The **ciphertext branch** ends at **`P (27,24)`**. The **key branch** ends at **`EA (19,13)`**, the center of the diagonal `IA–EA–IA` mirror.

These mirror relations specify a traceable geometric route. The selection of this path at each intersection is part of the proposed construction.

### 3. Derive and align the alternative key

Keep the two outer `IA` runes. Transform the center of `IA–EA–IA`:

`EA = 28 → φ(28) = 12 → EO`

The unrotated key is **`IA–EO–IA`**.

| Key rune | Rune index | Totient | Möbius value |
|:---:|:---:|:---:|:---:|
| IA | 27 | φ(27) = 18 | μ(18) = 0 |
| EO | 12 | φ(12) = 4 | μ(4) = 0 |
| IA | 27 | φ(27) = 18 | μ(18) = 0 |

The **totient signature** is `(18, 4, 18)` and the **Möbius signature** is `(0, 0, 0)`.

`Rotation = (0 + 0 + 0) mod 3 = 0`

**Final repeating key: `IA–EO–IA`.** No rotation is needed.

### 4. Read and decrypt the alternative ciphertext

From **`P (27,24)`**, read **four cells rightward** to the edge of row 27:

`P (27,24) → S (27,25) → U (27,26) → W (27,27)`

Apply the repeating key `IA–EO–IA` and subtract **modulo 29**:

| Cell | Ciphertext | Key | Calculation (mod 29) | Decrypted rune |
|:---:|:---:|:---:|:---:|:---:|
| (27,24) | P = 13 | IA = 27 | 13 − 27 ≡ 15 | **S** |
| (27,25) | S = 15 | EO = 12 | 15 − 12 ≡ 3 | **O** |
| (27,26) | U = 1 | IA = 27 | 1 − 27 ≡ 3 | **O** |
| (27,27) | W = 7 | IA = 27 | 7 − 27 ≡ 9 | **N** |

**Decrypted rune sequence:** `S · O · O · N`

**Proposed reading: SOON**

The arithmetic is correct for this second ciphertext and key as well. The fact that two selected routes produce the same word is noteworthy, but does not establish that either route was uniquely prescribed.

</details>

## 5. Numerical and geometric connections

### Shared starting cell with YOU

**YOU** ends at **`X (25,16)`**, and **both routes to SOON** start from that cell or use it as their initial anchor. The main route immediately reads from `X`; the alternative route reaches its ciphertext after traversing connected mirrors.

### A shared totient value

The three key-generating mirror centers and the final rune of the **main** ciphertext share a totient value:

`φ(C = 5) = φ(I = 10) = φ(EO = 12) = φ(H = 8) = 4`

For the three mirror centers, this gives **`R = 4`** in the unrotated key. For `H (25,19)`, it is an additional numerical match, not a separate decryption instruction.

### Gematria Primus equality

Using **Gematria Primus prime values** rather than rune indices:

| Expression | Calculation | Total |
|:---|:---|:---:|
| `L + H` | 73 + 23 | **96** |
| `SOON` | S (53) + O (7) + O (7) + N (29) | **96** |

Therefore, **`GP(L) + GP(H) = GP(SOON) = 96`**.

This equality is exact. The number **96 itself is not prime**; the calculation is a sum of prime-valued rune weights. It is an additional numerical observation, not an independent proof of the plaintext or the route.
