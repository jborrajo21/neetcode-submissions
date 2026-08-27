class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cs = [0]
        for c in coins:
            if c <= amount:
                cs.append(c)

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            dp[a] = min(dp[a], min(dp[a-c] for c in cs) + 1)

        res = dp[amount] 

        return res if res < float("inf") else -1