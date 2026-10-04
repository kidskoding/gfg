import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

merge_k_lists = load("14_heaps.24_merge_k_sorted_lists").merge_k_lists


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([[1, 2, 2], [1, 1, 2]], [1, 1, 1, 2, 2, 2]),
        ([[1], [0]], [0, 1]),
        ([[], [-1, 5], []], [-1, 5]),
        ([[7, 8, 9]], [7, 8, 9]),
        ([[]], []),
        ([], []),
    ],
)
def test_merge_k_lists(lists, expected):
    assert to_list(merge_k_lists([build_list(x) for x in lists])) == expected
