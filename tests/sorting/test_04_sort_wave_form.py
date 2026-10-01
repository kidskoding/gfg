import pytest
from helpers import load

sort_wave = load("sorting.04_sort_wave_form").sort_wave


def _is_wave(arr):
    return all(
        arr[i] >= arr[i + 1] if i % 2 == 0 else arr[i] <= arr[i + 1]
        for i in range(len(arr) - 1)
    )


@pytest.mark.parametrize(
    "arr",
    [
        [10, 5, 6, 3, 2, 20, 100, 80],
        [20, 10, 8, 6, 4, 2],
        [2, 4, 7, 8, 9, 10],
        [1, 1, 5, 5, 5],
        [3, 3, 3, 3],
        [1, 2],
        [1],
        [],
    ],
)
def test_sort_wave(arr):
    original = sorted(arr)
    sort_wave(arr)
    assert sorted(arr) == original
    assert _is_wave(arr)
