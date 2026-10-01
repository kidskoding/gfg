import pytest
from helpers import load

kth_smallest_in_matrix = load("heaps.12_kth_smallest_in_matrix").kth_smallest_in_matrix

M = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
N = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]


@pytest.mark.parametrize(
    "matrix, k, expected",
    [
        (M, 3, 20),
        (M, 7, 30),
        (M, 16, 50),
        (N, 8, 13),
        (N, 9, 15),
        ([[1, 2], [1, 3]], 2, 1),  # duplicates
        ([[5]], 1, 5),
    ],
)
def test_kth_smallest_in_matrix(matrix, k, expected):
    assert kth_smallest_in_matrix(matrix, k) == expected
