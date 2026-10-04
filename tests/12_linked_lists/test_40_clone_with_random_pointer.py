import pytest
from helpers import load
from helpers.linked_lists import build_list, nodes

clone_random = load("12_linked_lists.40_clone_with_random_pointer").clone_random


def _build(values, randoms):
    head = build_list(values)
    all_nodes = nodes(head)
    for node, r in zip(all_nodes, randoms):
        node.random = None if r is None else all_nodes[r]
    return head


def _snapshot(head):
    """(values, random indices) describing a list; also identifies each node."""
    all_nodes = nodes(head)
    index = {id(node): i for i, node in enumerate(all_nodes)}
    for node in all_nodes:
        assert node.random is None or id(node.random) in index, (
            "random points outside the list"
        )
    randoms = [
        None if node.random is None else index[id(node.random)] for node in all_nodes
    ]
    return [node.value for node in all_nodes], randoms


@pytest.mark.parametrize(
    "values, randoms",
    [
        ([1, 2, 3, 4, 5], [2, 0, 4, 1, 3]),
        ([1, 3, 5, 9], [None, 0, None, 2]),
        ([7, 7, 7], [2, 2, 0]),  # equal values must not be confused
        ([1, 2, 3], [0, 1, 2]),  # every node points to itself
        ([1, 2], [None, None]),
        ([4], [0]),
        ([4], [None]),
    ],
)
def test_clone_random(values, randoms):
    head = _build(values, randoms)
    original_nodes = {id(node) for node in nodes(head)}
    copy = clone_random(head)
    assert _snapshot(copy) == (values, randoms)
    assert original_nodes.isdisjoint(id(node) for node in nodes(copy))
    assert _snapshot(head) == (values, randoms)  # original intact


def test_clone_random_empty():
    assert clone_random(None) is None
