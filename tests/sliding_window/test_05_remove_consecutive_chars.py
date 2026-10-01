import pytest
from helpers import load

remove_consecutive = load(
    "sliding_window.05_remove_consecutive_chars"
).remove_consecutive


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aabb", "ab"),
        ("aabaa", "aba"),
        ("abba", "aba"),
        ("abc", "abc"),
        ("aaaa", "a"),
        ("", ""),
    ],
)
def test_remove_consecutive(s, expected):
    assert remove_consecutive(s) == expected
