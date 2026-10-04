import pytest
from helpers import load

min_dice_throws = load("07_queues.17_snake_and_ladder").min_dice_throws


@pytest.mark.parametrize(
    "n, jumps, expected",
    [
        (30, {3: 22, 5: 8, 11: 26, 20: 29, 27: 1, 21: 9, 17: 4, 19: 7}, 3),
        (7, {}, 1),
        (8, {}, 2),
        (20, {}, 4),
        (20, {7: 2, 13: 3}, 4),  # snakes are avoidable
        (100, {2: 100}, 1),
        (
            10,
            {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1},
            -1,
        ),  # every roll from 1 is a snake back to 1
        (1, {}, 0),
    ],
)
def test_min_dice_throws(n, jumps, expected):
    assert min_dice_throws(n, jumps) == expected
