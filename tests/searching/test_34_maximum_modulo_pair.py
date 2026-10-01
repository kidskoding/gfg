import pytest
from helpers import load

max_modulo_pair = load("searching.34_maximum_modulo_pair").max_modulo_pair


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 4, 7], 3),
        ([6, 11, 15], 5),
        ([2, 7, 9, 10], 3),
        ([3, 8], 2),
        ([5, 10], 0),
        ([1, 2], 0),
        ([4, 4, 4, 4], 0),
    ],
)
def test_max_modulo_pair(arr, expected):
    assert max_modulo_pair(arr) == expected
