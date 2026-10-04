import pytest
from helpers import load

find_mother_vertex = load("16_graphs.25_mother_vertex").find_mother_vertex


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (7, [(0, 1), (0, 2), (1, 3), (4, 1), (6, 4), (5, 6), (5, 2), (6, 0)], 5),
        (4, [(1, 0), (1, 2), (2, 3)], 1),
        (3, [(0, 1), (1, 2), (2, 0)], 0),  # every vertex is a mother; smallest wins
        (3, [(1, 2), (2, 1), (1, 0)], 1),  # 1 and 2 both work
        (3, [(0, 1), (2, 1)], -1),
        (2, [], -1),
        (1, [], 0),
    ],
)
def test_find_mother_vertex(n, edges, expected):
    assert find_mother_vertex(n, edges) == expected
