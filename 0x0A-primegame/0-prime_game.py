#!/usr/bin/python3


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    # Step 1: Find the maximum value of n
    max_n = max(nums)

    # Step 2: Generate a prime sieve up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Step 3: Precompute the number of primes up to each number n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Step 4: Simulate the game for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # The number of prime
        # numbers up to n will determine the number of moves.
        primes_in_n = prime_counts[n]

        # Maria starts first,
        # so if there are an odd number of primes, Maria wins
        # Otherwise, Ben wins.
        if primes_in_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
