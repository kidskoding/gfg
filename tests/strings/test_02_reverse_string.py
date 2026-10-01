import pytest
from helpers import load

reverse_string = load("strings.02_reverse_string").reverse_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", "olleh"),
        ("Geeks", "skeeG"),
        ("ab cd", "dc ba"),
        ("aaa", "aaa"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected
