import pytest
from helpers import load
from helpers.linked_lists import build_list

is_palindrome = load("linked_lists.21_palindrome_linked_list").is_palindrome


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 1, 1, 2, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 1], False),
        ([1, 1], True),
        ([1, 2], False),
        ([7], True),
        ([], True),
    ],
)
def test_is_palindrome(values, expected):
    assert is_palindrome(build_list(values)) is expected
