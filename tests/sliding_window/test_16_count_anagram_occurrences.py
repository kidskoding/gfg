import pytest
from helpers import load

count_anagrams = load("sliding_window.16_count_anagram_occurrences").count_anagrams


@pytest.mark.parametrize(
    "txt, pat, expected",
    [
        ("forxxorfxdofr", "for", 3),
        ("aabaabaa", "aaba", 4),
        ("cbaebabacd", "abc", 2),
        ("aaaa", "aa", 3),  # overlapping
        ("abc", "d", 0),
        ("ab", "abc", 0),
    ],
)
def test_count_anagrams(txt, pat, expected):
    assert count_anagrams(txt, pat) == expected
