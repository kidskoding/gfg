import pytest
from helpers import load

LinkedStack = load("linked_lists.11_stack_using_linked_list").LinkedStack


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("push", 11),
                ("push", 22),
                ("push", 33),
                ("peek",),
                ("pop",),
                ("pop",),
                ("peek",),
            ],
            [None, None, None, 33, 33, 22, 11],
        ),
        (
            [("push", 2), ("push", 3), ("pop",), ("push", 4), ("pop",), ("len",)],
            [None, None, 3, None, 4, 1],
        ),
        (
            [
                ("empty",),
                ("len",),
                ("push", 1),
                ("empty",),
                ("len",),
                ("pop",),
                ("empty",),
            ],
            [True, 0, None, False, 1, 1, True],
        ),
        (
            [("push", 5), ("push", 5), ("pop",), ("peek",), ("len",)],
            [None, None, 5, 5, 1],
        ),
    ],
)
def test_linked_stack(ops, expected):
    stack = LinkedStack()
    calls = {
        "push": stack.push,
        "pop": stack.pop,
        "peek": stack.peek,
        "empty": stack.is_empty,
        "len": lambda: len(stack),
    }
    assert [calls[name](*args) for name, *args in ops] == expected


@pytest.mark.parametrize("method", ["pop", "peek"])
def test_linked_stack_empty_raises(method):
    stack = LinkedStack()
    with pytest.raises(IndexError):
        getattr(stack, method)()


def test_linked_stack_many():
    stack = LinkedStack()
    for i in range(1000):
        stack.push(i)
    assert [stack.pop() for _ in range(1000)] == list(range(999, -1, -1))
    assert stack.is_empty()
