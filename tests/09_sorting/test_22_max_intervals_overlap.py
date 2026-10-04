import pytest
from helpers import load

max_guests = load("09_sorting.22_max_intervals_overlap").max_guests


@pytest.mark.parametrize(
    "entry, exit, expected",
    [
        ([1, 2, 9, 5, 5], [4, 5, 12, 9, 12], (3, 5)),
        ([1, 2, 10, 5, 5], [4, 5, 12, 9, 12], (3, 5)),
        (
            [2, 3, 5, 7, 8],
            [4, 6, 8, 9, 10],
            (3, 8),
        ),  # guests present at their exit time
        ([0, 8], [10, 9], (2, 8)),
        ([1, 1, 1], [5, 5, 5], (3, 1)),
        ([1, 10], [2, 12], (1, 1)),  # tie: earliest time
        ([3], [3], (1, 3)),
    ],
)
def test_max_guests(entry, exit, expected):
    assert tuple(max_guests(entry, exit)) == expected
