import pytest
from helpers import load

egg_drop = load("dynamic_programming.20_egg_dropping").egg_drop


@pytest.mark.parametrize(
    "eggs, floors, expected",
    [
        (1, 2, 2),
        (2, 10, 4),
        (2, 36, 8),
        (2, 100, 14),
        (3, 14, 4),
        (2, 1, 1),
        (5, 0, 0),
        (1, 7, 7),
    ],
)
def test_egg_drop(eggs, floors, expected):
    assert egg_drop(eggs, floors) == expected
