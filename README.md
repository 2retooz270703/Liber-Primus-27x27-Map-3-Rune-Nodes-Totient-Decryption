---

<p align="center">
  <em>
    As I go, the weather turns cold.<br>
    I may cry now.
  </em>
</p>

<p align="center">
  <em>
    The idea of the end is death.<br>
    See you soon, then.
  </em>
</p>

<p align="center">
  <em>
    The key is to go ...
  </em>
</p>

---

```text
The first 17 stages, from AS I GO to THEN, used ciphertext cells 61 times: 54 unique cells, plus 7 repeated uses. Summing their Gematria Primus prime values, including those repetitions, gives 3274. 3274 + 27 = 3301. Here, 27 is the side length of our 27 × 27 matrix. This looks like the author’s signature.
```

```text
Moreover, the 54 unique cells have a total GP value of 2867, while the sum of their absolute positions is 26083. The crazy part is that 26083 is the 2867th prime number.
```

---

**If you're visiting this repository for the first time, start by opening the interactive HTML map.**

I created it specifically to make it easier to verify my findings. So open it up and take some time to explore the map visually.

#### **[Interactive Matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)**

---

**After exploring the interactive map, open the folder below and briefly look through the files to get an overview of the project.**

Some things might not make sense at first, but it should help you understand the overall concept.

#### [Plaintext Records](./plaintext-i-found/)

---

**Once you've taken a look, explore how I discovered and reconstructed the plaintext path.**

The documents below contain my research into the discovered plaintext. Most of it was found manually, and I believe it is correct because it stood out geometrically. My manual discoveries were based on the methods described in `00.md`, so I recommend reading that file carefully. I was confident in the accuracy of what I had found, so I began searching for patterns in how the plaintext was generated. This led to the creation of `01.md`, `02.md`, and the subsequent files. What makes these findings particularly interesting is that the system I discovered does not appear to be random.

---

#### [00 — The Decryption Method](./Start-reading-here/00-decryption-method.md)

The foundation of the system. Explains how three-rune structures produce decryption keys, how Euler's totient and Möbius functions determine their cyclic alignment, and how modular subtraction reveals plaintext.

---

#### [01 — Predicting the Next-Key Signature](./Start-reading-here/01-next-key-signature.md)

Describes how the current ciphertext predicts the next key's phase and complete Möbius signature. Explores cumulative phase cycles, Direct and Reflected modes, and the relationship between 90° and 180° matrix rotations.

---

#### [02 — The Leftmost Cell and Rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md)

Examines the leftmost ciphertext cell and its own Möbius state. Introduces the 270° rotation rule, which predicts whether the leftmost cell of the next ciphertext will be its beginning or end, and shows how all four matrix rotations are connected.

---

#### [03 — Predicting the Reading Axis](./Start-reading-here/03-predicting-axis-and-reading-direction.md)

Explains how the next ciphertext's horizontal, vertical, or diagonal axis can be predicted. Combines this result with the 270° rule to constrain the reading direction.

---

#### [04 — Predicting the Next Key’s Center Parity](./Start-reading-here/04-predicting-next-key-center-parity.md)

Explains how two coordinate formulas predict whether the next key’s center lies in an even or odd row and column. Both rules match all 16 recorded transitions. After THEN, their combined parity filter reduces the 44 mirror nodes with signature (+1,+1,+1) to 16 candidates.

---

#### [05 — Predicting the Next Ciphertext’s Row Parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md)

Introduces two related formulas predicting whether the next ciphertext’s endpoint and leftmost cell lie in even or odd rows. They connect the current phase and key center with a 180° rotation and the earlier center-parity rule. Both match all 16 recorded transitions and the proposed THE, giving conditional 17/17. After THEN, they reduce the possible leftmost cells from 337 to 186.

---

#### [06 — Ciphertext Ray & Möbius Deviation](Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md)

A geometric rule showing that the next ciphertext begins on or within one cell of eight directional rays from the previous ciphertext’s leftmost cell (16/16 transitions). One-cell deviations are linked to zero Möbius values, with a remarkable mirror symmetry between SEE and YOU.

---

**Also, take a look at the file below. I believe it contains the strongest evidence confirming the discovered plaintext.**

If you ask me which one is my favorite, it's the fact that the sum of the Gematria Primus values of all runes from AS I GO through DEATH equals 2163, which factorizes as 3 × 7 × 103. These three prime numbers correspond exactly to the runes spelling YOU in Gematria Primus (Y = 103, O = 7, U = 3), revealing a striking connection to 3301's 2016 message: "Seek and you will be found."

#### [Strongest Plaintext Evidence](./Start-reading-here/strongest-plaintext-evidence.md)

---

From “AS I GO” to “THEN,” there are exactly 17 plaintext-generation steps, with “DEATH” appearing precisely at step 13. This suggests a deliberate structure: the 17 steps appear designed to reveal the underlying algorithm. Beyond this point, rules 01, 02, and onward apply, while certain rules from 00, such as the coordinate selector and center/outer rule, no longer work.

I suspect Cicada only needed to carefully design the first 17 stages, making them as interconnected as possible, both geometrically and numerically. I've already explored these relationships in detail in this post. My theory is that they used a specific set of formulas and constraints to construct these stages, and their purpose was to help the solver discover those exact rules. Once identified, the same rules could be extended across the rest of the 27×27 matrix to reconstruct the remaining plaintext. This could explain the illustrations of crossroads and directional signs, as well as the phrase "SEE YOU SOON, THEN".

Essentially, this would be a geometric method of encrypting plaintext within a matrix. The first 17 stages would serve as both clues and part of the algorithm. After stage 17, a simple program could continue placing ciphertexts and keys according to the same constraints, including cell rotations of 0°, 90°, 180°, and 270°, Möbius predictions, and geometric relationships. Without knowing these rules, the matrix would look like a chaotic collection of unrelated cells. But applying the correct formulas would reveal the hidden message. Cicada wouldn't need to explain the method at all. The solver would discover the first 17 stages, derive the formulas, and use them to find the rest of the plaintext. All Cicada had to do was design those initial stages and then distribute the remaining plaintext programmatically using the same rules.
