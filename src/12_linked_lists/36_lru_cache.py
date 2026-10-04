"""36. LRU Cache (GFG, hard)."""


class LRUCache:
    """Fixed-capacity cache (capacity >= 1); get and put are O(1). get returns None for a
    missing key; both get and put mark the key most recently used. put on a full cache
    evicts the least recently used key first."""

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: object) -> object | None:
        raise NotImplementedError

    def put(self, key: object, value: object) -> None:
        raise NotImplementedError
