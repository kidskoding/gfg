from collections import deque

import pytest
from helpers import load
from helpers.trees import build, find

connect_same_level = load("13_trees.33_connect_nodes_same_level").connect_same_level


def _levels(root):
    out, queue = [], deque([root] if root else [])
    while queue:
        row = []
        for _ in range(len(queue)):
            node = queue.popleft()
            row.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        out.append(row)
    return out


def _levels_via_next_right(root):
    """Walk each level using next_right, starting from the leftmost node."""
    out = []
    while root:
        row, node = [], root
        while node:
            row.append(node.value)
            node = node.next_right
        out.append(row)
        root = root.left or root.right
    return out


def test_connect_same_level():
    root = build([10, 20, 30, 40, 60])
    connect_same_level(root)
    assert _levels_via_next_right(root) == [[10], [20, 30], [40, 60]]
    assert root.next_right is None
    assert find(root, 30).next_right is None


def test_connect_same_level_across_subtrees():
    root = build([1, 2, 3, 4, None, None, 5, 6, None, None, 7])
    connect_same_level(root)
    assert find(root, 4).next_right is find(root, 5)
    assert find(root, 6).next_right is find(root, 7)
    assert find(root, 7).next_right is None


def test_connect_same_level_skips_gaps():
    # 4 and 5 sit far apart with missing nodes between them
    root = build([1, 2, 3, 4, None, None, 5])
    connect_same_level(root)
    assert find(root, 4).next_right is find(root, 5)
    assert find(root, 2).next_right is find(root, 3)


@pytest.mark.parametrize(
    "tree",
    [
        [1],
        [1, 2],
        [1, None, 2],
        [1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, None, 2, None, 3, None, 4],  # right chain: every next_right is None
        [1, 2, None, 3, None, 4],  # left chain
        [1, 2, 3, None, 4, 5, None, 6, None, None, 7],
        [1, 2, 3, 4, None, None, 5, 6, None, None, 7],
        [1, 2, 3, None, None, None, 4, 5, None, 6],
    ],
)
def test_connect_same_level_every_level(tree):
    root = build(tree)
    connect_same_level(root)
    for row in _levels(root):
        assert [n.next_right for n in row] == row[1:] + [None]


def test_connect_same_level_empty():
    connect_same_level(None)
