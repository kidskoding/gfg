import pytest
from helpers import load

is_scramble = load("recursion.38_scrambled_strings").is_scramble


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("coder", "ocder", True),
        ("abcde", "caebd", False),
        ("great", "rgeat", True),
        ("great", "rgtae", True),
        ("ab", "ba", True),
        ("a", "a", True),
        ("abcd", "bdac", False),
        ("abc", "ab", False),  # lengths differ
        ("abc", "abd", False),  # different letters
    ],
)
def test_is_scramble(s1, s2, expected):
    assert is_scramble(s1, s2) is expected
