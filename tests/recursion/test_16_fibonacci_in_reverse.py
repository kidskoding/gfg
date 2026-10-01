import pytest
from helpers import load

fibonacci_reverse = load("recursion.16_fibonacci_in_reverse").fibonacci_reverse


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [3, 2, 1, 1, 0]),
        (8, [13, 8, 5, 3, 2, 1, 1, 0]),
        (10, [34, 21, 13, 8, 5, 3, 2, 1, 1, 0]),
        (1, [0]),
        (2, [1, 0]),
        (0, []),
    ],
)
def test_fibonacci_reverse(n, expected):
    assert fibonacci_reverse(n) == expected
