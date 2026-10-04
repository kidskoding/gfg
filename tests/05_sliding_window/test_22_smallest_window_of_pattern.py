import pytest
from helpers import load

smallest_window_len = load(
    "05_sliding_window.22_smallest_window_of_pattern"
).smallest_window_len


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("timetopractice", "toc", 6),
        ("zoomlazapzo", "oza", 4),
        ("ADOBECODEBANC", "ABC", 4),
        ("zoom", "zooe", -1),
        ("a", "aa", -1),  # multiplicity matters
        ("a", "a", 1),
        ("", "a", -1),
    ],
)
def test_smallest_window_len(s, p, expected):
    assert smallest_window_len(s, p) == expected
