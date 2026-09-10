class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for n, freq in dp[i].items():
                dp[i+1][n + nums[i]] += freq
                dp[i+1][n - nums[i]] += freq
        
        return dp[-1][target]