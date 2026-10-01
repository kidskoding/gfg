import pytest
from helpers import load

has_two_sum_to_third = load("two_pointers.16_sum_two_equals_third").has_two_sum_to_third


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([5, 32, 1, 7, 10, 50, 19, 21, 2], True),
        ([5, 3, 4], False),
        ([3, 3, 3], False),
        ([0, 5, 7], False),  # 0 + 5 == 5 needs a second 5
        ([0, 0, 0], True),
        ([-1, 2, 1], True),
        ([1], False),
    ],
)
def test_has_two_sum_to_third(arr, expected):
    assert has_two_sum_to_third(arr) is expected
