import pytest
from helpers import load

russian_peasant = load("bit_manipulation.15_russian_peasant").russian_peasant


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (18, 1, 18),
        (20, 12, 240),
        (123, 456, 56088),
        (2**20, 3, 3145728),
        (1, 1, 1),
        (0, 5, 0),
        (7, 0, 0),
    ],
)
def test_russian_peasant(a, b, expected):
    assert russian_peasant(a, b) == expected
