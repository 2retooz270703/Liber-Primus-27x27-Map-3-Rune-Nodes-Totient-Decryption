# Minimum Ciphertext Block Length

**A Proposed Constraint on Independent Single-Rune Decryptions**

*27 × 27 matrix · LP2 pages 0–2 · 29-rune alphabet · Plaintext block boundaries · False-positive reduction*

---

The recorded reconstruction contains a consistent structural feature: **none of its independently decrypted ciphertext blocks is only one rune long**. Single-letter English words, especially **I**, occur inside longer blocks rather than being decrypted from isolated cells.

This suggests a useful additional constraint for exploring the matrix: **a candidate continuation should contain at least two decrypted runes per independent ciphertext block**. The aim is to reduce the large number of short, easily fitted branches—not to assert that single-rune decryption is mathematically impossible.

**Status:** An empirical observation about the project's *selected reconstruction*, proposed as a search filter. It is not yet a demonstrated requirement of the original Cicada 3301 encryption method.

**Contents**

[01. Observation](#observation) · [02. Minimum-length constraint](#minimum-length-constraint) · [03. Why it matters](#why-it-matters) · [04. Application and limitations](#application-and-limitations)

---

## Observation

The block boundary is **not** necessarily a word boundary. In the recorded route, multiple English words can be produced by **one continuous ciphertext and one derived key stream**.

| Recorded plaintext block | Decrypted rune sequence | Rune count |
|---|---|---:|
| [AS I GO, THE](../plaintext-i-found/01-as-i-go-the.md) | `A · S · I · G · O · TH · E` | **7** |
| [I MAY](../plaintext-i-found/05-i-may.md) | `I · M · A · Y` | **4** |
| [NOW THE](../plaintext-i-found/07-now-the.md) | `N · O · W · TH · E` | **5** |
| [OF](../plaintext-i-found/09-of.md) | `O · F` | **2** |
| [THE](../plaintext-i-found/10-the.md) | `TH · E` | **2** |
| [IS](../plaintext-i-found/12-is.md) | `I · S` | **2** |

For example, the word **I** in `I MAY` is **not** assigned a separate ciphertext cell and key. It is part of a four-rune reading. Likewise, **I** in `AS I GO, THE` belongs to a seven-rune block.

**Rune count differs from English letter count.** In the project's 29-rune alphabet, `TH` and `EA` each represent one rune. Thus `THE` is a **two-rune** plaintext (`TH · E`), despite being three English letters.

Across the **17 selected blocks** from `AS I GO, THE` through `THEN`, the recorded lengths are:

| Runes in one block | Number of recorded blocks |
|:---:|---:|
| **2** | 3 |
| **3** | 7 |
| **4** | 3 |
| **5** | 3 |
| **7** | 1 |
| **1** | **0** |

The five *candidate* blocks of `THE KEY IS TO GO` also each contain at least two runes. They are part of a proposed continuation, however, and should not be counted as independently verified evidence.

---

## Minimum-Length Constraint

For any independently selected ciphertext block, let `N` be its number of matrix cells read in sequence. Each cell produces one decrypted rune under the project's modular subtraction method.

**Proposed rule:**

```text
N >= 2
```

In practical terms:

- **Allowed:** a single-letter word embedded in a longer decrypted block, such as `I MAY`.
- **Allowed:** an independent block containing two or more runes, such as `O · F` or `TH · E`.
- **Excluded by this proposed filter:** an independent one-cell block yielding only `I`, `A`, or any other single rune.

This is a restriction on **ciphertext-block length**, not a prohibition on one-letter words in the resulting English sentence. A three-rune *key node* may still be used to decrypt a two-rune ciphertext; these are separate lengths.

---

## Why It Matters

A single decrypted rune is weak evidence for plaintext. Many ciphertext cells and possible key alignments can produce a chosen output rune, especially when the search permits non-mirrored key nodes. This flexibility makes one-cell words convenient for assembling grammatical but potentially accidental continuations.

Requiring at least two runes removes this particularly permissive class of candidates. It also prevents an English phrase from being split into arbitrarily many independently keyed one-letter units just to satisfy the geometric constraints.

For example, a proposed sequence that treats **BE**, **A**, and **GOD** as **three separate blocks** fails this minimum-length filter at **A**, even if each isolated decryption satisfies the earlier geometric rules. The same English words would not automatically fail if they were demonstrated to arise from a **single longer ciphertext block**.

This condition is intended to **supplement**, not replace, Reports 00–07: every retained candidate must still satisfy the applicable decryption, key, and coordinate tests.

---

## Application and Limitations

During continuation searches, apply the length test **before ranking meaningful English phrases**:

1. Identify a candidate ciphertext's cells and its independent key assignment.
2. Count the **decrypted runes**, not letters or words.
3. Reject the candidate as a **standalone block** if it contains only one rune.
4. Apply the remaining documented constraints to blocks of two or more runes.

**Important distinction:** The project's arithmetic can decrypt a single cell; the observed reconstruction simply does **not** use such a cell as an independent plaintext block. Consequently, the evidence does not establish that the original author *could not* encode a single rune or deliberately forbade doing so.

A convincingly established one-rune ciphertext block in the same underlying scheme would challenge this proposed constraint. Until then, the two-rune minimum is a practical, explicit safeguard against overfitting—not independent proof of the true plaintext.
