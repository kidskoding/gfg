import pytest
from helpers import load

string_to_int = load("11_recursion.27_string_to_integer").string_to_int


@pytest.mark.parametrize(
    "s, expected",
    [
        ("1235", 1235),
        ("0", 0),
        ("9", 9),
        ("007", 7),
        ("1000", 1000),
        ("-123", -123),
        ("-5", -5),
        ("2147483648", 2147483648),
    ],
)
def test_string_to_int(s, expected):
    result = string_to_int(s)
    assert type(result) is int
    assert result == expected
