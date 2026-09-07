#!/usr/bin/env python3
"""
Verifier for SOLUTION 0-2 — Volume 2.

This script checks the mechanically reproducible claims in:
    other-stuff/md/0-2-volume-2.md
against:
    other-stuff/0-2-runes.txt

The report deliberately separates:
    PASS  - reproduced directly from the rune grid and stated formulas
    FAIL  - a mechanically testable claim did not match
    INFO  - extra computed context that is useful but not itself a Volume-2 claim
    N/A   - a hypothesis / selection rule that cannot be proved from the grid alone

The verifier is standalone and uses only the Python 3 standard library.

Typical use from the repository root:
    python3 verify_volume_2.py

Or with an explicit rune file:
    python3 verify_volume_2.py --runes other-stuff/0-2-runes.txt
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


# -----------------------------------------------------------------------------
# Gematria Primus — zero-based rune order used in Volumes 1 and 2
# -----------------------------------------------------------------------------

RUNES = [
    "F", "U/V", "TH", "O", "R", "C/K", "G", "W", "H", "N",
    "I", "J", "EO", "P", "X", "S/Z", "T", "B", "E", "M",
    "L", "NG", "OE", "D", "A", "AE", "Y", "IA/O", "EA",
]

INDEX = {rune: i for i, rune in enumerate(RUNES)}
MODULUS = 29


# -----------------------------------------------------------------------------
# Number-theory helpers
# -----------------------------------------------------------------------------

def phi(n: int) -> int:
    """Euler's totient function φ(n), for n >= 1."""
    if n < 1:
        raise ValueError("phi() expects n >= 1")

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


def mobius(n: int) -> int:
    """Möbius function μ(n), for n >= 1."""
    if n < 1:
        raise ValueError("mobius() expects n >= 1")
    if n == 1:
        return 1

    x = n
    factors = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            factors += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1

    if x > 1:
        factors += 1
    return -1 if factors % 2 else 1


def rune_for_index(value: int) -> str:
    """Convert an integer to a rune using mod-29 Gematria Primus."""
    return RUNES[value % MODULUS]


# -----------------------------------------------------------------------------
# Key operations
# -----------------------------------------------------------------------------

def compile_mirrored_node(node: Sequence[str]) -> tuple[str, str, str]:
    """Volume rule: a-b-a -> a-phi(b)-a."""
    if len(node) != 3:
        raise ValueError("A node must contain exactly three runes")
    left, center, right = node
    if left != right:
        raise ValueError(f"Expected a mirrored node a-b-a, got {tuple(node)}")
    return left, rune_for_index(phi(INDEX[center])), right


def totient_signature(key: Sequence[str]) -> tuple[int, ...]:
    """signature(K) = (phi(K1), phi(K2), ...)."""
    return tuple(phi(INDEX[rune]) for rune in key)


def mobius_terms(key: Sequence[str]) -> tuple[int, ...]:
    """Return μ(φ(K_i)) for each rune in a key."""
    return tuple(mobius(phi(INDEX[rune])) for rune in key)


def key_phase(key: Sequence[str]) -> int:
    """p = sum(mu(phi(K_i))) mod 3."""
    return sum(mobius_terms(key)) % 3


def rotate_left(items: Sequence[str], amount: int) -> tuple[str, ...]:
    amount %= len(items)
    return tuple(items[amount:]) + tuple(items[:amount])


def repeat_key(key: Sequence[str], length: int) -> list[str]:
    return [key[i % len(key)] for i in range(length)]


def decrypt_mod29(ciphertext: Sequence[str], key: Sequence[str]) -> list[str]:
    """P = C - K (mod 29)."""
    if len(ciphertext) != len(key):
        raise ValueError("ciphertext and key must have the same length")
    return [
        rune_for_index(INDEX[c] - INDEX[k])
        for c, k in zip(ciphertext, key)
    ]


def plaintext_for_phase(
    ciphertext: Sequence[str], key: Sequence[str], phase: int
) -> list[str]:
    """Decrypt with one of the three cyclic rotations of a 3-rune key."""
    active_cycle = rotate_left(key, phase)
    return decrypt_mod29(ciphertext, repeat_key(active_cycle, len(ciphertext)))


def tokens(items: Sequence[str]) -> str:
    return "-".join(items)


# -----------------------------------------------------------------------------
# 27x27 grid helpers — all coordinates are 1-based
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
        rune_tokens = text.split()

        if len(rune_tokens) != 729:
            raise ValueError(f"Expected 729 rune tokens, found {len(rune_tokens)}")

        unknown = sorted(set(rune_tokens) - set(RUNES))
        if unknown:
            raise ValueError(f"Unknown rune tokens: {unknown}")

        rows = [rune_tokens[i:i + 27] for i in range(0, 729, 27)]
        return cls(rows)

    def at(self, coord: Coord) -> str:
        row, col = coord
        if not (1 <= row <= 27 and 1 <= col <= 27):
            raise IndexError(f"Coordinate outside 27x27 grid: {coord}")
        return self.rows[row - 1][col - 1]

    def move(self, start: Coord, direction: str, distance: int) -> Coord:
        dr, dc = DIRECTIONS[direction]
        row, col = start
        dest = (row + dr * distance, col + dc * distance)
        self.at(dest)  # validates destination
        return dest

    def read(self, start: Coord, direction: str, length: int) -> list[str]:
        dr, dc = DIRECTIONS[direction]
        row, col = start
        return [
            self.at((row + dr * i, col + dc * i))
            for i in range(length)
        ]

    def runes_at(self, coords: Sequence[Coord]) -> list[str]:
        return [self.at(coord) for coord in coords]

    def count_exact_straight_pattern(
        self, sequence: Sequence[str], step: int = 1
    ) -> int:
        """
        Count exact straight occurrences, ignoring reverse-direction duplicates.

        `step=1` means contiguous cells.  `step=2` means one cell is skipped
        between each rune, which is needed for NG(13,8)-B(15,8)-NG(17,8).
        """
        unique: set[tuple[Coord, ...]] = set()

        for row in range(1, 28):
            for col in range(1, 28):
                for dr, dc in DIRECTIONS.values():
                    coords: list[Coord] = []
                    ok = True

                    for i, expected in enumerate(sequence):
                        coord = (row + dr * step * i, col + dc * step * i)
                        r, c = coord
                        if not (1 <= r <= 27 and 1 <= c <= 27):
                            ok = False
                            break
                        if self.at(coord) != expected:
                            ok = False
                            break
                        coords.append(coord)

                    if ok:
                        # A palindrome found forwards and backwards is one object.
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

    @property
    def failed(self) -> bool:
        return any(result.status == "FAIL" for result in self.results)

    def print(self) -> None:
        current_section: str | None = None

        for result in self.results:
            if result.section != current_section:
                current_section = result.section
                print(f"\n=== {current_section} ===")

            print(f"[{result.status:4}] {result.claim}")
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
            print("Core reproducible Volume-2 checks completed without a mismatch.")
        else:
            print("One or more reproducible claims did not match; inspect FAIL lines above.")


# -----------------------------------------------------------------------------
# Volume 2 verification
# -----------------------------------------------------------------------------

def verify(grid: Grid) -> Report:
    r = Report()

    # ------------------------------------------------------------------
    # 1. Source data and the Volume-1 handoff state
    # ------------------------------------------------------------------
    flat = [rune for row in grid.rows for rune in row]
    r.check(
        "1. Source data and Volume-1 handoff",
        "729 rune tokens form exactly a 27 x 27 grid",
        len(flat) == 729 and len(grid.rows) == 27 and all(len(row) == 27 for row in grid.rows),
    )

    parent_node_coords = [(25, 19), (26, 19), (27, 19)]
    parent_node = tuple(grid.runes_at(parent_node_coords))
    r.check(
        "1. Source data and Volume-1 handoff",
        "The preserved parent node is H-TH-H at column 19, rows 25..27",
        parent_node == ("H", "TH", "H"),
        f"node={tokens(parent_node)}; center=TH(26,19)",
    )

    cold_key = compile_mirrored_node(parent_node)
    r.check(
        "1. Source data and Volume-1 handoff",
        "phi(TH=2)=1=U/V, so H-TH-H compiles to H-U/V-H",
        phi(INDEX["TH"]) == 1 and cold_key == ("H", "U/V", "H"),
        f"compiled_key={tokens(cold_key)}",
    )

    cold_signature = totient_signature(cold_key)
    r.check(
        "1. Source data and Volume-1 handoff",
        "The COLD key H-U/V-H has totient signature 4-1-4",
        cold_signature == (4, 1, 4),
        f"signature={list(cold_signature)}",
    )

    # Reproduce the minimum necessary part of Volume 1 instead of simply
    # trusting the claimed endpoint.
    cold_ct = grid.read((14, 7), "UP", 4)
    cold_phase = key_phase(cold_key)
    cold_active = repeat_key(rotate_left(cold_key, cold_phase), len(cold_ct))
    cold_pt = decrypt_mod29(cold_ct, cold_active)
    r.check(
        "1. Source data and Volume-1 handoff",
        "The Volume-1 COLD handoff reproduces G-J-EA-A -> C-O-L-D",
        cold_ct == ["G", "J", "EA", "A"]
        and cold_phase == 1
        and cold_pt == ["C/K", "O", "L", "D"],
        f"ciphertext={tokens(cold_ct)}; phase={cold_phase}; plaintext={tokens(cold_pt)}",
    )

    cold_endpoint = (11, 7)
    r.check(
        "1. Source data and Volume-1 handoff",
        "The final COLD ciphertext rune is A at (11,7)",
        grid.at(cold_endpoint) == "A" and cold_ct[-1] == "A",
        f"endpoint={grid.at(cold_endpoint)}{cold_endpoint}",
    )

    # ------------------------------------------------------------------
    # 2. Structural fingerprint at the COLD endpoint
    # ------------------------------------------------------------------
    endpoint_node_coords = [(10, 7), (11, 7), (12, 7)]
    endpoint_node = tuple(grid.runes_at(endpoint_node_coords))
    r.check(
        "2. COLD endpoint fingerprint",
        "A(11,7) is the center of contiguous EA-A-EA",
        endpoint_node == ("EA", "A", "EA"),
        f"EA(10,7)-A(11,7)-EA(12,7)",
    )

    endpoint_signature = totient_signature(endpoint_node)
    r.check(
        "2. COLD endpoint fingerprint",
        "EA-A-EA has totient signature 12-8-12",
        endpoint_signature == (12, 8, 12),
        f"phi(EA=28)={phi(28)}, phi(A=24)={phi(24)}, signature={list(endpoint_signature)}",
    )

    endpoint_count = grid.count_exact_straight_pattern(["EA", "A", "EA"], step=1)
    r.info(
        "2. COLD endpoint fingerprint",
        "Exact contiguous EA-A-EA is globally unique in this 27 x 27 grid",
        f"undirected exact-pattern count={endpoint_count}",
    )

    # ------------------------------------------------------------------
    # 3. Inherited 4-1-4 movement locates B
    # ------------------------------------------------------------------
    after_d4 = grid.move(cold_endpoint, "DOWN", cold_signature[0])
    after_r1 = grid.move(after_d4, "RIGHT", cold_signature[1])

    r.check(
        "3. Inherited 4-1-4 movement",
        "D4 from A(11,7) reaches S/Z(15,7)",
        after_d4 == (15, 7) and grid.at(after_d4) == "S/Z",
        f"A(11,7) -> D{cold_signature[0]} -> {grid.at(after_d4)}{after_d4}",
    )
    r.check(
        "3. Inherited 4-1-4 movement",
        "R1 from S/Z(15,7) reaches B(15,8)",
        after_r1 == (15, 8) and grid.at(after_r1) == "B",
        f"S/Z(15,7) -> R{cold_signature[1]} -> {grid.at(after_r1)}{after_r1}",
    )
    r.check(
        "3. Inherited 4-1-4 movement",
        "The movement distances 4 and 1 are exactly the first two values of the inherited COLD signature 4-1-4",
        cold_signature[:2] == (4, 1),
        f"cold_signature={list(cold_signature)}; movement=D4,R1",
    )

    # ------------------------------------------------------------------
    # 4. NG-B-NG reveals the I MAY key
    # ------------------------------------------------------------------
    imay_node_coords = [(13, 8), (15, 8), (17, 8)]
    imay_node = tuple(grid.runes_at(imay_node_coords))
    r.check(
        "4. Hidden mirrored node and I MAY key",
        "B(15,8) is the center of NG(13,8)-B(15,8)-NG(17,8)",
        imay_node == ("NG", "B", "NG") and imay_node_coords[1] == after_r1,
        f"node={tokens(imay_node)} with equal vertical spacing 2",
    )

    imay_key = compile_mirrored_node(imay_node)
    r.check(
        "4. Hidden mirrored node and I MAY key",
        "phi(B=17)=16=T, so NG-B-NG compiles to NG-T-NG",
        phi(INDEX["B"]) == 16 and imay_key == ("NG", "T", "NG"),
        f"compiled_key={tokens(imay_key)}",
    )

    imay_signature = totient_signature(imay_key)
    r.check(
        "4. Hidden mirrored node and I MAY key",
        "NG-T-NG has totient signature 12-8-12",
        imay_signature == (12, 8, 12),
        f"signature={list(imay_signature)}",
    )
    r.check(
        "4. Hidden mirrored node and I MAY key",
        "EA-A-EA and NG-T-NG have the exact same 12-8-12 signature",
        endpoint_signature == imay_signature == (12, 8, 12),
        f"endpoint_signature={list(endpoint_signature)}; key_signature={list(imay_signature)}",
    )

    imay_node_count = grid.count_exact_straight_pattern(["NG", "B", "NG"], step=2)
    r.info(
        "4. Hidden mirrored node and I MAY key",
        "The exact equally spaced NG-B-NG structure (step 2) is globally unique in the grid",
        f"undirected exact-pattern count={imay_node_count}",
    )

    # ------------------------------------------------------------------
    # 5. Möbius phase and all three I MAY phase alternatives
    # ------------------------------------------------------------------
    imay_mu = mobius_terms(imay_key)
    imay_phase = key_phase(imay_key)
    r.check(
        "5. I MAY Möbius phase",
        "mu(12), mu(8), mu(12) are all 0, so NG-T-NG has phase 0",
        imay_signature == (12, 8, 12)
        and imay_mu == (0, 0, 0)
        and imay_phase == 0,
        f"signature={list(imay_signature)}; mu={list(imay_mu)}; phase={imay_phase}",
    )

    imay_ct = grid.read((26, 19), "LEFT", 4)
    expected_imay_ct = ["TH", "G", "T", "E"]
    r.check(
        "5. I MAY Möbius phase",
        "Reading left from preserved center TH(26,19) gives TH-G-T-E",
        imay_ct == expected_imay_ct,
        f"ciphertext={tokens(imay_ct)}; coordinates=(26,19)->(26,16)",
    )

    imay_phase_results = [plaintext_for_phase(imay_ct, imay_key, p) for p in range(3)]
    expected_imay_phases = [
        ["I", "M", "A", "Y"],
        ["S/Z", "X", "A", "TH"],
        ["I", "X", "F", "Y"],
    ]
    r.check(
        "5. I MAY Möbius phase",
        "The three cyclic phases reproduce the Volume-2 I MAY phase table",
        imay_phase_results == expected_imay_phases,
        "phase0={} ; phase1={} ; phase2={}".format(
            tokens(imay_phase_results[0]),
            tokens(imay_phase_results[1]),
            tokens(imay_phase_results[2]),
        ),
    )
    r.check(
        "5. I MAY Möbius phase",
        "The numerically selected phase 0 decrypts TH-G-T-E to I-M-A-Y",
        imay_phase == 0 and imay_phase_results[imay_phase] == ["I", "M", "A", "Y"],
        f"selected_plaintext={tokens(imay_phase_results[imay_phase])}",
    )

    # ------------------------------------------------------------------
    # 6. Parent-state return / endpoint of I MAY
    # ------------------------------------------------------------------
    r.check(
        "6. I MAY result and next-node handoff",
        "The I MAY ciphertext starts exactly at the preserved H-TH-H center TH(26,19)",
        grid.at((26, 19)) == "TH" and parent_node[1] == "TH",
        "The same parent node that generated the COLD key is reused as the read origin.",
    )

    imay_endpoint = (26, 16)
    r.check(
        "6. I MAY result and next-node handoff",
        "The I MAY ciphertext ends at E(26,16)",
        imay_ct[-1] == "E" and grid.at(imay_endpoint) == "E",
        f"endpoint={grid.at(imay_endpoint)}{imay_endpoint}",
    )

    cry_node_coords = [(24, 16), (25, 16), (26, 16)]
    cry_node = tuple(grid.runes_at(cry_node_coords))
    r.check(
        "6. I MAY result and next-node handoff",
        "The final E of I MAY is immediately the lower edge of E-X-E",
        cry_node == ("E", "X", "E") and cry_node_coords[-1] == imay_endpoint,
        "E(24,16)-X(25,16)-E(26,16)",
    )

    cry_node_count = grid.count_exact_straight_pattern(["E", "X", "E"], step=1)
    r.info(
        "6. I MAY result and next-node handoff",
        "Exact contiguous E-X-E is globally unique in this 27 x 27 grid",
        f"undirected exact-pattern count={cry_node_count}",
    )

    # ------------------------------------------------------------------
    # 7. E-X-E generates E-G-E and Möbius fixes phase 1
    # ------------------------------------------------------------------
    cry_key = compile_mirrored_node(cry_node)
    r.check(
        "7. CRY key and Möbius phase",
        "phi(X=14)=6=G, so E-X-E compiles to E-G-E",
        phi(INDEX["X"]) == 6 and cry_key == ("E", "G", "E"),
        f"compiled_key={tokens(cry_key)}",
    )

    cry_signature = totient_signature(cry_key)
    r.check(
        "7. CRY key and Möbius phase",
        "E-G-E has totient signature 6-2-6",
        cry_signature == (6, 2, 6),
        f"signature={list(cry_signature)}",
    )

    cry_mu = mobius_terms(cry_key)
    cry_phase = key_phase(cry_key)
    active_cry_cycle = rotate_left(cry_key, cry_phase)
    r.check(
        "7. CRY key and Möbius phase",
        "mu(6)=+1, mu(2)=-1, mu(6)=+1 gives phase 1",
        cry_mu == (1, -1, 1) and cry_phase == 1,
        f"mu={list(cry_mu)}; sum={sum(cry_mu)}; phase={cry_phase}",
    )
    r.check(
        "7. CRY key and Möbius phase",
        "Phase 1 rotates E-G-E to the active key G-E-E",
        active_cry_cycle == ("G", "E", "E"),
        f"active_key={tokens(active_cry_cycle)}",
    )

    # ------------------------------------------------------------------
    # 8. Inherited 6 reaches J and exposes the CRY ciphertext
    # ------------------------------------------------------------------
    cry_center = (25, 16)
    inherited_six = cry_signature[0]
    j_coord = grid.move(cry_center, "UP", inherited_six)
    r.check(
        "8. Inherited value 6 and CRY ciphertext",
        "The outer totient value of E-G-E is 6",
        inherited_six == 6 and cry_signature[-1] == 6,
        f"signature={list(cry_signature)}",
    )
    r.check(
        "8. Inherited value 6 and CRY ciphertext",
        "UP 6 from X(25,16) lands exactly on J(19,16)",
        j_coord == (19, 16) and grid.at(j_coord) == "J",
        f"X(25,16) -> U{inherited_six} -> {grid.at(j_coord)}{j_coord}",
    )

    j_node_coords = [(18, 16), (19, 16), (20, 16)]
    j_node = tuple(grid.runes_at(j_node_coords))
    r.check(
        "8. Inherited value 6 and CRY ciphertext",
        "J(19,16) is the exact center of contiguous OE-J-OE",
        j_node == ("OE", "J", "OE"),
        "OE(18,16)-J(19,16)-OE(20,16)",
    )

    j_node_count = grid.count_exact_straight_pattern(["OE", "J", "OE"], step=1)
    r.info(
        "8. Inherited value 6 and CRY ciphertext",
        "Exact contiguous OE-J-OE is globally unique in this 27 x 27 grid",
        f"undirected exact-pattern count={j_node_count}",
    )

    cry_ct = grid.read(j_coord, "UP", 3)
    r.check(
        "8. Inherited value 6 and CRY ciphertext",
        "Reading upward from J(19,16) gives J-OE-S/Z",
        cry_ct == ["J", "OE", "S/Z"],
        f"ciphertext={tokens(cry_ct)}; coordinates=(19,16)->(17,16)",
    )

    # ------------------------------------------------------------------
    # 9. Decrypt CRY and audit all three phases
    # ------------------------------------------------------------------
    cry_phase_results = [plaintext_for_phase(cry_ct, cry_key, p) for p in range(3)]
    expected_cry_phases = [
        ["OE", "T", "Y"],
        ["C/K", "R", "Y"],
        ["OE", "R", "N"],
    ]
    r.check(
        "9. CRY decryption",
        "The three cyclic phases reproduce the Volume-2 CRY phase table",
        cry_phase_results == expected_cry_phases,
        "phase0={} ; phase1={} ; phase2={}".format(
            tokens(cry_phase_results[0]),
            tokens(cry_phase_results[1]),
            tokens(cry_phase_results[2]),
        ),
    )
    r.check(
        "9. CRY decryption",
        "The numerically selected phase 1 decrypts J-OE-S/Z to C/K-R-Y",
        cry_phase == 1 and cry_phase_results[cry_phase] == ["C/K", "R", "Y"],
        f"selected_plaintext={tokens(cry_phase_results[cry_phase])}",
    )
    r.check(
        "9. CRY decryption",
        "The active G-E-E subtraction is exactly J-G=C/K, OE-E=R, S/Z-E=Y (mod 29)",
        [
            (INDEX[c] - INDEX[k]) % MODULUS
            for c, k in zip(cry_ct, active_cry_cycle)
        ] == [INDEX["C/K"], INDEX["R"], INDEX["Y"]],
        "{}-{}-{} -> {}".format(tokens(cry_ct), tokens(active_cry_cycle), "mod29", tokens(cry_phase_results[1])),
    )

    # ------------------------------------------------------------------
    # 10. Totient-chain / structural-inheritance cross-checks
    # ------------------------------------------------------------------
    r.check(
        "10. Totient-chain cross-checks",
        "The 12-8-12 endpoint fingerprint exactly reappears as the I MAY key signature",
        endpoint_signature == imay_signature == (12, 8, 12),
    )
    r.check(
        "10. Totient-chain cross-checks",
        "The value 4 is first present in the COLD signature and is reused as D4 after COLD",
        cold_signature[0] == 4 and after_d4 == (15, 7),
    )
    r.check(
        "10. Totient-chain cross-checks",
        "The value 1 is present in the COLD signature and is reused as R1 after D4",
        cold_signature[1] == 1 and after_r1 == (15, 8),
    )
    r.check(
        "10. Totient-chain cross-checks",
        "The value 6 is part of the CRY-key signature and is reused as U6 from X",
        cry_signature[0] == 6 and j_coord == (19, 16),
    )
    r.check(
        "10. Totient-chain cross-checks",
        "The Möbius rule remains unchanged from I MAY to CRY",
        key_phase(imay_key) == 0 and key_phase(cry_key) == 1,
        "same formula p=sum(mu(phi(K_i))) mod 3; phases are 0 then 1",
    )

    # Compare with the non-mirrored hidden-key example referenced in Volume 2.
    hidden_nonmirror_coords = [(4, 23), (14, 23), (24, 23)]
    hidden_nonmirror = tuple(grid.runes_at(hidden_nonmirror_coords))
    r.check(
        "10. Totient-chain cross-checks",
        "The earlier non-mirrored hidden structure H-NG-C/K exists on column 23 with equal spacing 10",
        hidden_nonmirror == ("H", "NG", "C/K"),
        f"node={tokens(hidden_nonmirror)} at rows 4,14,24",
    )
    r.check(
        "10. Totient-chain cross-checks",
        "H-NG-C/K is non-mirrored, while NG-B-NG and E-X-E are mirrored",
        hidden_nonmirror[0] != hidden_nonmirror[2]
        and imay_node[0] == imay_node[2]
        and cry_node[0] == cry_node[2],
    )

    # Reproduce the earlier hidden-key example that Volume 2 uses for comparison.
    turns_crossroads = (14, 19)
    hidden_center = grid.move(turns_crossroads, "RIGHT", 4)
    hidden_top = grid.move(hidden_center, "UP", 10)
    hidden_bottom = grid.move(hidden_center, "DOWN", 10)
    r.check(
        "10. Totient-chain cross-checks",
        "In the earlier hidden-key example, R4 from A(14,19) locates NG(14,23), and +/-10 locates H/C/K",
        hidden_center == (14, 23)
        and grid.at(hidden_center) == "NG"
        and hidden_top == (4, 23)
        and grid.at(hidden_top) == "H"
        and hidden_bottom == (24, 23)
        and grid.at(hidden_bottom) == "C/K",
        "A(14,19) -> R4 -> NG(14,23); U10 -> H(4,23); D10 -> C/K(24,23)",
    )

    hidden_signature = totient_signature(hidden_nonmirror)
    hidden_phase = key_phase(hidden_nonmirror)
    hidden_ct = grid.read(turns_crossroads, "UP", 5)
    hidden_active = repeat_key(rotate_left(hidden_nonmirror, hidden_phase), len(hidden_ct))
    hidden_pt = decrypt_mod29(hidden_ct, hidden_active)
    r.check(
        "10. Totient-chain cross-checks",
        "The non-mirrored H-NG-C/K comparison key is used directly at phase 0 and decrypts A-OE-N-B-W to T-U-R-N-S/Z",
        hidden_signature == (4, 12, 4)
        and hidden_phase == 0
        and hidden_ct == ["A", "OE", "N", "B", "W"]
        and hidden_pt == ["T", "U/V", "R", "N", "S/Z"],
        f"signature={list(hidden_signature)}; phase={hidden_phase}; ciphertext={tokens(hidden_ct)}; plaintext={tokens(hidden_pt)}",
    )

    # ------------------------------------------------------------------
    # 11. Claims that need a rule/criterion beyond arithmetic + grid data
    # ------------------------------------------------------------------
    r.na(
        "11. Claims requiring additional rule or criterion",
        "A deterministic rule that activates hidden-key search after COLD",
        "Volume 2 explicitly states that the activation condition is not yet known. This script can verify the stated D4/R1 route, but cannot derive the decision to start that search from first principles.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "A deterministic rule that chooses D4 then R1, including direction and order",
        "The values 4 and 1 are genuinely inherited from 4-1-4 and the stated moves land on B, but Volume 2 does not yet provide a universal selector for DOWN vs RIGHT or for their order.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "A universal rule saying every mirrored hidden node must compile its center with phi and every non-mirrored hidden key must be used directly",
        "The concrete examples are reproducible; the universal classification rule is still a model hypothesis rather than a theorem derivable from this dataset alone.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "A formal parent-state-return rule explaining why NG-T-NG is applied back at H-TH-H",
        "The return is geometrically reproducible and gives I MAY, but Volume 2 lists formal representation of parent-state return as unresolved.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "A deterministic rule choosing UP for the inherited value 6 after E-X-E",
        "UP 6 does land exactly on J, but the volume explicitly says the fully deterministic movement-direction rule is still unknown.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "The linguistic ranking that I MAY and CRY are the strongest plaintext candidates",
        "The script reproduces the arithmetic outputs and all three key phases, but 'strongest' is a cryptanalytic/model-selection judgment rather than a grid-only identity.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "A deterministic continuation after CRY without adding a new rule",
        "Volume 2 explicitly leaves this as the next out-of-sample test of the model.",
    )
    r.na(
        "11. Claims requiring additional rule or criterion",
        "The broad interpretation that totients form a persistent control layer for the whole system",
        "The repeated 4, 1, 12, 8, 6, and 2 relationships checked above are factual; treating them as a universal control layer is the research hypothesis under evaluation.",
    )

    return r


# -----------------------------------------------------------------------------
# Command-line interface
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
        here / "0-2-runes.txt",                  # script beside rune file
        Path.cwd() / "other-stuff" / "0-2-runes.txt",
        Path.cwd() / "0-2-runes.txt",
    ]

    for path in candidates:
        if path.exists():
            return path.resolve()

    searched = "\n  - ".join(str(path) for path in candidates)
    raise FileNotFoundError(
        "Could not find 0-2-runes.txt. Searched:\n  - " + searched
        + "\nRun with --runes PATH to specify it explicitly."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reproduce the mechanically testable claims in SOLUTION 0-2 Volume 2."
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

    print("SOLUTION 0-2 — Volume 2 verifier")
    print(f"Rune source: {rune_path}")
    print("Coordinates: 1-based (row, column)")
    print("Arithmetic: zero-based Gematria Primus, Euler phi, Möbius mu, mod 29")
    print("Scope: COLD handoff -> I MAY -> CRY, totient inheritance, phase audit")

    report = verify(grid)
    report.print()
    return 1 if report.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
