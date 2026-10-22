# 12 — DEATH

## 1. Locate the nodes

The IS ciphertext ends at D(21,10), the center of E–D–E. Moving 2 cells down-right, perpendicular to this mirror, reaches B(23,12).

| Node | First outer | Center | Second outer | Radius |
|:---|:---:|:---:|:---:|:---:|
| E–D–E | E(19,12) | D(21,10) | E(23,8) | 2 |
| J–B–J | J(19,16) | B(23,12) | J(27,8) | 4 |
| J–C–J | J(25,6) | C(26,7) | J(27,8) | 1 |
| C–OE–C | C(26,3) | OE(26,5) | C(26,7) | 2 |

J–B–J provides the key. The connected J–C–J and C–OE–C mirrors lead to the ciphertext.

## 2. Derive the key and starting point

| Step | Calculation | Result |
|:---|:---|:---|
| Key | B = 17; φ(17) = 16 = T | J–T–J |
| Totient signature | φ(J = 11) = 10; φ(T = 16) = 8; φ(J = 11) = 10 | (10, 8, 10) |
| Möbius signature | μ(10) = +1; μ(8) = 0; μ(10) = +1 | (+1, 0, +1) |
| Rotation | (1 + 0 + 1) mod 3 = 2 | J–J–T |
| Movement | Down-right 2; down-left 4; up-left 1; left 4 | D(21,10) → B(23,12) → J(27,8) → C(26,7) → C(26,3) |

## 3. Read and decrypt

From C(26,3), read three runes leftward. Subtract the J–J–T key modulo 29.

| Cell | Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|:---:|
| (26,3) | C = 5 | J = 11 | 5 − 11 ≡ 23 | D |
| (26,2) | I = 10 | J = 11 | 10 − 11 ≡ 28 | EA |
| (26,1) | E = 18 | T = 16 | 18 − 16 ≡ 2 | TH |

### DEATH

## 4. Numerical connections

| Connection | Evidence |
|:---|:---|
| Reused key | J–B–J generates the same J–J–T key used for END. |
| Passage totals | AS I GO THE WEATHER TURNS COLD = 233; THE IDEA OF THE END IS DEATH = 232; φ(233) = 232. |
| 17 and 53 | THE IDEA OF THE END IS DEATH contains 17 runes. B = 17; φ(17) = 16; the 16th prime is 53. DEATH = D(23) + EA(28) + TH(2) = 53. |
