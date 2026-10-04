import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

delete_all_occurrences = load(
    "12_linked_lists.22_delete_all_occurrences"
).delete_all_occurrences


@pytest.mark.parametrize(
    "values, key, expected",
    [
        ([2, 2, 1, 8, 2, 3, 2, 7], 2, [1, 8, 3, 7]),
        ([1, 2, 3, 4], 5, [1, 2, 3, 4]),
        ([1, 1, 2, 1], 1, [2]),  # head run and tail
        ([3, 3, 3], 3, []),
        ([1, 2, 2, 2, 3], 2, [1, 3]),
        ([4], 4, []),
        ([], 1, []),
    ],
)
def test_delete_all_occurrences(values, key, expected):
    assert to_list(delete_all_occurrences(build_list(values), key)) == expected
