import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

merge_k = load("linked_lists.37_merge_k_sorted_lists").merge_k


@pytest.mark.parametrize(
    "lists",
    [
        [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]],
        [[1, 3], [8], [4, 5, 6]],
        [[1, 1], [1], [1, 2]],
        [[-5, 0], [-10, 10], [3]],
        [[], [1], []],
        [[1, 2, 3]],
        [[], []],
        [],
    ],
)
def test_merge_k(lists):
    expected = sorted(v for values in lists for v in values)
    assert to_list(merge_k([build_list(values) for values in lists])) == expected


def test_merge_k_reuses_nodes():
    heads = [build_list([1, 4]), build_list([2, 3])]
    originals = {id(node) for head in heads for node in nodes(head)}
    merged = nodes(merge_k(heads))
    assert {id(node) for node in merged} == originals
