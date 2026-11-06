
import pytest

from algorithms import stairs_iter, stairs_memo, stairs_naive


def test_stairs_basic():
    expected = [1, 1, 2, 4, 7, 13, 24]

    for n in range(7):
        assert stairs_naive(n) == expected[n]
        assert stairs_memo(n) == expected[n]
        assert stairs_iter(n) == expected[n]


def test_stairs_zero():
    assert stairs_naive(0) == 1
    assert stairs_memo(0) == 1
    assert stairs_iter(0) == 1


def test_stairs_negative():
    assert stairs_naive(-1) == 0
    assert stairs_memo(-1) == 0
    assert stairs_iter(-1) == 0


def test_stairs_iter_matches_memo():
    for n in range(50):
        assert stairs_iter(n) == stairs_memo(n)


def test_stairs_naive_matches_memo():
    for n in range(15):
        assert stairs_naive(n) == stairs_memo(n)


def test_cache_clear():
    stairs_memo.cache_clear()
    stairs_memo(10)

    assert stairs_memo.cache_info().currsize > 0

    stairs_memo.cache_clear()

    assert stairs_memo.cache_info().currsize == 0


def test_invalid_input():
    with pytest.raises(TypeError):
        stairs_naive(2.5)

    with pytest.raises(TypeError):
        stairs_memo("5")

    with pytest.raises(TypeError):
        stairs_iter(True)
