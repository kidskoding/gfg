import pytest
from helpers import load

max_triplet_product = load("01_arrays.06_max_triplet_product").max_triplet_product


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 3, 5, 6, 20], 1200),
        ([-10, -3, -5, -6, -20], -90),
        ([1, -4, 3, -6, 7, 0], 168),
        ([1, 2, 3], 6),
        ([-1, -2, 0], 0),
        ([-5, -4, 1, 2, 3], 60),
        ([4, 4, 4, 4], 64),
    ],
)
def test_max_triplet_product(arr, expected):
    assert max_triplet_product(arr) == expected
