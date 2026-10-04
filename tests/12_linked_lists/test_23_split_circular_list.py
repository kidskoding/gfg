import pytest
from helpers import load
from helpers.linked_lists import build_circular, circular_to_list

split_circular = load("12_linked_lists.23_split_circular_list").split_circular


@pytest.mark.parametrize(
    "values, first, second",
    [
        ([1, 2, 3, 4], [1, 2], [3, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3], [4, 5]),  # odd: first half gets the extra node
        ([10, 4, 9], [10, 4], [9]),
        ([2, 6, 1, 5, 7, 8], [2, 6, 1], [5, 7, 8]),
        ([1, 2], [1], [2]),
    ],
)
def test_split_circular(values, first, second):
    head1, head2 = split_circular(build_circular(values))
    assert circular_to_list(head1) == first
    assert circular_to_list(head2) == second


def test_split_circular_single():
    head = build_circular([7])
    head1, head2 = split_circular(head)
    assert head1 is head
    assert head2 is None
    assert head.next is head


def test_split_circular_empty():
    assert split_circular(None) == (None, None)
