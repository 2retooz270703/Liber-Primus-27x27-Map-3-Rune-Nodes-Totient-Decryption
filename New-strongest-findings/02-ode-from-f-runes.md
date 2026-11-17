# Report 02 — ODE in the Three ᚠ Runes

**Liber Primus, LP2 pages 0–2 · The 27 × 27 map · 17 November 2026**

The proposed 38-block route reads exactly **three** ciphertext ᚠ runes. Take the plaintext letter produced at each of those cells and read the letters in the original order of the pages. They spell **ODE**. Every ᚠ visited by the route contributes, and ordinary page order determines the sequence. The extraction is especially notable because ᚠ already has a documented role in solved Cicada ciphers.

## 1. Recovering ODE

Coordinates are one-based `(row, column)` pairs. The position of a cell in the original text is $n_0(r,c)=27(r-1)+c$. The recorded route reads 115 ciphertext positions, counting repeated visits. The full grid contains 34 instances of ᚠ, and the route visits exactly three of them. Each of these visits uses the block’s aligned key and the standard subtraction modulo 29. [Decryption method](../Start-reading-here/00-decryption-method.md) · [Interactive map](../0-2-live-map.html)

| Page-order position | Grid cell | Block | Place in block | Applied key | Subtraction modulo 29 | Output |
| ---: | --- | --- | --- | --- | --- | :---: |
| **190** | `(8,1)` | [35 · GO](../plaintext-i-found/35-go.md) | Last | Y (26) | $0-26\equiv3$ | **O** |
| **253** | `(10,10)` | [32 · DEATH](../plaintext-i-found/32-death.md) | First | G (6) | $0-6\equiv23$ | **D** |
| **509** | `(19,23)` | [11 · END](../plaintext-i-found/11-end.md) | First | J (11) | $0-11\equiv18$ | **E** |

In block order, the visits run through **END → DEATH → GO** and yield **EDO**. In the original page order, the same cells occur at **190 → 253 → 509** and yield **ODE**. The route supplies the cells and their decrypted values. Page order supplies the order of the letters.

To reproduce the extraction, record the coordinate and decrypted rune index at every step of the 38-block route. Keep all visits whose **ciphertext** rune is ᚠ, sort them by $n_0$, and transliterate the resulting plaintext indices. The expected result is `[3, 23, 18]`, or **O · D · E**.

## 2. Why ᚠ matters here

On the solved page **AN END** (LP2 p56, scan 73), the cipher subtracts the totients of successive primes. The 57th rune is ᚠ, stays **F** in **OF**, and leaves the next keystream value available for the following rune. The other four ciphertext ᚠ runes undergo ordinary subtraction. The glyph therefore has a documented relationship to the use of the keystream. [Page 56 transcription](https://github.com/Wulfic/Cicada3301-Liber_Primus/blob/main/pages/page_73/runes.txt) · [Page 56 solution](https://github.com/Wulfic/Cicada3301-Liber_Primus/blob/main/pages/page_73/README.md)

In the proposed pages 0–2 route, all three selected ᚠ runes consume their aligned key components. Each one also sits on a block boundary. The known exception on p56 gives a reason to examine ᚠ specifically, while the candidate route gives the three letters by its ordinary arithmetic. As a comparison, extracting the outputs of all five ᚠ runes on p56 in page order yields **AIDFC**. Extracting the four that undergo subtraction yields **AIDC**.

## 3. Testing ODE against alternative keys

For each of the three transitions, fix the preceding block and its state from the recorded route. Hold the incoming ciphertext segment fixed and enumerate key assignments that satisfy the transition rules **00–15**. Each assignment specifies a source node, its reading orientation, and its center operation when distinct. The search uses the documented key phase and the cyclic phase schedule, with no plaintext dictionary filter on the blocks.

| Block | Incoming state `(S, a)` | Possible outputs at ᚠ | Compatible assignments | Assignments giving the ODE letter |
| --- | :---: | --- | ---: | ---: |
| **GO (35)** | `(28, 0)` | O, TH | 2 | **1** |
| **DEATH (32)** | `(24, 0)` | AE, D, Y | 26 | **12** |
| **END (11)** | `(9, 1)` | E, IA, L | 5 | **3** |

The three output sets give **18 distinct rune triples** in page order. **ODE** is the only complete entry in the tested English Hunspell word list. Among the $2\times26\times5=260$ combinations of local assignments, $1\times12\times3=36$ produce **ODE**. These counts apply to three separate searches with the recorded incoming states. They measure how the word narrows the available choices within the model.

Requiring **O** at `(8,1)` selects the exact recorded reading **GO** from the two compatible assignments for that segment. Allowing the segment to vary while keeping ᚠ as its endpoint leaves **three of eight** assignments with **O**. The fixed-segment searches for **DEATH** and **END** retain multiple keys even after requiring their ODE letters. A comparison across the other ciphertext runes read exactly three times in distinct cells also yields **GEE** from ciphertext **O**. The special role of ᚠ and the page-order extraction are what make **ODE** the result of interest.

## 4. A possible address to the reader

An **ode** is a lyric poem that addresses and often celebrates its subject. That sense fits a striking feature of the proposed main text. The speaker turns toward a reader with “See you soon, then” and ends with a request to that reader, “Go, do as I ask.” If **ODE** was placed deliberately, it could name a poem or tribute addressed to the person following the route. The extraction gives the word itself, and the proposed text supplies the possible addressee. [Meaning of *ode*](https://www.poetryfoundation.org/education/glossary/ode) · [Proposed text](../README.md#plaintext)

The result gives a concrete test for future route searches. Fix **ODE** as the target before the search, withhold the three block placements, and check whether the extracted letters in page order recover the documented continuation among other admissible routes. The present enumeration establishes exactly what the word selects when the recorded segments and preceding states are supplied. [Report 01 and the recovery of I ASK](01-3301-constraints.md)
