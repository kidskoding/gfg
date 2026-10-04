import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

skip_m_delete_n = load("12_linked_lists.32_delete_n_after_m").skip_m_delete_n


@pytest.mark.parametrize(
    "values, m, n, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8], 2, 2, [1, 2, 5, 6]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 2, [1, 2, 3, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 1, [1, 3, 5, 7, 9]),
        ([1, 2, 3, 4, 5], 2, 3, [1, 2]),
        ([1, 2, 3, 4, 5, 6, 7], 2, 4, [1, 2, 7]),  # partial delete run then keep
        ([1, 2, 3], 5, 2, [1, 2, 3]),  # m >= length: unchanged
        ([1, 2], 1, 5, [1]),
        ([], 1, 1, []),
    ],
)
def test_skip_m_delete_n(values, m, n, expected):
    assert to_list(skip_m_delete_n(build_list(values), m, n)) == expected
