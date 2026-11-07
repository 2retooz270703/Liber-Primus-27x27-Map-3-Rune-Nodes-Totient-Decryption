# Minimum Ciphertext Block Length

## 1. Proposed rule

Require **at least two runes per independently decrypted ciphertext block** when searching for continuations.

Let `N` be the number of ciphertext cells read continuously with one assigned key stream. Each cell produces one decrypted rune. Keep blocks where:

$$
N\ge2.
$$

A block may contain several English words. Count runes using the project’s **29-rune alphabet**: `TH` and `EA` each count as one rune.

### Direct implementation

Supply one independently decrypted block as a list of ciphertext cell coordinates, with one entry per rune read using the same assigned key stream. Counting cells gives the rune count directly: a decrypted `TH` or `EA` still corresponds to one cell.

Apply the test to the complete block, including all its words. A two-cell block passes when its key contains three runes.

```python
def accepts_ciphertext_block_length(cipher_cells):
    """Require at least two cells in one independently decrypted block."""
    return len(cipher_cells) >= 2


# Keep a proposed ciphertext block only if:
# accepts_ciphertext_block_length(next_cipher_cells)
```

## 2. Examples

| Independent block | Decrypted runes | Rune count | Filter result |
| :--- | :--- | ---: | :--- |
| THE | TH · E | 2 | Keep |
| I MAY | I · M · A · Y | 4 | Keep |
| I | I | 1 | Reject |

The word **I** in **I MAY** belongs to the four-rune block and receives no separate key assignment.

A three-rune key node can still decrypt a two-rune ciphertext block.
