import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

delete_last_occurrence = load(
    "12_linked_lists.06_delete_last_occurrence"
).delete_last_occurrence


@pytest.mark.parametrize(
    "values, key, expected",
    [
        ([1, 2, 3, 5, 2, 10], 2, [1, 2, 3, 5, 10]),
        ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5]),  # only occurrence is the head
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4]),  # tail
        ([1, 2, 3], 9, [1, 2, 3]),  # absent: unchanged
        ([7, 7, 7], 7, [7, 7]),
        ([4], 4, []),
        ([], 1, []),
    ],
)
def test_delete_last_occurrence(values, key, expected):
    assert to_list(delete_last_occurrence(build_list(values), key)) == expected
