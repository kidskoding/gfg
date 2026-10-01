import pytest
from helpers import load

smallest_window = load("strings.28_smallest_window_containing_all").smallest_window


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("timetopractice", "toc", "toprac"),
        ("zoomlazapzo", "oza", "apzo"),
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("xaybxa", "ab", "ayb"),  # tie: leftmost wins
        ("aa", "aa", "aa"),  # multiplicity matters
        ("a", "a", "a"),
        ("zoom", "zooe", ""),
        ("abc", "d", ""),
    ],
)
def test_smallest_window(s, p, expected):
    assert smallest_window(s, p) == expected
