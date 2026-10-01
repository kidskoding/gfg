import pytest
from helpers import load

min_weight_cycle = load("graphs.32_min_weight_cycle").min_weight_cycle


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [(0, 1, 2), (1, 2, 2), (1, 3, 1), (1, 4, 1), (0, 4, 3), (2, 3, 4)], 6),
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 5)], 4),
        (6, [(0, 1, 5), (1, 2, 5), (2, 0, 5), (3, 4, 1), (4, 5, 1), (5, 3, 1)], 3),
        (3, [(0, 1, 1), (1, 2, 1), (2, 0, 1)], 3),
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)], -1),  # tree
        (1, [], -1),
    ],
)
def test_min_weight_cycle(n, edges, expected):
    assert min_weight_cycle(n, edges) == expected
