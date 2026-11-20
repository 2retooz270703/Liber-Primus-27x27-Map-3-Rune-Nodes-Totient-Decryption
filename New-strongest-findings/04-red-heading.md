# Report 4 — The Red Heading on LP2 Page 0

**Source repository:** [FlareZ123 / liber-primus](https://github.com/FlareZ123/liber-primus)

**Agents 28 and 29, 18 November 2026. Classification:** intermediate evidence with a substantially stronger internal checksum structure. A source-selected 27×27/totient construction reproducibly yields the final five raw runes `R-A-T-I-O`. Agent29 found that the physical 13-dot mark's **4-5-4** stencil supplies a length ladder `3,4,5,8,13` matching the second key, first key, second word, first word, and full title. The GP-index sums of those same five objects are `15,42,57,99,156`, an exact additive recurrence, with the final 156 independently closing as `13*phi(13)`. This recurrence selects the same `X-N-X-C` first-key rectangle from a finite anchor-symmetry family without MAP and without a numeric 3:1 aspect guess. Exact forward reconstruction yields the raw 13-rune candidate `S-E-C-U-E-N-D-I | R-A-T-I-O`. The demonstrated English-source GP register fails the physical 8+5=13 grouping and the additive checksum chain, while a coherent direct Latin-letter register preserves both. This makes the direct Latin register internally selected by the artifact, although the equal-radius geometry and lexical interpretation still require independent validation before plaintext status is promoted.

## Original marked region

The physical p0 red heading is exactly 13 GP29 runes in an 8+5 grouping:

```
S H E O G M IA F | S Y E NG C
```

It is followed by a large red 13-dot delimiter. The canonical p0-p2 corpus begins with those 13 runes.

The first eight runes have the MAP-free additive-symmetry candidate output:

```
S E C U E N D I
```

The final five have the source-derived geometric output:

```
R A T I O
```

These rune sequences are exact arithmetic outputs. Their interpretation as Latin words is a separate claim and is constrained by GP orthography.

## The delimiter system uniquely selects a 27×27 span

Across LP2 there are nine page-start red title spans immediately followed by a red 13-dot mark. Eight have a later red 13-dot mark and therefore define a finite title-start-to-next-red13 span.

Those eight rune counts are:

```
729, 119, 20, 1021, 1433, 91, 308, 85
```

Only the first is a perfect square:

```
p0 title start -> p2 terminal red13 = 729 = 27² runes
```

Thus the manuscript's own rubrication uniquely identifies the p0-p2 span as square-sized among the comparable red-title/red13 sections. Reshaping that selected span row-major is still an interpretive step, but choosing the first three pages after noticing 729 is no longer necessary.

## Source geometry for the final five runes

Let the visible red delimiter count be `n=13`. Solved LP explicitly states that the totient function is sacred, so:

```
phi(13) = 12
```

Use the ordered coordinate `(n,phi(n))=(13,12)` in the 27×27 matrix. The original rune there is **J**.

The final red group has visible length 5. Use 5 as a diagonal stride and test all four sign directions for two equal steps from J. Exactly one direction satisfies the internal relation `phi(rune(middle)) = rune(end)`:

```
J(13,12) -> R(18,17) -> TH(23,22)
              +5,+5            +5,+5

phi(index(R)) = phi(4) = 2 = index(TH)
```

Applying the center-totient operation gives:

```
J - R - TH  ->  J - TH - TH
```

Subtract that repeating key modulo 29 from the untouched final five red ciphertext runes:

```
S  Y  E  NG C
J  TH TH J  TH
--------------
R  A  T  I  O
```

Forward addition exactly reconstructs the source.

The coordinate-order control matters. Swapping the anchor to `(phi(n),n)=(12,13)` also produces a southeast phi-chain, but its derived key outputs `AE-R-AE-TH-EO`. The natural ordered-pair convention therefore remains one assumption.

Reproducer: `sims/lp2_p0_red_ratio_sourceonly_sft.cjs`.

## Register selection: English-source spelling fails the source numbers

The source-calibrated GP spelling gate, `sims/lp2_native_gp_source_orthography_sft.cjs`, reconstructs 181 authenticated solved LP1 words and all 95 clear p57 runes. In that demonstrated English register, `IO` compresses to IA/IOR and `QU` is written C-W. The proposed phrase would therefore be:

```
SEQUENDI RATIO
S E C W E N D I | R A T IA
```

That encoding has word lengths **8+4=12** and GP-index sums **105+71=176**. It conflicts with the physical red grouping **8+5=13**, the adjacent 13-dot mark, the marker/object length ladder `3,4,5,8,13`, and the additive sum chain `15,42,57,99,156`.

A coherent direct Latin-letter register instead reads each decrypted rune as one Latin letter, retaining U and separate I/O and using the existing C/K rune for unavailable Q. It maps `SEQUENDI RATIO` to the exact raw 13-rune sequence and preserves every physical length and every sum relation above.

This materially changes the earlier orthography objection. The artifact's own numbers discriminate **against the English-source digraph register and in favor of the direct Latin-letter register** if the lexical reading is correct. An authenticated external runic-Latin QU/IO control would still be valuable, but it is no longer the only route to choosing the register: the original p0 counts and held-out checksum architecture select it internally.

## Original p0 artwork gives an independent reversal cue

The exact original p0 JPEG (`resources/liber-primus/17.jpg`) contains two very large black illustrations at diagonally opposite page positions. A source-pixel connected-component test isolates them as the only two black components above 100,000 pixels. Their tight boxes are **490×1254** pixels each; their binary masks agree at **0.9858 IoU after a 180° rotation**. Their centroids sum to `(2399.077, 3598.992)`, while the 2400×3600 page's exact 180° center condition is `(2399,3599)`.

Thus the page itself visibly and quantitatively demonstrates a 180° reversal before any candidate plaintext is read. This does not by itself specify a cipher, but it independently motivates two operations used below: pairing opposite rectangle corners and reversing the first eight red ciphertext runes. The result is reproduced directly from original JPEG pixels by `sims/lp2_p0_artwork_rot180_symmetry_sft.py`.

## First eight: anchor symmetry plus an additive checksum chain

The original-image punctuation census, `sims/lp2_original_color_dots_census_sft.py`, establishes that every physical 13-dot mark uses the same **4-5-4** column stencil. At p0 that gives five natural counts:

```
3  = number of columns
4  = one outer-column height
5  = center-column height
8  = both outer columns together
13 = all dots
```

Those counts exactly match the primitive object lengths in the candidate construction:

```
3  = J-TH-TH second key
4  = X-N-X-C first key
5  = final red word
8  = first red word
13 = complete red title
```

This correspondence is source-visible and removes the earlier need to interpret `RATIO` as a literal numeric 3:1 rectangle instruction.

Use only the source-derived anchor `J=(13,12)` and the mark's bilateral symmetry. Enumerate every pair of equal original runes that can serve as opposite corners of an axis-aligned rectangle and are at equal squared distance from J. Across the complete 27×27 p0-p2 source grid there are exactly **72** such symmetric rectangles.

The final-five source derivation already fixes two numerical objects before the first word is touched:

```
sum(J-TH-TH) = 15
sum(R-A-T-I-O) = 57
```

The visible title itself has the additive length relation `5+8=13`, so test the corresponding backward additive sum rule. If the second plaintext sum is the sum of the two key sums, the first-key corner sum must be:

```
57 - 15 = 42
```

Only **two of the 72** symmetric rectangles have corner sum42:

```
rows 6..24, cols 3..9   -> X-N-X-C
rows 9..14, cols 5..20  -> G-H-G-OE
```

A useful held-out property appears here: **both** sum42 survivors have exact 3:1 aspect ratios, even though aspect ratio was not used to construct the 72-rectangle family or to select sum42. Only 9 of the 72 symmetric rectangles are 3:1. Thus the earlier `RATIO -> 3:1` observation reappears downstream as a consequence rather than an input.

Continue the same recurrence one term. The first plaintext must then have sum:

```
42 + 57 = 99
```

For those two rectangles, exhaust every corner start, clockwise/counter-clockwise traversal, forward/reversed first ciphertext, and plus/minus GP29 arithmetic. This is 64 configurations. Exactly **eight** have plaintext sum99, and **all eight use the X-N-X-C rectangle with subtraction**. They collapse to four distinct rune sequences:

```
SECUENDI
IDNEUCES
UORDNGXPL
LPXNGDROU
```

Exactly two symmetry-equivalent configurations give `SECUENDI`; both reverse the original first-word ciphertext and use the same repeating `X-N-X-C` key. Forward addition exactly reconstructs the source.

The original artwork now removes the ciphertext-direction choice independently: use the demonstrated **180° reversal**. Keep the **subtraction** direction already fixed by the source-only second-word derivation. The remaining conventional rectangle read is upper-left → upper-right → lower-right → lower-left, giving `X-N-X-C` directly. Under these choices, the first eight raw runes are `SECUENDI` without consulting a language score. The only nontrivial geometric premise still needing independent authorship is the equal-rune/equal-radius rectangle-family rule.

The selection above does **not** use the full-title sum. After selecting X-N-X-C and the sum99 first-word family, the resulting complete candidate closes on:

```
15, 42, 57, 99, 156
    15+42=57
       42+57=99
          57+99=156

156 = 13 * phi(13)
```

Thus `156=13*12` is now a held-out closure of the recurrence rather than the selector that found the rectangle.

The remaining premise is geometric: why should equal-rune opposite corners equidistant from the source anchor define the first key? The symmetric 4-5-4 mark and the already-source-derived J anchor motivate that finite family, while no signed Cicada instruction explicitly states the rule. This is materially stronger than the previous 3:1 interpretation, but it remains intermediate evidence until the same mechanism predicts untouched original ciphertext or a source clue names the symmetry operation.

## Prospective recurrence continuation: 255 meets the p50 table boundary

The five-object title construction above had already frozen the additive sums `15,42,57,99,156`. Continuing the same recurrence one term gives **99+156=255**. The original pp49–51 numerical object contains exactly **256 cells**, so 255 is its terminal **zero-based** address; a one-based table would terminate at 256 instead. Because the printed table has exactly 8 columns, the same addresses have the compact octal/row-major forms **`017,052,071,143,234,377`**, ending at row 31, column 7, the physical lower-right cell. This is a manuscript-internal cross-link conditional on the title construction. The table resource predates the strengthened title recurrence in repository history, and 255 was not used to derive the table's 32×8 cardinality.

The immediate receiver is negative. Reading the recurrence values as zero-based row-major table addresses `[15,42,57,99,156,255]` gives printed tokens `3W 0S 1w 0Y 0q 1K`, canonical bytes `[212,28,118,34,52,80]`, and GP29 residues `N-EA-TH-C-D-OE`. The equally direct rival “locate each recurrence number as a table byte value” also stops: value 99 is absent, while 42 occurs twice and 156 three times; only 15, 57 and 255 are unique. No phase, alternate traversal, arithmetic sign, or nearby index was tried.

**Scope:** this does not authenticate the conditional `SEQUENDI RATIO` title and does not turn the p50 table into a decoder. It supplies a prospective consequence of the already-frozen recurrence and gives conditional manuscript-internal support to viewing the 256-cell table as a zero-based address space. The separate historical audit still finds no Cicada-authored 2012–2014 zero-based row-major convention. Director #1612 has now performed that source-receiver audit. Original cell255 is ordinary lower-right token `1K`, visually unmarked relative to the table, and the same physical page continues below with black runic text. No first-party LP2 instruction or authenticated 2012–2016 Cicada convention reviewed by #1570 names cell255, a terminal-table receiver, or zero-based row-major addressing. The recurrence therefore stops here as a **conditional zero-origin cross-link**, not an executable handoff. Do not tune neighboring cells, alternate recurrences, traversals, token radices, or table walks absent a new independent receiver clue. The referenced #1612 source-gate note, `lp2-p0-title-recurrence-p50-cell255-source-gate.md`, is absent from this project archive.

Reproducer: `sims/lp2_p0_title_recurrence_p50_255_sft.cjs`.

## Recurrence residues do not supply a direct GP29 body key

The same frozen checksum recurrence also has a cheap direct-cipher consequence. Continuing the recurrence modulo 29 from the already fixed first two terms 15 and 42 produces the exact period-14 residue stream

```
15,13,28,12,11,23,5,28,4,3,7,10,17,27
S, P, EA, EO, J, D, C, EA, R, O, W, I, B, IA
```

because terms 14 and 15 return to residues 15 and 13. I tested this complete finite key family on the original p0-p2 ciphertext before inspecting any candidate plaintext: whole 729-rune chapter and 716-rune post-heading body, both additive signs, and all 14 phases. All **56** direct variants remain ciphertext-like; the maximum ordinary GP29 IoC is **0.0356526155408837** on the 716-rune body, sign +1, phase12, close to the uniform baseline **1/29 = 0.0344827586**. Exact inverse re-encryption is asserted for every variant.

The authenticated p56 transparent-plaintext-F rule is even more decisive here. Across the same two targets, two signs and fourteen phases, **0/56** variants have a legal complete inverse: every path eventually maps a non-F ciphertext rune to forbidden plaintext F. The source-natural continuation immediately after the five observed checksum terms is included in this exhaustive phase set.

**Scope:** this closes only the simplest interpretation in which the title's additive checksum sequence itself becomes a repeating GP29 additive key. It does not weaken the 255→p50 address coincidence above, the conditional title construction, or a different source-authored operation on the recurrence values. Do not tune nearby phases, signs, F exceptions or partial windows; the full finite direct family is already covered.

Reproducer: `sims/lp2_p0_secuendi_recurrence_key_gate_sft.cjs`. Windows Node 22 CI: [run 44398637616](https://github.com/FlareZ123/liber-primus/actions/runs/44398637616).

## Independent MAP corroboration of the same second-key node

The published stage-28 MAP source center is `M=(16,9)`, with endpoint `E=(17,13)`. The affine extrapolation:

```
R = 2E - M = (18,17)
T = 2R - J = (23,22)
```

lands on the same original `R,TH` pair used by the source-only 5-stride construction. Across every eligible prefix endpoint of the frozen first-38 route, 20 extrapolations remain in bounds and exactly one satisfies `phi(rune(R))=rune(T)`: stage 28 MAP at its three-rune endpoint.

Chronology reduces hindsight concerns:

- standalone stage-28 `MAP` first appears on **26 October 2026** at commit `d6d82764bae48db306fd779c0d555f15260f8343`;
- the red-heading report first appears on **30 October 2026**;
- `MAP LIFE` first appears on **4 November 2026** at commit `2f0c928e14d1338ea3f60ff0d19ffbd98900def8`.

Thus MAP and its endpoint predate the red-heading construction. This corroborates the geometry while leaving the route's earlier transition ambiguity unresolved.

## Full-title checksum: held-out recurrence closure

The complete raw candidate has GP29 index sum156. In the strengthened construction, 156 is not used to select a rectangle or first-word sum. The recurrence is driven backward from the independently derived second key and second raw word:

```
K2 = 15
P2 = 57
K1 = P2 - K2 = 42
P1 = K1 + P2 = 99
```

Only after those choices are made does the full title give:

```
P1 + P2 = 156 = 13 * phi(13)
```

The exact closure is therefore a genuine internal cross-check of the declared recurrence family. The recurrence itself was discovered after the candidate heading existed, so it still requires prospective validation before it can authenticate plaintext.

## Plausible intended solve path

The mechanism now has a human-visible causal sequence rather than a collection of fitted cipher layers.

1. The p0 red title is visibly **8+5 runes** followed by **13 dots**. The red13 delimiter system uniquely makes the p0-p2 span **729=27²**, inviting a square.
2. The manuscript explicitly treats the totient as sacred. The visible 13 gives `phi(13)=12`, so the ordered source coordinate **(13,12)** selects J. The visible five-rune second word supplies stride5; testing the four finite sign directions gives one `J -> R -> TH` phi-chain and exact raw `R-A-T-I-O`.
3. The same original p0 page visibly demonstrates **180° reversal**: its two large black illustrations are near-pixel-identical rotated counterparts centered on the physical page. This supplies an independent reason to reverse the first red word and to inspect opposite-pair geometry.
4. The physical 13-dot mark is **4-5-4**. Its natural counts `3,4,5,8,13` match the two key lengths, two word lengths and full-title length.
5. The signed 2016 Cicada message says that Liber Primus's **words are the map, their meaning is the road, and their numbers are the direction**, while warning against false paths. Once the second raw word reads as `RATIO`, using the title's source numbers as a selector is therefore historically motivated rather than arbitrary.
6. Around the source-selected J anchor, the page's reversal/symmetry cue defines the bounded equal-rune/equal-radius opposite-corner family. The independently fixed sums15 and57 force first-key sum42. Only two of 72 symmetric rectangles survive, and both unexpectedly have held-out 3:1 aspect. The next additive term99 leaves only X-N-X-C.
7. Keep the page-indicated reversal and the already-fixed subtraction direction; read the rectangle by the ordinary UL→UR→LR→LL perimeter convention. The first word becomes raw `SECUENDI`, with exact forward reconstruction.
8. The final title sum closes held out at `156 = 13*phi(13)`. The demonstrated English GP spelling would destroy the physical and numerical structure; the direct Latin-letter register preserves all of it and reads the candidate as **SEQUENDI RATIO**, approximately “method/plan of following.”

This route is consistent with known Cicada design practice inside Liber Primus. The solved LP1 “Some Wisdom” artifact contains a 5×5 numerical square with exact 180° rotational symmetry and common row/column/diagonal sums, and its JPEG is itself byte-palindromic around a hidden reversed-hex center payload. Symmetry plus sum invariants are therefore demonstrated creator-facing validation devices, although that prior artifact does not prove this p0 construction.

The unresolved point is now narrow: the page does not literally state “choose equal-rune opposite corners equidistant from J.” The visual 180° pairing and signed number-direction hint motivate it, while a prospective untouched-cipher consequence would authenticate it. Direct 3:1 body interleaving, 3:1 diagonal repeating keys, 180° grid sum/difference, recurrence-position reads, and immediate Fibonacci-length body checks have all been tested and remain ciphertext-like, so those simple continuations are retired.

## Current decision

The strongest current chain is:

1. original rubrication uniquely selects the 729-rune p0-p2 square-sized span;
2. original counts plus totient give the selective `J-R-TH` diagonal and exact five-rune output `R-A-T-I-O`;
3. the physical 4-5-4 mark yields the object-length ladder `3,4,5,8,13`;
4. the corresponding objects have sums `15,42,57,99,156`, an exact additive recurrence;
5. inside all 72 equal-rune/equidistant-J rectangle symmetries, the recurrence first reduces the first key to two sum42 rectangles and then uniquely selects the `X-N-X-C` rectangle through the required first-word sum99;
6. complete-word orientation yields exact raw `S-E-C-U-E-N-D-I` and exact forward reconstruction;
7. the full-title sum closes independently at `156=13*phi(13)`;
8. the older MAP route independently lands on the same geometry;
9. source-English GP orthography yields 8+4=12 runes and sums 105+71=176, breaking the source counts and recurrence; the direct Latin-letter register yields exactly 8+5=13 and preserves the full numerical architecture.

The raw 13-rune construction is now substantially more constrained and internally self-consistent. The main remaining gap is the equal-rune/equal-radius geometry rule; an external Latin control would strengthen the register interpretation but the artifact's own numbers already discriminate between the two candidate spelling registers. A prospective untouched-cipher consequence is still required before calling the title established plaintext.

## Reproduction references

The commands refer to the original analysis workspace. The `sims/` scripts and their source images are absent from this project archive.

```
node sims/lp2_p0_red_ratio_sourceonly_sft.cjs
node sims/lp2_p0_red_heading_raw13_register_geometry_sft.cjs
node sims/lp2_p0_red_heading_sequendi_ratio_gate_sft.cjs
python sims/lp2_original_color_dots_census_sft.py
python sims/lp2_p0_artwork_rot180_symmetry_sft.py
```

The first script derives the five-rune raw output and square selector. The Agent29 script now enumerates all 72 source-anchor symmetric rectangles, proves the `15,42,57,99,156` additive chain, selects X-N-X-C without a 3:1 aspect assumption, verifies the held-out `13*phi(13)` closure, checks exact reencryption, and reproduces the source-native/direct-Latin register split. The third preserves MAP-route corroboration. The image census independently establishes the physical 4-5-4 stencil.

External numerical proposal credited for the candidate heading constructions:
https://github.com/2retooz270703/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption

Historical red-heading snapshot inspected: `ca96de9d14a9743cd6d53c612e41f4919a52b3bb` (30 October 2026).
