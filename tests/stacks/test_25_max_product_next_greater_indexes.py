import pytest
from helpers import load

max_index_product = load("stacks.25_max_product_next_greater_indexes").max_index_product


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 4, 3, 4, 5], 8),
        ([1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 24),
        ([3, 1, 2], 3),
        ([1, 2, 3], 0),
        ([2, 2, 2], 0),
        ([1], 0),
        ([], 0),
    ],
)
def test_max_index_product(arr, expected):
    assert max_index_product(arr) == expected
