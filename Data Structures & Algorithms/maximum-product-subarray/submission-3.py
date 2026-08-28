class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxN = nums[0]
        minN = nums[0]

        res = maxN

        for i in range(1, n):
            l = [maxN * nums[i], minN * nums[i], nums[i]]
            maxN = max(l)
            minN = min(l)
        
            res = max(res, maxN)
        
        return res

