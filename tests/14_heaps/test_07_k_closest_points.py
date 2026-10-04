import pytest
from helpers import load

k_closest_points = load("14_heaps.07_k_closest_points").k_closest_points


@pytest.mark.parametrize(
    "points, k, expected",
    [
        ([(1, 3), (-2, 2)], 1, [(-2, 2)]),
        ([(3, 3), (5, -1), (-2, 4)], 2, [(3, 3), (-2, 4)]),
        ([(5, 5), (0, 0), (-1, 0)], 2, [(0, 0), (-1, 0)]),
        ([(1, 1), (1, 1), (4, 4)], 2, [(1, 1), (1, 1)]),  # duplicate points
        ([(1, 1), (2, 2), (3, 3)], 3, [(1, 1), (2, 2), (3, 3)]),
        ([(0, 1)], 1, [(0, 1)]),
    ],
)
def test_k_closest_points(points, k, expected):
    result = [tuple(p) for p in k_closest_points(points, k)]
    assert sorted(result) == sorted(expected)
