import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

reverse_in_groups = load("12_linked_lists.16_reverse_in_groups").reverse_in_groups


@pytest.mark.parametrize(
    "values, k, expected",
    [
        ([1, 2, 2, 4, 5, 6, 7, 8], 4, [4, 2, 2, 1, 8, 7, 6, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 5, 4]),  # short last group is reversed too
        ([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3], 3, [3, 2, 1]),
        ([1, 2, 3], 5, [3, 2, 1]),  # k > length
        ([1], 2, [1]),
        ([], 3, []),
    ],
)
def test_reverse_in_groups(values, k, expected):
    assert to_list(reverse_in_groups(build_list(values), k)) == expected


def test_reverse_in_groups_relinks_nodes():
    head = build_list([1, 2, 3, 4])
    a, b, c, d = nodes(head)
    assert nodes(reverse_in_groups(head, 2)) == [b, a, d, c]
