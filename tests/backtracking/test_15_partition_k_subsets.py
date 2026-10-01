import pytest
from helpers import load

can_partition_k_subsets = load(
    "backtracking.15_partition_k_subsets"
).can_partition_k_subsets


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([2, 1, 4, 5, 6], 3, True),
        ([2, 1, 5, 5, 6], 3, False),
        ([4, 3, 2, 3, 5, 2, 1], 4, True),
        ([2, 2, 2, 2, 3, 4, 5], 4, False),  # sum divisible by k but no valid split
        ([1, 2, 3, 4], 3, False),  # sum not divisible by k
        ([3, 3, 3, 3, 6], 3, True),
        ([1, 1, 1, 1], 4, True),  # one element per group
        ([1, 2], 3, False),  # more groups than elements
    ],
)
def test_can_partition_k_subsets(arr, k, expected):
    assert can_partition_k_subsets(arr, k) is expected


def test_can_partition_k_subsets_single_group():
    assert can_partition_k_subsets([7], 1) is True
