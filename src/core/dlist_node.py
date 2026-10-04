from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class DListNode:
    value: Any
    prev: DListNode | None = None
    next: DListNode | None = None
