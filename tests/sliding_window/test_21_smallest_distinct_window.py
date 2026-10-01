import pytest
from helpers import load

smallest_distinct_window = load(
    "sliding_window.21_smallest_distinct_window"
).smallest_distinct_window


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aabcbcdbca", 4),
        ("aaab", 2),
        ("geeksforgeeks", 7),
        ("abac", 3),
        ("abc", 3),
        ("aaaa", 1),
        ("", 0),
    ],
)
def test_smallest_distinct_window(s, expected):
    assert smallest_distinct_window(s) == expected
