import pytest
from helpers import load

max_visible_people = load("06_stacks.38_maximum_visible_people").max_visible_people


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([6, 2, 5, 4, 5, 1, 6], 6),
        ([1, 3, 6, 4], 4),
        ([2, 1, 2, 1, 2], 3),
        ([1, 2, 3, 4], 4),
        ([4, 3, 2, 1], 4),
        ([3, 3, 3], 1),
        ([5], 1),
        ([], 0),
    ],
)
def test_max_visible_people(heights, expected):
    assert max_visible_people(heights) == expected
