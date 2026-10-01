import pytest
from helpers import load

mod_power_of_two = load("bit_manipulation.05_mod_power_of_two").mod_power_of_two


@pytest.mark.parametrize(
    "n, d, expected",
    [
        (6, 4, 2),
        (12, 8, 4),
        (7, 8, 7),
        (64, 64, 0),
        (1023, 512, 511),
        (5, 1, 0),
        (0, 16, 0),
    ],
)
def test_mod_power_of_two(n, d, expected):
    assert mod_power_of_two(n, d) == expected
