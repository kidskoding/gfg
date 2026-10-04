import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes

intersection = load("12_linked_lists.17_intersection_point").intersection


def _y_lists(prefix1, prefix2, common):
    """Two lists that share the `common` tail. Returns (head1, head2, first shared node)."""
    shared = build_list(common)
    heads = []
    for prefix in (prefix1, prefix2):
        head = build_list(prefix)
        if head is None:
            head = shared
        else:
            nodes(head)[-1].next = shared
        heads.append(head)
    return heads[0], heads[1], shared


@pytest.mark.parametrize(
    "prefix1, prefix2, common",
    [
        (
            [10, 15],
            [3, 6, 9],
            [15, 30],
        ),  # equal values before the merge are not the answer
        ([4, 1], [5, 6, 1], [8, 4, 5]),
        ([1, 2, 3, 4], [9], [7]),
        ([], [1, 2], [3, 4]),  # list 1 starts at the intersection
        ([1, 2], [], [3]),
        ([], [], [5, 6]),  # same list
    ],
)
def test_intersection(prefix1, prefix2, common):
    head1, head2, shared = _y_lists(prefix1, prefix2, common)
    assert intersection(head1, head2) is shared
    assert intersection(head2, head1) is shared


@pytest.mark.parametrize(
    "a, b",
    [
        ([1, 2, 3], [1, 2, 3]),  # equal values, distinct nodes
        ([1], [2, 3]),
        ([], [1]),
        ([], []),
    ],
)
def test_intersection_none(a, b):
    assert intersection(build_list(a), build_list(b)) is None
