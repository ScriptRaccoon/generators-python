"""Generation of prime numbers with a list"""

import sys


def is_prime(p: int) -> bool:
    """checks if an integer is a prime number"""
    return p > 1 and all(p % a for a in range(2, int(p**0.5 + 1)))


def primes(n: int) -> list[int]:
    """computs the list of all primes < n"""
    result = []
    p = 2
    while p < n:
        if is_prime(p):
            result.append(p)
        p += 1
    return result
    # shorter implementation: [p for p in range(n) if is_prime(p)]


def main() -> None:
    """prints all primes below a million with a precomputed list (slow!)"""
    first_primes = primes(1_000_000)
    print(sys.getsizeof(first_primes))  # 632824 bytes
    for p in first_primes:
        print(p)  # takes time before printing!


if __name__ == "__main__":
    main()
