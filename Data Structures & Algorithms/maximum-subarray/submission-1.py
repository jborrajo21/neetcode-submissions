class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = float("-inf")
        for n in nums:
            s += n
            res = max(s, res)
            if s < 0:
                s = 0
        
        return res