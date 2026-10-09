# 15 — SOON

Two different ciphertexts decrypt to SOON. The first route is shown below; the second is included at the end.

## 1. Locate the node

The YOU key has phase 1. At X(25,16), this gives V₁ = (0, 0). The retained values are L = 20 and H = 8.

Three nodes connect to the EA–EA–EA mirror in row 25:

| First outer | Center | Second outer |
|:---:|:---:|:---:|
| L(25,4) | C(25,7) | EA(25,10) |
| L(15,15) | I(20,15) | EA(25,15) |
| L(25,8) | EO(25,14) | EA(25,20) |

All three centers transform to R, giving the same key: L–R–EA.

## 2. Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | φ(C = 5) = φ(I = 10) = φ(EO = 12) = 4 = R | L–R–EA |
| Totient signature | φ(L = 20) = 8; φ(R = 4) = 2; φ(EA = 28) = 12 | (8, 2, 12) |
| Möbius signature | μ(8) = 0; μ(2) = −1; μ(12) = 0 | (0, −1, 0) |
| Rotation | (0 − 1 + 0) mod 3 = 2 | EA–L–R |
| Movement | H = 8 marks the last rune | X(25,16) → H(25,19) (right 3) |

## 3. Read and decrypt

From X(25,16), read four runes rightward. Subtract the repeating EA–L–R key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (25,16) | X = 14 | EA = 28 | 14 − 28 ≡ 15 | S |
| (25,17) | D = 23 | L = 20 | 23 − 20 ≡ 3 | O |
| (25,18) | W = 7 | R = 4 | 7 − 4 ≡ 3 | O |
| (25,19) | H = 8 | EA = 28 | 8 − 28 ≡ 9 | N |

### SOON

<details>
<summary>Second route — P–S–U–W</summary>

A separate ciphertext also decrypts to SOON.

The same X(25,16) connects E–X–E to E–TH–E through E(24,16). The paths split at TH(23,15):

| Ciphertext path | Key path |
|:---|:---|
| X–TH–X → X(27,11) | D–TH–D → D(22,15) |
| D–X–D → D(27,20) | D–NG–D → D(22,19) |
| P–D–P → P(27,24) | IA–D–IA → IA(22,16) |
| | IA–EA–IA → EA(19,13) |

The IA–EA–IA mirror generates the second key.

### Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | EA = 28; φ(28) = 12 = EO | IA–EO–IA |
| Totient signature | φ(IA = 27) = 18; φ(EO = 12) = 4; φ(IA = 27) = 18 | (18, 4, 18) |
| Möbius signature | μ(18) = 0; μ(4) = 0; μ(18) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | Two connected paths from TH(23,15) | P(27,24) for ciphertext; EA(19,13) for key |

### Read and decrypt

From P(27,24), read four runes rightward. Subtract the repeating IA–EO–IA key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (27,24) | P = 13 | IA = 27 | 13 − 27 ≡ 15 | S |
| (27,25) | S = 15 | EO = 12 | 15 − 12 ≡ 3 | O |
| (27,26) | U = 1 | IA = 27 | 1 − 27 ≡ 3 | O |
| (27,27) | W = 7 | IA = 27 | 7 − 27 ≡ 9 | N |

### SOON

</details>

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Shared totient | φ(5) = φ(8) = φ(10) = φ(12) = 4. The values belong to C, H, I, and EO: three key centers and the ciphertext endpoint. |
| Prime-valued sum | L + H = 73 + 23 = 96; SOON = 53 + 7 + 7 + 29 = 96. |
