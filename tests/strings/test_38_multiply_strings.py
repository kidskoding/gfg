import pytest
from helpers import load

multiply_strings = load("strings.38_multiply_strings").multiply_strings


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("11", "23", "253"),
        ("0033", "2", "66"),  # leading zeros
        ("-123", "456", "-56088"),
        ("-5", "-4", "20"),
        ("-1", "1", "-1"),
        ("0", "-12", "0"),  # never "-0"
        ("-0", "5", "0"),
        ("123456789", "987654321", "121932631112635269"),
    ],
)
def test_multiply_strings(a, b, expected):
    assert multiply_strings(a, b) == expected
