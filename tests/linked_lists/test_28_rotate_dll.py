import pytest
from helpers import load
from helpers.linked_lists import build_dlist, to_dlist

rotate_dll = load("linked_lists.28_rotate_dll").rotate_dll


@pytest.mark.parametrize(
    "values, n, expected",
    [
        (["a", "b", "c", "d", "e"], 2, ["c", "d", "e", "a", "b"]),
        ([1, 2, 3, 4, 5, 6], 4, [5, 6, 1, 2, 3, 4]),
        ([1, 2, 3, 4], 0, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),  # full turn
        ([1, 2, 3], 7, [2, 3, 1]),  # 7 % 3 == 1
        ([1, 2], 1, [2, 1]),
        ([1], 5, [1]),
        ([], 3, []),
    ],
)
def test_rotate_dll(values, n, expected):
    assert to_dlist(rotate_dll(build_dlist(values), n)) == expected


def test_rotate_dll_relinks_nodes():
    head = build_dlist([1, 2, 3])
    second = head.next
    assert rotate_dll(head, 1) is second
    assert head.next is None
    assert head.prev.value == 3
