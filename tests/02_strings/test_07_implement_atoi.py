import pytest
from helpers import load

my_atoi = load("02_strings.07_implement_atoi").my_atoi


@pytest.mark.parametrize(
    "s, expected",
    [
        ("42", 42),
        ("   -42", -42),
        ("+1", 1),
        ("4193 with words", 4193),
        ("00012a3", 12),
        ("words and 987", 0),
        ("  +-12", 0),
        ("-0", 0),
        ("", 0),
        ("2147483648", 2147483647),  # clamp high
        ("91283472332", 2147483647),
        ("-91283472332", -2147483648),  # clamp low
    ],
)
def test_my_atoi(s, expected):
    assert my_atoi(s) == expected
