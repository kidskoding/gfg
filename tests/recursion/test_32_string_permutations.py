import pytest
from helpers import load

permutations = load("recursion.32_string_permutations").permutations


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ABC", ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]),
        ("AB", ["AB", "BA"]),
        ("AAB", ["AAB", "ABA", "BAA"]),  # no duplicate permutations
        ("aaa", ["aaa"]),
        ("a", ["a"]),
        ("", [""]),
    ],
)
def test_permutations(s, expected):
    assert sorted(permutations(s)) == sorted(expected)


@pytest.mark.parametrize("s, count", [("abcde", 120), ("aabbc", 30), ("aabb", 6)])
def test_permutations_counts(s, count):
    result = permutations(s)
    assert len(result) == count
    assert len(set(result)) == count
    assert all(sorted(p) == sorted(s) for p in result)
