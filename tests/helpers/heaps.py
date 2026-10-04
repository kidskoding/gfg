"""Test-only helpers for heap problems."""


def is_max_heap(arr):
    """True iff the array-form binary heap satisfies the max-heap property."""
    return all(arr[(i - 1) // 2] >= arr[i] for i in range(1, len(arr)))
