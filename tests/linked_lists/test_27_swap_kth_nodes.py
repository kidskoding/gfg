import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

swap_kth = load("linked_lists.27_swap_kth_nodes").swap_kth


@pytest.mark.parametrize(
    "values, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 1, [5, 2, 3, 4, 1]),  # head and tail
        ([1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5]),  # middle swaps with itself
        ([1, 2, 3, 4], 2, [1, 3, 2, 4]),  # adjacent nodes
        ([1, 2, 3, 4], 4, [4, 2, 3, 1]),  # k == length
        ([1, 2, 3, 4], 5, [1, 2, 3, 4]),  # k > length: unchanged
        ([1, 2], 1, [2, 1]),
        ([1], 1, [1]),
    ],
)
def test_swap_kth(values, k, expected):
    assert to_list(swap_kth(build_list(values), k)) == expected


@pytest.mark.parametrize(
    "k, order",
    [
        (1, [4, 1, 2, 3, 0]),
        (2, [0, 3, 2, 1, 4]),
        (5, [4, 1, 2, 3, 0]),
    ],
)
def test_swap_kth_relinks_nodes(k, order):
    head = build_list([1, 2, 3, 4, 5])
    original = nodes(head)
    assert nodes(swap_kth(head, k)) == [original[i] for i in order]
