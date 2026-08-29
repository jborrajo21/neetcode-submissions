class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        target = s // 2

        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j]: break
                dp[j] = dp[j - num]

        return dp[target]
        
