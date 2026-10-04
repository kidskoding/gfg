import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

merge_k_lists = load("09_sorting.35_merge_k_sorted_lists").merge_k_lists


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]], list(range(12))),
        ([[1, 3], [8], [4, 5, 6]], [1, 3, 4, 5, 6, 8]),
        ([[-5, 0], [-10, 10]], [-10, -5, 0, 10]),
        ([[2, 2], [2]], [2, 2, 2]),
        ([[], [1]], [1]),
        ([[], []], []),
        ([], []),
    ],
)
def test_merge_k_lists(lists, expected):
    heads = [build_list(values) for values in lists]
    original = {id(node) for head in heads for node in nodes(head)}
    head = merge_k_lists(heads)
    assert to_list(head) == expected
    assert set(map(id, nodes(head))) == original  # relinked, not rebuilt
