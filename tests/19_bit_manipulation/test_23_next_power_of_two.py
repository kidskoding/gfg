import pytest
from helpers import load

next_power_of_two = load("19_bit_manipulation.23_next_power_of_two").next_power_of_two


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 8),
        (17, 32),
        (32, 32),
        (1000, 1024),
        (2**40 + 1, 2**41),
        (1, 1),
        (0, 1),
    ],
)
def test_next_power_of_two(n, expected):
    assert next_power_of_two(n) == expected
