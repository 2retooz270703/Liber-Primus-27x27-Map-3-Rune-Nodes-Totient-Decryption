# 17 — THE

*Candidate continuation after THEN: THE KEY IS TO GO.*

## 1. Locate the node

The selected vertical mirror has center **M(20,17)** and radius **3**:

| First outer | Center | Second outer | Radius |
|:---:|:---:|:---:|:---:|
| N(17,17) | M(20,17) | N(23,17) | 3 |

The incoming THEN → THE ray is measured from the previous leftmost cell L(25,25) to the new beginning J(22,21): **d₈=1 ≤ q=1**.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | M = 19; φ(19) = 18 = E | N–E–N |
| Totient signature | φ(N = 9) = 6; φ(E = 18) = 6; φ(N = 9) = 6 | (6, 6, 6) |
| Möbius signature | μ(6) = +1; μ(6) = +1; μ(6) = +1 | (+1, +1, +1) |
| Rotation | 3 mod 3 = 0; cyclic left shift by 0 | N–E–N |
| Incoming prediction | Report 01, evaluated on THEN | (+1, +1, +1); phase 0 |
| Reading geometry | Reports 02–03 predict DIAGONAL; leftmost cell is the END | Read diagonally up-left from J(22,21) |
| Center parity | Report 04 predicts even row / odd column | (20,17) matches |

## 3. Read and decrypt

From **J(22,21)**, read 2 runes diagonally up-left. Subtract the aligned key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (22,21) | J = 11 | N = 9 | 11 − 9 ≡ 2 | TH |
| (21,20) | W = 7 | E = 18 | 7 − 18 ≡ 18 | E |

### THE

## 4. Connections in the matrix

| Connection | Evidence |
|:---|:---|
| THEN → THE ray | From L_THEN=(25,25) to J(22,21), Δ=(-3,-4) and d₈=1. The endpoint W(25,27) gives n₀=675 and n₃=25, both with μ=0, so q=1 permits this offset. |
| Next-center parity | Report 04 predicts an even row and odd column after THEN. M(20,17) satisfies both conditions. |
| Rows from Report 05 | Both the endpoint and the leftmost cell are W(21,20), in odd row 21, as predicted. |
| GP total points to the key center | GP(THEN)=101 and GP(THE KEY IS TO GO)=429. Their sum is 530=27(20−1)+17=n₀(M(20,17)), the center of this THE key node. This is a numerical observation on the selected continuation. |

This is the **N–M–N** realization of THE at J(22,21) → W(21,20), not the separate E–O–E realization at (24,27) → (23,26). The explicit formulas in Reports 01–06 pass.
