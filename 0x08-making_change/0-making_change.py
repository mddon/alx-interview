#!/usr/bin/python3
"""Script that defines change making module.
"""


def makeChange(coins, total):
    """Determines the least number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    idx = 0
    sorted_coins = sorted(coins, reverse=True)
    coin_numb = len(coins)
    while rem > 0:
        if idx >= coin_numb:
            return -1
        if rem - sorted_coins[idx] >= 0:
            rem -= sorted_coins[idx]
            coins_count += 1
        else:
            idx += 1
    return coins_count
