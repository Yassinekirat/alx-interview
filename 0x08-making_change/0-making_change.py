#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Compute the minimum
    coins required for each amount from 1 to total
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amt in range(coin, total + 1):
            if dp[amt - coin] != float('inf'):
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
