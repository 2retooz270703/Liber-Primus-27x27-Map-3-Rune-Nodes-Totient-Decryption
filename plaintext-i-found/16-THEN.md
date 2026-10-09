# 16 — THEN

## 1. Locate the node

The SOON key has phase 2. At H(25,19), this gives V₂ = (0, +1) → RIGHT. The retained values are φ²(25) = 8 and φ²(19) = 6.

| Row | Column 19 | Column 22 | Column 25 | Column 26 | Column 27 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 25 | H | IA | L | T | W |
| 26 | | IA | | | |
| 27 | | IA | | | |

RIGHT 6 reaches L(25,25); RIGHT 8 reaches W(25,27). IA(25,22) is halfway to L and belongs to the vertical IA–IA–IA mirror.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | IA = 27; φ(27) = 18 = E | IA–E–IA |
| Totient signature | φ(IA = 27) = 18; φ(E = 18) = 6; φ(IA = 27) = 18 | (18, 6, 18) |
| Möbius signature | μ(18) = 0; μ(6) = +1; μ(18) = 0 | (0, +1, 0) |
| Rotation | (0 + 1 + 0) mod 3 = 1 | E–IA–IA |
| Movement | φ²(25) = 8; φ²(19) = 6 | H → L (right 6); H → W (right 8) |

## 3. Read and decrypt

From L(25,25), read three runes rightward. Subtract the E–IA–IA key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (25,25) | L = 20 | E = 18 | 20 − 18 ≡ 2 | TH |
| (25,26) | T = 16 | IA = 27 | 16 − 27 ≡ 18 | E |
| (25,27) | W = 7 | IA = 27 | 7 − 27 ≡ 9 | N |

### THEN

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Shared endpoint mirror | W(25,27)–NG(26,27)–W(27,27) connects the end of THEN to the secondary SOON route. |
| Matching phase | W–NG–W → W–EO–W gives (6, 4, 6) → (+1, 0, +1), phase 2. At W(25,27), T₂ = (8, 6) and V₂ = (0, +1), as at H(25,19). |
| Totient sum | SEE + YOU + SOON = 51 + 30 + 30 = 111; φ(111) = 72 = 18 + 27 + 27, the sum of E–IA–IA. |
