"""Performance measurement of listing all permutations as a generator"""

from time import perf_counter
from collections.abc import Iterator


def permutations(items: list) -> Iterator[list]:
    """Generator for all permutations of a list, recursively implemented"""
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(n):
            for rest in permutations(items[:i] + items[i + 1 :]):
                yield [items[i]] + rest


def main() -> None:
    """Measures how long it takes to generate the list of all permutations of 10 numbers"""
    start = perf_counter()
    for p in permutations(list(range(10))):
        print(p)  # starts printing immediately!
    end = perf_counter()
    print(end - start)  # 14 seconds


if __name__ == "__main__":
    main()
