import pytest
from helpers import load

has_path = load("16_graphs.21_path_exists").has_path


@pytest.mark.parametrize(
    "n, edges, src, dest, expected",
    [
        (4, [(0, 1), (1, 2)], 0, 2, True),
        (4, [(0, 1), (2, 3)], 0, 3, False),
        (5, [(0, 1), (1, 2), (3, 4), (4, 2)], 0, 3, True),
        (3, [(2, 1), (1, 0)], 0, 2, True),  # undirected
        (3, [], 0, 2, False),
        (1, [], 0, 0, True),
    ],
)
def test_has_path(n, edges, src, dest, expected):
    assert has_path(n, edges, src, dest) is expected
