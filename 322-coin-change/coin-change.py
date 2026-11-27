class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if coin <= x and dp[x - coin] != INF:
                    dp[x] = min(dp[x], 1 + dp[x - coin])

        return -1 if dp[amount] == INF else dp[amount]
        