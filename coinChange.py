# encoding: utf-8

"""
date: 2020/03/16/18/15

"""


class Solution:
    def coinChange(self, coins, amount):
        if not amount: return 0
        min_coins = [0] + [float('inf')] * amount
        for c in coins:
            for i in range(c, amount + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

        return min_coins[-1] if min_coins[-1] != float('inf') else -1


S = Solution()

print(S.coinChange([1,2,4],10))