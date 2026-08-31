class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        for i in range(len(coins) + 1):
            dp[amount][i] = 1

        for a in range(amount, -1, -1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i+1]
                if a + coins[i] <= amount:
                    dp[a][i] += dp[a+coins[i]][i]

        return dp[0][0]