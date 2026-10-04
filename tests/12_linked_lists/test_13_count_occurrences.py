import pytest
from helpers import load
from helpers.linked_lists import build_list

count_occurrences = load("12_linked_lists.13_count_occurrences").count_occurrences


@pytest.mark.parametrize(
    "values, key, expected",
    [
        ([1, 2, 1, 2, 1, 3, 1], 1, 4),
        ([1, 2, 1, 2, 1], 3, 0),
        ([5, 5, 5, 5], 5, 4),
        ([-1, 2, -1], -1, 2),
        ([7], 7, 1),
        ([], 1, 0),
    ],
)
def test_count_occurrences(values, key, expected):
    assert count_occurrences(build_list(values), key) == expected
