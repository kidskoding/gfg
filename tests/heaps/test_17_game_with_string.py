import pytest
from helpers import load

game_with_string = load("heaps.17_game_with_string").game_with_string


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abccc", 1, 6),
        ("aaab", 2, 2),
        ("aabbcc", 2, 6),
        ("zzzzyyx", 3, 6),
        ("aaaa", 0, 16),
        ("abc", 3, 0),
        ("a", 5, 0),  # k larger than the string
    ],
)
def test_game_with_string(s, k, expected):
    assert game_with_string(s, k) == expected
