import pytest
from helpers import load

from_matrix = load("12_linked_lists.30_linked_list_from_matrix").from_matrix


def _grid(head, rows, cols):
    """Walk via down then next; return node grid. Fails on a wrong shape."""
    grid, row_head = [], head
    for _ in range(rows):
        assert row_head is not None
        row, node = [], row_head
        for _ in range(cols):
            assert node is not None
            row.append(node)
            node = node.next
        assert node is None, "row too long"
        grid.append(row)
        row_head = row_head.down
    assert row_head is None, "too many rows"
    return grid


@pytest.mark.parametrize(
    "matrix",
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2], [3, 4]],
        [[1, 2, 3, 4], [5, 6, 7, 8]],
        [[1, 2, 3]],
        [[1], [2], [3]],
        [[5, 5], [5, 5]],
        [[1]],
    ],
)
def test_from_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    grid = _grid(from_matrix(matrix), rows, cols)
    for i in range(rows):
        for j in range(cols):
            node = grid[i][j]
            assert node.value == matrix[i][j]
            assert node.next is (grid[i][j + 1] if j + 1 < cols else None)
            assert node.down is (grid[i + 1][j] if i + 1 < rows else None)


@pytest.mark.parametrize("matrix", [[], [[]]])
def test_from_matrix_empty(matrix):
    assert from_matrix(matrix) is None
