"""Performance measurement of listing all permutations as a list"""

from time import perf_counter


def permutations(items: list) -> list[list]:
    """List of all permutations of a list, recursively implemented"""
    n = len(items)
    if n == 0:
        return [[]]
    return [
        [items[i]] + rest
        for i in range(n)
        for rest in permutations(items[:i] + items[i + 1 :])
    ]


def main() -> None:
    """Measures how long it takes to generate all permutations of 10 numbers
    with a precomputed list (much slower!)"""
    start = perf_counter()
    for p in permutations(list(range(10))):
        print(p)  # does not print immediately!
    end = perf_counter()
    print(end - start)  # 21 seconds


if __name__ == "__main__":
    main()
