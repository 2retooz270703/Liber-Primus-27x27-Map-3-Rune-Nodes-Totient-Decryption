# 02 — The Red Heading: A Rectangular `X–N–X–C` Key and the Candidate Reading `SEQUENDI`

*Liber Primus LP2, pages 0–2 · 27×27 rune matrix · Research note dated 29 October 2026*

> **Status: exact rune output `SECUENDI`; proposed Latin reading `SEQUENDI`.**
> The first red word yields eight reproducible plaintext runes when read right
> to left and decrypted with a repeating four-corner key. A geometric condition
> involving the route's opening `J(13,12)` and the original `MAP` source selects
> exactly this rectangle within the tested family. The condition was formulated
> after finding the word candidate; an intended Cicada 3301 solution is not yet
> established.

This note follows [01 — The Red Heading: A Geometric `J–TH–TH` Key and the
Candidate Plaintext `RATIO`](01-Red-Heading-RATIO-Geometric-Key.md). It addresses
the first eight red runes, using a separate key from the one for `RATIO`.
The literal combined output is **`SECUENDI RATIO`**. Under the additional
interpretation of rune `C/K` as Latin `Q`, the proposed heading is
**`SEQUENDI RATIO` — “a method of following.”**

The principal new result is a link between the first word's rectangular key,
the same opening `J` used by the RATIO source, and the three original MAP-key
cells. The plaintext's prime-weight sums also have equal Euler totients,
while their combined sum is prime.

## 1. Fixed input and numerical conventions

The original red heading is:

```text
ᛋᚻᛖᚩᚷᛗᛡᚠ • ᛋᚣᛖᛝᚳ
S–H–E–O–G–M–IA–F • S–Y–E–NG–C
```

It occupies **row 1, columns 1–13** of the project's matrix. The separator is
not a matrix cell. The two original word groups contain **8 and 5 runes**;
their boundary is retained throughout this calculation.

The first word, before reversal, is:

| Position | Matrix cell `(row,column)` | Rune | Transliteration | Rune index |
|---:|:---:|:---:|:---:|---:|
| 1 | (1,1) | ᛋ | S/Z | 15 |
| 2 | (1,2) | ᚻ | H | 8 |
| 3 | (1,3) | ᛖ | E | 18 |
| 4 | (1,4) | ᚩ | O | 3 |
| 5 | (1,5) | ᚷ | G | 6 |
| 6 | (1,6) | ᛗ | M | 19 |
| 7 | (1,7) | ᛡ | IA/IO | 27 |
| 8 | (1,8) | ᚠ | F | 0 |
| **Total** | | | **8 runes** | **96** |

Coordinates are **1-based**, with rows increasing downward and columns to the
right. Cipher arithmetic uses **rune indices 0–28**, not prime weights:

```text
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Rune:   F  U TH  O  R  C  G  W  H  N  I  J EO  P  X  S  T  B  E  M  L NG OE  D  A AE  Y IA EA
```

Euler's totient is written `φ`; the Möbius function is `μ`. **GP**, used in
Section 9, means the sum of the corresponding **prime weights**: index 0
has weight 2, index 1 has weight 3, and so on through index 28 with weight 109.

## 2. The four actual corner cells and their reading order

The candidate key is formed by four existing matrix cells:

| Clockwise order | Corner | Coordinate | Matrix rune | Index |
|---:|---|:---:|:---:|---:|
| 1 | Upper left | **(6,3)** | **X** | **14** |
| 2 | Upper right | **(6,9)** | **N** | **9** |
| 3 | Lower right | **(24,9)** | **X** | **14** |
| 4 | Lower left | **(24,3)** | **C/K** | **5** |

Read the corners **clockwise, starting at the upper-left X**:

```text
X(6,3) → N(6,9) → X(24,9) → C/K(24,3)

Key:        X   N   X   C
Indices:   14   9  14   5
```

The four corner indices are used **directly**. No totient transformation is
applied to any corner rune before subtraction. Although this key contains
only three distinct values, its **repeating period is four**, not three.

This is a new source shape relative to the equally spaced three-rune nodes
used in Note 01. The arithmetic below specifies the selected starting corner
and direction explicitly; it does not assume that the older phase rule has
already established them.

## 3. Reverse the first word, then subtract the repeated key

Reverse the order of the **eight runes**, keeping each rune intact:

```text
Original:  S–H–E–O–G–M–IA–F
Reversed:  F–IA–M–G–O–E–H–S
```

`IA` is one rune, index 27. It remains `IA` when the sequence is reversed;
the operation does not reverse the individual letters of its transliteration.

Repeat the four-rune key twice:

```text
Ciphertext:   F   IA   M   G   O   E   H   S
Key stream:   X    N   X   C   X   N   X   C

Cipher:       0   27  19   6   3  18   8  15
Key:         14    9  14   5  14   9  14   5
Plain:       15   18   5   1  18   9  23  10
```

For zero-based positions `j = 0,…,7`, with the original ciphertext `C` and
`K = (14,9,14,5)`, the complete operation is:

$$
P_j=\bigl(C_{7-j}-K_{j\bmod4}\bigr)\bmod29.
$$

| Read order | Original cell | Reversed cipher | Key | Difference modulo 29 | Plaintext rune |
|---:|:---:|---|---|---|:---:|
| 1 | (1,8) | F = 0 | X = 14 | `0 − 14 ≡ 15` | **S** |
| 2 | (1,7) | IA = 27 | N = 9 | `27 − 9 = 18` | **E** |
| 3 | (1,6) | M = 19 | X = 14 | `19 − 14 = 5` | **C/K** |
| 4 | (1,5) | G = 6 | C = 5 | `6 − 5 = 1` | **U/V** |
| 5 | (1,4) | O = 3 | X = 14 | `3 − 14 ≡ 18` | **E** |
| 6 | (1,3) | E = 18 | N = 9 | `18 − 9 = 9` | **N** |
| 7 | (1,2) | H = 8 | X = 14 | `8 − 14 ≡ 23` | **D** |
| 8 | (1,1) | S = 15 | C = 5 | `15 − 5 = 10` | **I** |

The literal rune output is therefore:

```text
S–E–C–U–E–N–D–I → SECUENDI
```

All eight original ciphertext runes are consumed. No rune is discarded,
inserted, or replaced during the arithmetic. The three negative differences
are corrected by adding 29, giving the index-sum checksum:

$$
96-2(14+9+14+5)+3\times29=96-84+87=99.
$$

The output indices sum to the same **99**. The interpretation of the third
plaintext rune as Latin `Q` is a separate step, discussed in Section 8.

## 4. Connection to the opening J: equal distances to opposite X corners

Let the already recorded opening point be **`J = (13,12)`**. This is the
center of the opening `AE–J–EA` source and the first cell of the diagonal
RATIO source described in Note 01.

The two opposite X corners are:

$$
X_{\mathrm{NW}}=(6,3),\qquad X_{\mathrm{SE}}=(24,9).
$$

Their **squared Euclidean distances** from J are exactly equal:

$$
\lVert J-X_{\mathrm{NW}}\rVert^2
=(13-6)^2+(12-3)^2=7^2+9^2=130,
$$

$$
\lVert J-X_{\mathrm{SE}}\rVert^2
=(24-13)^2+(9-12)^2=11^2+3^2=130.
$$

Thus both X corners lie on the **same circle centered at the pre-existing
J**, with radius **√130**. The distances themselves are not 130; their
squares are 130.

### The rectangle center and the reflection axis

The rectangle's center is a different point:

$$
Q=\frac{(6,3)+(24,9)}2=(15,6).
$$

The matrix rune at Q is `C/K`. J is **not** the rectangle center. Instead,
J lies on the perpendicular bisector of the segment joining the two X corners.
That line is:

$$
\boxed{3r+c=51.}
$$

Indeed, `3×13 + 12 = 51`, and the vectors satisfy:

$$
(X_{\mathrm{SE}}-X_{\mathrm{NW}})\cdot(J-Q)
=(18,6)\cdot(-2,6)=-36+36=0.
$$

Reflection across this line exchanges the two X corners while fixing J.
This is a symmetry of these particular points; it is not a global symmetry
of the square matrix that sends every integer cell to another integer cell.

## 5. Connection to MAP: the original source lies on one side

The project's selected [MAP block](../plaintext-i-found/28-map.md) uses the
original vertical source:

| MAP source role | Coordinate | Rune |
|---|:---:|:---:|
| Upper arm | **(15,9)** | **EO** |
| Center | **(16,9)** | **X** |
| Lower arm | **(17,9)** | **I** |

The rectangle's right side runs from `(6,9)` to `(24,9)`. **All three MAP
source cells lie on that side.** The repeated opposite corner symbol X also
matches the central rune of MAP, rather than merely matching itself.

Furthermore, the side's midpoint is exactly the MAP source's **upper arm**:

$$
\frac{(6,9)+(24,9)}2=(15,9)=\mathrm{EO}(15,9).
$$

The MAP center `X(16,9)` is one row below that midpoint. It must not be
confused with the midpoint itself or with the MAP ciphertext endpoint
`AE(17,13)`.

### Width, totient, and aspect ratio

Measured in steps between cell centers, the rectangle has:

$$
\mathrm{width}=9-3=6,\qquad \mathrm{height}=24-6=18.
$$

The central MAP rune X has index 14, so:

$$
\boxed{\mathrm{width}=6=\varphi(14)
=\varphi(\text{MAP-center rune index}).}
$$

Its **height-to-width ratio is 3:1**. If the boundary cells are counted
inclusively, the enclosed grid region contains **19 rows × 7 columns**;
“18×6” describes coordinate differences, not the number of cells.

Neither the width 6 nor the ratio 3:1 is imposed in the selector in Section 6.
They are additional exact observations about the selected result, not an
established instruction for constructing arbitrary later rectangles.

### Geometry diagram

![The SEQUENDI rectangle, its two equal squared distances from J, and the MAP and RATIO source cells](../assets/discoveries/02-sequendi-rectangle.png)

*The supplied diagram is reproduced unchanged. Gold dashed segments connect
J to the two X corners; blue marks identify the original MAP source and the
previously recorded diagonal RATIO source. The center Q and side midpoint EO
are separate cells.*

## 6. A finite geometric selector and its exact uniqueness claim

There are **123,201 axis-aligned, non-degenerate rectangles** with their four
corners at cell centers in a 27×27 matrix:

$$
\binom{27}{2}\binom{27}{2}=351^2=123201.
$$

This count concerns horizontal/vertical sides and cell-center corners. It
does not include tilted rectangles or rectangles defined on cell boundaries.

### Selection without inspecting N, C, or the word

Keep the opening J and the original MAP source fixed, then apply this recipe:

1. Read the MAP-center symbol, **X**, and collect all cells with that rune.
2. Consider every pair of those cells at every distance; retain pairs whose
   squared distances to **J(13,12)** are equal.
3. Require different rows and different columns, so each pair defines the
   opposite corners of a non-degenerate axis-aligned rectangle.
4. Retain a rectangle only if the **entire three-cell original MAP source**
   lies on one of its sides.

The results are:

| Selection step | Number remaining |
|---|---:|
| X cells in the matrix | **28** |
| Unordered pairs of X cells | **378** |
| Pairs equidistant from fixed J | **6** |
| Non-degenerate rectangles defined by those pairs | **5** |
| Rectangles with all three MAP-source cells on one side | **1** |

The unique result is:

```text
(6,3), (6,9), (24,9), (24,3)
```

The rune values **N and C/K are not tested by the selector**. They are read
from the other two corners only after the coordinates have been selected.
The selector also does not inspect the heading ciphertext, a dictionary, the
desired plaintext, the radius 130, or a prescribed rectangle size.

### The five surviving rectangles before the MAP-side condition

Corner runes are listed clockwise from the upper left. The equal X pair can
occupy either diagonal.

| Top-left and bottom-right coordinates | Corner runes | Equal squared distance to J | Entire MAP source on one side? |
|---|---|---:|:---:|
| (4,6) and (7,21) | X–IA–X–T | 117 | No |
| (6,17) and (8,19) | X–TH–X–NG | 74 | No |
| **(6,3) and (24,9)** | **X–N–X–C** | **130** | **Yes** |
| (7,17) and (8,18) | X–AE–X–NG | 61 | No |
| (19,6) and (20,19) | OE–X–H–X | 85 | No |

The sixth equal-distance pair is `X(3,6)` and `X(3,18)`, both at squared
distance 136. Its points share a row, so it does not define a non-degenerate
rectangle.

### Independent enumeration in the opposite order

The same result was checked by enumerating **all 123,201 rectangles first**,
then testing their source-side relation and both diagonals:

| Check | Count |
|---|---:|
| All axis-aligned rectangles | **123,201** |
| Entire MAP source on one side | **4,290** |
| Their diagonal records, two per rectangle | **8,580** |
| Diagonal records with two X endpoints, without the J condition | **16** |
| Diagonal records equidistant from J, without requiring X | **50** |
| Both conditions together | **1** |

The 4,290 side-compatible rectangles can also be counted directly: 15 choices
for the top row, 11 for the bottom row, and 26 for the other vertical side,
giving `15×11×26 = 4290`. Both left and right sides are allowed; the successful
rectangle was not selected by requiring the MAP node to be on the right.

**Scope of uniqueness:** one rectangle satisfies this particular combination
of anchors, rune equality, metric, and side relation. This is not a claim that
only one interesting rectangle exists under all possible geometric rules.

## 7. How this joins the earlier RATIO geometry

Note 01 starts from the MAP-key center `M = X(16,9)` and its selected
ciphertext endpoint `E = AE(17,13)`. Extending the same displacement once more
gives the RATIO-source center:

$$
R=2E-M=2(17,13)-(16,9)=(18,17).
$$

The opening J then determines the far arm:

$$
2R-J=2(18,17)-(13,12)=(23,22)=\mathrm{TH}.
$$

This gives `J–R–TH`, whose center transformation `φ(4)=2` produces
**`J–TH–TH = (11,2,2)`**. Its Möbius signature is `(1,1,1)`, so its
three-rune phase is 0. Repeating it over the second red word in its original
left-to-right order yields `R–A–T–I–O`.

The two proposed heading keys therefore reuse the same **J/MAP construction**
in different ways:

| Feature | First word | Second word |
|---|---|---|
| Source shape | Four rectangle corners | Equally spaced three-cell diagonal |
| Link to J | Opposite X corners equidistant from J | J is the first source arm |
| Link to MAP | Original MAP node lies on one side | Extend MAP center-to-endpoint displacement |
| Source-derived key | X–N–X–C | J–TH–TH |
| Center totient during key derivation | None | R → TH |
| Ciphertext reading | Right to left | Left to right |
| Literal result | **SECUENDI** | **RATIO** |

Read separately from the printed separator outward, the two words have
opposite directions. This is compatible with the selected calculations,
but a general instruction to read headings this way has not yet been established.
The keys start independently at the word boundary; the entire 13-rune heading
is not reversed or decrypted under one common key.

## 8. Literal output, Latin interpretation, and meaning

The arithmetic produces rune **C/K at index 5**, not a separate Q rune.
Likewise, the fourth output is the ordinary U/V rune at index 1. The literal
transliteration used for the numerical checks is therefore:

```text
SECUENDI RATIO
```

The proposed Latin interpretation is:

```text
SEQUENDI RATIO
```

This reading requires **C/K to represent Latin Q** in this word. The 29-rune
alphabet has no dedicated Q, but that absence alone does not establish this
particular spelling convention. No new numerical value is assigned to Q;
the underlying third rune remains index 5.

In this phrase, **sequendi** is naturally understood as the genitive gerund
of **sequor**, expressing the activity of following or pursuing. With
**ratio** in the sense of a method or procedure, a natural translation is
**“a method of following”**, or **“a method of pursuit”** in a suitable context.
The phrase does not specify an object to follow or independently identify a
particular route through the matrix.

The lexical senses can be checked in Lewis and Short, under
[`sequor`](https://alatius.com/ls/index.php?l=sequor) and
[`ratio`](https://alatius.com/ls/index.php?l=ratio), particularly the latter's
sense II.B.1.c.α for method or procedure. The grammatical interpretation is
separate from the claim that the candidate was intentionally encoded.

## 9. GP sums: equal totients and a prime combined total

All calculations in this section use the **actual recovered rune sequence**,
including C/K = index 5. Prime weights are assigned by rune index; they are
not substituted into the modulo-29 decryption.

### 9.1 The first word

| Recovered rune | Index | GP prime weight |
|:---:|---:|---:|
| S | 15 | 53 |
| E | 18 | 67 |
| C/K | 5 | 13 |
| U/V | 1 | 3 |
| E | 18 | 67 |
| N | 9 | 29 |
| D | 23 | 89 |
| I | 10 | 31 |
| **Total** | **99** | **352** |

$$
\mathrm{GP}(\mathrm{SECUENDI})
=53+67+13+3+67+29+89+31=352.
$$

### 9.2 The second word

| Recovered rune | Index | GP prime weight |
|:---:|---:|---:|
| R | 4 | 11 |
| A | 24 | 97 |
| T | 16 | 59 |
| I | 10 | 31 |
| O | 3 | 7 |
| **Total** | **57** | **205** |

$$
\mathrm{GP}(\mathrm{RATIO})=11+97+59+31+7=205.
$$

### 9.3 Identical Euler totients

The word sums have different factorizations:

$$
352=2^5\times11,\qquad 205=5\times41.
$$

Applying Euler's totient gives:

$$
\varphi(352)=352\left(1-\frac12\right)
\left(1-\frac1{11}\right)=160,
$$

$$
\varphi(205)=205\left(1-\frac15\right)
\left(1-\frac1{41}\right)=160.
$$

Hence:

$$
\boxed{\varphi\!\left(\mathrm{GP}(\mathrm{SECUENDI})\right)
=\varphi\!\left(\mathrm{GP}(\mathrm{RATIO})\right)=160.}
$$

### 9.4 The whole heading has prime GP sum

$$
\boxed{\mathrm{GP}(\mathrm{SECUENDI\ RATIO})=352+205=557,}
$$

and **557 is prime**. Trial division by the primes up to √557 —
`2, 3, 5, 7, 11, 13, 17, 19, 23` — finds no divisor.

The individual word sums **352 and 205 are composite**; their common
totient is 160, while their **combined** sum 557 is prime. References to
`GP(SEQUENDI)` in connection with this candidate mean the same underlying
`S–E–C–U–E–N–D–I` rune encoding, under the stated Q interpretation.

The ordinary **index sum** of the heading is a different total:

$$
99+57=156.
$$

As a complete modulo-29 checksum, the original ciphertext totals 181, the
consumed key stream totals `84+28=112`, and there are three wraparounds:

$$
181-112+3\times29=156.
$$

The GP/totient relationships are exact additional observations. They do not
by themselves identify a cipher, establish the Q convention, or provide an
independent probability that the candidate is intentional.

## 10. What the geometry establishes, and what remains open

### 10.1 Discovery order and conditional uniqueness

The word candidate and its repeating four-rune key were found during an
exploratory lexical/key search. The rectangular source was then located,
and the more specific J/MAP geometric selector was formulated afterward.

The selector can now reproduce the rectangle **without using N, C, or the
word**, but that does not make it a prediction made before the original
search. Its usefulness is that it supplies a precise, falsifiable connection
between existing project anchors and this particular key placement.

### 10.2 A four-rune key is not the established three-rune phase model

The four direct corner indices have the following signature components:

| Key element | Index | `φ(index)` | `μ(φ(index))` |
|:---:|---:|---:|---:|
| X | 14 | 6 | +1 |
| N | 9 | 6 | +1 |
| X | 14 | 6 | +1 |
| C/K | 5 | 4 | 0 |

Their sum is 3. Mechanically retaining the old modulus gives `3 mod 3 = 0`;
changing the modulus to the four-rune key length gives `3 mod 4 = 3`.
There is not yet a justified general rule for choosing between these
extensions or for selecting a four-corner source instead of a three-cell node.

The successful calculation in Section 3 uses the explicitly stated order
**upper-left X, then clockwise**, with no cyclic shift. Calling this merely
“phase 0” would hide the unresolved extension from three-rune to four-rune keys.

### 10.3 Cipher direction and equivalent corner walks

The rectangle selector does not independently prescribe reversal of the
first red word. Both cipher directions, both perimeter directions, and all
four starting corners were checked: **16 configurations** in total.

The literal `SECUENDI` output appears in two equivalent descriptions:

- Start at the **upper-left X**, then walk **clockwise**.
- Start at the **lower-right X**, then walk **counterclockwise**.

Both yield exactly the same numerical key `X–N–X–C`. They are one arithmetic
match, not two independent confirmations. The original left-to-right
ciphertext with this key does not produce the selected word.

### 10.4 Sensitivity to the circle center

Holding the MAP source fixed, the same X-pair/side test was repeated with
every one of the **729 matrix coordinates** as the circle center:

- **705** centers selected no rectangle.
- **24** centers selected one rectangle each.
- Among all **24 cells bearing J**, only the original **J(13,12)** selected
  a rectangle under this test.

Replacing J by the RATIO center `(18,17)`, its far TH arm `(23,22)`, the MAP
center `(16,9)`, MAP ciphertext endpoint `(17,13)`, MAP ciphertext start
`(19,11)`, or matrix center `(14,14)` yielded no selected rectangle.

These are descriptive controls of the stated, retrospectively formulated
rule. They are not a calibrated significance test, and the conditions should
not be multiplied together as if they were independently chosen in advance.

### 10.5 Scope within the larger project

This is a **separate word-level heading candidate**. It is not a demonstration
that the red words are the immediate next ordinary ciphertext blocks after
MAP under Reports 01–08. In particular, Note 01 already records a mismatch
between the RATIO signature and the next sequential signature predicted
after MAP.

The geometric anchors also inherit the status of the proposed route: the
first 17 stages form its original reconstruction, while stages 18–28,
including MAP, are candidate extensions. Exact arithmetic and source-cell
checks do not establish the authenticity or uniqueness of that larger route.

## 11. Verification recipe (standard Python, no external packages)

The following script reads the matrix directly from the supplied project's
`0-2-live-map.html`, checks its numerical fingerprint, selects the rectangle
without inspecting N or C, independently enumerates all axis-aligned
rectangles, verifies the two literal outputs, and checks the GP claims.

Save it as `verify_heading_02.py` and run:

```sh
python verify_heading_02.py /path/to/project.zip
```

It verifies the **stated candidate and geometric family**; it is not an
unconstrained word search or a complete implementation of Reports 00–08.

```python
from itertools import combinations, product
from math import comb, gcd, isqrt
import hashlib
import re
import sys
import zipfile

alphabet = 'F U TH O R C G W H N I J EO P X S T B E M L NG OE D A AE Y IA EA'.split()
index = {r: i for i, r in enumerate(alphabet)}

# Usage: python verify_heading_02.py /path/to/project.zip
with zipfile.ZipFile(sys.argv[1]) as archive:
    name = next(n for n in archive.namelist() if n.endswith('/0-2-live-map.html'))
    page = archive.read(name).decode('utf-8')
table = re.search(r'<table class="rune-grid">(.*?)</table>', page, re.S)[1]
matrix = []
for row in re.findall(r'<tr>(.*?)</tr>', table, re.S):
    runes = re.findall(r'<span class="rune">(.*?)</span>', row)
    if runes:
        matrix.append([index[r.split('/')[0]] for r in runes])
assert len(matrix) == 27 and all(len(r) == 27 for r in matrix)
digest = hashlib.sha256(bytes(v for r in matrix for v in r)).hexdigest()
assert digest == '7878349fef98939f6c816d657547e7e80f1b875d83b28e239c328e67b26159c7'

def value(p):
    return matrix[p[0]-1][p[1]-1]

def d2(a, b):
    return sum((x-y)**2 for x, y in zip(a, b))

def phi(n):
    return sum(gcd(n, k) == 1 for k in range(1, n+1))

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def corners(a, b):
    r1, r2 = sorted((a[0], b[0]))
    c1, c2 = sorted((a[1], b[1]))
    return ((r1, c1), (r1, c2), (r2, c2), (r2, c1))

def on_one_side(rect, points):
    r1, c1 = rect[0]
    r2, c2 = rect[2]
    return any(all(p[axis] == edge and lo <= p[1-axis] <= hi for p in points)
               for axis, edge, lo, hi in [(0, r1, c1, c2), (0, r2, c1, c2),
                                          (1, c1, r1, r2), (1, c2, r1, r2)])

J = (13, 12)
map_source = ((15, 9), (16, 9), (17, 9))
assert [value(p) for p in map_source] == [12, 14, 10]
xs = [p for p in product(range(1, 28), repeat=2) if value(p) == value(map_source[1])]
equal_pairs = [(a, b) for a, b in combinations(xs, 2) if d2(a, J) == d2(b, J)]
rectangles = [corners(a, b) for a, b in equal_pairs if a[0] != b[0] and a[1] != b[1]]
selected = [r for r in rectangles if on_one_side(r, map_source)]
assert (len(xs), len(equal_pairs), len(rectangles), len(selected)) == (28, 6, 5, 1)
assert selected[0] == ((6, 3), (6, 9), (24, 9), (24, 3))
assert comb(27, 2)**2 == 123201

# Independently enumerate every axis-aligned rectangle and both diagonals.
counts = dict(all=0, source_side=0, equal_diagonals=0, X_diagonals=0, both=0)
for r1, r2 in combinations(range(1, 28), 2):
    for c1, c2 in combinations(range(1, 28), 2):
        rect = ((r1, c1), (r1, c2), (r2, c2), (r2, c1))
        counts['all'] += 1
        if not on_one_side(rect, map_source):
            continue
        counts['source_side'] += 1
        for i, j in ((0, 2), (1, 3)):
            a, b = rect[i], rect[j]
            equal = d2(a, J) == d2(b, J)
            both_X = value(a) == value(b) == index['X']
            counts['equal_diagonals'] += equal
            counts['X_diagonals'] += both_X
            counts['both'] += equal and both_X
assert counts == dict(all=123201, source_side=4290, equal_diagonals=50, X_diagonals=16, both=1)

rect = selected[0]
assert d2(rect[0], J) == d2(rect[2], J) == 130
assert tuple((a+b)//2 for a, b in zip(rect[1], rect[2])) == map_source[0]
width = rect[1][1]-rect[0][1]
height = rect[2][0]-rect[1][0]
assert width == phi(value(map_source[1])) == 6 and height == 3*width == 18

key = [value(p) for p in rect]
assert key == [14, 9, 14, 5]
cipher = matrix[0][:8][::-1]
plain1 = [(c-key[i % 4]) % 29 for i, c in enumerate(cipher)]
assert ''.join(alphabet[i] for i in plain1) == 'SECUENDI'
assert sum(plain1) == 96-84+3*29 == 99

ratio_source = ((13, 12), (18, 17), (23, 22))
raw = [value(p) for p in ratio_source]
ratio_key = [raw[0], phi(raw[1]), raw[2]]
assert ratio_key == [11, 2, 2]
plain2 = [(c-ratio_key[i % 3]) % 29 for i, c in enumerate(matrix[0][8:13])]
assert ''.join(alphabet[i] for i in plain2) == 'RATIO' and sum(plain2) == 57

primes = [n for n in range(2, 110) if prime(n)]
assert len(primes) == 29
gp1, gp2 = [sum(primes[i] for i in p) for p in (plain1, plain2)]
assert (gp1, gp2) == (352, 205)
assert phi(gp1) == phi(gp2) == 160
assert gp1+gp2 == 557 and prime(557)
print('Rectangle:', rect, '| Literal heading: SECUENDI RATIO')
print('GP:', gp1, '+', gp2, '=', gp1+gp2, '(prime) | Both totients:', phi(gp1))
print('Verified rectangle counts:', counts)
```

## 12. What would strengthen the candidate?

The next useful tests should be specified before examining their output:

1. **Derive the source shape, corner order, and cipher direction from one
   general rule.** The current geometry selects the rectangle, but the rule
   must also explain when to use four corners rather than a three-cell node.
2. **Resolve the phase extension.** The same procedure should account for
   both the four-rune first key and the three-rune RATIO key, without a
   separately chosen convention for each successful example.
3. **Test the Q interpretation against additional fixed Latin candidates or
   other independently justified rune encodings.** The missing Q rune alone
   is insufficient to establish the spelling convention.
4. **Apply the frozen selection recipe to another predefined target or
   controlled background.** Include negative results and the full set of
   permitted shape, direction, phase, and spelling choices.

## Conclusion

The first red word, reversed by rune order and decrypted with the repeating
corner key **`X–N–X–C`**, yields exactly **`SECUENDI`**. Interpreting C/K as Q
gives the Latin candidate **`SEQUENDI`**; combined with Note 01's RATIO result,
the proposed heading is **`SEQUENDI RATIO` — “a method of following.”**

The rectangle has an exact connection to the opening J and the original MAP
node: its opposite X corners have equal squared distance **130** from J,
the entire MAP source lies on one side, and **EO(15,9)** is that side's
midpoint. Within the explicitly tested family, this selects **one** rectangle
without consulting the other two corner letters or the candidate word.

Its width is **φ(14)=6**, its height-to-width ratio is **3:1**, and the two
literal word GP sums satisfy **φ(352)=φ(205)=160**, with prime combined total
**557**. These verified observations make the candidate worth further tests;
the remaining cipher-direction, four-rune-phase, and Q-spelling choices still
need a general explanation.

---

### Project sources and scope

Checked against the supplied snapshot
`Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption-main(20261029-062428).zip`,
particularly:

- [0-2-live-map.html](../0-2-live-map.html) — the 729-rune matrix and source-cell annotations.
- [01 — AS I GO, THE](../plaintext-i-found/01-as-i-go-the.md) — the opening source and J(13,12).
- [28 — MAP](../plaintext-i-found/28-map.md) — the original EO–X–I source and selected ciphertext endpoint.
- [Discovery 01 — RATIO](01-Red-Heading-RATIO-Geometric-Key.md) — the separate three-rune heading key and its scope.
- [Report 00 — Decryption method](../Start-reading-here/00-decryption-method.md) — the original index, totient, signature, and phase definitions.

The SHA-256 of the matrix's 729 indices serialized as one byte per index is:

```text
7878349fef98939f6c816d657547e7e80f1b875d83b28e239c328e67b26159c7
```

The attached English geometry diagram is stored as
`assets/discoveries/02-sequendi-rectangle.png` relative to the repository root
and is reproduced without editing.

### Lexical references

- Lewis, C. T., and Short, C. *A Latin Dictionary*. Entry [sequor](https://alatius.com/ls/index.php?l=sequor).
- Lewis, C. T., and Short, C. *A Latin Dictionary*. Entry [ratio](https://alatius.com/ls/index.php?l=ratio), especially II.B.1.c.α.

The lexical references support the proposed Latin interpretation; they do not
authenticate the cryptographic or geometric hypothesis.
