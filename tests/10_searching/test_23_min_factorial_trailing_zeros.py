import pytest
from helpers import load

min_factorial_zeros = load(
    "10_searching.23_min_factorial_trailing_zeros"
).min_factorial_zeros


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 5),
        (2, 10),
        (6, 25),
        (5, 25),  # no factorial has exactly 5 zeros (24! has 4, 25! has 6)
        (7, 30),
        (24, 100),
        (100, 405),
        (0, 0),
    ],
)
def test_min_factorial_zeros(n, expected):
    assert min_factorial_zeros(n) == expected
