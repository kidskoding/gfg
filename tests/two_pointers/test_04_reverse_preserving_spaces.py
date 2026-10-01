import pytest
from helpers import load

reverse_preserving_spaces = load(
    "two_pointers.04_reverse_preserving_spaces"
).reverse_preserving_spaces


@pytest.mark.parametrize(
    "s, expected",
    [
        ("internship at geeks for geeks", "skeegrofsk ee gtapi hsn retni"),
        ("Help others", "sreh topleH"),
        ("abc de", "edc ba"),
        (" a b ", " b a "),
        ("   ", "   "),
        ("x", "x"),
        ("", ""),
    ],
)
def test_reverse_preserving_spaces(s, expected):
    assert reverse_preserving_spaces(s) == expected
