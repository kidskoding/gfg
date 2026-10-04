import pytest
from helpers import load

merge_k_arrays = load("14_heaps.23_merge_k_sorted_arrays").merge_k_arrays


@pytest.mark.parametrize(
    "arrays, expected",
    [
        ([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]], list(range(12))),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[-3, 0], [-5, 10]], [-5, -3, 0, 10]),
        ([[1, 1], [1]], [1, 1, 1]),
        ([[], [1], []], [1]),
        ([[4]], [4]),
        ([], []),
    ],
)
def test_merge_k_arrays(arrays, expected):
    assert merge_k_arrays(arrays) == expected
