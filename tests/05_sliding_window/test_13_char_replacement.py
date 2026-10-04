import pytest
from helpers import load

longest_char_replacement = load(
    "05_sliding_window.13_char_replacement"
).longest_char_replacement


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABCDE", 1, 2),
        ("ABBB", 2, 4),
        ("AAAA", 0, 4),
        ("ABCDE", 0, 1),
        ("", 2, 0),
    ],
)
def test_longest_char_replacement(s, k, expected):
    assert longest_char_replacement(s, k) == expected
