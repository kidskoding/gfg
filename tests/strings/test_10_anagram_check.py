import pytest
from helpers import load

are_anagrams = load("strings.10_anagram_check").are_anagrams


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("geeks", "kseeg", True),
        ("listen", "silent", True),
        ("allergy", "allergic", False),
        ("aab", "abb", False),  # same letters, different counts
        ("ab", "a", False),
        ("Listen", "Silent", False),  # case-sensitive
        ("g", "g", True),
        ("", "", True),
    ],
)
def test_are_anagrams(s1, s2, expected):
    assert are_anagrams(s1, s2) is expected
