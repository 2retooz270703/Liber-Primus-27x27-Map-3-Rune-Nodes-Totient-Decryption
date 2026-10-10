# 01 — How Runes Become Plaintext

**Three runes → Key → Phase → Plaintext**

The 729 runes from pages 0–2 are arranged row by row in a **27 × 27 matrix**. Each rune has an index from **0 to 28**. These indices—not the Gematria Primus prime values—are used below. `TH`, `EA`, and `NG` each count as one rune.

## 1. Start with a three-rune structure

| Row | Column 4 | Column 5 | Column 6 |
|:---:|:---:|:---:|:---:|
| 14 | X | OE | X |

The middle rune is the **center**; the other two are **outers**. Matching outers form a *mirror*. The three cells need not be adjacent, and some stages use non-mirrored triples, such as `H–NG–C`.

## 2. Form the key

**Euler's totient**, `φ(n)`, counts how many integers from 1 through `n` share no factor with `n` except 1. For example, `φ(10) = 4`: the integers are 1, 3, 7, and 9.

Let `a`, `b`, and `c` be the three rune indices. Apply `φ` **only to the center** (`b`), then convert its result back into a rune:

$$
(a,b,c)\ \longrightarrow\ (a,\varphi(b),c)
$$

| | Left | Center | Right |
|:---|:---:|:---:|:---:|
| Structure | X = 14 | OE = 22 | X = 14 |
| Key | X = 14 | **I = 10** | X = 14 |

`φ(22) = 10`, so **X–OE–X → X–I–X**. The outer runes do not change. In some recorded cases, such as `H–NG–C`, the triple is instead used directly.

## 3. Find the phase

The **Möbius function**, `μ(n)`, checks a number’s prime factors. A squared prime factor gives `0`; without one, the sign depends on how many distinct prime factors there are:

| Value | When | Example |
|:---:|:---|:---|
| `0` | Contains a squared prime factor | `μ(4) = 0` (`4 = 2²`) |
| `+1` | An even number of distinct prime factors | `μ(6) = +1` (`6 = 2 × 3`) |
| `−1` | An odd number of distinct prime factors | `μ(2) = −1` |

Also, `μ(1) = +1`.

For the **generated key**, let `k₁`, `k₂`, `k₃` be its three indices. Apply `φ` to **each one**, then apply `μ` to the results:

| | k₁ | k₂ | k₃ |
|:---|:---:|:---:|:---:|
| Key | X = 14 | I = 10 | X = 14 |
| φ | 6 | 4 | 6 |
| μ | +1 | 0 | +1 |

Add the three Möbius values to get the **phase**. `mod 3` means taking the remainder in the range 0–2:

$$
p = [\mu(\varphi(k_1)) + \mu(\varphi(k_2)) + \mu(\varphi(k_3))]\bmod 3
$$

Here, **p = (1 + 0 + 1) mod 3 = 2**. The phase tells us how many places to rotate the key **left**:

| Phase 0 | Phase 1 | Phase 2 |
|:---:|:---:|:---:|
| X–I–X | I–X–X | **X–X–I** |

The full Möbius signature `(+1, 0, +1)` is kept for the route rules; its sum is used for rotation.

## 4. Recover the plaintext

In this example, the ciphertext is read across row 14, columns 14–18: **NG–P–EO–O–E**. Repeat the phase-2 key to match its length: **X–X–I–X–X**.

Subtract each key index from the matching ciphertext index:

$$
\text{Plaintext index} = (\text{Ciphertext index} - \text{Key index})\bmod 29
$$

`mod 29` keeps the answer between 0 and 28. For example, `13 − 14 = −1 ≡ 28 (mod 29)`, which is the rune `EA`.

| Ciphertext | Key | Subtraction (mod 29) | Plaintext |
|:---:|:---:|:---:|:---:|
| NG = 21 | X = 14 | 21 − 14 = 7 | W |
| P = 13 | X = 14 | 13 − 14 ≡ 28 | EA |
| EO = 12 | I = 10 | 12 − 10 = 2 | TH |
| O = 3 | X = 14 | 3 − 14 ≡ 18 | E |
| E = 18 | X = 14 | 18 − 14 = 4 | R |

### W–EA–TH–E–R → WEATHER

This explains **how** a selected key decrypts a selected ciphertext. How the algorithm locates those structures and chooses the next reading direction is a separate question, covered by the movement and mirror rules.
