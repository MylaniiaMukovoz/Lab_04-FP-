
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from random import choice
from typing import Generator, Optional


def check_n(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")


def stairs_naive(n: int) -> int:
    check_n(n)

    if n < 0:
        return 0
    if n == 0:
        return 1

    return (
        stairs_naive(n - 1)
        + stairs_naive(n - 2)
        + stairs_naive(n - 3)
    )


@lru_cache(maxsize=None)
def stairs_memo(n: int) -> int:
    check_n(n)

    if n < 0:
        return 0
    if n == 0:
        return 1

    return (
        stairs_memo(n - 1)
        + stairs_memo(n - 2)
        + stairs_memo(n - 3)
    )


def stairs_iter(n: int) -> int:
    check_n(n)

    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b, c = 1, 1, 2

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c


def quicksort(xs: list[int]) -> list[int]:
    if len(xs) <= 1:
        return xs[:]

    pivot = choice(xs)

    left = [x for x in xs if x < pivot]
    middle = [x for x in xs if x == pivot]
    right = [x for x in xs if x > pivot]

    return quicksort(left) + middle + quicksort(right)


@dataclass(slots=True)
class Node:
    key: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def preorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return

    yield t.key
    yield from preorder(t.left)
    yield from preorder(t.right)


def inorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return

    yield from inorder(t.left)
    yield t.key
    yield from inorder(t.right)


def postorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return

    yield from postorder(t.left)
    yield from postorder(t.right)
    yield t.key


def bfs_level_order(t: Optional[Node]) -> list[int]:
    if t is None:
        return []

    queue = deque([t])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.key)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


def dfs_preorder_iter(t: Optional[Node]) -> list[int]:
    if t is None:
        return []

    stack = [t]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.key)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    check_n(n)

    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def fib_iter(n: int) -> int:
    check_n(n)

    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
