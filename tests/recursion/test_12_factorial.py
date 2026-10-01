import pytest
from helpers import load

factorial = load("recursion.12_factorial").factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 120),
        (4, 24),
        (0, 1),
        (1, 1),
        (2, 2),
        (10, 3628800),
        (20, 2432902008176640000),
    ],
)
def test_factorial(n, expected):
    assert factorial(n) == expected
