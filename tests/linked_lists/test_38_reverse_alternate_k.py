import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

reverse_alternate_k = load("linked_lists.38_reverse_alternate_k").reverse_alternate_k


@pytest.mark.parametrize(
    "values, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [3, 2, 1, 4, 5, 6, 9, 8, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [3, 2, 1, 4, 5, 6, 9, 8, 7, 10]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 2, [2, 1, 3, 4, 6, 5, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, [3, 2, 1, 4, 5, 6, 8, 7]),  # short reverse group
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),  # short keep group
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2], 3, [2, 1]),
        ([], 2, []),
    ],
)
def test_reverse_alternate_k(values, k, expected):
    assert to_list(reverse_alternate_k(build_list(values), k)) == expected
