import pytest
from helpers import load
from helpers.linked_lists import build_dlist, to_dlist

reverse_dll = load("linked_lists.03_reverse_doubly_linked_list").reverse_dll


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3, 4],
        [75, 122, 59, 196],
        [1, 2],
        [3, 3, 1],
        [-5, 0, 5, 10, 15],
        [1],
        [],
    ],
)
def test_reverse_dll(values):
    assert to_dlist(reverse_dll(build_dlist(values))) == values[::-1]


def test_reverse_dll_relinks_nodes():
    head = build_dlist([1, 2, 3])
    tail = head.next.next
    assert reverse_dll(head) is tail
    assert head.next is None
    assert head.prev.value == 2
