import pytest
from helpers import load

are_isomorphic = load("02_strings.17_isomorphic_strings").are_isomorphic


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("aab", "xxy", True),
        ("egg", "add", True),
        ("paper", "title", True),
        ("aab", "xyz", False),
        ("foo", "bar", False),
        ("ab", "aa", False),  # two chars cannot map to one
        ("badc", "baba", False),
        ("abc", "ab", False),
        ("", "", True),
    ],
)
def test_are_isomorphic(s1, s2, expected):
    assert are_isomorphic(s1, s2) is expected
