"""29. Stack with getRandom() in O(1) (GFG, hard)."""


class RandomizedCollection:
    """Multiset with average O(1) insert/remove/get_random; insert returns True if val was absent,
    remove deletes one copy and returns True if val was present, get_random returns each stored copy with
    equal probability (use the `random` module) or None when empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def get_random(self) -> int | None:
        raise NotImplementedError
