import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

delete_middle = load("12_linked_lists.07_delete_middle").delete_middle


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5], [1, 2, 4, 5]),
        ([2, 4, 6, 7, 5, 1], [2, 4, 6, 5, 1]),  # even: second middle
        ([1, 2, 3, 4], [1, 2, 4]),
        ([1, 2], [1]),
        ([1, 2, 3], [1, 3]),
        ([1], []),
        ([], []),
    ],
)
def test_delete_middle(values, expected):
    assert to_list(delete_middle(build_list(values))) == expected
