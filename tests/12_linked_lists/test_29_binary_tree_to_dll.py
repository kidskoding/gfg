import pytest
from helpers import load
from helpers.trees import build

tree_to_dll = load("12_linked_lists.29_binary_tree_to_dll").tree_to_dll


def _walk(head, limit=10_000):
    """Return forward values; check head.left is None and left/right links agree."""
    assert head.left is None
    forward, node = [], head
    while node is not None:
        assert len(forward) < limit, "list too long"
        forward.append(node.value)
        if node.right is not None:
            assert node.right.left is node
        node = node.right
    return forward


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([10, 12, 15, 25, 30, 36], [25, 12, 30, 10, 36, 15]),
        ([1, 3, 2], [3, 1, 2]),
        ([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, None, 3], [3, 2, 1]),  # left chain
        ([1, None, 2, None, 3], [1, 2, 3]),  # right chain
        ([5, 3, None, None, 4], [3, 4, 5]),
        ([1], [1]),
    ],
)
def test_tree_to_dll(tree, expected):
    assert _walk(tree_to_dll(build(tree))) == expected


def test_tree_to_dll_reuses_nodes():
    root = build([2, 1, 3])
    left, right = root.left, root.right
    head = tree_to_dll(root)
    assert head is left
    assert head.right is root
    assert root.right is right
    assert right.right is None


def test_tree_to_dll_empty():
    assert tree_to_dll(None) is None
