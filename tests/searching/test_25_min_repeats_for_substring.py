import pytest
from helpers import load

min_repeats = load("searching.25_min_repeats_for_substring").min_repeats


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("abcd", "cdabcdab", 3),
        ("ab", "cab", -1),
        ("a", "aa", 2),
        ("abc", "abc", 1),
        ("abc", "b", 1),
        ("aa", "a", 1),  # b shorter than a
        ("abc", "cabca", 3),  # spans three copies
        ("abab", "aba", 1),
        ("abc", "d", -1),
    ],
)
def test_min_repeats(a, b, expected):
    assert min_repeats(a, b) == expected
