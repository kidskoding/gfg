import pytest
from helpers import load

min_dice_throws = load("16_graphs.06_snake_and_ladder").min_dice_throws


GFG_BOARD = {3: 22, 5: 8, 11: 26, 20: 29, 27: 1, 21: 9, 17: 4, 19: 7}


@pytest.mark.parametrize(
    "n, moves, expected",
    [
        (30, GFG_BOARD, 3),
        (6, {}, 1),
        (7, {}, 1),
        (8, {}, 2),
        (12, {}, 2),
        (10, {2: 10}, 1),  # ladder straight to the end
        (13, {7: 2}, 3),  # snake blocks the only 2-throw route
        (10, {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}, -1),  # every throw is a snake
        (1, {}, 0),
    ],
)
def test_min_dice_throws(n, moves, expected):
    assert min_dice_throws(n, moves) == expected
