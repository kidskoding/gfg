import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

pairwise_swap = load("linked_lists.12_pairwise_swap").pairwise_swap


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
        ([1, 2, 2, 4, 5, 6, 7, 8], [2, 1, 4, 2, 6, 5, 8, 7]),
        ([1, 3, 4, 7, 9, 10, 1], [3, 1, 7, 4, 10, 9, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ],
)
def test_pairwise_swap(values, expected):
    assert to_list(pairwise_swap(build_list(values))) == expected


def test_pairwise_swap_relinks_nodes():
    head = build_list([1, 2, 3])
    a, b, c = nodes(head)
    assert nodes(pairwise_swap(head)) == [b, a, c]
