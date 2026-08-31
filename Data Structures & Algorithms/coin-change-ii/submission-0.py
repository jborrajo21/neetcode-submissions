class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Backtracking with amount and inex dp
        Find dp
        backtracking arguments: current sum, index of coin array
        Store: unique combinations to get target when current sum is a and when index evaluated is i

        Back track call:
        Possibilities = Include coin at index, continue with i + 1
        Call bt(a + c, i) if a + c <= amount, bt(a, i + 1)
        
        dp[a][i] = dp[a][i+1]
        if a + c <= amount:
            dp[a][i] = dp[a+c][i]
        """

        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        for i in range(len(coins) + 1):
            dp[amount][i] = 1

        for a in range(amount, -1, -1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i+1]
                if a + coins[i] <= amount:
                    dp[a][i] += dp[a+coins[i]][i]

        return dp[0][0]