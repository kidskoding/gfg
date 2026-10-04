import pytest
from helpers import load

closest_pair_two_arrays = load(
    "04_two_pointers.09_closest_pair_two_sorted"
).closest_pair_two_arrays


@pytest.mark.parametrize(
    "a, b, x, best_gap",
    [
        ([1, 4, 5, 7], [10, 20, 30, 40], 32, 1),
        ([1, 4, 5, 7], [10, 20, 30, 40], 50, 3),
        ([1, 2, 3], [4, 5, 6], 7, 0),  # several exact pairs
        ([-5, 0, 5], [-3, 3], 0, 2),
        ([10, 20], [1, 2], 0, 11),
        ([1], [2], 10, 7),
    ],
)
def test_closest_pair_two_arrays(a, b, x, best_gap):
    p, q = closest_pair_two_arrays(a, b, x)
    assert p in a
    assert q in b
    assert abs(p + q - x) == best_gap
