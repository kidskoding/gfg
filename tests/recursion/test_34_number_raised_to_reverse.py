import pytest
from helpers import load

power_of_reverse = load("recursion.34_number_raised_to_reverse").power_of_reverse


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 4),
        (3, 27),
        (57, 262042770),
        (12, 864354781),
        (21, 459895852),
        (10, 10),  # reverse of 10 is 01 == 1
        (123, 329844637),
        (1, 1),
    ],
)
def test_power_of_reverse(n, expected):
    assert power_of_reverse(n) == expected


def test_power_of_reverse_needs_fast_exponentiation():
    # exponent 4321: one-multiply-per-level recursion would blow the recursion limit
    assert power_of_reverse(1234) == pow(1234, 4321, 1_000_000_007)
