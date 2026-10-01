import pytest
from helpers import load

longest_prefix_suffix = load("strings.26_longest_prefix_suffix").longest_prefix_suffix


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abab", 2),
        ("aabcdaabc", 4),
        ("abcab", 2),
        ("aaaa", 3),  # proper prefix only
        ("abc", 0),
        ("a", 0),
        ("", 0),
    ],
)
def test_longest_prefix_suffix(s, expected):
    assert longest_prefix_suffix(s) == expected
