import pytest
from helpers import load

min_repeats = load("02_strings.22_min_repeats_substring").min_repeats


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("abcd", "cdabcdab", 3),
        ("abc", "cabca", 3),
        ("a", "aa", 2),
        ("abc", "abc", 1),
        ("abc", "b", 1),
        ("aa", "a", 1),
        ("ab", "cab", -1),
        ("abc", "ac", -1),
    ],
)
def test_min_repeats(a, b, expected):
    assert min_repeats(a, b) == expected
