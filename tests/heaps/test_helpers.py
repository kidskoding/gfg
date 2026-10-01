from helpers.heaps import build_list, is_max_heap, to_list


def test_build_list_and_to_list_roundtrip():
    head = build_list([1, 2, 3])
    assert (head.value, head.next.value, head.next.next.value) == (1, 2, 3)
    assert head.next.next.next is None
    assert to_list(head) == [1, 2, 3]


def test_build_list_empty():
    assert build_list([]) is None
    assert to_list(None) == []


def test_to_list_stops_on_cycle():
    head = build_list([1, 2])
    head.next.next = head
    assert to_list(head, limit=5) == [1, 2, 1, 2, 1]


def test_is_max_heap():
    assert is_max_heap([])
    assert is_max_heap([1])
    assert is_max_heap([9, 4, 7, 1, 2, 6])
    assert is_max_heap([5, 5, 5])
    assert not is_max_heap([1, 2])
    assert not is_max_heap([9, 4, 7, 5])
