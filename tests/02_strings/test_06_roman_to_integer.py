import pytest
from helpers import load

roman_to_int = load("02_strings.06_roman_to_integer").roman_to_int


@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("LVIII", 58),
        ("CDXLIV", 444),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
    ],
)
def test_roman_to_int(s, expected):
    assert roman_to_int(s) == expected
