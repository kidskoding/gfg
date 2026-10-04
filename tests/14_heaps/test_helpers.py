from helpers.heaps import is_max_heap


def test_is_max_heap():
    assert is_max_heap([])
    assert is_max_heap([1])
    assert is_max_heap([9, 4, 7, 1, 2, 6])
    assert is_max_heap([5, 5, 5])
    assert not is_max_heap([1, 2])
    assert not is_max_heap([9, 4, 7, 5])
