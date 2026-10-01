from helpers.hashing import build_list, to_list


def test_build_list_and_to_list_roundtrip():
    head = build_list([3, 1, 2])
    assert (head.value, head.next.value, head.next.next.value) == (3, 1, 2)
    assert head.next.next.next is None
    assert to_list(head) == [3, 1, 2]


def test_build_list_empty():
    assert build_list([]) is None
    assert to_list(None) == []
