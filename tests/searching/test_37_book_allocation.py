import pytest
from helpers import load

allocate_books = load("searching.37_book_allocation").allocate_books


@pytest.mark.parametrize(
    "pages, k, expected",
    [
        ([12, 34, 67, 90], 2, 113),
        ([15, 17, 20], 5, -1),  # more students than books
        ([22, 23, 67], 1, 112),
        ([10, 20, 30, 40], 2, 60),
        ([10, 20, 30, 40], 3, 40),
        ([10, 20, 30, 40], 4, 40),
        ([1, 1, 1, 1, 100], 2, 100),
        ([5], 1, 5),
    ],
)
def test_allocate_books(pages, k, expected):
    assert allocate_books(pages, k) == expected
