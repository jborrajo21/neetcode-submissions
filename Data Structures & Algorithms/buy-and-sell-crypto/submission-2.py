class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            while prices[r] - prices[l] < 0 and l < r:
                l += 1
            max_profit = max(max_profit, prices[r] - prices[l])
        
        return max_profit