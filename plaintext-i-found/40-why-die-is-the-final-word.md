# 40 — Why the DIE Branch Stops

The proposed reading ends with **GO DO AS I ASK DIE**. With editorial punctuation, it reads **“Go, do as I ask. Die.”** The final imperative fits the preceding instruction. Under Reports 00–18, the reference Hunspell check admits `JAB` and the segmented reading `EA AB` after `DIE`. Either placement leads to a geometric contradiction on the following step. The historical `JOES` example gives the same contradiction if that spelling is admitted. With Report 19 added, the search stops at `DIE` itself. The full replay under 00–27 also finds a terminal `WINGING` branch from `I ASK`. This walkthrough examines the stopping condition for the specified `DIE` placement. [Both terminal routes](../Start-reading-here/27-key-alignment-from-node-geometry.md) [Block 39 — DIE](39-DIE.md)

## 1. What the search finds after DIE

The starting point is the fixed geometry of Block 39. Its original key node is `(18,10) → (18,14) → (18,18)`. Its three ciphertext cells are read down-right from `(3,22)` to `(5,24)`. The aligned key is `(23,27,5)` and subtracts from `(17,8,23)` modulo 29 to give `(23,10,18)`, or `D · I · E`. The state at `DIE` is phase $p=1$, accumulated phase $S=33$, and outer state $a=0$.

For the next block, the enumeration uses the straight, contiguous ciphertext segments and admissible source nodes of the project. A **geometry** is an ordered ciphertext segment paired with three physical source cells. A **key assignment** is a geometry paired with a distinct aligned key. A geometry can support more than one key assignment.

| Filters applied after DIE | Geometries | Key assignments | Ordered ciphertext segments |
| :--- | ---: | ---: | ---: |
| Reports 00–15 | 912 | 1,064 | 152 |
| Add Report 17 | 760 | 912 | 152 |
| Add Report 18 | **15** | **18** | **3** |
| Add Report 19 | **0** | **0** | **0** |

The 18 assignments under Report 18 give 18 distinct rune strings. The counts in the table precede the whole-word check from [Report 16](../Start-reading-here/16-whole-word-block-boundaries.md).

## 2. Why the example placements cannot continue

The `JAB` and `JOES` rune outputs both come from the upward ciphertext segment `(3,26) → (2,26) → (1,26)`. It contains `P · X · W`, with indices `(13,14,7)`.

| Reading | Original key node | Aligned key | Decrypted rune indices |
| :--- | :--- | :--- | :--- |
| `JAB` | `(10,17), (15,17), (20,17)` | `(2,19,19)` | `(11,24,17)` → `J · A · B` |
| `JOES` | `(8,17), (15,17), (22,17)` | `(2,21,21)` | `(11,22,15)` → `J · OE · S` |

Both nodes have the original center $M=(15,17)$ with rune index $h=6$. Both readings have phase $p=1$. The two readings therefore supply the same inputs to the relevant parts of [Report 03](../Start-reading-here/03-predicting-axis-and-reading-direction.md) and [Report 05](../Start-reading-here/05-predicting-next-ciphertext-row-parity.md).

Report 03 gives a diagonal axis and requires the leftmost cell to be read last. With the notation of that report,

$$
q=\mu(650+395)+\mu(\gcd(702,704))=-1-1=-2,
\qquad
\tau=(\mu(28)+\varphi(6))\bmod2=0.
$$

On either allowed leftward diagonal the next endpoint $E'$ is the next leftmost cell $L'$. Report 05 predicts an odd row for $E'$ and an even row for $L'$. The same cell cannot have both row parities. This leaves **zero admissible ciphertext segments** after either `JAB` or `JOES`, regardless of the next key or plaintext.

The reference Hunspell dictionary admits `JAB` and `EA AB` when word breaks are allowed between runes. The `EA AB` reading uses the same upward segment with key center `(7,17)` and gives the same odd/even contradiction. The geometric check in the next section applies to every placement independently of the lexicon. [Dictionary details](../Start-reading-here/16-whole-word-block-boundaries.md#4-applying-the-rule-during-searches)

## 3. Why Report 19 stops the search at DIE

The [two-distance rule](../Start-reading-here/19-predicting-next-ciphertext-start-distance.md) uses the start of the previous block `I ASK`, $B_{\rm prev}=(5,17)$, and the current `DIE` geometry:

$$
B=L=(3,22),\qquad E=(5,24),\qquad U=(18,10).
$$

$U$ is the first original key cell in row-column order. The two inputs to the forecast are

$$
\begin{aligned}
n_2(B)\oplus n_2(B_{\rm prev}) &= 654\oplus605=211,
& 211\bmod7 &=1,\\
n_0(U)+n_0(E) &=469+132=601,
& \mu(601)&=-1.
\end{aligned}
$$

Since $601$ is prime, the negative-Möbius bit is $1$. The XOR divisibility bit is $0$. The bits differ, so any next start must be **farther than seven cells from both** $B$ and $L$ in Chebyshev distance.

| Segment surviving Report 18 | Length | Distance from each of $B$ and $L$ | Report 19 |
| :--- | ---: | ---: | :--- |
| `(3,26) ↑ (1,26)` | 3 | 4 | Fails |
| `(5,24) ↑ (1,24)` | 5 | 2 | Fails |
| `(7,26) ↑ (1,26)` | 7 | 4 | Fails |

Each arrow represents a contiguous segment including both endpoints. All three starts are too close. The full set of **15 geometries and 18 aligned-key assignments** is therefore eliminated before any word check.

## 4. Reproducing the two contradictions

The Python code checks both recorded calculations from the listed geometry. The counts in Section 1 come from the full candidate enumeration.

```python
from math import gcd


def mobius(n):
    """Evaluate the Möbius function for a positive integer."""
    sign = 1
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            if n % factor == 0:
                return 0
            sign = -sign
        factor += 1
    return -sign if n > 1 else sign


def rotated_indices(cell):
    r, c = cell
    n0 = 27 * (r - 1) + c
    n1 = 27 * (c - 1) + 28 - r
    return n0, n1, 730 - n0, 730 - n1


def chebyshev(first, second):
    return max(abs(first[0] - second[0]), abs(first[1] - second[1]))


def decrypt(ciphertext_indices, aligned_key):
    return tuple((ciphertext - key) % 29
                 for ciphertext, key in zip(ciphertext_indices, aligned_key))


# Both JAB and JOES have the same B, E, M, original center index and phase.
assert decrypt((13, 14, 7), (2, 19, 19)) == (11, 24, 17)
assert decrypt((13, 14, 7), (2, 21, 21)) == (11, 22, 15)
beginning, endpoint, center = (3, 26), (1, 26), (15, 17)
original_center_index, phase = 6, 1
center_totient = sum(gcd(i, original_center_index) == 1
                     for i in range(1, original_center_index + 1))
_, _, begin_180, _ = rotated_indices(beginning)
_, end_90, end_180, end_270 = rotated_indices(endpoint)
center_0, _, center_180, _ = rotated_indices(center)

axis_score = mobius(begin_180 + center_0) + mobius(gcd(end_90, end_180))
leftmost_first = (mobius(end_270) + center_totient) % 2

next_center_row = (1 + beginning[1] + endpoint[0] + center[0]
                   + mobius(begin_180)) % 2
next_end_row = (1 + phase + mobius(center_180)) % 2
next_left_row = (next_center_row + 1 + phase + mobius(center[0])) % 2

assert axis_score < 0 and leftmost_first == 0
assert (next_end_row, next_left_row) == (1, 0)


# Report 19 applied to the preceding block DIE.
previous_beginning = (5, 17)
beginning = leftmost = (3, 22)
endpoint, upper_key_end = (5, 24), (18, 10)
start_xor = rotated_indices(beginning)[2] ^ rotated_indices(previous_beginning)[2]
index_sum = rotated_indices(upper_key_end)[0] + rotated_indices(endpoint)[0]
divisible_by_seven = start_xor % 7 == 0
negative_mobius = mobius(index_sum) < 0
near_required = divisible_by_seven == negative_mobius

assert (start_xor, index_sum, near_required) == (211, 601, False)
starts = ((3, 26), (5, 24), (7, 26))
assert all(chebyshev(start, beginning) <= 7
           and chebyshev(start, leftmost) <= 7 for start in starts)
print("JAB and JOES require opposite row parities for the same cell.")
print("Report 19 excludes all three starts after DIE.")
```

## Conclusion

**DIE is terminal for the tested branch under the rules through Report 19.** Reports 03 and 05 also explain why the illustrated placements from the earlier filters cannot lead to a further block. The conclusion uses the fixed placement of `DIE`, the project's segment conventions and the empirical filter in Report 19. It supports reading `DIE` as the last word of this proposed route.
