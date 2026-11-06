
from timeit import timeit

from algorithms import stairs_iter, stairs_memo, stairs_naive


def run_benchmark() -> None:
    numbers = [10, 20, 25]

    print(
        f"{'n':<10}"
        f"{'Naive (s)':<18}"
        f"{'Memo (s)':<18}"
        f"{'Iterative (s)':<18}"
    )

    for n in numbers:
        naive_time = timeit(
            lambda: stairs_naive(n),
            number=1,
        )

        stairs_memo.cache_clear()

        memo_time = timeit(
            lambda: stairs_memo(n),
            number=1,
        )

        iterative_time = timeit(
            lambda: stairs_iter(n),
            number=1,
        )

        print(
            f"{n:<10}"
            f"{naive_time:<18.8f}"
            f"{memo_time:<18.8f}"
            f"{iterative_time:<18.8f}"
        )


if __name__ == "__main__":
    run_benchmark()
