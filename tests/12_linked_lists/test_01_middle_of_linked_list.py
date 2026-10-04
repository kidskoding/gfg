import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes

middle = load("12_linked_lists.01_middle_of_linked_list").middle


@pytest.mark.parametrize(
    "values, index",
    [
        ([1, 2, 3, 4, 5], 2),
        ([2, 4, 6, 7, 5, 1], 3),  # even length: second middle
        ([1, 2], 1),
        ([1, 2, 3], 1),
        ([7, 7, 7, 7], 2),
        ([1], 0),
    ],
)
def test_middle(values, index):
    head = build_list(values)
    assert middle(head) is nodes(head)[index]


def test_middle_empty():
    assert middle(None) is None
