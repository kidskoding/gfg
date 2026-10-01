import pytest
from helpers import load

peak_element = load("searching.15_peak_element").peak_element


def _is_peak(arr, i):
    left = arr[i - 1] if i > 0 else float("-inf")
    right = arr[i + 1] if i + 1 < len(arr) else float("-inf")
    return arr[i] > left and arr[i] > right


@pytest.mark.parametrize(
    "arr",
    [
        [1, 2, 4, 5, 7, 8, 3],
        [10, 20, 15, 2, 23, 90, 80],  # two peaks: either is fine
        [1, 3, 2, 4, 1],
        [1, 2, 3],  # peak at the end
        [3, 2, 1],  # peak at the start
        [-5, -1, -3],
        [5],
    ],
)
def test_peak_element(arr):
    i = peak_element(arr)
    assert 0 <= i < len(arr)
    assert _is_peak(arr, i)
