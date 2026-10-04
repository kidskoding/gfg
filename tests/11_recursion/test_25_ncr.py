import pytest
from helpers import load

ncr = load("11_recursion.25_ncr").ncr


@pytest.mark.parametrize(
    "n, r, expected",
    [
        (5, 2, 10),
        (3, 2, 3),
        (6, 3, 20),
        (10, 0, 1),
        (10, 10, 1),
        (1, 1, 1),
        (20, 10, 184756),
        (2, 5, 0),
        (5, -1, 0),
    ],
)
def test_ncr(n, r, expected):
    assert ncr(n, r) == expected
