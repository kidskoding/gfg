import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

rotate = load("linked_lists.04_rotate_linked_list").rotate


@pytest.mark.parametrize(
    "values, k, expected",
    [
        ([10, 20, 30, 40, 50, 60], 4, [50, 60, 10, 20, 30, 40]),
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # full turn
        ([1, 2, 3], 7, [2, 3, 1]),  # k > length: 7 % 3 == 1
        ([1, 2], 1, [2, 1]),
        ([9], 3, [9]),
        ([], 2, []),
    ],
)
def test_rotate(values, k, expected):
    assert to_list(rotate(build_list(values), k)) == expected


def test_rotate_relinks_nodes():
    head = build_list([1, 2, 3, 4])
    original = nodes(head)
    assert nodes(rotate(head, 1)) == original[1:] + original[:1]
