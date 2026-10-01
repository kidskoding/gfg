import pytest
from helpers import load

min_window = load("sliding_window.26_min_window_substring").min_window


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("timetopractice", "toc", "toprac"),
        ("zoomlazapzo", "oza", "apzo"),
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
        ("abab", "ab", "ab"),  # leftmost on ties
        ("aa", "aa", "aa"),
        ("zoom", "zooe", ""),
        ("a", "b", ""),
    ],
)
def test_min_window(s, p, expected):
    assert min_window(s, p) == expected
