import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

delete_node = load("linked_lists.18_delete_without_head").delete_node


@pytest.mark.parametrize(
    "values, index, expected",
    [
        ([1, 2, 3, 4], 1, [1, 3, 4]),
        ([10, 20, 4, 30], 2, [10, 20, 30]),
        ([1, 2, 3], 0, [2, 3]),  # the head itself
        ([1, 2, 3], 1, [1, 3]),  # second to last
        ([5, 5, 5], 0, [5, 5]),
        ([1, 2], 0, [2]),
    ],
)
def test_delete_node(values, index, expected):
    head = build_list(values)
    delete_node(nodes(head)[index])
    assert to_list(head) == expected
