from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class TreeNode:
    value: Any
    left: TreeNode | None
    right: TreeNode | None

    # for 13_trees problem 33
    next_right: TreeNode | None

    # for 13_trees problem 42
    random: TreeNode | None
