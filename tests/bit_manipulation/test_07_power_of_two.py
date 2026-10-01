import pytest
from helpers import load

is_power_of_two = load("bit_manipulation.07_power_of_two").is_power_of_two


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (2, True),
        (16, True),
        (2**40, True),
        (3, False),
        (98, False),
        (2**40 + 1, False),
        (0, False),
        (-8, False),
    ],
)
def test_is_power_of_two(n, expected):
    assert is_power_of_two(n) is expected
