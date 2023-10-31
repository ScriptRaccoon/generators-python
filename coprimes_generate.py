"""Prints approximations of pi using a generator function"""

from collections.abc import Iterator
from math import gcd, sqrt


def phi(n: int) -> int:
    """Euler phi function: number of positive integers <= n that are coprime to n"""
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def approximations_pi() -> Iterator[float]:
    """
    Function that approximates pi by using the (amazing) fact that the probability that
    two natural numbers are coprime is pi^2 / 6. The amount a(n) of natural numbers x,y <= n
    that are coprime is computed recursively via a(1) = 1 and a(n) = a(n-1) + 2 * phi(n).
    Then a(n)/n^2 converges to pi^2 / 6, or equivalently, n sqrt(6/a) converges to pi.
    This generator function yields n sqrt(6/a) forever.
    """
    a = 1
    n = 1
    while n < 20:
        yield n * sqrt(6 / a)
        n += 1
        a += 2 * phi(n)


def main() -> None:
    """Prints approximations of pi"""
    for x in approximations_pi():
        print(x)


if __name__ == "__main__":
    main()
