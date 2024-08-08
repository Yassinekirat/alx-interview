#!/usr/bin/python3
""" Script that computes the minimum operations needed for a CopyAll - Paste task."""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste
    """
    if n < 2:
        return 0
    list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                list.append(i)
    return sum(list)
