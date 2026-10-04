import pytest
from helpers import load

longest_palindromic_rearrangement = load(
    "02_strings.42_longest_palindrome_rearrange"
).longest_palindromic_rearrangement


@pytest.mark.parametrize(
    "s, expected",
    [
        ("adbabd", 6),
        ("abcab", 5),
        ("aabbc", 5),
        ("zzabcz", 3),
        ("aabb", 4),
        ("abcde", 1),
        ("a", 1),
        ("", 0),
    ],
)
def test_longest_palindromic_rearrangement(s, expected):
    assert longest_palindromic_rearrangement(s) == expected
