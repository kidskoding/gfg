import pytest
from helpers import load

count_paths = load("16_graphs.22_possible_paths").count_paths


@pytest.mark.parametrize(
    "n, edges, src, dest, expected",
    [
        (5, [(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 4), (3, 2)], 0, 4, 4),
        (4, [(0, 1), (0, 2), (1, 3), (2, 3)], 0, 3, 2),
        (3, [(0, 1), (1, 2)], 0, 2, 1),
        (4, [(0, 1), (1, 2), (2, 1), (2, 3), (1, 3)], 0, 3, 2),  # cycle not re-entered
        (3, [(0, 1), (1, 0), (1, 2)], 0, 2, 1),
        (3, [(1, 0), (2, 1)], 0, 2, 0),  # edges are directed
        (1, [], 0, 0, 1),
    ],
)
def test_count_paths(n, edges, src, dest, expected):
    assert count_paths(n, edges, src, dest) == expected
