import pytest
from helpers import load
from helpers.linked_lists import build_dlist, nodes, to_dlist

merge_sort_dll = load("09_sorting.25_merge_sort_dll").merge_sort_dll


@pytest.mark.parametrize(
    "values",
    [
        [8, 2, 3, 1, 7],
        [5, 4, 3, 2, 1],
        [1, 2, 3],
        [2, 2, 1, 1],
        [-3, 10, 0, -3],
        [1],
        [],
    ],
)
def test_merge_sort_dll(values):
    head = build_dlist(values)
    original = set(map(id, nodes(head)))
    head = merge_sort_dll(head)
    assert to_dlist(head) == sorted(values)  # also checks every prev pointer
    assert set(map(id, nodes(head))) == original  # relinked, not rebuilt


def test_merge_sort_dll_is_stable():
    head = build_dlist([2, 1, 2, 1])
    n0, n1, n2, n3 = nodes(head)
    assert nodes(merge_sort_dll(head)) == [n1, n3, n0, n2]
