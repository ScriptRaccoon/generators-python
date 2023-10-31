"""Generation of prime numbers with a generator"""

from collections.abc import Iterator
import sys


def is_prime(p: int) -> bool:
    """checks if an integer is a prime number"""
    return p > 1 and all(p % a for a in range(2, int(p**0.5 + 1)))


def primes(n: int) -> Iterator[int]:
    """generator for prime numbers < n"""
    p = 2
    while p < n:
        if is_prime(p):
            yield p
        p += 1
    # shorter implementation: (p for p in range(n) if is_prime(p))


def all_primes() -> Iterator[int]:
    """infinite sequence of all prime numbers"""
    p = 2
    while True:
        if is_prime(p):
            yield p
        p += 1


def main() -> None:
    """prints all primes below a million with a generator function (fast!)"""
    print(sys.getsizeof(primes(1_000_000)))  # 208 bytes
    for p in primes(1_000_000):
        print(p)  # starts printing immediately!


if __name__ == "__main__":
    main()
