import pytest
from helpers import load

reverse_string = load("06_stacks.02_reverse_string").reverse_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", "olleh"),
        ("GeeksforGeeks", "skeeGrofskeeG"),
        ("ab cd", "dc ba"),
        ("racecar", "racecar"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected
