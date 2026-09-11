class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for num, freq in dp[i].items():
                dp[i+1][num + nums[i]] += freq
                dp[i+1][num - nums[i]] += freq
        
        return dp[n][target]