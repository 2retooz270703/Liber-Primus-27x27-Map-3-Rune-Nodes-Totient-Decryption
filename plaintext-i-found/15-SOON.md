# 15 — SOON

Two different ciphertexts in the matrix decrypt to SOON.

## 1. First route

The YOU key has phase 1. At X(25,16), this gives V₁ = (0, 0). The project's hidden-value rule retains φ(25) = 20 = L and φ(16) = 8 = H.

Three structures connected to the same EA–EA–EA mirror produce the key:

| Node | First outer | Center | Second outer |
|:---|:---:|:---:|:---:|
| EA–EA–EA | EA(25,10) | EA(25,15) | EA(25,20) |
| L–C–EA | L(25,4) | C(25,7) | EA(25,10) |
| L–I–EA | L(15,15) | I(20,15) | EA(25,15) |
| L–EO–EA | L(25,8) | EO(25,14) | EA(25,20) |

### Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | φ(C = 5) = φ(I = 10) = φ(EO = 12) = 4 = R | L–R–EA |
| Totient signature | φ(L = 20) = 8; φ(R = 4) = 2; φ(EA = 28) = 12 | (8, 2, 12) |
| Möbius signature | μ(8) = 0; μ(2) = −1; μ(12) = 0 | (0, −1, 0) |
| Rotation | (0 − 1 + 0) mod 3 = 2 | EA–L–R |
| Movement | φ(16) = 8 = H | X(25,16) → H(25,19) (right 3) |

### Read and decrypt

From X(25,16), read four runes rightward. Subtract the repeating EA–L–R key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (25,16) | X = 14 | EA = 28 | 14 − 28 ≡ 15 | S |
| (25,17) | D = 23 | L = 20 | 23 − 20 ≡ 3 | O |
| (25,18) | W = 7 | R = 4 | 7 − 4 ≡ 3 | O |
| (25,19) | H = 8 | EA = 28 | 8 − 28 ≡ 9 | N |

## 2. Second route

The same X(25,16) belongs to E–X–E. Through the shared E(24,16), it connects to E–TH–E at TH(23,15). Two mirror paths then lead to a second ciphertext and key.

| Path | Connected mirrors | Destination |
|:---|:---|:---|
| Ciphertext | X–TH–X (23,15) → D–X–D (27,11) → P–D–P (27,20) | P(27,24) |
| Key | D–TH–D (23,15) → D–NG–D (22,17) → IA–D–IA (22,19) → IA–EA–IA (19,13) | EA(19,13) |

### Derive the key

| Step | Calculation | Result |
|:---|:---|:---|
| Key | EA = 28; φ(28) = 12 = EO | IA–EO–IA |
| Totient signature | φ(IA = 27) = 18; φ(EO = 12) = 4; φ(IA = 27) = 18 | (18, 4, 18) |
| Möbius signature | μ(18) = 0; μ(4) = 0; μ(18) = 0 | (0, 0, 0) |
| Rotation | (0 + 0 + 0) mod 3 = 0 | Key unchanged |
| Movement | Mirror paths from TH(23,15) | P(27,24) (ciphertext); EA(19,13) (key center) |

### Read and decrypt

From P(27,24), read four runes rightward. Subtract the repeating IA–EO–IA key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (27,24) | P = 13 | IA = 27 | 13 − 27 ≡ 15 | S |
| (27,25) | S = 15 | EO = 12 | 15 − 12 ≡ 3 | O |
| (27,26) | U = 1 | IA = 27 | 1 − 27 ≡ 3 | O |
| (27,27) | W = 7 | IA = 27 | 7 − 27 ≡ 9 | N |

## 3. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| Shared totient | φ(5) = φ(8) = φ(10) = φ(12) = 4. C, I and EO are the first key's centers; H ends its ciphertext. |
| Prime-valued sum | L + H = 73 + 23 = 96; SOON = 53 + 7 + 7 + 29 = 96. |

### SOON
