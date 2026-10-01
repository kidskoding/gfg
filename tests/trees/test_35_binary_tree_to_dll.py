import pytest
from helpers import load
from helpers.trees import build

to_dll = load("trees.35_binary_tree_to_dll").to_dll


def _walk(head):
    """Return (forward values, backward values) and check link symmetry."""
    forward, node = [], head
    assert head.left is None
    while node.right:
        assert node.right.left is node
        forward.append(node.value)
        node = node.right
    forward.append(node.value)
    backward = []
    while node:
        backward.append(node.value)
        node = node.left
    return forward, backward


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([10, 12, 15, 25, 30, 36], [25, 12, 30, 10, 36, 15]),
        ([1, 2, 3], [2, 1, 3]),
        ([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, None, 3], [3, 2, 1]),  # left chain: head is the deepest node
        ([1, None, 2, None, 3], [1, 2, 3]),  # right chain: head is root
        ([5, 3, None, None, 4], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]),
        ([1, 2], [2, 1]),
        ([1, None, 2], [1, 2]),
        ([1], [1]),
    ],
)
def test_to_dll(tree, expected):
    forward, backward = _walk(to_dll(build(tree)))
    assert forward == expected
    assert backward == expected[::-1]


def test_to_dll_reuses_nodes():
    root = build([2, 1, 3])
    left, right = root.left, root.right
    head = to_dll(root)
    assert head is left
    assert head.right is root
    assert head.right.right is right


def test_to_dll_empty():
    assert to_dll(None) is None
