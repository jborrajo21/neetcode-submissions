class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [0] * (n+2)
        best_sale = 0

        for i in range(n-1,-1,-1):
            dp[i] = max([best_sale - prices[i], dp[i+1]])
            best_sale = max(best_sale, prices[i] + dp[i+2])
        
        return dp[0]