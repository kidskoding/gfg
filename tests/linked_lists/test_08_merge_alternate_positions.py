import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

merge_alternate = load("linked_lists.08_merge_alternate_positions").merge_alternate


@pytest.mark.parametrize(
    "first, second, merged, rest",
    [
        (
            [5, 7, 17, 13, 11],
            [12, 10, 2, 4, 6],
            [5, 12, 7, 10, 17, 2, 13, 4, 11, 6],
            [],
        ),
        ([1, 2, 3], [4, 5, 6, 7, 8], [1, 4, 2, 5, 3, 6], [7, 8]),
        ([1, 2, 3, 4], [9], [1, 9, 2, 3, 4], []),
        ([1], [2, 3], [1, 2], [3]),
        ([1, 2], [], [1, 2], []),
        ([], [1, 2], [], [1, 2]),
    ],
)
def test_merge_alternate(first, second, merged, rest):
    head1, head2 = merge_alternate(build_list(first), build_list(second))
    assert to_list(head1) == merged
    assert to_list(head2) == rest


def test_merge_alternate_reuses_nodes():
    a, b = build_list([1, 2]), build_list([3, 4, 5])
    a_nodes, b_nodes = nodes(a), nodes(b)
    head1, head2 = merge_alternate(a, b)
    assert nodes(head1) == [a_nodes[0], b_nodes[0], a_nodes[1], b_nodes[1]]
    assert head2 is b_nodes[2]
