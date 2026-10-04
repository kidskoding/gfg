import pytest
from helpers import load

lps_length = load("02_strings.44_longest_palindromic_subsequence").lps_length


@pytest.mark.parametrize(
    "s, expected",
    [
        ("bbabcbcab", 7),
        ("agbdba", 5),
        ("bbbab", 4),
        ("cbbd", 2),
        ("aaaa", 4),
        ("abcd", 1),
        ("a", 1),
        ("", 0),
    ],
)
def test_lps_length(s, expected):
    assert lps_length(s) == expected
