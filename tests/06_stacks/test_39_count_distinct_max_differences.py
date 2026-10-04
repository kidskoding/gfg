import pytest
from helpers import load

count_distinct_max_diffs = load(
    "06_stacks.39_count_distinct_max_differences"
).count_distinct_max_diffs


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 1, 3], 2),
        ([5, 2, 3, 8], 4),
        ([4, 1, 2, 8], 5),
        ([1, 2, 3, 4], 1),
        ([1, 2], 1),
        ([7], 0),
        ([], 0),
    ],
)
def test_count_distinct_max_diffs(arr, expected):
    assert count_distinct_max_diffs(arr) == expected
