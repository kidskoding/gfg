import pytest
from helpers import load
from helpers.linked_lists import build_list, to_list

mod = load("03_hashing.02_union_intersection_linked_lists")
union_lists = mod.union_lists
intersection_lists = mod.intersection_lists

CASES = [
    # list1, list2, union, intersection
    ([10, 15, 4, 20], [8, 4, 2, 10], [2, 4, 8, 10, 15, 20], [4, 10]),
    ([9, 6, 4, 2, 3, 8], [1, 2, 8, 6, 2], [1, 2, 3, 4, 6, 8, 9], [2, 6, 8]),
    ([1, 1, 2, 2], [2, 2, 3], [1, 2, 3], [2]),  # duplicates collapse
    ([1, 2], [3, 4], [1, 2, 3, 4], []),  # nothing shared
    ([], [5, 3], [3, 5], []),
    ([], [], [], []),
    ([-3, 0, 7], [7, -3], [-3, 0, 7], [-3, 7]),
]


@pytest.mark.parametrize("a, b, expected, _", CASES)
def test_union_lists(a, b, expected, _):
    head1, head2 = build_list(a), build_list(b)
    assert to_list(union_lists(head1, head2)) == expected
    assert to_list(head1) == a and to_list(head2) == b  # inputs unchanged


@pytest.mark.parametrize("a, b, _, expected", CASES)
def test_intersection_lists(a, b, _, expected):
    head1, head2 = build_list(a), build_list(b)
    assert to_list(intersection_lists(head1, head2)) == expected
    assert to_list(head1) == a and to_list(head2) == b
