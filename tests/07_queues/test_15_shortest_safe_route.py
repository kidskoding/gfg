import copy

import pytest
from helpers import load

shortest_safe_route = load("07_queues.15_shortest_safe_route").shortest_safe_route


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0],
            ],
            6,
        ),
        ([[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]], -1),
        (
            [
                [1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1],
            ],
            6,
        ),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
        ([[1, 1], [1, 0]], -1),  # every last-column cell touches the mine
        ([[1], [1]], 1),
        ([[1], [0], [1]], -1),
        ([[0]], -1),
        ([], -1),
    ],
)
def test_shortest_safe_route(grid, expected):
    original = copy.deepcopy(grid)
    assert shortest_safe_route(grid) == expected
    assert grid == original


def test_shortest_safe_route_detour():
    # Mine (0, 2) blocks rows 0-1 at column 2; mine (3, 4) blocks rows 2-3 at column 4.
    # The route must run low past column 2, then climb at column 3 to pass column 4 high.
    grid = [
        [1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1],
    ]
    assert shortest_safe_route(grid) == 8
