import pytest
from helpers import load

count_k_distinct = load("01_arrays.45_subarrays_k_distinct").count_k_distinct


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 2, 3], 2, 4),
        ([1, 1, 1, 1], 1, 10),
        ([1, 2, 1, 2, 3], 2, 7),
        ([1, 2, 1, 3, 4], 3, 3),
        ([1, 2, 3], 4, 0),
        ([5], 1, 1),
        ([], 1, 0),
    ],
)
def test_count_k_distinct(arr, k, expected):
    assert count_k_distinct(arr, k) == expected
