
import pytest

from algorithms import fib, fib_iter


def test_fib_small():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    assert [fib(i) for i in range(10)] == expected


def test_fib_iter_matches():
    for n in range(50):
        assert fib(n) == fib_iter(n)


def test_fib_zero():
    assert fib(0) == 0
    assert fib_iter(0) == 0


def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-1)

    with pytest.raises(ValueError):
        fib_iter(-1)


def test_fib_cache_clear():
    fib.cache_clear()
    fib(10)

    assert fib.cache_info().currsize > 0

    fib.cache_clear()

    assert fib.cache_info().currsize == 0
