import pytest
from helpers import load

path_more_than_k = load("15_backtracking.14_path_more_than_k").path_more_than_k

GFG_EDGES = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 3, 7),
    (2, 8, 2),
    (2, 5, 4),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (6, 8, 6),
    (7, 8, 7),
]


@pytest.mark.parametrize(
    "n, edges, src, k, expected",
    [
        (9, GFG_EDGES, 0, 58, True),
        (9, GFG_EDGES, 0, 62, False),
        (9, GFG_EDGES, 0, 61, True),  # 0-7-1-2-3-4-5-6-8 weighs exactly 61
        (9, GFG_EDGES, 0, 0, True),
        (
            3,
            [(0, 1, 5), (1, 2, 5)],
            1,
            6,
            False,
        ),  # from the middle a simple path can't double back
        (3, [(0, 1, 5), (1, 2, 5)], 0, 10, True),
        (3, [(1, 2, 10)], 0, 5, False),  # src is isolated
        (1, [], 0, 1, False),
    ],
)
def test_path_more_than_k(n, edges, src, k, expected):
    assert path_more_than_k(n, edges, src, k) is expected
