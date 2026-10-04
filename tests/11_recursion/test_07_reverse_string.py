import pytest
from helpers import load

reverse_string = load("11_recursion.07_reverse_string").reverse_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Geeks for Geeks", "skeeG rof skeeG"),
        ("abcd", "dcba"),
        ("ab", "ba"),
        ("a", "a"),
        ("", ""),
        ("racecar", "racecar"),
        ("aaab", "baaa"),
        ("12 34!", "!43 21"),
    ],
)
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected
