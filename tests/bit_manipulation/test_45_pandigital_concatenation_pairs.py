import pytest
from helpers import load

count_pandigital_pairs = load(
    "bit_manipulation.45_pandigital_concatenation_pairs"
).count_pandigital_pairs


@pytest.mark.parametrize(
    "nums, expected",
    [
        (["123567", "098234", "14765", "19804"], 3),
        (["01234", "56789", "0123456789"], 3),
        (["0123456789", "5"], 1),
        (["0123456789"] * 3, 3),
        (["12", "34"], 0),
        (["0123456789"], 0),  # needs a pair
        ([], 0),
    ],
)
def test_count_pandigital_pairs(nums, expected):
    assert count_pandigital_pairs(nums) == expected
