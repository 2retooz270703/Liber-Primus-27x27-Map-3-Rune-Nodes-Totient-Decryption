# Liber Primus — LP2

Pages 0–2 · 27 × 27 rune matrix

This repository documents a proposed plaintext reconstruction of pages 0–2 of Cicada 3301's *Liber Primus*. It brings together an interactive matrix, individual plaintext records, and research notes on the decryption method.

## Proposed plaintext

> As I go, the weather turns cold.  
> I may cry now.  
> The idea of the end is death.  
> See you soon, then.

The recorded path from **AS I GO** to **THEN** covers **17 stages**. A proposed continuation is:

> The key is to go ...

Most of the initial path was found manually. The research now focuses on whether the relationships between keys and ciphertext cells can help predict further plaintext.

## Start here

1. **[Interactive matrix](https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/)** — Explore the ciphertext cells, keys, and proposed plaintext path.
2. **[Plaintext records](./plaintext-i-found/)** — Inspect each recorded stage and its location in the matrix.
3. **[Decryption method](./Start-reading-here/00-decryption-method.md)** — Follow how the keys are constructed and applied.

## Method and research notes

The method uses three-rune keys constructed with Euler's totient and Möbius functions, followed by modular subtraction. The notes below examine geometric and numerical constraints that may help identify the next key and ciphertext.

Read them in order:

| Note | Focus |
| --- | --- |
| [00 — Decryption method](./Start-reading-here/00-decryption-method.md) | Key construction and plaintext extraction. |
| [01 — Next-key signature](./Start-reading-here/01-next-key-signature.md) | The next key's phase and Möbius signature. |
| [02 — Leftmost cell and rotations](./Start-reading-here/02-leftmost-cell-and-rotations.md) | Matrix rotations and whether the leftmost ciphertext cell is the beginning or end. |
| [03 — Reading axis and direction](./Start-reading-here/03-predicting-axis-and-reading-direction.md) | The next ciphertext's axis and reading direction. |
| [04 — Key-center parity](./Start-reading-here/04-predicting-next-key-center-parity.md) | Whether the next key's center lies on an even or odd row and column. |
| [05 — Ciphertext row parity](./Start-reading-here/05-predicting-next-ciphertext-row-parity.md) | Row parity of the next ciphertext's endpoint and leftmost cell. |
| [06 — Ciphertext ray and Möbius deviation](./Start-reading-here/06-predicting-next-ciphertext-ray-and-mobius-deviation.md) | An eight-direction geometric rule with at most a one-cell deviation. |

## Numerical observations

GP refers to **Gematria Primus**, the numerical values assigned to the runes.

- **3274 + 27 = 3301.** Across the first 17 stages, 61 ciphertext-cell uses—54 unique cells and 7 repeated uses—have a total GP value of 3274. Adding the matrix's side length gives 3301.
- **26083 is the 2867th prime.** The 54 unique ciphertext cells have a GP sum of 2867; their absolute positions sum to 26083.
- **2163 = 3 × 7 × 103.** The plaintext GP sum from **AS I GO** through **DEATH** is 2163. Its prime factors match the rune values in **YOU**: U = 3, O = 7, Y = 103.

Whether these relationships were deliberately built into the matrix remains an open question. Further discussion, including a possible connection to Cicada's 2016 message, is in **[Plaintext evidence](./Start-reading-here/strongest-plaintext-evidence.md)**.

## Current research

The working hypothesis is that the first 17 stages, ending with **THEN**, reveal a geometric method for finding subsequent words.

Some constraints described in note 00 no longer hold after THEN. The later notes explore which constraints may continue to apply. The current goal is to extend the plaintext with meaningful, grammatical phrases that satisfy those constraints without changing the rules to fit a preferred reading.

