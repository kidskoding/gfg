import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

reorder = load("linked_lists.33_rearrange_in_place").reorder


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2], [1, 2]),
        ([7, 7, 8], [7, 8, 7]),
        ([1], [1]),
    ],
)
def test_reorder(values, expected):
    head = build_list(values)
    reorder(head)
    assert to_list(head) == expected


def test_reorder_relinks_nodes():
    head = build_list([1, 2, 3, 4])
    a, b, c, d = nodes(head)
    reorder(head)
    assert nodes(head) == [a, d, b, c]


def test_reorder_empty():
    reorder(None)
