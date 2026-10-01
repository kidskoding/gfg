import pytest
from helpers import load

remove_and_reverse = load("two_pointers.21_remove_and_reverse").remove_and_reverse


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abab", "ba"),
        ("dddd", "d"),
        ("abcabc", "bac"),
        ("aabb", "ab"),
        ("xyzy", "yzx"),
        ("abc", "abc"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_remove_and_reverse(s, expected):
    assert remove_and_reverse(s) == expected
