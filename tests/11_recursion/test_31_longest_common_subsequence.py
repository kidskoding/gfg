import pytest
from helpers import load

lcs = load("11_recursion.31_longest_common_subsequence").lcs


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ABC", "ACD", 2),
        ("AGGTAB", "GXTXAYB", 4),
        ("ABCDGH", "AEDFHR", 3),
        ("ABC", "CBA", 1),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
        ("aaaa", "aa", 2),
    ],
)
def test_lcs(s1, s2, expected):
    assert lcs(s1, s2) == expected
