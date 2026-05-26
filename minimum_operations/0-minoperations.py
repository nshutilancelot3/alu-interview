#!/usr/bin/python3
"""
Module for computing the minimum number of Copy All / Paste
operations needed to reach exactly n 'H' characters in a file
that starts with a single 'H'.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations to result in exactly
    n 'H' characters using only 'Copy All' and 'Paste' operations.

    The optimal strategy maps to prime factorization: every time we
    copy-then-paste a block of k characters we spend k operations
    (1 Copy All + k-1 Pastes).  Chaining these multiplicative steps
    to reach n is equivalent to summing the prime factors of n.

    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Minimum number of operations, or 0 if n is impossible
             to achieve (n <= 1).
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    # If n is still greater than 1, it is a prime factor itself
    if n > 1:
        operations += n

    return operations
