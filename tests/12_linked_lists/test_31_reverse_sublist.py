import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

reverse_between = load("12_linked_lists.31_reverse_sublist").reverse_between


@pytest.mark.parametrize(
    "values, m, n, expected",
    [
        ([10, 20, 30, 40, 50, 60, 70], 3, 6, [10, 20, 60, 50, 40, 30, 70]),
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),  # whole list
        ([1, 2, 3, 4, 5], 1, 2, [2, 1, 3, 4, 5]),  # head changes
        ([1, 2, 3, 4, 5], 4, 5, [1, 2, 3, 5, 4]),  # tail part
        ([1, 2, 3], 2, 2, [1, 2, 3]),  # m == n
        ([5], 1, 1, [5]),
    ],
)
def test_reverse_between(values, m, n, expected):
    assert to_list(reverse_between(build_list(values), m, n)) == expected


def test_reverse_between_relinks_nodes():
    head = build_list([1, 2, 3, 4])
    a, b, c, d = nodes(head)
    assert nodes(reverse_between(head, 2, 3)) == [a, c, b, d]
