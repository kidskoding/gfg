import pytest
from helpers import load

lcs_length = load("dynamic_programming.01_longest_common_subsequence").lcs_length


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ABCDGH", "AEDFHR", 3),
        ("AGGTAB", "GXTXAYB", 4),
        ("ABC", "ACD", 2),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("aaaa", "aa", 2),
        ("abc", "", 0),
        ("", "", 0),
    ],
)
def test_lcs_length(s1, s2, expected):
    assert lcs_length(s1, s2) == expected
