# Report 03 — LP1 Matches at Both Boundaries of the LP2 Opening

The proposed 22-word reading of *Liber Primus* LP2 page 0 through block 17, **THEN**, has a numerical match with a solved LP1 passage at each end. The first seven words match a passage on LP1 page 1. The last seven match a different passage on LP1 page 10. Both pairs agree in rune count and Gematria Primus prime-value sum, and each pair's rune-index sums are related by Euler's totient function. The direction of that relation reverses between the two boundaries.

## 1. The 22-word prefix

~~~text
AS I GO, THE WEATHER TURNS COLD.
I MAY CRY NOW.
THE IDEA OF THE END IS DEATH.
SEE YOU SOON, THEN.
~~~

The comparison counts English words and ignores punctuation. The two boundary windows occupy words **1–7** and **16–22**, with **eight intervening words**. The closing window begins at **END**, crosses the proposed sentence break between **DEATH** and **SEE**, and ends exactly at **THEN**.

| Position in the prefix | Words | Passage |
|---|---:|---|
| Opening window | 1–7 | AS I GO THE WEATHER TURNS COLD |
| Intervening words | 8–15 | I MAY CRY NOW THE IDEA OF THE |
| Closing window | 16–22 | END IS DEATH SEE YOU SOON THEN |

## 2. How the comparison works

The audit compared every contiguous seven-word window in the candidate with every within-page seven-word window of the solved LP1 text on pages 0–16. The candidate contributes **16 windows** and LP1 contributes **658**, giving **10,528 possible pairs**. A candidate window can cross a line or sentence break. The LP1 search keeps each window on a single page.

For each window, the audit counted rune symbols, summed their indices in the **0–28** Gematria Primus alphabet, and summed their GP prime values. If a rune has index $i$, its GP value is the $(i+1)$st prime. For instance, **TH** is one rune with index **2** and GP value **5**.

A pair qualified when it met all three conditions.

1. The two windows contain the same number of runes.
2. Their GP prime-value sums are identical.
3. Applying Euler's totient function to one rune-index sum gives the other.

The audit applied the repository's GP spelling conventions to English, including **QU → CW**, **V → U**, **K/Q → C**, **Z → S**, **ING → NG**, and **IO → IA/IOR**. The tables show English words for readability and the rune groupings used to obtain the numerical totals.

## 3. The two matches

| Boundary | Text | Seven-word passage | Runes | Index sum | GP sum |
|---|---|---|---:|---:|---:|
| Opening | LP2 page 0, words 1–7 | AS I GO THE WEATHER TURNS COLD | 21 | **233** | **825** |
| Opening | Solved LP1 page 1 | YOU KNOW TO BE TRUE TEST THE | 21 | **232** | **825** |
| Closing | LP2 page 0, words 16–22 | END IS DEATH SEE YOU SOON THEN | 21 | **268** | **969** |
| Closing | Solved LP1 page 10 | WE HAVE WHAT WE HAVE NOW BY | 21 | **269** | **969** |

The opening match was previously documented. In the LP1 transcription used in *Strongest Plaintext Evidence*, the passage appears as **YOV CNOW TO BE TRVE TEST THE**, crossing the line break between **TRVE** and **TEST**. Its index sum of 232 comes from applying the totient to the LP2 index sum of 233.

The closing match reverses that direction. Here, the **LP1** index sum of 269 gives the **LP2** index sum of 268. Both 233 and 269 are prime, so their totients are one less than the input.

$$
\varphi(233)=232 \qquad \text{(opening, LP2 to LP1)}
$$

$$
\varphi(269)=268 \qquad \text{(closing, LP1 to LP2)}
$$

These were the **only two qualifying pairs** in the exhaustive comparison. Each boundary had one partner, on a different solved LP1 page, and the other **14 candidate windows** yielded no qualifying pair. The comparison searched all 16 positions, so the exclusive placement at the two ends is an observed feature of the result. The closing match ends at the last word of the previously documented prefix, **THEN**.

### Worked calculation for the closing match

| LP2 word | Rune grouping | Index sum | GP | LP1 word | Rune grouping | Index sum | GP |
|---|---|---:|---:|---|---|---:|---:|
| END | E · N · D | 50 | 185 | WE | W · E | 25 | 86 |
| IS | I · S | 25 | 84 | HAVE | H · A · U · E | 51 | 190 |
| DEATH | D · EA · TH | 53 | 203 | WHAT | W · H · A · T | 55 | 198 |
| SEE | S · E · E | 51 | 187 | WE | W · E | 25 | 86 |
| YOU | Y · O · U | 30 | 113 | HAVE | H · A · U · E | 51 | 190 |
| SOON | S · O · O · N | 30 | 96 | NOW | N · O · W | 19 | 55 |
| THEN | TH · E · N | 29 | 101 | BY | B · Y | 43 | 164 |
| **Total** | **21 runes** | **268** | **969** | **Total** | **21 runes** | **269** | **969** |

For example, **DEATH** has indices $23+28+2=53$ and GP values $89+109+5=203$. On the LP1 side, **HAVE** uses the rune U for V. Its indices are $8+24+1+18=51$ and its GP values are $23+97+3+67=190$. The comparison is between aggregate measurements of whole windows. The rows simply show each passage in its own word order.

## 4. Comparison with other English texts

The audit applied the same comparison to every contiguous **22-word span** in three pre-existing English corpora. For each span, it tested the **first seven** and **last seven** words against the same **658 solved LP1 windows**. A span counted as a two-boundary match if each end found a qualifying partner anywhere in those LP1 windows. The reported criterion accepts either totient direction at each end.

| English corpus | 22-word spans | At least one matching boundary | Share with at least one match | Both boundaries match |
|---|---:|---:|---:|---:|
| Shakespeare | 55,386 | 166 | 0.300% | 0 |
| Gibran | 15,712 | 61 | 0.388% | 0 |
| Emerson | 77,911 | 219 | 0.281% | 0 |
| **Combined** | **149,009** | **446** | **0.299%** | **0** |

Every corpus produced one-boundary matches. Across all three, **446 spans** matched at one end and **none** matched at both. The controls show that a single match can arise in English literary texts under the same scoring rule. The paired result specifies where both matches occur within the candidate.

The zero count needs context because single matches are already uncommon. For scale, suppose the two ends had the same match rate $q$ and matched independently. Fitting that hypothetical model to the pooled share with at least one match gives $1-(1-q)^2=446/149{,}009$. It would predict about **0.33** double-hit spans across all three corpora. This calculation illustrates how a zero count can arise at low single-hit rates. The actual control spans overlap, and the audit reports a pooled count for spans that hit at either end. Estimating a chance rate for the joint pattern would require evidence about the separate rates and their dependence.

## 5. What the match bears on

The 22-word prefix through THEN existed before the audit. The idea of treating its two boundaries as a pair arose after the closing match was found. A prospective check would need a predeclared endpoint rule, fixed LP1 reference windows, and fresh controls before another frequency comparison could be interpreted as confirmatory.

The match depends on the proposed words. The recorded **SOON** placements in rows 25 and 27 give the same word sequence through THEN and therefore the same LP1 boundary matches. Choosing between those routes requires evidence that uses the ciphertext cells or key geometry. A test for a shared cipher mechanism would specify a reversible rule independently and check whether it maps both LP1 passages to their respective LP2 partners.

## 6. Source and reproduction

The window search and literary controls are from Agent29's *P0 first-17 dual solved-LP1 boundary match*, dated 19 November 2026, in **lp2-p0-first17-dual-lp1-boundary-match.md**. The candidate prefix, earlier opening match and alternative **SOON** placements are documented in *Strongest Plaintext Evidence*. The four rune-count, index-sum and GP entries were checked separately. The search counts are reported from the audit.

The audit gives the following command to run from the root of its repository.

~~~sh
node sims/lp2_p0_first17_dual_lp1_boundary_match_sft.cjs
~~~
