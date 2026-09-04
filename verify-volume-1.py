#!/usr/bin/env python3
"""
verify-volume-1.py

Reproducibility verifier for:
    SOLUTION 0-2 — Volume 1
    Cicada 3301 / Liber Primus pages 0–2

PURPOSE
-------
This script checks the core *reproducible* claims in Volume 1 against the
machine-readable 729-rune dataset:

    liber-primus-0-2-729-runes.txt

It intentionally separates:
  1. source-data / geometry checks,
  2. deterministic arithmetic checks,
  3. supporting numerical checks,
  4. interpretive/statistical claims that are NOT verified here.

A PASS means only that the stated operation reproduces the stated result from
the local dataset and the explicit rules encoded below. It does NOT mean that
Cicada 3301 has officially confirmed the proposed plaintext.

NO THIRD-PARTY DEPENDENCIES
---------------------------
Python 3 standard library only. No network access is required.

DATA / NOTATION
---------------
- Matrix coordinates are 1-based: (row, column).
- The 729 tokens are read row-wise into a 27×27 matrix.
- Tokens such as U/V, C/K, S/Z and IA/O each represent ONE rune.
- Core arithmetic uses the standard 0-based Gematria Primus index 0..28.
- Decryption is P = C - K (mod 29).
- Euler's totient is phi(n); phi(0) is intentionally undefined here.
- Möbius is mu(n).

SOURCE-FIDELITY NOTES
---------------------
The verifier follows the local transitions stated/shown in Volume 1. It does
NOT invent a universal movement rule where Volume 1 does not state one.

In particular:
- Stage 1 RIGHT 14 is checked from the left edge of AE-J-EA at (13,11).
- Stage 2 RIGHT 10 is checked from the left edge/final X of X-OE-X at (14,4).
- WEATHER is checked by reading the 5 highlighted row cells beginning at the
  central NG (14,14): NG-P-EO-O-E.
- TURNS is checked by reading upward from A(14,19).
- COLD is checked by reading upward from G(14,7).
- H-NG-C/K is used directly as the TURNS key, matching Volume 1; it is not
  silently center-compiled by phi.

Repository snapshot integrity:
- The expected normalized SHA-256 below fingerprints the verified 27×27 Latin
  token transcription. It is an integrity check for this repository snapshot,
  not proof of provenance by itself.

External transcription cross-check used when preparing the repository:
https://github.com/relikd/LiberPrayground/blob/main/pages/p0-2.txt
"""

from __future__ import annotations

import argparse
import hashlib
import math
import sys
from pathlib import Path
from typing import Iterable, Sequence


# ---------------------------------------------------------------------------
# Gematria Primus — standard 0-based order used by Volume 1
# ---------------------------------------------------------------------------

GP_TOKENS: tuple[str, ...] = (
    "F", "U/V", "TH", "O", "R", "C/K", "G", "W", "H", "N",
    "I", "J", "EO", "P", "X", "S/Z", "T", "B", "E", "M",
    "L", "NG", "OE", "D", "A", "AE", "Y", "IA/O", "EA",
)

GP_INDEX = {token: i for i, token in enumerate(GP_TOKENS)}
INDEX_TO_TOKEN = {i: token for token, i in GP_INDEX.items()}

MATRIX_SIZE = 27
EXPECTED_TOKEN_COUNT = 729
EXPECTED_NORMALIZED_SHA256 = (
    "8db8d16dfb109f6757c20ab6dc61c051ffc13255b2ee0d4ba98716859835efa7"
)


# ---------------------------------------------------------------------------
# Small deterministic math helpers
# ---------------------------------------------------------------------------

def euler_phi(n: int) -> int:
    """Euler's totient φ(n), defined here for n >= 1."""
    if n < 1:
        raise ValueError("phi(n) is defined here only for n >= 1")

    result = n
    x = n
    p = 2

    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1

    if x > 1:
        result -= result // x

    return result


def mobius_mu(n: int) -> int:
    """Möbius μ(n), defined for n >= 1."""
    if n < 1:
        raise ValueError("mu(n) is defined only for n >= 1")
    if n == 1:
        return 1

    x = n
    prime_factor_count = 0
    p = 2

    while p * p <= x:
        if x % p == 0:
            x //= p
            prime_factor_count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1

    if x > 1:
        prime_factor_count += 1

    return -1 if prime_factor_count % 2 else 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


def nth_prime(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ---------------------------------------------------------------------------
# Dataset and matrix helpers
# ---------------------------------------------------------------------------

def load_matrix(path: Path) -> list[list[str]]:
    text = path.read_text(encoding="utf-8")
    nonempty_lines = [line.strip() for line in text.splitlines() if line.strip()]
    matrix = [line.split() for line in nonempty_lines]
    return matrix


def normalize_matrix_text(matrix: Sequence[Sequence[str]]) -> str:
    """Stable line-ending-independent representation for integrity hashing."""
    return "\n".join(" ".join(row) for row in matrix) + "\n"


def matrix_sha256(matrix: Sequence[Sequence[str]]) -> str:
    normalized = normalize_matrix_text(matrix).encode("utf-8")
    return hashlib.sha256(normalized).hexdigest()


def flat_matrix(matrix: Sequence[Sequence[str]]) -> list[str]:
    return [token for row in matrix for token in row]


def cell(matrix: Sequence[Sequence[str]], coord: tuple[int, int]) -> str:
    """Read a 1-based (row, column) coordinate."""
    r, c = coord
    if not (1 <= r <= len(matrix)):
        raise IndexError(f"row out of bounds: {r}")
    if not (1 <= c <= len(matrix[r - 1])):
        raise IndexError(f"column out of bounds: {c}")
    return matrix[r - 1][c - 1]


def move(
    coord: tuple[int, int],
    *,
    dr: int = 0,
    dc: int = 0,
) -> tuple[int, int]:
    r, c = coord
    return r + dr, c + dc


def read_direction(
    matrix: Sequence[Sequence[str]],
    start: tuple[int, int],
    *,
    dr: int,
    dc: int,
    length: int,
) -> list[str]:
    return [
        cell(matrix, (start[0] + i * dr, start[1] + i * dc))
        for i in range(length)
    ]


def read_row_major(
    matrix: Sequence[Sequence[str]],
    start: tuple[int, int],
    length: int,
) -> list[str]:
    """Read row-wise and wrap from column 27 to the next row."""
    width = len(matrix[0])
    start_index = (start[0] - 1) * width + (start[1] - 1)
    flat = flat_matrix(matrix)
    end_index = start_index + length
    if start_index < 0 or end_index > len(flat):
        raise IndexError("row-major read exceeds matrix")
    return flat[start_index:end_index]


def row_major_end(
    start: tuple[int, int],
    length: int,
    width: int = MATRIX_SIZE,
) -> tuple[int, int]:
    start_index = (start[0] - 1) * width + (start[1] - 1)
    end_index = start_index + length - 1
    return end_index // width + 1, end_index % width + 1


# ---------------------------------------------------------------------------
# Cipher helpers
# ---------------------------------------------------------------------------

def rune_index(token: str) -> int:
    try:
        return GP_INDEX[token]
    except KeyError as exc:
        raise KeyError(f"unknown GP token: {token!r}") from exc


def rune_for_index(index: int) -> str:
    return INDEX_TO_TOKEN[index % 29]


def compile_center_with_phi(node: Sequence[str]) -> list[str]:
    """
    K = (a, phi(b), c)

    Only valid when the center rune's index is >= 1 and phi(index(b))
    maps directly back into the 0..28 GP index range.
    """
    if len(node) != 3:
        raise ValueError("node must contain exactly 3 runes")
    a, b, c = node
    center_value = rune_index(b)
    transformed = euler_phi(center_value)
    return [a, rune_for_index(transformed), c]


def key_phase(key: Sequence[str]) -> int:
    """
    p = Σ mu(phi(index(k_i))) mod 3

    This intentionally raises if any key rune has index 0, because phi(0)
    is not defined by the rule as written.
    """
    values = []
    for token in key:
        idx = rune_index(token)
        values.append(mobius_mu(euler_phi(idx)))
    return sum(values) % 3


def rotate_key(key: Sequence[str], phase: int) -> list[str]:
    if len(key) != 3:
        raise ValueError("phase rotation is defined here for a 3-rune key")
    p = phase % 3
    return list(key[p:]) + list(key[:p])


def repeat_key(key: Sequence[str], length: int) -> list[str]:
    if not key:
        raise ValueError("key may not be empty")
    return [key[i % len(key)] for i in range(length)]


def decrypt_mod29(
    ciphertext: Sequence[str],
    key_stream: Sequence[str],
) -> list[str]:
    if len(ciphertext) != len(key_stream):
        raise ValueError("ciphertext and key stream lengths differ")

    result = []
    for c, k in zip(ciphertext, key_stream):
        p = (rune_index(c) - rune_index(k)) % 29
        result.append(rune_for_index(p))
    return result


def gp_sum(tokens: Iterable[str]) -> int:
    return sum(rune_index(token) for token in tokens)


def canonical_english(tokens: Sequence[str]) -> str:
    """
    Render only the ambiguous rune spellings needed by the proposed plaintext.
    The underlying verification remains token-level.
    """
    render = {
        "U/V": "U",
        "S/Z": "S",
        "C/K": "C",
        "IA/O": "IA",
    }
    return "".join(render.get(token, token) for token in tokens)


# ---------------------------------------------------------------------------
# Transparent check runner
# ---------------------------------------------------------------------------

class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.skipped = 0

    def section(self, title: str) -> None:
        print(f"\n=== {title} ===")

    def equal(self, label: str, actual, expected) -> None:
        if actual == expected:
            self.passed += 1
            print(f"[PASS] {label}: {actual!r}")
        else:
            self.failed += 1
            print(
                f"[FAIL] {label}\n"
                f"       expected: {expected!r}\n"
                f"       actual:   {actual!r}"
            )

    def true(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passed += 1
            suffix = f": {detail}" if detail else ""
            print(f"[PASS] {label}{suffix}")
        else:
            self.failed += 1
            suffix = f": {detail}" if detail else ""
            print(f"[FAIL] {label}{suffix}")

    def info(self, label: str, value) -> None:
        print(f"[INFO] {label}: {value}")

    def skip(self, label: str, reason: str) -> None:
        self.skipped += 1
        print(f"[SKIP] {label}: {reason}")


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify(data_path: Path) -> int:
    checks = Checks()

    if not data_path.exists():
        print(f"[FATAL] dataset not found: {data_path}", file=sys.stderr)
        return 2

    matrix = load_matrix(data_path)

    # ---- Dataset -----------------------------------------------------------
    checks.section("1. Dataset integrity")

    checks.equal("row count", len(matrix), 27)

    row_lengths = [len(row) for row in matrix]
    checks.true(
        "every row contains 27 rune tokens",
        len(row_lengths) == 27 and all(n == 27 for n in row_lengths),
        detail=f"row lengths={row_lengths}",
    )

    token_count = sum(row_lengths)
    checks.equal("total rune-token count", token_count, 729)

    unknown = sorted(set(flat_matrix(matrix)) - set(GP_TOKENS))
    checks.equal("unknown GP tokens", unknown, [])

    observed_tokens = set(flat_matrix(matrix))
    missing_from_alphabet = sorted(set(GP_TOKENS) - observed_tokens)
    checks.equal("GP alphabet tokens absent from dataset", missing_from_alphabet, [])

    digest = matrix_sha256(matrix)
    checks.equal("normalized dataset SHA-256", digest, EXPECTED_NORMALIZED_SHA256)

    # ---- Basic geometry ----------------------------------------------------
    checks.section("2. 27×27 geometry and key landmarks")

    center = ((MATRIX_SIZE + 1) // 2, (MATRIX_SIZE + 1) // 2)
    checks.equal("unique geometric center coordinate", center, (14, 14))
    checks.equal("matrix center rune", cell(matrix, center), "NG")

    checks.equal("A crossroads", cell(matrix, (14, 19)), "A")
    checks.equal("right-hand NG", cell(matrix, (14, 23)), "NG")
    checks.equal("H above right-hand NG", cell(matrix, (4, 23)), "H")
    checks.equal("C/K below right-hand NG", cell(matrix, (24, 23)), "C/K")
    checks.equal("G next-stage ciphertext start", cell(matrix, (14, 7)), "G")

    # ---- Initial ROAD / PATH / WAY ----------------------------------------
    checks.section("3. ROAD / PATH / WAY prelude")

    road = ["R", "O", "A", "D"]
    path = ["P", "A", "TH"]
    way = ["W", "A", "Y"]

    checks.equal("ROAD index sum", gp_sum(road), 54)
    checks.equal("ROAD mod 29", gp_sum(road) % 29, GP_INDEX["AE"])
    checks.equal("PATH index sum", gp_sum(path), 39)
    checks.equal("PATH mod 29", gp_sum(path) % 29, GP_INDEX["I"])
    checks.equal("WAY index sum", gp_sum(way), 57)
    checks.equal("WAY mod 29", gp_sum(way) % 29, GP_INDEX["EA"])

    # ---- Stage 1 -----------------------------------------------------------
    checks.section("4. Stage 1 — AS I GO THE")

    node1_start = (13, 11)
    node1 = read_direction(matrix, node1_start, dr=0, dc=1, length=3)
    checks.equal("node AE-J-EA at row 13, cols 11–13", node1, ["AE", "J", "EA"])

    compiled1 = compile_center_with_phi(node1)
    checks.equal("AE-J-EA -> AE-I-EA via phi(J=11)=10", compiled1, ["AE", "I", "EA"])
    checks.equal("phi(J=11)", euler_phi(GP_INDEX["J"]), 10)
    checks.equal("phi(I=10)", euler_phi(GP_INDEX["I"]), 4)

    phase1 = key_phase(compiled1)
    checks.equal("Möbius phase of AE-I-EA", phase1, 0)
    checks.equal("active Stage-1 key", rotate_key(compiled1, phase1), ["AE", "I", "EA"])

    movement1 = GP_INDEX["I"] + euler_phi(GP_INDEX["I"])
    checks.equal("movement value 10 + phi(10)", movement1, 14)

    cipher1_start = move(node1_start, dc=movement1)
    checks.equal("RIGHT 14 from left edge of AE-J-EA", cipher1_start, (13, 25))

    cipher1 = read_row_major(matrix, cipher1_start, 7)
    checks.equal(
        "7-rune Stage-1 ciphertext",
        cipher1,
        ["L", "AE", "N", "TH", "P", "U/V", "X"],
    )

    key1_stream = repeat_key(rotate_key(compiled1, phase1), len(cipher1))
    plain1 = decrypt_mod29(cipher1, key1_stream)
    checks.equal(
        "Stage-1 plaintext rune tokens",
        plain1,
        ["A", "S/Z", "I", "G", "O", "TH", "E"],
    )
    checks.equal("Stage-1 conventional reading", canonical_english(plain1), "ASIGOTHE")

    cipher1_end = row_major_end(cipher1_start, len(cipher1))
    checks.equal("Stage-1 final ciphertext coordinate", cipher1_end, (14, 4))
    checks.equal("Stage-1 final ciphertext rune", cell(matrix, cipher1_end), "X")

    # ---- Stage 2 -----------------------------------------------------------
    checks.section("5. Stage 2 — WEATHER")

    node2_start = cipher1_end
    node2 = read_direction(matrix, node2_start, dr=0, dc=1, length=3)
    checks.equal("adjacent node X-OE-X", node2, ["X", "OE", "X"])

    compiled2 = compile_center_with_phi(node2)
    checks.equal("X-OE-X -> X-I-X via phi(OE)=10", compiled2, ["X", "I", "X"])
    checks.equal("phi(OE=22)", euler_phi(GP_INDEX["OE"]), 10)

    phi10_preimages = [
        GP_TOKENS[i]
        for i in range(1, 29)  # phi(0) intentionally excluded
        if euler_phi(i) == 10
    ]
    checks.equal("GP values 1..28 whose totient equals 10", phi10_preimages, ["J", "OE"])

    phase2 = key_phase(compiled2)
    checks.equal("Möbius phase of X-I-X", phase2, 2)

    active2 = rotate_key(compiled2, phase2)
    checks.equal("active Stage-2 key cycle", active2, ["X", "X", "I"])

    stage2_start = move(node2_start, dc=GP_INDEX["I"])
    checks.equal("RIGHT 10 from left edge/final X", stage2_start, (14, 14))
    checks.equal("RIGHT 10 destination is central NG", cell(matrix, stage2_start), "NG")

    cipher2 = read_direction(matrix, stage2_start, dr=0, dc=1, length=5)
    checks.equal("5-rune WEATHER ciphertext", cipher2, ["NG", "P", "EO", "O", "E"])

    key2_stream = repeat_key(active2, len(cipher2))
    checks.equal("5-rune active key stream", key2_stream, ["X", "X", "I", "X", "X"])

    plain2 = decrypt_mod29(cipher2, key2_stream)
    checks.equal(
        "Stage-2 plaintext rune tokens",
        plain2,
        ["W", "EA", "TH", "E", "R"],
    )
    checks.equal("Stage-2 conventional reading", canonical_english(plain2), "WEATHER")

    stage2_end = move(stage2_start, dc=len(cipher2) - 1)
    checks.equal("WEATHER final ciphertext coordinate", stage2_end, (14, 18))
    checks.equal("cell immediately after WEATHER", move(stage2_end, dc=1), (14, 19))
    checks.equal("cell immediately after WEATHER is A", cell(matrix, (14, 19)), "A")

    # ---- Stage 3 -----------------------------------------------------------
    checks.section("6. Stage 3 — TURNS")

    a_crossroads = (14, 19)

    up10 = move(a_crossroads, dr=-10)
    right4 = move(a_crossroads, dc=4)
    checks.equal("A UP 10 coordinate", up10, (4, 19))
    checks.equal("A UP 10 lands on NG", cell(matrix, up10), "NG")
    checks.equal("A RIGHT 4 coordinate", right4, (14, 23))
    checks.equal("A RIGHT 4 lands on NG", cell(matrix, right4), "NG")

    left_a = move(right4, dc=-4)
    right_a = move(right4, dc=4)
    checks.equal("A exactly 4 left of NG(14,23)", cell(matrix, left_a), "A")
    checks.equal("A exactly 4 right of NG(14,23)", cell(matrix, right_a), "A")

    # Exhaustive check of the exact, well-defined uniqueness claim.
    symmetric_ng_matches = []
    for r in range(1, 28):
        for c in range(5, 24):
            if (
                cell(matrix, (r, c)) == "NG"
                and cell(matrix, (r, c - 4)) == "A"
                and cell(matrix, (r, c + 4)) == "A"
            ):
                symmetric_ng_matches.append((r, c))
    checks.equal(
        "NG cells with A exactly 4 left AND 4 right",
        symmetric_ng_matches,
        [(14, 23)],
    )

    h_coord = move(right4, dr=-10)
    c_coord = move(right4, dr=10)
    checks.equal("NG(14,23) UP 10", h_coord, (4, 23))
    checks.equal("NG(14,23) DOWN 10", c_coord, (24, 23))

    node3 = [cell(matrix, h_coord), cell(matrix, right4), cell(matrix, c_coord)]
    checks.equal("vertical node H-NG-C/K", node3, ["H", "NG", "C/K"])

    node3_signature = [euler_phi(rune_index(x)) for x in node3]
    checks.equal("totient signature of H-NG-C/K", node3_signature, [4, 12, 4])

    ini = read_direction(matrix, (4, 18), dr=0, dc=1, length=3)
    checks.equal("I-NG-I structure", ini, ["I", "NG", "I"])
    ini_signature = [euler_phi(rune_index(x)) for x in ini]
    checks.equal("totient signature of I-NG-I", ini_signature, [4, 12, 4])
    checks.equal("H-NG-C/K and I-NG-I signatures match", node3_signature, ini_signature)

    # Volume 1 uses H-NG-C directly for TURNS.
    phase3 = key_phase(node3)
    checks.equal("derived Möbius phase of H-NG-C/K", phase3, 0)

    cipher3 = read_direction(matrix, a_crossroads, dr=-1, dc=0, length=5)
    checks.equal("ciphertext read upward from A", cipher3, ["A", "OE", "N", "B", "W"])

    key3_stream = repeat_key(rotate_key(node3, phase3), len(cipher3))
    checks.equal(
        "Stage-3 key stream",
        key3_stream,
        ["H", "NG", "C/K", "H", "NG"],
    )

    plain3 = decrypt_mod29(cipher3, key3_stream)
    checks.equal(
        "Stage-3 plaintext rune tokens",
        plain3,
        ["T", "U/V", "R", "N", "S/Z"],
    )
    checks.equal("Stage-3 conventional reading", canonical_english(plain3), "TURNS")

    turns_end = move(a_crossroads, dr=-(len(cipher3) - 1))
    checks.equal("TURNS final ciphertext coordinate", turns_end, (10, 19))
    checks.equal("TURNS final ciphertext rune", cell(matrix, turns_end), "W")

    # ---- Stage 4 -----------------------------------------------------------
    checks.section("7. Stage 4 — COLD")

    phi_ng = euler_phi(GP_INDEX["NG"])
    checks.equal("phi(NG=21)", phi_ng, 12)

    down12 = move(a_crossroads, dr=phi_ng)
    left12 = move(a_crossroads, dc=-phi_ng)
    checks.equal("A DOWN 12", down12, (26, 19))
    checks.equal("A LEFT 12", left12, (14, 7))
    checks.equal("A LEFT 12 lands on G", cell(matrix, left12), "G")

    node4 = read_direction(matrix, (25, 19), dr=1, dc=0, length=3)
    checks.equal("vertical H-TH-H around DOWN-12 center", node4, ["H", "TH", "H"])
    checks.equal("DOWN 12 lands on H-TH-H center", cell(matrix, down12), "TH")

    compiled4 = compile_center_with_phi(node4)
    checks.equal("H-TH-H -> H-U/V-H", compiled4, ["H", "U/V", "H"])
    checks.equal("phi(TH=2)", euler_phi(GP_INDEX["TH"]), 1)

    phase4 = key_phase(compiled4)
    checks.equal("Möbius phase of H-U/V-H", phase4, 1)

    active4 = rotate_key(compiled4, phase4)
    checks.equal("active Stage-4 key cycle", active4, ["U/V", "H", "H"])

    cipher4 = read_direction(matrix, left12, dr=-1, dc=0, length=4)
    checks.equal("ciphertext read upward from G(14,7)", cipher4, ["G", "J", "EA", "A"])

    key4_stream = repeat_key(active4, len(cipher4))
    checks.equal("Stage-4 key stream", key4_stream, ["U/V", "H", "H", "U/V"])

    plain4 = decrypt_mod29(cipher4, key4_stream)
    checks.equal(
        "Stage-4 plaintext rune tokens",
        plain4,
        ["C/K", "O", "L", "D"],
    )
    checks.equal("Stage-4 conventional reading", canonical_english(plain4), "COLD")

    cold_end = move(left12, dr=-(len(cipher4) - 1))
    checks.equal("COLD final ciphertext coordinate", cold_end, (11, 7))
    checks.equal("COLD final ciphertext rune", cell(matrix, cold_end), "A")
    checks.equal("phi(A=24)", euler_phi(GP_INDEX["A"]), 8)
    checks.equal("GP rune at index 8", rune_for_index(8), "H")

    # ---- Full plaintext and numerical checks -------------------------------
    checks.section("8. Full proposed plaintext and numerical checks")

    # Explicit word boundaries from the Volume-1 reading.
    words = [
        ["A", "S/Z"],
        ["I"],
        ["G", "O"],
        ["TH", "E"],
        plain2,
        plain3,
        plain4,
    ]

    rendered_words = [canonical_english(word) for word in words]
    checks.equal(
        "seven-word proposed plaintext",
        rendered_words,
        ["AS", "I", "GO", "THE", "WEATHER", "TURNS", "COLD"],
    )

    checks.equal("word count", len(words), 7)

    full_plain_tokens = [token for word in words for token in word]
    checks.equal("plaintext rune count", len(full_plain_tokens), 21)
    checks.equal("21 = 3 × 7", len(full_plain_tokens), 3 * len(words))

    checks.equal("0-based GP sum of full plaintext", gp_sum(full_plain_tokens), 233)
    checks.equal("0-based GP sum of COLD", gp_sum(plain4), 51)
    checks.equal("51st prime", nth_prime(51), 233)
    checks.equal("F_7", fibonacci(7), 13)
    checks.equal("F_13", fibonacci(13), 233)

    checks.equal("NG zero-based GP index", GP_INDEX["NG"], 21)
    checks.equal("COLD ciphertext start column", left12[1], 7)
    checks.equal("TURNS ciphertext end column", turns_end[1], 19)
    checks.equal("19 - 7", turns_end[1] - left12[1], 12)
    checks.equal("19 - 7 equals phi(NG)", turns_end[1] - left12[1], phi_ng)

    # Prime-value observation: GP index i maps to the (i+1)-th prime.
    prime_values = [nth_prime(i + 1) for i in range(29)]
    checks.equal("W zero-based GP index", GP_INDEX["W"], 7)
    checks.equal("W prime value", prime_values[GP_INDEX["W"]], 19)

    diff12 = [
        GP_TOKENS[i]
        for i, p in enumerate(prime_values)
        if p - i == 12
    ]
    checks.equal(
        "runes whose prime value minus GP index equals 12",
        diff12,
        ["W"],
    )

    # ---- Explicit non-claims -----------------------------------------------
    checks.section("9. Deliberately NOT verified by this script")

    checks.skip(
        "0.0041% / ~1 in 24,000 random-window estimate",
        "the exact shuffle procedure, selection rule and search space are not encoded in Volume 1 strongly enough for an independent statistical reproduction here",
    )
    checks.skip(
        "J -> OE evidential probability",
        "1/29^2 is trivial arithmetic, but it is not a complete post-selection / multiple-comparisons probability model",
    )
    checks.skip(
        "H-TH-H 'only mirrored structure in the lower area'",
        "'lower area' is not defined as a formal exhaustive search region in the source",
    )
    checks.skip(
        "separator / dot interpretations",
        "the 729-rune TXT intentionally contains rune tokens only and does not encode the page separators/dot geometry needed for those claims",
    )
    checks.skip(
        "RTN / GEB interpretation",
        "conceptual analogy, not a deterministic cryptographic check",
    )
    checks.skip(
        "DIVINITY WITHIN = 491 / 'A' CROSSROADS = 491",
        "secondary thematic gematria claim; omitted from the core verifier to avoid mixing it with the deterministic route",
    )
    checks.skip(
        "2014 hidden-prime-space / missing-19 claim",
        "requires a separate external source file and is not derivable from the 729-rune dataset",
    )

    # ---- Final --------------------------------------------------------------
    checks.section("10. Summary")

    current_plaintext = " ".join(rendered_words)
    checks.info("current proposed plaintext", current_plaintext)
    checks.info("passes", checks.passed)
    checks.info("failures", checks.failed)
    checks.info("skipped/non-core claims", checks.skipped)

    if checks.failed:
        print("\nVERIFICATION FAILED")
        return 1

    print(
        "\nALL CORE VOLUME 1 CHECKS PASSED\n"
        "Current proposed plaintext:\n"
        f"{current_plaintext}\n\n"
        "Interpretation note: passing these checks establishes internal\n"
        "reproducibility of the encoded Volume-1 route; it does not constitute\n"
        "official authentication of the proposed Liber Primus plaintext."
    )
    return 0


def parse_args() -> argparse.Namespace:
    default_data = Path(__file__).resolve().with_name(
        "liber-primus-0-2-729-runes.txt"
    )

    parser = argparse.ArgumentParser(
        description="Verify reproducible core claims in SOLUTION 0-2 — Volume 1."
    )
    parser.add_argument(
        "data",
        nargs="?",
        type=Path,
        default=default_data,
        help=(
            "Path to the 729-rune TXT dataset "
            "(default: liber-primus-0-2-729-runes.txt next to this script)"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("SOLUTION 0-2 — Volume 1 reproducibility verifier")
    print(f"Dataset: {args.data}")
    return verify(args.data)


if __name__ == "__main__":
    raise SystemExit(main())
