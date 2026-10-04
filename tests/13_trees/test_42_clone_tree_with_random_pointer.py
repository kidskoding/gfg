import pytest
from helpers import load
from helpers.trees import build, to_list

clone_random = load("13_trees.42_clone_tree_with_random_pointer").clone_random


def _nodes(root):
    return [] if root is None else [root] + _nodes(root.left) + _nodes(root.right)


def _make(tree, randoms):
    """Build the tree, then wire node.random from a {value: value} map."""
    root = build(tree)
    by_value = {node.value: node for node in _nodes(root)}
    for src, dst in randoms.items():
        by_value[src].random = by_value[dst]
    return root


@pytest.mark.parametrize(
    "tree, randoms",
    [
        ([1, 2, 3, 4, 5, None, 6], {1: 5, 2: 2, 4: 1, 6: 3}),
        ([1, 2, 3, 4, 5, None, 6], {}),  # no random pointers at all
        ([1, 2, 3, 4, 5, None, 6], {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}),  # every node points to itself
        ([1, 2, 3, 4, 5, None, 6], {1: 6, 6: 1}),  # cycle between root and leaf
        ([1, 2, 3, 4, 5, None, 6], {4: 5, 5: 4, 2: 3, 3: 2}),  # cross-subtree pairs
        ([1, 2, 3, 4, 5, None, 6], {2: 1, 4: 2, 5: 2, 6: 3}),  # random = parent
        ([1, 2, 3, 4, 5, None, 6], {1: 4, 2: 4, 3: 4, 5: 4, 6: 4}),  # many-to-one
        ([1, None, 2, None, 3], {3: 1, 1: 3}),  # chain
        ([1, 2], {1: 2, 2: 1}),
        ([1], {1: 1}),
        ([1], {}),
    ],
)
def test_clone_random(tree, randoms):
    root = _make(tree, randoms)
    clone = clone_random(root)

    assert clone is not root
    assert to_list(clone) == to_list(root)
    originals, copies = _nodes(root), _nodes(clone)
    assert not set(map(id, originals)) & set(map(id, copies))
    mapping = dict(zip(originals, copies))
    for orig, copy in zip(originals, copies):
        assert copy.value == orig.value
        assert copy.random is (mapping[orig.random] if orig.random else None)


def test_clone_random_leaves_original_untouched():
    root = _make([1, 2, 3], {1: 3, 3: 2})
    before = [(n.value, n.random.value if n.random else None) for n in _nodes(root)]
    clone_random(root)
    after = [(n.value, n.random.value if n.random else None) for n in _nodes(root)]
    assert after == before


def test_clone_random_empty():
    assert clone_random(None) is None
