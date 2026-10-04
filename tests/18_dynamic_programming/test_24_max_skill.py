import pytest
from helpers import load

max_skill = load("18_dynamic_programming.24_max_skill").max_skill


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3], 1654),
        ([5], 5),
        ([2, 2, 2], 14),
        ([], 0),
    ],
)
def test_max_skill(arr, expected):
    assert max_skill(arr) == expected
