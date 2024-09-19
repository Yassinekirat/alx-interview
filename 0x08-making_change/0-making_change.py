#!/usr/bin/python3
"""Making Change"""
from collections import deque


def makeChange(coins, total):
    """Compute the minimum
    coins required for each amount from 1 to total
    """

    if total <= 0:
        return 0

    queue = deque([(0, 0)])  # (current amount, number of coins)
    visited = set()  # to track visited amounts

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            new_amount = current_amount + coin
            if new_amount == total:
                return num_coins + 1
            if new_amount < total and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    return -1
