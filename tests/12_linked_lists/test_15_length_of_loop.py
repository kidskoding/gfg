import pytest
from helpers import load
from helpers.linked_lists import build_cycle

loop_length = load("12_linked_lists.15_length_of_loop").loop_length


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([25, 14, 19, 33, 10], 2, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6, 5),
        ([1, 2, 3, 4], 0, 4),
        ([1, 2, 3, 4], 3, 1),  # self loop
        ([1, 2, 3], -1, 0),
        ([1], 0, 1),
        ([], -1, 0),
    ],
)
def test_loop_length(values, pos, expected):
    head, _ = build_cycle(values, pos)
    assert loop_length(head) == expected
