from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class ListNode:
    value: Any
    next: ListNode | None = None

    # for 12_linked_lists problems 30 and 39
    down: ListNode | None = None

    # for 12_linked_lists problem 40
    random: ListNode | None = None
