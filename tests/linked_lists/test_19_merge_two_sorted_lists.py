import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

merge_sorted = load("linked_lists.19_merge_two_sorted_lists").merge_sorted


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([5, 10, 15, 40], [2, 3, 20], [2, 3, 5, 10, 15, 20, 40]),
        ([1, 1], [2, 4], [1, 1, 2, 4]),
        ([1, 3, 5], [1, 3, 5], [1, 1, 3, 3, 5, 5]),
        ([-3, 0], [-5, -1, 7], [-5, -3, -1, 0, 7]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [4], [4]),
        ([], [], []),
    ],
)
def test_merge_sorted(a, b, expected):
    assert to_list(merge_sorted(build_list(a), build_list(b))) == expected


def test_merge_sorted_reuses_nodes_and_keeps_ties_stable():
    a, b = build_list([1, 3]), build_list([1, 2])
    a1, a3 = nodes(a)
    b1, b2 = nodes(b)
    assert nodes(merge_sorted(a, b)) == [a1, b1, b2, a3]
