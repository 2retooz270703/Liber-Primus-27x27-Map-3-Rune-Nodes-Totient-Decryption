# 15 — SOON

> **Recovered plaintext candidate:** `SOON`  
> **Current sequence:** `AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON`  
> **Status:** strongest current continuation after `YOU`; the primary reconstruction starts directly from the final `X(25,16)` and generates the same key through three independent `L-*-EA` structures. A second, longer mirror route independently recovers `SOON` and is treated as a supporting cross-check rather than the primary handoff.

Everything below uses the same 27×27 rune grid:

https://2retooz270703.github.io/Liber-Primus-27x27-Map-3-Rune-Nodes-Totient-Decryption/0-2-live-map.html

---

## 1. Starting state after YOU

`YOU` ends at:

```text
X(25,16)
```

The key used for `YOU` comes from:

```text
P-R-P
→ P-TH-P
```

with:

```text
signature = 12-1-12
M         = (0,+1,0)
phase     = 1
```

So the coordinate layer at the final `X` uses the same phase:

```text
p = 1
```

Before Möbius reduction:

```text
T₁(25,16)
=
(φ(25), φ(16))
=
(20,8)
=
(L,H)
```

Applying Möbius:

```text
μ(20)=0
μ(8)=0
```

therefore:

```text
V₁(25,16)=(0,0)
```

The directional selector disappears, but by the hidden-value rule the pre-Möbius values remain available:

```text
L = 20
H = 8
```

These two retained values split naturally into two local roles:

```text
L → key family
H → ciphertext endpoint
```

---

## 2. H fixes the local ciphertext from X

On row 25, starting from:

```text
X(25,16)
```

the retained rune:

```text
H = 8
```

occurs at:

```text
H(25,19)
```

exactly three cells to the right.

The cells between them are:

```text
X(25,16)
D(25,17)
W(25,18)
H(25,19)
```

So the direct local string is:

```text
CIPHERTEXT = X-D-W-H
```

A scan of all eight contiguous straight directions finds this as the only `X-D-W-H` occurrence in the 27×27 grid.

The important point is that the endpoint is not chosen from the plaintext. It is already supplied by the hidden coordinate value:

```text
T₁=(L,H)
      ↑
      H
      ↓
X → RIGHT 3 → H
```

---

## 3. The unique EA-EA-EA mirror beside the ciphertext

The ciphertext lies inside the right side of the exact horizontal mirror:

```text
EA(25,10) —5— EA(25,15) —5— EA(25,20)
```

or:

```text
EA-EA-EA
```

This is the only standard horizontal, vertical, or 45° `EA-EA-EA` mirror in the grid.

Its right arm contains the full ciphertext:

```text
EA(25,15) | X(25,16) D(25,17) W(25,18) H(25,19) | EA(25,20)
              X         D         W         H
```

The three `EA` positions of this mirror are important because each is the endpoint of a separate equal-step three-rune structure beginning with the other retained hidden value:

```text
L = 20
```

---

## 4. Three independent generators converge on the same key

### Generator A

The left `EA` of the large mirror is reached by:

```text
L(25,4) —3— C(25,7) —3— EA(25,10)
```

The center is:

```text
C = 5
```

and:

```text
φ(5)=4=R
```

so:

```text
L-C-EA
→
L-R-EA
```

### Generator B

The central `EA` is reached vertically by:

```text
L(15,15) —5— I(20,15) —5— EA(25,15)
```

The center is:

```text
I = 10
```

and:

```text
φ(10)=4=R
```

so:

```text
L-I-EA
→
L-R-EA
```

### Generator C

The right `EA` is reached by:

```text
L(25,8) —6— EO(25,14) —6— EA(25,20)
```

The center is:

```text
EO = 12
```

and:

```text
φ(12)=4=R
```

so:

```text
L-EO-EA
→
L-R-EA
```

All three structures therefore compile independently to the same key family:

```text
L-C-EA  ─┐
L-I-EA  ─┼→ L-R-EA
L-EO-EA ─┘
```

This is the strongest part of the construction: the key is not selected because it decrypts to an English word. It is produced three times by three different centers attached to the three `EA` nodes of one larger mirror.

---

## 5. A totient cross-check: C, H, I, EO

Within the positive rune-value range, the complete set satisfying:

```text
φ(n)=4
```

is:

```text
{5,8,10,12}
=
{C,H,I,EO}
```

Three of these values are exactly the three centers used by the key generators:

```text
C  → φ(C)=4=R
I  → φ(I)=4=R
EO → φ(EO)=4=R
```

The remaining member is:

```text
H = 8
```

which is exactly the hidden value that terminates the ciphertext:

```text
X-D-W-H
```

So the same four-member totient class is split across the construction as:

```text
C, I, EO → three key confirmations
H        → ciphertext endpoint
```

This relation is not required for the decryption, but it is a strong structural cross-check.

---

## 6. Determine the key phase

The common generated key is:

```text
L-R-EA
```

Its totient signature is:

```text
φ(L=20)  = 8
φ(R=4)   = 2
φ(EA=28) = 12
```

therefore:

```text
signature = 8-2-12
```

Apply Möbius:

```text
μ(8)=0
μ(2)=-1
μ(12)=0
```

so:

```text
M=(0,-1,0)
```

and:

```text
phase
=
(0-1+0) mod 3
=
2
```

Therefore:

```text
L-R-EA
→ phase 2
→ EA-L-R
```

Repeated across four ciphertext runes:

```text
KEY = EA-L-R-EA
```

No manual key rotation is needed.

---

## 7. Primary decryption

Use the established rule:

```text
P = (C - K) mod 29
```

with:

```text
Ciphertext: X   D   W   H
Key:        EA  L   R   EA
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `X=14` | `EA=28` | `14-28 ≡ 15 = S` |
| 2 | `D=23` | `L=20` | `23-20 = 3 = O` |
| 3 | `W=7` | `R=4` | `7-4 = 3 = O` |
| 4 | `H=8` | `EA=28` | `8-28 ≡ 9 = N` |

Therefore:

```text
X-D-W-H
-
EA-L-R-EA
=
S-O-O-N
```

# **SOON**

The plaintext becomes:

# **AS I GO THE WEATHER TURNS COLD I MAY CRY NOW THE IDEA OF THE END IS DEATH SEE YOU SOON**

---

## 8. Why the primary reconstruction is strong

The complete local chain is:

```text
YOU
↓
X(25,16)

phase 1
↓
T₁(25,16)=(L,H)
V₁(25,16)=(0,0)

H
↓
X-D-W-H

L
↓
three independent structures attached to EA-EA-EA
↓
L-C-EA  → L-R-EA
L-I-EA  → L-R-EA
L-EO-EA → L-R-EA

L-R-EA
↓
8-2-12
↓
M=(0,-1,0)
↓
phase 2
↓
EA-L-R-EA

X-D-W-H
-
EA-L-R-EA
=
SOON
```

This route has several independent constraints:

```text
final X from YOU
same inherited phase p=1
hidden pair (L,H)
unique local H on row 25
unique contiguous X-D-W-H
unique EA-EA-EA standard mirror
three independent key generators
one common compiled key L-R-EA
phase fixed arithmetically by Möbius
```

For that reason this is treated as the **primary reconstruction** of `SOON`.

---

## 9. Independent secondary reconstruction

A second route reaches the same plaintext through a substantially different mirror chain.

This route is longer and contains more local branch choices, so it is not used as the primary handoff. Its importance is that it independently reconstructs the same word from different ciphertext and key material.

### 9.1. Re-enter the mirror network from X

The final cell:

```text
X(25,16)
```

is the center of:

```text
E(24,16)
X(25,16)
E(26,16)
```

or:

```text
E-X-E
```

Using the previously unused upper outer gives:

```text
E(24,16)
```

That cell is itself the lower outer of:

```text
E(22,14)
TH(23,15)
E(24,16)
```

so the route enters:

```text
E-TH-E
```

The center:

```text
TH(23,15)
```

is a genuine multi-mirror hub. Besides `E-TH-E`, it is also the center of:

```text
D(22,15) —1— TH(23,15) —1— D(24,15)
```

and:

```text
X(19,19) —4— TH(23,15) —4— X(27,11)
```

From this single hub, one branch reaches the ciphertext while another reaches the key.

---

## 10. Secondary ciphertext branch

Take the radius-4 mirror:

```text
X(19,19) —4— TH(23,15) —4— X(27,11)
```

and continue through:

```text
X(27,11)
```

which is the center of:

```text
D(27,2) —9— X(27,11) —9— D(27,20)
```

The right outer:

```text
D(27,20)
```

is then the center of:

```text
P(27,16) —4— D(27,20) —4— P(27,24)
```

The left outer:

```text
P(27,16)
```

is the same `P` already used in the reconstruction of `YOU`.

Taking the opposite outer reaches:

```text
P(27,24)
```

and the grid then ends with the unique contiguous run:

```text
P(27,24)
S(27,25)
U(27,26)
W(27,27)
```

Therefore the secondary ciphertext is:

```text
CIPHERTEXT₂ = P-S-U-W
```

A scan of all eight straight directions finds this as the only contiguous `P-S-U-W` occurrence in the grid.

---

## 11. Secondary key branch

Return to the same hub:

```text
TH(23,15)
```

and take:

```text
D(22,15) —1— TH(23,15) —1— D(24,15)
```

Using:

```text
D(22,15)
```

enters the exact mirror:

```text
D(22,15) —2— NG(22,17) —2— D(22,19)
```

The opposite outer:

```text
D(22,19)
```

is the center of:

```text
IA(22,16) —3— D(22,19) —3— IA(22,22)
```

Following the left outer:

```text
IA(22,16)
```

reaches another exact mirror:

```text
IA(16,10) —3— EA(19,13) —3— IA(22,16)
```

So the key generator is:

```text
IA-EA-IA
```

Apply the center transformation:

```text
EA = 28
φ(28)=12=EO
```

therefore:

```text
IA-EA-IA
→
IA-EO-IA
```

Its totient signature is:

```text
φ(IA=27)=18
φ(EO=12)=4
φ(IA=27)=18
```

so:

```text
18-4-18
```

and:

```text
μ(18)=0
μ(4)=0
μ(18)=0
```

therefore:

```text
M=(0,0,0)
phase=0
```

The secondary key remains:

```text
IA-EO-IA
```

Repeated over four runes:

```text
KEY₂ = IA-EO-IA-IA
```

---

## 12. Secondary decryption

Use:

```text
Ciphertext: P   S   U   W
Key:        IA  EO  IA  IA
```

| # | C | K | Result |
|---:|---:|---:|---|
| 1 | `P=13` | `IA=27` | `13-27 ≡ 15 = S` |
| 2 | `S=15` | `EO=12` | `15-12 = 3 = O` |
| 3 | `U=1` | `IA=27` | `1-27 ≡ 3 = O` |
| 4 | `W=7` | `IA=27` | `7-27 ≡ 9 = N` |

Therefore:

```text
P-S-U-W
-
IA-EO-IA-IA
=
S-O-O-N
```

# **SOON**

---

## 13. Two different constructions, one plaintext

The two reconstructions are genuinely different:

```text
PRIMARY

X-D-W-H
-
EA-L-R-EA
=
SOON
```

and:

```text
SECONDARY

P-S-U-W
-
IA-EO-IA-IA
=
SOON
```

They do not reuse the same ciphertext or the same key.

The first is preferred as the actual continuation because it begins directly at the final `X(25,16)` of `YOU`, preserves the active phase, exposes the hidden values `(L,H)`, and produces its key three times independently around the local `EA-EA-EA` structure.

The second requires a longer sequence of mirror handoffs and contains unresolved branch-selection questions. It is therefore better interpreted as an **independent structural confirmation** of the plaintext rather than as the main route.

A possible interpretation is that the map deliberately contains redundancy:

```text
one local route
+
one larger mirror-network route
→
the same plaintext
```

That possibility is consistent with the repeated mirror, recursion, and self-return behavior already seen elsewhere in the reconstruction, but intentional redundancy is **not yet proven**. The evidence currently supports only the narrower statement:

```text
two structurally different constructions independently decrypt to SOON
```

---

## 14. What remains unproven

The primary construction is strongly constrained once the hidden pair:

```text
T₁(25,16)=(L,H)
```

is retained, but the exact universal rule assigning:

```text
L → key structures
H → same-row ciphertext endpoint
```

has not yet been demonstrated at another route stage.

The secondary construction has a different weakness: several mirror-network branch choices still need a general selector, especially the choice of:

```text
IA(22,16)
```

rather than:

```text
IA(22,22)
```

inside:

```text
IA-D-IA
```

So the current hierarchy of evidence is:

```text
SOON plaintext          = very strong
primary X-based route   = strongest current derivation
secondary mirror route  = independent supporting cross-check
universal post-YOU rule = still incomplete
```
