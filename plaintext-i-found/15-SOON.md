# 15 — SOON

## 1. Locate the nodes

The YOU key has phase 1. At X(25,16), this gives V₁ = (0, 0), while the totient values are φ(25) = 20 = L and φ(16) = 8 = H. The project's hidden-value rule retains L and H.

The ciphertext X–D–W–H begins at X(25,16) and ends at H(25,19). It lies between EA(25,15) and EA(25,20).

| Node | First outer | Center | Second outer | Radius |
|:---|:---:|:---:|:---:|:---:|
| EA–EA–EA | EA(25,10) | EA(25,15) | EA(25,20) | 5 |
| L–C–EA | L(25,4) | C(25,7) | EA(25,10) | 3 |
| L–I–EA | L(15,15) | I(20,15) | EA(25,15) | 5 |
| L–EO–EA | L(25,8) | EO(25,14) | EA(25,20) | 6 |

The three L–…–EA structures each generate the same key because φ(C = 5) = φ(I = 10) = φ(EO = 12) = 4 = R.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | C, I and EO each transform into R = 4 | L–R–EA |
| Totient signature | φ(L = 20) = 8; φ(R = 4) = 2; φ(EA = 28) = 12 | (8, 2, 12) |
| Möbius signature | μ(8) = 0; μ(2) = −1; μ(12) = 0 | (0, −1, 0) |
| Rotation | (0 − 1 + 0) mod 3 = 2 | EA–L–R |
| Movement | φ(16) = 8 = H | X(25,16) → H(25,19) (right 3) |

## 3. Read and decrypt

From X(25,16), read four runes rightward. Subtract the repeating EA–L–R key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (25,16) | X = 14 | EA = 28 | 14 − 28 ≡ 15 | S |
| (25,17) | D = 23 | L = 20 | 23 − 20 ≡ 3 | O |
| (25,18) | W = 7 | R = 4 | 7 − 4 ≡ 3 | O |
| (25,19) | H = 8 | EA = 28 | 8 − 28 ≡ 9 | N |

## 4. Second route to SOON

A second route starts at the same X(25,16). The shared E(24,16) links E–X–E to E–TH–E. From TH(23,15), one branch locates the ciphertext and the other locates the key.

| Branch | Node | First outer | Center | Second outer |
|:---|:---|:---:|:---:|:---:|
| Shared | E–X–E | E(24,16) | X(25,16) | E(26,16) |
| Shared | E–TH–E | E(22,14) | TH(23,15) | E(24,16) |
| Ciphertext | X–TH–X | X(19,19) | TH(23,15) | X(27,11) |
| Ciphertext | D–X–D | D(27,2) | X(27,11) | D(27,20) |
| Ciphertext | P–D–P | P(27,16) | D(27,20) | P(27,24) |
| Key | D–TH–D | D(22,15) | TH(23,15) | D(24,15) |
| Key | D–NG–D | D(22,15) | NG(22,17) | D(22,19) |
| Key | IA–D–IA | IA(22,16) | D(22,19) | IA(22,22) |
| Key | IA–EA–IA | IA(16,10) | EA(19,13) | IA(22,16) |

The ciphertext branch reaches P(27,24). The key comes from IA–EA–IA.

### Derive the second key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | EA = 28; φ(28) = 12 = EO | IA–EO–IA |
| Totient signature | φ(IA = 27) = 18; φ(EO = 12) = 4; φ(IA = 27) = 18 | (18, 4, 18) |
| Möbius signature | μ(18) = 0; μ(4) = 0; μ(18) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | Connected mirror branches from TH(23,15) | Ciphertext: P(27,24); key center: EA(19,13) |

### Read and decrypt

From P(27,24), read four runes rightward. Subtract the repeating IA–EO–IA key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (27,24) | P = 13 | IA = 27 | 13 − 27 ≡ 15 | S |
| (27,25) | S = 15 | EO = 12 | 15 − 12 ≡ 3 | O |
| (27,26) | U = 1 | IA = 27 | 1 − 27 ≡ 3 | O |
| (27,27) | W = 7 | IA = 27 | 7 − 27 ≡ 9 | N |

## 5. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Complete φ(n) = 4 set | C = 5, H = 8, I = 10 and EO = 12 are the four rune values with φ(n) = 4. Three are key centers; H ends the first ciphertext. |
| Prime-valued sum | L + H = 73 + 23 = 96; S + O + O + N = 53 + 7 + 7 + 29 = 96. |
| Two ciphertexts | X–D–W–H and P–S–U–W use different keys but both decrypt to SOON. |
| Reported uniqueness | The original full-grid scan found each ciphertext once and the EA–EA–EA radius-5 mirror once. |

### SOON
