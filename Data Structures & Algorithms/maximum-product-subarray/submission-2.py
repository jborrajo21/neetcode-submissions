class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        maxEnd = [1] * n
        minEnd = [1] * n
        maxEnd[0] = nums[0]
        minEnd[0] = nums[0]

        res = maxEnd[0]

        for i in range(1, n):
            l = [maxEnd[i-1] * nums[i], minEnd[i-1] * nums[i], nums[i]]
            maxEnd[i] = max(l)
            minEnd[i] = min(l)
        
            res = max(res, maxEnd[i])
        
        return res

