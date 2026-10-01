from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class ListNode:
    value: Any
    next: ListNode | None = None

    # for problems 30 and 39
    down: ListNode | None = None

    # for problem 40
    random: ListNode | None = None


@dataclass(eq=False)
class DListNode:
    value: Any
    prev: DListNode | None = None
    next: DListNode | None = None
