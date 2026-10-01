import pytest
from helpers import load

string_length = load("recursion.08_length_of_string").string_length


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcd", 4),
        ("GEEKSFORGEEKS", 13),
        ("a", 1),
        ("", 0),
        ("  ", 2),
        ("hello world", 11),
        ("x" * 300, 300),
    ],
)
def test_string_length(s, expected):
    assert string_length(s) == expected
