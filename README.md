<h1 align="center">Liber Primus — LP2</h1>

<p align="center">
  <sub>Pages 0–2 · 27 × 27 rune matrix · A proposed plaintext reconstruction</sub>
</p>

<p align="center">
  <strong>
    As I go, the weather turns cold.<br>
    I may cry now.
  </strong>
</p>

<p align="center">
  <strong>
    The idea of the end is death.<br>
    See you soon, then.
  </strong>
</p>

<p align="center">
  <strong>The key is to go ...</strong>
</p>

<p align="center">
  <sub>AS I GO → THEN: 17 recorded stages · THE KEY IS TO GO: proposed continuation</sub>
</p>

---

## Start here

If you're new to this project, I recommend exploring it in this order:

1. **[Interactive Matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)** — See the ciphertext cells, keys, and proposed plaintext path on the 27 × 27 grid.
2. **[Plaintext Records](./plaintext-i-found/)** — Check the individual words and their locations.
3. **[Decryption Method](./Start-reading-here/00-decryption-method.md)** — Learn how the three-rune keys and modular subtraction are used.

I found most of the initial path manually. The research notes below explain how I began testing whether its geometric patterns could predict what comes next.

## Two numerical connections

**3274 + 27 = 3301**  
<sub>Across the first 17 stages, 61 ciphertext-cell uses (54 unique + 7 repeated) have a combined Gematria Primus value of 3274. The matrix is 27 × 27.</sub>

**26083 is the 2867th prime number**  
<sub>The 54 unique ciphertext cells have a GP sum of 2867, while their absolute positions sum to 26083.</sub>

These relationships caught my attention because **3301** is Cicada's number and the second result connects a GP sum to a prime's index. Whether they were deliberately built into the matrix remains an open question.

## Research notes

Read the documents in order. Each builds on the previous one.

- **[00 — Decryption Method](./Start-reading-here/00-decryption-method.md)** — Constructing three-rune keys with Euler's totient and Möbius functions, then using modular subtraction to reveal plaintext.
- **[01 — Next-Key Signature](./Start-reading-here/01-next-key-signature.md)** — Predicting the next key's phase and Möbius signature.
- **[02 — Leftmost Cell & Rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md)** — Using matrix rotations to identify whether the next ciphertext's leftmost cell is its beginning or end.
- **[03 — Reading Axis](./Start-reading-here/03-predicting-axis-and-reading-direction.md)** — Predicting the next ciphertext's axis and reading direction.
- **[04 — Key-Center Parity](./Start-reading-here/04-predicting-next-key-center-parity.md)** — Predicting whether the next key's center is on an even or odd row and column; narrows 44 candidates to 16 after THEN.
- **[05 — Ciphertext Row Parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md)** — Predicting row parity for the next ciphertext's endpoint and leftmost cell; narrows 337 candidates to 186 after THEN.
- **[06 — Ciphertext Ray & Möbius Deviation](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md)** — Testing an eight-direction geometric rule with at most a one-cell deviation.

The rules in **04–06** match all **16 transitions** along the recorded 17-stage path. This is evidence about the *proposed path*, not yet independent proof of a correct decryption.

## More plaintext evidence

**2163 = 3 × 7 × 103**

The GP sum from **AS I GO** through **DEATH** is 2163. Its prime factors match the values of the runes spelling **YOU** (U = 3, O = 7, Y = 103), an interesting parallel to Cicada's 2016 message, *“Seek and you will be found.”*

**[Read the strongest plaintext evidence →](./Start-reading-here/strongest-plaintext-evidence.md)**

## What I'm trying to find out

My hypothesis is that the first **17 stages**, ending with **THEN**, were arranged to reveal a geometric decryption method. **DEATH** appears at stage 13. The positions of keys and ciphertext cells, their rotations, and their Möbius values may provide rules for finding the next words.

Some rules from **00** stop working after THEN, while the later notes explore constraints that might continue to apply. The next challenge is to find **meaningful plaintext beyond THEN** without adjusting the rules just to fit a desired phrase.

<sub>This is an independent investigation and a proposed reconstruction.</sub>
