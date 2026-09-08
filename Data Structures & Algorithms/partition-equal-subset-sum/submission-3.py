class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for a in range(target, -1, -1):
                if n <= a:
                    dp[a] = dp[a] or dp[a - n]

        return dp[target]