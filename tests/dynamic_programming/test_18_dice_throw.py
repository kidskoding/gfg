import pytest
from helpers import load

dice_throw_ways = load("dynamic_programming.18_dice_throw").dice_throw_ways


@pytest.mark.parametrize(
    "faces, dice, target, expected",
    [
        (6, 3, 12, 25),
        (2, 3, 6, 1),
        (4, 2, 1, 0),
        (6, 3, 8, 21),
        (4, 3, 5, 6),
        (6, 2, 7, 6),
        (6, 1, 6, 1),
        (6, 2, 13, 0),
    ],
)
def test_dice_throw_ways(faces, dice, target, expected):
    assert dice_throw_ways(faces, dice, target) == expected
