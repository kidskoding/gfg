import pytest
from helpers import load

min_cost_via = load("07_queues.18_min_cost_path_via_nodes").min_cost_via


@pytest.mark.parametrize(
    "n, edges, src, dst, via, expected",
    [
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 10)], 0, 3, [], 3),
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 10)], 0, 3, [2], 3),
        (4, [(0, 1, 1), (1, 3, 1), (0, 2, 5), (2, 3, 5), (1, 2, 1)], 0, 3, [2], 7),
        (
            4,
            [(0, 1, 1), (1, 2, 2), (2, 1, 2), (1, 3, 1)],
            0,
            3,
            [2],
            6,
        ),  # must revisit 1
        (
            5,
            [(0, 1, 1), (0, 2, 1), (1, 2, 10), (2, 1, 1), (1, 4, 1), (2, 4, 1)],
            0,
            4,
            [1, 2],
            3,
        ),  # order matters
        (5, [(0, 1, 1), (1, 2, 1)], 0, 2, [4], -1),  # intermediate unreachable
        (2, [], 0, 1, [], -1),
        (1, [], 0, 0, [], 0),
    ],
)
def test_min_cost_via(n, edges, src, dst, via, expected):
    assert min_cost_via(n, edges, src, dst, via) == expected
