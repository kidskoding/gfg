import pytest
from helpers import load

floyd_warshall = load("graphs.15_floyd_warshall").floyd_warshall


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (
            5,
            [
                (0, 1, 4),
                (0, 3, 5),
                (1, 2, 1),
                (1, 4, 6),
                (2, 0, 2),
                (2, 3, 3),
                (3, 2, 1),
                (3, 4, 2),
                (4, 0, 1),
                (4, 3, 4),
            ],
            [
                [0, 4, 5, 5, 7],
                [3, 0, 1, 4, 6],
                [2, 6, 0, 3, 5],
                [3, 7, 1, 0, 2],
                [1, 5, 5, 4, 0],
            ],
        ),
        (
            4,
            [(0, 1, 3), (1, 2, 1), (0, 2, 7), (2, 3, 2), (3, 0, 4)],
            [[0, 3, 4, 6], [7, 0, 1, 3], [6, 9, 0, 2], [4, 7, 8, 0]],
        ),
        (
            3,
            [(0, 1, 4), (1, 2, -2), (0, 2, 3)],
            [[0, 4, 2], [None, 0, -2], [None, None, 0]],
        ),
        (2, [(0, 1, 5)], [[0, 5], [None, 0]]),
        (3, [], [[0, None, None], [None, 0, None], [None, None, 0]]),
        (1, [], [[0]]),
    ],
)
def test_floyd_warshall(n, edges, expected):
    assert floyd_warshall(n, edges) == expected
