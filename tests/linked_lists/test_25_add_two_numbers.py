import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

add_numbers = load("linked_lists.25_add_two_numbers").add_numbers


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([4, 5], [3, 4, 5], [3, 9, 0]),
        ([0, 0, 6, 3], [0, 7], [7, 0]),  # leading zeros dropped
        ([9, 9, 9], [1], [1, 0, 0, 0]),  # carry grows the number
        ([9, 9], [9, 9], [1, 9, 8]),
        ([1, 2, 3], [0], [1, 2, 3]),
        ([0], [0], [0]),
        ([0, 0], [0, 0, 0], [0]),
    ],
)
def test_add_numbers(a, b, expected):
    head_a, head_b = build_list(a), build_list(b)
    assert to_list(add_numbers(head_a, head_b)) == expected
    assert to_list(head_a) == a  # inputs untouched
    assert to_list(head_b) == b
