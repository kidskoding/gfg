import pytest
from helpers import load
from helpers.linked_lists import build_list

nth_from_end = load("linked_lists.05_nth_node_from_end").nth_from_end


@pytest.mark.parametrize(
    "values, n, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8),
        ([10, 5, 100, 5], 5, None),  # n exceeds length
        ([35, 15, 4, 20], 4, 35),  # n == length: the head
        ([35, 15, 4, 20], 1, 20),  # last node
        ([1, 2, 3], 2, 2),
        ([42], 1, 42),
        ([], 1, None),
    ],
)
def test_nth_from_end(values, n, expected):
    assert nth_from_end(build_list(values), n) == expected
