import pytest
from helpers import load

wave_array = load("01_arrays.09_wave_array").wave_array


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
        ([2, 4, 7, 8, 9, 10], [4, 2, 8, 7, 10, 9]),
        ([1], [1]),
        ([], []),
        ([1, 1, 2, 2], [1, 1, 2, 2]),
        ([-3, -1, 0], [-1, -3, 0]),
    ],
)
def test_wave_array(arr, expected):
    wave_array(arr)
    assert arr == expected


@pytest.mark.parametrize(
    "arr", [[1, 2, 3, 4, 5], [2, 4, 7, 8, 9, 10], [1, 3, 3, 5, 6, 8, 9]]
)
def test_wave_array_is_wave(arr):
    before = sorted(arr)
    wave_array(arr)
    assert sorted(arr) == before
    assert all(
        arr[i] >= arr[i + 1] if i % 2 == 0 else arr[i] <= arr[i + 1]
        for i in range(len(arr) - 1)
    )
