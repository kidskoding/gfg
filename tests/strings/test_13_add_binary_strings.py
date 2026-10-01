import pytest
from helpers import load

add_binary = load("strings.13_add_binary_strings").add_binary


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("1101", "111", "10100"),
        ("00100", "010", "110"),  # strip leading zeros
        ("1111", "1", "10000"),
        ("1", "1", "10"),
        ("000", "0", "0"),
        ("0", "0", "0"),
    ],
)
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected
