import pytest
from helpers import load

rabin_karp_search = load("02_strings.40_rabin_karp_search").rabin_karp_search


@pytest.mark.parametrize(
    "text, pat, expected",
    [
        ("aabaacaadaabaaba", "aaba", [0, 9, 12]),
        ("GEEKS FOR GEEKS", "GEEK", [0, 10]),
        ("THIS IS A TEST TEXT", "TEST", [10]),
        ("abababab", "abab", [0, 2, 4]),  # overlapping
        ("aaaaa", "aa", [0, 1, 2, 3]),
        ("ab", "ab", [0]),
        ("abc", "d", []),
        ("abc", "abcd", []),
        ("", "a", []),
    ],
)
def test_rabin_karp_search(text, pat, expected):
    assert rabin_karp_search(text, pat) == expected
