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

Evaluate word boundaries on the established rune transliteration. Multi-letter rune labels such as `TH` and `EA` still represent one rune each.

The minimum length in Report 08 applies to the **whole block**. Thus, the one-letter word I is allowed inside the multiword block `IMAY`; this does not permit a separate one-rune block.

**Acceptance condition: every block is fully accounted for by complete English words, and every word belongs entirely to one block.**

