import pytest
from helpers import load

add_strings = load("02_strings.36_sum_large_numbers").add_strings


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("25", "23", "48"),
        ("2500", "23", "2523"),
        ("11", "9", "20"),
        ("999", "1", "1000"),
        ("0001", "009", "10"),  # strip leading zeros
        ("0", "0", "0"),
        (
            "123456789012345678901234567890",
            "987654321098765432109876543210",
            "1111111110111111111011111111100",
        ),
    ],
)
def test_add_strings(a, b, expected):
    assert add_strings(a, b) == expected
