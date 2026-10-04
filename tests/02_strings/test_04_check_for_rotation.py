import pytest
from helpers import load

are_rotations = load("02_strings.04_check_for_rotation").are_rotations


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("abcd", "cdab", True),
        ("aab", "aba", True),
        ("abab", "baba", True),
        ("abcd", "acbd", False),
        ("abc", "abcabc", False),  # different lengths
        ("aa", "ab", False),
        ("a", "a", True),
        ("", "", True),
    ],
)
def test_are_rotations(s1, s2, expected):
    assert are_rotations(s1, s2) is expected
