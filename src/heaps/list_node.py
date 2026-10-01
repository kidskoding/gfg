from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class ListNode:
    value: Any
    next: ListNode | None = None
