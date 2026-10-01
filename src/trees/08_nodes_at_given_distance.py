"""08. Nodes at Given Distance (GFG, easy)."""
from collections import deque

from trees import TreeNode


def k_distance(root: TreeNode | None, target: int, k: int) -> list[int]:
    parent = {}

    def findParent(node: TreeNode | None, parent: TreeNode | None):
        if not node:
            return

        parent[node] = parent
        findParent(node.left, node)
        findParent(node.right, node)

    findParent(root, None)

    queue = deque([target])
    visited = set([target])
    curr_dist = 0

    while queue:
        if curr_dist == k:
            return [node.val for node in queue]

        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)

            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)

            if node in parent and parent[node] and parent[node] not in visited:
                visited.add(parent[node])
                queue.append(parent[node])

        curr_dist += 1

    return []
