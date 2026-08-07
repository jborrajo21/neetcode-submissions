class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        prev = 0
        while l <= r:
            i = (l + r) // 2
            if nums[i] < nums[i - 1]:
                return nums[i]
            if nums[i] < nums[prev]:
                r = i - 1
            else:
                l = i + 1
        return nums[0] 