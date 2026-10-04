import pytest
from helpers import load

smallest_non_representable = load(
    "09_sorting.33_smallest_non_representable"
).smallest_non_representable


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 7),
        ([1, 1, 1, 1], 5),
        ([1, 2, 6, 10, 11, 15], 4),
        ([1, 1, 3, 4], 10),
        ([1, 2, 5, 10, 20, 40], 4),
        ([4, 1, 2], 8),  # unsorted input
        ([2, 3], 1),
        ([], 1),
    ],
)
def test_smallest_non_representable(arr, expected):
    assert smallest_non_representable(arr) == expected
