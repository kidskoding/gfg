from helpers.trees import build, build_list, find, inorder, to_list


def test_build_and_to_list_roundtrip():
    values = [1, 2, 3, None, 4, None, None, 5]
    root = build(values)
    assert to_list(root) == values
    assert root.left.right.value == 4
    assert root.left.right.left.value == 5


def test_build_empty():
    assert build([]) is None
    assert to_list(None) == []


def test_inorder_and_find():
    root = build([2, 1, 3])
    assert inorder(root) == [1, 2, 3]
    assert find(root, 3) is root.right
    assert find(root, 9) is None


def test_build_list():
    head = build_list([1, 2, 3])
    assert (head.value, head.next.value, head.next.next.value) == (1, 2, 3)
    assert head.next.next.next is None
    assert build_list([]) is None
