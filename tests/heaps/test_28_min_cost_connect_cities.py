import pytest
from helpers import load

min_cost_connect_cities = load(
    "heaps.28_min_cost_connect_cities"
).min_cost_connect_cities


@pytest.mark.parametrize(
    "cost, expected",
    [
        (
            [
                [0, 1, 2, 3, 4],
                [1, 0, 5, 0, 7],
                [2, 5, 0, 6, 0],
                [3, 0, 6, 0, 0],
                [4, 7, 0, 0, 0],
            ],
            10,
        ),
        (
            [
                [0, 1, 1, 100, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [100, 0, 0, 0, 2, 2],
                [0, 0, 0, 2, 0, 2],
                [0, 0, 0, 2, 2, 0],
            ],
            106,
        ),
        ([[0, 3], [3, 0]], 3),
        ([[0, 0], [0, 0]], -1),  # no road at all
        ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], -1),  # city 2 isolated
        ([[0]], 0),
        ([], 0),
    ],
)
def test_min_cost_connect_cities(cost, expected):
    assert min_cost_connect_cities(cost) == expected
