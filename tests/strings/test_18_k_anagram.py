import pytest
from helpers import load

are_k_anagrams = load("strings.18_k_anagram").are_k_anagrams


@pytest.mark.parametrize(
    "s1, s2, k, expected",
    [
        ("anagram", "grammar", 3, True),
        ("anagram", "grammar", 1, False),  # needs 2 changes
        ("geeks", "eggkf", 1, False),
        ("fodr", "gork", 2, True),
        ("abc", "cba", 0, True),
        ("aaa", "bbb", 3, True),
        ("aaa", "bbb", 2, False),
        ("abc", "abcd", 4, False),  # different lengths
    ],
)
def test_are_k_anagrams(s1, s2, k, expected):
    assert are_k_anagrams(s1, s2, k) is expected
