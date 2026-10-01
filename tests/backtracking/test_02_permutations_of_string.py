import pytest
from helpers import load

permutations = load("backtracking.02_permutations_of_string").permutations


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ABC", ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]),
        ("AB", ["AB", "BA"]),
        ("AAB", ["AAB", "ABA", "BAA"]),
        (
            "CBA",
            ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"],
        ),  # output sorted regardless of input order
        ("AAA", ["AAA"]),
        ("ABAB", ["AABB", "ABAB", "ABBA", "BAAB", "BABA", "BBAA"]),
        ("A", ["A"]),
        ("", [""]),
    ],
)
def test_permutations(s, expected):
    assert permutations(s) == expected


def test_permutations_count_distinct():
    out = permutations("ABCDE")
    assert len(out) == 120
    assert len(set(out)) == 120
