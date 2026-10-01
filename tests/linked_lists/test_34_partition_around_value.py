import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes, to_list

partition = load("linked_lists.34_partition_around_value").partition


@pytest.mark.parametrize(
    "values, x, expected",
    [
        ([1, 4, 3, 2, 5, 2, 3], 3, [1, 2, 2, 3, 3, 4, 5]),
        ([1, 4, 2, 10], 3, [1, 2, 4, 10]),
        ([10, 4, 20, 10, 3], 3, [3, 10, 4, 20, 10]),  # order kept within each part
        ([5, 3, 1, 3, 7], 3, [1, 3, 3, 5, 7]),
        ([5, 1, 5, 2], 0, [5, 1, 5, 2]),  # everything greater
        ([5, 1, 5, 2], 9, [5, 1, 5, 2]),  # everything smaller
        ([3, 3, 3], 3, [3, 3, 3]),
        ([1], 1, [1]),
        ([], 5, []),
    ],
)
def test_partition(values, x, expected):
    assert to_list(partition(build_list(values), x)) == expected


def test_partition_is_stable_on_nodes():
    head = build_list([4, 3, 1, 3, 4, 1])
    n = nodes(head)
    assert nodes(partition(head, 3)) == [n[2], n[5], n[1], n[3], n[0], n[4]]
