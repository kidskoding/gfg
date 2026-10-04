import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

reverse = load("12_linked_lists.02_reverse_linked_list").reverse


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3, 4],
        [2, 7, 10, 9, 8],
        [1, 2],
        [5, 5, 3],
        [-1, 0, 1],
        [1],
        [],
    ],
)
def test_reverse(values):
    assert to_list(reverse(build_list(values))) == values[::-1]


def test_reverse_relinks_nodes():
    head = build_list([1, 2, 3])
    original = nodes(head)
    new_head = reverse(head)
    assert nodes(new_head) == original[::-1]
    assert head.next is None
