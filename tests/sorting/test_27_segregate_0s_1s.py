import pytest
from helpers import load

segregate01 = load("sorting.27_segregate_0s_1s").segregate01


@pytest.mark.parametrize(
    "arr",
    [
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 0],
        [1, 0],
        [0, 1],
        [1, 1, 1],
        [],
    ],
)
def test_segregate01(arr):
    expected = sorted(arr)
    assert segregate01(arr) is None
    assert arr == expected
