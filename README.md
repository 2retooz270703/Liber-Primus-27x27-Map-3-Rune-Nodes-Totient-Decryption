# Cicada 3301 Liber Primus 0–2 — 27×27 Rune Matrix Decryption

This repository documents my proposed solution framework for **Cicada 3301's Liber Primus, pages 0–2**.

The central observation is simple:

**Liber Primus pages 0–2 contain exactly 729 runes.**

Since:

**729 = 27 × 27**

the complete rune sequence can be written left-to-right, row-by-row, as a **27×27 rune matrix**.

My approach therefore does not treat Liber Primus 0–2 only as a linear ciphertext. It treats the 729 runes as a **spatial map** containing mirrored and symmetrical **three-rune structures** that act as nodes, keys, and navigation points.

The proposed method combines:

**27×27 geometry → three-rune nodes → Euler's totient function φ → spatial movement → Möbius function μ → key-phase selection → Gematria Primus mod 29 decryption**

Using this process, my current Volume 1 result is:

> **AS I GO, THE WEATHER TURNS COLD**

This is a **proposed and ongoing solution**, not an officially verified decryption of Liber Primus.

**Core idea:** 729 runes → 27×27 matrix → mirrored three-rune nodes → Euler totient navigation → Möbius key phase → Gematria Primus mod 29 decryption.

---

## The core idea

The 729 runes of Liber Primus pages 0–2 are arranged into a **27×27 grid**.

Once arranged this way, the text reveals unusual mirrored structures around important locations in the matrix.

Examples include:

**AE-J-EA**

**X-OE-X**

**I-NG-I**

**H-NG-C**

**H-TH-H**

These structures are not treated as decorative patterns. In this model, their rune values are transformed mathematically and used to generate short repeating keys and movement distances through the matrix.

The basic process is:

**find a structure → transform its values → generate a key → move through the matrix → decrypt the next segment → reach another structure**

This creates a linked route through the 27×27 matrix rather than a sequence of unrelated decryptions.

---

## 1. The 729-rune 27×27 matrix

The starting point is the exact rune count:

**729 runes = 27 × 27**

The entire text of pages 0–2 can therefore be written into a square matrix without adding or removing runes.

The runes are placed in their original order:

**left to right → next row → left to right → next row**

The resulting 27×27 matrix becomes the coordinate system for the proposed solution.

In this interpretation, position matters.

A rune is not only a cryptographic symbol. Its location relative to mirrored nodes, the center of the matrix, and other structures can determine the next step.

---

## 2. Three-rune nodes and Euler's totient

A central mathematical operation in the method is **Euler's totient function**, written:

**φ(n)**

One of the first important structures is:

**AE-J-EA**

Using Gematria Primus values:

**J = 11**

and:

**φ(11) = 10**

Gematria Primus value **10 = I**, therefore:

**AE-J-EA → AE-I-EA**

This produces the repeating three-rune key:

**AE-I-EA**

The same transformation also produces a movement value.

Since:

**φ(10) = 4**

then:

**10 + 4 = 14**

which gives:

**RIGHT 14**

At that location, applying the repeating key with modular subtraction yields the proposed plaintext:

> **AS I GO THE**

So the same mathematical structure participates in both **key generation** and **navigation through the matrix**.

---

## 3. From X-OE-X to the center of the matrix

The end of the first stage leads into another mirrored three-rune structure:

**X-OE-X**

The center rune again reduces through Euler's totient:

**φ(OE) = 10 = I**

giving:

**X-OE-X → X-I-X**

The value **10** then gives another movement:

**RIGHT 10**

This movement reaches **NG**, the exact center of the 27×27 matrix.

The next proposed plaintext produced from this stage is:

> **WEATHER**

This is important because the route is not manually restarted after the first plaintext segment.

The previous stage physically leads into the structure that controls the next stage.

---

## 4. Möbius function and key phase

A three-rune repeating key can have three possible starting positions.

To determine which phase should be used, I propose the following rule:

**p = [μ(φ(k₁)) + μ(φ(k₂)) + μ(φ(k₃))] mod 3**

where:

**φ** = Euler's totient function  
**μ** = Möbius function  
**k₁, k₂, k₃** = the three runes of the key

The resulting value determines the rotation of the repeating key:

**p = 0 → start from rune 1**  
**p = 1 → start from rune 2**  
**p = 2 → start from rune 3**

For example, the key:

**X-I-X**

produces phase:

**p = 2**

so the active repeating key becomes:

**X-X-I**

This phase is used in the proposed decryption of:

> **WEATHER**

The phase therefore does not have to be chosen manually for each segment.

---

## 5. Totient-based navigation

After WEATHER, the route continues through the geometry of the matrix.

Two important derived values are:

**10**

and:

**φ(10) = 4**

At an important A position in the matrix:

**UP 10 → NG**

and:

**RIGHT 4 → NG**

This produces a route through another NG-centered structure.

The structure:

**H-NG-C**

has the totient pattern:

**4-12-4**

Using this structure as the repeating key while reading the corresponding ciphertext upward produces:

> **TURNS**

Another important value is:

**φ(NG) = φ(21) = 12**

The shift of **12** leads to the mirrored structure:

**H-TH-H**

This becomes the key for the next stage.

---

## 6. Mod 29 decryption

The actual rune decryption uses **Gematria Primus values modulo 29**.

The rule is:

**P = C - K mod 29**

where:

**P** = plaintext rune  
**C** = ciphertext rune  
**K** = active key rune

For the final word of the current Volume 1 plaintext, the mirrored structure is:

**H-TH-H**

Since:

**φ(TH = 2) = 1 = U**

the transformed key is:

**H-U-H**

The Möbius phase rule gives:

**p = 1**

therefore the active repeating key becomes:

**U-H-H**

The ciphertext is:

**G-J-EA-A**

Applying:

**P = C - K mod 29**

gives:

**G-J-EA-A − U-H-H-U = C-O-L-D**

Result:

> **COLD**

The current proposed plaintext is therefore:

> **AS I GO, THE WEATHER TURNS COLD**

---

## 7. The route as a connected system

The important point of this approach is not only that individual ciphertext fragments can produce English words.

The proposed solution attempts to connect the stages structurally.

In simplified form:

**729 runes**

↓

**27×27 rune matrix**

↓

**mirrored three-rune structure**

↓

**Euler totient transformation**

↓

**three-rune key + movement value**

↓

**Möbius key phase**

↓

**Gematria Primus mod 29 decryption**

↓

**plaintext**

↓

**next structural node**

↓

**next stage**

The current route produces:

**AS I GO THE → WEATHER → TURNS → COLD**

The goal is to determine whether this same structural logic can continue through the matrix.

---

## 8. Numerical structure of the plaintext

The recovered phrase:

> **AS I GO THE WEATHER TURNS COLD**

contains:

**7 words**

and:

**21 runes**

Using 0-based Gematria Primus indices, the complete plaintext has a total value of:

**233**

The word:

**COLD**

has a Gematria Primus index sum of:

**51**

and:

**233 is the 51st prime number**

There is also a Fibonacci relationship:

**F₇ = 13**

and:

**F₁₃ = 233**

This gives the chain:

**7 → 13 → 233**

The value **21** also appears independently as the Gematria Primus value of **NG**, which occupies the center of the 27×27 matrix.

These numerical relationships are treated as possible **consistency checks or structural signatures**, not as standalone proof that the plaintext is correct.

---

## 9. Recursive Transition Network hypothesis

A broader interpretation developed from this research is that the 27×27 map may behave like a **Recursive Transition Network (RTN)**.

A Recursive Transition Network can be thought of as a system of:

**nodes → transitions → procedures → continuation or return**

This resembles the behavior proposed for the Liber Primus matrix:

**structure → mathematical operation → movement → decryption → new structure**

Under this interpretation, Liber Primus may be designed less like one conventional linear cipher and more like a **network or labyrinth of connected states**.

The RTN interpretation is a broader architectural hypothesis and is not required for the core Volume 1 derivation above.

---

## What this solution is proposing

The central hypothesis of this repository is:

> **Liber Primus pages 0–2 may encode part of their solution spatially. The exact 729-rune length allows the ciphertext to form a 27×27 matrix, and mirrored three-rune structures inside that matrix may generate both cryptographic keys and navigation instructions through Euler's totient function. A Möbius-function rule selects the phase of the repeating key, while Gematria Primus subtraction modulo 29 produces the plaintext.**

Current proposed result:

> **AS I GO, THE WEATHER TURNS COLD**

The research is ongoing.

---

## Files

### [SOLUTION 0-2 — Volume 1](./SOLUTION%200-2%20volume%201.pdf)

The main technical document for this stage of the research.

It contains the full proposed Liber Primus 0–2 derivation, including the **729-rune 27×27 matrix**, mirrored three-rune structures, Euler totient transformations, navigation rules, Möbius-function key phase, Gematria Primus mod 29 decryption, and the numerical relationships surrounding the current plaintext.

### [What is Liber Primus?](./What%20is%20Liber%20Primus%3F.pdf)

A separate conceptual explanation of my interpretation of Liber Primus.

It presents the idea that Liber Primus may be a deliberately structured journey or sequence of discoveries rather than a conventional cipher governed everywhere by one fixed decoding rule.

---

## Research status

This repository contains a **proposed cryptanalytic solution and ongoing research**.

It should not be treated as an officially confirmed solution to Cicada 3301 or Liber Primus.

I am publishing the method publicly so that it can be:

**read, reproduced, tested, criticized, falsified, improved, or continued by other researchers.**

If you find a mistake, an alternative explanation, a statistical problem, or an independently reproducible continuation, please open an Issue.

---

## Related terminology

This research concerns **Cicada 3301, Liber Primus, Liber Primus decryption, Liber Primus solver research, Gematria Primus, the 729 runes of pages 0–2, a 27×27 rune matrix, mirrored three-rune nodes, Euler's totient function, totient-based navigation, the Möbius function, Möbius key-phase selection, modular arithmetic mod 29, Fibonacci 233, and a possible Recursive Transition Network structure**.
