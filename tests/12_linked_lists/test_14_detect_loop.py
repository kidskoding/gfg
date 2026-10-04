import pytest
from helpers import load
from helpers.linked_lists import build_cycle

has_loop = load("12_linked_lists.14_detect_loop").has_loop


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([1, 3, 4], 1, True),
        ([1, 8, 3, 4], -1, False),
        ([1, 2, 3, 4], 0, True),  # tail back to head
        ([1, 2, 3, 4], 3, True),  # self loop at tail
        ([5, 5, 5], -1, False),  # repeated values are not a loop
        ([1], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ],
)
def test_has_loop(values, pos, expected):
    head, _ = build_cycle(values, pos)
    assert has_loop(head) is expected
