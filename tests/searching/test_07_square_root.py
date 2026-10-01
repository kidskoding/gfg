import pytest
from helpers import load

floor_sqrt = load("searching.07_square_root").floor_sqrt


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (11, 3),
        (15, 3),
        (16, 4),
        (99, 9),
        (2147395599, 46339),  # just below 46340 ** 2
        (10**12 + 1, 10**6),
    ],
)
def test_floor_sqrt(n, expected):
    assert floor_sqrt(n) == expected
