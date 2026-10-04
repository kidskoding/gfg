import pytest
from helpers import load

boruvka_mst = load("17_greedy.17_boruvkas_algorithm").boruvka_mst


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 19),
        (
            5,
            [
                (0, 1, 2),
                (0, 3, 6),
                (1, 2, 3),
                (1, 3, 8),
                (1, 4, 5),
                (2, 4, 7),
                (3, 4, 9),
            ],
            16,
        ),
        (
            6,
            [
                (0, 1, 4),
                (0, 2, 4),
                (1, 2, 2),
                (2, 3, 3),
                (2, 5, 2),
                (2, 4, 4),
                (3, 4, 3),
                (5, 4, 3),
            ],
            14,
        ),
        (
            4,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 1)],
            3,
        ),  # ties must not form cycles
        (3, [(0, 1, -2), (1, 2, -3), (0, 2, 4)], -5),
        (2, [(0, 1, 7), (0, 1, 3)], 3),
        (1, [], 0),
    ],
)
def test_boruvka_mst(n, edges, expected):
    assert boruvka_mst(n, edges) == expected
