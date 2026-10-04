import pytest
from helpers import load
from helpers.linked_lists import build_circular

circular_values = load("12_linked_lists.09_circular_list_traversal").circular_values


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3, 4],
        [11, 2, 56, 12],
        [5, 5, 5],  # duplicate values must not stop the walk early
        [1, 2],
        [7],
        [],
    ],
)
def test_circular_values(values):
    assert circular_values(build_circular(values)) == values


def test_circular_values_starts_at_given_node():
    head = build_circular([1, 2, 3, 4])
    assert circular_values(head.next.next) == [3, 4, 1, 2]
