#!/usr/bin/python3
"""
    Minimum Operations
    Algorithm
    Python
"""


def minOperations(n):
    """
        calculates number of operations
    """
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
