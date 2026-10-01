import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

sort_012 = load("linked_lists.20_sort_0s_1s_2s").sort_012


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 2, 1, 2, 0, 2, 2],
        [2, 2, 0, 1],
        [2, 1, 0],
        [0, 0, 0],
        [2, 2],
        [1],
        [],
    ],
)
def test_sort_012(values):
    assert to_list(sort_012(build_list(values))) == sorted(values)
