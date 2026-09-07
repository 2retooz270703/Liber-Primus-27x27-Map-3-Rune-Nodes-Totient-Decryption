#!/usr/bin/env python3
"""
Full verifier for SOLUTION 0-2 — Volume 1.

This script checks the reproducible claims in:
    other-stuff/md/0-2-volume-1.md
against:
    other-stuff/0-2-runes.txt

It deliberately separates four kinds of output:
    PASS  - mechanically reproduced from the rune grid / stated formulas
    FAIL  - a reproducible claim did not match
    INFO  - useful computed context or an interpretive claim with a hard core
    N/A   - cannot be independently reproduced because the MD does not provide
            the required source data, exact search space, or selection rule

No third-party Python packages are required.

Typical use from the repository root:
    python3 verify_volume_1.py

Or with an explicit rune file:
    python3 verify_volume_1.py --runes other-stuff/0-2-runes.txt
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


# -----------------------------------------------------------------------------
# Gematria Primus: 0-based rune order used by Volume 1
# -----------------------------------------------------------------------------

RUNES = [
    "F", "U/V", "TH", "O", "R", "C/K", "G", "W", "H", "N",
    "I", "J", "EO", "P", "X", "S/Z", "T", "B", "E", "M",
    "L", "NG", "OE", "D", "A", "AE", "Y", "IA/O", "EA",
]

INDEX = {rune: i for i, rune in enumerate(RUNES)}
MODULUS = 29


# -----------------------------------------------------------------------------
# Small math helpers
# -----------------------------------------------------------------------------

def phi(n: int) -> int:
    """Euler's totient function for n >= 1."""
    if n < 1:
        raise ValueError("phi() is defined here only for positive integers")
    result = n
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result


def mobius(n: int) -> int:
    """Möbius function μ(n) for n >= 1."""
    if n < 1:
        raise ValueError("mobius() is defined here only for positive integers")
    if n == 1:
        return 1

    x = n
    prime_factors = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            prime_factors += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def first_primes(count: int) -> list[int]:
    out: list[int] = []
    n = 2
    while len(out) < count:
        if all(n % p for p in range(2, math.isqrt(n) + 1)):
            out.append(n)
        n += 1
    return out


def fibonacci(n: int) -> int:
    """F1=1, F2=1 convention used by the Volume 1 observation."""
    if n < 1:
        raise ValueError("fibonacci() expects n >= 1")
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a + b
    return a


PRIMES = first_primes(29)
PRIME_VALUE = {rune: PRIMES[i] for i, rune in enumerate(RUNES)}


# -----------------------------------------------------------------------------
# Rune/key operations
# -----------------------------------------------------------------------------

def rune_for_index(value: int) -> str:
    return RUNES[value % MODULUS]


def compile_node(node: Sequence[str]) -> tuple[str, str, str]:
    """Volume 1 rule: (a, b, c) -> (a, rune(phi(index(b))), c)."""
    if len(node) != 3:
        raise ValueError("A node must contain exactly 3 runes")
    a, b, c = node
    return a, rune_for_index(phi(INDEX[b])), c


def key_phase(key: Sequence[str]) -> int:
    """p = sum(mu(phi(index(K_i)))) mod 3."""
    terms = [mobius(phi(INDEX[rune])) for rune in key]
    return sum(terms) % 3


def rotate_left(items: Sequence[str], amount: int) -> tuple[str, ...]:
    amount %= len(items)
    return tuple(items[amount:]) + tuple(items[:amount])


def repeat_key(key: Sequence[str], length: int) -> list[str]:
    return [key[i % len(key)] for i in range(length)]


def decrypt_mod29(ciphertext: Sequence[str], key: Sequence[str]) -> list[str]:
    if len(ciphertext) != len(key):
        raise ValueError("ciphertext and key must have the same length")
    return [
        rune_for_index(INDEX[c] - INDEX[k])
        for c, k in zip(ciphertext, key)
    ]


def gp_sum(tokens: Sequence[str]) -> int:
    return sum(INDEX[token] for token in tokens)


def prime_sum(tokens: Sequence[str]) -> int:
    return sum(PRIME_VALUE[token] for token in tokens)


# -----------------------------------------------------------------------------
# 27x27 grid helpers (coordinates are 1-based, as in Volume 1)
# -----------------------------------------------------------------------------

Coord = tuple[int, int]

DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
    "UP_LEFT": (-1, -1),
    "UP_RIGHT": (-1, 1),
    "DOWN_LEFT": (1, -1),
    "DOWN_RIGHT": (1, 1),
}


class Grid:
    def __init__(self, rows: list[list[str]]):
        self.rows = rows

    @classmethod
    def from_file(cls, path: Path) -> "Grid":
        text = path.read_text(encoding="utf-8")
        tokens = text.split()
        if len(tokens) != 729:
            raise ValueError(f"Expected 729 rune tokens, found {len(tokens)}")
        unknown = sorted(set(tokens) - set(RUNES))
        if unknown:
            raise ValueError(f"Unknown rune tokens: {unknown}")
        rows = [tokens[i:i + 27] for i in range(0, 729, 27)]
        return cls(rows)

    def at(self, coord: Coord) -> str:
        row, col = coord
        if not (1 <= row <= 27 and 1 <= col <= 27):
            raise IndexError(f"Coordinate outside 27x27 grid: {coord}")
        return self.rows[row - 1][col - 1]

    def move(self, start: Coord, direction: str, distance: int) -> Coord:
        dr, dc = DIRECTIONS[direction]
        row, col = start
        dest = row + dr * distance, col + dc * distance
        # Validate destination.
        self.at(dest)
        return dest

    def read(self, start: Coord, direction: str, length: int) -> list[str]:
        dr, dc = DIRECTIONS[direction]
        row, col = start
        out = []
        for i in range(length):
            out.append(self.at((row + dr * i, col + dc * i)))
        return out

    def read_row_major(self, start: Coord, length: int) -> list[str]:
        """Read in the original row-wise 729-rune order, allowing row wrap."""
        row, col = start
        start_index = (row - 1) * 27 + (col - 1)
        flat = [token for grid_row in self.rows for token in grid_row]
        end = start_index + length
        if end > len(flat):
            raise IndexError("row-major read leaves the grid")
        return flat[start_index:end]

    def find_sequence(self, sequence: Sequence[str]) -> list[tuple[Coord, str]]:
        """Find a contiguous sequence in all 8 straight directions."""
        found: list[tuple[Coord, str]] = []
        for row in range(1, 28):
            for col in range(1, 28):
                for direction, (dr, dc) in DIRECTIONS.items():
                    ok = True
                    for i, expected in enumerate(sequence):
                        r, c = row + dr * i, col + dc * i
                        if not (1 <= r <= 27 and 1 <= c <= 27):
                            ok = False
                            break
                        if self.at((r, c)) != expected:
                            ok = False
                            break
                    if ok:
                        found.append(((row, col), direction))
        return found

    def count_undirected_palindrome(self, sequence: Sequence[str]) -> int:
        """Count straight occurrences once, ignoring reverse-direction duplicates."""
        unique: set[tuple[Coord, ...]] = set()
        for start, direction in self.find_sequence(sequence):
            dr, dc = DIRECTIONS[direction]
            coords = tuple(
                (start[0] + dr * i, start[1] + dc * i)
                for i in range(len(sequence))
            )
            unique.add(tuple(sorted(coords)))
        return len(unique)


# -----------------------------------------------------------------------------
# Structured report
# -----------------------------------------------------------------------------

@dataclass
class Result:
    status: str
    section: str
    claim: str
    detail: str = ""


class Report:
    def __init__(self) -> None:
        self.results: list[Result] = []

    def check(self, section: str, claim: str, condition: bool, detail: str = "") -> None:
        self.results.append(Result("PASS" if condition else "FAIL", section, claim, detail))

    def info(self, section: str, claim: str, detail: str = "") -> None:
        self.results.append(Result("INFO", section, claim, detail))

    def na(self, section: str, claim: str, detail: str = "") -> None:
        self.results.append(Result("N/A", section, claim, detail))

    def print(self) -> None:
        current = None
        for result in self.results:
            if result.section != current:
                current = result.section
                print(f"\n=== {current} ===")
            line = f"[{result.status:4}] {result.claim}"
            print(line)
            if result.detail:
                print(f"       {result.detail}")

        counts = {status: 0 for status in ("PASS", "FAIL", "INFO", "N/A")}
        for result in self.results:
            counts[result.status] += 1

        print("\n=== SUMMARY ===")
        print(
            f"PASS={counts['PASS']}  FAIL={counts['FAIL']}  "
            f"INFO={counts['INFO']}  N/A={counts['N/A']}"
        )
        if counts["FAIL"] == 0:
            print("Core reproducible checks completed without a mismatch.")
        else:
            print("One or more reproducible claims did not match; inspect FAIL lines above.")

    @property
    def failed(self) -> bool:
        return any(result.status == "FAIL" for result in self.results)


# -----------------------------------------------------------------------------
# Volume 1 verification
# -----------------------------------------------------------------------------

def verify(grid: Grid) -> Report:
    r = Report()

    # ------------------------------------------------------------------
    # Source data / global facts
    # ------------------------------------------------------------------
    flat = [token for row in grid.rows for token in row]
    r.check("1. Source data and global structure", "729 rune tokens are present", len(flat) == 729)
    r.check(
        "1. Source data and global structure",
        "Row-wise placement forms exactly 27 rows x 27 columns",
        len(grid.rows) == 27 and all(len(row) == 27 for row in grid.rows),
    )
    r.check(
        "1. Source data and global structure",
        "The exact matrix center (14,14) is NG",
        grid.at((14, 14)) == "NG",
        f"(14,14)={grid.at((14,14))}",
    )
    phi10 = [n for n in range(1, 29) if phi(n) == 10]
    r.check(
        "1. Source data and global structure",
        "J=11 and OE=22 are the only GP values 1..28 with phi(n)=10",
        phi10 == [11, 22],
        f"solutions={phi10} -> {[rune_for_index(n) for n in phi10]}",
    )

    # Exact nodes used later.
    r.check(
        "1. Source data and global structure",
        "AE-J-EA exists at row 13, columns 11..13",
        grid.read((13, 11), "RIGHT", 3) == ["AE", "J", "EA"],
    )
    r.check(
        "1. Source data and global structure",
        "X-OE-X exists at row 14, columns 4..6",
        grid.read((14, 4), "RIGHT", 3) == ["X", "OE", "X"],
    )
    r.check(
        "1. Source data and global structure",
        "I-NG-I exists at row 4, columns 18..20",
        grid.read((4, 18), "RIGHT", 3) == ["I", "NG", "I"],
    )
    r.check(
        "1. Source data and global structure",
        "H-TH-H exists vertically at column 19, rows 25..27",
        grid.read((25, 19), "DOWN", 3) == ["H", "TH", "H"],
    )
    hthh_count = grid.count_undirected_palindrome(["H", "TH", "H"])
    r.check(
        "1. Source data and global structure",
        "The exact contiguous H-TH-H pattern occurs once globally (undirected)",
        hthh_count == 1,
        f"global exact-pattern count={hthh_count}",
    )

    # ------------------------------------------------------------------
    # Stage 1: AS I GO THE
    # ------------------------------------------------------------------
    node1 = ("AE", "J", "EA")
    key1 = compile_node(node1)
    r.check(
        "2. Stage 1 — AS I GO THE",
        "phi(J=11)=10=I and AE-J-EA compiles to AE-I-EA",
        phi(INDEX["J"]) == 10 and key1 == ("AE", "I", "EA"),
        f"compiled_key={'-'.join(key1)}",
    )
    movement1 = phi(INDEX["J"]) + phi(phi(INDEX["J"]))
    r.check(
        "2. Stage 1 — AS I GO THE",
        "10 + phi(10)=14",
        movement1 == 14,
        f"movement_value={movement1}",
    )

    # The MD says RIGHT 14 from the first node. In the actual grid this is
    # reproduced from the left outer AE, not from the center J.
    stage1_start = grid.move((13, 11), "RIGHT", movement1)
    r.check(
        "2. Stage 1 — AS I GO THE",
        "RIGHT 14 from the left outer AE(13,11) reaches L(13,25)",
        stage1_start == (13, 25) and grid.at(stage1_start) == "L",
        "Important origin convention: using the center J(13,12) would land on AE(13,26), not L.",
    )
    ct1 = grid.read_row_major(stage1_start, 7)
    expected_ct1 = ["L", "AE", "N", "TH", "P", "U/V", "X"]
    r.check(
        "2. Stage 1 — AS I GO THE",
        "Seven row-major ciphertext runes are L-AE-N-TH-P-U/V-X",
        ct1 == expected_ct1,
        f"read={'-'.join(ct1)} (crosses row 13 -> row 14)",
    )
    phase1 = key_phase(key1)
    r.check(
        "2. Stage 1 — AS I GO THE",
        "Möbius phase of AE-I-EA is 0",
        phase1 == 0,
        f"phi(K)={[phi(INDEX[x]) for x in key1]}, mu={[mobius(phi(INDEX[x])) for x in key1]}, phase={phase1}",
    )
    active1 = repeat_key(rotate_left(key1, phase1), len(ct1))
    pt1 = decrypt_mod29(ct1, active1)
    expected_pt1 = ["A", "S/Z", "I", "G", "O", "TH", "E"]
    r.check(
        "2. Stage 1 — AS I GO THE",
        "Mod-29 subtraction decrypts Stage 1 to A-S-I-G-O-TH-E",
        pt1 == expected_pt1,
        f"plaintext={'-'.join(pt1)}",
    )
    final_x = (14, 4)
    r.check(
        "2. Stage 1 — AS I GO THE",
        "The final Stage-1 ciphertext rune is X at (14,4)",
        grid.at(final_x) == "X" and ct1[-1] == "X",
    )

    # ------------------------------------------------------------------
    # Stage 2: WEATHER
    # ------------------------------------------------------------------
    r.check(
        "3. Stage 2 — WEATHER",
        "The final X at (14,4) is the left edge of adjacent X-OE-X",
        grid.read(final_x, "RIGHT", 3) == ["X", "OE", "X"],
    )
    node2 = ("X", "OE", "X")
    key2 = compile_node(node2)
    r.check(
        "3. Stage 2 — WEATHER",
        "phi(OE=22)=10=I and X-OE-X compiles to X-I-X",
        phi(INDEX["OE"]) == 10 and key2 == ("X", "I", "X"),
        f"compiled_key={'-'.join(key2)}",
    )
    phase2 = key_phase(key2)
    active2_cycle = rotate_left(key2, phase2)
    r.check(
        "3. Stage 2 — WEATHER",
        "Möbius phase of X-I-X is 2, giving active cycle X-X-I",
        phase2 == 2 and active2_cycle == ("X", "X", "I"),
        f"phi(K)={[phi(INDEX[x]) for x in key2]}, mu={[mobius(phi(INDEX[x])) for x in key2]}, phase={phase2}",
    )
    center = grid.move(final_x, "RIGHT", 10)
    r.check(
        "3. Stage 2 — WEATHER",
        "RIGHT 10 from final X(14,4) reaches the exact center NG(14,14)",
        center == (14, 14) and grid.at(center) == "NG",
        "Origin is the final ciphertext X; RIGHT 10 from the node center OE would not reach (14,14).",
    )
    ct2 = grid.read(center, "RIGHT", 5)
    expected_ct2 = ["NG", "P", "EO", "O", "E"]
    r.check(
        "3. Stage 2 — WEATHER",
        "The five matrix runes from central NG are NG-P-EO-O-E",
        ct2 == expected_ct2,
        f"ciphertext={'-'.join(ct2)}",
    )
    active2 = repeat_key(active2_cycle, 5)
    pt2 = decrypt_mod29(ct2, active2)
    expected_pt2 = ["W", "EA", "TH", "E", "R"]
    r.check(
        "3. Stage 2 — WEATHER",
        "X-X-I-X-X decrypts NG-P-EO-O-E to W-EA-TH-E-R",
        pt2 == expected_pt2,
        f"plaintext={'-'.join(pt2)}",
    )
    r.check(
        "3. Stage 2 — WEATHER",
        "W-EA-TH appears directly above the first three WEATHER ciphertext cells",
        grid.read((13, 14), "RIGHT", 3) == ["W", "EA", "TH"],
        "W-EA-TH is at row 13, cols 14..16; ciphertext starts below at row 14, col 14.",
    )
    r.check(
        "3. Stage 2 — WEATHER",
        "WEATHER ciphertext ends at E(14,18) and is followed by A(14,19)",
        grid.at((14, 18)) == "E" and grid.at((14, 19)) == "A",
    )

    # ------------------------------------------------------------------
    # Stage 3: TURNS
    # ------------------------------------------------------------------
    a_cross = (14, 19)
    up10 = grid.move(a_cross, "UP", 10)
    right4 = grid.move(a_cross, "RIGHT", 4)
    r.check(
        "4. Stage 3 — TURNS",
        "A(14,19) is the stated crossroads",
        grid.at(a_cross) == "A",
    )
    r.check(
        "4. Stage 3 — TURNS",
        "UP 10 from A(14,19) reaches NG(4,19)",
        up10 == (4, 19) and grid.at(up10) == "NG",
    )
    r.check(
        "4. Stage 3 — TURNS",
        "RIGHT 4 from A(14,19) reaches NG(14,23)",
        right4 == (14, 23) and grid.at(right4) == "NG",
    )
    r.check(
        "4. Stage 3 — TURNS",
        "NG(14,23) has A exactly 4 cells left and right",
        grid.at((14, 19)) == "A" and grid.at((14, 27)) == "A",
        "A(14,19) --4-- NG(14,23) --4-- A(14,27)",
    )
    vertical_node = [grid.at((4, 23)), grid.at((14, 23)), grid.at((24, 23))]
    r.check(
        "4. Stage 3 — TURNS",
        "The vertical 10-step axis is H(4,23)-NG(14,23)-C/K(24,23)",
        vertical_node == ["H", "NG", "C/K"],
        f"node={'-'.join(vertical_node)}",
    )
    sig_hngc = [phi(INDEX[x]) for x in vertical_node]
    sig_ingi = [phi(INDEX[x]) for x in ["I", "NG", "I"]]
    r.check(
        "4. Stage 3 — TURNS",
        "H-NG-C/K has totient signature 4-12-4",
        sig_hngc == [4, 12, 4],
        f"signature={sig_hngc}",
    )
    r.check(
        "4. Stage 3 — TURNS",
        "I-NG-I has the same totient signature 4-12-4",
        sig_ingi == [4, 12, 4],
        f"signature={sig_ingi}",
    )
    phase3 = key_phase(vertical_node)
    r.check(
        "4. Stage 3 — TURNS",
        "The stated Möbius rule gives phase 0 for H-NG-C/K",
        phase3 == 0,
        f"mu={[mobius(phi(INDEX[x])) for x in vertical_node]}, phase={phase3}",
    )
    ct3 = grid.read(a_cross, "UP", 5)
    expected_ct3 = ["A", "OE", "N", "B", "W"]
    r.check(
        "4. Stage 3 — TURNS",
        "Reading upward from A(14,19) gives A-OE-N-B-W",
        ct3 == expected_ct3,
        f"ciphertext={'-'.join(ct3)}",
    )
    active3 = repeat_key(vertical_node, 5)
    pt3 = decrypt_mod29(ct3, active3)
    expected_pt3 = ["T", "U/V", "R", "N", "S/Z"]
    r.check(
        "4. Stage 3 — TURNS",
        "H-NG-C/K-H-NG decrypts A-OE-N-B-W to T-U-R-N-S",
        pt3 == expected_pt3,
        f"plaintext={'-'.join(pt3)}",
    )
    r.check(
        "4. Stage 3 — TURNS",
        "The final TURNS ciphertext rune W lies in column 19",
        grid.at((10, 19)) == "W" and ct3[-1] == "W",
        "W is at (10,19).",
    )

    # ------------------------------------------------------------------
    # Stage 4: COLD
    # ------------------------------------------------------------------
    control12 = phi(INDEX["NG"])
    r.check(
        "5. Stage 4 — COLD",
        "phi(NG=21)=12",
        control12 == 12,
    )
    down12 = grid.move(a_cross, "DOWN", control12)
    left12 = grid.move(a_cross, "LEFT", control12)
    r.check(
        "5. Stage 4 — COLD",
        "DOWN 12 from A(14,19) reaches TH(26,19), the center of H-TH-H",
        down12 == (26, 19)
        and grid.at(down12) == "TH"
        and grid.read((25, 19), "DOWN", 3) == ["H", "TH", "H"],
    )
    r.check(
        "5. Stage 4 — COLD",
        "LEFT 12 from A(14,19) reaches G(14,7), the COLD ciphertext start",
        left12 == (14, 7) and grid.at(left12) == "G",
    )
    key4 = compile_node(("H", "TH", "H"))
    r.check(
        "5. Stage 4 — COLD",
        "phi(TH=2)=1=U/V and H-TH-H compiles to H-U/V-H",
        phi(INDEX["TH"]) == 1 and key4 == ("H", "U/V", "H"),
        f"compiled_key={'-'.join(key4)}",
    )
    phase4 = key_phase(key4)
    active4_cycle = rotate_left(key4, phase4)
    r.check(
        "5. Stage 4 — COLD",
        "Möbius phase of H-U/V-H is 1, giving U/V-H-H",
        phase4 == 1 and active4_cycle == ("U/V", "H", "H"),
        f"phi(K)={[phi(INDEX[x]) for x in key4]}, mu={[mobius(phi(INDEX[x])) for x in key4]}, phase={phase4}",
    )
    ct4 = grid.read(left12, "UP", 4)
    expected_ct4 = ["G", "J", "EA", "A"]
    r.check(
        "5. Stage 4 — COLD",
        "Reading upward from G(14,7) gives G-J-EA-A",
        ct4 == expected_ct4,
        f"ciphertext={'-'.join(ct4)}",
    )
    active4 = repeat_key(active4_cycle, 4)
    pt4 = decrypt_mod29(ct4, active4)
    expected_pt4 = ["C/K", "O", "L", "D"]
    r.check(
        "5. Stage 4 — COLD",
        "U/V-H-H-U/V decrypts G-J-EA-A to C-O-L-D",
        pt4 == expected_pt4,
        f"plaintext={'-'.join(pt4)}",
    )
    r.check(
        "5. Stage 4 — COLD",
        "The final COLD ciphertext cell is A(11,7), and phi(A=24)=8=H",
        grid.at((11, 7)) == "A" and phi(INDEX["A"]) == 8 and rune_for_index(8) == "H",
    )
    r.check(
        "5. Stage 4 — COLD",
        "The H-TH-H vertical node lies entirely in the A-crossroads column 19",
        a_cross[1] == 19 and all(grid.at((row, 19)) == expected for row, expected in [(25, "H"), (26, "TH"), (27, "H")]),
    )

    # ------------------------------------------------------------------
    # Full plaintext and numerical observations
    # ------------------------------------------------------------------
    full_plaintext = pt1 + pt2 + pt3 + pt4
    expected_full = expected_pt1 + expected_pt2 + expected_pt3 + expected_pt4
    r.check(
        "6. Full plaintext and numerical checks",
        "The four stages contain 21 plaintext rune tokens",
        len(full_plaintext) == 21 and full_plaintext == expected_full,
        f"rune_count={len(full_plaintext)}",
    )
    r.check(
        "6. Full plaintext and numerical checks",
        "The human-readable phrase has 7 words",
        len("AS I GO THE WEATHER TURNS COLD".split()) == 7,
    )
    full_sum = gp_sum(full_plaintext)
    cold_sum = gp_sum(pt4)
    r.check(
        "6. Full plaintext and numerical checks",
        "The 21 zero-based GP indices sum to 233",
        full_sum == 233,
        f"sum={full_sum}",
    )
    r.check(
        "6. Full plaintext and numerical checks",
        "COLD has zero-based GP index sum 51",
        cold_sum == 51,
        f"sum={cold_sum}",
    )
    primes_51 = first_primes(51)
    r.check(
        "6. Full plaintext and numerical checks",
        "233 is the 51st prime number",
        primes_51[-1] == 233,
        f"51st_prime={primes_51[-1]}",
    )
    r.check(
        "6. Full plaintext and numerical checks",
        "F7=13 and F13=233",
        fibonacci(7) == 13 and fibonacci(13) == 233,
        f"F7={fibonacci(7)}, F13={fibonacci(13)}",
    )
    r.check(
        "6. Full plaintext and numerical checks",
        "21 = 3 x 7 and NG has GP value 21",
        21 == 3 * 7 and INDEX["NG"] == 21,
    )

    # ------------------------------------------------------------------
    # Column 19 / column 7 observations
    # ------------------------------------------------------------------
    r.check(
        "7. Column 19 / column 7 observations",
        "A crossroads, I-NG-I center, and H-TH-H center are all in column 19",
        a_cross[1] == 19 and (4, 19)[1] == 19 and (26, 19)[1] == 19,
        "A=(14,19), I-NG-I center NG=(4,19), H-TH-H center TH=(26,19)",
    )
    r.check(
        "7. Column 19 / column 7 observations",
        "W has zero-based GP index 7 and prime value 19",
        INDEX["W"] == 7 and PRIME_VALUE["W"] == 19,
        f"index(W)={INDEX['W']}, prime_value(W)={PRIME_VALUE['W']}",
    )
    r.check(
        "7. Column 19 / column 7 observations",
        "19 - 7 = 12 = phi(NG)",
        19 - 7 == control12 == 12,
    )
    r.check(
        "7. Column 19 / column 7 observations",
        "TURNS ends in column 19 and COLD begins in column 7",
        (10, 19)[1] == 19 and left12[1] == 7,
        "TURNS final ciphertext W=(10,19); COLD start G=(14,7)",
    )

    # ------------------------------------------------------------------
    # Additional arithmetic observations
    # ------------------------------------------------------------------
    road = ["R", "O", "A", "D"]
    path = ["P", "A", "TH"]
    way = ["W", "A", "Y"]
    r.check(
        "8. Additional reproducible observations",
        "ROAD: 4+3+24+23=54 -> 54 mod 29 = 25 = AE",
        gp_sum(road) == 54 and gp_sum(road) % 29 == INDEX["AE"] == 25,
    )
    r.check(
        "8. Additional reproducible observations",
        "PATH: 13+24+2=39 -> 39 mod 29 = 10 = I",
        gp_sum(path) == 39 and gp_sum(path) % 29 == INDEX["I"] == 10,
    )
    r.check(
        "8. Additional reproducible observations",
        "WAY: 7+24+26=57 -> 57 mod 29 = 28 = EA",
        gp_sum(way) == 57 and gp_sum(way) % 29 == INDEX["EA"] == 28,
    )
    r.check(
        "8. Additional reproducible observations",
        "ROAD / PATH / WAY therefore reduce to AE-I-EA",
        [rune_for_index(gp_sum(x) % 29) for x in (road, path, way)] == ["AE", "I", "EA"],
    )

    way_occurrences = grid.find_sequence(["W", "A", "Y"])
    way_through_a = any(
        start == (15, 18) and direction == "UP_RIGHT"
        for start, direction in way_occurrences
    )
    r.check(
        "8. Additional reproducible observations",
        "WAY passes diagonally through A(14,19) with A at its center",
        way_through_a
        and grid.read((15, 18), "UP_RIGHT", 3) == ["W", "A", "Y"],
        "W(15,18) -> A(14,19) -> Y(13,20)",
    )

    divinity_within = ["D", "I", "U/V", "I", "N", "I", "T", "Y", "W", "I", "TH", "I", "N"]
    a_crossroads = ["A", "C/K", "R", "O", "S/Z", "S/Z", "R", "O", "A", "D", "S/Z"]
    div_sum = prime_sum(divinity_within)
    cross_sum = prime_sum(a_crossroads)
    r.check(
        "8. Additional reproducible observations",
        "DIVINITY WITHIN and A CROSSROADS both have GP prime-value sum 491",
        div_sum == 491 and cross_sum == 491,
        f"DIVINITY WITHIN={div_sum}, A CROSSROADS={cross_sum}",
    )

    stage1_cipher_prime_sum = prime_sum(ct1)
    stage1_plain_prime_sum = prime_sum(pt1)
    r.check(
        "8. Additional reproducible observations",
        "The Stage-1 ciphertext associated with AS I GO THE has prime-value sum 301",
        stage1_cipher_prime_sum == 301,
        f"ciphertext sum={stage1_cipher_prime_sum}; plaintext sum={stage1_plain_prime_sum}. The 301 value belongs to L-AE-N-TH-P-U/V-X under this prime table.",
    )

    simple_p = 1 / (29 ** 2)
    r.check(
        "8. Additional reproducible observations",
        "The simple J -> OE estimate 1/29^2 equals about 0.119%",
        math.isclose(simple_p * 100, 0.1189060642, rel_tol=1e-8),
        f"1/841={simple_p:.9f} = {simple_p*100:.6f}%",
    )
    r.check(
        "8. Additional reproducible observations",
        "0.0041% is arithmetically of the same order as approximately 1 in 24,000",
        abs((1 / 24000) * 100 - 0.0041) < 0.0001,
        f"1/24000={(1/24000)*100:.6f}%",
    )

    # EA-G-AE is a real matrix pattern, but the MD's 'false path' interpretation
    # is not a deterministic claim. We record the hard fact and keep the choice as INFO.
    ea_g_ae_occ = []
    # Search equally spaced straight triples at any spacing 1..13.
    for row in range(1, 28):
        for col in range(1, 28):
            for direction, (dr0, dc0) in DIRECTIONS.items():
                for step in range(1, 14):
                    coords = [(row + dr0 * step * i, col + dc0 * step * i) for i in range(3)]
                    if all(1 <= rr <= 27 and 1 <= cc <= 27 for rr, cc in coords):
                        if [grid.at(c) for c in coords] == ["EA", "G", "AE"]:
                            ea_g_ae_occ.append((coords, step, direction))
    # Deduplicate reversed paths by coordinate set.
    unique_ea_g_ae = {tuple(sorted(coords)) for coords, _, _ in ea_g_ae_occ}
    r.info(
        "8. Additional reproducible observations",
        "EA-G-AE exists as an equally spaced straight pattern, but 'false path' is interpretive",
        f"unique straight coordinate sets found={len(unique_ea_g_ae)}",
    )

    # ------------------------------------------------------------------
    # Claims that cannot be independently reproduced from the MD + rune file
    # ------------------------------------------------------------------
    r.na(
        "9. Claims requiring additional source/criteria",
        "Random-shuffle probability 0.0041% as an empirical result",
        "The MD reports the estimate but does not specify the exact randomization procedure, search window, stopping rule, or selection criteria. The arithmetic 0.0041% ~ 1/24,000 is checked above; the experiment itself is not reproducible from these files alone.",
    )
    r.na(
        "9. Claims requiring additional source/criteria",
        "The broad H-TH-H 'only mirrored structure in the lower area' wording",
        f"The exact H-TH-H token pattern is globally unique in this 27x27 grid (count={hthh_count}), but 'lower area' is not formally bounded in the MD, so the broader search-space claim should not be assigned a probability without a precise region/node definition.",
    )
    r.na(
        "9. Claims requiring additional source/criteria",
        "Separator/dot alignments and separator-count sum 14",
        "other-stuff/0-2-runes.txt contains rune tokens only; separator positions/counts are not encoded in this file.",
    )
    r.na(
        "9. Claims requiring additional source/criteria",
        "2014 message.txt.asc hidden-space primes 2..37 except 19",
        "The external 2014 source file is not part of the Volume-1 rune dataset used by this verifier.",
    )
    r.na(
        "9. Claims requiring additional source/criteria",
        "The statement that AE-I-EA also appears in the separate 3x3 matrix",
        "The separate 3x3 source matrix is not provided as machine-readable input to this verifier.",
    )
    r.na(
        "9. Claims requiring additional source/criteria",
        "Global visual symmetry, dot-line patterns, GEB/RTN meaning, and thematic interpretations",
        "These are interpretive/contextual observations rather than falsifiable arithmetic checks under the stated Volume-1 formulas.",
    )
    r.na(
        "9. Claims requiring additional source/criteria",
        "A universal deterministic movement rule",
        "Volume 1 explicitly does not claim one. The script therefore verifies each stated local movement with its stated origin/value instead of inventing a global navigation formula.",
    )

    return r


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def locate_rune_file(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(path)
        return path

    here = Path(__file__).resolve().parent
    candidates = [
        here / "other-stuff" / "0-2-runes.txt",  # script at repository root
        here / "0-2-runes.txt",                  # script inside other-stuff
        Path.cwd() / "other-stuff" / "0-2-runes.txt",
        Path.cwd() / "0-2-runes.txt",
    ]
    for path in candidates:
        if path.exists():
            return path.resolve()

    searched = "\n  - ".join(str(p) for p in candidates)
    raise FileNotFoundError(
        "Could not find 0-2-runes.txt. Searched:\n  - " + searched
        + "\nRun with --runes PATH to specify it explicitly."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reproduce the mechanically testable claims in SOLUTION 0-2 Volume 1."
    )
    parser.add_argument(
        "--runes",
        help="Path to other-stuff/0-2-runes.txt (auto-detected when omitted).",
    )
    args = parser.parse_args()

    try:
        rune_path = locate_rune_file(args.runes)
        grid = Grid.from_file(rune_path)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 2

    print("SOLUTION 0-2 — Volume 1 verifier")
    print(f"Rune source: {rune_path}")
    print("Coordinates: 1-based (row, column)")
    print("Arithmetic: zero-based Gematria Primus, Euler phi, Möbius mu, mod 29")

    report = verify(grid)
    report.print()
    return 1 if report.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
