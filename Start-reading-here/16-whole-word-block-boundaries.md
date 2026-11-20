# Whole-Word Block Boundaries

## 1. Required rule

**Each independently decrypted block must contain one complete English word or a sequence of complete English words. No English word may be split across two or more blocks.**

A block is the complete plaintext output of one independently decrypted ciphertext block, read in its established order with its assigned key stream. Its boundaries must also be valid word boundaries.

Several words may appear together without spaces. For example, `IMAY` is read as **I MAY**, and `NOWTHE` is read as **NOW THE**. Every word must begin and end within that same block.

This is a required plaintext acceptance criterion for this project. Apply it together with the constraints in Reports **00–15**.

## 2. Valid examples

In the tables below, `│` marks a boundary between independently decrypted blocks.

| Decrypted block or blocks | Word segmentation | Result |
| :--- | :--- | :--- |
| `WEATHER` | WEATHER | Valid: one complete word. |
| `IMAY` | I MAY | Valid: two complete words in one block. |
| `NOWTHE` | NOW THE | Valid: two complete words in one block. |
| `ASIGOTHE` | AS I GO THE | Valid: four complete words in one block. |
| `YOU │ FEAR` | YOU / FEAR | Valid: both words are complete within their respective blocks. |

A block does **not** have to be a complete sentence or a self-contained phrase. Its words may connect grammatically to words in neighboring blocks. For example, `NOWTHE` contains complete words even though THE requires a continuation.

## 3. Forbidden word splitting

A readable combined sentence does not make an invalid block boundary acceptable.

| Decrypted blocks | Attempted reading | Why it fails |
| :--- | :--- | :--- |
| `WEA │ THER` | WEATHER | WEATHER is split between blocks. |
| `NOWTH │ E` | NOW THE | THE begins in one block and ends in the next. |
| `YOUF │ EAR` | YOU FEAR | The first block ends with a fragment of FEAR. EAR being a word does not repair YOUF. |
| `WEATHERX` | WEATHER, with X ignored | The complete block contains an unexplained extra letter. |

Do not borrow letters from neighboring blocks, discard leftover letters, or change decrypted letters to obtain complete words. Adding spaces must preserve the entire decrypted sequence.

## 4. Applying the rule during searches

For each candidate continuation:

1. Keep the candidate's independently decrypted block boundaries explicit.
2. Check each block separately. Its entire plaintext must be segmentable into one or more complete English words, with no leftover letters.
3. Reject the candidate if any intended word crosses a block boundary.
4. Check the grammar and meaning of the resulting continuation in context.
5. Retain it only if it also passes the applicable constraints in Reports 00–15.

Evaluate word boundaries on the established rune transliteration. Split only between complete rune emissions. For example, `TH` and `EA` each come from a single rune, and ᛝ (index 21) can emit `NG` or `ING`. The standalone decoder also accepts `QU` from the adjacent pair `C/K + W` (indices `5, 7`), with no word break inside that pair. Reports 23–27 count Hunspell readings using single-rune emissions. [Decoder](../README.md#experimental-python-decoder) · [Report 27](27-key-alignment-from-node-geometry.md)

The minimum length in Report 08 applies to the **whole block**. Thus, the one-letter word I is allowed inside the multiword block `IMAY`; this does not permit a separate one-rune block.

The numerical Hunspell checks can vary with the installed dictionary. The reference `en_US` pair used for the tables in this project has the following SHA-256 hashes.

```text
70fe5778717d097ce2f3326baaa5c1e4d2206d81a5a81d3ea8e11c4770806dd5  en_US.aff
829a043cf078d1e80e886289a13823454977f442a239a859d2133ea61944aa60  en_US.dic
```

**Acceptance condition: every block is fully accounted for by complete English words, and every word belongs entirely to one block.**

