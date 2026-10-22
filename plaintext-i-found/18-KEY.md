# 18 — KEY

*Candidate continuation after THEN: THE KEY IS TO GO.*

## 1. Locate the node

The selected vertical mirror has center **H(12,16)** and radius **1**:

| First outer | Center | Second outer | Radius |
|:---:|:---:|:---:|:---:|
| TH(11,16) | H(12,16) | TH(13,16) | 1 |

The incoming THE → KEY ray is measured from the previous leftmost cell W(21,20) to the new beginning N(21,4): **d₈=0 ≤ q=0**.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | H = 8; φ(8) = 4 = R | TH–R–TH |
| Totient signature | φ(TH = 2) = 1; φ(R = 4) = 2; φ(TH = 2) = 1 | (1, 2, 1) |
| Möbius signature | μ(1) = +1; μ(2) = -1; μ(1) = +1 | (+1, -1, +1) |
| Rotation | 1 mod 3 = 1; cyclic left shift by 1 | R–TH–TH |
| Incoming prediction | Report 01, evaluated on THE | (+1, -1, +1); phase 1 |
| Reading geometry | Reports 02–03 predict VERTICAL; leftmost cell is the BEGINNING | Read upward from N(21,4) |
| Center parity | Report 04 predicts even row / even column | (12,16) matches |

## 3. Read and decrypt

From **N(21,4)**, read 3 runes upward. Subtract the aligned key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (21,4) | N = 9 | R = 4 | 9 − 4 ≡ 5 | C |
| (20,4) | L = 20 | TH = 2 | 20 − 2 ≡ 18 | E |
| (19,4) | EA = 28 | TH = 2 | 28 − 2 ≡ 26 | Y |

### KEY

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| THE → KEY ray | W(21,20), the endpoint and leftmost cell of THE, lies on the same row as N(21,4). Moving left 16 cells reaches the KEY beginning; d₈=0 and q=0. |
| Shared diagonal | N(21,4), X(18,7), OE(19,6), U(9,16), and NG(8,17) all satisfy r+c=25. Thus KEY begins on the same diagonal occupied by the complete IS and TO ciphertexts. |
| Selecting the original node | TH(4,2)–I(12,2)–TH(20,2) also derives TH–R–TH. In the mirrored-node enumeration with Reports 01–06 fixed, only the node centered on H(12,16) permits the following IS. |
| Rows from Report 05 | The endpoint EA(19,4) and leftmost cell N(21,4) are both in odd rows, as predicted. |
